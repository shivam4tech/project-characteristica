"""E1 analysis — MEASUREMENT_PLAN §1.4 formulas ONLY (§1.9 quarantined).

Reads experiments/results/E1/*.csv (+ raw_outputs for H2/F3/unit audits).
Frozen pre-unblinding. Bootstrap seed 20260824, 10k resamples, two-sided .05.
"""
import csv, json, math, random, statistics as st
from collections import defaultdict
from pathlib import Path

REPO = Path("/home/shivam/philosophy/project-characteristica")
RES = REPO / "experiments" / "results" / "E1"
CFG = json.load(open(RES / "manifest.json"))
P_IN, P_OUT = CFG["price_vector"]["p_in_usd_per_token"], CFG["price_vector"]["p_out_usd_per_token"]
N_VALUES = [1, 10, 25, 100]
NCONV_VALUES = [1, 10]
BOOT_N, BOOT_SEED = 10000, 20260824
ARMS = ["NL-plain", "NL-opt", "JSON", "CSIR-SIR"]
BASELINES = ["NL-plain", "NL-opt", "JSON"]

def read_rows(name):
    fp = RES / name
    if not fp.exists(): return []
    return list(csv.DictReader(open(fp)))

def num(x):
    try: return float(x)
    except Exception: return 0.0

def latest_valid(rows):
    """DEV-7 rule: latest non-transport-fail reading per (arm,item,rep)."""
    best = {}
    for r in sorted(rows, key=lambda r: r.get("ts", "")):
        if r.get("transport_fail") == "True": continue
        best[(r["arm"], r["item_id"], str(r.get("rep", "")))] = r
    return best

