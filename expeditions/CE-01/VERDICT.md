# CE-01 Director Verdict — P5 Verdict Synthesis

**Expedition:** CE-01 / Project Characteristica · E1 Efficiency/Fidelity Pilot  
**Director:** characteristica-prime (bounded review 2026-08-28, this file)  
**Inputs verified in full before verdict:**  
`experiments/results/E1/E1_RESULTS_FINAL.md` (AUTHORITATIVE, 600 admitted + h2 300 + repl 180, Addenda A/B), `experiments/results/E1/outcomes.csv` + `h2_outcomes.csv` + `repl_outcomes.csv` + `rerun_sir_outcomes.csv`, `experiments/E1_PRE_REGISTRATION.md` (FROZEN, 213 ln), `benchmarks/MEASUREMENT_PLAN.md` §1.4 formulas only, `critiques/P4_PREP.md`, `critiques/P4_REVIEW_DRAFT.md` §4 EXECUTED (Cycle 4, 15-cell recomputation + ALL-600 fabrication sweep), `critiques/A1_ROOT_CAUSE.md`, `paper/E1_PAPER_DRAFT.md` (351 ln, Figs.1–5 FINAL), `manifest.json` (stealth/ox-alpha, $0 price vector, seeds), `CLAIM_LEDGER.md` C-001–C-019.

**Verdict governs:** CSIR/0 as specified in `systems/csir0_architecture.md` (validated checkpoint contract, two-tier vocab, 7-label edge set, D-4 converter=executor) evaluated on the E1 task distribution (EX/CP/TU, 50 items/family, n=600 primary @T=0). All conclusions scoped to **single model family stealth/ox-alpha** (P8) and **CE-01 power ceiling** (≥15–20 F1 pts / large $ deltas detectable; smaller effects invisible).

---

## 1. Executive verdict

### RED — Discontinue CSIR/0 as specified

Per `LAB_CHARTER.md` §Lab Verdicts: *the central hypothesis provides no meaningful advantage, is already substantially solved, or fails under experimental scrutiny.* A RED verdict is a **successful research outcome if well supported** — it is.

**One-line synthesis (modern technical framing):** CSIR/0 fails as an **inference-time interchange** because its **per-item neural conversion stage dominates end-to-end cost** (K≈11.1k tokens, 7.4k of which is deterministic repair traffic) while producing **no executable artifact on 99.3% of inputs**; even post-hoc amortization accounting and KV-cache-style F/N reuse cannot recover break-even. The economics localize cleanly to the converter, not to executor payload efficiency or marginal fidelity gaps — a textbook **UNL-replay failure** (C-007) reproduced under contemporary LLM serving mechanics.

This is not a "no advantage" universality claim. Per pre-reg §4.5 power honesty, the licensed language is: **CSIR/0 shows no detectable advantage at CE-01 scale on any registered endpoint in any family** and is **strictly dominated by the JSON-schema control in every family on both F1 and amortized tokens.**

---

## 2. What P4 established before any verdict could be issued

P4 ran under `P4_PREP.md` §2 protocol (Lane discipline: stored aggregates not trusted). **Data verdict: ACCEPT — all 8 gates pass.** No partial acceptance per §4.

| Gate | Check | Evidence |
|---|---|---|
| G1 Coverage | 12/12 blocks 50/50 (≥80%) | Counter in `P4_REVIEW_DRAFT.md` §4 A.6 |
| G2 Arm presence | 4 arms present | — |
| G3 Fidelity integrity | F0 fails have registered cause (A1, 149/150 kerr) | §4 A.6 |
| G4 Deviation discipline | Amendments 1–3 + DEVIATIONS.md cover all changes | — |
| G5 TU wording | P6 confirmed verbatim, not softened | §4 A.5 |
| G6 Quarantine | 0/600 rows before 00:35 IST cutoff | — |
| G7 Converter accounting | SIR `k_*` + `f_conv_tok` folded per D-4 | `analysis.py:total_sir()` |
| G8 Oracle residue | 0 hits /1050 raw files | §4 A.4 |

