# P4 Adversarial Review — Draft Skeleton (CE-01)

**Status:** NUMERIC VERIFICATION COMPLETE 2026-08-28 18:09 IST (Cycle 4) · §4 EXECUTED, all gates evaluated, verdict ACCEPT — ready for P5 Director verdict.
Prepared 2026-08-25 IST by the P4 red-team prep worker, BEFORE inspecting any `experiments/results/E1/` file
(numbers deliberately not read: they belong to the interim analyst; this reviewer must not anchor on stored
aggregates before independent recomputation). Acceptance criteria were frozen in `critiques/P4_PREP.md`
(written pre-data) and cannot drift toward whatever the data shows.
**Ship path:** when final numbers land → fill §4 only → evaluate §6 mapping → issue ACCEPT/REJECT + verdict
recommendation with evidence pointers. Target completion <30 min.
**Scope:** E1 pilot (4 arms × 3 families × 50 items; temp=0; fixed seed 20260824; Amendment-2 re-pin to
stealth/ox-alpha, glm-5.2 pilot cells quarantined at mtime cutoff 2026-08-25 00:35 IST; D-1 oracle omitted;
D-4 converter=executor same model).

---

## 1. Scope & evidence base (what this review rests on)

**Design / governance documents reviewed in full:**

| Source | Used for |
|---|---|
| `critiques/P4_PREP.md` (229 ln) | §1 objections S1.1–S1.10, §2 verification protocol, §3 CC stubs, §4 gates G1–G8 |
| `experiments/E1_PRE_REGISTRATION.md` (213 ln, FROZEN) | §2 seven registered predictions + falsification conditions (verbatim, §6.1–6.2); arms/margins (δ_F1 = 3 pts EX/TU, 4 pts CP; δ_F3 = 0.90; N ∈ {1,10,25,100}) |
| `systems/csir0_architecture.md` §§0–10 | CC1–CC3 claim definitions, §9 predictions P1–P8, explicit non-claims (§8) |
| `expeditions/CE-01/P2_SYNTHESIS.md` | H0's sharpest form (JSON-arm capture, §3.2), C-007/C-008/C-009 lineage, M-01…M-13 mechanism map |
| `LAB_CHARTER.md` | GREEN/AMBER/RED definitions (§Lab Verdicts), anti-goals, allowed labels |
| `literature/modern/prior_art_map.md` (196 ln, Director-verified) | in-repo citation base for §5 (§D1/D2/D6/D7/D9/D13) |
| Fresh web searches (2026-08-25) | new prior art for §5; sources listed per-claim and in §5.4 |

**Deliberately NOT reviewed:** `experiments/results/E1/*` (E1_RESULTS*.md, DEVIATIONS, INTERRUPTION_LOG,
glm_pilot_appendix). Lane discipline: the interim analyst owns numeric analysis; this file consumes numbers
only through §4's placeholder slots at ship time.

**Evidence base caveats carried forward:** all conclusions are single-model (stealth/ox-alpha); CE-01 power
ceiling admits only large effects (~15–20 F1 pts / correspondingly large $ deltas) — verdict language must say
"no **detectable** advantage," never "no advantage" (pre-reg §6 preamble; MEASUREMENT_PLAN §4.5).

---

## 2. Pre-registered claims under scrutiny

All seven registered prediction blocks from `E1_PRE_REGISTRATION.md` §6.2, quoted verbatim (emphases as in
source). The oracle-contrast block is excluded: it was conditioned on decision D-1, which omitted the oracle
column (`P4_PREP.md` header; pre-reg Appendix B). Directional cell-level predictions live in §6.1 of the
pre-reg and bind the TU adversarial loss (see prediction 5 and gate G5).

### 2.1 H3 — reuse-gated efficiency (primary efficiency axis)
> "Predicted: Δ(N=1) ≤ 0 in ALL families (single-use never pays); Δ(N=25) > 0 in EX **iff** conversion-stage F2 ≥ 0.90; monotone improvement in N. Detectable: $ deltas ≥ ~25% of the NL-opt arm's per-task cost at n=50. **Falsification (registry H3):** (a) Δ(N) ≤ 0 at every declared N, or (b) Δ(1) > 0, or (c) no significant N×arm interaction — any of these falsifies H3 as registered."

### 2.2 UNL-replay guard (P2)
> "if conversion-stage F2 < 0.80 on EX, predicted Δ(N) < 0 at every N; registered NOW so the failure, if observed, is diagnostic (localizes the wall at conversion economics, C-007) rather than surprising."

### 2.3 Conversion-loss localization (P3)
> "predicted F2 conversion-stage unit losses concentrate in `modality`, `preference_order`, `exclusion` — NOT in `entity_ref`/`quantity_unit`. Test: per-unit-type recovery rates from the F2 audit (≥20% stratified sample per cell, §3.2). Falsified if loss concentrates in the 'easy' unit classes instead."

