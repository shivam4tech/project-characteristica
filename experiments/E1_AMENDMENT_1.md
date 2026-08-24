# AMENDMENT-1 to E1 Decision Record — D-2 Model Re-Pin

**Date:** 2026-08-24 ~17:50 IST
**Authority:** Research Director acting under Operator Standing Grant (RESUME_STATE.md, 2026-08-24): full autonomy granted; escalate only budget>36h / foundational breaks / direction changes.
**Trigger:** Scored-run gate blocked 2026-08-24 ~17:35 IST: pinned model `openai/gpt-5.4-mini` returns HTTP 402 (key is OpenRouter free-tier). Worker correctly STOPPED per decision-record condition #2. Zero scored calls executed — pre-registration uncontaminated.

## Amendment

**D-2 revised:** The pinned model shall be **the highest-capability OpenRouter `:free`-tier model verifiably serving at run time**, selected once, recorded in the results header with its exact model id, and used for ALL arms identically (converter and executor alike, preserving D-4).

**Rationale:** funding constraint, not design preference. Original pin becomes Path-A confirmation batch should operator credit arrive later.

## Scientific integrity conditions (binding)

1. Selection rule applied ONCE before first scored call; no switching thereafter.
2. Results header records: amended model id, free-tier status, and this amendment reference.
3. Results template MUST carry Red Team flag P8 (model dependence): conclusions are provisionally scoped to the amended model family until a paid-model confirmation batch (E1b) replicates direction.
4. All seven registered predictions evaluated exactly as stated against the amended model's data; no re-wording.
5. This amendment does NOT touch arms, families, metrics, N-grid, seeds logic, stopping rules, or §1.4 analysis formulas.

## Countersignature

Director countersignature renewed for amended configuration: ✅ W0f' 2026-08-24.