**Fabrication sweep (S2.4) over ALL 600 admitted rows:** CLEAN — 597/600 unique latencies (max dup 2), 512/600 unique token-tuples, 93/600 unique details (max dup 35 = expected identical SIR empty-doc payload), 0 missing `v_in`, 0 missing raws (1050 files), 0 oracle leakage. **Score recomputation (S2.2)** and **cost recomputation (S2.3)** on the 15-cell stratified sample (12 median + 3 reserves) match reported aggregates within rounding; recomputed N* = none exists, matching reported no break-even. **TU verbatim (S2.5):** verbatim per P6 (see §3).

Data are **trustworthy and uncompromised.** Verdict rests on clean measurement.

---

## 3. Results as measured (FINAL, authoritative)

### 3.1 Efficacy — F1 (gate-conditioned), n=50/cell, T=0

Source: `E1_RESULTS_FINAL.md` §2 (paired bootstrap 10k, seed 20260824; comparator = strongest baseline per pre-reg §7 = JSON in all families).

| Arm | EX mean ±SD (gate%) | CP (gate%) | TU (gate%) |
|---|---|---|---|
| JSON (comparator) | **0.826 ±0.123 (4.0%)** | **0.806 ±0.360 (66.0%)** | **0.940 ±0.240 (94.0%)** |
| CSIR-SIR | **0.082 ±0.118 (0.0%)** | **0.071 ±0.148 (0.0%)** | **0.000 ±0.000 (0.0%)** |
| Δ (SIR−JSON) | **−0.743 [−0.785,−0.699] dz −4.73** | **−0.734 [−0.835,−0.626] dz −1.96** | **−0.940 [−1.000,−0.860] dz −3.92** |

Every SIR deficit is **4–6× the §4.5 power ceiling** (≥15–20 pts). TU is 0.000 on all 50 items. Sensitivity (dropping 11 string-typed checker exceptions): SIR CP 0.071→0.085, TU stays 0.000 — direction unchanged.

**H1/H0 framing (pre-reg §7 gate):** H1 requires **all four** conditions per family — (1) SIR beats strongest baseline on $/task with CI excluding zero, (2) F1 non-inferiority within δ (EX/TU 3 pts, CP 4 pts), (3) replication, (4) red-team survival (P4). (1) fails because $≡$0 on the `:free` tier (degenerate instrument — token-space diagnostic shows SIR *worse* by 9–11.5k tok, CI excludes zero the wrong way); (2) fails by 74.3/73.4/94.0 pts; (3) evaluated via repl — see §3.4; (4) passes (P4 ACCEPT) but is moot. **No family passes a single non-trivial H1 condition → H1 finds no support in any family → H0 stands, favored.**

### 3.2 Cost — amortized tokens, MEASUREMENT_PLAN §1.4

Price vector $0/$0 ⇒ all $ identically $0.00; token-space is decision-relevant per manifest.

| Arm | V_in | V_out | F | R | K | K_reinj | A(1) | A(10) | A(25) | A(100) |
|---|---|---|---|---|---|---|---|---|---|---|
| NL-plain | 274 | 1349 | 85 | 0 | 0 |0| 1708|1632|1627|1624|
| NL-opt | 281 | 1615 | 449 | 0 | 0 |0| 2345|1941|1914|1901|
| JSON | 274 | 861 | 389 | 386 | 0 |0| 1910|1560|1536|1525|
| **CSIR-SIR** | 206 | 292 | 295 | 374 | **11112** | **7408 (66.7%)** | **12280**|**12014**|**11997**|**11988**|

SIR executor payload is *cheapest* (V+F small); loss is **entirely conversion-stage**. K's dominant term is **K_reinj = 7,408 tok (66.7%)** — deterministic repair traffic: `n_conv_attempts=3` on 149/150 items, `conv_errors='json:no JSON object found'` on 149/150, `p_out` capped at 2048 = MAX_TOKENS on 445/448 conversions (converter budget exhausted before any JSON object emitted). Single valid CSIR document in 150 (EX-04-05, 30 nodes/15 edges, scored 0.813 when it did emit) — pipeline works when it emits; it almost never emits.

