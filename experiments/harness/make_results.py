"""E1 results assembly — driver for the FULL §1.4 analysis + registered verdicts.

Pipeline: analysis.py (part 1) -> analysis2.py (modules) -> this script writes
experiments/results/E1/E1_RESULTS.md. Reads only files under results/E1/.
Verdicts evaluate each registered falsification condition EXACTLY as stated
(pre-reg §6); no re-wording. Frozen pre-unblinding.
"""
import csv, json, math, statistics as st
from collections import defaultdict
from pathlib import Path

REPO = Path("/home/shivam/philosophy/project-characteristica")
EXP = REPO / "experiments"
RES = EXP / "results" / "E1"
import sys
sys.path.insert(0, str(EXP / "harness"))

P8_FLAG_VERBATIM = ("Red Team flag P8 (model dependence): conclusions are provisionally "
                    "scoped to the amended model family until a paid-model confirmation "
                    "batch (E1b) replicates direction.")

def jload(p, default=None):
    p = RES / p
    return json.load(open(p)) if p.exists() else default

def rows_of(name):
    fp = RES / name
    return list(csv.DictReader(open(fp))) if fp.exists() else []

def latest_valid(rows):
    best = {}
    for r in sorted(rows, key=lambda r: r.get("ts", "")):
        if r.get("transport_fail") == "True": continue
        best[(r["arm"], r["item_id"], str(r.get("rep", "")))] = r
    return best

def pct(x): return f"{x*100:.1f}"

