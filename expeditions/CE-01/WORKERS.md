# CE-01 Worker Registry

Live roster of delegated workers. Statuses: QUEUED / ACTIVE / BLOCKED / COMPLETED / TERMINATED / NEEDS_REVIEW / PAUSED. Worker IDs are lab-side identifiers; Hermes subagent IDs are recorded when returned by delegation. This registry prevents duplicated or orphaned research.

## Terminated batch — `deleg_ff12b2e5` (incident log)

Dispatched 2026-08-23 14:46 IST; killed same day by host app exit before any worker produced output. Director verified 2026-08-24 via transcript inspection (`~/.hermes/profiles/characteristica-prime/cache/delegation/live/deleg_ff12b2e5/task-{0..5}.log`) that every worker read only binding docs, then failed at ~22 s with `HTTP 429: Rate limit exceeded: free-models-per-day-stealth`. All six output-target directories were empty at verification time; FINAL_REPORT.md 0 bytes. Zero hours charged. Roster rows below retained for audit, superseded by re-dispatch.

| Worker ID | Hermes ID | Role | Workstream | Start | Stop | Status | Last report | Output files | Director disposition |
|---|---|---|---|---|---|---|---|---|---|
| W1-MODERN | sa-0-982d65a2 | Modern Representation Researcher | WS-MODERN | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |
| W2-INFOTH | sa-1-da2863c1 | Info Theory / Compression Researcher | WS-INFOTH | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |
| W3-LEIBNIZ | sa-2-66a63080 | Leibniz Researcher | WS-LEIBNIZ | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |
| W4-PRE | sa-3-3fd68abb | Pre-Leibniz Researcher | WS-PRE | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |
| W5-POSTL | sa-4-539fc6ae | Post-Leibniz Researcher | WS-POSTL | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |
| W6-IR | sa-5-84f53c4d | Compiler / IR Researcher | WS-IR | 2026-08-23 14:52 IST | 2026-08-23 (host exit) | TERMINATED | died pre-output (HTTP 429) | none produced | no hours charged |

## Terminated batch — `deleg_791e44c6` (incident log #2)

Dispatched 2026-08-24 ~12:34 IST by Director kickoff run; all six workers interrupted simultaneously at 12:43:06 IST — the exact moment the Director's parent CLI session exited (session 20260824_122345, duration 19m21s). Cause: Hermes tears down child subagents when the parent session ends; the Director completed its other duties and closed its session while the batch was still running. **This was NOT an API/rate-limit failure** — transcript inspection shows workers productively verifying sources right up to termination (W7: 9 papers verified via arXiv API + AMR/AAAI full-text extractions; W10: downloaded Loemker DAC text/PDF + OUP intro to literature/pre_leibniz/sources/; W3: located complete Gerhardt Die philosophischen Schriften vol. 4 & 7 djvu.txt on Internet Archive). No output .md files were written. Substantive work performed before teardown ≈ 0.9 agent-hours aggregate; charged as 1.0 h to be conservative. Salvage: downloaded source files retained in literature/pre_leibniz/sources/.

| Worker ID | Hermes ID | Role | Workstream | Start | Stop | Status | Last report | Output files | Director disposition |
|---|---|---|---|---|---|---|---|---|---|
| W7-MODERN | sa-0-1864acd6 | Modern Representation Researcher | WS-MODERN | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted mid-API-call, post-verification of 9 sources | none written (work in transcript only) | 0.2 h charged; re-dispatched as W13 |
| W8-INFOTH | sa-1-5e005fe0 | Info Theory / Compression Researcher | WS-INFOTH | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted mid-API-call | none written | 0.15 h charged; re-dispatched as W16 |
| W9-LEIBNIZ | sa-2-d6d15b40 | Leibniz Researcher | WS-LEIBNIZ | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted; had located Gerhardt vols on archive.org | none written | 0.2 h charged; re-dispatched as W14 |
| W10-PRE | sa-3-900fb72c | Pre-Leibniz Researcher | WS-PRE | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted; sources downloaded to literature/pre_leibniz/sources/ | source PDFs/TXTs retained | 0.2 h charged; re-dispatched as W15 |
| W11-POSTL | sa-4-8b264a73 | Post-Leibniz Researcher | WS-POSTL | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted mid-API-call | none written | 0.15 h charged; re-dispatched as W17 |
| W12-IR | sa-5-a9fd635a | Compiler / IR Researcher | WS-IR | 2026-08-24 12:34 IST | 2026-08-24 12:43:06 (parent teardown) | TERMINATED | interrupted mid-API-call | none written | 0.1 h charged; re-dispatched as W18 |

**Structural lesson recorded:** one-shot `hermes chat --query-file` sessions MUST NOT leave delegate_task batches running at turn end. Either the Director holds its session open until batch consolidation completes, or work hosting moves to a session that persists (desktop coordinator session) or is made resumable (per-role sessions with file-based checkpoints).

## Completed batch — P1 reconnaissance (third attempt, hosting via desktop coordinator)

