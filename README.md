# Project Characteristica

**Characteristica Research Lab** investigates whether historical and modern attempts at universal representation can inform a useful **model-independent semantic intermediate representation (SIR)** for AI systems — a structured layer between human intent and AI computation.

## Mission

Natural-language prompting may be an inefficient interface for communicating human intent to AI systems. A structured semantic intermediate representation may preserve task meaning while improving token efficiency, cost, latency, consistency, compositionality, interpretability, cross-model portability, formal reasoning, or tool interoperability. The lab tests this empirically and honestly — including the possibility that the answer is no.

## Central Hypothesis (H1)

> For at least some broad classes of AI tasks, a model-independent semantic representation can communicate equivalent task intent more efficiently and/or reliably than conventional natural-language prompting, after accounting for representation-conversion overhead.

Null hypothesis (H0): after all overheads, SIRs provide no meaningful general advantage over strong natural-language prompting. See `hypotheses/REGISTRY.md`.

## CE-01 Purpose

Characteristica Expedition 01 is a **feasibility study**, not an attempt to build a universal language. It determines whether a genuine, experimentally accessible research frontier exists between human natural language and machine-facing representations, and ends with a defensible GREEN / AMBER / RED verdict. Details: `expeditions/CE-01/README.md`; live state: `expeditions/CE-01/STATUS.md`.

## Repository Structure

| Path | Purpose |
|---|---|
| `LAB_CHARTER.md` | Mission, scientific principles, allowed finding labels, lab verdicts, anti-goals |
| `RESEARCH_QUESTION.md` | Primary question, 10 operational questions, working architecture, H1/H0 |
| `RESEARCH_PROTOCOL.md` | Source discipline, extraction rules, prior-art rule, baselines, metrics, red-team requirement |
| `CLAIM_LEDGER.md` | Canonical registry of every material research claim |
| `BIBLIOGRAPHY.md` | Canonical source registry |
| `OPEN_QUESTIONS.md` | Tracked open questions with ownership and resolution criteria |
| `expeditions/` | One directory per expedition (CE-01 first); each has README (scope), STATUS (dashboard), FINAL_REPORT |
| `agents/ORGANIZATION.md` | Multi-agent role definitions: mandates, inputs/outputs, prohibitions, handoffs |
| `literature/` | Research notes by era: `pre_leibniz/`, `leibniz/`, `post_leibniz/`, `modern/` |
| `hypotheses/REGISTRY.md` | Registered hypotheses with falsification criteria |
| `benchmarks/BENCHMARK_DESIGN.md` | Benchmark task families and measurement requirements (no results here) |
| `experiments/`, `results/` | Pre-registered experiment records; raw outputs |
| `prototypes/`, `systems/` | Candidate representations and adapter implementations |
| `critiques/` | Red-team memos and prior-art challenges |
| `decisions/` | Director decisions with rationale |
| `logs/`, `archive/` | Session logs; terminated/duplicated directions |

## Scientific Philosophy

1. Evidence over enthusiasm; reproducibility over anecdotes.
2. Falsification is valuable; negative results are valid results.
3. Historical claims require sources; novelty claims require prior-art review; experimental claims require strong baselines.
4. Compression must account for decoding and translation overhead.
5. Agents may propose discoveries but may not declare them established; LLM agreement is not evidence.
6. History is mined for mechanisms, failure modes, and experimental implications — never written as biography.

## How Expeditions Are Organized

Each expedition is a time-boxed (budgeted) unit of research with a fixed phase structure — setup → parallel reconnaissance → synthesis → experimentation → adversarial review → verdict — pre-registered deliverables, stopping rules, and one mandatory terminal verdict (GREEN pursue / AMBER continue narrowly / RED discontinue). Only the Research Director may issue a verdict or mark a *Candidate Contribution*. Work is distributed across specialized agents defined in `agents/ORGANIZATION.md`; every claim must be auditable through sources, files, commits, and experiment records.
