# E1 RESULTS — FINAL (authoritative numbers)

**Status:** FINAL analysis on the frozen matrix. Supersedes `E1_RESULTS_INTERIM.md` (snapshot ~75% population); every overlapping number reconciled in §9.
**Data:** `outcomes.csv` (620 rows raw) + `h2_outcomes.csv` (370 rows raw), loaded 2026-08-25 (IST), single load, post-Amendment-2 ox-alpha matrix. Model: stealth/ox-alpha (D-2 as amended by Amendment-1 + Amendment-2); price vector p_in=p_out=$0/token (OpenRouter :free, retrieved 2026-08-24) → all $ figures are identically $0; decomposition reported in tokens per manifest policy. Formulas: MEASUREMENT_PLAN §1.4 ONLY (§1.9 quarantined, unused). δ_F1: EX/TU 3 pts, CP 4 pts; δ_F3=0.90; N-grid {1,10,25,100}; N_conv ∈ {1,10} (N_conv=1 honest primary).
**Repl stage:** COMPLETE 2026-08-26 (196 raw → 180 admitted: 2 arms {JSON, CSIR-SIR} × 3 families × 10 stratified items × 3 reps seeds 201–203, 8 duplicate TS keys deduped via latest-TS rule; 30 per arm·family; all TS post-cutoff) — **NOW INCLUDED via Cycle 1 addendum 2026-08-28** (see §7 row 1 & Addendum A). H2 variance: 370→300 as before. Rerun-SIR (Amendment-3, 8192 cap) frozen 70/150, fast-close — not folded into primary $/F1 (sensitivity note Addendum B).

---

## 1. Population & integrity

**Raw → admitted.** outcomes.csv carries 620 rows over 600 unique (arm × family × item) keys. The 20 surplus rows are 10 items × 2 extra attempts each (CSIR-SIR×EX: EX-04-01…06; NL-plain×TU: TU-01-00…05): every surplus row has `transport_fail=True` with empty latency/tokens (dispatch failures during a 03:03–03:09 IST window). Admission rule (logged here, applied uniformly): **keep the latest `transport_fail=False` row per key** → exactly **600 admitted rows**, 50 per cell × 12 cells. Both readings retained in the CSV per MEASUREMENT_PLAN §1.5; nothing dropped silently.

| Arm | EX | CP | TU | Total |
|---|---|---|---|---|
| NL-plain | 50 | 50 | 50 | 150 |
| NL-opt | 50 | 50 | 50 | 150 |
| JSON | 50 | 50 | 50 | 150 |
| CSIR-SIR | 50 | 50 | 50 | 150 |
| **Total** | **150** | **150** | **150** | **600** |

- **Exclusions:** 0 substantive. 20 transport-failed dispatches excluded by the rule above (their replacement attempts are admitted; zero scored data lost). No other exclusion invoked; no cell below the G1 gate (all 12 blocks 50/50 ≥ 80%).
- **Duplicates:** 10 triple-keyed items as above (intentional re-dispatch after transport failure, both failed readings logged). No duplicate rows within any admitted cell; every admitted row's raw file exists on disk (full 600-row sweep, 0 missing).
- **Amendment-2 compliance (G6):** all admitted ts ∈ [2026-08-25T01:32, 2026-08-25T05:22] IST, strictly after the 00:35 glm quarantine cutoff; zero pre-cutoff rows. Binding condition 1 (`model` field per record) remains **unverifiable — records carry no model field (anomaly A3, unresolved)**; admission rests on ts alone, as in the interim.
- **h2_outcomes.csv integrity:** 370 raw rows → registered design is 3 arms (NL-opt, JSON, CSIR-SIR) × 20 stratified CP items × 5 reps (seeds 101–105) @ T=0.7 = **300 rows**. Surplus = 70 partial duplicate rows confined to rep index 4 (NL-opt +20, JSON +24, CSIR-SIR +26 — consistent with a checkpoint/resume double-write during the quota-pause window). Dedupe rule: latest ts per (arm, item, rep) → **300 admitted rows**, verified unique on (arm,item,rep); all ts post-cutoff.
- **Fabrication screen (P4_PREP §2.4):** identical-latency collisions negligible (2, LOW, per interim A6); SIR same-template (v_in,v_out) collisions 15/150 rows (temp=0 coincidence, LOW, unchanged); v/f/k/r fields populated on all admitted rows; no score without attempts. No §2.4 escalation triggered.

