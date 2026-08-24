# E1 RESULTS — INTERIM

**INTERIM — ~75% population, not final.**

*Snapshot 2026-08-25 ~05:15 IST: **593/600 primary cells admitted** (single load; ox-alpha-only per Amendment-2, mtime >= 2026-08-25 00:35 IST). Runner is STILL writing CSIR-SIR x CP (cell count moved 31->36->39 during this session) — every number here is provisional and MUST be regenerated on the frozen matrix.*

*Deviation noted up front: outcome records carry **no `model` field**, so Amendment-2 binding condition 1 cannot be literally verified; admission rests on mtime+ts alone (zero pre-cutoff files found under raw_outputs/). Anomaly A3.*

---

## 1. Population audit (raw_outputs mtimes vs G1 go-gate)

| Arm | Family | Cells | Completion | G1 gate (>=40/50 = 80%) |
|---|---|---|---|---|
| NL-plain | EX | 50/50 | 100% | PASS |
| NL-opt | EX | 50/50 | 100% | PASS |
| JSON | EX | 50/50 | 100% | PASS |
| CSIR-SIR | EX | 50/50 | 100% | PASS |
| NL-plain | CP | 50/50 | 100% | PASS |
| NL-opt | CP | 50/50 | 100% | PASS |
| JSON | CP | 50/50 | 100% | PASS |
| CSIR-SIR | CP | 43/50 | 86% | PASS |
| NL-plain | TU | 50/50 | 100% | PASS |
| NL-opt | TU | 50/50 | 100% | PASS |
| JSON | TU | 50/50 | 100% | PASS |
| CSIR-SIR | TU | 50/50 | 100% | PASS |
| **Total** | | **593/600** | 99% | **12/12 PASS at snapshot** (CSIR-SIR x CP reached 43/50=86% during this session; it sat BELOW the gate through most of the interim window — re-verify on frozen matrix, 7 cells outstanding) |

- Zero quarantined glm-5.2 residue under raw_outputs/. `glm_pilot_appendix/raw/` found EMPTY (recursive glob) — quarantine payload location unconfirmed.
- Mid-write race observed during analysis; machine-readable snapshot saved to `_interim_snapshot.json`.

## 2. Effectiveness per arm x family (computed over outcome JSONs)

| Arm | Family | n | Mean score | Cond. mean (F0-ok) | F0 fail % | Gate-pass % |
|---|---|---|---|---|---|---|
| NL-plain | EX | 50 | 0.821 | 0.821 | 0% | 2% |
| NL-opt | EX | 50 | 0.769 | 0.769 | 0% | 0% |
| JSON | EX | 50 | 0.826 | 0.826 | 0% | 4% |
| CSIR-SIR | EX | 50 | 0.082 | 0.093 | 12% | 0% |
| NL-plain | CP | 50 | 0.309 | 0.309 | 0% | 18% |
| NL-opt | CP | 50 | 0.285 | 0.285 | 0% | 18% |
| JSON | CP | 50 | 0.805 | 0.959 | 16% | 66% |
| CSIR-SIR | CP | 43 | 0.083 | 0.102 | 19% | 0% |
| NL-plain | TU | 50 | 0.720 | 0.720 | 0% | 72% |
| NL-opt | TU | 50 | 0.360 | 0.360 | 0% | 36% |
| JSON | TU | 50 | 0.940 | 0.940 | 0% | 94% |
| CSIR-SIR | TU | 50 | 0.000 | 0.000 | 6% | 0% |

**Headline:** CSIR-SIR collapses everywhere — EX 0.082, CP 0.083, TU 0.000 (0/50 items scored >0) — while JSON leads every family (EX 0.826, CP 0.805, TU 0.940). NL-plain beats NL-opt on EX (0.821 vs 0.769) and TU (0.720 vs 0.360).

## 3. §1.4 cost decomposition per arm (token space; pinned prices $0/$0)

