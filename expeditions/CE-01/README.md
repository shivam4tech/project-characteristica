# CE-01: Universal Representation Feasibility Study

## Title

Characteristica Expedition 01 — Universal Representation Feasibility Study

## Research Objective

Determine whether historical and modern attempts at universal representation contain principles that can support a useful model-independent semantic intermediate representation (SIR) for AI, and determine experimentally whether such a representation merits further research.

CE-01 succeeds if it produces enough evidence for a defensible GREEN, AMBER, or RED decision per `RESEARCH_PROTOCOL.md` §10. It does **not** need to produce a finished language.

## Scope

In scope:

1. **Targeted historical genealogy** — pre-Leibniz systems (only those earning time under the relevance gate below), Leibniz's characteristica universalis / calculus ratiocinator / Ars Combinatoria in depth, key post-Leibniz formal systems (symbolic logic, controlled languages, interlinguas, ontologies), each extracted as mechanisms, failure modes, and modern analogues per Protocol §2.
2. **Modern prior-art survey** — semantic parsing, meaning representations, knowledge graphs, structured prompting, prompt compression, neuro-symbolic AI, tool/function schemas, compiler IRs, interlingua MT, controlled NLs, machine-to-machine protocols (Protocol §3 list).
3. **Conceptual synthesis** — recurring mechanisms across eras mapped to candidate SIR design principles; at least one candidate architecture sketch.
4. **Minimal decisive experimentation** — one or two pre-registered pilot experiments comparing a candidate structured representation against strong natural-language baselines on 2–3 task families, with full overhead accounting (Protocol §§4–6).
5. **Prior-art challenge and red-team review** of any positive signal.
6. **Verdict synthesis** — FINAL_REPORT with a defensible label.

### Historical relevance gate

Pre-Leibniz research begins before Leibniz but is a targeted genealogy, not a history of philosophy. A pre-Leibniz system earns research time only if it plausibly contributes ≥1 of: representation primitives; compositional mechanisms; symbolic inference; combinatorial generation; taxonomic organization; ambiguity reduction; formalization of conceptual relations; machine-relevant design principles; demonstrable influence on later universal-representation projects. Likely candidates include Ramon Llull and earlier logical/classificatory traditions — but relevance must be established, never assumed. Relevance must be justified in writing within the literature note within 30 minutes of starting a system; failing that gate, stop and log to `archive/`.

## Explicit Non-Goals

- Building a complete, general-purpose universal language or full SIR implementation.
- Writing general history of philosophy or biographies; producing summaries instead of mechanism extractions.
- Claiming novelty without completed prior-art review.
- Benchmarking against intentionally weak prompts; optimizing exclusively for token count.
- Hiding complexity in compilers/adapters without accounting for its cost.
- Testing on a single task family or single model and calling it general.
- Any claim of "solving universal language."

## Budget

**40 cumulative agent work-hours** (research budget). Wall-clock time may be shorter due to parallelism; compute does not substitute for experimental quality — hours are charged per agent-hour of substantive work. Budget ledger is maintained in `STATUS.md`; every workstream logs hours spent.

Hard cap: when cumulative budget reaches 36 h, no new workstreams may start; remaining hours go to synthesis, red team, and final report.

## Phase Structure

| Phase | Name | Budget | Objective | Exit condition |
|---|---|---|---|---|
| P0 | Setup & Registration | 3 h | Registries live; H1/H0 registered; benchmark framework approved | All setup artifacts populated; Director signs off |
| P1 | Parallel Reconnaissance | 14 h | Historical genealogy (Llull → Leibniz → successors), modern prior-art survey, compiler-IR analogy check, information-theoretic measurement framing | Mechanism extraction tables done; prior-art landscape map drafted; ≥8 sources in bibliography |
| P2 | Synthesis | 6 h | Chief Scientist unifies findings into candidate mechanism set + ≥1 candidate SIR architecture sketch; Curator registers derived hypotheses | Architecture sketch registered with falsifiable predictions |
| P3 | Pilot Experimentation | 9 h | Prototype minimal SIR for 2–3 task families; run pre-registered pilots vs. strong baselines with full overhead accounting | At least one discriminating experiment completed with raw results logged |
| P4 | Adversarial Review | 4 h | Prior-Art Investigator + Red Team attack the strongest positive and negative signals | Red-team memo filed; claims dispositioned in ledger |
| P5 | Verdict Synthesis | 4 h | Director weighs evidence; write FINAL_REPORT with GREEN/AMBER/RED | FINAL_REPORT committed |

