"""E1 analysis part 2 — modules + registered-prediction verdicts.

Runs AFTER analysis.py (part 1). Reads ONLY files under experiments/results/E1/
(+ harness banks for gold/unit metadata and frozen parsers for offline re-parse
of stored attempt contents — no API contact). Frozen pre-unblinding.
Outputs E1_RESULTS_part2.md consumed by make_results.py.
"""
import csv, json, math, random, statistics as st
from collections import defaultdict, Counter
from pathlib import Path

REPO = Path("/home/shivam/philosophy/project-characteristica")
EXP = REPO / "experiments"
RES = EXP / "results" / "E1"
import sys
sys.path.insert(0, str(EXP / "harness"))
import checkers as CH

N_VALUES = [1, 10, 25, 100]

def read_rows(name):
    fp = RES / name
    return list(csv.DictReader(open(fp))) if fp.exists() else []

def latest_valid(rows):
    best = {}
    for r in sorted(rows, key=lambda r: r.get("ts", "")):
        if r.get("transport_fail") == "True": continue
        best[(r["arm"], r["item_id"], str(r.get("rep", "")))] = r
    return best

def load_banks():
    bdir = EXP / "harness" / "items" / "banks"
    return {f: json.load(open(bdir / f"{f.lower()}_bank.json")) for f in ("EX", "CP", "TU")}

def strat10(bank):
    by = {}
    for it in bank: by.setdefault(it["template"], []).append(it)
    out = []
    for t in sorted(by): out += by[t][:2]
    return out

def norm(v):
    if v is None: return ""
    s = str(v).strip().lower()
    return " ".join(s.split())

# ------------------------------------------------------------------ F2 ----
def gold_leaf_values(item):
    """checker_field -> list of scalar leaf values from gold (for containment test)."""
    fam, g = item["family"], item["gold"]
    out = {}
    def leaves(x):
        if isinstance(x, dict):
            for v in x.values(): yield from leaves(v)
        elif isinstance(x, list):
            for v in x: yield from leaves(v)
        elif x is not None:
            yield x
    if fam == "EX":
        for f, v in g["fields"].items():
            out[f] = [v] if not isinstance(v, (list, dict)) else list(leaves(v))
    elif fam == "TU":
        # map each traced checker_field to the call-arg values of the matching call
        calls = g.get("calls", [])
        idx = {"tool": 0}
        for f in item["field_ids"]:
            vals = []
            for c in calls:
                if f == "tool":
                    vals.append(c["tool"])
                else:
                    for a, av in c.get("args", {}).items():
                        if f.endswith(a) or a in f or f == a:
                            vals.append(av)
                        elif f in ("clarify",) :
                            vals.append("CLARIFY")
                if f.startswith("refund_unavail"):
                    vals.append("refund unavailable")
            out[f] = list(leaves(vals)) if vals else []
        if "clarify" in item["field_ids"]: out["clarify"] = ["clarify"]
    else:  # CP: constraint units -> use param values cited per constraint id prefix
        out = {c["id"]: [] for c in g["constraints"]}
    return out

