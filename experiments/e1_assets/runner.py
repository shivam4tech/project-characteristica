"""E1 runner — four arms per FROZEN pre-reg §3. Modes: smoke|primary|h2|repl|f3.

Metering per MEASUREMENT_PLAN §1 (F/V/R splits; converter K separate); provider
usage fields authoritative. Incremental writes after every BATCH_FLUSH outcomes.
Zero post-hoc filtering: every attempt logged verbatim under raw_outputs/.
NO EDITS after first scored call (pre-reg §8.5).
"""
import argparse, csv, json, sys, threading, time, random, re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO = Path("/home/shivam/philosophy/project-characteristica")
EXP = REPO / "experiments"
sys.path.insert(0, str(EXP / "harness"))
import config as CFG          # frozen pins
import fblocks as FB          # frozen F-blocks
import checkers as CH         # frozen parsers/checkers

RESULTS = CFG.RESULTS
RAW = RESULTS / "raw_outputs"
F_EXEC_BLOCK = FB.F_EXEC

# Frozen F3 decode prompt (authored pre-first-scored-call; hashed via runner.py copy)
P_F3DEC = ("You convert a CSIR/0 document back into fluent natural language that preserves EVERY "
           "node, edge label, attribute value, unknown-flag, branch and exclusion - complete, "
           "nothing omitted, nothing added. Output only the paragraph.")

_TIER_A = {"entity_ref","predicate","quantity_unit","temporal_qualifier","constraint","scope_marker",
           "modality","negation","preference_order","output_shape","speech_act","style_constraint","exclusion"}
_RELS = {"hasArg","modifies","constrains","orderedBefore","excludes","quantifiesOver","requestsOutput"}

_key_lock = threading.Lock()
_key_cache = None

def api_key():
    global _key_cache
    with _key_lock:
        if _key_cache is None:
            auth = json.load(open(Path.home() / ".hermes" / "auth.json"))
            entries = auth["credential_pool"]["openrouter"]
            _key_cache = next(e["access_token"] for e in entries if e.get("access_token"))
        return _key_cache

