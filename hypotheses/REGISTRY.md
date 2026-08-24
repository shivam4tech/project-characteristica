# Hypothesis Registry

Canonical registry of hypotheses. Statuses: `registered` → `under-investigation` → `supported` / `falsified` / `unresolved`. Only falsifiable hypotheses are admitted; each must name experiments able to discriminate it from alternatives.

---

## H1 — Central Hypothesis

- **Statement:** For at least some broad classes of AI tasks, a model-independent semantic intermediate representation can communicate equivalent task intent more efficiently and/or reliably than conventional natural-language prompting, after accounting for representation-conversion overhead.
- **Motivation:** Working architecture in `RESEARCH_QUESTION.md`; charter's core hypothesis; recurring historical ambition (Llull → Leibniz → symbolic logic → interlinguas → semantic representations) that has never been decisively tested against *modern strong* prompting baselines.
- **Falsification criteria:** Across all pre-registered task families in a methodologically clean pilot (strong baselines: ordinary NL, optimized NL, structured JSON/schema; full overhead accounting per Protocol §6), no condition shows a material advantage on any registered metric that survives red-team review — i.e., H0 cannot be rejected for every tested class. A single failed task family does not falsify ("some broad classes"); failure across all tested classes does, subject to the scope caveat below.
- **Measurable variables:** input/output/total tokens; API/inference cost; latency; task accuracy/success rate; semantic fidelity (operationalized per OQ12); conversion overhead (tokens+time+error); adapter overhead; robustness to paraphrase; cross-model delta; cross-task delta.
- **Predicted outcomes if true:** ≥1 task family shows net gain (typically consistency/fidelity or multi-turn/tool-call token efficiency) that holds against optimized-NL baseline and replicates across seeds; gains survive inclusion of one-time schema/conversion amortization over realistic reuse counts.
- **Strongest competing explanation:** Any apparent advantage is explained by prompt engineering quality (the JSON/schema baseline captures everything an SIR offers), or by hidden overhead making net effect ≤ 0 once conversion is honestly counted.
- **Discriminating experiments:** E1 efficiency/fidelity pilot (2–3 task families × 4 arms); E2 robustness/portability probe (paraphrase sets, ≥2 model families) if E1 shows signal.
- **Scope caveat:** Falsification within CE-01 applies to tested task families and models only; generalization claims beyond them require new registration.
- **Status:** `registered` (untested)
- **Registered:** Expedition initialization (CE-01)

## H0 — Null Hypothesis

- **Statement:** After accounting for conversion, decoding, schema overhead, model adaptation, and performance loss, semantic intermediate representations provide no meaningful general advantage over strong natural-language prompting.
- **Motivation:** Default skeptical position; charter principle "compression must account for decoding and translation overhead" makes this the conservative prior given decades of interlingua/formal-representation shortfalls outside narrow domains.
- **Falsification criteria:** A pre-registered experiment demonstrates a material, replicable net advantage for an SIR over the strongest NL baseline in ≥1 broad task family, surviving red-team review of baselines and overhead accounting.
- **Measurable variables:** identical to H1 (same experiments discriminate both).
- **Predicted outcomes if true:** All four arms statistically indistinguishable after overhead accounting; or apparent SIR gains fully absorbed by the optimized-JSON arm; conversion overhead ≥ savings in all conditions.
- **Strongest competing explanation:** n/a (null), but its own strongest rival is that pilot scale (2–3 task families) lacks power to detect small real effects — hence verdict language must distinguish "no evidence of advantage at CE-01 scale" from "advantage impossible."
- **Discriminating experiments:** shared with H1 (E1/E2).
- **Status:** `registered` (untested)

---

## Derived sub-hypotheses

Registered during P2 synthesis (Director, 2026-08-24) from cross-workstream mechanism claims. Each follows the same template as H1/H0; registration rule 3 satisfied via the cited CLAIM_LEDGER.md claim IDs.

### H2 — Primitive-vocabulary consistency gain