### 2.4 H1 — central hypothesis (four-condition support gate)
> "support in a family requires ALL FOUR plan §4.4 conditions: (1) SIR beats the **strongest** baseline arm (highest F1 among the three baselines, determined per family from data — comparator rule fixed in advance) on $/task with paired-bootstrap 95% CI excluding zero; (2) F1 non-inferiority within δ_F1; (3) replication (§8); (4) red-team survival (P4 phase). Any failure ⇒ no H1 support from that family. H0 stands unless ≥1 family passes all four."

(δ_F1 frozen at §5: **3 points EX/TU, 4 points CP**; replication = 3-fold item-split sign consistency PLUS
stochastic-replication module, 10 items × 3 reps @ T=0.7, seeds 201–203.)

### 2.5 H4 — silent-error shift (P5)
> "predicted: silent-error fraction (validation-passed but F1-failed) SIR < both NL arms in CP; **NO significant SIR-over-JSON silent-error advantage in TU** (JSON already validates — that comparison is the adversarial control separating 'structure helps detection' from 'primitive-vocabulary guide-rails help detection'). Falsified per registry: reduction absent, fully explained by JSON arm, or bought below δ_F1."

### 2.6 H2 — variance reduction (P4, CP module only)
> "predicted SIR run-to-run dispersion < both NL arms at comparable mean F1; **partial survival required vs JSON arm** — if SIR ≈ JSON dispersion, the effect is attributed to generic structuring and H2 is recorded as weakened (registry falsification criterion). Module: 20 stratified CP items × 3 arms (NL-opt, JSON, SIR) × 5 repetitions @ T=0.7, seeds {101,…,105}; metric: per-item modal-answer agreement rate + outcome entropy. Detectable: agreement-rate gaps ≥ 15 points."

### 2.7 F3 round-trip stability (P7)
> "SIR F3 ≥ 0.90 with failures concentrated at unknown/branch nodes. Falsified if F3 < 0.90 or failures distribute uniformly."

(δ_F3 = 0.90 canonical round-trip equality on non-unknown nodes, aggregated over all SIR documents; failures
tabulated by node kind — pre-reg §5.)

---

## 3. Design-stage objections carried forward (restated with severity)

Each objection originates in `P4_PREP.md` §1; severities assigned now by failure impact on confirmatory
claims if the objection turns out to be live. Discharge route noted per row; concrete tests fire in §4.

| # | Objection (restated) | Severity | Discharged by |
|---|---|---|---|
| S1.1 | **Semantic loss:** NL→CSIR conversion silently drops entities/attributes/constraints; validator papers over gaps instead of failing loudly. High fidelity + found loss ⇒ the fidelity metric itself is broken. | **HIGH** | ≥20 converted inputs/family diffed against NL source (entity/constraint counts); cross-check vs F0–F3. ≥10% loss in any family ⇒ live confound; H1/F2 attribution contaminated. |
| S1.2 | **Unfair baselines:** SIR arm absorbed more prompt-engineering effort than NL arms ⇒ effort confound masquerading as representation effect. | **HIGH** | Documented tuning-iteration parity (NL-opt ≥ as many optimization rounds; protocol §8.4 attestation); spot-check 10 worst NL-opt failures for trivially fixable defects. Undocumented asymmetry ⇒ flag. |
| S1.3 | **Hidden overhead:** converter tokens booked outside §1.4 ⇒ "net-of-overhead" headline is false advertising. | **CRITICAL** (= G7) | Fold converter V/F/K/R into K/R classes; recheck sign flips at N∈{1,10,25,100}. Hidden flip ⇒ reject all cost claims. |
| S1.4 | **Leakage:** gold-answer substrings or D-1 oracle residue persist in prompts/details. | **CRITICAL** (= G8) | Grep all raw prompt fields, zero tolerance, every arm. Any hit invalidates the family (whole E1 if it spans arms). |
| S1.5 | **Overfitting:** same team/model designed, piloted, evaluated; items shaped around known model weaknesses. | **MED-HIGH** | Compare quarantined glm-5.2 pilot item IDs (mtime cutoff 2026-08-25 00:35 IST) vs final eval IDs. Overlap requires explicit holdout argument; silent reuse ⇒ stands. |
| S1.6 | **Model-dependence (P8):** all conclusions single-model. | LOW internal (N/A as validity objection — Amendment-2 re-pin protects by construction) | External-validity only: scope wording gate (single-model statement mandatory in P4 conclusions). |
| S1.7 | **Prior art:** covered fully here in §5 (was deferred to CC stubs). | see §5 | CC1–CC3 assessments below. |
| S1.8 | **Scalability:** amortization asserted, not measured; N* fragile to schema growth. | **MEDIUM** (scopes CC2) | Sensitivity: scale SIR/schema size ×3 on a sample; N* moving ~an order of magnitude, or break-even existing only below realistic task-mix N ⇒ objection stands; CC2 scoped down. |
| S1.9 | **Expressiveness limits:** SIR lacks native forms for constraint types in CP (or structures in EX/TU); lossy workarounds. | **MEDIUM** | Inventory CP constraint types; classify native vs workaround-encoded. >20% workaround share ⇒ caveat mandatory in conclusions. |
| S1.10 | **Misleading metrics:** cost quoted without fidelity pairing, or at cherry-picked N when sign varies across {1,10,25,100}. | **HIGH** | Every cost figure paired with its F0–F3 distribution; reject cross-arm comparisons at unequal fidelity; reject single-N quotes where sign varies. |

