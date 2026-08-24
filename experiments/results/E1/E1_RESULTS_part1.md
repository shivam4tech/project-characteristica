# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)

**Model pin (D-2):** `z-ai/glm-5.2:free` · tokenizer o200k_base (tiktoken; glm-5.2 server tokenizer approximated for F/V split only; authoritative counts are provider usage fields)
**Price vector:** p_in=$0.00/M, p_out=$0.00/M (retrieved 2026-08-24, https://openrouter.ai/api/v1/models; live re-check equal)
**Decisions:** D-1 oracle OMITTED (diagnostic loss acknowledged: representation-intrinsic vs converter-attributable causes NOT separable in E1) · D-3 paraphrase deferred to E2 · D-4 converter model = executor model
**Analysis basis:** benchmarks/MEASUREMENT_PLAN.md §1.4 formulas ONLY; §1.9 quarantined (illustrative-only). Bootstrap 10k, seed 20260824, paired item-level, two-sided α=.05.
**Power honesty (plan §4.5):** only effects ≳15–20 F1 pts or correspondingly large $ deltas are interpretable; verdict language respects this ceiling.

## 1. Cells: F0-gated F1 success rate, fidelity, latency (primary, T=0, n=50/family/arm)

| arm | family | n | F0 ok | **gate success %** | mean item score | silent-error % (F0∧¬gate) | K_err | doc valid | p95 ms |
|---|---|---|---|---|---|---|---|---|---|

## 2. Net-of-overhead cost per arm×family, $(N) at N∈{1,10,25,100} (§1.4)

Comparator rule (fixed pre-reg §7): strongest baseline = highest gate success among {NL-plain, NL-opt, JSON}; ties → higher mean score → later listed. Result: 

### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=1)

| family | baseline | Δ N=1 | Δ N=10 | Δ N=25 | Δ N=100 | $SIR N=1 | $SIR N=10 | $SIR N=25 | $SIR N=100 |
|---|---|---|---|---|---|---|---|---|---|

### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=10) (PROJECTED scenario math — N_conv>1 not confirmatory)

| family | baseline | Δ N=1 | Δ N=10 | Δ N=25 | Δ N=100 | $SIR N=1 | $SIR N=10 | $SIR N=25 | $SIR N=100 |
|---|---|---|---|---|---|---|---|---|---|

## 3. Paired item-level bootstrap — SIR vs strongest baseline (95% CI of difference)

| family | metric | comparator | lo | mean | hi | sig? |
|---|---|---|---|---|---|---|
