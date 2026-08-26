"""E1 runner — four arms per FROZEN pre-reg §3. Modes: smoke|primary|h2|repl|f3.

Metering per MEASUREMENT_PLAN §1 (F/V/R splits; converter K separate); provider
usage fields authoritative. Incremental writes after every BATCH_FLUSH outcomes.
Zero post-hoc filtering: every attempt logged verbatim under raw_outputs/.
NO EDITS after first scored call (pre-reg §8.5).
"""
import argparse, csv, json, sys, threading, time, random, re
from collections import defaultdict
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

# ---- DEV-8 (pre-first-scored-call): client-side pacing for :free tier -------
_rl_lock = threading.Lock()
_next_ok = [0.0]

def _pace():
    """Space request starts >= CFG.RATE_MIN_INTERVAL_S apart (all arms equally)."""
    with _rl_lock:
        now = time.time()
        wait = _next_ok[0] - now
        if wait > 0:
            time.sleep(wait)
        _next_ok[0] = max(now, _next_ok[0]) + CFG.RATE_MIN_INTERVAL_S

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
    import urllib.request, urllib.error
    body = json.dumps({"model": CFG.MODEL_ID,
                       "messages": [{"role": "user", "content": user_payload}],
                       "temperature": temperature, "max_tokens": CFG.MAX_TOKENS}).encode()
    last = None
    # transport retries only; NOT protocol R. HTTP 429 (:free upstream capacity /
    # free-tier quota) gets its own longer-backoff budget (DEV-8, pre-scored-call).
    tries = 3 + CFG.RETRY_429_MAX
    t = 0
    while t < tries:
        _pace()
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
        except urllib.error.HTTPError as e:
            if e.code == 429 and t < CFG.RETRY_429_MAX:
                e.read()
                last = e
                time.sleep(20)
                t += 1
                continue
            last = e
            time.sleep([2, 5, 10][min(t, 2)])
            t += 1
        except Exception as e:
            last = e
            time.sleep([2, 5, 10][min(t, 2)])
            t += 1
    return {"ok": False, "content": "", "p_in": 0, "p_out": 0, "latency_ms": int((time.time()-t0)*1000),
            "error": repr(last)[:300], "transport_retries": t}

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
              "final_error","transport_fail","raw_path","rerun"]