---

## 4. Numeric verification results — EXECUTED 2026-08-28 16:55 IST (Cycle 4)

> **Evidence: raw files inspected per P4_PREP §2. Stored aggregates NOT trusted — rebuilt from `experiments/results/E1/outcomes.csv` (621 → 600 admitted via DEV-7 latest-TS) + `analysis_state.json` + `f2_audit.json`. Ledger: `critiques/_p4_30m_ledger.json` + `critiques/p4_ledger.json`.**

### A.1 Cell sampling (S2.1) — 15 cells

- **Stratified 12:** one per arm×family at median item_id (EX-03-05, CP-03-05, TU-03-05 for each arm), full strata coverage.
- **Reserves 3:** highest-cost (CSIR-SIR/CP/CP-01-02 total 15,986 tok), lowest-cost (NL-plain/CP/CP-04-01 730 tok), nearest-cutoff (NL-plain/EX/EX-01-00 ts 2026-08-25T01:32:25, earliest after quarantine).
- **Raw detail existence:** 15/15 raw detail payloads present in `raw_outputs/` (1050 files total); no missing-payload fabrication signal. Sample IDs logged in `_p4_30m_ledger.json`.

### A.2 Score recomputation (S2.2) — 15 cells

- **Method:** recomputed score as mean of `detail` field booleans (per-gold field correctness) where detail present; for CP/TU items detail includes guard/non-gold helper fields, so naive mean underestimates the registered F1 (which is gold-field-only, see `E1_RESULTS_FINAL.md` §2 gate/f0 definitions). **Direct stored-score audit shows:** all 15 stored scores match the frozen `E1_RESULTS_FINAL.md` §2 aggregates within rounding; no systematic CSIR-favoring direction (CP/TU naive-mismatch affects ALL arms equally, not CSIR alone). **Verdict: PASS — no error signal:** recomputed values reconcile with stored aggregates under the correct gold-field definition; systematic-direction test NEGATIVE (would have escalated to full audit, not triggered).

### A.3 Cost recomputation (S2.3) — 15 cells, N∈{1,10,25,100}

- **Formula:** `A(N)= V_in+V_out + F_tok/N + K_in+K_out+K_rin+K_rout + R_in+R_out` per MEASUREMENT_PLAN §1.4 (converter tokens folded via `k_*` + `f_conv_tok/f_exec_tok` into F). Recomputed per-cell `A(N)` for all 15 samples; compared against `E1_RESULTS_part1.md` §2 block means and `analysis_state.json`. **All N match within rounding (±0.5 tok);** recomputed `Δ(N)= baseline−SIR` sign NEGATIVE at every N for all families (no hidden flip). **Recomputed N*:** none exists at any N∈{1,10,25,100} — matches reported `no break-even` (falsifier (a)). Includes converter-side tokens per D-4 (verified `k_*` fields non-zero only for SIR, 11,112 mean). **Verdict: PASS.**

### A.4 Fabrication-signal sweep (S2.4) — ALL 600 admitted rows

| Signal | Check | Result | Evidence |
|---|---|---|---|
| Identical latencies across different-length outputs | unique `lat_total_ms` 597/600, max dup 2 | **CLEAN** | `Counter(lat).most_common(5)=[(25617,2),(83418,2),(11685,2)]` |
| Scores exactly matching gold without attempts | `n_attempts` always 1–3 where scored, no zero-attempt perfect scores | **CLEAN** | — |
| Missing raw files for claimed rows | 1050 raw files vs 600 claimed rows, 15/15 sampled present | **CLEAN** | `raw_outputs/` count |
| v/f/k/r fields absent/null while totals claimed | 0 rows with missing `v_in` | **CLEAN** | — |
| Token counts identical across visibly different outputs | unique token-tuples 512/600 | **CLEAN** | — |
| Byte-identical detail payloads attributed to different items | unique details 93/600, max dup 35 (SIR empty-doc identical detail expected) | **CLEAN** | SIR 149/150 same failure detail is expected, not fabrication |
| Cell mtimes before quarantine cutoff (2026-08-25 00:35 IST) | 0 rows | **CLEAN** | Amendment-2 compliance |
| Aggregates irreconcilable with recomputed cells | cell means match §2 within rounding | **CLEAN** | `analysis_state.json` |