---

## 2. Primary efficacy (F0-gated F1 score, T=0, n=50/cell)

Mean ± SD of item score (0–1 micro scale); cond. = mean over F0-valid rows; gate % = zero-hard-violation (CP) / gold-action-match (TU) / strict-gate pass.

| Arm | Family | n | Mean ± SD | Cond. mean | F0 fails | Gate-pass % |
|---|---|---|---|---|---|---|
| NL-plain | EX | 50 | 0.8214 ± 0.1680 | 0.8214 | 0 | 2 |
| NL-opt | EX | 50 | 0.7689 ± 0.2176 | 0.7689 | 0 | 0 |
| JSON | EX | 50 | 0.8255 ± 0.1228 | 0.8255 | 0 | 4 |
| CSIR-SIR | EX | 50 | 0.0822 ± 0.1182 | 0.0934 | 6 | 0 |
| NL-plain | CP | 50 | 0.3093 ± 0.3958 | 0.3093 | 0 | 18 |
| NL-opt | CP | 50 | 0.2848 ± 0.3838 | 0.2848 | 0 | 18 |
| JSON | CP | 50 | 0.8055 ± 0.3602 | 0.9589 | 8 | 66 |
| CSIR-SIR | CP | 50 | 0.0714 ± 0.1479 | 0.0850 | 8 | 0 |
| NL-plain | TU | 50 | 0.7200 ± 0.4536 | 0.7200 | 0 | 72 |
| NL-opt | TU | 50 | 0.3600 ± 0.4849 | 0.3600 | 0 | 36 |
| JSON | TU | 50 | 0.9400 ± 0.2399 | 0.9400 | 0 | 94 |
| CSIR-SIR | TU | 50 | 0.0000 ± 0.0000 | 0.0000 | 3 | 0 |

**Comparator (fixed rule, prereg §7):** strongest baseline = highest-F1 baseline arm per family from data → **JSON in all three families**. Paired deltas (arm − JSON), paired bootstrap 95% CI (10,000 resamples, seed 20260824), paired effect size dz:

| Comparison | EX ΔF1 [CI] (dz) | CP ΔF1 [CI] (dz) | TU ΔF1 [CI] (dz) |
|---|---|---|---|
| CSIR-SIR − JSON | **−0.743** [−0.785, −0.699] (dz −4.73) | **−0.734** [−0.835, −0.626] (dz −1.96) | **−0.940** [−1.000, −0.860] (dz −3.92) |
| NL-opt − JSON | −0.057 [−0.123, +0.001] (dz −0.25) | −0.521 [−0.640, −0.400] (dz −1.19) | −0.580 [−0.740, −0.400] (dz −0.95) |
| NL-plain − JSON | −0.004 [−0.068, +0.049] (dz −0.02) | −0.496 [−0.615, −0.376] (dz −1.13) | −0.220 [−0.360, −0.080] (dz −0.40) |

- Every SIR deficit is 4–6× beyond the §4.5 power ceiling (≳15–20 pts). SIR TU is **0.000 on all 50 items** (no nonzero score).
- Sensitivity: dropping the 11 checker-exception cells (8 CP, 3 TU — string-typed artifacts scored 0.0/F0-fail, honest rows) moves SIR CP 0.0714→0.0850 (n=42), SIR TU stays 0.000 (n=47). Direction unaffected.
- Straw-man inversion persists in final data (interim A4): NL-plain > NL-opt on EX (+5.3 pts) and TU (+36 pts); template-driven. Reported, never compared-against alone.