**Amortization:** `A(N)= V_in+V_out+F/N+K+R`. Even at `N→∞` (F fully cached, KV-prefix-cache analogue), SIR floor ≈11,988 tok vs best baseline 1,525 → Δ(∞)≈−10,463. **No break-even N* exists on the registered N-grid {1,10,25,100} nor anywhere — while K≈11.1k stands, K alone exceeds any baseline's entire per-task cost by ~7×.** Conditional cost per *successful* task is undefined for SIR (0 successes → ∞) vs JSON 3,493 tok.

**Projected sensitivity (NON-CONFIRMATORY):** if per-item repair could one day be deduplicated and charged at `K/N_conv`, break-even `N_conv`≈11 vs NL-opt /15 vs NL-plain /18 vs JSON @N=25 — arithmetic, not a claim.

### 3.3 System dynamics — latency and reliability surface

| Arm | p50 | p90 | p95 | max |
|---|---|---|---|---|
| CSIR-SIR | **17.2 s** | **35.6 s** | **45.3 s** | 118 s |
| JSON | 29.4 s | 78.4 s | **209.6 s** | 275 s |

Registered prediction P1 had SIR p95 `>` all baselines (serial-conversion surcharge) — **INVERTED**: SIR is fastest at every percentile because short executor outputs (V_out 292 vs 861–1615) outweigh the hop. JSON owns the tail (retry/truncation loops). Speed here is **degenerate**: faster by skipping verification, not by efficiency — classic goodharting of a latency metric when fidelity is at floor.

Fidelity gates: NL arms 100% F0-ok; JSON 94.7% (8 CP truncations, source of its R=386); SIR converter-stage **valid documents 1/150 (0.7%)**, `kerr_flag=True` 149/150, `doc_valid=False` 149/150 — **loud failure**, not silent absorption. Inference overhead from executor retries is real and asymmetric: items with retries JSON 12/150, SIR 54/150, NL arms 0.

### 3.4 Replication, variance, and the instruments that lacked signal

- **Stochastic replication (repl, 196→180 admitted, 2 arms ×3 families ×10 items ×3 reps @T0.7, DEV-7 dedupe):** gate-delta sign-consistency SIR−JSON — CP **True** [−0.8,−1.0,−0.7], TU **True** [−1.0,−0.9,−1.0], EX **False** [−0.1, 0.0, 0.0] (two zero folds break strict consistency). Item-split on primary (3 folds) mirrors: CP True, TU True, EX False. Under P4's replication gate this **passes for CP/TU, fails for EX** — moot because H1 already fails on (1)(2). Direction: repl **strengthens the negative** (CP/TU advantage is reliably in the baseline's favor).
- **H2 variance (h2, 300 admitted, CP strata, 3 arms ×20 items ×5 reps @T0.7):** within-item SD SIR 0.000 < JSON 0.119 < NL-opt 0.144 nominally; grand means 0.086/0.838/0.323 — **comparable-mean precondition fails catastrophically** (SIR degenerate at floor, every rep identical). NOT-EVALUABLE, degenerate (stability-at-failure, not stability-at-parity). JSON disperses less than NL-opt even at matched means — would weaken H2 to "generic structuring" per registry had means matched. Agreement-gap 8 pts < 15-pt detectability threshold.
- **F2/F3:** `f2_audit.json` empty (all conv 0.00, beh 0.00 except `quantity_unit` beh 0.11, n=18 — too sparse); `conversions.csv` absent. **P2/P3/P7 NOT-EVALUABLE** (instrument missing; with 1/150 valid docs there is almost nothing to audit or round-trip). P5/H4 (H4) silent-error fraction nominally SIR 0% vs JSON 34% in CP but **bought by total rejection** (valid-doc denominator ≈1) plus F1 collapse >δ — registry falsifier fires: **FALSIFIED** (reduction explained by JSON arm; bought below δ; degenerate validator behavior). The one falsifiable where data exist, it falsifies.

### 3.5 Hypothesis scoreboard (registered wording, P4-clean)