Manifest price vector (OpenRouter :free, retrieved 2026-08-24) is p_in=p_out=$0/token -> all $ figures identically $0; decomposition reported in tokens. Formula A(N)=V_in+V_out+F/N plus R,K actuals. K charged per-item (honest primary N_conv=1; K-amortization = PROJECTED only).

| Arm | n | V_in | V_out | F | R | K | A(1) | A(10) | A(25) | A(100) | lat p50/p95 ms |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NL-plain | 150 | 274 | 1349 | 85 | 0 | 0 | 1708 | 1632 | 1627 | 1624 | 40,692/91,581 |
| NL-opt | 150 | 281 | 1615 | 449 | 0 | 0 | 2345 | 1941 | 1914 | 1901 | 59,419/105,814 |
| JSON | 150 | 274 | 861 | 389 | 386 | 0 | 1910 | 1560 | 1536 | 1525 | 29,435/203,569 |
| CSIR-SIR | 143 | 208 | 296 | 295 | 393 | 11110 | 12302 | 12037 | 12019 | 12010 | 17,178/42,487 |

- SIR K≈11.1k tok/item: 142/143 SIR items hit the 3-attempt converter repair limit (~3.7k tok/attempt). K dominates: SIR A(N) flat ≈12019 tok vs baselines 1.5–2.3k.
- **Δ(N)=baseline−SIR<0 at every N∈{1,10,25,100}, every pairing** -> no break-even N* on the registered grid. PROJECTED K-amortization break-even ≈ N_conv 9–10 (vs NL-opt), non-confirmatory per prereg §3.2.
- R retry load real: JSON 386, SIR 393, NL arms 0 tok/item.

## 4. PRELIMINARY directional reads vs registered predictions — ALL INTERIM

Comparator rule (prereg §7): strongest baseline per family = **JSON in all three families** on interim data. Power ceiling ≳15–20 F1 pts at n=50; observed gaps are 62–94 pts.