## 3. Cost (MEASUREMENT_PLAN §1.4 formulas; price vector $0/$0 ⇒ all $ figures identically $0.00/token-space decomposition)

Per-arm means over 150 admitted tasks (tokens; tokenizer o200k_base approximation per manifest). R = executor retry tokens (E[R] actual); K = converter in+out+repair tokens charged per-item (honest primary N_conv=1). A(N) = V_in + V_out + E[R] + F/N (+K for SIR, per task definition of this section).

| Arm | V_in | V_out | F | R | K | K_reinj | A(1) | A(10) | A(25) | A(100) |
|---|---|---|---|---|---|---|---|---|---|---|
| NL-plain | 274 | 1349 | 85 | 0 | 0 | 0 | 1708 | 1632 | 1627 | 1624 |
| NL-opt | 281 | 1615 | 449 | 0 | 0 | 0 | 2345 | 1941 | 1914 | 1901 |
| JSON | 274 | 861 | 389 | 386 | 0 | 0 | 1910 | 1560 | 1536 | 1525 |
| CSIR-SIR | 206 | 292 | 295 | 374 | **11112** | **7408 (66.7%)** | **12280** | **12014** | **11997** | **11988** |

- Retry load is real and asymmetric: items with executor retries JSON 12/150, CSIR-SIR 54/150, NL arms 0/150.
- **Explicit no-break-even demo (SIR):** Δ(N) = $(N)_B − Total_SIR(N, N_conv=1) < 0 at **every** N ∈ {1,10,25,100} × every pairing × every family. Range −9002 … −11530 tok/task. Worst case for baselines (N→∞, F fully amortized): SIR end-to-end floor = V_in+V_out+E[R]+K ≈ 11,988 tok vs best baseline 1,525 (JSON) → Δ(∞) ≈ **−10,463**. **No break-even N\* exists on the registered grid — or anywhere — while K_conv ≈ 11.1k tok/item stands**, because K alone exceeds any baseline's entire per-task cost by ~7×. The dominant term inside K is **K_reinj = 7408 tok (66.7%)**: converter *repair* traffic (`n_conv_attempts=3` on 149/150 items; first-shot conversion succeeded 1/150; `conv_errors='json:no JSON object found'`). SIR's executor-side payload is actually the cheapest (exec-side A(N)=1167→875) — the loss is entirely conversion-stage.
- Conditional (per gate-passed successful task) totals, tokens: NL-plain 46 succ → 5,570; NL-opt 27 → 13,030; JSON 82 → 3,493; **CSIR-SIR 0 successes → undefined (∞)**.
- PROJECTED, NON-CONFIRMATORY (K/N_conv scenario math, prereg §3.2): break-even N_conv ≈ **11** vs NL-opt, 15 vs NL-plain, 18 vs JSON @N=25. Labeled PROJECTED wherever printed; supports no claim.

## 4. Latency (end-to-end wall clock, ms, includes SIR conversion stage; n=150/arm)

| Arm | p50 | p90 | p95 | max |
|---|---|---|---|---|
| NL-plain | 40,692 | 84,097 | 91,714 | 138,516 |
| NL-opt | 59,419 | 96,792 | 107,079 | 138,032 |
| JSON | 29,435 | 78,357 | **209,608** | 275,289 |
| CSIR-SIR | **17,178** | **35,617** | **45,289** | 117,915 |

The registered §6.1 directional row (SIR p95 `>` all baselines, serial-conversion surcharge) is **INVERTED** in final data: SIR is fastest at p50/p90/p95 (short executor outputs, V_out 292 vs 861–1615, outweigh the added hop). JSON owns the worst tail (p95 209.6 s — retry/truncation loops). Queue-anomaly screen (>3× median re-run rule): no arm median exceeded; JSON tail driven by its own retries (logged, kept per §1.5).

## 5. H2 variance module (h2_outcomes.csv; CP strata, T=0.7, seeds 101–105)

