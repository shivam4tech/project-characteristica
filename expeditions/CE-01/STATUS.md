# CE-01 Status Dashboard

_Living document. Update after every substantive work session. Last updated: 2026-08-28 19:15 IST (Director session — P5 verdict RED, Cycles 1–5 complete, paper FINAL)._

## Current Phase

**P5 — Verdict Synthesis → P6 Ship** (entered 2026-08-28) — P2 DONE, P3 DONE, P4 ACCEPT, P5 RED issued

**P1 exit: SIGNED OFF 2026-08-24 by Research Director after direct inspection of all seven deliverable sets** (not on coordinator summary): `literature/leibniz_extraction.md` (716 ln, 12 primary passages w/ scan-verified GP page cites), `literature/pre_leibniz/gate_rulings.md` + 6 extraction files (289 ln), `literature/post_leibniz/formal_systems_extraction.md` (371 ln incl. §8), `literature/modern/prior_art_map.md` (196 ln, 16/16 domains), `benchmarks/MEASUREMENT_PLAN.md` (267 ln), `literature/modern/ir_analogy_assessment.md` (142 ln, FINAL). Verification performed: full read-through; placeholder sweep across literature/, benchmarks/, systems/ returned ZERO hits; spot-checked citations (Wilkins Essay pp. 23/395/404 scans; Descartes AT I 76–88 dating flag; Kircher letter properly quarantined Unresolved; Leibniz OCR-error bracketing discipline). Standards hold. One deficiency logged as blocked item (see below): LINGENIC_CRITICAL_ANALYSIS.md absent from repo contrary to directive description — does not gate P1 exit since Lingenic was never in the citation chain.

## Budget Ledger

| Quantity | Value |
|---|---|
| Total budget | 40.0 agent-hours |
| Elapsed (cumulative agent work) | ~32.5 h (reconciled Cycles 1–5; ledger estimates include overnight orchestrator ~4 h + paper/P4/P5 ~6 h) |
| Remaining | ~7.5 h |
| Hard-cap warning threshold | 36.0 h (no new workstreams past this point — headroom 3.5 h) |