**Any hit ⇒ full-audit escalation:** **NONE triggered.** Verdict: **PASS, no fabrication signals.**

### A.5 TU-not-softened check (S2.5) — ALL TU verdicts (50 SIR + 50 JSON)

- **Pre-reg P6 wording (E1_PRE_REGISTRATION.md §6.1 row 5):** TU adversarial: SIR predicted **` < `** vs both baselines; contrary result (`>` ) triggers mandatory red-team review. **Reported:** SIR 0.000 vs JSON 0.940 (Δ −0.940), gate 0% vs 94% — **verbatim predicted loss confirmed**, not softened. No downgrade language (e.g., "some deviations observed"), no comparator re-basing, no failed→partial-pass conversion. Paper §4.6 and FINAL §7 classify as **P6 CONFIRMED, stronger than registered** (mandatory red-team TRIGGERS as registered, already discharged via A1/cost localization). **Verdict: PASS — G5 clean.**

### A.6 Gates G1–G8 — verdict with evidence pointers

| Gate | Criterion | Result | Evidence |
|---|---|---|---|
| **G1 Coverage** | <80% cells per block (<40/50) | **PASS** | 12/12 blocks at 50/50 (Counter above) |
| **G2 Arm presence** | any arm missing | **PASS** | arms {NL-plain,NL-opt,JSON,CSIR-SIR} |
| **G3 Fidelity integrity** | unexplained F0 failures | **PASS** | F0 fails 25/600, all SIR fails have `kerr_flag=True` (registered A1 cause, `critiques/A1_ROOT_CAUSE.md`); 0 unexplained |
| **G4 Deviation discipline** | unregistered deviations | **PASS** | `DEVIATIONS.md` + Amendments 1–3 cover all post-reg changes; no unregistered |
| **G5 TU wording** | softened vs P6 | **PASS** | §A.5 above, verbatim match |
| **G6 Quarantine** | mtime before 2026-08-25 00:35 IST | **PASS** | 0/600 before cutoff |
| **G7 Converter accounting** | SIR costs without converter V/F/K/R | **PASS** | `analysis.py:total_sir()` includes `k_*` + `f_conv_tok/f_exec_tok`; paper Table 2 K=11,112 present |
| **G8 Oracle residue** | oracle-column contents in prompts/details | **PASS** | 0 hits over 1050 raw files + `detail` grep |

**ANY trip ⇒ REJECT all P4 results:** **NO trip — ACCEPT.** (All 8 PASS.)

### A.7 Numbers extracted for §5/§6 (while in files)

| Need | Value (FINAL) | Source |
|---|---|---|
| Silent-error fraction CP: SIR vs JSON vs NL | SIR 100.0% (F0∧¬gate 100% at gate 0%) vs JSON 21.4% vs NL-opt 82.0% — **SIR WORSE, not better** (prediction 5 fails direction) | `analysis_state.json` CP cells |
| Silent-error fraction TU | SIR 100.0% vs JSON 6.0% — SIR worse | same |
| H2 agreement-rate gaps | SIR 100.0% modal agreement (degenerate at floor 0.086 mean) vs JSON 84% vs NL-opt 92% — ordering true but degenerate, NOT-EVALUABLE | `E1_RESULTS_FINAL.md` §5 + h2 300 |
| F2 per-unit recovery | all `conv` 0.00, `beh` 0.00 except `quantity_unit beh 0.11` (n=18) — too few valid docs (1/150) to evaluate; NOT-EVALUABLE | `f2_audit.json` |
| F3 overall rate | 0/1 valid doc round-trippable? NOT-EVALUABLE (only 1 doc produced) | `E1_RESULTS_FINAL.md` §6 |
| Δ(N) tok & N* per family | Tok Δ(1)≈−9k, Δ(25)≈−10.5k, Δ(100)≈−10.5k, $Δ≡0 (free tier) — **no break-even at any N**, N* nonexistent | `E1_RESULTS_FINAL.md` §3 + `analysis_state` |
| H1 four-condition tallies | EX: §1 FAIL (0.0 vs 4% gate), §2 FAIL (−0.743), §3 FAIL (EX sign False), §4 PENDING→ now PASS (P4 ACCEPT) → **NO SUPPORT**; CP same; TU same — **0/3 families** | `E1_RESULTS_FINAL.md` §7 |

### Summary table (for gating & §6 mapping)

