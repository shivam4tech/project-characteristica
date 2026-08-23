# Open Questions

Tracked questions for Project Characteristica / CE-01. OQ1–OQ10 are the operational questions from `RESEARCH_QUESTION.md` (verbatim intent); OQ11+ are setup-derived. Statuses: `open` / `in-progress` / `resolved` / `parked`. Update rows as evidence lands; resolution requires meeting the stated criteria.

| ID | Question | Priority | Owner | Dependencies | Current evidence | Status | Resolution criteria |
|---|---|---|---|---|---|---|---|
| OQ1 | What mechanisms recur across important historical systems of representation? | High | Historical Foundations Lead (+era researchers) | P1 recon workstreams | none | open | ≥5 systems extracted per Protocol §2; recurring-mechanism table produced and registered in ledger |
| OQ2 | Which of those mechanisms have modern technical analogues? | High | Chief Scientist | OQ1, WS-MODERN | none | open | Each recurring mechanism mapped to ≥0 modern analogue with citation or explicitly marked "none found" |
| OQ3 | What existing work already occupies this research space? | Critical | Modern Representation Researcher → Prior-Art Investigator | WS-MODERN | none | open | Prior-art landscape map covers all 16 Protocol §3 domains; nearest-neighbor analysis done for candidate mechanisms |
| OQ4 | Can human intent be transformed into a more compact structured representation without material semantic loss? | Critical | Chief Scientist + Experimental Engineering Lead | OQ2, OQ12, E1 | none | open | Pilot measures fidelity vs. compactness on pre-registered tasks; loss thresholds defined in advance |
| OQ5 | Can such a representation improve token use, cost, latency, consistency, reasoning, or interoperability? | Critical | Experimental Engineering Lead | OQ4, benchmark framework, E1 | none | open | E1 completed vs. strong baselines incl. optimized NL and JSON/schema arms, full overhead accounting |
| OQ6 | Can the same underlying representation work across multiple model families? | Medium | Experimental Engineering Lead | E1 signal, ≥2 model APIs available | none | open | Same SIR (stable schema) tested on ≥2 independently developed model families; portability delta reported |
| OQ7 | Does the representation generalize across substantially different task classes? | High | Experimental Engineering Lead | Benchmark framework (≥2–3 task families in CE-01) | none | open | ≥2 distinct task families tested under identical protocol; interaction effects reported |
| OQ8 | Does translation into and out of the representation introduce more cost or error than it saves? | Critical | Info Theory Researcher + Experimental Lead | OQ10 measurement plan, E1 | none | open | Conversion overhead measured end-to-end (tokens, time, error rate); net-benefit curve vs. reuse count plotted |
| OQ9 | Where does natural language outperform structured semantic representations? | High | Red Team / Cassandra | E1 results | none | open | Failure-mode list for SIR conditions documented from pilot data, not speculation |
| OQ10 | Is there enough evidence after CE-01 to justify a larger research program? | Critical | Research Director | all of the above, red-team memo | none | open | FINAL_REPORT issues defensible GREEN/AMBER/RED per Protocol §10 decision standard |
| OQ11 | Which pre-Leibniz systems pass the historical relevance gate, and on what written justification? | High | Pre-Leibniz Researcher | relevance gate (CE-01 README) | none — gate defined, no rulings yet | open | Per-system ruling logged within 30 min of study start; failing systems archived with rationale |
| OQ12 | How should "semantic fidelity" be operationalized so it is measurable and hard to game? | Critical | Info Theory Researcher | WS-INFOTH | none | open | Measurement plan defines fidelity metric(s), elicitation procedure, and gaming-resistance argument before E1 runs |
| OQ13 | Is the compiler IR analogy technically load-bearing or merely decorative for an SIR? | Medium | Compiler/IR Researcher | WS-IR | none | open | Memo lists concrete borrowable design elements AND disanalogies with implications; registered as claim |
| OQ14 | What is the minimal schema/grammar spec an LLM needs to reliably emit and consume the candidate SIR? | High | Chief Scientist + Experimental Lead | P2 architecture sketch | none | open | Prototype round-trips ≥N example tasks with error rate below pre-set threshold using ≤K instruction tokens |

### Seeding note
OQ11–OQ14 were added at setup because they block P1/P2/P3 work and were implicit in the governance docs but never tracked.