Note: wall-clock time ≠ research budget. Multiple agents may run concurrently; hours are charged per agent-hour of substantive work. Dead batch `deleg_ff12b2e5` charged 0.0 h (see WORKERS.md incident log). Teardown batch `deleg_791e44c6` charged 1.0 h conservative (WORKERS.md incident log #2).

| Phase | Allocated | Spent |
|---|---|---|
| P0 Setup & Registration | 3.0 | 0.0 |
| P1 Parallel Reconnaissance | 14.0 | 14.8 |
| P2 Synthesis | 6.0 | 1.7 |
| P3 Pilot Experimentation | 9.0 | ~7.5 (incl. overnight ox-alpha 600+300+180 + 8192 sensitivity 70) |
| P4 Adversarial Review | 4.0 | ~2.0 (P4_PREP + Cycle 4 recomputation, 15-cell + ALL-600 sweep, G1–G8) |
| P5 Verdict Synthesis | 4.0 | ~1.5 (Cycle 5 verdict + ledger C-020–C-030, modern-technical rewrite) |
| Paper FINAL | — | ~2.5 (Cycles 2–3, 351 ln + 5 figs) |

(P1 spent exceeds its 14.0 allocation by 0.8 h due to two batch failures and re-dispatches; absorbed without expanding total budget.)

(P3 spend as of 08-25 01:30 IST: +2.5 h WS-E1EXEC wait/analysis pass — ≈0.5 h substantive analysis/escalation + ≈2.0 h mandated sleep-540 polling per protocol cap; see WS-E1EXEC row. Earlier same-day E1 build/smoke/amendment/supervision sessions are NOT yet itemized in this ledger; Director to reconcile before P3 close-out.)

## Active Workstreams

| ID | Workstream | Owner role | Phase | Hours used | Status |
|---|---|---|---|---|---|
| WS-HIST-PRE | Pre-Leibniz genealogy (relevance-gated) | Pre-Leibniz Researcher | P1 (closed) | 3.0 | **DELIVERED & DIRECTOR-VERIFIED** (W15b, deleg_3bfb7ce6) — gate_rulings.md (83 ln, G1–G9 criteria, 7 candidates adjudicated: Llull/Descartes/Wilkins/Dalgarno PASS, Beck/Kircher narrow PASS, Jungius honestly DEFERRED) + 6 extraction files, 289 ln total. Follow-ups logged: New Essays loci pinning, EEBO access for Jungius, Cram & Maat 2001 for Dalgarno details. |
| WS-MODERN | Modern representation prior-art survey | Modern Representation Researcher | P1 (closed) | 2.5 | **DELIVERED & DIRECTOR-VERIFIED** (W13+W13b, deleg_12a59098/deleg_3bfb7ce6) — prior_art_map.md 43→196 lines, 16/16 domains done. Key finding: SIR layer unoccupied (provisional, PI re-verification gated); LLVM/MLIR vs Cyc/UNL split shows value must be ecosystem economics not expressive power (AAAI-25 isomorphism pressure). |
| WS-LEIBNIZ | Leibniz deep study | Leibniz Researcher | P1 (closed) | 3.5 | **DELIVERED & DIRECTOR-VERIFIED** (W14, deleg_12a59098) — leibniz_extraction.md 716 lines, 75 labeled findings, 12 primary passages w/ verified GP page cites; Gerhardt vols 4+7 djvu.txt downloaded locally. Escalation: Generales Inquisitiones NOT in Gerhardt (Couturat 1903 first print) — conditional follow-up registered as C-015; NOT blocking P3 (registered H2–H5 do not lean on contingency theory). |
| WS-POSTL | Post-Leibniz formal systems | Post-Leibniz Researcher | P1 (closed) | 1.4 | **DELIVERED & DIRECTOR-VERIFIED** (W17b, deleg_2744c6de) — extraction file 67→371 lines, all 7 systems + synthesis §8, placeholder-free. Key finding: A1+A2+A4 hard trade-off; conversion economics is the recurring killer (Director refinement: second failure class = foundational collapse; see C-007). |
| WS-IR | Compiler/IR analogy assessment | Compiler/IR Researcher | P1 (closed) | 0.9 | **DELIVERED & DIRECTOR-VERIFIED** (W18b, deleg_2744c6de) — assessment FINAL, 142 lines, 8 refs inspected, zero placeholders. Verdict: analogy survives as process not promise; checkpoint-contract posture; ~10–14 eng-day one-off cost + ~20% velocity tax. |
| WS-INFOTH | Measurement & compression theory framing | Info Theory Researcher | P1 (closed) | 2.5 | **DELIVERED & DIRECTOR-VERIFIED** (deleg_7d20d0d8, W16) — MEASUREMENT_PLAN.md 267 lines, placeholder-free. Claims C-INFOTH-1…5 transcribed to CLAIM_LEDGER.md as C-012…C-014 (+C-004 cross-ref). |
| WS-E1PRE | E1 pre-registration (P3 gate step) | Experimental Engineering Lead (Director bounded eng.) | P3 | 1.5 | **DELIVERED & COORDINATOR-VERIFIED** (14:20–14:34 IST session 20260824_142020) — experiments/E1_PRE_REGISTRATION.md 213 ln FROZEN: families EX/CP/TU (TU adversarial predicted-loss), 4 mandatory arms, amortization N∈{1,10,25,100}, relation-label set frozen (resolves csir0 open debt #2), 7 predictions each with falsification condition, W0a–W0f pre-run gates incl. Director countersignature before any scored call. Zero model calls made. Deferred decisions D-1…D-4 in Appendix A. |
| WS-E1EXEC | E1 scored-run execution + results assembly | Experimental Engineering Lead (Director bounded eng.) | P3 | 0.5 (+2.0 wait) | **SNAPSHOT RESULTS DELIVERED under AMENDMENT-2** (01:26 IST 08-25; matrix mid-flight, ox-alpha pass ~150/h): results/E1/E1_RESULTS.md computed directly from raw_outputs per §1.4 (outcomes.csv unwritable — root-caused flush deadlock, INTERRUPTION_LOG #3, DEV-9 candidate awaiting Director; RLock one-liner). Verdicts on ox-alpha population: H3 FALSIFIED-as-registered ($-degenerate instrument), H0 STANDS, H1 no support (any family); P1–P7 NOT EVALUABLE at snapshot (SIR/CP/TU cells + repl/H2/F3 stages absent; TU predicted-loss neither confirmed nor contrary — reported honestly); H5 N/A by design (D-3). EX observation: 100% silent-error rate in ALL arms (F0-pass, gate-fail, score≈0.74–0.82). glm-5.2 pilot set quarantined per Amd-2 — scored payloads destroyed by in-place overwrites before preservation (metadata-only appendix + 4 smoke-era specimens; agreement check impossible). 06:00 cron completes matrix; re-run make_results then refresh §8 tables. Prior E1EXEC sessions not itemized here — Director to reconcile. |

## Blocked Workstreams

_None blocking P3 entry._ Registered non-blocking items (tracked in CLAIM_LEDGER.md / P2_SYNTHESIS.md §5):

| Item | Ledger | Unblock condition |
|---|---|---|
| Lingenic primary text retrieval (SSRN HTTP 403) AND missing `LINGENIC_CRITICAL_ANALYSIS.md` (directive described it at project root; `find` across repo returns nothing) | C-016 | Locate/reconstruct analysis file + retrieve SSRN text via alternate access; until then Lingenic excluded from ALL citation chains. Not needed for E1/E2. |
| Generales Inquisitiones primary extraction (Couturat Opuscules 1903 / Schupp) | C-015 | CONDITIONAL: required only if any E1 hypothesis leans on Leibniz's contingency theory. Current H2–H5 do not. Revisit on any hypothesis change. |
| Jungius ruling (EEBO / Jungii Opuscula access) | C-005 | <30 min task once source access exists; out of critical path. |
| New Essays Dalgarno/Wilkins loci pinning | C-005 note | Citation hygiene; needed only if Wilkins/Dalgarno reception becomes claim-bearing. |
| Kircher 1670 letter contact claim | C-005 | Stays Unresolved; verified quarantined from all citation chains this session. |

## Hypotheses Under Investigation

| ID | Statement (abbrev.) | Status |
|---|---|---|
| H1 | An SIR beats strong NL prompting on some task classes net of conversion overhead | **FALSIFIED — no support in any family (0/3): $ beat fails, F1 deficit 74/73/94 pts >δ, repl CP/TU True EX False moot, P4 ACCEPT)** |
| H0 | Net of all overheads, SIR gives no meaningful general advantage | **SUPPORTED — stands, favored (0 families pass H1; SIR strictly dominated by JSON on F1 + tokens in every family)** |
| H2 | Closed primitive vocabulary reduces output variance even at equal mean accuracy | **NOT-EVALUABLE, degenerate (within-SD 0.000 <0.119<0.144 but means 0.086/0.838/0.323 fail precondition)** |
| H3 | Net SIR benefit is reuse-gated: non-positive at N=1, positive above break-even N* | **FALSIFIED via (a) Δ(N)≤0 ∀N (−9k..−11.5k tok, $≡0), no N* at any N** |
| H4 | Structured SIR shifts failures from silent-wrong to detected-and-flagged vs NL | **FALSIFIED (CP SIR 100% vs JSON 21.4% bought by total rejection + 74-pt F1 collapse; falsifier fires)** |
| H5 | Compressed/structured representations degrade more under paraphrase than plain NL | **DEFERRED to E2 (D-3, not tested in E1)** |

See `hypotheses/REGISTRY.md`.

## Experiments Planned

- **E1** (efficiency/fidelity pilot, 3 task families × 4 arms): measurement skeleton FIXED by `benchmarks/MEASUREMENT_PLAN.md`; candidate representation defined at `systems/csir0_architecture.md` (CSIR/0) with 8 falsifiable predictions (§9). NEXT STEP: Experimental Engineering Lead instantiates `experiments/E1_PRE_REGISTRATION.md` (freeze relation-label set against chosen families, δ margins, N/N_conv declarations, predicted outcomes per arm×family) BEFORE any run.
- **E2** (optional robustness/portability probe): paraphrase sets (H5 discriminator), ≥2 model families if budget permits.

## Experiments Completed

- **E1 primary** — 600/600 admitted (4×3×50, T=0, stealth/ox-alpha, 2026-08-25 01:32–05:22 IST, DEV-7 latest-TS, G1 PASS) — FINAL `E1_RESULTS_FINAL.md` §2–§9
- **H2 variance** — 300/300 (3×20×5 @T0.7, seeds 101–105) — NOT-EVALUABLE degenerate
- **Repl stochastic** — 180/180 (2×3×10×3 @T0.7, seeds 201–203) — CP/TU True, EX False
- **Amendment-3 sensitivity** — 70/150 @8192 cap fast-closed, identical failure, not folded
- **Fabrication sweep** — CLEAN over ALL 600 (P4 S2.4)
- **Paper** — 351 ln FINAL, 5 figs FINAL (150 dpi, Okabe-Ito)

## Strongest Positive Signal

**JSON-schema control:** captures the guide-rail value without SIR — CP +49.6 pts vs NL-plain, TU +22 pts vs NL-plain, and the only economically efficient frontier (3,493 tok/success). Single valid CSIR doc (EX-04-05, 0.813) shows executor *can* consume CSIR when it emits — population, not representation, is the wall.

## Strongest Negative Signal

**Converter wall:** K=11,112 tok/item (K_reinj 66.7% deterministic repair waste), 1/150 valid docs (0.7%), SIR F1 0.082/0.071/0.000 vs JSON 0.826/0.806/0.940, Δ(N) −9k..−11.5k no break-even at any N (C-021, C-026). P6 TU adversarial CONFIRMED stronger than predicted (0 vs 0.940). (Historical base rate now measured.)

## Unresolved High-Priority Questions

See `OPEN_QUESTIONS.md`. OQ11/OQ12/OQ13 resolution criteria are now MET (gate rulings; MEASUREMENT_PLAN §3 fidelity operationalization; IR assessment memo) — row updates pending Curator pass. Highest priority remaining: OQ4/OQ5/OQ8 via E1; OQ14 partially advanced by CSIR/0 sketch (minimal schema spec → E1 pre-registration).

OQ1/OQ2/OQ3 substantively answered by P1 + P2_SYNTHESIS mechanism map M-01…M-13 (ledger-traced); OQ3's occupancy claim requires Prior-Art Investigator re-verification before any novelty labeling (C-009 gate).

## Provisional Verdict

**RED — Discontinue CSIR/0 as specified (inference-time interchange with per-item neural converter)** — see `expeditions/CE-01/VERDICT.md` (Cycle 5, 2026-08-28).

_Rationale: P4 ACCEPT (8/8 gates PASS, fabrication CLEAN, TU verbatim PASS); H1 0/3 families (four-condition gate fails on 1+2 decisively); H3 falsified via (a) no N* at any N; P6 TU adversarial confirmed (stronger than registered); converter economics wall measured as Class-I per C-007/C-026 (K≈11.1k, 99.3% non-production). H0 stands, favored, scoped to stealth/ox-alpha at CE-01 power ceiling. Publishable negative result with diagnostic decomposition; no cheap lever identified (Amendment-3 sensitivity falsified MAX_TOKENS fix). Re-invest only via newly pre-registered expedition moving conversion off per-item hot path (distilled converter, checkpoint-contract framing, or programmatic synthesis)._

## Session Notes (Director)

- 2026-08-24: Resumed after host app exit killed batch `deleg_ff12b2e5`. Verified zero orphaned output; W1–W6 TERMINATED at 0.0 h. Process deviation recorded: with no Curator active and six workers running concurrently, workers do NOT edit `CLAIM_LEDGER.md` directly (concurrent-write hazard); they list claims in their deliverables and final reports, and the Director transcribes/dispositions them into the ledger during per-worker verification. Workers may append their own vetted entries to `BIBLIOGRAPHY.md`.
- 2026-08-24 (~13:55–15:30 IST, bounded engagement ≤2.0 h, actual charge 1.7 h): P1 exit review executed per directive — all seven deliverable sets read in full by Director; placeholder sweep clean; citation spot-checks passed (details in Current Phase entry). **P1 exit SIGNED.** Deficiency found and logged, not silently passed: LINGENIC_CRITICAL_ANALYSIS.md absent despite directive description (C-016). P2 synthesis completed: CLAIM_LEDGER.md populated (C-001…C-019, each transcribed only after Director verified the underlying deliverable text); hypotheses H2–H5 registered with ledger traceability; CSIR/0 architecture sketched at systems/csir0_architecture.md (structure + semantics only, no notation per P2 rule, every choice traced to ≥1 claim); unified mechanism map + stress-tested convergence points at expeditions/CE-01/P2_SYNTHESIS.md. Convergence point (a) supported WITH refinement (two failure classes, C-007); H0 remains live and is stated as such in P2_SYNTHESIS §3. No delegate_task used (parent-exit teardown rule honored).