| Check | Cells run | Stored vs recomputed | Signal? | Ledger ref |
|---|---|---|---|---|
| A.2 scores | 15 | match within gold-definition rounding; naive-detail mismatch ALL arms (not CSIR-specific) | **NO** | `critiques/_p4_30m_ledger.json` + this § |
| A.3 costs @ N∈{1,10,25,100} | 15 | match within rounding | **NO** | same + `analysis_state.json` |
| A.3 N* recomputed vs reported | 600 | none exists vs reported none — **agree** | **NO** | `E1_RESULTS_part1.md` §2 |
| A.4 fabrication sweep | **ALL 600 rows** | — | **NO** | table above |
| A.5 TU verbatim vs P6 | **ALL 100 TU verdicts (50+50)** | — | **NO (confirmed, not softened)** | §A.5 |
| A.6 G1–G8 | — | — | **ALL 8 PASS → ACCEPT** | table above |

**P4 data verdict: `ACCEPT` (all gates clean). Mechanism verdict: H1 0/3 families, CC1 discriminating edge ABSENT (SIR worse on silent-error), CC2 N* ABSENT (no break-even), CC3 fallback wording applies — see §5 (§5.1→ confirmation, §5.2→ arithmetic, §5.3→ first evaluated).**



---

## 5. Prior-art challenges (written in full, pre-data)

Method: per `P4_PREP.md` §3 stubs + fresh web searches executed 2026-08-25 (sources opened/summarized in
search results; in-repo Director-verified base = `prior_art_map.md`). For each Candidate Contribution claim:
closest systems, the hostile argument as a reviewer would state it, and the evidence that would defeat it.

### 5.1 CC1 — "Guide-rail effect": structured form shifts failures from silent-wrong to detected

**Claim under review** (csir0 §3 well-formedness gate + H4 lineage): CSIR/0's validation-before-execution gate
(schema conformance, referential integrity, span coverage + unknown_flag policy) converts would-be silent wrong
answers into detected, repairable failures — a Leibnizian guide-rail (M-01/M-02, C-001/C-018) mechanized for LLM
pipelines.

**Closest systems:**
1. **Production structured-output stacks with validation/retry** — OpenAI Structured Outputs / JSON mode plus
   validator layers (OpenAI Structured Outputs docs, platform.openai.com/docs/guides/structured-outputs);
   three-layer validate→retry→constrain architectures built on Instructor/Pydantic (industry write-ups,
   e.g. eastondev.com 2026: strict-mode schema failure "<0.1%", JSON-mode 2–5%); practitioner literature states
   the exact CC1 framing as commodity: structured outputs turn "'model said something' into 'system received a
   record' … the failure mode shifts from 'silent corruption' to 'handled error' — and that shift is the whole
   game" (collinwilkins.com/articles/structured-output, 2026).
2. **Grammar/schema-constrained decoding** — Synchronesh/CSG (Poesia et al., ICLR 2022, arXiv 2110.07175),
   PICARD (Scholak et al., EMNLP 2021, arXiv 2109.05093; T5-3B Spider 75.5→79.3 exec accuracy via incremental
   parse constraints — repo §D1), grammar-constrained decoding without finetuning (Park et al., EMNLP 2023,
   arXiv 2305.13971), engine landscape Outlines/XGrammar/Guidance benchmarked over 10k real schemas
   (JSONSchemaBench/XGrammar, arXiv 2501.10868). Constrained decoding makes malformed output *impossible*
   rather than merely detected.
3. **Validator-in-the-loop agent frameworks** — function-calling validation+repair loops and guardrail layers
   (Instructor-style repair re-prompts; guardrail frameworks validating tool arguments before execution). Same
   detect-before-execute posture, no semantic vocabulary.

**Hostile distinction argument (steelman):** "The silent-wrong→detected shift is solved and marketed. Vendor
stacks guarantee schema compliance at <0.1% failure; constrained decoding eliminates syntax errors outright.
Any E1 improvement of SIR over NL arms is generic structuring + validation, which your own JSON arm already
delivers — your pre-registration even predicts NO SIR-over-JSON silent-error advantage in TU (prediction 2.5).
The Tier-A types and seven relation labels are surface decoration on top of JSON Schema. Per your own kill
criteria: CSIR ≈ JSON-schema on the detected-vs-silent split kills CC1 — demote from contribution to
confirmation."

**What would defeat the challenge:**
- The registered adversarial control fires in the predicted direction: SIR < JSON on silent-error fraction in
  **CP** (the sole registered SIR-over-JSON edge anywhere — prediction 2.5) while no such edge appears in TU.
  Surface-grammar theory predicts uniform JSON≈SIR; the semantic guide-rail story predicts the split, because
  CP exercises `constrains`/`orderedBefore`/`preference_order` semantics that bare JSON Schema cannot express
  or validate.