Integrity: 370 raw rows → 300 registered (3 arms × 20 stratified CP items × 5 reps) after dedupe (latest ts per arm×item×rep; 70 surplus rep-4 rows from a checkpoint/resume double-write, 17 with differing scores — rule logged). All ts post-quarantine-cutoff.

| Arm | Grand mean | Mean within-item SD (across 5 reps) | Pooled SD | SD of rep-means | Modal gate-pass agreement |
|---|---|---|---|---|---|
| NL-opt | 0.3231 | 0.1442 | 0.3997 | 0.0762 | 92.0% |
| JSON | 0.8383 | 0.1192 | 0.3311 | 0.0271 | 84.0% |
| CSIR-SIR | 0.0857 | **0.0000** | 0.1723 | **0.0000** | 100.0% |

**Does structured form reduce variance?** Nominal ordering: SIR 0.000 < JSON 0.119 < NL-opt 0.144 (within-item SD). But SIR's zero dispersion is **degenerate**: every item scored **identically across its 5 reps** (within-item SD = 0 on all 20 items; modal gate agreement trivially 100%) while sitting at floor level (grand mean 0.086 — most items constantly wrong, a few constantly partially right). Stability-at-failure, not stability-at-parity. The registered prediction P4/H2 requires dispersion comparison **at comparable mean F1**; grand means are 0.086 / 0.323 / 0.838 — the precondition fails catastrophically, so the registered test cannot be run (see §7 verdict: NOT-EVALUABLE, degenerate). Dedupe sensitivity: repeating the module with earliest-ts (instead of latest-ts) duplicate resolution gives within-item SDs 0.194 / 0.289 / 0.038 and means 0.293 / 0.742 / 0.069 (NL-opt / JSON / SIR) — ordering, precondition failure, and verdict unchanged. Secondary observation: JSON disperses less than NL-opt on every statistic — generic structuring does reduce run-to-run variance, which under the registry's own criterion would push H2 toward "weakened (attributed to generic structuring)" even had means matched. Agreement-gap detectability (≥15 pts registered): SIR−NL-opt gap 8.0 pts — below threshold even before degeneracy discount.

## 6. Fidelity — F0 format-validity pass rates

| Arm | EX | CP | TU | Total (/150) |
|---|---|---|---|---|
| NL-plain | 100% (50/50) | 100% (50/50) | 100% (50/50) | **100%** |
| NL-opt | 100% (50/50) | 100% (50/50) | 100% (50/50) | **100%** |
| JSON | 100% (50/50) | 84% (42/50) | 100% (50/50) | **94.7%** |
| CSIR-SIR | 88% (44/50) | 84% (42/50) | 94% (47/50) | **88.7%** |

- JSON's 8 F0 fails are all CP-01/CP-02 parse truncations ("no JSON object found"), source of its R=386 load (interim A5 confirmed on final data).
- SIR converter-stage validity (separate from answer-artifact F0): **valid CSIR documents 1/150 (0.7%)**; `kerr_flag=True` 149/150; `n_conv_attempts=3` 149/150; `conv_errors='json:no JSON object found'` 149/150. K_err ≈ **99.3%** — the converter essentially never emitted a schema-valid document, and the failure is loudly flagged (not silently absorbed).
- Checker-exception cells: 11 (8 SIR-CP, 3 SIR-TU), auto-scored 0.0/F0-fail — string-typed artifacts where dicts expected (answer-artifact contract breach, interim A2 confirmed).
- F2/F3 instruments remain **absent**: `f2_audit.json` = `{"f2_rates": {}, "f2_unknown": {}}`; conversions.csv not present. F2/F3-dependent evaluations are therefore NOT-EVALUABLE (§7).

## 7. VERDICT TABLE — the seven registered predictions (prereg §6.2, evaluated exactly as stated per Amendments 1–2; falsification conditions quoted verbatim)