| # | Registered prediction | Numbers | Verdict |
|---|---|---|---|
| H1 | Four-condition support gate per family | (1) FAIL, (2) FAIL by 74/73/94 pts, (3) CP/TU True EX False (moot), (4) P4 PASS | **NO H1 SUPPORT — 0/3 families** |
| H3 | Falsifiers (a) Δ(N)≤0 ∀N / (b) Δ(1)>0 / (c) no N×arm interaction | Δ(N)<0 ∀N (−9k..−11.5k tok), $Δ≡0 | **FALSIFIED via (a)** |
| P2 UNL-replay guard | if F2<0.80 on EX then Δ<0 ∀N | F2 unmeasured; consequent observed true | **NOT-EVALUABLE** (consequent consistent) |
| P3 localization | losses in modality/preference_order/exclusion not entity_ref/quantity_unit | F2 audit absent | **NOT-EVALUABLE** |
| P5/H4 | silent-error SIR < NL in CP; no SIR>JSON edge in TU | CP 100% vs JSON 34% but degeneration → falsifier fires | **FALSIFIED** |
| P4/H2 | SIR dispersion < NLs at comparable mean | precondition fails (degenerate) | **NOT-EVALUABLE** |
| P7/F3 | F3≥0.90 | no docs to round-trip | **NOT-EVALUABLE** |
| **P6 TU adversarial** | SIR `<` JSON in TU (G5 verbatim) | 0.000 vs 0.940 Δ−0.940 [−1,−0.86] | **CONFIRMED, stronger than registered** |

Supplementary registered directional rows: latency p95 prediction INVERTED; H0 disposition: **zero families pass H1 → H0 NOT rejected — stands, favored**, scoped to stealth/ox-alpha, CE-01 scale.

**Ceiling-triggered localization (H0 typology):** with P6 CONFIRMED + TU formally adversarial, pre-reg §10.3 specifies **Pattern C1** — failure localized at **conversion economics (C-007)**, UNL-replay. This is the diagnostic win inside the RED: we know *where* the wall is.

---

## 4. Why it failed — mechanism, not vibes

### 4.1 The converter wall as the binding constraint

Contemporary LLM serving separates **prefill-bound fixed context** (cacheable, amortized as F/N — analogous to KV-cache prefix reuse after ~2 reads [Anthropic prompt-caching]) from **decode-bound per-token generation** (paid per item). SIR's executor payload is *smaller* than every baseline's (V 498 vs 1,135–1,896). Under a naive prompt-cache mental model, SIR should amortize well. It does not, because the architecture **adds a second inference call per item** whose output is bounded by `MAX_TOKENS=2048` and whose input carries the full F_conv + source. That call's per-item retry loop is **deterministic at T=0** — same prompt → same truncated `content=""` → same `json:no JSON object found` — so `n_conv_attempts=3` is pure waste, not exploration. Caching the converter's fixed prefix would amortize F_conv, not K; the bottleneck is **K_reinj, which is per-item and non-cacheable**.

Amendment-3 (converter MAX_TOKENS 2048→8192, 70 cells, fast-closed) confirms sensitivity: **identical failure signature**, K≈11k unchanged, `json:no JSON object found` persists — **not a context-window edge fix.** The wall is structural to the per-item conversion contract, not a budget trim.

### 4.2 Mapping to C-007's two-class taxonomy

P2_SYNTHESIS refined C-007 into two failure classes: **Class-I economics** (population/authoring cost kills artifacts) vs **Class-II collapse** (formal inconsistency, expressive limits). E1 is unambiguously **Class-I**: the calculus ships no proof system (C-002 respected), Tier-B vocabulary avoids the primitives-first deadlock (C-017), and the graph depth cap (§3) is honored. No logical contradiction was exposed. What died is the **artifact's economics** — the same lineage as Wilkins' maintenance cascade → UNL certified writers → Cyc manual assertion — now instantiated as **per-item neural re-injection** instead of human writer cost. Four centuries, same variable: *who pays population cost, and does per-unit cost go to ~zero?* (P2_SYNTHESIS §1d). For CSIR/0 the answer is the caller, on every item.

### 4.3 What the data *do* show about the representation layer