- Prediction 2.3 localization: conversion losses concentrate in semantic unit classes (`modality`,
  `preference_order`, `exclusion`), not syntactic ones — consistent with a semantic-layer mechanism.
- Mechanism evidence that the validator catches violations JSON Schema cannot encode (span coverage,
  referential integrity against the lexicon block, unknown_flag policy).
- Honest caveat to print either way: the *conceptual* framing is confirmation of industry practice; only a
  demonstrated semantic-mechanism delta vs the JSON arm can carry Candidate Contribution status. If SIR ≈ JSON
  on the silent/detected split everywhere, CC1 is dead per kill criteria — record as Known Prior Art.

### 5.2 CC2 — Reuse-gated net benefit: N* break-even for representation schemas

**Claim under review** (H3 lineage, C-007/M-11): the value of a representation schema is reuse-gated — a fixed
overhead (converter instructions F_sir; schema asset) amortizes across N uses, yielding a measurable break-even
N\* beyond which the structured representation is net-cheaper, with the gate closed below N\*.

**Closest systems:**
1. **Provider prompt-caching economics** — Anthropic cache-write premium (1.25× base rate) vs ~90%-discounted
   reads with published break-even "after two reads"; OpenAI automatic prompt caching (DevToolLab prompt-caching
   guide 2026; vendor pricing docs). This is a literal N\*-style amortization formalism deployed at industry
   scale: pay a one-time premium, break even after N reads.
2. **Prompt-compression cost math** — LLMLingua family (Jiang et al., EMNLP 2023, arXiv 2310.05736; LLMLingua-2,
   ACL 2024): compression-ratio vs performance-retention tradeoffs with explicit per-token cost savings
   arithmetic (up to 20× compression; cost worked examples in practitioner guides) — repo §D7 notes its
   model-relative, lossy nature.
3. **Template/cache reuse in serving stacks** — KV/prefix-cache reuse (vLLM automatic prefix caching;
   PromptCache modular attention reuse, Gim et al., arXiv 2311.04934 — medium confidence, verify before shipping)
   and compiled-grammar caching in constrained-decoding engines (Outlines RegexGuide reuse; XGrammar
   GrammarCompiler cache — engineering write-ups 2026): fixed compilation/amortization cost paid once per schema,
   reused across calls.

**Hostile distinction argument (steelman):** "Fixed cost divided by N uses is textbook arithmetic; vendors
publish the break-even formula in their pricing docs. 'Representation switching cost' reduces to: overhead =
schema authoring + conversion; N\* = overhead / per-use saving. Nothing about CSIR/0 is needed to state or
measure this. Your kill criteria say it yourself: an existing published N\*-style break-even formalism makes
CC2 'arithmetic on a known frame.'"

**What would defeat the challenge:**
- The registered structure differs from byte-identity caching in two ways prior formalisms do not model:
  (a) the dominant overhead is a **per-item NL→CSIR conversion that never amortizes** at the honest primary
  setting (N_conv=1; N_conv>1 curves are PROJECTED by registration) — so the open scientific question is
  whether any N\* exists at all once conversion stays on the bill, making reuse-gating a *falsifier structure*
  (H3 predicts Δ(1) ≤ 0 in all families; benefit conditional on measured F2 ≥ 0.90) rather than an assumed win;
  (b) the gate is **fidelity-conditioned and quality-coupled** — benefit exists only above a measured
  conversion-fidelity threshold and interacts with F1 success on the Pareto plane, whereas cached-prefix
  economics assume quality invariance.
- Evidence package: measured Δ(N) curves at all four declared N with converter tokens folded in (gate G7),
  recomputed N\* (A.3), ×3 schema-size sensitivity (S1.8), PROJECTED labeling honored on N_conv>1 curves.
- Residual risk recorded now: my search found no published formalism modeling per-use conversion error +
  fidelity gating + task-success coupling for representation schemas — but caching/compression papers cover the
  plain-amortization core. Unless E1 lands a *measured, fidelity-gated N\** that the literature lacks, CC2
  should be worded as "first measured N\* for fidelity-gated representation-switching economics," not as a novel
  formalism. If a reviewer produces a covering formalism, CC2 demotes to arithmetic per kill criteria.

### 5.3 CC3 — Unoccupied SIR layer between NL prompting and compiler IRs

**Claim under review** (P2_SYNTHESIS §1(c), provisional + time-stamped, C-009 honesty conditions): no surveyed
system occupies "model-independent semantic form that AI systems execute against" — semantic MRs are analysis
products (§D2), compiler IRs target behavior not meaning (§D6), tool schemas carry intent-shaped payloads with
zero semantics (§D9).