| Prediction | Registered | Interim read | Direction | What final data could change |
|---|---|---|---|---|
| **H1 / H0 (central)** | H1 support: SIR beats strongest baseline on $/task (CI excl. 0) AND F1 non-inferiority (δ_F1 EX/TU 3pt, CP 4pt) AND replication AND red-team survival | SIR loses F1 everywhere by 74–94 pts vs JSON AND carries K≈11k tok/item → worse $/task at every N. H1 condition (2) fails in all 3 families ⇒ **no H1 support possible; H0 currently favored**. | AGAINST H1 (strong) | Only CP is still filling (+7 cells); its gap (~72 pts vs 4-pt margin) is effectively immutable. Bootstrap CIs pending but direction is far beyond the power ceiling. |
| **H3 reuse-gating** | Δ(1)≤0 all families; Δ(25)>0 in EX iff conversion F2≥0.90; monotone in N; falsified if Δ(N)≤0 at every declared N | Δ(N)<0 at EVERY N∈{1,10,25,100} vs every baseline (SIR flat ~12.1k tok; baselines 1.5–2.3k). Matches the registered falsifier shape. | AGAINST H3 (as registered) | PROJECTED K-amortization curve (break-even ≈N_conv 9–10 vs NL-opt) computable but non-confirmatory; missing F2 audit decides whether framing is "conversion economics" (P2 guard) or artifact-contract failure. |
| **P2 UNL-replay guard** | if conversion-stage F2<0.80 on EX then Δ(N)<0 at all N (diagnostic localization) | Consistent with observation, but **F2 not computed** (`f2_audit.json` empty). Guard unevaluated. | UNRESOLVED (mechanism) | Final F2 audit localizes loss at converter vs representation/contract. |
| **H2 variance (CP module)** | SIR run-to-run dispersion < NL arms at comparable mean; partial survival vs JSON required | **PENDING — module absent**: zero rep≠'' rows; T=0.7 repetitions not yet run. "Comparable mean" precondition already fails (SIR CP 0.083). | PENDING | Module execution + agreement-rate/entropy; prereg detectable threshold 15 pts. |
| **H4 silent-error guide-rail (P5)** | silent-error fraction (validation-passed ∧ F1-failed): SIR < both NL arms in CP; NO SIR-over-JSON edge in TU | Proxy (doc_valid=True ∧ gate fail): SIR-CP docs validate 100% while scores ≈0.08 → silent-error rate near-maximal for SIR, opposite of prediction; JSON validates *and* scores 0.81. kerr_flag=False on 143/143. | AGAINST P5 (interim) | Validator-semantics check (schema-only vs behavioral); final CP cells; explicit per-arm silent-error table. |
| **P6 TU adversarial loss** | verbatim: "TU: SIR vs JSON **`<`** — registered adversarial loss (P6); contrary result triggers mandatory red-team review before any claim" | Confirmed and exceeded: **SIR TU mean 0.000, 0/50 items scored >0** vs JSON 0.940. Quoted verbatim per P4_PREP §S2.5 — no softening, no re-basing. | CONFIRMED (stronger than registered) | Nothing plausible at n=50 with zero nonzero items. Red-team review of the SIR pipeline now mandatory. |
| **P7 converter fidelity / F3≥0.90** | canonical round-trip equality ≥0.90; failures concentrate at unknown/branch nodes | **NOT COMPUTABLE**: f2_audit.json empty ({f2_rates:{},f2_unknown:{}}); conversions.csv absent. Indirect telemetry self-contradictory (anomaly A1): repair limit hit on 142/143 items yet conv_errors empty, kerr_flag=False, doc_valid=True throughout. | UNRESOLVED (instrument missing) | Run F2/F3 from raw `attempts[*] stage='convert'` payloads; then evaluate δ_F3 and failure concentration. |
| Latency rows (§6.1) | SIR p95 `>` all baselines (serial conversion adds a hop) | **INVERTED**: SIR p50/p95 = 17.7s/45.3s vs NL-plain 40.7s/91.6s, NL-opt 59.4s/105.8s, JSON 29.4s/203.6s. Short executor outputs (V_out≈300 vs 861–1615) beat the added hop. | AGAINST registered sign | Confirm on frozen matrix; apply §1.5 queue-anomaly rule check. |

**Interim headline:** every directional signal points against the CSIR/SIR representation — worst effectiveness, worst net cost at every N, no latency compensation, total adversarial-family loss. Open question is *where* the loss lives (converter vs representation vs answer-artifact contract), which the missing F2/F3 instruments must settle.

## 5. Anomalies (incl. P4_PREP §2.4 fabrication-signal screen)

