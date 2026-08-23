# Benchmark Design Framework

**Status: design only. No benchmark results are manufactured here.** This document fixes what any CE-01 (or later) experiment must measure and how task families are constructed, so pilots cannot drift toward favorable conditions.

Governed by `RESEARCH_PROTOCOL.md` §§4–8.

## 1. Required comparison arms

Every benchmark run must include **all four** arms unless the Director approves a documented exception (recorded in `decisions/`):

1. **NL-plain** — ordinary natural-language prompt, as a competent practitioner would write it.
2. **NL-optimized** — carefully engineered prompt (role framing, explicit output contract, few-shot if allowed anywhere, allowed anywhere else). This arm exists to kill straw-man comparisons.
3. **JSON/schema** — same task expressed as structured JSON conforming to an explicit schema, with schema instructions included.
4. **Characteristica SIR** — the candidate representation under test, with its schema/decoder instructions fully included.

Arms must hold constant everything not under test: model, decoding parameters, max tokens, tools, context, number of samples.

## 2. Candidate task families

Minimum set (CE-01 pilots select 2–3; later expeditions extend):

| Family | Example task shape | Why it discriminates |
|---|---|---|
| Extraction | pull structured fields from messy text | fidelity vs. compactness directly observable |
| Classification | multi-label categorization w/ rubric | consistency/variance differences show up cleanly |
| Retrieval | query formulation / result selection | tests whether structure helps disambiguate intent |
| Planning | multi-step plan generation w/ constraints | compositionality stress test |
| Reasoning | multi-hop inference w/ verifiable answers | formal-representation advantage hypothesis |
| Coding | function synthesis from spec | existing structured formats are strong here — good adversarial case |
| Tool use | API/function-call selection & parameterization | native structured territory; tests portability of the idea |
| Constraint satisfaction | scheduling/allocation under constraints | symbolic-friendliness probe |
| Document analysis | long-document QA / summarization w/ citations | length & redundancy stress conversion overhead |

Selection rule for CE-01: pick families where the mechanism claims from P1/P2 predict differential advantage, **and** include at least one family where the SIR is *predicted to lose* (falsification value).

## 3. Required measurements

Per run, per arm:

- input tokens, output tokens, total tokens
- task success / accuracy against a pre-registered answer key or checker
- semantic fidelity (metric fixed by the measurement plan, OQ12 — must be defined **before** data collection)
- completion rate (parse/format failures counted as failures, not dropped)
- latency where measurable
- API/inference cost
- conversion overhead: cost of producing the representation from source (tokens + time + error)
- adapter overhead: model-specific wrapping cost, amortized per Protocol §6 over a pre-declared realistic reuse count (declared in the pre-registration, not chosen after seeing results)
- robustness: performance delta under paraphrased inputs
- cross-task generalization: same representation reused across ≥2 task families without redesign
- cross-model portability: same representation on ≥2 independently developed model families where feasible

## 4. Fairness rules (anti-straw-man)

1. Baselines may not be intentionally weakened: no stripped instructions, no artificially bad formats for competing arms.
2. The JSON/schema arm gets equivalent engineering effort to the SIR arm; if the SIR gets few-shot examples, so do the baselines when practical.
3. All representation-instruction costs (schema definitions, grammars, decoder prompts, examples) are charged to the arm that needs them and amortized only per pre-declared reuse assumptions.
4. Identical models/parameters/checkers across arms; answer keys and checkers fixed before runs.
5. Seeds and sample sizes pre-registered; stopping conditions declared in advance; all conditions reported including unfavorable ones.
6. Any post-hoc exclusion of runs must be justified in writing in the experiment record and flagged in `CLAIM_LEDGER.md`.

## 5. Experiment record requirements

Each experiment gets `experiments/E<N>_PRE_REGISTRATION.md` (hypothesis link, arms, task sets, metrics, seeds, predicted outcomes, stopping rule) **before** execution, and raw outputs land in `results/`. Analysis goes in the experiment record; claims then register in `CLAIM_LEDGER.md`.