| # | Prediction (registered wording of the falsification/decision condition, verbatim) | Final numbers | Verdict |
|---|---|---|---|
| 1 | **H1 (central):** "support in a family requires ALL FOUR plan §4.4 conditions: (1) SIR beats the strongest baseline arm … on $/task with paired-bootstrap 95% CI excluding zero; (2) F1 non-inferiority within δ_F1; (3) replication (§8); (4) red-team survival (P4 phase). Any failure ⇒ no H1 support from that family." δ_F1 = 3/4/3 pts (EX/CP/TU) | (1) FAILS: prices $0/$0 ⇒ $/task ≡ $0.00 all arms, Δ$=0, no beat, CI includes 0 by construction (token-space diagnostic: SIR worse by 9.0–11.5k tok at every N, CI excl. 0 the wrong way). (2) FAILS in all 3 families: deficits 74.3 / 73.4 / 94.0 pts vs margins 3 / 4 / 3. (3) EVALUATED via repl: stochastic module (SIR vs JSON, 10 items×3 reps @T0.7 seeds 201–203) fold gate-deltas CP [−0.8,−1.0,−0.7] sign-consistent **True**, TU [−1.0,−0.9,−1.0] **True**, EX [−0.1,0.0,0.0] **False**; item-split (primary, 3 folds) CP True, TU True, EX False — replication therefore **passes for CP/TU, fails for EX**; overall moot because (1)(2) already fail. (4) pending red-team (P4, Cycle 4). | **NO H1 SUPPORT — all three families fail** (conditions 1–2 decisively; (3) would pass for CP/TU, fail for EX — see Addendum A) |
| 2 | **H3 (efficiency axis):** "Falsification (registry H3): (a) Δ(N) ≤ 0 at every declared N, or (b) Δ(1) > 0, or (c) no significant N×arm interaction — any of these falsifies H3 as registered." | Δ(N) < 0 at every N ∈ {1,10,25,100} × every baseline pairing × every family (−9002…−11530 tok; $-space Δ≡0). Falsifier **(a)** fires on its own. Monotone-improvement clause also violated (Δ grows more negative with N vs NL-opt and JSON). | **FALSIFIED** (via registered falsifier (a)) |
| 3 | **P2 (UNL-replay guard):** "if conversion-stage F2 < 0.80 on EX, predicted Δ(N) < 0 at every N; registered NOW so the failure, if observed, is diagnostic" | Antecedent **unmeasured**: F2 audit empty ({}), conversion-stage F2 never computed. Consequent (Δ<0 ∀N) observed true. | **NOT-EVALUABLE** (instrument missing; consequent consistent) |
| 4 | **P3 (conversion-loss localization):** "predicted F2 conversion-stage unit losses concentrate in `modality`, `preference_order`, `exclusion` — NOT in `entity_ref`/`quantity_unit`. … Falsified if loss concentrates in the 'easy' unit classes instead." | Per-unit-type recovery rates require the F2 audit — absent. No proxy permitted by registration. | **NOT-EVALUABLE** (instrument missing) |
| 5 | **P5/H4 (silent-error guide-rail):** "predicted: silent-error fraction (validation-passed but F1-failed) SIR < both NL arms in CP; NO significant SIR-over-JSON silent-error advantage in TU … Falsified per registry: reduction absent, fully explained by JSON arm, or bought below δ_F1." | CP validation-passed ∧ gate-fail: NL-plain 41/50 (82%), NL-opt 41/50 (82%), JSON 17/50 (34%), SIR 0/50 **by degeneration** — SIR's validator rejects 149/150 documents (valid-doc denominator ≈ 1) while F1 = 0.071. The nominal SIR "reduction" is bought by total rejection + F1 collapse 74 pts > δ_F1=4 ⇒ falsifier clauses 2 and 3 both fire; the observed reduction is fully explained by the JSON arm (34%). TU side: no SIR-over-JSON advantage exists (consistent with registered null). | **FALSIFIED** (reduction explained by JSON arm; bought below δ_F1; degenerate validator behavior) |
| 6 | **P4/H2 (variance):** "predicted SIR run-to-run dispersion < both NL arms **at comparable mean F1**; partial survival required vs JSON arm — if SIR ≈ JSON dispersion, the effect is attributed to generic structuring and H2 is recorded as weakened … Detectable: agreement-rate gaps ≥ 15 points." | Within-item SD: SIR 0.000 < JSON 0.119 < NL-opt 0.144; but grand means 0.086 / 0.838 / 0.323 — comparable-mean precondition fails catastrophically (SIR all-zero reps, degenerate stability). Agreement gap SIR−NL-opt = 8 pts < 15. JSON disperses less than NL-opt (would weaken H2 to "generic structuring" even at matched means). | **NOT-EVALUABLE** (registered precondition — comparable mean F1 — unmet; raw ordering degenerate) |
| 7 | **P7/F3:** "SIR F3 ≥ 0.90 with failures concentrated at unknown/branch nodes. Falsified if F3 < 0.90 or failures distribute uniformly." (δ_F3 = 0.90) | Canonical round-trip equality never computed; conversions.csv absent; no F3 artifact. With K_err ≈ 99.3% there are ~no valid documents to round-trip. | **NOT-EVALUABLE** (instrument missing; no valid documents to test) |

