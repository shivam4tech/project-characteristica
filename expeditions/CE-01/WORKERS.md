# CE-01 Worker Registry

Live roster of delegated workers. Statuses: QUEUED / ACTIVE / BLOCKED / COMPLETED / TERMINATED / NEEDS_REVIEW / PAUSED. Worker IDs are lab-side identifiers; Hermes subagent IDs are recorded when returned by delegation. This registry prevents duplicated or orphaned research.

| Worker ID | Hermes ID | Role | Workstream | Start | Stop | Status | Last report | Output files | Director disposition |
|---|---|---|---|---|---|---|---|---|---|
| W1-MODERN | (pending spawn) | Modern Representation Researcher | WS-MODERN | 2026-08-23 ~14:50 IST | — | ACTIVE | — | literature/modern/prior_art_map.md | — |
| W2-INFOTH | (pending spawn) | Info Theory / Compression Researcher | WS-INFOTH | 2026-08-23 ~14:50 IST | — | ACTIVE | — | benchmarks/MEASUREMENT_PLAN.md | — |
| W3-LEIBNIZ | (pending spawn) | Leibniz Researcher | WS-LEIBNIZ | 2026-08-23 ~14:50 IST | — | ACTIVE | — | literature/leibniz/leibniz_extraction.md | — |
| W4-PRE | (pending spawn) | Pre-Leibniz Researcher | WS-PRE | 2026-08-23 ~14:50 IST | — | ACTIVE | — | literature/pre_leibniz/gate_rulings.md + system extractions | — |
| W5-POSTL | (pending spawn) | Post-Leibniz Researcher | WS-POSTL | 2026-08-23 ~14:50 IST | — | ACTIVE | — | literature/post_leibniz/*.md | — |
| W6-IR | (pending spawn) | Compiler / IR Researcher | WS-IR | 2026-08-23 ~14:50 IST | — | ACTIVE | — | literature/modern/ir_analogy_assessment.md | — |

Concurrency control: max ~6 active workers during P1 (within the 4–7 guideline). Experimental engineering and full Red Team deliberately NOT activated until P3/P4.
