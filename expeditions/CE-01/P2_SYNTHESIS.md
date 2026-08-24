# P2 Synthesis — Cross-Workstream Mechanism Map (CE-01)

**Author:** Research Director (characteristica-prime session), 2026-08-24
**Inputs:** all six P1 deliverables, inspected directly by the Director during P1 exit review (not accepted on worker self-report): `literature/leibniz_extraction.md` (716 ln); `literature/pre_leibniz/gate_rulings.md` + 6 extraction files (289 ln); `literature/post_leibniz/formal_systems_extraction.md` (371 ln, §8 synthesis); `literature/modern/prior_art_map.md` (196 ln, 16/16 domains); `benchmarks/MEASUREMENT_PLAN.md` (267 ln); `literature/modern/ir_analogy_assessment.md` (142 ln). Claim IDs below reference CLAIM_LEDGER.md rows C-001–C-019.
**Status:** P2 deliverable. Companion artifacts: candidate architecture at `systems/csir0_architecture.md`; derived sub-hypotheses H2–H5 in `hypotheses/REGISTRY.md`.

---

## 1. Convergence points stress-tested

The directive asked four convergence claims to be tested against the files, not merely collated. Results:

### 1(a) "Conversion economics is the recurring historical killer" — SUPPORTED with one refinement

**Evidence for:** Descartes' primitives-first deadlock (pre-Leibniz extraction: representation engineering blocked on a completed metaphysics); Wilkins' tree-surgery maintenance cascade; UNL's certified-writer economics explicitly identified as the failure mode ("The interlingua was never the bottleneck; getting *into* it was", §6); ACE's own admission of being a formal language that must be learned (1–2 days + fluency, §5); OWL's ontology-engineering burden (§7); Cyc's decades of manual assertion entry (prior_art_map §D4); IR assessment: golden-suite curation ≈ 20% velocity permanently (§4).

**Refinement (recorded as C-007):** the single-cause reading is too strong. A SECOND failure class exists — **foundational/theoretical collapse** — which killed claims rather than artifacts: Russell's paradox broke Grundgesetze; Gödel capped PM's universality from inside; Carnap's tolerance dissolved the single-language ideal; Leibniz's valuation calculus was never constructed and he said so himself (GP VII 126). The two classes interact: Class-II collapses freed survivors to be re-scoped as machinery (Boolean algebra → circuits/SQL; PM → type theory), while Class-I economics is what prevented any of them from living as universal *languages*. For CE-01 this means E1 must meter conversion overhead first-class (it does — MEASUREMENT_PLAN §1.2) AND avoid selling calculus-grade guarantees the record shows are unstatable for intent (IR D1/D2 do).

### 1(b) "A1+A2+A4 hard trade-off" — SUPPORTED, strengthened by modern corroboration

Post-Leibniz §8.1: across Frege, Peano/Russell, Boole/Schröder, Carnap, ACE, UNL, DL/OWL, no system maximizes more than two of {display language, full calculus, universality}. This is now corroborated twice independently: (i) historically by the seven-system grid; (ii) theoretically by the AAAI-25 recursive-isomorphism result (C-008) — since all universal formalisms are intercompilable, no point on the surface can dominate another on expressive power, so trade-offs are the *only* possibility. Pre-Leibniz data adds the origin: Descartes set the terms (primitives-first deadlock) and Leibniz's own fragments show him buying A2-partial at the cost of scope restrictions declared inside his systems ("propositiones negativas ... nunc non attingemus", GP VII 218). **Design consequence adopted in CSIR/0:** choose the point explicitly — validated structure (A2-adjacent checking) + checkpoint usability (partial A5-for-machines) — and pay openly in universality (scope = pre-registered task families) and display (spans preserved but graph not human-fluent).

### 1(c) "The SIR layer is unoccupied" — SUPPORTED provisionally, time-stamped, PI review mandatory

Prior-art map cross-domain #1: analysis MRs are products not execution targets (§D2); compiler IRs target behavior not meaning (§D6); tool schemas carry intent-shaped payloads with zero semantics (§D9). No surveyed system occupies "model-independent semantic form that AI systems execute against." Two honesty conditions attached (C-009): the claim is med-high confidence and time-stamped 2026-08-24, and it must survive independent Prior-Art Investigator review before any Potential Novelty label — vendor agentic plan formats are converging toward intent-shaped structured payloads from the schema side, and that motion could close the gap from below within months. Nothing in CE-01 currently depends on novelty; H1/H0 are about net advantage, not firstness.

### 1(d) "LLVM/MLIR vs Cyc/UNL split" — SUPPORTED, with the load-bearing variable named