def call(block_name, user_payload, temperature):
    """One API request. Returns dict with content, usage, latency, transport status."""
    import urllib.request
    body = json.dumps({"model": CFG.MODEL_ID,
                       "messages": [{"role": "user", "content": user_payload}],
                       "temperature": temperature, "max_tokens": CFG.MAX_TOKENS}).encode()
    last = None
    for t in range(3):                       # transport retries only; NOT protocol R
        t0 = time.time()
        try:
            req = urllib.request.Request(
                CFG.API_BASE + "/chat/completions", data=body,
                headers={"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=180))
            u = r.get("usage", {})
            return {"ok": True, "content": r["choices"][0]["message"]["content"] or "",
                    "p_in": u.get("prompt_tokens", 0), "p_out": u.get("completion_tokens", 0),
                    "latency_ms": int((time.time() - t0) * 1000),
                    "resp_id": r.get("id", ""), "transport_retries": t}
        except Exception as e:
            last = e
            time.sleep([2, 5, 10][t])
    return {"ok": False, "content": "", "p_in": 0, "p_out": 0, "latency_ms": int((time.time()-t0)*1000),
            "error": repr(last)[:300], "transport_retries": 3}

_enc = None
def tok(s):
    global _enc
    if _enc is None:
        import tiktoken; _enc = tiktoken.get_encoding("o200k_base")
    return len(_enc.encode(s))

def validate_csir(doc):
    """Frozen csir0 §3 gate: schema conformance, referential integrity, span coverage."""
    e = []
    if not isinstance(doc, dict): return ["doc:not-an-object"]
    if doc.get("csir_version") != "0.1.0": e.append("csir_version")
    if not isinstance(doc.get("speech_act"), dict): e.append("speech_act")
    lex = {}
    for l in doc.get("lexicon", []) or []:
        if isinstance(l, dict) and l.get("id"): lex[l["id"]] = l
    ids, nodes = set(), []
    for n in doc.get("nodes", []) or []:
        if not isinstance(n, dict): e.append("node:not-object"); continue
        nid = n.get("id"); ids.add(nid)
        if n.get("kind") not in _TIER_A: e.append(f"{nid}:kind:{n.get('kind')}")
        sp = n.get("spans")
        if not (isinstance(sp, list) and sp and all(isinstance(x, list) and len(x) == 2
                and all(isinstance(v, int) for v in x) for x in sp)):
            e.append(f"{nid}:spans")
        if n.get("kind") == "entity_ref" and n.get("ref") not in lex:
            e.append(f"{nid}:ref-missing:{n.get('ref')}")
        nodes.append(n)
    edges = []
    for ed in doc.get("edges", []) or []:
        if not isinstance(ed, dict): continue
        if ed.get("rel") not in _RELS: e.append(f"edge:rel:{ed.get('rel')}")
        if ed.get("from") not in ids or ed.get("to") not in ids: e.append("edge:dangling")
        edges.append((ed.get("from"), ed.get("to")))
    # acyclicity + depth<=3 over hasArg/modifies/constrains/orderedBefore/excludes/quantifiesOver
    adj = {}
    for a, b in edges: adj.setdefault(a, []).append(b)
    color = {}
    def dfs(u, depth=0):
        color[u] = 1; md = depth
        for v in adj.get(u, []):
            if color.get(v) == 1: raise ValueError("cycle")
            if color.get(v) is None: md = max(md, dfs(v, depth + 1))
        color[u] = 2
        return md
    maxd = 0
    try:
        for n in nodes:
            if color.get(n["id"]) is None: maxd = max(maxd, dfs(n["id"]))
    except ValueError:
        e.append("graph:cycle")
    if maxd > 3: e.append(f"depth:{maxd}")
    return e

def extract_json(raw):
    m = re.search(r"\{.*\}", raw, re.S)
    if not m: raise ValueError("no JSON object found")
    return json.loads(m.group(0))

def run_arm(arm, item, temperature, rep=None):
    """Execute one item on one arm. Returns outcome dict (all attempts retained)."""
    fam, src, q = item["family"], item["source_text"], item["question"]
    vin_txt = f"SOURCE:\n{src}\n\nREQUEST:\n{q}"
    attempts = []                            # every API attempt, verbatim-loggable
    def rec(stage, idx, blockname, resp, note=""):
        attempts.append({"stage": stage, "idx": idx, "block": blockname, **resp,
                         "note": note, "f_tok": tok(FB.FBLOCKS.get(blockname, ""))})
    # ---------------- single-stage arms ----------------
    if arm in ("NL-plain", "NL-opt", "JSON"):
        blk = {"NL-plain": "NL-plain", "NL-opt": "NL-opt", "JSON": "JSON"}[arm]
        base_prompt = FB.FBLOCKS[blk] + "\n\n" + vin_txt
        r = call(blk, base_prompt, temperature)
        rec("execute", 1, blk, r)
        art = perr = None
        for att in range(1, CFG.REPAIR_LIMIT + 2):
            if r["ok"] and perr is None:
                try:
                    art = CH.parse_answer(item, arm, r["content"]); break
                except Exception as ex:
                    perr = f"parse: {ex}"[:200]
            if att > CFG.REPAIR_LIMIT: break
            fix = ("Your previous reply was invalid: %s Re-output ONLY the corrected answer "
                   "artifact, nothing else." % (perr or "empty response"))
            r = call(blk, base_prompt + "\n\n" + fix +
                     "\n\nYour previous reply:\n" + (attempts[-1]["content"][:1500]), temperature)
            rec("execute-repair", att + 1, blk, r, note=perr or "")
            perr = None
            try:
                art = CH.parse_answer(item, arm, r["content"]); perr = None
            except Exception as ex:
                perr = f"parse: {ex}"[:200]
        return finish(arm, item, rep, temperature, attempts, art, perr)
    # ---------------- CSIR-SIR two-stage arm ----------------
    conv_in = (FB.F_CONV + "\n\nSOURCE INTENT:\n" + src +
               "\n\nREQUIRED OUTPUT ARTIFACT (task question):\n" + q +
               "\n\nConvert this intent to its CSIR/0 JSON document now.")
    doc = None; derrs = None; cand = None
    cidx = 0
    while True:
        cidx += 1
        if cidx == 1:
            payload = conv_in
        else:
            payload = (conv_in + "\n\nYour previous document FAILED VALIDATION:\n- "
                       + "\n- ".join(derrs) + "\nRe-emit the FULL corrected CSIR/0 JSON document only.")
        r = call("CSIR-SIR::conv", payload, temperature)
        rec("convert", cidx, "CSIR-SIR::conv", r, note=";".join(derrs or []))
        if not r["ok"]:
            break
        try:
            cand = extract_json(r["content"])
            derrs = validate_csir(cand)
        except Exception as ex:
            derrs = [f"json:{ex}"[:160]]
        if not derrs or cidx > CFG.REPAIR_LIMIT:
            break
    # repairs exhausted -> proceed with validator-reported state (never silently repaired)
    return sir_finish(arm, item, rep, temperature, attempts, cand, derrs or [], q)

def sir_finish(arm, item, rep, temperature, attempts, cand_doc, cerrs, q):
    exec_in = "CSIR/0 DOCUMENT:\n" + (json.dumps(cand_doc, indent=1) if cand_doc else "{}")
    if cerrs:
        exec_in += ("\n\nVALIDATOR REPORT (these parts failed; work only with what validated, "
                    "mark gaps UNKNOWN, never fabricate):\n- " + "\n- ".join(cerrs))
    exec_in += "\n\nTASK QUESTION:\n" + q
    perr = None; art = None
    for att in range(1, CFG.REPAIR_LIMIT + 2):
        r = call("CSIR-SIR::exec", F_EXEC_BLOCK + "\n\n" + exec_in +
                 ("" if att == 1 else "\n\nYour previous reply was invalid: " + (perr or "") +
                  " Re-output ONLY the corrected answer artifact."),
                 temperature)
        attempts.append({"stage": "execute" if att == 1 else "execute-repair", "idx": att,
                         "block": "CSIR-SIR::exec", **r, "note": perr or "",
                         "f_tok": tok(F_EXEC_BLOCK)})
        if not r["ok"]: break
        try:
            art = CH.parse_answer(item, arm, r["content"]); perr = None; break
        except Exception as ex:
            perr = f"parse: {ex}"[:200]
    out = finish(arm, item, rep, temperature, attempts, art, perr)
    out["conv_errors"] = ";".join(cerrs)[:400]
    out["kerr_flag"] = bool(cerrs)
    out["doc_valid"] = bool(cand_doc) and not cerrs
    return out

def finish(arm, item, rep, temperature, attempts, art, perr):
    fam = item["family"]
    score, det, gate = 0.0, {}, False
    f0 = art is not None
    if f0:
        try:
            score, det = CH.score_item(item, arm, art)
            gate = (det.get("hard_violations", 1) == 0) if fam == "CP" else (score == 1.0)
        except Exception as ex:
            f0, det = False, {"checker_exception": repr(ex)[:200]}
    o = {"arm": arm, "family": fam, "template": item["template"], "item_id": item["id"],
         "rep": rep if rep is not None else "", "temperature": temperature,
         "n_attempts": len(attempts),
         "lat_total_ms": sum(a["latency_ms"] for a in attempts if a["stage"].startswith("execute")),
         "conv_lat_ms": sum(a["latency_ms"] for a in attempts if a["stage"].startswith("convert")),
         "score": round(score, 4), "gate_pass": gate, "f0_ok": f0,
         "detail": json.dumps(det)[:500], "final_error": (perr or "")[:200],
         "transport_fail": any(not a["ok"] for a in attempts)}
    # token components (§1): first execute attempt -> V/F; later attempts -> R; convert -> K
    ex_first = next((a for a in attempts if a["stage"] == "execute"), None)
    o["v_in"] = max(0, (ex_first["p_in"] - ex_first["f_tok"])) if ex_first and ex_first["ok"] else 0
    o["v_out"] = ex_first["p_out"] if ex_first and ex_first["ok"] else 0
    o["f_tok"] = ex_first["f_tok"] if ex_first else 0
    o["r_in"] = sum(a["p_in"] for a in attempts
                    if a["stage"].startswith("execute-repair") and a["ok"])
    o["r_out"] = sum(a["p_out"] for a in attempts
                     if a["stage"].startswith("execute-repair") and a["ok"])
    convs = [a for a in attempts if a["stage"].startswith("convert")]
    o["k_in"] = sum(a["p_in"] for a in convs if a["idx"] == 1)
    o["k_out"] = sum(a["p_out"] for a in convs if a["idx"] == 1)
    o["k_rin"] = sum(a["p_in"] for a in convs if a["idx"] > 1)
    o["k_rout"] = sum(a["p_out"] for a in convs if a["idx"] > 1)
    o["n_conv_attempts"] = len(convs)
    o["f_conv_tok"] = convs[0]["f_tok"] if convs else 0
    o["f_exec_tok"] = next((a["f_tok"] for a in attempts if a["stage"] == "execute"), 0)
    o["conv_errors"] = ""
    o["kerr_flag"] = False
    o["doc_valid"] = True
    # verbatim raw retention
    d = RAW / arm.replace("/", "_") / fam
    d.mkdir(parents=True, exist_ok=True)
    fn = d / (item["id"] + ("" if rep is None else f"_r{rep}") + ".json")
    fn.write_text(json.dumps({"outcome": o, "attempts": [
        {k: v for k, v in a.items()} for a in attempts], "artifact_keys":
        sorted(art.keys()) if isinstance(art, dict) else None}, indent=1))
    o["raw_path"] = str(fn.relative_to(REPO))
    o["csir_doc_path"] = ""
    if arm == "CSIR-SIR" and isinstance(art, dict):
        pass
    return o

def load_banks():
    bdir = EXP / "harness" / "items" / "banks"
    return {f: json.load(open(bdir / f"{f.lower()}_bank.json")) for f in CFG.FAMILIES}

def append_csv(path, rows, fields):
    new = not Path(path).exists()
    with open(path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore", restval="")
        if new: w.writeheader()
        w.writerows(rows)
        fh.flush()

OUT_FIELDS = ["ts","arm","family","template","item_id","rep","temperature","n_attempts",
              "n_conv_attempts","lat_total_ms","conv_lat_ms","score","gate_pass","f0_ok",
              "v_in","v_out","f_tok","r_in","r_out","k_in","k_out","k_rin","k_rout",
              "f_conv_tok","f_exec_tok","doc_valid","kerr_flag","conv_errors","detail",
              "final_error","transport_fail","raw_path"]

def run_batch(mode, jobs, tag):
    """jobs: list of dicts {arm,item,rep,temp}. Executes concurrently, flushes every 10."""
    out_csv = RESULTS / {"primary": "outcomes.csv", "h2": "h2_outcomes.csv",
                         "repl": "repl_outcomes.csv", "smoke": "smoke_outcomes.csv"}[mode]
    buf, done, lock = [], 0, threading.Lock()
    t_start = time.time()
    def work(j):
        time.sleep(random.uniform(0, 0.3))
        return run_arm(j["arm"], j["item"], j["temp"], j["rep"])
    with ThreadPoolExecutor(max_workers=CFG.MAX_WORKERS) as px:
        futs = {px.submit(work, j): j for j in jobs}
        for fu in as_completed(futs):
            try:
                o = fu.result()
            except Exception as ex:
                o = {"arm": futs[fu]["arm"], "family": futs[fu]["item"]["family"],
                     "template": futs[fu]["item"]["template"], "item_id": futs[fu]["item"]["id"],
                     "rep": futs[fu]["rep"] or "", "transport_fail": True,
                     "final_error": repr(ex)[:250], "score": 0.0, "gate_pass": False, "f0_ok": False}
            o.setdefault("ts", ""); o["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            with lock:
                buf.append(o); done += 1
                if len(buf) >= CFG.BATCH_FLUSH:
                    append_csv(out_csv, buf, OUT_FIELDS); buf = []
                    print(f"[{tag}] {done}/{len(jobs)} flushed ({time.time()-t_start:.0f}s)", flush=True)
    if buf: append_csv(out_csv, buf, OUT_FIELDS)
    print(f"[{tag}] DONE {done} outcomes -> {out_csv.name}", flush=True)

def jobs_primary(banks):
    js = []
    for fam in CFG.FAMILIES:
        for arm in CFG.ARMS:
            for it in banks[fam]:
                js.append({"arm": arm, "item": it, "rep": None, "temp": 0.0})
    return js

def jobs_h2(banks):
    js = []
    cp = banks["CP"]
    sel = [it for it in cp if it["idx"] in (0, 2, 4, 6)]      # 5 templates x 4 = 20 stratified
    assert len(sel) == 20, len(sel)
    for rep, seed in enumerate(CFG.H2_SEEDS):
        for it in sel:
            for arm in ("NL-opt", "JSON", "CSIR-SIR"):
                js.append({"arm": arm, "item": it, "rep": rep, "temp": 0.7})
    return js

def strat10(bank):
    by = {}
    for it in bank: by.setdefault(it["template"], []).append(it)
    out = []
    for t in sorted(by): out += by[t][:2]
    return out                                              # 2/template = 10 stratified

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["smoke", "primary", "h2"])
    banks = load_banks()
    a = ap.parse_args()
    if a.mode == "smoke":
        jobs = [{"arm": ar, "item": it, "rep": None, "temp": 0.0}
                for ar in ("NL-plain", "NL-opt", "JSON") for it in
                (banks["EX"][0], banks["TU"][0])]
        jobs.append({"arm": "CSIR-SIR", "item": banks["EX"][0], "rep": None, "temp": 0.0})
        run_batch("smoke", jobs, "SMOKE")
    elif a.mode == "primary":
        run_batch("primary", jobs_primary(banks), "PRIMARY")
    elif a.mode == "h2":
        run_batch("h2", jobs_h2(banks), "H2")

if __name__ == "__main__":
    main()
