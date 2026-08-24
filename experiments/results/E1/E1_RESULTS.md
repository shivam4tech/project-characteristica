# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)

> ## ⚠ HANDOFF NOTE — MATRIX NOT COMPLETE (2026-08-25 01:30 IST, WS-E1EXEC wait/analysis pass)
>
> - **State:** scored matrix INCOMPLETE. Primary stage at **72/600** outcomes since the 22:28 IST
>   restart (87 raw-output JSONs on disk across two passes; pace 0–19 items/h under z-ai/glm-5.2:free
>   shared-pool congestion). `outcomes.csv` has **0 rows**; repl/H2/F3 stages never started.
> - **Root cause found (evidence-based):** `runner.py` `emit()`→`_flush()` re-acquires the same
>   non-reentrant `threading.Lock` (L347-356) ⇒ chain deadlocks permanently at `BATCH_FLUSH=10`;
>   verified live (/proc: main thread futex-blocked, workers in socket poll). As frozen, the chain
>   can never write the CSV its own resume/analysis depends on. Full timeline, evidence, and the
>   Director decision menu (one-line RLock fix DEV-9; optional audited outcomes.csv rebuild from
>   raw_outputs JSONs to salvage ~87–159 completed items) are in `INTERRUPTION_LOG.md` #3.
> - **Verdicts:** none issued in this pass — no fixed-n data exist in analyzable form, and pre-reg
>   forbids inventing verdicts. All tables below are the untouched pre-registered SKELETON.
> - **Next steps:** 06:00 IST cron `characteristica-e1-analysis-resume` resumes supervision. After
>   the authorized fix (+ optional rebuild) and a clean `make_results` run on complete data, insert
>   the three prepared blocks from `E1_RESULTS_verdict_drafts.md` (mixed-batch header note; H3
>   reuse-gating verdict; H5 paraphrase N/A note), then update STATUS.md WS-E1EXEC.

**STATUS:** scored-run data collected under AMENDMENT-1 · analysis basis MEASUREMENT_PLAN §1.4 ONLY (§1.9 quarantined illustrative-only)

**Amended model pin (D-2 per Amendment-1, countersigned W0f' 2026-08-24):** `z-ai/glm-5.2:free` — **OpenRouter `:free` tier (is_free_tier=true)**, selected ONCE at run time as the highest-capability :free model verifiably serving (selection record in manifest.json; AA Intelligence Index ranking: glm-5.2=53 > inkling=41[harness-gated 403] > nemotron-ultra=38). Used identically for ALL arms incl. converter (D-4 preserved). Amendment reference: experiments/E1_AMENDMENT_1.md.

**Price vector (run date 2026-08-24, https://openrouter.ai/api/v1/models):** p_in=$0.00/M, p_out=$0.00/M (`:free` tier publishes $0/$0). Consequence declared BEFORE unblinding: §1.4 formulas are unchanged (amendment condition #5), so every $(N) and Δ(N) below is identically $0.000000 — **the dollar axis is degenerate under a zero price vector**; no $ comparison can show a detectable advantage or disadvantage (plan §4.5 ceiling applies a fortiori). Directional $ predictions are therefore evaluated as 'no detectable difference (degenerate instrument)', and token diagnostics are reported alongside as raw diagnostics.

> **Red Team flag P8 (model dependence): conclusions are provisionally scoped to the amended model family until a paid-model confirmation batch (E1b) replicates direction.**

**Power honesty (plan §4.5):** n=50/cell ⇒ only effects ≳15–20 F1 points interpretable; verdict language says "no detectable advantage", never "no advantage".
**Exclusions:** none. DEV-7 rule applied mechanically (both readings retained; latest non-transport-fail reading analyzed). Zero rows dropped.

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


## 4. F2 conversion-stage vs behavioral fidelity (stratified 20% sample, SIR arm)

| unit type | n | conversion-stage recovery | behavioral recovery |
|---|---|---|---|

_Note (CP instrumentation limit): CP gold constraints are internal ids checked against the emitted plan; leaf-value containment cannot attribute CP losses per unit type. CP F2 is therefore reported qualitatively via K_err/doc_valid/silent-error rather than per-unit._

## 5. H2 variance module (20 CP items x 5 reps @ T=0.7)

| arm | items | modal-answer agreement | outcome entropy (bits) | mean score |
|---|---|---|---|---|

## 6. Replication (H1 condition 3)

- Stochastic module (10 stratified items x 3 reps @ T=0.7, seeds 201–203), SIR vs strongest baseline:
- Item-split module (primary, 3 folds):

## 7. F3 round-trip stability

- F3 probe not run/empty.


## 8. Registered predictions — evaluated exactly as stated (pre-reg §6)

### P1 — EX: SIR vs strongest NL arm
- Conversion-stage F2 (EX, unit-weighted across audited types): **None** (condition-to-fire '>': F2 ≥ 0.90 → NOT FIRED)
- Insufficient data.
- $ @N=1 `<` and $ @N=25 `>` iff F2≥0.90: $ instrument degenerate (all $≡0) → **no detectable difference on the registered $ endpoint**; F1 side: n/a

### P2 — UNL-replay guard (fires iff EX conversion-stage F2 < 0.80)
- Condition: EX F2 < 0.80 → NOT FIRED

### P3 — Conversion-loss localization
- Per-type conversion-stage losses: entity_ref=—, exclusion=—, modality=—, preference_order=—, quantity_unit=—
- Insufficient audited coverage in the named classes to evaluate (see F2 table).

### P4 — H2 variance (CP module)
- H2 module data absent/not yet run.

### P5 — H4 silent errors (CP ↓ both NL arms; TU: NO significant SIR>JSON edge)
- Silent-error data incomplete.

### P6 — TU adversarial loss (SIR ≤ JSON in tool-use; contrary ⇒ mandatory red-team review)
- TU data incomplete.

### P7 — F3 round-trip stability (δ_F3=0.90; failures concentrate at unknown/branch nodes)
- F3 probe not run.

### H1 central gate (four conditions, per family) & H0 standing

- **H0 standing:** stands unless ≥1 family passes all four conditions — **H0 STANDS** (no family passes condition 1 on a degenerate $ instrument).

---
*Deviations ledger: DEVIATIONS.md DEV-1..DEV-8 (DEV-8 = Amendment-1 re-pin, pacing, checkpoint-resume; all pre-first-scored-call). Interruptions: INTERRUPTION_LOG.md.*