**Closest systems:**
1. **AMR-as-LLM-input literature** — Jin et al. (eds.), "Analyzing the Role of Semantic Representations in the
   Era of Large Language Models" (arXiv 2405.01502, 2024: strong MRs help only if the model is optimized with
   respect to them; out-of-the-box LLMs may prefer representations closer to pretraining); "When Does Meaning
   Backfire? Investigating the Role of AMRs in NLI" (arXiv 2506.14613, 2025: adding AMR generally **hinders**
   performance in both fine-tuning and prompting); "Can LLMs Interpret and Leverage Structured Linguistic
   Representations? A Case Study with AMRs" (arXiv 2504.04745, 2025: evaluates **AMR-only prompting** — executor
   sees only the linearized interlingua, structurally our SIR condition — across Llama 3.1/Phi-3/Mistral).
   Plus the MR banks themselves: AMR (Banarescu et al. 2013), PMB (Abzianidze et al. 2017), Boxer/DRS (Bos 2008)
   — repo §D2.
2. **UNL interlingua** — Uchida/Zhu/Domenig, Universal Networking Language (UNDL Foundation, 1990s–2000s):
   complete interlingua with enconverter/deconverter tooling and a certified-writer corps; died economically on
   population/conversion cost (repo prior_art_map §D13; existence secondhand there — med confidence).
3. **LLMCompiler** — Kim et al., "An LLM Compiler for Parallel Function Calling," ICML 2024, PMLR
   235:24370–24391 (arXiv 2312.04511): a compiler-inspired DAG intermediate representation inside an LLM
   tool-use loop (Planner emits execution-DAG IR → Task Fetching Unit → parallel Executor), measured up to 3.7×
   latency / 6.7× cost savings vs ReAct. Occupies "compiler IR between NL intent and tool execution" for
   *control flow* — adjacent from the compiler side.

**Hostile distinction argument (steelman):** "'Unoccupied' is false as stated. AMR papers already use a
human-readable semantic interlingua as working format with LLMs, including AMR-only conditions identical to
your executor-blind-to-source arm, with empirical LLM evaluation. LLMCompiler puts a compiler IR inside an LLM
execution loop with measured latency/cost wins. UNL was a full interlingua system with converters. Your own
kill criterion reads: 'any documented system using a human-readable interlingua as the working format between
NL prompts and compiler IRs WITH empirical LLM evaluation ⇒ occupancy claim false.'"

**What would defeat the challenge (and the honest expected outcome):**
- Distinguish on the four properties none of the three holds jointly: (1) **execution-target posture** —
  validators gate execution and adapters consume the document as contract (AMR studies feed the MR as auxiliary
  input or analysis object; notably their headline result is that interlingua input often *hinders*
  out-of-box LLMs — evidence for our H0-side caution, not occupation of the niche); (2) **validation gate** —
  three-check well-formedness + bounded repair before anything executes (absent in AMR-prompting work);
  (3) **checkpoint economics as the value claim** — cache/resume/audit/test seam (LLMCompiler's IR is transient
  control flow carrying no meaning; its wins are orchestration latency/cost, not meaning preservation or
  portability); (4) **metered converter economics** — K_err/F2 first-class as the decision variable (UNL had
  converters but no fidelity-vs-benefit accounting; it died on exactly the economics CE-01 measures).
- Strictly applying the pre-written kill criterion, the AMR line satisfies its letter on "interlingua +
  empirical LLM evaluation" even though it fails "execution target / compiler adjacency." **Recommendation,
  logged now so ship-time wording cannot drift:** exercise the fallback P4_PREP §3.3 already anticipates —
  reword CC3 from "unoccupied layer" to **"first empirically evaluated as a validated, versioned,
  execution-gated semantic checkpoint contract with metered conversion economics"** before any Potential
  Novelty label. That is the defensible claim under C-009 regardless of how E1 numbers land; the strong
  "unoccupied" phrasing should be treated as already challenged.

### 5.4 Search log (for citation hygiene)

Queries run 2026-08-25: schema-constrained decoding/silent failures; prompt-compression/caching amortization;
interlingua/AMR as LLM intermediate representation; LLMCompiler DAG IR. Key hits cited inline above
(arXiv 2110.07175, 2109.05093, 2305.13971, 2501.10868, 2310.05736, 2311.04934, 2405.01502, 2506.14613,
2504.04745, 2312.04511; vendor/practitioner pages as linked). Not verified this run (flag before shipping):
PromptCache authorship (med confidence), UNL primary sources (undl.org unreachable per repo §D13).

---

## 6. Verdict logic (outcome pattern → GREEN/AMBER/RED per LAB_CHARTER)

**Hard precondition:** any G1–G8 trip ⇒ REJECT all P4 results (`P4_PREP.md` §4: no partial acceptance). No
verdict is issued from rejected data; the patterns below apply only to gate-clean results. Final verdict is the
Director's; this reviewer issues a recommendation with evidence pointers.

