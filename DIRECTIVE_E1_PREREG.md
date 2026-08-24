# DIRECTIVE — E1 Pre-Registration (CE-01 P3 gate step)

**From:** Operator via coordinator session, 2026-08-24 ~15:35 IST
**Role:** You are the Experimental Engineering Lead (ORGANIZATION.md §11) for this bounded engagement. Budget: **≤2.0 agent-hours**.

## Context
P1 delivered and verified; P1 exit SIGNED by Director. P2 synthesis complete: `expeditions/CE-01/P2_SYNTHESIS.md`, architecture sketch `systems/csir0_architecture.md` (CSIR/0), hypotheses H1–H5 registered, measurement plan `benchmarks/MEASUREMENT_PLAN.md` (use §1.4 formulas ONLY for any computed figures — §1.9's example has known arithmetic slips, see Director's log). Budget: 23.5h remaining of 40; E1 allocation 9.0h.

## Your Task — pre-registration document ONLY, no execution

Produce `experiments/E1_PRE_REGISTRATION.md` with:

### 1. Frozen relation labels & task families
Select 2–3 concrete task families from MEASUREMENT_PLAN's provisional list, including at least one adversarial predicted-loss family. Specify 3–5 concrete tasks per family (real content, not placeholders).

### 2. Arms & conditions
Per MEASUREMENT_PLAN: strong NL baseline arm, CSIR/0 arm (+ converter), schema-amortization sub-conditions at N∈{1,10,25,100}, optional oracle decomposition sub-condition. State what each arm receives, byte-for-byte category counts expected.

### 3. Metrics & predicted outcomes
For each arm×family: primary metric from the plan (net-of-overhead cost + fidelity F0–F3), directional prediction per registered hypothesis (H1/H3 especially), effect size you consider detectable given CE-01's power ceiling, and the falsification condition that would count against each prediction.

### 4. Protocol discipline
Stopping rules; seeds/model versions to pin; converter-fidelity (F2/K_err) as first-class measurement; symmetric treatment of NL arms' fixed blocks; explicit statement that no test-set tuning occurs before unblinding.

## Hard prohibitions
- Do NOT run any model calls or pilot runs.
- Do NOT modify MEASUREMENT_PLAN, REGISTRY, or ledger files — propose edits in an appendix section if needed.
- No placeholder text. If a decision can't be made now, write "DECISION NEEDED: <question>" explicitly.

End with: hours_spent (honest), files_written + line counts, decisions_deferred list.
