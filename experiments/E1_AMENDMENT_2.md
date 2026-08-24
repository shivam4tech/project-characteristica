# AMENDMENT-2 to E1 Decision Record — Uniform Re-Pin to stealth/ox-alpha

**Date:** 2026-08-25 ~00:45 IST
**Authority:** Research Director under Operator Standing Grant. Countersigned: ✅ W0f″
**Trigger:** Operator reset API keys (~22:00 IST), restoring stealth/ox-alpha daily quota. Live probe 00:40 IST: `stealth/ox-alpha` WORKS (cost=0); `z-ai/glm-5.2:free` returning 429s again. Rationale for original glm pin (only free-tier model verifiably serving at 18:52) no longer holds.

## Amendment

**D-2 superseded:** All REMAINING scored cells execute on `stealth/ox-alpha`. The ~90 cells already completed on glm-5.2 are **quarantined** to `results/E1/glm_pilot_appendix/` — treated as a pilot-replication set, NOT merged into the primary per-arm analysis (mixing models inside arm comparisons would confound).

## Binding conditions

1. Primary analysis runs exclusively on ox-alpha-scored cells; every cell must carry `"model": "stealth/ox-alpha"` in its outcome record to be admitted.
2. P8 flag EXTENDED: results header names BOTH models used across the expedition and scopes conclusions accordingly; glm-vs-ox-alpha agreement on overlapping cells (if any get re-run) reported as a robustness check.
3. All seven registered predictions evaluated exactly as stated on the ox-alpha matrix. No re-wording.
4. Quota guard: ox-alpha daily budget ≈1000 req shared with agent infrastructure. Runner monitors remaining-cell count; if quota exhausts mid-matrix, runner pauses cleanly (checkpointed) and resumes on next daily reset — glm-5.2 is NOT a fallback for primary data.
5. No other design element changes (arms, families, metrics, N-grid, stopping rules, §1.4 formulas).