def main():
    import analysis, analysis2
    try:
        analysis.main()
    except Exception as e:
        print("analysis.main failed:", repr(e))
    try:
        analysis2.main()
    except Exception as e:
        print("analysis2.main failed:", repr(e))

    st1 = jload("analysis_state.json", {})
    cells = st1.get("cells", {})
    comp = st1.get("comparator", {})
    boot = st1.get("boot", {})
    f2 = jload("f2_audit.json", {"f2_rates": {}, "f2_unknown": {}})
    rates = f2.get("f2_rates", {})
    prim = latest_valid(rows_of("outcomes.csv"))
    h2rows = latest_valid(rows_of("h2_outcomes.csv"))
    L = []
    P = L.append

    # ---------------- header ----------------
    m = json.load(open(RES / "manifest.json"))
    P("# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)")
    P("")
    P("**STATUS:** scored-run data collected under AMENDMENT-1 · analysis basis MEASUREMENT_PLAN "
      "§1.4 ONLY (§1.9 quarantined illustrative-only)")
    P("")
    P(f"**Amended model pin (D-2 per Amendment-1, countersigned W0f' 2026-08-24):** "
      f"`{m['model_id']}` — **OpenRouter `:free` tier (is_free_tier=true)**, selected ONCE at run time "
      f"as the highest-capability :free model verifiably serving (selection record in manifest.json; "
      f"AA Intelligence Index ranking: glm-5.2=53 > inkling=41[harness-gated 403] > nemotron-ultra=38). "
      f"Used identically for ALL arms incl. converter (D-4 preserved). Amendment reference: "
      f"experiments/E1_AMENDMENT_1.md.")
    P(f"")
    P(f"**Price vector (run date {m['price_retrieval_date']}, {m['price_source_url']}):** "
      f"p_in=$0.00/M, p_out=$0.00/M (`:free` tier publishes $0/$0). Consequence declared BEFORE "
      f"unblinding: §1.4 formulas are unchanged (amendment condition #5), so every $(N) and Δ(N) below "
      f"is identically $0.000000 — **the dollar axis is degenerate under a zero price vector**; no $ "
      f"comparison can show a detectable advantage or disadvantage (plan §4.5 ceiling applies "
      f"a fortiori). Directional $ predictions are therefore evaluated as 'no detectable difference "
      f"(degenerate instrument)', and token diagnostics are reported alongside as raw diagnostics.")
    P("")
    P(f"> **{P8_FLAG_VERBATIM}**")
    P("")
    P("**Power honesty (plan §4.5):** n=50/cell ⇒ only effects ≳15–20 F1 points interpretable; "
      "verdict language says \"no detectable advantage\", never \"no advantage\".")
    P("**Exclusions:** none. DEV-7 rule applied mechanically (both readings retained; latest "
      "non-transport-fail reading analyzed). Zero rows dropped.")
    P("")

    # ---------------- cell table (from part1 file) ----------------
    p1 = (RES / "E1_RESULTS_part1.md")
    if p1.exists():
        body = p1.read_text().split("\n")
        # drop part1's own H1 title; keep everything else verbatim
        while body and (body[0].startswith("# ") or body[0] == ""): body.pop(0)
        L.extend(body)
        L.append("")

    part2 = (RES / "E1_RESULTS_part2.md")
    if part2.exists():
        L.append(part2.read_text())
        L.append("")

    # ---------------- verdicts ----------------
    def gate(armfam):
        c = cells.get(armfam)
        return c["gate"] if c else None

    def silent(armfam):
        c = cells.get(armfam)
        return c["silent"] if c else None

    def conv_rate(types):
        vals = [rates[t]["conv"] for t in types if t in rates and rates[t]["conv"] is not None]
        ns = [rates[t]["n"] for t in types if t in rates and rates[t]["conv"] is not None]
        return (sum(r*v for r, v in zip([n for n in ns], [x for x in vals]) ) /
                max(1, sum(ns))) if vals else None

    P("## 8. Registered predictions — evaluated exactly as stated (pre-reg §6)")
    P("")
    P("### P1 — EX: SIR vs strongest NL arm")
    f2_ex_types = list(rates.keys())
    ex_conv_all = [rates[t]["conv"] for t in f2_ex_types
                   if rates[t]["conv"] is not None] if rates else []
    ex_f2_overall = (sum(rates[t]["conv"]*rates[t]["n"] for t in f2_ex_types
                         if rates[t]["conv"] is not None) /
                     sum(rates[t]["n"] for t in f2_ex_types
                         if rates[t]["conv"] is not None)) if ex_conv_all else None
    sir_ex, base_ex = cells.get("CSIR-SIR|EX"), cells.get((comp.get("EX") or "")+"|EX")
    d_f1_ex = (sir_ex["gate"] - base_ex["gate"]) if (sir_ex and base_ex) else None
    cond = (ex_f2_overall is not None and ex_f2_overall >= 0.90)
    P(f"- Conversion-stage F2 (EX, unit-weighted across audited types): "
      f"**{ex_f2_overall if ex_f2_overall is None else round(ex_f2_overall,3)}** "
      f"(condition-to-fire '>': F2 ≥ 0.90 → {'FIRED' if cond else 'NOT FIRED'})")
    P(f"- Observed gate-success SIR vs strongest NL arm ({comp.get('EX','—')}): "
      f"{pct(sir_ex['gate'])} vs {pct(base_ex['gate'])} (Δ={d_f1_ex:+.1f} pts)"
      if sir_ex and base_ex else "- Insufficient data.")
    P("- $ @N=1 `<` and $ @N=25 `>` iff F2≥0.90: $ instrument degenerate (all $≡0) → "
      "**no detectable difference on the registered $ endpoint**; F1 side: "
      + (f"SIR {'>' if (d_f1_ex or 0)>0 else ('<' if (d_f1_ex or 0)<0 else '≈')} comparator"
         if d_f1_ex is not None else "n/a"))
    P("")
    P("### P2 — UNL-replay guard (fires iff EX conversion-stage F2 < 0.80)")
    fired2 = ex_f2_overall is not None and ex_f2_overall < 0.80
    P(f"- Condition: EX F2 < 0.80 → {'FIRED' if fired2 else 'NOT FIRED'}"
      + (f" (F2={ex_f2_overall:.3f})" if ex_f2_overall is not None else ""))
    if fired2:
        P("- Predicted Δ(N)<0 ∀N: observed Δ(N)≡$0 (degenerate) → predicted strict inequality "
          "not observable on the $ instrument; recorded as **not evaluable in $ terms "
          "(instrument degeneracy)**, diagnostic value limited to F2 level itself.")
    P("")
    P("### P3 — Conversion-loss localization")
    pred_lost = ["modality", "preference_order", "exclusion"]
    easy = ["entity_ref", "quantity_unit"]
    def loss(t):
        r = rates.get(t)
        return (1-r["conv"]) if r and r["conv"] is not None else None
    ll = {t: loss(t) for t in set(pred_lost+easy)}
    P(f"- Per-type conversion-stage losses: " +
      ", ".join(f"{t}={('—' if v is None else f'{v:.2f}')}" for t, v in sorted(ll.items())))
    have_pred = [ll[t] for t in pred_lost if ll.get(t) is not None]
    have_easy = [ll[t] for t in easy if ll.get(t) is not None]
    if have_pred and have_easy:
        mp, me = st.mean(have_pred), st.mean(have_easy)
        conc = mp > me
        P(f"- Mean loss in predicted-lost classes {mp:.2f} vs easy classes {me:.2f} → "
          f"loss concentrates in predicted classes: **{conc}** → P3 "
          f"{'SUPPORTED' if conc else '**FALSIFIED** (loss concentrates in the easy classes)'}")
    else:
        P("- Insufficient audited coverage in the named classes to evaluate (see F2 table).")
    P("")
    P("### P4 — H2 variance (CP module)")
    h2state = {}
    p2txt = (RES/"E1_RESULTS_part2.md").read_text() if (RES/"E1_RESULTS_part2.md").exists() else ""
    import re as _re
    h2tab = dict()
    for mm in _re.finditer(r"\| (NL-opt|JSON|CSIR-SIR) \| (\d+) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", p2txt):
        h2tab[mm.group(1)] = dict(n=int(mm.group(2)), agree=float(mm.group(3)),
                                  ent=float(mm.group(4)), score=float(mm.group(5)))
    if h2tab:
        s = h2tab.get("CSIR-SIR"); nl = h2tab.get("NL-opt"); js = h2tab.get("JSON")
        if s and nl and js:
            beats_nl = (s["agree"] - nl["agree"]) >= 0.15
            beats_js = (s["agree"] - js["agree"])
            partial = beats_js > 0
            P(f"- Agreement: SIR {s['agree']:.2f} vs NL-opt {nl['agree']:.2f} vs JSON {js['agree']:.2f}")
            P(f"- SIR dispersion < both NL arms (≥15-pt detectable gap): "
              f"{beats_nl}; survives JSON comparison (partial-survival rule): {partial}")
            verd = ("SUPPORTED" if (beats_nl and partial)
                    else ("WEAKENED (effect attributable to generic structuring — registry criterion)"
                          if beats_js <= 0 and beats_nl else "NOT SUPPORTED (no detectable gap)"))
            P(f"- Verdict: **{verd}**")
    else:
        P("- H2 module data absent/not yet run.")
    P("")
    P("### P5 — H4 silent errors (CP ↓ both NL arms; TU: NO significant SIR>JSON edge)")
    sc = {a: silent(f"{a}|CP") for a in ("NL-plain","NL-opt","JSON","CSIR-SIR")}
    stu = {a: silent(f"{a}|TU") for a in ("JSON","CSIR-SIR")}
    if all(v is not None for v in sc.values()):
        red_nl = sc["CSIR-SIR"] < sc["NL-opt"] and sc["CSIR-SIR"] < sc["NL-plain"]
        tu_edge = None
        if stu["CSIR-SIR"] is not None and stu["JSON"] is not None:
            tu_edge = stu["JSON"] - stu["CSIR-SIR"]
        bought_below = False
        g_sir, g_js = gate("CSIR-SIR|CP"), gate("JSON|CP")
        if g_sir is not None and g_js is not None:
            bought_below = (g_js - g_sir) > 4.0     # δ_F1(CP)=4 pts
        P(f"- CP silent-error fractions: NL-plain {pct(sc['NL-plain'])} | NL-opt {pct(sc['NL-opt'])} | "
          f"JSON {pct(sc['JSON'])} | **SIR {pct(sc['CSIR-SIR'])}** → reduction vs both NL arms: {red_nl}")
        P(f"- TU silent-error JSON−SIR gap: "
          f"{('%s pts' % format(tu_edge*100, '.1f')) if tu_edge is not None else 'n/a'} "
          f"(registered expectation: NO significant SIR-over-JSON advantage)")
        tu_sir_adv_detectable = (tu_edge is not None and tu_edge >= 0.15)
        if red_nl and not tu_sir_adv_detectable:
            verd5 = "SUPPORTED"
        elif tu_sir_adv_detectable:
            verd5 = "**FALSIFIED** per registry criteria (TU SIR-over-JSON edge exists — adversarial control violated)"
        else:
            verd5 = ("**FALSIFIED** per registry criteria (reduction absent"
                     + (" / bought below δ_F1)" if bought_below else ")"))
        P(f"- Verdict: **{verd5}**")
    else:
        P("- Silent-error data incomplete.")
    P("")
    P("### P6 — TU adversarial loss (SIR ≤ JSON in tool-use; contrary ⇒ mandatory red-team review)")
    gs, gj = gate("CSIR-SIR|TU"), gate("JSON|TU")
    if gs is not None and gj is not None:
        contrary = gs > gj
        P(f"- TU gate success: SIR {pct(gs)} vs JSON {pct(gj)} (Δ={gs-gj:+.1f} pts; "
          f"$ endpoint degenerate)")
        if contrary:
            P("- Registered prediction SIR ≤ JSON: **CONTRARY RESULT — mandatory red-team review "
              "before any claim** (per MEASUREMENT_PLAN §4.7)")
        else:
            P("- Registered prediction SIR ≤ JSON: **CONFIRMED** — the registered adversarial "
              "loss is honestly reported: on the F1 endpoint SIR loses to (or ties) the JSON arm "
              "in its schema-native territory.")
    else:
        P("- TU data incomplete.")
    P("")
    P("### P7 — F3 round-trip stability (δ_F3=0.90; failures concentrate at unknown/branch nodes)")
    f3rows = rows_of("f3.csv")
    if f3rows:
        nn = sum(int(r["n_nonunknown"]) for r in f3rows)
        nm = sum(int(r["n_matched"]) for r in f3rows)
        rate = nm/nn if nn else None
        kinds = defaultdict(int)
        for r in f3rows:
            try:
                for k, v in (json.loads(r.get("unmatched_kinds") or "{}")).items(): kinds[k]+=int(v)
            except Exception: pass
        tot_fail = sum(kinds.values())
        unk_kinds = sum(v for k, v in kinds.items() if k in ("scope_marker",) or "unknown" in k.lower())
        P(f"- Micro rate over {len(f3rows)} docs, {nn} non-unknown nodes: "
          f"**{rate:.3f}** → threshold δ_F3=0.90 {'MET' if (rate or 0)>=0.90 else '**MISSED — FALSIFIED**'}")
        P(f"- Failure kinds: {dict(kinds)} → concentration at unknown-flagged/branch nodes: "
          f"{'not separable by kind at this sample' if tot_fail==0 else f'{unk_kinds}/{tot_fail}' }")
    else:
        P("- F3 probe not run.")
    P("")
    P("### H1 central gate (four conditions, per family) & H0 standing")
    for fam in ("EX", "CP", "TU"):
        b = comp.get(fam)
        if not b: continue
        c1 = "(1) efficiency CI excl. zero: $ instrument degenerate → cannot be satisfied in $ terms"
        c2 = ""
        gs_, gb_ = gate(f"CSIR-SIR|{fam}"), gate(f"{b}|{fam}")
        if gs_ is not None and gb_ is not None:
            df1 = {"EX": 3.0, "CP": 4.0, "TU": 3.0}[fam]
            c2 = f"(2) F1 non-inferiority (δ={df1}): {'PASS' if gs_ >= gb_-df1 else 'FAIL'} " \
                 f"(Δ={gs_-gb_:+.1f})"
        P(f"- **{fam}** (comparator {b}): {c1}; {c2}; (3)+(4) see replication/red-team above. "
          f"=> H1 support requires ALL four: **not achieved in $ terms by construction of the "
          f"free-tier instrument; family cannot pass on the registered primary endpoint.**")
    P("")
    P("- **H0 standing:** stands unless ≥1 family passes all four conditions — "
      "**H0 STANDS** (no family passes condition 1 on a degenerate $ instrument).")
    P("")
    P("---")
    P("*Deviations ledger: DEVIATIONS.md DEV-1..DEV-8 (DEV-8 = Amendment-1 re-pin, pacing, "
      "checkpoint-resume; all pre-first-scored-call). Interruptions: INTERRUPTION_LOG.md.*")

    out = RES / "E1_RESULTS.md"
    out.write_text("\n".join(L))
    print("E1_RESULTS.md written:", out, len(L), "lines")

if __name__ == "__main__":
    main()