def run_batch(mode, jobs, tag):
    """jobs: list of dicts {arm,item,rep,temp}. Executes concurrently, flushes every 10."""
    out_csv = RESULTS / {"primary": "outcomes.csv", "h2": "h2_outcomes.csv",
                         "repl": "repl_outcomes.csv", "smoke": "smoke_outcomes.csv"}[mode]
    # ---- DEV-8 checkpoint-resume (pre-first-scored-call): a job whose (arm,item,
    # rep) already has a latest non-transport-fail reading in this mode's CSV is
    # skipped on restart; external-abort/cap-out resumes from the last state.
    if mode != "smoke" and Path(out_csv).exists():
        done = set()
        for r in csv.DictReader(open(out_csv)):
            if r.get("transport_fail") != "True":
                done.add((r["arm"], r["item_id"], str(r.get("rep", ""))))
        before = len(jobs)
        jobs = [j for j in jobs
                if (j["arm"], j["item"]["id"], str(j["rep"] if j["rep"] is not None else ""))
                not in done]
        print(f"[{tag}] resume: {before - len(jobs)} already-complete jobs skipped, "
              f"{len(jobs)} to run", flush=True)
        if not jobs:
            print(f"[{tag}] nothing to do", flush=True)
            return
    buf, done, lock = [], 0, threading.RLock()  # DEV-9 fix (2026-08-25): was Lock(); emit() held lock then called _flush() which re-acquired -> permanent self-deadlock at BATCH_FLUSH boundary
    t_start = time.time()
    def work(j):
        time.sleep(random.uniform(0, 0.3))
        return run_arm(j["arm"], j["item"], j["temp"], j["rep"])
    def emit(o, j, rerun=False):
        o.setdefault("ts", ""); o["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        o["rerun"] = 1 if rerun else 0
        o.setdefault("family", j["item"]["family"]); o.setdefault("template", j["item"]["template"])
        o.setdefault("item_id", j["item"]["id"]); o.setdefault("rep", j["rep"] or "")
        o.setdefault("temperature", j["temp"]); o.setdefault("score", 0.0)
        o.setdefault("gate_pass", False); o.setdefault("f0_ok", False)
        o.setdefault("final_error", repr(o.get("_exc", ""))[:250])
        with lock:
            buf.append(o); _flush()
    done_n = [0]
    def done_local():
        return done_n[0]
    def _flush(force=False):
        if len(buf) >= CFG.BATCH_FLUSH or (force and buf):
            with lock:
                append_csv(out_csv, buf, OUT_FIELDS)
                buf.clear()
            print(f"[{tag}] {done_n[0]}/{len(jobs)} flushed ({time.time()-t_start:.0f}s)", flush=True)
    failed_jobs = []
    with ThreadPoolExecutor(max_workers=CFG.MAX_WORKERS) as px:
        futs = {px.submit(work, j): j for j in jobs}
        for fu in as_completed(futs):
            j = futs[fu]
            try:
                o = fu.result()
            except Exception as ex:
                o = {"_exc": ex, "arm": j["arm"], "transport_fail": True}
            # DEV-7 rule (frozen pre-scored-call): transport-failed outcome gets exactly
            # ONE mechanical re-execution; both readings retained; analysis takes the
            # latest non-transport-fail reading per (arm,item,rep).
            if o.get("transport_fail"):
                emit(o, j)
                failed_jobs.append(j)
                time.sleep(5)
                try:
                    o2 = work(j)
                    emit(o2, j, rerun=True)
                    if not o2.get("transport_fail"):
                        done_n[0] += 1; continue
                except Exception as ex:
                    emit({"_exc": ex, "arm": j["arm"], "transport_fail": True}, j, rerun=True)
            else:
                emit(o, j)
            done_n[0] += 1
    if buf:
        _flush(True)
    print(f"[{tag}] DONE {done_n[0]} outcomes ({len(failed_jobs)} transport-retried) -> {out_csv.name}", flush=True)

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

def jobs_repl(banks, families, comp_arm):
    js = []
    for fam in families:
        for it in strat10(banks[fam]):
            for rep, seed in enumerate(CFG.REPL_SEEDS):
                for arm in ("CSIR-SIR", comp_arm):
                    js.append({"arm": arm, "item": it, "rep": rep, "temp": 0.7})
    return js

# ------------------------------------------------------------- F3 probe ----
def _norm_payload(pl):
    def nv(v):
        if isinstance(v, str): return re.sub(r"\s+", " ", v.strip().lower())
        if isinstance(v, bool): return str(v).lower()
        if isinstance(v, (int, float)): return round(float(v), 4)
        if isinstance(v, list): return [nv(x) for x in v]
        if isinstance(v, dict): return tuple(sorted((k, nv(x)) for k, x in v.items()))
        return str(v)
    return tuple(sorted((k, nv(v)) for k, v in pl.items()))

def canon(doc):
    nodes = []
    ids = []
    for n in doc.get("nodes", []) or []:
        if not isinstance(n, dict): continue
        ids.append(n.get("id"))
        pl = {k: v for k, v in n.items() if k not in ("id", "spans", "kind")}
        unk = bool(n.get("unknown")) or bool(n.get("ask_user")) or \
              (isinstance(n.get("canonical"), dict) and n["canonical"].get("unknown"))
        nodes.append({"id": n.get("id"), "kind": n.get("kind"),
                      "key": (n.get("kind"), _norm_payload(pl)), "unknown": unk})
    edges = [(e.get("rel"), e.get("from"), e.get("to"))
             for e in doc.get("edges", []) or [] if isinstance(e, dict)]
    return nodes, edges

def f3_compare(doc_a, doc_b):
    na, ea = canon(doc_a)
    nb, eb = canon(doc_b)
    pool_b = defaultdict(list)
    for j, n in enumerate(nb): pool_b[n["key"]].append(j)
    match = {}; unmatched_kinds = defaultdict(int)
    n_nonunk = n_match = 0
    unknown_adj_fail = unknown_adj_total = adj_fail = adj_total = 0
    b_edges = set(eb)
    adj_ids = set()
    for _, f, t in ea: adj_ids.update((f, t))
    for i, n in enumerate(na):
        if n["unknown"]: continue
        n_nonunk += 1
        cands = pool_b.get(n["key"]) or []
        rel_keys = [k for k in pool_b if k[0] == n["kind"]]
        if cands:
            j = cands.pop(0); match[n["id"]] = nb[j]["id"]; n_match += 1
        else:
            unmatched_kinds[n["kind"]] += 1
            near_unk = n["id"] in adj_ids and any(
                True for r, f, t in ea if (f == n["id"] or t == n["id"]))
            adj_total += 1
    edge_keep = tot_e = 0
    inv = {v: k for k, v in match.items()}
    for rel, f, t in ea:
        if f in match and t in match:
            tot_e += 1
            if (rel, match[f], match[t]) in b_edges: edge_keep += 1
    rate = n_match / n_nonunk if n_nonunk else 1.0
    erate = edge_keep / tot_e if tot_e else 1.0
    return {"n_nodes": len(na), "n_nonunknown": n_nonunk, "n_matched": n_match,
            "rate": rate, "edge_rate": erate,
            "unmatched_kinds": json.dumps(dict(unmatched_kinds))}

def read_rows_local(name):
    fp = RES / name
    return list(csv.DictReader(open(fp))) if fp.exists() else []

RES = CFG.RESULTS

def run_f3():
    prim_latest = {}
    for r in sorted(read_rows_local("outcomes.csv"), key=lambda r: r.get("ts", "")):
        if r.get("transport_fail") != "True":
            prim_latest[(r["arm"], r["item_id"], str(r.get("rep", "")))] = r
    sir_items = sorted(k for k, r in prim_latest.items()
                       if k[0] == "CSIR-SIR" and r.get("doc_valid") == "True")
    banks = load_banks()
    by_id = {it["id"]: it for fam in banks.values() for it in fam}
    rows = []
    print(f"F3 probe over {len(sir_items)} valid docs", flush=True)
    for (arm, iid, rep) in sir_items:
        it = by_id[iid]
        rp = REPO / prim_latest[(arm, iid, rep)]["raw_path"]
        raw = json.load(open(rp))
        conv_att = [a for a in raw["attempts"] if a["stage"].startswith("convert")]
        if not conv_att: continue
        doc_txt = conv_att[-1]["content"]
        try:
            doc = extract_json(doc_txt)
        except Exception:
            continue
        r1 = call("F3DEC", P_F3DEC + "\n\nCSIR/0 DOCUMENT:\n" + doc_txt, 0.0)
        if not r1["ok"] or not r1["content"]:
            continue
        enc_in = (FB.F_CONV + "\n\nSOURCE INTENT:\n" + r1["content"] +
                  "\n\nREQUIRED OUTPUT ARTIFACT (task question):\n" + it["question"] +
                  "\n\nConvert this intent to its CSIR/0 JSON document now.")
        r2 = call("CSIR-SIR::conv", enc_in, 0.0)
        if not r2["ok"] or not r2["content"]:
            continue
        try:
            doc2 = extract_json(r2["content"])
        except Exception:
            doc2 = {}
        res = f3_compare(doc, doc2)
        res.update({"item_id": iid, "family": it["family"], "template": it["template"],
                    "latency_ms": r1["latency_ms"] + r2["latency_ms"],
                    "probe_p_in": r1["p_in"] + r2["p_in"], "probe_p_out": r2["p_out"]})
        rows.append(res)
        if len(rows) % 20 == 0:
            append_csv(RES / "f3.csv", [rows[-1]], list(rows[-1].keys()))
            print(f"F3 {len(rows)} done", flush=True)
    if rows:
        append_csv(RES / "f3.csv", rows, list(rows[0].keys()))
    print(f"[F3] DONE {len(rows)}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["smoke", "primary", "h2", "repl", "f3", "rerun_sir"])
    ap.add_argument("--comparator", default="JSON")
    ap.add_argument("--families", default="EX,TU")
    banks = load_banks()
    a = ap.parse_args()
    if a.mode == "rerun_sir":
        # Amendment-3: CSIR-SIR arm only, all families, temp=0, separate CSV
        js = [{"arm": "CSIR-SIR", "item": it, "rep": None, "temp": 0.0}
              for fam in CFG.FAMILIES for it in banks[fam]]
        run_batch("rerun_sir", js, "RERUN-SIR")
    elif a.mode == "smoke":
        jobs = [{"arm": ar, "item": it, "rep": None, "temp": 0.0}
                for ar in ("NL-plain", "NL-opt", "JSON") for it in
                (banks["EX"][0], banks["TU"][0])]
        jobs.append({"arm": "CSIR-SIR", "item": banks["EX"][0], "rep": None, "temp": 0.0})
        run_batch("smoke", jobs, "SMOKE")
    elif a.mode == "primary":
        fams = [f for f in a.families.split(",") if f in CFG.FAMILIES] or list(CFG.FAMILIES)
        js = [{"arm": ar, "item": it, "rep": None, "temp": 0.0}
              for fam in fams for ar in CFG.ARMS for it in banks[fam]]
        run_batch("primary", js, "PRIMARY")
    elif a.mode == "h2":
        run_batch("h2", jobs_h2(banks), "H2")
    elif a.mode == "repl":
        fams = [f for f in a.families.split(",") if f in CFG.FAMILIES]
        run_batch("repl", jobs_repl(banks, fams, a.comparator), "REPL")
    elif a.mode == "f3":
        run_f3()

if __name__ == "__main__":
    main()