- **Statement:** Constraining an LLM to emit task output through a small closed primitive vocabulary with typed composition (vs free-form NL or ad-hoc JSON keys) reduces output *variance* on repeated equivalent tasks even where mean accuracy is unchanged.
- **Derivation:** From C-004 (Leibniz's alphabet-of-thoughts premise and its unbuilt status), C-003 (term-product composition mechanics), C-009 (schema payloads carry zero semantics today). The historical alphabet bet was about *reliable generation*, not accuracy — hence the consistency framing.
- **Falsification criteria:** In any pre-registered task family, SIR/structured arms show no significant variance reduction vs optimized-NL arm across seeds/shuffles on matched items (e.g., overlapping distributions of per-item outcome entropy or inter-run disagreement rates), OR variance reduction appears equally in the JSON/schema arm (i.e., it is a formatting effect, not a primitive-vocabulary effect).
- **Measurable variables:** per-cell variance / inter-run agreement rate; F2 content-unit stability across paraphrase variants; token cost (per Protocol §6 accounting).
- **Predicted outcomes if true:** SIR arm shows lower run-to-run dispersion than both NL arms at comparable F1 means; part of any such effect survives comparison against JSON arm (else attributed to structure alone).
- **Strongest competing explanation:** Any variance reduction is a generic structuring/formatting effect available to plain JSON schemas — nothing specifically "primitive-vocabulary-like" is needed.
- **Discriminating experiments:** E1 (variance secondary endpoint); E2 if signal.
- **Traceability:** C-001, C-003, C-004, C-009.
- **Status:** `registered` (untested)
- **Registered:** 2026-08-24 (P2 synthesis)

### H3 — Reuse-gated net benefit

- **Statement:** Net benefit of an SIR over strong NL prompting is non-positive at single-use (N=1) and becomes positive only above a break-even reuse count N* (multi-turn sessions, repeated task templates), because fixed representation/conversion costs amortize while payload savings recur.
- **Derivation:** From C-007 (conversion economics as the recurring killer — inverted into a positive prediction: where reuse exists, economics flip) and MEASUREMENT_PLAN §1.4's break-even machinery (`Δ(N)` curve, N* definition). This is the historical lesson converted into a testable interaction.
- **Falsification criteria:** Measured Δ(N) curve shows either (a) Δ(N) ≤ 0 for all declared N ∈ {1, 10, 25, 100}, or (b) Δ(1) > 0 (which would falsify the gating claim even if later N also win), or (c) no significant N×arm interaction.
- **Measurable variables:** amortized end-to-end $ per dispatched task at declared reuse counts (MEASUREMENT_PLAN §§1.2–1.4); converter error rate K_err; p50/p95 latency including conversion stage.
- **Predicted outcomes if true:** SIR arm loses or breaks even at N=1 and wins monotonically with N; the win requires fidelity non-inferiority to hold simultaneously (gated per §4.4).
- **Strongest competing explanation:** Payload savings are illusory once tokenizer effects are normalized (C-012 ground 1–3), so no N makes Δ positive; or converter costs dominate at all practical N.
- **Discriminating experiments:** E1 primary efficiency endpoints at N ∈ {1, 25}; full curve reported regardless.
- **Traceability:** C-007, C-010, C-012.
- **Status:** `registered` (untested)
- **Registered:** 2026-08-24 (P2 synthesis)

### H4 — Self-detecting malformation (guide-rail effect)

- **Statement:** Structured SIR outputs make silent execution errors rarer than NL outputs: malformed intents surface as validation failures caught before execution (or as explicit unknowns flagged for clarification) rather than as confidently-wrong tool calls or answers, at equal or better task success rates.
- **Derivation:** From C-001 (Leibniz's "ineptiae sese ipsae prodent" — nonsense self-detects — and paralogism-as-calculation-error criterion), C-018 (composibility gate mechanized as validation-before-execution), C-011/R1–R4 (validated checkpoint contract; explicit unknowns instead of silent defaults), C-019 (structural metrics alone insufficient — hence the metric must be downstream execution failures, not format checks).
- **Falsification criteria:** Rate of confident-but-wrong executions (errors reaching tools/users without being flagged) is not lower in the SIR arm than the strongest NL baseline, or the reduction is fully explained by the JSON-schema arm's existing validation, or SIR buys error-detection only by degrading success rate below the non-inferiority margin δ.
- **Measurable variables:** fraction of items with undetected errors (validation-passed but F1-failed); ask_user/unknown flag rates; false-positive validation rejection rate; F1 success under the standard gates.
- **Predicted outcomes if true:** SIR arm shifts failure mass from silent-wrong to detected-and-flagged relative to NL arms; detection advantage persists after excluding trivial format errors.
- **Strongest competing explanation:** Modern LLMs already self-monitor well enough that explicit structure adds no incremental error detection beyond what JSON schemas provide.
- **Discriminating experiments:** E1 (all families log parse/validation outcomes per MEASUREMENT_PLAN §4.3; analysis splits silent vs detected failures).
- **Traceability:** C-001, C-011, C-018, C-019.
- **Status:** `registered` (untested)
- **Registered:** 2026-08-24 (P2 synthesis)

### H5 — Redundancy trade-off under paraphrase (robustness cost of compression)

- **Statement:** Because natural-language redundancy functions as channel coding for a stochastic decoder, compressed/structured intent representations degrade more than plain NL when inputs are paraphrased — compression purchases economy partly with robustness.
- **Derivation:** Directly from C-014 (MEASUREMENT_PLAN H-C2, §2 ground 7); registered here as the formal sub-hypothesis so E2 can discriminate it. Complements H3: what reuse does to the *cost* axis, paraphrase does to the *robustness* axis.
- **Falsification criteria:** On pre-registered paraphrase variant sets, performance deltas between original and paraphrased inputs do not differ significantly between SIR and NL-plain arms (or SIR degrades less).
- **Measurable variables:** per-arm ΔF1 between canonical and paraphrase variants; F2 unit-loss attribution (conversion-stage vs decoder-stage).
- **Predicted outcomes if true:** |ΔF1(paraphrase)| strictly ordered: SIR > JSON > optimized-NL > NL-plain (most compressed degrades most).
- **Strongest competing explanation:** Paraphrase sensitivity is uniform across representations because modern LLMs normalize surface variation internally.
- **Discriminating experiments:** E2 (paraphrase sets); optionally a small E1 add-on if budget permits.
- **Traceability:** C-014 (and MEASUREMENT_PLAN §2 ground 7).
- **Status:** `registered` (untested)
- **Registered:** 2026-08-24 (P2 synthesis)

## Registration rules

1. New hypotheses enter as `registered` with all fields filled before related work begins.
2. Status changes require citing the discriminating experiment record(s).
3. Sub-hypotheses must trace to ≥1 mechanism claim in `CLAIM_LEDGER.md`.