Phases P1 sub-workstreams run concurrently. A phase may be exited early if its stopping rules fire.

## Deliverables

1. Populated `BIBLIOGRAPHY.md` (≥15 vetted sources spanning all four eras incl. modern).
2. Mechanism-extraction tables (Protocol §2 schema) for ≥5 historical systems + Leibniz in depth.
3. Prior-art landscape map (`literature/modern/prior_art_map.md`) covering all 16 Protocol §3 domains.
4. Registered hypothesis set in `hypotheses/REGISTRY.md` (H1/H0 + ≥2 derived sub-hypotheses).
5. ≥1 candidate SIR architecture sketch with explicit primitive/composition/inference/ambiguity/extensibility choices.
6. ≥1 completed pilot experiment record in `experiments/` with raw results in `results/`.
7. Red-team memo in `critiques/`.
8. `FINAL_REPORT.md` with a defensible GREEN/AMBER/RED recommendation.
9. Updated `CLAIM_LEDGER.md` with every material claim dispositioned.

## Decision Criteria

GREEN requires ≥1 of (Protocol §10): reproducible efficiency gain; reproducible reliability gain; meaningful cross-model portability signal; technically plausible underexplored mechanism surviving red-team scrutiny; candidate representation architecture surviving red-team scrutiny — each supported by pre-registered experiments and honest overhead accounting.

AMBER: interesting but incomplete signal — e.g., gains exist but are task-specific, portability untested, or conversion overhead unresolved.

RED: after accounting for conversion/schema/model-adaptation overhead, the SIR shows no meaningful advantage over strong NL prompting, or the space is shown substantially occupied by existing work, or the concept fails under experimental scrutiny. RED must clearly state why continued research is unlikely to be worthwhile. A well-supported RED is a successful outcome.

Provisional verdict starts UNDECIDED and is updated in `STATUS.md` as evidence accumulates.

## Stopping Rules

Any of these terminates the expedition early with a verdict written from evidence so far:

1. Budget exhausted (40 h hard cap).
2. Pilot experiment decisively falsifies H1 across all tested task families with clean methodology → fast-track RED.
3. Prior-art investigation finds the core idea already substantially solved and validated (e.g., existing SIR with published strong-baseline wins) → RED or pivot-to-evaluation AMBER.
4. Two consecutive phases produce no registrable claims → RED with "frontier does not exist" analysis.
5. External blocker (no API access, no reproducible environment) persists >4 h despite mitigation.

## Extending Promising Work

A direction may gain up to +25% of its phase budget (taken from another workstream, never exceeding the 40 h cap) if: it produced a registrable claim labeled Potential Novelty or a positive Experimental Result; the extension is pre-registered (what will be tested, what outcome would kill it); and the Director approves. Only one extension per workstream.

## Terminating Weak Directions

A workstream is terminated and archived when: it fails the historical relevance gate; it produces only restatements of known prior art; its continuation would duplicate another agent's assigned scope; or it consumes >150% of allocated hours without a registrable claim. Termination is logged in `STATUS.md` (blocked/closed workstreams) with a one-paragraph rationale. Terminated directions move notes to `archive/`.

## Governance

Bound by `LAB_CHARTER.md`, `RESEARCH_QUESTION.md`, `RESEARCH_PROTOCOL.md`. Roles and handoffs: `agents/ORGANIZATION.md`. Claims: `CLAIM_LEDGER.md`. Sources: `BIBLIOGRAPHY.md`. Open questions: `OPEN_QUESTIONS.md`. Verdict authority: Research Director only.
