# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)

**Model pin (D-2):** `z-ai/glm-5.2:free` · tokenizer o200k_base (tiktoken; glm-5.2 server tokenizer approximated for F/V split only; authoritative counts are provider usage fields)
**Price vector:** p_in=$0.00/M, p_out=$0.00/M (retrieved 2026-08-24, https://openrouter.ai/api/v1/models; live re-check equal)
**Decisions:** D-1 oracle OMITTED (diagnostic loss acknowledged: representation-intrinsic vs converter-attributable causes NOT separable in E1) · D-3 paraphrase deferred to E2 · D-4 converter model = executor model
**Analysis basis:** benchmarks/MEASUREMENT_PLAN.md §1.4 formulas ONLY; §1.9 quarantined (illustrative-only). Bootstrap 10k, seed 20260824, paired item-level, two-sided α=.05.
**Power honesty (plan §4.5):** only effects ≳15–20 F1 pts or correspondingly large $ deltas are interpretable; verdict language respects this ceiling.

## 1. Cells: F0-gated F1 success rate, fidelity, latency (primary, T=0, n=50/family/arm)

| arm | family | n | F0 ok | **gate success %** | mean item score | silent-error % (F0∧¬gate) | K_err | doc valid | p95 ms |
|---|---|---|---|---|---|---|---|---|---|
| NL-plain | EX | 50 | 100% | **2.0** | 0.821 | 98.0 | 0% | 100% | 66305 |
| NL-opt | EX | 50 | 100% | **0.0** | 0.769 | 100.0 | 0% | 100% | 63331 |
| JSON | EX | 50 | 100% | **4.0** | 0.826 | 96.0 | 0% | 100% | 50098 |
| CSIR-SIR | EX | 50 | 88% | **0.0** | 0.082 | 100.0 | 98% | 2% | 218751 |
| NL-plain | CP | 50 | 100% | **18.0** | 0.309 | 82.0 | 0% | 100% | 120888 |
| NL-opt | CP | 50 | 100% | **18.0** | 0.285 | 82.0 | 0% | 100% | 112638 |
| JSON | CP | 50 | 84% | **66.0** | 0.805 | 21.4 | 0% | 100% | 256193 |
| CSIR-SIR | CP | 50 | 84% | **0.0** | 0.071 | 100.0 | 100% | 0% | 207309 |
| NL-plain | TU | 50 | 100% | **72.0** | 0.720 | 28.0 | 0% | 100% | 64725 |
| NL-opt | TU | 50 | 100% | **36.0** | 0.360 | 64.0 | 0% | 100% | 95472 |
| JSON | TU | 50 | 100% | **94.0** | 0.940 | 6.0 | 0% | 100% | 77363 |
| CSIR-SIR | TU | 50 | 94% | **0.0** | 0.000 | 100.0 | 100% | 0% | 305833 |

## 2. Net-of-overhead cost per arm×family, $(N) at N∈{1,10,25,100} (§1.4)

Comparator rule (fixed pre-reg §7): strongest baseline = highest gate success among {NL-plain, NL-opt, JSON}; ties → higher mean score → later listed. Result: EX→JSON, CP→JSON, TU→JSON

### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=1)

| family | baseline | Δ N=1 | Δ N=10 | Δ N=25 | Δ N=100 | $SIR N=1 | $SIR N=10 | $SIR N=25 | $SIR N=100 |
|---|---|---|---|---|---|---|---|---|---|
| EX | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |
| CP | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |
| TU | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |

### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=10) (PROJECTED scenario math — N_conv>1 not confirmatory)

| family | baseline | Δ N=1 | Δ N=10 | Δ N=25 | Δ N=100 | $SIR N=1 | $SIR N=10 | $SIR N=25 | $SIR N=100 |
|---|---|---|---|---|---|---|---|---|---|
| EX | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |
| CP | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |
| TU | JSON | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ | 0.0µ$ |

## 3. Paired item-level bootstrap — SIR vs strongest baseline (95% CI of difference)

| family | metric | comparator | lo | mean | hi | sig? |
|---|---|---|---|---|---|---|
| EX | $/task diff (SIR−JSON) N=1,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| EX | gate-success diff (pts) N/A | | -10.0 | -4.0 | +0.0 | no |
| EX | $/task diff (SIR−JSON) N=25,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| EX | gate-success diff (pts) N/A | | -10.0 | -4.0 | +0.0 | no |
| CP | $/task diff (SIR−JSON) N=1,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| CP | gate-success diff (pts) N/A | | -78.0 | -66.0 | -52.0 | YES (SIR<) |
| CP | $/task diff (SIR−JSON) N=25,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| CP | gate-success diff (pts) N/A | | -78.0 | -66.0 | -52.0 | YES (SIR<) |
| TU | $/task diff (SIR−JSON) N=1,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| TU | gate-success diff (pts) N/A | | -100.0 | -94.0 | -86.0 | YES (SIR<) |
| TU | $/task diff (SIR−JSON) N=25,Nc=1 | µ$×1e6 | +0.00 | +0.00 | +0.00 | no |
| TU | gate-success diff (pts) N/A | | -100.0 | -94.0 | -86.0 | YES (SIR<) |