def cell_table(rows):
    """arm x family -> aggregates."""
    agg = {}
    g = defaultdict(list)
    for r in rows: g[(r["arm"], r["family"])].append(r)
    for (arm, fam), rs in g.items():
        n = len(rs)
        f0 = sum(r["f0_ok"] == "True" for r in rs) / n
        gate = sum(r["gate_pass"] == "True" for r in rs) / n
        score = st.mean(num(r["score"]) for r in rs)
        def m(k): return st.mean(num(r[k]) for r in rs)
        lats = [num(r["lat_total_ms"]) + num(r["conv_lat_ms"]) for r in rs]
        lats.sort()
        p50 = lats[len(lats)//2]; p95 = lats[min(len(lats)-1, int(math.ceil(.95*len(lats)))-1)]
        silent = (sum(1 for r in rs if r["f0_ok"] == "True" and r["gate_pass"] != "True")
                  / max(1, sum(1 for r in rs if r["f0_ok"] == "True")))
        kerr = sum(r.get("kerr_flag") == "True" for r in rs) / n
        docv = sum(r.get("doc_valid") == "True" for r in rs) / n
        agg[(arm, fam)] = dict(n=n, f0=f0, gate=gate, score=score,
                               v_in=m("v_in"), v_out=m("v_out"), f_tok=m("f_tok"),
                               r_in=m("r_in"), r_out=m("r_out"),
                               k_in=m("k_in"), k_out=m("k_out"), k_rin=m("k_rin"),
                               k_rout=m("k_rout"), lat_p50=p50, lat_p95=p95,
                               silent=silent, kerr=kerr, doc_valid=docv)
    return agg

def dollars(c, N):
    """§1.4: $(N) = p_in*(V_in + F/N + E[R_in]) + p_out*(V_out + E[R_out])"""
    return P_IN * (c["v_in"] + c["f_tok"] / N + c["r_in"]) + P_OUT * (c["v_out"] + c["r_out"])

def k_dollars(c):
    """Converter K$ per query (all converter attempts incl retries, F_conv included)."""
    return P_IN * (c["k_in"] + c["k_rin"]) + P_OUT * (c["k_out"] + c["k_rout"])

def total_sir(c, N, N_conv):
    return dollars(c, N) + k_dollars(c) / N_conv

def delta(curves_b, c_sir, N, N_conv):
    return curves_b - total_sir(c_sir, N, N_conv)

def item_dollars(r, arm, fam_cells, N, N_conv):
    """Item-level paired $: same formula on the item's own tokens."""
    v_in, v_out = num(r["v_in"]), num(r["v_out"])
    r_in, r_out = num(r["r_in"]), num(r["r_out"])
    f = num(r["f_tok"])
    d = P_IN * (v_in + f / N + r_in) + P_OUT * (v_out + r_out)
    if arm == "CSIR-SIR":
        d += (P_IN * (num(r["k_in"]) + num(r["k_rin"])) +
              P_OUT * (num(r["k_out"]) + num(r["k_rout"]))) / N_conv
    return d

def bootstrap_ci(diffs, seed=BOOT_SEED, n=BOOT_N):
    rng = random.Random(seed)
    m = len(diffs)
    if m == 0: return (0, 0, 0)
    means = []
    for _ in range(n):
        s = [diffs[rng.randrange(m)] for _ in range(m)]
        means.append(st.mean(s))
    means.sort()
    return (means[int(0.025*n)], st.mean(diffs), means[int(0.975*n)-1])

def strongest_baseline(agg, fam):
    key = lambda a: (agg[(a, fam)]["gate"], agg[(a, fam)]["score"])
    return max(BASELINES, key=lambda a: (key(a), BASELINES.index(a)))

def fmt(x, nd=6):
    return f"{x:.{nd}f}".rstrip("0").rstrip(".") if x == x else "nan"

def main():
    prim = latest_valid(read_rows("outcomes.csv"))
    rows = list(prim.values())
    agg = cell_table(rows)
    lines = []
    P = lines.append
    P("# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)")
    P("")
    P(f"**Model pin (D-2):** `{CFG['model_id']}` · tokenizer {CFG['tokenizer_id']}")
    P(f"**Price vector:** p_in=${P_IN*1e6:.2f}/M, p_out=${P_OUT*1e6:.2f}/M "
      f"(retrieved {CFG['price_retrieval_date']}, {CFG['price_source_url']}; live re-check equal)")
    P(f"**Decisions:** D-1 oracle OMITTED (diagnostic loss acknowledged: representation-intrinsic "
      f"vs converter-attributable causes NOT separable in E1) · D-3 paraphrase deferred to E2 · "
      f"D-4 converter model = executor model")
    P("**Analysis basis:** benchmarks/MEASUREMENT_PLAN.md §1.4 formulas ONLY; §1.9 quarantined "
      "(illustrative-only). Bootstrap 10k, seed 20260824, paired item-level, two-sided α=.05.")
    P("**Power honesty (plan §4.5):** only effects ≳15–20 F1 pts or correspondingly large $ deltas "
      "are interpretable; verdict language respects this ceiling.")
    P("")
    # ---------------- cell tables ----------------
    P("## 1. Cells: F0-gated F1 success rate, fidelity, latency (primary, T=0, n=50/family/arm)")
    P("")
    P("| arm | family | n | F0 ok | **gate success %** | mean item score | silent-error % (F0∧¬gate) | K_err | doc valid | p95 ms |")
    P("|---|---|---|---|---|---|---|---|---|---|")
    for fam in ("EX", "CP", "TU"):
        for arm in ARMS:
            c = agg.get((arm, fam))
            if not c: continue
            P(f"| {arm} | {fam} | {c['n']} | {c['f0']:.0%} | **{c['gate']*100:.1f}** | "
              f"{c['score']:.3f} | {c['silent']*100:.1f} | {c['kerr']:.0%} | "
              f"{c['doc_valid']:.0%} | {c['lat_p95']:.0f} |")
    P("")
    # ---------------- cost curves ----------------
    P("## 2. Net-of-overhead cost per arm×family, $(N) at N∈{1,10,25,100} (§1.4)")
    P("")
    comp = {}
    for fam in ("EX", "CP", "TU"):
        try:
            comp[fam] = strongest_baseline(agg, fam)
        except Exception:
            pass
    P("Comparator rule (fixed pre-reg §7): strongest baseline = highest gate success among "
      "{NL-plain, NL-opt, JSON}; ties → higher mean score → later listed. Result: " +
      ", ".join(f"{f}→{a}" for f, a in comp.items()))
    P("")
    for N_conv in NCONV_VALUES:
        tag = " (PROJECTED scenario math — N_conv>1 not confirmatory)" if N_conv > 1 else ""
        P(f"### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv={N_conv}){tag}")
        P("")
        P("| family | baseline | " + " | ".join(f"Δ N={n}" for n in N_VALUES) +
          " | " + " | ".join(f"$SIR N={n}" for n in N_VALUES) + " |")
        P("|---|---|" + "---|" * (len(N_VALUES)*2))
        for fam in ("EX", "CP", "TU"):
            cs = agg.get(("CSIR-SIR", fam)); cb = agg.get((comp.get(fam), fam))
            if not cs or not cb: continue
            ds = [delta(dollars(cb, n), cs, n, N_conv) for n in N_VALUES]
            ss = [total_sir(cs, n, N_conv) for n in N_VALUES]
            P(f"| {fam} | {comp[fam]} | " +
              " | ".join(("**+" if d > 0 else "") + f"{d*1e6:.1f}µ$" for d in ds) + " | " +
              " | ".join(f"{s*1e6:.1f}µ$" for s in ss) + " |")
        P("")
    # ---------------- bootstrap ----------------
    P("## 3. Paired item-level bootstrap — SIR vs strongest baseline (95% CI of difference)")
    P("")
    P("| family | metric | comparator | lo | mean | hi | sig? |")
    P("|---|---|---|---|---|---|---|")
    boot_summary = {}
    for fam in ("EX", "CP", "TU"):
        b_arm = comp.get(fam)
        if not b_arm: continue
        pairs = defaultdict(lambda: ([], []))
        for (arm, iid, rep), r in prim.items():
            if r["family"] != fam or arm not in ("CSIR-SIR", b_arm): continue
            pairs[iid][0 if arm == "CSIR-SIR" else 1].append(r)
        for N in (1, 25):
            for N_conv in (1,):
                d_cost, d_gate = [], []
                for iid, (sir, base) in pairs.items():
                    if not sir or not base: continue
                    d_cost.append(st.mean(item_dollars(x, "CSIR-SIR", agg, N, N_conv) for x in sir) -
                                  st.mean(item_dollars(x, b_arm, agg, N, N_conv) for x in base))
                    d_gate.append(st.mean(1.0 if x["gate_pass"] == "True" else 0.0 for x in sir) -
                                  st.mean(1.0 if x["gate_pass"] == "True" else 0.0 for x in base))
                lo, mu, hi = bootstrap_ci(d_cost)
                sig = "YES" if (lo > 0 or hi < 0) else "no"
                P(f"| {fam} | $/task diff (SIR−{b_arm}) N={N},Nc={N_conv} | µ$×1e6 | "
                  f"{lo*1e6:+.2f} | {mu*1e6:+.2f} | {hi*1e6:+.2f} | {sig} |")
                boot_summary[(fam, "cost", N)] = (lo, mu, hi)
                lo, mu, hi = bootstrap_ci(d_gate)
                sig = "YES (SIR>)" if lo > 0 else ("YES (SIR<)" if hi < 0 else "no")
                P(f"| {fam} | gate-success diff (pts) N/A | | {lo*100:+.1f} | {mu*100:+.1f} | "
                  f"{hi*100:+.1f} | {sig} |")
                boot_summary[(fam, "gate")] = (lo, mu, hi)
    P("")
    json.dump({"boot": {str(k): v for k, v in boot_summary.items()},
               "comparator": comp,
               "cells": {f"{a}|{f}": v for (a, f), v in agg.items()}},
              open(RES / "analysis_state.json", "w"), indent=1, default=float)
    (RES / "E1_RESULTS_part1.md").write_text("\n".join(lines))
    print("\n".join(lines[:30]))
    print("... part1 written:", RES / "E1_RESULTS_part1.md")

if __name__ == "__main__":
    main()
