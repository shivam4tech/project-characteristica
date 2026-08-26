# AMENDMENT-3 to E1 Decision Record — SIR-Arm Re-Run (Converter Cap Fix)

**Date:** 2026-08-25 ~15:00 IST (2026-08-26 session)
**Authority:** Research Director under Operator Standing Grant. Countersigned: ✅ W0f‴
**Trigger:** A1_ROOT_CAUSE.md verdict — converter starvation at `MAX_TOKENS=2048` (445/448 calls burned cap pre-output, empty content; temp=0 repairs identical). Sole produced document scored 0.8125 → architecture untested, pipeline was.

## Amendment

The **CSIR-SIR arm only** is re-run across all three families (EX/CP/TU × 50 items = 150 cells) with `MAX_TOKENS=8192`. All other arms' primary data stand untouched.

## Binding conditions

1. Re-run cells written to a separate namespace (`*_rerun` rep tag / separate CSV) — never mixed with primary outcomes.csv.
2. Results header discloses both runs and the cap difference (2048 vs 8192).
3. Analysis reports BOTH: original SIR data (as-designed-at-the-time) AND re-run (as-intended), plus the delta — the comparison itself is a finding about sensitivity to decoding budget.
4. All 7 registered predictions re-evaluated on the re-run SIR population alongside originals; no re-wording of predictions.
5. Baseline arms are NOT re-run (no reason to believe 2048 harmed them; their outputs were non-empty by inspection).
6. If re-run SIR scores remain ≈0 with valid docs produced → the architecture finding stands strengthened. If scores jump → conversion-budget sensitivity becomes the headline finding. Either way publishable per charter.