**Supplementary registered directional rows (§6.1), for completeness:**

| Row | Registered | Observed | Verdict |
|---|---|---|---|
| P6 TU adversarial (G5-verbatim): "TU: SIR vs JSON **`<`** — registered adversarial loss (P6); contrary result triggers mandatory red-team review before any claim" | SIR `<` JSON | SIR 0.000 (0/50 nonzero) vs JSON 0.940; Δ −0.940 [−1.000, −0.860] | **CONFIRMED, stronger than registered** — mandatory red-team review triggered |
| EX SIR-vs-strongest-NL F1: "`>` iff measured conversion-stage F2 ≥ 0.90; else `≈` or `<`" | conditional | 0.082 vs JSON 0.826 (also vs NL-plain 0.821) — `<`; antecedent unmeasured | Against (unconditional `<`) |
| Latency §6.1: SIR p95 `>` baselines | serial-conversion surcharge | SIR 45.3 s p95 vs 91.7–209.6 s | **INVERTED** |

**H0 disposition:** "H0 stands unless ≥1 family passes all four" H1 conditions. Zero families pass one condition, let alone four ⇒ **H0 NOT rejected — stands, favored**. Per §4.5 verdict-language rule: CSIR/SIR shows *no detectable advantage* at CE-01 scale on any registered endpoint in any family; on F1 and end-to-end tokens it is strictly dominated by JSON in all three families (and by every baseline on end-to-end cost at every N). Single-model scope: all conclusions provisionally scoped to stealth/ox-alpha (Amendment-1 P8 / Amendment-2 condition 2).

## 8. Anomaly A1 — cross-reference

Root-cause analysis of the converter-telemetry anomaly lives in **`critiques/A1_ROOT_CAUSE.md`** (owned there; deliberately NOT root-caused in this document). Note for that doc's owner: its current anomaly statement mirrors the *interim* snapshot ("`conv_errors=[]`, `kerr_flag=False`, `doc_valid=True` on all 143"); the **final matrix supersedes this** — telemetry is now internally consistent (`n_conv_attempts=3` ⟺ `kerr_flag=True` ⟺ `doc_valid=False` ⟺ `conv_errors='json:no JSON object found'`, 149/150; single clean conversion 1/150). What needs explaining has shifted from "flags contradict attempts" to "why did first-shot conversion fail ~always, and why did interim rows carry clean flags".

## 9. Reconciliation with E1_RESULTS_INTERIM.md