Neutral intermediate layers win when stable + versioned + tooled **and their endpoints are bounded** (N frontends × M backends closes the amortization argument, IR §1 P7). Semantic layers die when population/maintenance economics don't close (Cyc, UNL, Semantic Web standards). Wikidata (§D5) shows semantic infrastructure *can* reach web scale — 123M items — only under crowd maintenance + versioning + shallow semantics (triples carry no events/context/intent). The split therefore reduces to one variable: **who pays population cost, and does per-unit cost go to ~zero?** Compilers answered with bounded machine endpoints; Wikidata with crowdsourcing + shallow units. An intent-depth SIR can use neither answer directly — its units are deeper and its front end unbounded. The only available population mechanism is LLM converters (near-zero marginal authoring cost), which is precisely why converter fidelity (K_err, F2 conversion-stage) is the single most decision-relevant measurement CE-01 will make (P1/P2 predictions in csir0_architecture.md §9). This also explains why the IR-assessment inversion (§4b) matters: pivot economics never close for unbounded phrasings, so SIR value must be sought in checkpoint properties (cache/resume/audit/test), which ARE bounded-endpoint benefits.

## 2. Unified mechanism map (OQ1 × OQ2)

Recurring mechanisms across ≥2 eras, each mapped to its modern analogue(s) and disposition. "Disposition" states what CE-01 does with the mechanism.

