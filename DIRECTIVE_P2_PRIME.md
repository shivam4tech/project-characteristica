# DIRECTIVE — P1 Exit Review & P2 Synthesis (CE-01)

**From:** Operator via coordinator session, 2026-08-24 ~13:55 IST
**Context:** All six P1 workstreams DELIVERED and coordinator-verified on disk (zero placeholders across every file). Budget: 14.8h used / 40h cap. You are resuming as Research Director for a bounded engagement.

## Your Tasks

### 1. P1 exit review (~30 min)
Read these deliverables yourself — do not trust this summary:
- `literature/leibniz_extraction.md` (716 ln; note its escalation: Generales Inquisitiones NOT in Gerhardt vols 4/7 — Couturat 1903 is the first print; GI passages remain unstudied)
- `literature/pre_leibniz/gate_rulings.md` + 6 extraction files (Jungius honestly DEFERRED)
- `literature/post_leibniz/formal_systems_extraction.md` (371 ln, §8 synthesis)
- `literature/modern/prior_art_map.md` (196 ln, 16 domains)
- `benchmarks/MEASUREMENT_PLAN.md` (267 ln)
- `literature/modern/ir_analogy_assessment.md` (142 ln, FINAL)
Sign the P1 exit in STATUS.md if standards hold; log any deficiency as a blocked item instead of silently proceeding.

### 2. Cross-workstream synthesis → `expeditions/CE-01/P2_SYNTHESIS.md`
The workers independently converged on these candidate mechanisms — stress-test them against the files above:
(a) **Conversion economics is the recurring historical killer** (Descartes' primitives-first deadlock → UNL enconversion → ACE learnability → ontology engineering bottleneck), NOT formal expressive weakness.
(b) **A1+A2+A4 hard trade-off** (display + full calculus + universality): no historical system achieved all three; AAAI-25 recursive-isomorphism result says representation choice cannot carry intrinsic advantage.
(c) **The SIR layer is unoccupied**: analysis MRs (AMR) are not execution targets; compiler IRs target behavior not meaning; tool schemas carry intent-shaped payloads with zero semantics.
(d) **LLVM/MLIR vs Cyc/UNL split**: neutral intermediate layers win when stable+versioned+tooled; semantic layers die on population/maintenance economics.
Deliverable: unified mechanism map; ≥1 candidate SIR architecture sketch in `systems/` with primitive/composition/inference/ambiguity/extensibility choices each traced to ≥1 registered mechanism claim; derived sub-hypotheses for `hypotheses/REGISTRY.md`; falsifiable predictions for E1 consistent with MEASUREMENT_PLAN.md.

### 3. Open items to register (not solve now)
- GI passages need a follow-up extraction (Couturat 1903 / Schupp sources) before P3 if any E1 hypothesis leans on Leibniz's contingency theory
- Lingenic full text still unretrieved (Cloudflare); LINGENIC_CRITICAL_ANALYSIS.md at project root remains skeleton-with-TODOs
- Jungius deferral; New Essays Dalgarno/Wilkins loci; Kircher letter claim downgraded to Unresolved — keep out of any citation chain until resolved

## Constraints
- This engagement: ≤2.0 agent-hours. Charge honestly to STATUS.md when done.
- Do NOT spawn delegate_task batches — write your own synthesis. (Parent-exit teardown rule.)
- No notation design yet (P2 rule). Architecture sketch = structure + semantics choices, not pretty syntax.
- If evidence does not support convergence point (a), say so plainly — H0 remains live.