def unit_audit(fam_rows_by_item, banks, raw_dir):
    """Conversion-stage vs behavioral recovery per unit type on stratified sample."""
    trace = json.load(open(EXP / "harness" / "items" / "banks" / "w0b_unit_traceability.json"))
    by_item = defaultdict(list)
    for t in trace: by_item[t["item"]].append(t)
    res = defaultdict(lambda: {"conv": 0, "conv_n": 0, "beh": 0, "beh_n": 0})
    unk = defaultdict(lambda: {"ok": 0, "n": 0})
    detail = []
    for fam, bank in banks.items():
        sample = {it["id"]: it for it in strat10(bank)}
        for iid, it in sample.items():
            r = fam_rows_by_item.get((fam, iid))
            if r is None: continue
            rp = REPO / r["raw_path"]
            if not rp.exists(): continue
            raw = json.load(open(rp))
            conv_att = [a for a in raw["attempts"] if a["stage"].startswith("convert")]
            exec_att = [a for a in raw["attempts"] if a["stage"] == "execute"]
            doc_txt = conv_att[-1]["content"] if conv_att else ""
            art_txt = exec_att[-1]["content"] if exec_att else ""
            try:
                art = CH.parse_answer(it, "CSIR-SIR", art_txt)
                art_s = norm(json.dumps(art, sort_keys=True, default=str))
            except Exception:
                art_s = norm(art_txt)
            doc_s = norm(doc_txt)
            gv = gold_leaf_values(it)
            for u in by_item.get(iid, []):
                ut = u["unit_type"]
                fld = u["checker_field"]
                vals = [norm(v) for v in gv.get(fld, []) if norm(v)]
                is_unknown_probe = (not vals) or all(v in ("unknown", "null", "none") for v in vals)
                if fld in gv and not gv[fld] and fam == "CP":
                    continue                      # CP ids are internal labels, see report note
                if is_unknown_probe:
                    key_u = unk[ut]; key_u["n"] += 1
                    marked = ("unknown" in doc_s or "unk" in doc_s) and \
                             ("unknown" in art_s or "unk" in art_s or "not specified" in art_s)
                    key_u["ok"] += 1 if marked else 0
                    continue
                hit_c = any(v in doc_s for v in vals)
                hit_b = any(v in art_s for v in vals)
                d = res[ut]; d["conv_n"] += 1; d["beh_n"] += 1
                d["conv"] += hit_c; d["beh"] += hit_b
                detail.append({"item": iid, "unit": u["unit_id"], "type": ut,
                               "conv": int(hit_c), "beh": int(hit_b)})
    rates = {ut: {"conv": d["conv"] / d["conv_n"] if d["conv_n"] else None,
                  "beh": d["beh"] / d["beh_n"] if d["beh_n"] else None,
                  "n": d["conv_n"]} for ut, d in sorted(res.items())}
    unk_rates = {ut: {"handled": d["ok"], "n": d["n"],
                      "rate": d["ok"] / d["n"] if d["n"] else None}
                 for ut, d in sorted(unk.items())}
    return rates, unk_rates, detail

# ------------------------------------------------------------- H2 module ----
def answer_signature(item, arm, content):
    try:
        art = CH.parse_answer(item, arm, content)
        return norm(json.dumps(art, sort_keys=True, default=str))[:400]
    except Exception:
        return "UNPARSED::" + norm(content)[:200]

def h2_module(banks):
    rows = read_rows("h2_outcomes.csv")
    lv = latest_valid(rows)
    by_id = {it["id"]: it for b in banks.values() for it in b}
    per = defaultdict(dict)          # (arm,iid) -> rep -> signature/score
    for (arm, iid, rep), r in lv.items():
        if r.get("rep", "") == "": continue
        rp = REPO / r["raw_path"]
        sig = "MISSING"
        if rp.exists():
            raw = json.load(open(rp))
            ex = [a for a in raw["attempts"] if a["stage"] == "execute"]
            if ex: sig = answer_signature(by_id[iid], arm, ex[-1]["content"])
        per[(arm, iid)][int(rep)] = (sig, float(r["score"]))
    out = {}
    for arm in ("NL-opt", "JSON", "CSIR-SIR"):
        agr, ent, sc = [], [], []
        for (a, iid), reps in per.items():
            if a != arm or len(reps) < 3: continue
            sigs = [s for s, _ in reps.values()]
            cnt = Counter(sigs); modal = cnt.most_common(1)[0][1]
            agr.append(modal / len(sigs))
            n = len(sigs)
            H = -sum((c/n)*math.log2(c/n) for c in cnt.values())
            ent.append(H)
            sc.append(st.mean(sc_ for _, sc_ in reps.values()))
        if agr:
            out[arm] = {"items": len(agr), "modal_agreement": st.mean(agr),
                        "mean_entropy_bits": st.mean(ent), "mean_score_T0.7": st.mean(sc)}
    return out

