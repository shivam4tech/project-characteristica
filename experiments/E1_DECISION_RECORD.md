# E1 Decision Record & Countersignature (W0f)

**Date:** 2026-08-24 ~15:50 IST
**Countersigned by:** Research Director (characteristica-prime authority), on explicit operator greenlight relayed via coordinator session.
**Pre-registration:** `experiments/E1_PRE_REGISTRATION.md` (213 ln, FROZEN 14:34 IST). No modifications permitted after this signature except via documented amendment + re-countersignature.

## Deferred decisions — RESOLVED per Appendix A recommendations

| ID | Decision | Resolution |
|---|---|---|
| D-1 | SIR-oracle diagnostic column | **OMITTED** from E1 scoring; caveat logged in results template |
| D-2 | Model pinning | Single model family, pinned at run start and recorded in results header |
| D-3 | Paraphrase testing | Moved to E2 (out of E1 scope) |
| D-4 | Converter = executor identity | Same model for both roles |

## Gate status

- W0a pre-registration frozen ✅ · W0b task banks concrete ✅ · W0c metrics bound to MEASUREMENT_PLAN §1.4 ✅ · W0d seeds/stopping declared ✅ · W0e budget fit (≤9h vs 22h remaining) ✅ · **W0f Director countersignature — THIS DOCUMENT** ✅

## Execution authorization

The Experimental Engineering Lead is authorized to build the E1 harness and execute all scored runs per the frozen pre-registration, under these binding conditions:

1. Results written incrementally to `experiments/results/` after every run batch (checkpoint discipline).
2. Any deviation from pre-registration (API failure patterns, unexpected arm behavior requiring protocol change) → STOP and escalate; do not improvise protocol changes.
3. Raw outputs retained verbatim; no post-hoc filtering.
4. Hours charged honestly against E1's 9.0h allocation.
