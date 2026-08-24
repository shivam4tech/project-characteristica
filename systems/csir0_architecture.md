# CSIR/0 — Candidate SIR Architecture Sketch (CE-01 / P2)

**Author:** Research Director (characteristica-prime session), 2026-08-24
**Status:** P2 architecture sketch — structure + semantics choices ONLY. **No notation design** (P2 rule): the single JSON fragment below is illustrative instance data for review, non-normative, and makes no commitment about surface syntax. Any grammar/serialization decisions belong to the Experimental Engineering Lead at E1 pre-registration.
**Purpose:** a concrete enough target that (i) MEASUREMENT_PLAN.md applies unchanged, (ii) E1 task-family predictions can be registered, (iii) Red Team has a specific object to attack in P4.

---

## 0. Design posture (what CSIR/0 is, in one paragraph)

CSIR/0 (**C**haracteristica **S**emantic **I**nterchange **R**epresentation, candidate 0, semver'd from birth) is a **validated checkpoint contract** between natural-language intent and AI-computation adapters — *not* a universal language, *not* a calculus, *not* a knowledge base. It is an inert, typed, version-stamped data document produced by an LLM converter, consumed by validators and adapters, carrying explicit provenance back to source spans, explicit unknowns where intent is undetermined, and explicit analysis-status per vocabulary term. Its claimed value axes are checkpoint economics (cache/resume/audit/test), error surfacing before execution, and data portability across model families — never expressive power (C-008), never semantic-losslessness (C-013), never correctness guarantees (C-011 D2).

## 1. Layer position and role

| Choice | Decision | Trace |
|---|---|---|
| Position | Sits where RESEARCH_QUESTION.md puts it: after NL, before Model/Tool Adapter. The LLM is the front end (converter); CSIR/0 is the artifact it emits; adapters consume it. | C-011 §4(a) |
| Role | Checkpoint contract: cacheable, resumable, auditable, testable seam. Explicitly NOT a translation pivot — front-end diversity (user phrasings) is unbounded, so pivot economics never close. | C-011 §4(b), R1 |
| Scope | Task intents in pre-registered E1 families (extraction; constraint satisfaction/planning; tool use). No universality claim; scope growth = new registration. | C-006 (A4 trilemma — we buy A2-adjacent checking by abandoning A4), Protocol §10 |
| Consumers | (1) schema validator (gate), (2) task executor/adapter, (3) fidelity auditor (F2/F3 tooling), (4) clarification UI (spans), (5) CI golden-suite diffing. Five consumers justify the schema's existence per the pass-manager discipline. | C-011 M6, R10 |

## 2. Vocabulary: two tiers, no alphabet of thought

This is the central historical lesson applied. Every failed system that required a finished primitive inventory died on it (Descartes' deadlock; Wilkins' tree surgery; Leibniz's never-built alphabet; Cyc's decades of assertion entry).

| Tier | Content | Admission rule | Trace |
|---|---|---|---|
| **Tier A — closed structural core** | ~14 element types, deliberately aligned 1:1 with the MEASUREMENT_PLAN §3.2 content-unit taxonomy so F2 auditing is native: `entity_ref`, `predicate`, `quantity_unit`, `temporal_qualifier`, `constraint` (hard\|soft), `scope_marker`, `modality`, `negation`, `preference_order`, `output_shape`, `speech_act`, `style_constraint`, `exclusion`, plus cross-cutting `provenance_span` and `unknown_flag`. | Changes require major version bump; every Tier-A type needs producer guidance + consumer code + test (three-part rule). | C-017 (two-tier licensed by Leibniz GP VII 203); C-013 (fidelity is taxonomy-relative — make the taxonomy load-bearing); C-019 (units ≠ surface match); C-011 M2/M8 |
| **Tier B — open typed lexicon** | Domain terms: tool names, entity strings, domain predicates. Carried **opaque** by default (`analysis_status: opaque`), optionally `analyzed` when someone writes a definition composing Tier-A/Tier-B terms. No decomposition is ever *required* for entry. | Cheap append (minor version); declaration includes type signature + span of first attestation. | C-017 (Chinese-characters analogy verbatim); C-004 (avoids the A3 trap — no promise of complete analysis) |

**What is deliberately absent:** any primitive-concept alphabet claiming completeness; any arithmetic/combinatorial encoding of concepts (Leibniz's characteristic numbers stalled precisely on coprimality, C-004); any ontology-commitment layer (that is Wikidata/SNOMED's job — CSIR/0 references such identifiers via Tier-B entries when available, e.g. QIDs, instead of duplicating them, per prior_art_map §D5 "SIR must sit above KG level").

## 3. Composition: shallow typed graphs with one declared reading

| Choice | Decision | Trace |
|---|---|---|
| Structure | Attributed directed acyclic graph per task intent. Nodes = Tier-A elements or Tier-B terms; edges from a **closed relation-label set** bound to the speech-act templates of the core (e.g., `hasArg`, `constrains`, `orderedBefore`, `excludes`, `quantifiesOver`, `modifies`). | C-011 M2 (typed core) |
| Depth | Bounded nesting (≤3 levels) at E1. Deeper structure must be flattened via intermediate entities. Hard cap until measured pain (two-tier rule from compiler practice). | C-011 M1/R3 |
| Semantics | Each relation label has exactly ONE declared reading (documented per label). Where Leibniz's dual clause (intensional vs extensional containment, GP VII 224) would matter, CSIR/0 fixes extensional-by-default and provides an explicit `intensional` modifier attribute that converters may set only with span justification. Silent duality — the historical source of paradox charges — is impossible by construction. | C-003 |
| Negation/subtraction | Negation exists only as the `negation` marker on constraints/predicates. There is NO term-subtraction operation (Leibniz's own flagged partiality bug, GP VII 230; MINUS 4). Negative information = explicit exclusion elements, which are first-class auditable units. | C-003, C-004 item 4 |
| Well-formedness gate (the mechanized possibility oracle) | Three checks before any execution: (1) schema conformance (Tier-A types, arity, depth); (2) referential integrity (every Tier-B token used is declared in the document's lexicon block); (3) span coverage (every non-unknown node cites ≥1 source char-span; uncovered nodes rejected). Failure ⇒ bounded repair loop (≤2 re-prompts) then targeted clarification with quoted span. Nothing executes unvalidated. | C-018 (composibility gate); C-011 M2/M5, R1, R5 |

## 4. Inference stance: none shipped

| Choice | Decision | Trace |
|---|---|---|
| Calculus | CSIR/0 ships no consequence relation, no proof procedure. It is data. Any checking (consistency, entailment planning) is an EXTERNAL service invoked per-task, its results attached as dated annotations with their own provenance. | C-002 (deduction/valuation separation); UNL lesson inverted knowingly — UNL died partly because it promised interchange while needing processing it never specified; we promise interchange only |
| Valuation | Modality and preference slots carry DECLARED status (`asserted \| assumed \| queried`; preference ranks with source spans). No weights are computed inside the representation. If an E1 family needs scoring, scores live in the adapter layer, logged per MEASUREMENT_PLAN §4.3. | C-002 (Leibniz's own admission that value-units were never constructed); P12 conditional-output honesty |
| Premise status propagation | Every constraint/predicate node carries premise-status; downstream conclusions inherit it, so "hypothetical out" is visible in artifacts. | leibniz_extraction.md P12 (GP IV 429–430) |

## 5. Ambiguity policy: preserve, never silently resolve

| Choice | Decision | Trace |
|---|---|---|
| Detected ambiguity | Converter must either (a) branch explicitly — one subgraph per reading, each tagged with confidence + spans — or (b) emit `unknown_flag` + `ask_user` citing the exact span. Silent selection of one reading is prohibited output behavior (validator-rejected pattern). | C-011 D3/D4 (distinct readings are distinct intentions; source not authoritative), R4/R6 |
| Canonicalization | Only uncontroversial equivalences normalized (dates, units, enums, identifiers). Raw span stored beside every canonical value. Paraphrase collapsing PROHIBITED at conversion time. | C-011 M4/R6 |
| Residual vagueness | Represented as typed unknowns with the elicitation question embedded — requirements-elicitation posture (D4), not translation posture. | C-011 D4 |

## 6. Versioning, extensibility, model-independence mechanics

- **Semver from day one** (R7/M11): every artifact stamps `csir_version`; adapters declare supported ranges; breaking change = Tier-A change or relation-label semantic change. Migration notes mandatory per release even if trivial.
- **Three-part rule** for any new construct (R10): producer guidance + consumer code + test, or it does not enter the schema. Dead-schema growth is the failure mode this prevents.
- **Model independence** = data independence: CSIR/0 is plain structured data with no embedding, no logits, no model-relative component (prior_art_map §D12 defines what it must NOT be). Adapter hints live outside the document proper, hashed and logged per MEASUREMENT_PLAN §1.3 so cross-arm fairness is auditable.
- **Per-adapter conformance suites** (R8): each consuming adapter gets a test bundle; provider-specific capabilities enter through an explicit extension block, never by polluting the core.

## 7. Illustrative instantiation (NON-NORMATIVE — structure demo only, not notation design)

```json
{
  "csir_version": "0.1.0",
  "speech_act": {"type": "request", "span": [0, 87]},
  "lexicon": [
    {"id": "t1", "term": "staging", "tier": "B", "type": "environment_ref",
     "analysis_status": "opaque", "attestation_span": [31, 38]}
  ],
  "nodes": [
    {"id": "n1", "kind": "predicate", "term": "deploy", "status": "asserted", "spans": [[12, 19]]},
    {"id": "n2", "kind": "entity_ref", "ref": "t1"},
    {"id": "n3", "kind": "temporal_qualifier", "value_raw": "soon",
     "canonical": null, "unknown": true, "ask_user": true,
     "clarification": "by 'soon' (chars 45–49): did you mean today?", "spans": [[45, 49]]},
    {"id": "n4", "kind": "constraint", "polarity": "hard",
     "content": {"pred": "run_tests", "must_precede": "deploy"}, "spans": [[60, 87]]},
    {"id": "n5", "kind": "exclusion", "content": "no_force_push", "spans": [[70, 78]]}
  ],
  "edges": [
    {"rel": "hasArg", "from": "n1", "to": "n2"},
    {"rel": "modifies", "from": "n3", "to": "n1"},
    {"rel": "constrains", "from": "n4", "to": "n1"},
    {"rel": "excludes", "from": "n5", "to": "n1"}
  ]
}
```

Points the example carries: unknowns are first-class with clarification text; every node cites spans; the Tier-B term is opaque with attestation; premise status rides on the predicate; there is no hidden global state.

## 8. What CSIR/0 explicitly does NOT claim

| Refused claim | Reason | Trace |
|---|---|---|
| Expressive superiority | All universal formalisms recursively isomorphic; value must be positional/ecosystem | C-008 |
| Semantic losslessness | Equivalence undecidable; fidelity is taxonomy-relative | C-013 |
| Correctness guarantee vs intent | No formal source semantics, no equivalence relation statable | C-011 D1/D2 |
| Universality of scope | A4 trilemma: bought checking by abandoning universal scope | C-006 |
| Primitive-analysis completeness | A3 has no surviving heir in 250 years | C-004 |
| Inference capability | Deduction/valuation separation; calculus sold separately if ever | C-002 |
| Token-efficiency headline | Raw-token claims banned; joint cost×fidelity statistic only | C-012 |

## 9. Falsifiable predictions for E1 (consistent with MEASUREMENT_PLAN.md; to be transcribed into E1_PRE_REGISTRATION.md with numbers)

Baseline facts fixed by the measurement plan: four arms (NL-plain, NL-opt, JSON/schema, CSIR/0-SIR); primary endpoint = F0-gated F1 success; efficiency = amortized end-to-end $ at N ∈ {1, 25} (+ p95 latency); full curve Δ(N) reported regardless.

| # | Prediction | Family | Source hypothesis |
|---|---|---|---|
| P1 | Δ(N=1) ≤ 0 for the SIR arm in ALL families (single-use never pays); Δ(N=25) > 0 in extraction iff measured conversion fidelity (F2 conversion-stage unit recovery) ≥ 0.90 | all / extraction | H3, C-007 |
| P2 | If F2 conversion fidelity < 0.80 in extraction, Δ(N) < 0 at every declared N — the UNL-replay condition. Registered in advance so the failure, if it comes, is diagnostic not surprising | extraction | H3, C-007, prior_art_map §D13 |
| P3 | Conversion-stage unit loss concentrates in `modality`, `preference_order`, and `exclusion` units (saturation/context-dependent material), mirroring documented interlingua loss patterns — NOT in `entity_ref`/`quantity_unit` units | extraction | C-007, prior_art_map §D2/§D13 |
| P4 | SIR arm shows significantly lower run-to-run outcome variance than both NL arms at comparable F1 means in the constraint/planning family; part of the effect survives the JSON-arm comparison (if none survives, H2 attributes it to generic structuring and H2 is weakened accordingly) | constraint/planning | H2 |
| P5 | Silent-error fraction (validation-passed but F1-failed) is lower for SIR than both NL arms in constraint/planning; NO significant silent-error advantage of SIR over the JSON arm in tool-use (JSON already validates; that arm is the adversarial control) | planning / tool-use | H4, C-019 |
| P6 | Registered adversarial prediction: in tool-use, SIR ≤ JSON arm on primary endpoints. A contrary result triggers mandatory red-team review before any claim (per MEASUREMENT_PLAN §4.7) | tool-use | C-009 (schema payloads are the incumbent), C-008 |
| P7 | F3 round-trip stability for CSIR/0 exceeds a pre-registered threshold δ_F3 (value fixed at pre-registration, not here); failures concentrate at unknown-flagged and ambiguous-branch nodes, i.e., stability tracks declared undeterminacy | all | C-013, MEASUREMENT_PLAN §3.1 F3 |
| P8 | Paraphrase-robustness ordering (E2 or budget-permitting E1 add-on): degradation SIR ≥ JSON ≥ NL-opt ≥ NL-plain | cross-family | H5, C-014 |

Consistency check against MEASUREMENT_PLAN §4.2: these predictions *endorse* its provisional family list unchanged (extraction = mechanism-favored; planning = compositionality stress; tool-use = adversarial/falsification family), so the pre-registration follows the plan's own selection rule with no post-hoc steering.

## 10. Open design debts (registered, not hidden)

1. **Serialization/token economy untested.** Whether Tier-A verbosity survives its own F accounting at conversation scale is exactly what E1 measures; no compact-syntax work is permitted before baseline data exists (would violate C-012 gaming-resistance).
2. **Relation-label set not frozen.** The closed edge vocabulary must be finalized during E1 pre-registration against the chosen task families; freezing it here, before family selection, would be premature optimization.
3. **Branch handling cost unknown.** Explicit ambiguity branching can double document size on ambiguous items; the ask_user alternative shifts cost to interaction latency. Both metered in E1; choice per-item is converter policy to be studied, not fixed now.
4. **Scope-marker formalism minimal.** Quantifier scope gets an explicit marker node, not a full treatment; known simplification vs Montague-grade fragments (C-011 D1 explains why full fragments are out of scope at E1).
5. **Converter prompt = part of F.** The instructions teaching models to emit CSIR/0 count fully in `F_sir` per MEASUREMENT_PLAN §1.1 — no hiding the representation's instruction cost.

## 11. Provenance

Every design choice above traces to CLAIM_LEDGER.md rows C-001…C-019 (transcribed from verified P1 deliverables 2026-08-24) and to MEASUREMENT_PLAN.md sections cited inline. No choice rests on worker self-report alone; the Director inspected each underlying deliverable during P1 exit review.