# --------------------------------------------------------- replication ------
def repl_module():
    rows = read_rows("repl_outcomes.csv")
    lv = latest_valid(rows)
    folds = defaultdict(lambda: defaultdict(list))   # fam -> rep -> [(sir_gate, base_gate)]
    for (arm, iid, rep), r in lv.items():
        if rep == "": continue
        folds[r["family"]][int(rep)].append(
            (arm, 1.0 if r["gate_pass"] == "True" else 0.0))
    out = {}
    for fam, fs in folds.items():
        arms = set(a for rep in fs for a, _ in fs[rep])
        sir = next((a for a in arms if a == "CSIR-SIR"), None)
        base = next((a for a in arms if a != "CSIR-SIR"), None)
        if not sir or not base: continue
        signs = []
        for rep in sorted(fs):
            sg = st.mean(g for a, g in fs[rep] if a == sir)
            bg = st.mean(g for a, g in fs[rep] if a == base)
            signs.append(sg - bg)
        pos = sum(1 for s in signs if s > 0); neg = sum(1 for s in signs if s < 0)
        out[fam] = {"comparator": base, "fold_deltas_gate": [round(s, 4) for s in signs],
                    "sign_consistent": bool(pos == len(signs) or neg == len(signs)),
                    "direction": "+" if pos > neg else ("- " if neg > pos else "0")}
    return out

