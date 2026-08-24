# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)

**STATUS:** SNAPSHOT ANALYSIS under AMENDMENT-2 (countersigned W0f″, 2026-08-25 ~00:45 IST) · matrix **mid-flight** at snapshot 2026-08-25 01:26 IST · analysis basis MEASUREMENT_PLAN §1.4 ONLY (§1.9 quarantined illustrative-only) · superseded skeleton replaced; handoff/ops history lives in `INTERRUPTION_LOG.md` #3

**Model pin (Amendment-2 D-2′, supersedes Amendment-1 D-2):** PRIMARY = **`stealth/ox-alpha`** (uniform re-pin after operator key reset ~22:00 IST restored its quota; live probe 00:40 IST serving, cost=0). All remaining scored cells execute on this pin. The earlier `z-ai/glm-5.2:free` pilot set is QUARANTINED to `glm_pilot_appendix/`, not merged into any per-arm comparison.

> **Red Team flag P8 (model dependence) — EXTENDED per Amendment-2 condition 2:** conclusions are provisionally scoped to the amended model family until a paid-model confirmation batch (E1b) replicates direction. **Two models were used across the expedition:** `z-ai/glm-5.2:free` (pilot cells, quarantined) and `stealth/ox-alpha` (primary population). No cross-model agreement check is possible (see Appendix caveat — glm scored payloads were destroyed by in-place overwrites before quarantine).