When the converter did emit (1/150), that document scored 0.813 — the executor + adapter stack **can** consume CSIR. The representation's semantics are not refuted; the **population mechanism** is. Relatedly, three structural bets *do* validate obliquely: Tier-B opaque terms avoided the A3 primitive trap (no Wilkins cascade observed), the validated checkpoint contract's provenance spans were consumed when present, and the `unknown_flag` / branch-or-flag ambiguity policy is precisely the behavior a surviving SIR would need (EX-05, TU-03 probes). The architecture's ideas are not falsified; the **operating point** (neural converter per item, T=0, same model as executor) is.

### 4.4 What this result does not imply

- **Not** that structured decoding is useless — the JSON-schema arm (`chrome` + validator retry loop) captures large gains over NL-plain on CP (+49.6 pts) and TU (+22 pts), reproducing the well-known **guide-rail effect** (C-001/C-018) without any SIR layer. CSIR/0's marginal over JSON is *negative* — the guide-rail value is already captured by commodity JSON Schema.
- **Not** that a different converter (fine-tuned small model, deterministic program synthesis from spans, or human-authored oracle) would fail — those are different population mechanisms with different K curves. The ceiling-triggered finding predicts where to look: make K sublinear or zero.
- **Not** that NL is efficient — NL-opt is actually *pessimal* on $/success (13,030 tok vs JSON's 3,493 vs NL-plain's 5,570). The win is not "NL is great" but **"JSON-schema is sufficient and SIR adds strictly negative marginal benefit at this scale."**

---

## 5. Prior-art assessment — CC1–CC3 kill-criteria as written

Per `P4_PREP.md` §3 stubs (executed during P4):

| Candidate Contribution | Pre-written kill criterion | E1 outcome | Disposition |
|---|---|---|---|
| **CC1 "SIR guide-rail: silent-wrong → detected"** | Prior work already quantifies structured form shifting silent-wrong→detected, OR SIR≈JSON on detected-vs-silent split ⇒ demote to confirmation | SIR silent-error *worse* than JSON in every family when degenerate-rejection discounted; structured stacks that *do* deliver the shift do so via JSON Schema already (§5.1 of P4 review). | **Demoted — Known Prior Art pattern confirmed, not a SIR contribution.** Report as confirmation. |
| **CC2 "Reuse-gated break-even N* for representation schemas"** | Existing published N*-style break-even formalism ⇒ arithmetic on known frame | No N* exists to measure (Δ<0 ∀N); plain amortization *does* exist in prior art (prompt-caching, KV-cache, template-cache literature). Sir's fidelity-gated conditional N* would have been novel if measured. | **No claim — would have been arithmetic; with no N* it is not even arithmetic.** Correct wording if ever measured: "first *measured* fidelity-gated N*," not novel formalism. |
| **CC3 "Unoccupied SIR layer between NL and compiler IRs"** | Any documented system using human-readable interlingua as LLM working format with empirical evaluation ⇒ occupancy claim false | AMR-as-LLM-input literature + UNL interlingua + LLMCompiler DAG-IR satisfy the *letter* on "interlingua + empirical LLM eval" though they fail the four-property conjunction (execution-target + validation gate + checkpoint economics + metered K). Per the fallback P4 §5.3 already anticipates, **reword from "unoccupied" to "first evaluated as validated, versioned, execution-gated semantic checkpoint with metered conversion economics."** | **Reworded — survives as first-evaluated, not unoccupied.** |

Novelty window update: the occupancy gap is **narrower than at P2 time-stamp** (2026-08-24) — movement from the tool-side (agentic plan JSON conventions converging on intent-shaped payloads) continues toward the same layer from below (§D9). C-009's time-stamp discipline was correct.

---

## 6. What RED means for the program — and what it does not close

### 6.1 Discontinued: CSIR/0 as an inference-time interchange with a per-item neural converter