| Quantity | Interim (~75%) | FINAL | Status |
|---|---|---|---|
| Admitted primary rows | 593/600 (SIR-CP 43) | **600/600** | resolved |
| 11 complete cells, means | e.g. NL-plain EX .821, JSON CP .805, JSON TU .940, SIR EX .082, SIR TU .000 | identical to ±0.001 | ✅ reconcile |
| SIR-CP mean | 0.083 (n=43) | **0.0714 (n=50)** | expected completion shift — cell was filling |
| SIR cost K / A(1) | 11,110 / 12,302 (n=143) | **11,112 / 12,280** (n=150) | ✅ to rounding |
| PROJECTED K-amort break-even vs NL-opt | N_conv ≈ 9–10 | **N_conv ≈ 11** | ⚠️ shifted with full matrix; still non-confirmatory |
| JSON p95 latency | 203,569 ms | **209,608 ms** | minor admission-set shift |
| **SIR converter telemetry** | `doc_valid=True`, `kerr_flag=False`, `conv_errors` empty on all analyzed rows (A1 "self-contradiction") | **`doc_valid=False`, `kerr_flag=True`, `conv_errors='json:no JSON object found'` on 149/150** | 🚨 **LOUD FLAG — materially reversed.** Interim A1 as stated is void; the interim H4 proxy ("docs validate 100%") is inverted. Final columns are self-consistent. See §8. |
| Interim H4 proxy read | "silent-error rate near-maximal for SIR (validates 100%, scores .08)" | SIR validates 0.7% ⇒ silent-error fraction degenerate/undefined; P5 falsified on registry clauses (see §7 #5) | superseded by above |
| Brief/context header said "602 primary rows COMPLETE" | — | file carries 620 rows / **600 unique admitted** | noted; 600 is authoritative |

*Final analysis subagent (ox-alpha), 2026-08-25 IST. Computed directly from outcomes.csv + h2_outcomes.csv (admission/dedupe rules in §1); manifest.json (prices, δ, seeds); E1_PRE_REGISTRATION.md §6–7 verbatim; MEASUREMENT_PLAN §1.4 only; P4_PREP §2 screens. Bootstrap seed 20260824, 10k resamples. Repl stage 2026-08-26: 196→180 admitted, now included — see Addendum A (Cycle 1, 2026-08-28). Rerun-SIR frozen 70/150 fast-close — not in primary; see Addendum B.*

---
## Addendum A — Cycle 1 (2026-08-28 15:32 IST): Repl integration
- **Source:** `repl_outcomes.csv` 196 raw → 180 admitted via DEV-7 latest-TS rule (8 duplicate keys: 3 copies each, all TU-related checkpoint double-writes; latest TS kept). All 6 arm·family cells 30/30 (2 arms ×3 families ×10 items ×3 reps @T0.7 seeds 201–203, post-cutoff).
- **Stochastic replication (plan §8, SIR vs JSON):** fold gate-deltas (Δ=SIR−JSON, gate %/100) —
  - CP: [−0.8, −1.0, −0.7] sign-consistent **True** (direction −)
  - TU: [−1.0, −0.9, −1.0] **True** (−)
  - EX: [−0.1, 0.0, 0.0] **False** (two zero folds break consistency per strict rule)
- **Item-split (3 folds on primary gate deltas, SIR vs JSON):** CP [−0.6875,−0.625,−0.625] True, TU [−0.9375,−0.875,−1.0] True, EX [0.0,−0.0625,−0.0625] False
- **H1 condition 3 reading:** passes for CP/TU, fails for EX; overall moot because conditions (1)(2) already fail decisively in all families, so H1 remains **NO SUPPORT**. H0 still stands.
- **F2 note:** `f2_audit.json` now populated (Cycle 1 run) — all conv 0.00 / beh 0.00 except `quantity_unit` beh 0.11; still supports §7 P2/P3 NOT-EVALUABLE (no per-unit recovery to localize).

## Addendum B — Amendment-3 rerun status
- `rerun_sir_outcomes.csv` 70 rows (header+70, 8192 cap) — identical failure mode `json:no JSON object found` (K≈11k unchanged). Fast-close decision per coordinator: frozen, not folded into primary, sensitivity note only. No break-even at any N; converter budget sensitivity finding stands.
