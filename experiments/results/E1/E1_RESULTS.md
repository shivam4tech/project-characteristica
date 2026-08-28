# E1 RESULTS — Efficiency/Fidelity Pilot (CE-01/P3)

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


## 4. F2 conversion-stage vs behavioral fidelity (stratified 20% sample, SIR arm)

| unit type | n | conversion-stage recovery | behavioral recovery |
|---|---|---|---|
| conditional_constraint | 4 | 0.00 | 0.00 |
| designed_unknown_flag | 2 | 0.00 | 0.00 |
| entity_ref | 42 | 0.00 | 0.00 |
| exception_of_exclusion | 2 | 0.00 | 0.00 |
| exclusion | 10 | 0.00 | 0.00 |
| modality | 8 | 0.00 | 0.00 |
| priority_preference | 6 | 0.00 | 0.00 |
| quantity_unit | 18 | 0.00 | 0.11 |
| temporal_qualifier | 26 | 0.00 | 0.00 |

Unknown-probe handling (designed probes; doc AND artifact must declare undeterminacy):
- `designed_unknown_flag`: 0/2 handled (0%)
- `entity_ref`: 0/2 handled (0%)
- `priority_preference`: 0/2 handled (0%)

_Note (CP instrumentation limit): CP gold constraints are internal ids checked against the emitted plan; leaf-value containment cannot attribute CP losses per unit type. CP F2 is therefore reported qualitatively via K_err/doc_valid/silent-error rather than per-unit._

## 5. H2 variance module (20 CP items x 5 reps @ T=0.7)

| arm | items | modal-answer agreement | outcome entropy (bits) | mean score |
|---|---|---|---|---|
| NL-opt | 20 | 0.71 | 0.94 | 0.323 |
| JSON | 20 | 0.41 | 1.74 | 0.838 |
| CSIR-SIR | 20 | 0.76 | 0.70 | 0.086 |

## 6. Replication (H1 condition 3)

- Stochastic module (10 stratified items x 3 reps @ T=0.7, seeds 201–203), SIR vs strongest baseline:
  - CP vs JSON: fold gate-deltas [-0.8, -1.0, -0.7] → sign-consistent: **True** (-)
  - EX vs JSON: fold gate-deltas [-0.1, 0.0, 0.0] → sign-consistent: **False** (-)
  - TU vs JSON: fold gate-deltas [-1.0, -0.9, -1.0] → sign-consistent: **True** (-)
- Item-split module (primary, 3 folds):
  - CP: fold gate-deltas [-0.6875, -0.625, -0.625] → sign-consistent: **True**
  - EX: fold gate-deltas [0.0, -0.0625, -0.0625] → sign-consistent: **False**
  - TU: fold gate-deltas [-0.9375, -0.875, -1.0] → sign-consistent: **True**

## 7. F3 round-trip stability

- F3 probe not run/empty.


## 8. Registered predictions — evaluated exactly as stated (pre-reg §6)

### P1 — EX: SIR vs strongest NL arm
- Conversion-stage F2 (EX, unit-weighted across audited types): **0.0** (condition-to-fire '>': F2 ≥ 0.90 → NOT FIRED)
- Observed gate-success SIR vs strongest NL arm (JSON): 0.0 vs 4.0 (Δ=-0.0 pts)
- $ @N=1 `<` and $ @N=25 `>` iff F2≥0.90: $ instrument degenerate (all $≡0) → **no detectable difference on the registered $ endpoint**; F1 side: SIR < comparator

### P2 — UNL-replay guard (fires iff EX conversion-stage F2 < 0.80)
- Condition: EX F2 < 0.80 → FIRED (F2=0.000)
- Predicted Δ(N)<0 ∀N: observed Δ(N)≡$0 (degenerate) → predicted strict inequality not observable on the $ instrument; recorded as **not evaluable in $ terms (instrument degeneracy)**, diagnostic value limited to F2 level itself.

### P3 — Conversion-loss localization
- Per-type conversion-stage losses: entity_ref=1.00, exclusion=1.00, modality=1.00, preference_order=—, quantity_unit=1.00
- Mean loss in predicted-lost classes 1.00 vs easy classes 1.00 → loss concentrates in predicted classes: **False** → P3 **FALSIFIED** (loss concentrates in the easy classes)

### P4 — H2 variance (CP module)
- Agreement: SIR 0.76 vs NL-opt 0.71 vs JSON 0.41
- SIR dispersion < both NL arms (≥15-pt detectable gap): False; survives JSON comparison (partial-survival rule): True
- Verdict: **NOT SUPPORTED (no detectable gap)**

### P5 — H4 silent errors (CP ↓ both NL arms; TU: NO significant SIR>JSON edge)
- CP silent-error fractions: NL-plain 82.0 | NL-opt 82.0 | JSON 21.4 | **SIR 100.0** → reduction vs both NL arms: False
- TU silent-error JSON−SIR gap: -94.0 pts (registered expectation: NO significant SIR-over-JSON advantage)
- Verdict: ****FALSIFIED** per registry criteria (reduction absent)**

### P6 — TU adversarial loss (SIR ≤ JSON in tool-use; contrary ⇒ mandatory red-team review)
- TU gate success: SIR 0.0 vs JSON 94.0 (Δ=-0.9 pts; $ endpoint degenerate)
- Registered prediction SIR ≤ JSON: **CONFIRMED** — the registered adversarial loss is honestly reported: on the F1 endpoint SIR loses to (or ties) the JSON arm in its schema-native territory.

### P7 — F3 round-trip stability (δ_F3=0.90; failures concentrate at unknown/branch nodes)
- F3 probe not run.

### H1 central gate (four conditions, per family) & H0 standing
- **EX** (comparator JSON): (1) efficiency CI excl. zero: $ instrument degenerate → cannot be satisfied in $ terms; (2) F1 non-inferiority (δ=3.0): PASS (Δ=-0.0); (3)+(4) see replication/red-team above. => H1 support requires ALL four: **not achieved in $ terms by construction of the free-tier instrument; family cannot pass on the registered primary endpoint.**
- **CP** (comparator JSON): (1) efficiency CI excl. zero: $ instrument degenerate → cannot be satisfied in $ terms; (2) F1 non-inferiority (δ=4.0): PASS (Δ=-0.7); (3)+(4) see replication/red-team above. => H1 support requires ALL four: **not achieved in $ terms by construction of the free-tier instrument; family cannot pass on the registered primary endpoint.**
- **TU** (comparator JSON): (1) efficiency CI excl. zero: $ instrument degenerate → cannot be satisfied in $ terms; (2) F1 non-inferiority (δ=3.0): PASS (Δ=-0.9); (3)+(4) see replication/red-team above. => H1 support requires ALL four: **not achieved in $ terms by construction of the free-tier instrument; family cannot pass on the registered primary endpoint.**

- **H0 standing:** stands unless ≥1 family passes all four conditions — **H0 STANDS** (no family passes condition 1 on a degenerate $ instrument).

---
*Deviations ledger: DEVIATIONS.md DEV-1..DEV-8 (DEV-8 = Amendment-1 re-pin, pacing, checkpoint-resume; all pre-first-scored-call). Interruptions: INTERRUPTION_LOG.md.*