**Hosting model:** workers dispatched by the desktop coordinator session (operator chat), not a one-shot Director CLI run. All six workers DELIVERED; all outputs DIRECTOR-VERIFIED 2026-08-24 ~13:55–15:30 IST per the completion rule below (files opened and read in full; placeholder sweep clean; citation spot-checks passed). P1 exit signed in STATUS.md.

| Worker ID | Hermes ID | Role | Workstream | Start | Stop | Status | Last report | Output files | Director disposition |
|---|---|---|---|---|---|---|---|---|---|
| W13-MODERN | sa-0-c5684ea5 | Modern Representation Researcher | WS-MODERN | 2026-08-24 ~13:20 IST | 2026-08-24 ~13:50 IST | COMPLETED (deleg_12a59098) | delivered within 5.5 h budget | literature/modern/prior_art_map.md (196 ln, 16/16 domains) | VERIFIED: read in full; seed-source re-verifications checked (AAAI-25 DOI/abstract inspected; SSRN 403 honestly flagged); cross-domain synthesis sound. Claims → C-008/C-009/C-010/C-016. Hours 2.5 confirmed. |
| W14-LEIBNIZ | sa-1-ffeb615a | Leibniz Researcher | WS-LEIBNIZ | 2026-08-24 ~13:20 IST | 2026-08-24 ~13:55 IST | COMPLETED (deleg_12a59098) | delivered within 4.0 h budget | literature/leibniz_extraction.md (716 ln) | VERIFIED: read in full incl. §3 SECONDARY marking, §5 failure analysis, §7 escalations; GP page-marker discipline ("page seen") consistent throughout; Gen.Inq. gap escalated correctly. Claims → C-001…C-004, C-015, C-017, C-018(shared). Hours 3.5 confirmed. |
| W15-PRE | sa-2-4a90ea87 | Pre-Leibniz Researcher | WS-HIST-PRE | 2026-08-24 ~13:20 IST | 2026-08-24 ~13:45 IST | COMPLETED (deleg_12a59098) | delivered within 3.5 h budget | gate_rulings.md + 6 extraction files (289 ln total) | VERIFIED: rulings + Wilkins + Descartes + Kircher files read; reception discipline enforced (Kircher letter Unresolved, properly quarantined); Jungius deferral honest. Spot-check basis for remaining 3 files: placeholder sweep + line counts + ruling-file cross-references. Claims → C-005. Hours 3.0 confirmed. |
| W16-INFOTH | sa-0-be0b7667 | Info Theory / Compression Researcher | WS-INFOTH | 2026-08-24 ~13:22 IST | 2026-08-24 ~13:40 IST | COMPLETED (deleg_7d20d0d8) | delivered within 3.0 h budget | benchmarks/MEASUREMENT_PLAN.md (267 ln) | VERIFIED: read in full; worked example §1.9 recomputed by Director — two arithmetic slips found in the ILLUSTRATIVE numbers (N=1 total $0.00194 not reachable from its printed terms → $0.00163; N=25 "~1.9×" ignores the plan's own symmetry rule for the NL arm → ~1.69×); both directions survive correction, binding formulas §1.4 correct, finding logged in P2_SYNTHESIS §5 with instruction to compute pre-registration figures from §1.4 only. Claim register C-INFOTH-1…5 transcribed → C-012/C-013/C-014. Hours 2.5 confirmed. |
| W17-POSTL | sa-1-4f8aadc9 | Post-Leibniz Researcher | WS-POSTL | 2026-08-24 ~13:22 IST | 2026-08-24 ~13:50 IST | COMPLETED (deleg_2744c6de) | delivered within 3.5 h budget (self-report 1.4 h) | literature/post_leibniz/formal_systems_extraction.md (371 ln) | VERIFIED: read in full incl. all 7 Protocol-§2 tables + §8 synthesis + source register S-P1…S-P11; escalation notes honest. Claims → C-006, C-007(shared). Hours 1.4 confirmed. |
| W18-IR | sa-2-f929a861 | Compiler / IR Researcher | WS-IR | 2026-08-24 ~13:22 IST | 2026-08-24 ~13:40 IST | COMPLETED (deleg_2744c6de) | FINAL, within 2.5 h budget | literature/modern/ir_analogy_assessment.md (142 ln) | VERIFIED: read in full; R1–R10 internally consistent with M/D tables; [S1]–[S8] all real documents. Claims → C-011, C-018(shared), C-019(Director-added from [S7]). Hours 0.9 confirmed. |

Common brief: `expeditions/CE-01/WORKER_BRIEF_COMMON.md` (checkpoint discipline: append each studied system immediately).

Director completion rule: no worker is marked COMPLETED until the Director opens its output files, checks for placeholder text ("[Insert", "TODO", "[TBD]"), spot-checks ≥1 citation per file against Protocol §1 hierarchy, and only then charges hours in STATUS.md. Hermes subagent IDs recorded from dispatch handles above.

Concurrency control: max ~6 active workers during P1. Experimental engineering and full Red Team deliberately NOT activated until P3/P4.

**Next planned dispatches (P3):** Experimental Engineering Lead (E1 pre-registration + harness) — NOT yet dispatched; awaiting operator go, since E1 consumes budget (allocation 9.0 h of 23.5 h remaining).
