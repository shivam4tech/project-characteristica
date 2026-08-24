# KICKOFF DIRECTIVE — CE-01 Resumption (for Characteristica Prime)

**From:** Operator, relayed by coordinating session (2026-08-24)
**Situation:** Previous delegation batch (`deleg_ff12b2e5`, 6 workers, dispatched 2026-08-23 14:52 IST) was killed by an app exit before any worker produced output. WORKERS.md roster is stale (shows ACTIVE). Budget ledger correctly shows 0.0h spent. FINAL_REPORT.md is empty. No research was lost because none had occurred.

## Your Tasks, In Order

### 1. Reconcile state (≤15 min)
- Read STATUS.md, WORKERS.md, hypotheses/REGISTRY.md.
- Update WORKERS.md: mark W1–W6 from batch deleg_ff12b2e5 as TERMINATED (reason: host app exit, no output produced). Zero hours charged.
- Do not charge hours for the dead batch.

### 2. Re-dispatch P1 reconnaissance (fresh subagent batch)
Six workstreams, same mandates as ORGANIZATION.md §5–§10, same budgets:
| WS | Role | Budget | Output target |
|---|---|---|---|
| WS-MODERN | Modern Representation Researcher | 5.5 h | literature/modern/prior_art_map.md |
| WS-INFOTH | Info Theory / Compression Researcher | 3.0 h | benchmarks/MEASUREMENT_PLAN.md |
| WS-LEIBNIZ | Leibniz Researcher | 4.0 h | literature/leibniz/leibniz_extraction.md |
| WS-PRE | Pre-Leibniz Researcher | 3.5 h | literature/pre_leibniz/ (gate rulings + extractions) |
| WS-POSTL | Post-Leibniz Researcher | 3.5 h | literature/post_leibniz/formal_systems_extraction.md |
| WS-IR | Compiler / IR Researcher | 2.5 h | literature/modern/ir_analogy_assessment.md |

Each worker prompt MUST include: (a) binding docs to read first (LAB_CHARTER, RESEARCH_PROTOCOL incl. §1 source hierarchy and §2 extraction schema, CE-01 README); (b) its role section from agents/ORGANIZATION.md verbatim; (c) its budget in hours and instruction to state elapsed time honestly; (d) output file paths; (e) the evidence standard (every claim → source + confidence + finding label); (f) explicit prohibition on fabricating completions or placeholder text.

Known verified prior art to seed WS-MODERN (already verified by operator session — do not re-verify): Slavenskoj "Lingenic" paper = SSRN abstract 6291378, DOI 10.2139/ssrn.6291378, PhilArchive SLAOTR — notation-only scope, calculus ratiocinator explicitly out of scope, reader supplies reasoning. Also: Zhang/Jiang/Quan AAAI-25 (all universal KR formalisms recursively isomorphic, DOI 10.1609/aaai.v39i14.33674); Kausch 2024 (DOI 10.35492/docam/11/2/16).

### 3. While workers run
- Draft LINGENIC_CRITICAL_ANALYSIS.md skeleton at project root (top-level ~/philosophy/) from the verified abstract; mark PDF-dependent sections TODO pending retrieval.
- Keep STATUS.md updated as dispatches land.

### 4. Completion protocol (per worker)
Before recording any worker COMPLETED: open its output files yourself; check for placeholders ("[Insert", "TODO", "[TBD]"); spot-check one citation per file against Protocol §1; only then update STATUS/WORKERS and charge its hours.

### 5. Escalation triggers (report to operator immediately)
- Any worker fabricates output → terminate, log, note model used.
- Combined P1 spend projected >14h → pause new dispatches, report.
- Any foundational issue with H1/H0 framing discovered during recon → report before proceeding to P2.

## Constraints Reminder
- 40 agent-hour hard cap; warning at 36h. P1 allocation: 14h total.
- Max ~6 concurrent workers. Experimental Engineering and Red Team stay dark until P3/P4.
- Research before invention: no notation design during P1/P2.