| # | Severity | Finding |
|---|---|---|
| A1 | **HIGH** | Converter telemetry self-contradiction: `n_conv_attempts=3` (repair limit) on **142/143** SIR items — first-shot conversion essentially never passed — while `conv_errors` empty, `kerr_flag`=False, `doc_valid`=True on all 143. Either attempts are mis-instrumented or failures were absorbed silently, which prereg §3.1 prohibits ("never silently repaired"). Blocks clean K_err attribution; resolve BEFORE verdicts. |
| A2 | HIGH | **Checker crashes**: 11 cells (8 CSIR-CP, 3 CSIR-TU), detail=`{"checker_exception": AttributeError("'str' object has no attribute 'get'")}`, auto-scored 0.0/f0_ok=False. Honestly recorded, but means SIR emitted string-typed artifacts where dicts expected — answer-artifact contract breach. Excluding them moves CP mean only 0.083→0.102; direction unaffected. |
| A3 | MEDIUM | Amendment-2 cond. 1 unverifiable: no `model` field in any outcome record; ox-alpha admission rests on mtime alone (zero pre-cutoff residue found). `glm_pilot_appendix/raw/` EMPTY at snapshot — quarantined glm payloads' location unconfirmed. |
| A4 | MEDIUM | Straw-man inversion: NL-plain > NL-opt on EX (0.821 v 0.769) and TU (0.720 v 0.360), template-driven (TU-04: 0.70 v 0.20; TU-05: 0.90 v 0.10). Questions NL-opt prompt quality / §4.2 effort-parity attestation. |
| A5 | MEDIUM | JSON-CP parse failures cluster: 8/50 F0 fails, all "parse: no JSON object found", confined to CP-01/CP-02 — consistent with max_tokens truncation on long planning outputs; source of R=386 tok/item retry load. |
| A6 | LOW | SIR same-template duplicate (v_in,v_out) token-count pairs: 15/143. Plausibly temp=0 coincidence (payloads differ); below S2.4 escalation threshold. Identical-latency collisions across all arms: 2 (negligible). No outcomes.csv row lacked its raw file on spot-checks. |
| A7 | LOW | Latency inversion vs registered directional row (see §4). |
| A8 | MEDIUM | Missing instruments: f2_audit.json empty; conversions.csv absent; H2 replication module absent → P1/P2/P3/P7/H2 unevaluable until run. |
| A9 | LOW | Live-write race during analysis (CSIR×CP 31→36→39→43 cells); single-load snapshot frozen in `_interim_snapshot.json`. |

## 6. Exact remaining work for final analysis

1. Freeze matrix (7 CSIR×CP cells outstanding); re-run G1 gate + regenerate every table here from the frozen set (queries reproduce from `_interim_snapshot.json`).
2. Resolve A1 before verdicts: inspect raw `attempts[*] stage='convert'` records to establish true converter success semantics; correct or justify `n_conv_attempts`/`kerr_flag`; log in DEVIATIONS.md.
3. Backfill or formally waive the `model` field (Amendment-2 cond. 1) via DEVIATIONS.md; locate the actually-quarantined glm payloads.
4. Run F2 conversion-stage audit (populate f2_audit.json): per-unit-type recovery on ≥20% stratified sample/cell; test P3 concentration (modality/preference_order/exclusion, NOT entity_ref/quantity_unit); evaluate P1 gate (F2≥0.90) and P2 guard (F2<0.80).
5. Compute F3 canonical round-trip equality over all SIR documents (δ_F3=0.90); tabulate failures by node kind (unknown/branch concentration test).
6. Paired item-level bootstrap (10,000 resamples, seed 20260824): SIR−comparator deltas for F1 and $/task @ N∈{1,25} per family (comparator=JSON ×3 on current data); unconditional AND conditional stats; Pareto planes ($ vs F1).
7. Execute H2 variance module if budget allows: 20 stratified CP × {NL-opt, JSON, SIR} × 5 reps @ T=0.7, seeds 101–105; note 'comparable mean' precondition already fails.
8. Stochastic replication (10 stratified items × 3 reps @ T=0.7, seeds 201–203; SIR vs strongest baseline, EX+TU) + three-fold split sign-consistency → H1 condition (3).
9. Independent recomputation per P4_PREP §2.2 on the 15-cell sample (12 strata + highest-cost + lowest-cost + nearest-mtime-to-cutoff reserves); recompute N* from §1.4 curves (§2.3).
10. Write verdicts with S2.5-compliant verbatim TU language; schedule mandatory red-team review triggered by confirmed P6 loss; finalize H4 after validator-semantics check (A2).
11. Update STATUS.md (**final worker owns it** — deliberately untouched by this interim).

---
*Interim analysis subagent (ox-alpha), 2026-08-25 ~05:15 IST. Sources: raw_outputs/*/*/*.json mtime-filtered; manifest.json ($0/$0 price vector, δ margins, N-grid); E1_PRE_REGISTRATION.md §6–7; E1_AMENDMENT_2.md; MEASUREMENT_PLAN.md §1.4; P4_PREP.md §2. Helper: `_interim_snapshot.json`.*