| # | Mechanism (recurs across) | Modern analogues | Disposition |
|---|---|---|---|
| M-01 | **Guide-rail representation**: structure that prevents deviation for ordinary operators (Leibniz P1 bridge-railing; Wilkins self-interpreting characters; ACE determinism) | Schema-constrained decoding (PICARD, prior_art_map §D1); JSON-schema validation | Adopted: validation-before-execution gate (C-001, C-018); measured via H4 silent-error endpoint |
| M-02 | **Self-detecting malformation**: nonsense visibly malformed ("ineptiae sese ipsae prodent"; paralogism = soloecismus; PM checkable derivations) | Type systems; parser validators; CI gates | Adopted: F0 gate + bounded repair loop (C-001); basis of H4 |
| M-03 | **Two-tier vocabulary**: analyzed core + licensed opaque technical terms (Leibniz Chinese analogy GP VII 203; Dalgarno/Wilkins radical tables) | Typed ID systems (QIDs); enum vocabularies; tool registries | Adopted: Tier A closed / Tier B open-opaque (C-017); avoids C-004 trap |
| M-04 | **Composibility/well-formedness gate on generation** (Leibniz GP VII 294; DL consistency services) | OWL reasoners; schema validators; program-synthesis oracles | Adopted mechanized form: referential-integrity + span-coverage checks (C-018) |
| M-05 | **Dual readings must be declared, never silent** (Leibniz intension/extension clause GP VII 224 → historical paradox charges) | Intensional vs extensional KR duality; OWL open-world vs closed-world posture | Adopted: one declared reading per relation label + explicit intensional modifier (C-003) |
| M-06 | **Deduction ≠ valuation**: proof calculi marketed as decision procedures fail where weights are needed (Leibniz statics of reasons, value-units never built, GP VII 125–126) | Utility/scoring layers; calibrated uncertainty; decision theory | Adopted as refusal: CSIR/0 carries modality/preference status but computes nothing (C-002) |
| M-07 | **Compression-by-generalization with recovery discipline** (Leibniz sciences-shrink-as-they-grow GP VII 180 f.) | MDL; prompt compression (LLMLingua — model-relative, rejected as model) | Partially adopted: F accounting follows Protocol §6; no lossy statistical deletion permitted (C-012 ground 3) |
| M-08 | **Conditional-output honesty**: conclusions inherit premise status (Leibniz vi formae GP IV 429–430) | Proof assistants' assumption tracking; hypothesis flags | Adopted: premise-status attribute propagated (leibniz_extraction P12) |
| M-09 | **Codebook substitution without composition fails** (Beck numerals; Kircher word-tables → word-substitution MT) | Naive prompt-codebooks; bilingual dictionaries | Kept as control condition: predicts collapse on compositional items (kircher file, experimental implication) |
| M-10 | **Canonical typed identifiers reduce ambiguity but pay inventory/schema overhead** (Wilkins radicals; Beck codes as degenerate case) | QIDs/URIs; DBpedia; faceted classification | Testable arm, not core: Wilkins-arm pilot listed in wilkins_1668.md implication; deferred to E2 unless budget allows |
| M-11 | **Conversion/authoring economics decide adoption** (Descartes deadlock → UNL writers → ACE learnability → OWL engineers; LLVM stability bargain inverted) | Learned encoders as near-zero-cost populators — the new variable absent from every prior attempt | Central measurement target: K_tok/K_err/F2-conversion (MEASUREMENT_PLAN §1.2); H3, predictions P1/P2/P3 |
| M-12 | **Fragment-by-fragment scoping beats universal claims** (Leibniz's own scope deferrals; Carnap tolerance internalized in OWL profiles) | DL profiles EL/QL/RL; DSL ecosystems | Adopted: scope = pre-registered families only (C-006 consequence) |
| M-13 | **Structural match ≠ meaning preserved** (smatch above-human-IAA parsers still distorting; Opitz & Frank acceptability data) | All graph-matching MR metrics | Measurement constraint: F1-primary/F2-audit stack (C-019); bans smatch-style headline metrics |

Cross-cutting negative space (mechanisms conspicuously ABSENT from every survivor): complete primitive inventories (A3 — dead 250 years, C-004); intrinsic expressive advantage (dead by theorem, C-008); guarantee-bearing translation of informal meaning (dead by D1/D2, C-011). Any future proposal reintroducing these carries the full burden of the registered refutations.

## 3. Where the evidence does NOT converge (H0 remains live)

Per directive instruction, stated plainly:

1. **No positive existence proof exists yet.** Every mechanism above is either a failure lesson or an untested design bet. Nothing in P1 evidences that an SIR *can* beat strong NL prompting net of overheads; the historical record's base rate argues it usually cannot (every universal-language artifact died as language; survivors live as invisible machinery).
2. **The JSON/schema arm may capture everything.** The sharpest version of H0 (registry, H1 competing explanation): if optimized JSON schemas + validation already deliver guide-rail, malformation-detection, and reuse-amortization effects, then "SIR" adds nothing but vocabulary — prediction P5/P6 in csir0_architecture.md §9 registers exactly this discriminating test (no predicted SIR-over-JSON advantage except in planning-family silent-error reduction, and even that is H4's bet, not a certainty).
3. **Converter fidelity is an empirical unknown that could zero the whole program.** If F2 conversion-stage unit recovery lands <0.80 on extraction tasks, prediction P2 fires and Δ(N)<0 everywhere — the UNL replay. The architecture is designed so this failure would be diagnostic rather than fatal to knowledge (it would localize the wall precisely), but Director judgment is that P(H3 supported somewhere) is genuinely uncertain — 50/50 at best, not optimism-driven.
4. **Power ceiling acknowledged:** MEASUREMENT_PLAN §4.5 — CE-01 can only detect large effects; "no detectable advantage at CE-01 scale" is the strongest negative finding available. Small true advantages (<10 pts) are invisible here regardless of outcome.

## 4. Deliverables produced by this session

| Artifact | Path | Content |
|---|---|---|
| Claim ledger transcription (C-001…C-019) | CLAIM_LEDGER.md | 19 rows transcribed from verified deliverables incl. Director refinement of convergence point (a) |
| Derived sub-hypotheses | hypotheses/REGISTRY.md | H2 (consistency), H3 (reuse-gated benefit), H4 (malformation detection), H5 (paraphrase robustness cost), each tracing to ledger IDs |
| Candidate SIR architecture | systems/csir0_architecture.md | CSIR/0: structure + semantics choices, each traced to ≥1 mechanism claim; 8 falsifiable E1 predictions consistent with MEASUREMENT_PLAN.md; explicit non-claims; no notation design (P2 rule honored) |
| This mechanism map | expeditions/CE-01/P2_SYNTHESIS.md | Stress-tested convergence points; unified mechanism table M-01…M-13; negative-space register; honest divergence section (this §3) |

## 5. Registered open items (not solved here)

| Item | Ledger | Blocking condition |
|---|---|---|
| Generales Inquisitiones primary extraction (Couturat 1903 Opuscules / Schupp) before any E1 hypothesis leaning on Leibniz's contingency theory | C-015 | Conditional: registered H2–H5 do NOT lean on contingency theory, so P3 entry is NOT blocked; revisit if hypotheses change |
| Lingenic full text (SSRN 403 Cloudflare) + missing LINGENIC_CRITICAL_ANALYSIS.md | C-016 | File absent from repo contrary to directive description — logged, not reconstructed from memory; Lingenic stays out of all citation chains until primary text retrieved. Does not block P2/P3 (already excluded from scope) |
| Jungius deferral (EEBO/Opuscula access needed; <30 min ruling once available) | C-005 | Out of CE-01 critical path; recorded honestly as Unresolved |
| New Essays Dalgarno/Wilkins exact loci pinning (wilkins file ⚠ note) | C-005 note | Citation-hygiene item; needed only if Wilkins reception becomes claim-bearing |
| Kircher 1670 letter contact claim downgraded to Unresolved | C-005 | Verified quarantined: no deliverable cites it as fact; keep out of citation chains until resolved |
| MEASUREMENT_PLAN §1.9 illustrative-example arithmetic slips (N=1 total inconsistent with its printed terms; N=25 ratio ignores §1.4 symmetry rule for the NL arm) | n/a (non-binding illustration; binding formulas §1.4 correct) | None — directions of both illustrated conclusions survive correction. Instruction to Experimental Engineering Lead: compute all pre-registration figures from §1.4 formulas directly, never from the §1.9 example |
| Prior-Art Investigator re-verification of "unoccupied layer" before any novelty labeling | C-009 | Mandatory gate before Potential Novelty/Candidate Contribution labels; agentic plan formats are the moving risk |