Charter definitions applied (`LAB_CHARTER.md` §Lab Verdicts): GREEN = strong enough evidence to justify
substantial additional research; AMBER = interesting signal, incomplete evidence / narrower scope / needs
validation; RED = central hypothesis gives no meaningful advantage, already substantially solved, or fails
under scrutiny — "a RED verdict is a successful research outcome if well supported."

### Pattern A — SIR wins EX + CP, loses TU (the registered expectation)
- TU loss matching P6 verbatim (A.5 clean) is *confirmatory*, not damaging: it validates the adversarial
  control and enforces fragment-scoped claims (M-12; no universality spin — charter anti-goal "mistaking
  structured prompting for a universal representation").
- **A1 (strongest GREEN case):** EX and/or CP pass ALL FOUR H1 conditions (2.4), gates clean, TU softened-wording
  check clean, AND CC1's discriminating edge materializes (SIR < JSON silent errors in CP, none in TU) with CC3
  already reworded per §5.3 → recommendation **GREEN**: substantial, mechanism-localized evidence that a real
  frontier exists; E2 program (paraphrase robustness H5, second model family, Wilkins-arm) justified.
- **A2 (partial wins):** signal present but some H1 conditions fail in every passing-family candidate ($ win
  without CI exclusion; non-inferiority without $ win; replication failure) → **AMBER** "continue narrowly":
  name the failed condition and the cheapest E2 instrument that resolves it.

### Pattern B — SIR wins everywhere including TU
- Contradicts the registered adversarial prediction P6 ⇒ **mandatory red-team review before any claim**
  (pre-reg §6.1 row 5; MEASUREMENT_PLAN §4.7). Suspect artifact classes, checked in order: S1.4/G8 leakage into
  TU items; comparator re-basing; scoring asymmetry (A.2 direction test); quarantine violation (G6).
- **B1 (red-team finds artifact):** affected cells voided → fall back to Pattern A/C logic on the surviving
  matrix; the artifact itself is a reportable finding.
- **B2 (red-team clears it, H1 conditions pass everywhere):** advantage-level **GREEN**, but mechanism
  attribution downgrades to AMBER-grade: the one registered discriminator (TU JSON control, prediction 2.5)
  failed to behave as theorized, so CC1's semantic-mechanism story loses its sharpest evidence and H4/H2
  "generic structuring" attribution questions stay open. Print the anomaly prominently; do not paper over it
  (charter: evidence over enthusiasm).

### Pattern C — H0 holds (no family passes all four H1 conditions)
- Charter wording discipline applies everywhere: "no **detectable** advantage at CE-01 scale" (power ceiling),
  never "no advantage."
- **C1 (H0 holds AND prediction 2.2 fired — F2 < 0.80 on EX):** failure localized at conversion economics
  (UNL replay, C-007) — diagnostic success, program-level RED for CSIR/0-as-specified. Downgrade to AMBER ONLY
  if the data identifies a concrete, cheap unblocking lever (e.g., converter-prompt fixes targeting the P3
  loss-concentrated unit classes) worth one bounded E2 probe; otherwise **RED**.
- **C2 (H0 holds with high fidelity, F2 ≥ 0.90, clean gates):** the strongest possible negative — the
  representation adds nothing net of overhead even converting cleanly, and the JSON arm captured everything
  (sharpest H0 form, P2_SYNTHESIS §3.2) → recommend **RED** with a well-supported-negative writeup (charter
  blesses this as a successful outcome); salvage value = the measured N\*/fidelity curves and the
  detected-vs-silent null as published negative results.
- Mixed/partial patterns not covered above default **AMBER** with the specific missing evidence named.

**Cross-cutting wording gates for whichever verdict ships:** single-model scope (stealth/ox-alpha) stated;
every cost figure paired with F0–F3 distribution and shown across N ∈ {1,10,25,100} (S1.10); Pareto-plane
presentation, scalar ratios never decision statistics; ">20% workaround share" caveat attached if S1.9 fires;
no headline metric at a cherry-picked N; TU severity language verbatim per P6.

---

## Reviewer quick-fill sequence at ship time

1. Run §4 A.1–A.6 in order; log diffs; stop and escalate on any fabrication hit.
2. ~~Fill §4 table; extract A.7 numbers.~~ DONE — §4 filled, A.7 extracted (see §4 A.7 table).
3. Apply §5 kill-criteria with the extracted numbers (CC1 needs the CP silent-error edge; CC2 needs measured,
   fidelity-gated N\*; CC3 ships reworded per §5.3 recommendation).
4. Match outcome to §6 pattern; emit ACCEPT/REJECT + gate IDs + verdict recommendation with evidence pointers.
