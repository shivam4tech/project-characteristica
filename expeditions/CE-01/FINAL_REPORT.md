# CE-01 Final Report — The Converter Wall

**Expedition:** CE-01 · Project Characteristica · E1 Efficiency/Fidelity Pilot  
**Date:** 2026-08-28 19:20 IST (Cycle 5)  
**Status:** Paper FINAL + P4 ACCEPT + **Director Verdict RED** — expedition closed, ready to ship (Cycle 6).  
**One-line outcome:** CSIR/0 as a per-item neural interchange fails on conversion economics (K≈11.1k, 0.7% valid), strictly dominated by JSON-schema in every family — a measured UNL-replay, not a theory.

## Executive summary (for `foundation/`)

CE-01 asked whether a validated semantic interchange (CSIR/0) could beat strong NL prompting net of overhead on a pre-registered task distribution (EX/CP/TU). Under P4-verified accounting (600 primary @T=0 + 300 h2 + 180 repl + 70 sensitivity @8192, stealth/ox-alpha, DEV-7-admitted), the answer is **no — discontinued as specified**, with a single-model, CE-01-scale, power-ceiling-scoped RED. The wall is **per-item K_reinj (66.7% of cost, deterministic T=0 repair waste)** before any F1 point, with no break-even at any N. The JSON-schema arm already captures the guide-rail value. When the converter did emit (1/150), that doc scored 0.813 — representation not refuted, population mechanism is. Three cheaper levers (distilled/programmatic converter, checkpoint-contract framing, cross-model replication) are pre-falsifiable prerequisites for any CE-02, not a retry on this contract.

## Measurement provenance

- **Design:** pre-registered `E1_PRE_REGISTRATION.md` (FROZEN 2026-08-24, Amendments 1–3), `MEASUREMENT_PLAN.md` §1.4 formulas only, 4 arms ×3 families ×50 items, N∈{1,10,25,100}, δ_F1 3/4/3, δ_F3 0.90.
- **Data:** `experiments/results/E1/outcomes.csv` 621→600 admitted + `h2_outcomes.csv` 370→300 + `repl_outcomes.csv` 196→180 + `rerun_sir_outcomes.csv` 70@8192 (fast-closed, not folded).
- **Authoritative numbers:** `E1_RESULTS_FINAL.md` (FINAL, 600 + h2 + repl, Addenda A/B).
- **Governance:** P4 `ACCEPT` (8/8 gates PASS, ALL-600 fabrication CLEAN, 15-cell cost/score recomputation within rounding, TU verbatim PASS) — `critiques/P4_REVIEW_DRAFT.md` §4 + `P4_PREP.md`.
- **Root cause:** `critiques/A1_ROOT_CAUSE.md` (BOTH: instrumentation staleness + genuine 99.3% non-production at MAX_TOKENS 2048, verified at 8192).

## Key deltas to interim

Interim had SIR `doc_valid=True`, `kerr_flag=False`, `conv_errors=[]` self-contradiction + 593/600 coverage + empty `f2_audit.json`. FINAL reconciles: telemetry now self-consistent (149/150 `kerr=True`⇔`doc_valid=False`⇔`json:no JSON object found`), 600/600 complete, `f2_audit.json` populated (yet F2 still NOT-EVALUABLE for lack of valid docs), rerun 70 identical signature.

## Hypothesis outcomes (registered language)

- **H1 (central):** NO SUPPORT in any family (0/3) — $ beat fails, F1 deficits 74/73/94 pts >δ, repl CP/TU True EX False moot, P4 ACCEPT.
- **H0 (null):** STANDS, FAVORED — strictly dominated in every family, no detectable advantage at CE-01 scale.
- **H3 (reuse-gated):** FALSIFIED via (a) Δ(N)≤0 ∀N (−9k..−11.5k tok, $≡0), no N* anywhere.
- **P6 TU adversarial:** CONFIRMED, stronger than registered (0.000 vs 0.940, Δ−0.940).
- **P5/H4 (silent-error):** FALSIFIED (reduction explained by JSON + bought below δ, degenerate validator).
- **H2 (variance):** NOT-EVALUABLE, degenerate (stability-at-failure).
- **P2/P3/P7 (F2/F3):** NOT-EVALUABLE (instruments absent with 1/150 valid docs).
- **Latency prediction:** INVERTED — SIR fastest (17.2s p50 vs JSON 29.4s), but degenerately.

## Ledger and verdict pointers

- Ledger: `CLAIM_LEDGER.md` C-020–C-030 (Experimental Result / Falsified, `checked-clean`/`cleared`).
- Verdict: `expeditions/CE-01/VERDICT.md` (23k, modern technical language, §6 levers + publishable package).
- Paper: `paper/E1_PAPER_DRAFT.md` (351 ln, 6,454 w, 5 figs FINAL, [DATA:] 0, refs 19).
- Prior-art dispositions: CC1 confirmation, CC2 arithmetic (no N*), CC3 fallback wording "first evaluated" per §5.3.

## Publishable package

Negative result (H1 0/3, H3 falsified, P6 confirmed) + diagnostic K decomposition + Pareto frontier (JSON frontier) + method asset (pre-reg + adversarial family + DEV-7 admission + P4 recomputation). Wording gates honored (no detectable advantage, single-model scope, cost always paired with F0–F3, N-grid shown, TU verbatim P6, no cherry-picked N).

## What remains before `origin/main` push (Cycle 6)

Commit & push all (73 modified + ledgers + verdict + paper + STATUS + foundation), pause/keep watchdog `75a8ca76a1b4` as appropriate, final `verify` audit.

*— Director, characteristica-prime, Cycle 5 close. This file supersedes `expeditions/CE-01/P2_SYNTHESIS.md` as the current synthesis.*