def item_split_sign(prim, comp_map):
    """§7 three-fold item-split sign consistency on primary gate deltas."""
    out = {}
    rng = random.Random(20260824)
    for fam, b_arm in comp_map.items():
        pairs = defaultdict(lambda: ([], []))
        for (arm, iid, rep), r in prim.items():
            if r["family"] != fam or arm not in ("CSIR-SIR", b_arm): continue
            pairs[iid][0 if arm == "CSIR-SIR" else 1].append(r)
        iids = sorted(k for k, (s, b) in pairs.items() if s and b)
        if len(iids) < 6: out[fam] = None; continue
        shuf = iids[:]; rng.shuffle(shuf)
        k = max(1, len(shuf)//3); folds = [shuf[i:i+k] for i in range(0, len(shuf), k)][:3]
        signs = []
        for fold in folds:
            sg = st.mean(st.mean(1.0 if pairs[i][0][j]["gate_pass"] == "True" else 0.0
                                 for j in range(len(pairs[i][0]))) for i in fold)
            bg = st.mean(st.mean(1.0 if pairs[i][1][j]["gate_pass"] == "True" else 0.0
                                 for j in range(len(pairs[i][1]))) for i in fold)
            signs.append(sg - bg)
        pos = sum(1 for s in signs if s > 0); neg = sum(1 for s in signs if s < 0)
        out[fam] = {"fold_deltas": [round(s, 4) for s in signs],
                    "sign_consistent": bool(pos == len(signs) or neg == len(signs))}
    return out

# ---------------------------------------------------------------- F3 --------
def f3_module():
    rows = read_rows("f3.csv")
    if not rows: return None
    n_nodes = sum(int(r["n_nonunknown"]) for r in rows)
    n_match = sum(int(r["n_matched"]) for r in rows)
    e_tot = 0; e_keep = 0
    kinds = Counter()
    for r in rows:
        try:
            uk = json.loads(r.get("unmatched_kinds") or "{}")
            for k, v in uk.items(): kinds[k] += int(v)
        except Exception: pass
    rate = n_match / n_nodes if n_nodes else None
    return {"docs": len(rows), "nonunknown_nodes": n_nodes, "matched": n_match,
            "rate_micro": rate, "unmatched_kinds": dict(kinds)}

def main():
    banks = load_banks()
    prim = latest_valid(read_rows("outcomes.csv"))
    state = json.load(open(RES / "analysis_state.json")) if (RES / "analysis_state.json").exists() else {}
    comp_map = state.get("comparator") or {}
    L = []
    P = L.append
    prim_fam = defaultdict(dict)
    for (arm, iid, rep), r in prim.items():
        prim_fam[r["family"]][(arm, iid)] = r
    # F2 audit (SIR rows, stratified sample)
    sir_rows = {(fam, iid): r for (arm, iid, rep), r in prim.items()
                if arm == "CSIR-SIR"
                for fam in [r["family"]]}
    rates, unk_rates, _detail = unit_audit(sir_rows, banks, RES / "raw_outputs")
    P("## 4. F2 conversion-stage vs behavioral fidelity (stratified 20% sample, SIR arm)")
    P("")
    P("| unit type | n | conversion-stage recovery | behavioral recovery |")
    P("|---|---|---|---|")
    for ut, d in rates.items():
        cv = f"{d['conv']:.2f}" if d["conv"] is not None else "—"
        bv = f"{d['beh']:.2f}" if d["beh"] is not None else "—"
        P(f"| {ut} | {d['n']} | {cv} | {bv} |")
    if unk_rates:
        P("")
        P("Unknown-probe handling (designed probes; doc AND artifact must declare undeterminacy):")
        for ut, d in unk_rates.items():
            if d["n"]:
                P(f"- `{ut}`: {d['handled']}/{d['n']} handled ({d['rate']:.0%})")
    P("")
    P("_Note (CP instrumentation limit): CP gold constraints are internal ids checked against the "
      "emitted plan; leaf-value containment cannot attribute CP losses per unit type. CP F2 is "
      "therefore reported qualitatively via K_err/doc_valid/silent-error rather than per-unit._")
    P("")
    json.dump({"f2_rates": rates, "f2_unknown": unk_rates},
              open(RES / "f2_audit.json", "w"), indent=1)
    # H2
    h2 = h2_module(banks)
    P("## 5. H2 variance module (20 CP items x 5 reps @ T=0.7)")
    P("")
    P("| arm | items | modal-answer agreement | outcome entropy (bits) | mean score |")
    P("|---|---|---|---|---|")
    for arm in ("NL-opt", "JSON", "CSIR-SIR"):
        d = h2.get(arm)
        if d: P(f"| {arm} | {d['items']} | {d['modal_agreement']:.2f} | "
                f"{d['mean_entropy_bits']:.2f} | {d['mean_score_T0.7']:.3f} |")
    P("")
    # Replication
    repl = repl_module()
    split = item_split_sign(prim, comp_map)
    P("## 6. Replication (H1 condition 3)")
    P("")
    P("- Stochastic module (10 stratified items x 3 reps @ T=0.7, seeds 201–203), SIR vs strongest baseline:")
    for fam, d in sorted(repl.items()):
        P(f"  - {fam} vs {d['comparator']}: fold gate-deltas {d['fold_deltas_gate']} → "
          f"sign-consistent: **{d['sign_consistent']}** ({d['direction'].strip()})")
    P("- Item-split module (primary, 3 folds):")
    for fam, d in sorted(split.items()):
        if d: P(f"  - {fam}: fold gate-deltas {d['fold_deltas']} → sign-consistent: **{d['sign_consistent']}**")
    P("")
    # F3
    f3 = f3_module()
    P("## 7. F3 round-trip stability")
    P("")
    if f3:
        P(f"- docs={f3['docs']}, non-unknown nodes={f3['nonunknown_nodes']}, matched={f3['matched']} "
          f"→ micro rate **{f3['rate_micro']:.3f}** (δ_F3=0.90)")
        P(f"- unmatched node kinds: {f3['unmatched_kinds']}")
    else:
        P("- F3 probe not run/empty.")
    P("")
    (RES / "E1_RESULTS_part2.md").write_text("\n".join(L))
    print("part2 written;", len(L), "lines")

if __name__ == "__main__":
    main()