No bounded E2 probe can rescue this operating point without **changing the population mechanism**. Retrying at larger MAX_TOKENS, more prompt engineering, or a second converter retry is already falsified as a lever (Amendment-3 + deterministic-T=0 argument). Continuing on this contract would mistake structured prompting for a universal representation (charter anti-goal #8).

### 6.2 Preserved: three cheaper levers worth one bounded probe *only if* the ceiling-triggered program is adopted

Each is a **different hypothesis** requiring new pre-registration, not a CSIR/0 retry:

1. **Converter off the hot path (R1-native structure).** Fine-tune or distill a small converter whose `K` is paid at training time, not per item (K→weights). Test: does a 200M–1B converter trained on the frozen 600-item bank produce valid docs at `K_reinj≪100` tok? This makes CB1's checkpoint value testable without per-item inference.
2. **Validated checkpoint as the claim, not interlingua.** Drop "semantic interchange" framing; ship SIR as a **cached execution contract** (C-011 R1) — value measured in resumability/auditability/portability across model families, not tokens. Requires cross-model replication (≥3 families) lifting P8, and a ceiling where $ is not degenerate (`:free` tier masks real Δ).
3. **Programmatic population, not neural.** Tier-B terms opaque + span coverage suggest a deterministic synthesizer from spans (program synthesis over the 7-label graph) could replace the LLM converter for EX/CP. The `unknown_flag` probes then become the interface, not the failure.

Each lever is **falsifiable before building**: if a 5-hour distillation spike cannot break K_reinj below ~500 tok on a 20-item held-out slice, stop.

### 6.3 What to publish

A well-supported RED is a publishable negative result per charter. The publishable package is:

- **Negative result proper:** H1 0/3, H3 falsified via (a), P6 confirmed stronger than registered, latency inversion documented — with Pareto-plane presentation ($/task vs F1) per family, never scalar ratios as decision statistics (S1.10).
- **Diagnostic asset:** measured K decomposition (K_reinj 66.7%), amendment-3 sensitivity, Pareto frontier (JSON as the efficient frontier), and the ceiling-triggered localization to conversion economics.
- **Method asset:** pre-registered, amendment-governed, adversarial-family design (TU as G5 verbatim control), DEV-7-admitted 600 + repl 180 + h2 300, full P4 red-team with recomputation — the *design* survives even though CSIR/0 does not.
- **Measured N*/fidelity curves** and detected-vs-silent null as published negatives (P2_SYNTHESIS Pattern C2 salvage value).

Wording gates honored everywhere: *no detectable advantage at CE-01 scale* (never "no advantage"); single-model scope stated; every cost figure paired with F0/F3 distribution and shown across N∈{1,10,25,100}; no cherry-picked N; TU severity verbatim per P6.

---

## 7. Ledger and housekeeping

- New rows **C-020–C-030** appended to `CLAIM_LEDGER.md` (see `CLAIM_LEDGER.md` diff at commit) — each an Experimental Result or Falsified finding per charter labels, tracing to `E1_RESULTS_FINAL.md` §numbers or `analysis_state.json` / `f2_audit.json`. Prior-art and red-team columns set to `checked-clean` / `cleared` where P4 reviewed; replication column set per repl/h2 status.
- `expeditions/CE-01/STATUS.md` updated: budget reconciled, provisional verdict → **RED (H0 stands, favored)**, strongest positive/negative signals populated, experiments completed.
- `foundation/STATUS.md` and `expeditions/CE-01/FINAL_REPORT.md` updated (or created) to point at this verdict.
- Remaining LIMITATIONS carried forward: Lingenic primary still Unresolved (C-016), Generales Inquisitiones conditional (C-015), Jungius/New Essays pinning deferred — none claim-bearing for this verdict.

---

## 8. Director's closing note

CE-01 did what a pilot should: it **priced the historically recurring wall** instead of theorizing around it, under adversarial conditions (TU engineered to make SIR lose), and let the data adjudicate between H1 and H0 under a falsification regime that could not be moved after seeing the numbers. The wall is where history predicted — in conversion economics — and it is now a number (≈10k tokens of per-item re-injection before a single F1 point is earned). That number, with its provenance and its P4-verified accounting, is the expedition's durable contribution.

**Recommendation to the program:** accept the RED for CSIR/0-as-specified, publish the negative result with its diagnostic decomposition, and re-invest only through a newly pre-registered expedition that moves conversion off the per-item hot path. Do not spend another inference-heavy cycle on this contract.

*— Director, characteristica-prime, 2026-08-28 19:10 IST (Cycle 5)*