**Amendment references:** experiments/E1_AMENDMENT_1.md (W0f' 2026-08-24, original :free re-pin, pacing/resume infrastructure) · experiments/E1_AMENDMENT_2.md (W0f″ 2026-08-25, uniform re-pin to `stealth/ox-alpha`, quarantine rule). Manifest.json predates Amendment-2: its `model_id` line is STALE and was not used for per-cell attribution.

**Per-cell model attribution method:** the frozen runner schema carries no `"model"` field in outcome records (Amendment-2 condition 1's marker is unimplementable post-hoc), so the operator-directed mtime rule was applied: raw_outputs cells with mtime ≥ 2026-08-25 00:35 IST = ox-alpha primary population; older = glm-5.2 pilot. The ambiguous window [00:35, 00:45) contained **zero** files at snapshot ⇒ clean seam. Residual risk disclosed: pass-2 (glm) files were overwritten in place by pass-3 rather than archived; see Appendix caveat.

**Mixed-batch note (key reset):** scored calls span an operator API-key/quota reset (~22:00 IST 08-24) and the Amendment-2 re-pin seam (~00:44 IST 08-25). Within each model population, pre/post-reset calls are pooled with identical seeds (banks seed 20260824; H2 seeds {101–105}; repl seeds {201–203}), identical decoding (primary T=0), and unchanged harness logic across the seam; the reset is transport-class only (§8.1). Across the model seam, populations are NEVER pooled (Amendment-2 condition 1); the glm side is quarantined.

**Price vector:** p_in=$0.00/M, p_out=$0.00/M (re-pinned config retains :free-tier $0/$0, retrieval 2026-08-24). Consequence declared before unblinding: every $(N) and Δ(N) below is identically **$0.000000 — the dollar axis is degenerate**; no $ comparison can detect advantage/disadvantage. Directional $ predictions evaluate as 'no detectable difference (degenerate instrument)'; token diagnostics are the informative layer (plan §1.6 chars/task; §1.4 formulas unchanged per Amendment-1 condition #5, untouched by Amendment-2 condition 5).

**Exclusions:** none. DEV-7 rule applied mechanically (both readings retained; latest non-transport-fail reading per (arm,item,rep) analyzed; here n_attempts_mean=1.0, zero transport fails in the primary population).
**Power honesty (plan §4.5):** only effects ≳15–20 F1 points interpretable; verdict language says "no detectable advantage", never "no advantage". Snapshot n's below the registered n=50/cell are marked PARTIAL and cannot support or refute fixed-n predictions by themselves.

## ⚠ Operational finding affecting completion (full detail: INTERRUPTION_LOG.md #3)

`runner.py` `emit()`→`_flush()` re-acquires the same non-reentrant `threading.Lock` (L347–356): the chain deadlocks permanently once `BATCH_FLUSH=10` is reached — `outcomes.csv` is never written, downstream stages never start, and watchdog respawns re-run from scratch while overwriting prior-pass raw_outputs in place. Verified live (/proc thread states, 01:16 IST). Consequences for this document: analysis was computed directly from `raw_outputs/**.json` (each file carries the full outcome record); Director decision menu pending (RLock fix as DEV-9 candidate; CSV rebuild procedure). No protocol parameter is touched by this defect.

## 1. Cells: F0-gated F1 success rate, fidelity, latency (primary T=0; target n=50/family/arm)

| arm | family | n | F0 ok | gate success % | mean item score | silent-error % (F0∧¬gate) | K_err | doc valid | p95 ms |
|---|---|---|---|---|---|---|---|---|---|
| NL-plain | EX | 50 | 50 | **0.0** | 0.8171 | 100.0 | 0 | 50 | 64,240 |
| NL-opt | EX | 50 | 50 | **0.0** | 0.7357 | 100.0 | 0 | 50 | 63,737 |
| JSON | EX | 4 (PARTIAL) | 4 | **0.0** | 0.7678 | 100.0 | 0 | 4 | 36,731 |
| CSIR-SIR | EX | 0 | — | — | — | — | — | — | — |
| *all arms* | *CP* | *0* | — | — | — | — | — | — | — |
| *all arms* | *TU* | *0* | — | — | — | — | — | — | — |

**Observed pattern (descriptive, both completed EX cells):** 100% of items are F0-valid yet fail the zero-hard-violation gate with mean item score ≈0.74–0.82 — i.e., ox-alpha emits well-formed plans that satisfy most constraints but carry ≥1 hard-constraint violation on essentially every EX item, identically across representation formats. Empty `final_error` throughout (no parse failures). This uniformity across arms is itself format-independent and is the single most load-bearing observation in the snapshot.

## 2. Net-of-overhead cost per arm×family, $(N) at N∈{1,10,25,100} (§1.4)

With p≡($0,$0): **$(N) ≡ $0.000000 for every arm×family and every N; Δ(N) ≡ $0.000000; no break-even N\* exists (Δ never > 0)** — reported as-is per the pre-declared degeneracy clause. Token-amortization diagnostics A(N) = V_in + V_out + E[R] + F/N (tokens; R=repair retries E[R]=0 in snapshot):

| arm.family | V_in | V_out | E[R] | F | A(1) | A(10) | A(25) | A(100) |
|---|---|---|---|---|---|---|---|---|
| NL-plain.EX | 280.5 | 952.9 | 0.0 | 85 | 1318.4 | 1241.9 | 1233.8 | 1229.4 |
| NL-opt.EX | 287.5 | 1335.5 | 0.0 | 449 | 2072.0 | 1667.4 | 1640.4 | 1627.5 |
| JSON.EX (PARTIAL n=4) | 262.8 | 993.8 | 0.0 | 389 | 1645.6 | 1294.7 | 1271.9 | 1260.7 |

SIR-side Total_SIR(N, N_conv) and converter decomposition (K, F_conv) not computable — CSIR-SIR cells had not been reached by pass-3 at snapshot.

### Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=1)
≡ $0.000000 for all families, all N (degenerate instrument). Token-level Δ(N) deferred until SIR cells exist.

### Δ(N) at N_conv=10 (PROJECTED scenario math — not confirmatory)
Not computed: requires SIR converter cells (absent).

## 3. Paired item-level bootstrap — SIR vs strongest baseline (95% CI of difference)

Not computable: no CSIR-SIR cell data exist in the primary population at snapshot. Comparator rule (pre-reg §7) applied mechanically to available baselines for EX: gate-success tie (0.0 = 0.0) → higher mean score → **NL-plain (0.8171)** designated strongest baseline for EX. Straw-man-guard caveat (pre-reg §6.1): NL-plain is reported, and this designation is an artifact of a three-way tie at zero, not evidence NL-plain is strongest.

## 4. F2 conversion-stage vs behavioral fidelity (stratified 20% sample, SIR arm)

Not run: requires CSIR-SIR cells + F2 audit (`f2_audit.json` empty). No conversion-stage rates exist for either model population.

## 5. H2 variance module (20 CP items × 5 reps @ T=0.7, seeds 101–105)

Not run (`h2_outcomes.csv` absent; stage never launched due to ops finding).

## 6. Replication (H1 condition 3)

Stochastic module (10 items × 3 reps @ T=0.7, seeds 201–203) and 3-fold item-split: **not run** (`repl_outcomes.csv` absent).

## 7. F3 round-trip stability

**Not run** (`f3.csv` absent; stage never launched).

## 8. Registered predictions — evaluated EXACTLY as stated (pre-reg §6) on the ox-alpha primary population

### P1 — EX: SIR vs strongest NL arm
- Conversion-stage F2 (EX): **unmeasured** → firing condition 'F2 ≥ 0.90' **NOT MET (cannot fire)**.
- Observed SIR-vs-baseline gate comparison: **not computable** (no SIR cell). $ @N=1 `<` and $ @N=25 `>` iff F2≥0.90: $ instrument degenerate (all $≡0) → no detectable difference on the registered $ endpoint; F1 side: n/a.
- Verdict: **NOT EVALUABLE AT SNAPSHOT** (SIR cell absent; matrix mid-flight).

### P2 — UNL-replay guard (fires iff EX conversion-stage F2 < 0.80)
- Condition unmeasurable (no F2 audit) → **CANNOT FIRE**; recorded as not evaluable, diagnostic value nil at snapshot.

### P3 — Conversion-loss localization
- Per-type losses: entity_ref=—, exclusion=—, modality=—, preference_order=—, quantity_unit=— (no F2 audit).
- Verdict: **NOT EVALUABLE AT SNAPSHOT.**

### P4 — H2 variance (CP module)
- Module data absent → **NOT EVALUABLE AT SNAPSHOT** (registered weakening criterion inapplicable without dispersion data).

### P5 — H4 silent errors (CP: SIR < both NL arms; TU: NO significant SIR>JSON edge)
- CP/TU cells absent → registered comparison **not evaluable**.
- Descriptive EX-side observation (not a registered endpoint): silent-error fraction is 100% in every armed cell examined — validation passes while the hard-constraint gate fails everywhere — so at snapshot there is **no detectable guide-rail reduction in ANY arm**, the pattern H4 predicts should differentiate arms. Recorded as diagnostic only.

### P6 — TU adversarial loss (SIR ≤ JSON; contrary ⇒ mandatory red-team review)
- No TU cell exists for any arm at snapshot → the predicted loss is **NEITHER CONFIRMED NOR CONTRARY — NOT EVALUABLE**. Reported honestly: no TU data were collected on the primary model by snapshot time; no red-team review is triggered (contrary result absent).

### P7 — F3 round-trip stability (δ_F3=0.90; failures concentrated at unknown/branch nodes)
- F3 probe not run → **NOT EVALUABLE AT SNAPSHOT.**

### H3 — reuse-gating (primary efficiency axis; falsification conditions verbatim, pre-reg §6.2)
- (a) "Δ(N) ≤ 0 at every declared N": arithmetically **SATISFIED** — Δ(N) ≡ $0 ≤ 0 at N∈{1,10,25,100} under the zero price vector.
- (b) "Δ(1) > 0": **not observed** ($0).
- (c) "no significant N×arm interaction": **untestable** on an all-zero instrument.
- Verdict: **FALSIFIED AS REGISTERED on the $ endpoint** (condition (a) holds as stated). Scope caveat: falsification-by-instrument ("no detectable gain" under a degenerate $ axis), NOT affirmative evidence reuse gains are absent; token A(N) diagnostics above carry the object into E1b.

### H4 — silent-error guide-rail (registry criteria: reduction absent / fully explained by JSON / bought below δ_F1)
- Registered CP/TU comparisons unmeasurable at snapshot → **NOT EVALUABLE**; the descriptive EX pattern (above) shows no arm differentiation, consistent with — but not sufficient for — the registry's "reduction absent" branch once CP/TU data exist.

### H5 — paraphrase robustness: **N/A IN E1 BY DESIGN**
- D-3 (registered pre-run) defers the paraphrase arm to E2; Amendment-2 changes nothing here. Not evaluable; no verdict issued; E2 inherits the prediction unchanged.

### H1 central gate (four conditions, per family) & H0 standing
- **EX** (comparator NL-plain by mechanical tie-break): (1) efficiency CI excluding zero — impossible in $ terms (degenerate instrument) AND no SIR data; (2) F1 non-inferiority δ_F1(EX)=3.0 — no SIR cell; (3) replication — not run; (4) red-team survival — P4 phase not reached. → **H1 support NOT achieved in EX.**
- **CP, TU**: no primary data → all four conditions unevaluated → **H1 support NOT achieved.**
- **H0 standing:** stands unless ≥1 family passes all four conditions — **H0 STANDS** (no family can pass condition 1 on the degenerate $ instrument; independently, no SIR data exist at snapshot).

---

## Appendix A — glm-5.2 pilot quarantine (`glm_pilot_appendix/`)

Per Amendment-2, all cells scored on `z-ai/glm-5.2:free` belong to a quarantined pilot-replication set, excluded from every primary statistic above. Index: `glm_pilot_appendix/index.md`.

**Material disclosure (overwrites):** the frozen runner writes each item's raw record to a deterministic path and re-writes it in place on every pass, keeping no version history. Pass-1/pass-2 (glm-scored, ~87 and ~72 outcomes respectively) were progressively overwritten by pass-3 (ox-alpha, from 00:44 IST). At preservation time (01:24 IST) only **4 pre-pass-3 files survived** — all from the UNSCORED 17:22 smoke era (3 transport-fail records + 1 CSIR-SIR smoke record) — preserved verbatim under `glm_pilot_appendix/raw/`. **The glm-5.2 scored pilot payloads are therefore unrecoverable**; the quarantine set survives only as aggregate metadata (counts, pace buckets, timestamps) recorded in INTERRUPTION_LOG #3. Consequently the Amendment-2 condition-2 robustness check (glm-vs-ox-alpha agreement on overlapping cells) is **impossible**, and P8 scoping rests solely on the ox-alpha population.

---
*Deviations ledger: DEVIATIONS.md DEV-1..DEV-8 (all pre-first-scored-call) + proposed DEV-9 (runner flush-deadlock repair — awaiting Director authorization; INTERRUPTION_LOG #3). Interruptions: INTERRUPTION_LOG.md #1–#3. Amendments: E1_AMENDMENT_1.md, E1_AMENDMENT_2.md.*
