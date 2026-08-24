# E1 Pre-Registration — Efficiency/Fidelity Pilot (CE-01 / P3)

**Author:** Experimental Engineering Lead (ORGANIZATION.md §11), bounded engagement ≤2.0 agent-hours, 2026-08-24 ~16:10 IST.
**Status:** PRE-REGISTRATION. Binding on all E1 execution once countersigned by the Research Director. No model call may be made before the §9 pre-run gates pass and the countersignature exists. This document instantiates `benchmarks/MEASUREMENT_PLAN.md` unchanged and freezes the CSIR/0 E1 profile (`systems/csir0_architecture.md` open debts #2 and parts of #1/#3).
**Inputs honored:** MEASUREMENT_PLAN §§1–5 (measurement skeleton, binding); BENCHMARK_DESIGN §§1–5 (arms, fairness, record); hypotheses/REGISTRY.md H1/H0/H2/H3/H4 (H5 deferred to E2, see D-3); systems/csir0_architecture.md §9 predictions P1–P8 (transcribed with numbers in §6); expeditions/CE-01/P2_SYNTHESIS.md §5 row 6 (**all computed figures below derive from §1.4 formulas directly; the §1.9 worked example is quarantined as illustrative-only** — its known arithmetic slips are not propagated anywhere in this document).

---

## 1. Hypothesis links

| Hypothesis | Role in E1 | Where tested |
|---|---|---|
| H1 (central) | Primary discriminator | §7 H1-support gate, all 3 families |
| H0 (null) | Standing rival; verdict language per §4.5 power ceiling | Same data, opposite reading |
| H2 (variance) | Secondary endpoint, CP family only | §6.2 variance module |
| H3 (reuse-gated benefit) | Primary efficiency axis | §6 Δ(N) curves, N ∈ {1,10,25,100} |
| H4 (silent-error shift) | Secondary endpoint, all families | §6 silent-error fraction |
| H5 (paraphrase robustness) | **NOT TESTED IN E1** (deferred to E2; decision D-3) | — |

## 2. Task families and item banks (FROZEN)

Three families selected per MEASUREMENT_PLAN §4.2 and endorsed unchanged by csir0_architecture.md §9 consistency check: **EX** (extraction — mechanism-favored), **CP** (constraint satisfaction/planning — compositionality/variance stress), **TU** (tool use — adversarial, SIR predicted to lose). Selection rule satisfied: two mechanism-favored families + one predicted-loss family.

Each family = 5 task templates × 10 parametric instantiations = **50 items** (MEASUREMENT_PLAN §4.5 recommends ≥50/cell; 4 arms × 50 items × 3 families = 600 primary executor runs). One fully worked instance per template is reproduced below as real content. Remaining instantiations are rendered pre-run by a frozen generator script (seed 20260824, Python `random.Random(20260824)`; slot pools and ranges specified per template; CP draws are brute-force satisfiability-checked at build time and rejected+redrawn if unsatisfiable). Item bank, gold answers, and checkers are produced by one script from a single source of truth, guaranteeing checker↔gold consistency. **No item text is authored by any LLM** (leakage/bias guard).

All items carry the header `Today is 2026-08-24 (Monday).` where date resolution is needed.

### 2.1 Family EX — extraction from messy text

Checker: programmatic field-by-field comparison after typed normalization (dates→ISO-8601, amounts→(value, currency/unit) pairs, enums lowercased). Item score = matched fields / gold fields (micro). Content-unit types exercised are annotated formally in gate W0b; design coverage stated per template.

- **EX-01 Meeting actions** (units: `entity_ref`, `temporal_qualifier`, `priority/preference`, `exclusion`, `modality`, conditional constraint)
  Source: `"Marta: the beta launch slipped again. Priya, you own the load-test rerun before Thursday. Someone must tell the client — but do NOT promise a date in that note. Sam drafts the migration plan next week, low urgency. Nobody touches the staging cluster until Priya's tests pass."`
  Gold: actions=[{owner:Priya, act:rerun load tests, deadline:<Thursday date>, priority:high(unstated→null)}, {owner:null(unassigned), act:tell client, constraint:no-date-promise(exclusion)}, {owner:Sam, act:draft migration plan, deadline:+7d window, priority:low}], guard={target:staging cluster, condition:priya-tests-pass, type:negated-modification}.
- **EX-02 Incident report** (units: `entity_ref`, `quantity+unit`, `temporal_qualifier`, `exclusion`, exception-of-exclusion)
  Source: `"PagerDuty #4412 opened 2026-08-14 09:12 UTC: checkout-service returning 502s for ~8% of EU traffic since 08:55 UTC. On-call J. Okafor rolled back deploy 2026-08-13.7 at 09:31 UTC; error rate at baseline by 09:40 UTC. Suspected cause: uncached config reload in gateway v2.4.1. Status page updated 09:20 UTC. No enterprise email required per runbook §4 — except the account manager for Nordika GmbH must be notified directly."`
  Gold: id, service, symptom, t_open, blast{region:EU, share:0.08±tolerance}, rollback{deploy_id, t}, suspected_cause, comms{status_page_t, enterprise_email:false(exception:Nordika AM:true)}.
- **EX-03 Lease clause** (units: `quantity+unit`, `temporal_qualifier`, `negation`, `modality`)
  Source: `"Tenant shall remit rent on the first day of each month. Late payments incur a $45 fee after a five-day grace period. Tenant may not paint, sublet, or keep pets exceeding 20 kg without written consent. Landlord must give 24 hours' notice before entry, except in emergencies."`
  Gold: obligations=[rent monthly day-1], fees=[{amount:45 USD, trigger:>5 days late}], prohibitions=[paint, sublet, pets>20kg](consent-escape), notice=[24h, exception:emergency].
- **EX-04 Shipment consolidation** (units: `quantity+unit` ×many, conditional rule, `exclusion`, temporal resolution)
  Source (3 messages): `(1) Dana, warehouse: "Order #8841 ships Monday 2026-08-24. Contents: 12 crates of tile at 240 kg each, one pallet of grout, 380 kg. Do not stack pallets." (2) Marco, freight: "Carrier pickup window 10:00–12:00 local. If customs docs are not filed by Friday 2026-08-21 17:00 UTC, roll the shipment to Monday 2026-08-31." (3) Dana: "Customs invoice filed 2026-08-19."`
  Gold: ship_date=2026-08-24 (docs 08-19 < deadline 08-21 → condition NOT triggered), pickup_window, cargo=[{tile,12 crates,240 kg ea},{grout,1 pallet,380 kg}], handling_exclusion=no pallet stacking, conditional_rule recorded.
- **EX-05 Ticket triage** (units: `entity_ref`, conditional symptom, `priority/preference` (soft), designed unknown-flag probe)
  Source: `"Subject: Cannot export invoices. Since upgrading to v3.2.1 last week, Export spins forever on invoices over ~50 pages. Enterprise plan, ~200 seats. This blocks our month-end close, due on the 28th. Tried clearing cache and switching from Safari to Chrome. Please treat as urgent — our CEO is asking."`
  Gold: category=export-bug, version=3.2.1, symptom_condition=pages>50, tier=Enterprise, seats≈200, deadline=day-28(month UNSPECIFIED → gold marks unknown; correct behavior for machine arms = unknown/clarify flag, for NL arms = noting the gap), mitigations_tried=[cache, browser], priority=urgent+exec-visible(soft).

Instantiation pools: person names (20-pool), products/services (12-pool), percentages 2–15%, weights 50–800 kg, fees $20–$200, versions vN.M.K, day-of-month 1–28, ISO dates within 2026-08/09.

### 2.2 Family CP — constraint satisfaction / planning

Checker: programmatic constraint evaluator over the emitted plan/assignment/schedule. Item F1 = satisfied constraints / total constraints; **item success gate = zero hard-constraint violations** (soft ratio reported separately). Many-valid-plan design: gold = the frozen constraint set, never a unique solution.

- **CP-01 Room-day scheduling** (hard: capacity, equipment, precedence, blackout, availability; soft: quiet-room preference)
  Instance: Rooms: Atlas(cap 10), Borel(cap 4), Cyrus(cap 8, projector). Grid 09:00–17:00, 30-min slots. (a) Sprint review, 8 ppl, projector, 90 min; organizer unavailable 15 min before it (prep buffer). (b) 1:1 Maya/Sam, 30 min, neither available 09:00–11:00. (c) Vendor call, 3 ppl, quiet room preferred (soft). (d) Incident retro, 6 ppl, must start after (a) ends. Lunch 12:00–13:00 blacked out.
- **CP-02 Skill/workload allocation** (hard: skills, caps, coverage, precedence; soft: RANKED preference list — `preference_order` stress)
  Instance: Tickets T1(python,3) T2(python+sql,5) T3(sql,2) T4(rust,8) T5(any,1). Engineers Ana(python,sql,cap 6), Ben(rust,python,cap 9), Chao(sql,rust,cap 5). T4 → Ben or Chao only. Every ticket assigned; caps hold; T1 completes before T3 starts. Preferences, lexicographically ordered: 1) T2 early in week, 2) even load balance, 3) minimize per-person context switches.
- **CP-03 Release checklist** (conditional gates, retry bound, exclusion, dependency DAG)
  Instance: Cut release branch after merge-window PRs land. Migration dry-run on staging snapshot must precede tagging. Tag v2.7.0 only if dry-run clean; otherwise fix forward and retry dry-run once (maximum one retry). Publish notes after tag. Do NOT announce publicly before the support playbook is updated. Legal sign-off needed only if the changelog mentions pricing (current draft does not).
- **CP-04 Round-table seating** (universal quantification, adjacency exclusions)
  Instance: 8 guests A–H, fixed host at seat 1. Hard: A not adjacent to B; C not adjacent to D; E adjacent to F. Soft: G prefers not beside H. Constraint: every guest seated exactly once (scope_marker stress). Output: one arrangement + the checker verifies all constraints.
- **CP-05 Budget allocation** (floors/caps, sum conservation, ranked preferences, veto)
  Instance: Allocate €12,000 across infra/tooling/training/events. Hard: infra ≥ €4,000; training ≤ 25% of total; events+tooling ≤ €5,000 combined; sum exactly €12,000; no single line > €6,000 (lead veto). Soft, ranked: training ≥ €1,500 beats extra-events headroom beats infra headroom.

Instantiation: capacities ±2, points 1–8, budgets €8k–€20k, guest counts 6–10 (with isomorphic relabeling), constraint counts held at template cardinality.

### 2.3 Family TU — tool use (ADVERSARIAL: SIR predicted to lose here)

Mock registry frozen below (six tools, overlapping domains so selection is non-trivial). Fully programmatic scoring: emitted action sequence vs gold action sequence (tool id + normalized args + order); clarification-success where gold = CLARIFY. Registry deliberately contains **no refund capability** and **no board-alias address** to create genuine capability gaps.

```
calendar.book(room_id, date, start_min, end_min, attendee_count, needs_projector: bool)
mail.send(to: [], cc: [], subject, body, priority ∈ {low, normal, high})
tracker.create(title, severity ∈ {S1,S2,S3,S4}, component, assignee, due_date)
tracker.update(ticket_id, status, comment)
orders.lookup(customer_email?, order_id?, status_filter?, placed_after?)
orders.cancel(order_id, reason)
```

- **TU-01 Control, single call:** `"Book the Atlas room tomorrow 14:00–15:00 for 8 people; projector needed."` Gold: calendar.book(atlas, 2026-08-25, 840, 900, 8, true).
- **TU-02 Sequenced pair:** `"File an S2 tracker ticket titled 'nightly export failing', component pipelines, assignee priya, due Friday. Then email ops@corp.example about it — subject 'nightly export S2', reference the ticket id, high priority."` Gold: tracker.create(...) THEN mail.send(..., references ticket_id from step 1) — ordering asserted.
- **TU-03 Underspecified → clarify:** `"Send the quarterly numbers to the board."` Registry has no board alias and no content source → gold = CLARIFY (missing recipient-address and content). Success = any arm's recognized clarification; machine arms via structured CLARIFY object, NL arms via frozen clarify-detector on prose. Asking-is-scoring-symmetric by construction.
- **TU-04 Capability gap:** `"Cancel order #8841 and issue a refund to the original card."` Gold = orders.cancel(8841, reason) + explicit refund-unavailable signal; hallucinated refund/refund-tool call = automatic item failure.
- **TU-05 Filtered multi-step:** `"Look up orders for gunnar@example.com placed after 2026-06-01 still in 'processing', and cancel the oldest one."` Gold: orders.lookup(customer_email, status_filter=processing, placed_after=2026-06-01) → orders.cancel(argmin placement date).

Instantiation: emails/names/ticket titles/order ids from pools; anchor date fixed at 2026-08-24 for all items.

### 2.4 What E1 does NOT contain

No paraphrase variants (H5/E2, D-3); no second model family unless D-2 rules otherwise; no long-document family; no human-authored-SIR production condition inside the confirmatory arms (oracle sub-condition is diagnostic only, §3.3). Cross-task representation reuse (BENCHMARK_DESIGN §3 "cross-task generalization") is partially earned: the SAME frozen CSIR/0 profile (§4) and the SAME converter prompt serve all three families with zero redesign — this is registered as an observed design property, and the manifest logs identical asset hashes across family cells as evidence.

## 3. Arms and conditions

### 3.1 Mandatory arms (BENCHMARK_DESIGN §1 — all four run; no documented exception requested)

Identical across all arms: model id/version, decoding params (primary runs T=0, max_tokens=2048), tools/context, item bytes, scoring layer, retry allowance (≤2 repair re-prompts on parse/validation failure, metered as R). The task *question* ("produce the answer artifact for item k") is arm-neutral; arms differ only in the representation layer between intent and answer.

| Arm | Receives (byte categories) | F-block inventory (authored at W0a; sha256-pinned before first run) |
|---|---|---|
| **NL-plain** | F_NLp + V_in(source text + neutral question) | One short generic instruction paragraph naming the fields/goal in prose, as a competent practitioner would first write it. **Authoring cap ≤120 tok.** No examples, no format contract, no role framing. |
| **NL-optimized** | F_NLo + V_in(same) | Role framing; explicit field/constraint definitions matching the gold schema vocabulary; textual output template; 1 worked example. Engineering effort parity with SIR arm attested in experiment record (fairness rule §4.2). **Cap ≤450 tok.** |
| **JSON/schema** | F_js + V_in(same) | Complete JSON Schema for the answer artifact + validation/repair instructions + 1 worked example. Strict parse; validation failure → repair attempt (R). **Cap ≤700 tok.** |
| **CSIR/0-SIR** | F_conv (converter instructions incl. CSIR/0 profile §4 + 1 worked conversion example) → converter call → validated CSIR/0 document → F_exec (executor/decoder instructions + answer-artifact contract + 1 worked example) → executor call | Converter: T=0, same model as executor (D-4 default). Validation gate per csir0 §3 (schema conformance, referential integrity, span coverage); failure → ≤2 converter repair re-prompts, then item proceeds with validator-reported state (never silently repaired). Executor sees **only** the CSIR/0 document + question — never the raw source text (meaning must ride the representation; this is what makes F2 attribution meaningful). Caps: F_conv ≤1400 tok, F_exec ≤350 tok. |

Answer artifacts (scorer input) are IDENTICAL in target schema across arms: EX = field list; CP = plan/assignment structure; TU = ordered action list or CLARIFY. NL arms emit freeform and are read by one frozen tolerant parser (shared NL-parser, declared now); machine arms strict-parse. Parser failure after retries = F0 fail, counted as failure with full cost retention (MEASUREMENT_PLAN §1.7).

Expected category magnitudes (authoring caps above are binding budgets; measured per-tokenizer counts land in the manifest — these are design constants, not empirical predictions): V_in dominated by source text (identical bytes all arms); V_out comparable across arms (same answer artifact); SIR arm uniquely carries K_tok (converter in+out) and K_time (serial conversion stage); R possible in all arms (parse repairs) and additionally in SIR's converter stage (R_conv).

### 3.2 Amortization sub-conditions (analysis-time, zero extra runs)

Δ(N) computed at **N ∈ {1, 10, 25, 100}** from logged components via §1.4 formulas; primary efficiency endpoints at N ∈ {1, 25} (plan §4.4). Symmetry rule honored: NL arms' reusable blocks (role framing, templates, examples = F_NLp/F_NLo) amortize over the same N. **Earned-vs-projected distinction (binding reporting rule):** F/N amortization is *earned* — the same fixed block genuinely serves all 50 items. Converter-cost amortization at N_conv > 1 is *projected scenario math* (E1's converter runs per item; N_conv=1 is the honest primary). Both charging modes reported per plan §1.2; N_conv ∈ {1, 10}; only N_conv=1 supports confirmatory claims; N_conv=10 curves are labeled PROJECTED wherever printed.

### 3.3 SIR-oracle decomposition sub-condition — CONDITIONAL, decision D-1

Hand-authored CSIR/0 payloads for a 20-item stratified subsample per family, executed through the identical executor path, conversion cost/errors excluded from its totals and reported separately. Purpose: decompose any effect into representation-intrinsic vs pipeline-attributable (MEASUREMENT_PLAN §4.1). **Requires Director ruling** (BENCHMARK_DESIGN §1 fixes four arms; exceptions live in `decisions/`). If disallowed: dropped entirely; a null result will then be reported with the explicit caveat that representation-intrinsic vs converter-attributable causes are not separable in E1 (diagnostic loss acknowledged in FINAL_REPORT). If approved: labeled NON-CONFIRMATORY-DIAGNOSTIC in every table it appears in; proposed decision-record text in Appendix A.

## 4. CSIR/0 E1 profile — FROZEN relation-label set (resolves csir0 open debt #2)

Closed edge vocabulary for E1, seven labels, each with exactly one declared reading (csir0 §3; silent-duality impossible; `intensional` modifier available but defaults unset = extensional, and at E1 no converter prompt teaches it — it stays reserved):

| Label | Domain → Range | Single declared reading |
|---|---|---|
| `hasArg` | predicate → participant | Participant fills an argument slot of the predicate; slots ordered by first appearance in source spans. No thematic-role commitment. |
| `modifies` | {temporal_qualifier, modality, style_constraint, quantity_unit} → head node | Modifier scopes over/attribution-to the head; no truth-functional operator binding beyond the node's own declared semantics. |
| `constrains` | constraint → target node/subgraph | Restricts the admissible states/plans/answers involving target; `polarity` ∈ {hard, soft} carried on the constraint node. |
| `orderedBefore` | event/step → event/step | First must complete/occur before second (partial-order edge; no transitive closure asserted by the edge itself). |
| `excludes` | exclusion node → target | Target content forbidden/negated (negation-as-explicit-exclusion; there is NO term subtraction, csir0 §3). |
| `quantifiesOver` | scope_marker → subgraph root | Marker's `mode` (∃/∀/count-bound) binds the variable set of its scope subgraph; minimal scope-marker formalism per csir0 debt #4. |
| `requestsOutput` | speech_act/output_shape → root | Declares the required output artifact shape for consumers; declarative only, no execution semantics. |

Tier-A element usage per family: EX emphasizes `entity_ref/quantity_unit/temporal_qualifier/exclusion/modality`; CP emphasizes `constraint/preference_order/orderedBefore/scope_marker`; TU emphasizes `speech_act/output_shape/predicate(entity=tool)/hasArg/orderedBefore`. Depth ≤3 enforced by validator (csir0 §3). Well-formedness gate = the three csir0 checks; ambiguity policy = branch-or-`unknown_flag`, silent selection prohibited (validator-rejected); EX-05's unspecified month and TU-03 are designed probes of exactly this policy. **Serialization: the csir0 §7 JSON shape, non-normative instance data promoted to the working serialization for E1 as-is** — no compact-syntax work permitted pre-data (csir0 debt #1, C-012 gaming resistance). Converter prompt teaches: Tier-A types, the seven labels with their readings, lexicon-block rules, span citation requirement, unknown_flag/branch policy, one worked example.

## 5. Endpoints and metrics

Primary effectiveness: **F0-gated F1 success rate** per arm×family cell. Primary efficiency: **amortized end-to-end $ per dispatched task** at N∈{1,25} (N_conv=1), plus p95 latency end-to-end (SIR includes conversion). Full Δ(N) curve at N∈{1,10,25,100} reported for every family regardless of significance (H3 object). Secondary/diagnostic: raw token splits V/F/R(+R_conv), K_err, p50 latency, F2 conversion-vs-behavioral fidelity gap, F3 round-trip stability, silent-error fraction, variance module (CP only).

All dollar figures from §1.4 formulas with the price vector + retrieval date + source URL recorded in the manifest at run time (prices drift; vectors are never compared across dates). Cross-model claims, if any arise, use $/task and chars/task only — raw tokens stay diagnostics (C-012). Fidelity non-inferiority margins for the H1 gate: **δ_F1 = 3 points (EX, TU), 4 points (CP)** — tighter than the plan's 5-point default because all three checkers are fully programmatic (no judge noise); CP gets +1 for soft-constraint weighting sensitivity. **No LLM judges exist anywhere in E1** — every family is programmatically scorable by design, eliminating judge-bias machinery (plan §3.3) from this experiment.

F3 threshold (fixes csir0 P7's open value): **δ_F3 = 0.90** canonical round-trip equality rate on non-unknown nodes, aggregated over all SIR documents; failures tabulated by node kind with the prediction they concentrate at unknown-flagged/branch nodes.

## 6. Predicted outcomes per arm × family (registered before any run)

Signs: `>` / `<` / `≈` vs the stated comparator; "detectable" = beyond the §4.5 power ceiling (paired, n=50: only effects ≳15–20 F1 points or correspondingly large $ deltas are interpretable; smaller true effects are invisible at CE-01 scale and verdict language says "no detectable advantage," never "no advantage").

### 6.1 Directional predictions

| Cell | F1 success | $ @ N=1 | $ @ N=25 | Latency (p95) | Basis |
|---|---|---|---|---|---|
| EX: SIR vs strongest NL arm | `>` **iff** measured conversion-stage F2 ≥ 0.90; else `≈` or `<` | `<` | `>` iff F2 ≥ 0.90 (P1) | `>` (serial conversion) | H1, H3, P1 |
| EX: SIR vs JSON arm | `≈` (no predicted advantage; JSON captures structuring) | `<` | `≈` | `>` | C-009, H1 competing explanation |
| CP: SIR vs NL arms | `≈` mean, variance ↓ (module §6.2) | `<` | `≈`/weak `>` | `>` | H2, P4 |
| CP: SIR vs JSON | `≈`; silent-error ↓ predicted (sole predicted SIR-over-JSON edge) | `<` | `≈` | `>` | H4, P5 |
| TU: SIR vs JSON | **`<` — registered adversarial loss** (P6); contrary result triggers mandatory red-team review before any claim | `<` | `<` (schema-native territory; SIR pays conversion for nothing) | `>` | C-008/C-009, P6 |
| TU: SIR vs NL-opt | `≈` (NL-opt with explicit contract is competitive) | `<` | `≈` | `>` | H1 scope |
| All: NL-plain | weakest or equal F1; cheapest F; highest parser-failure rate | lowest $ | lowest $ | `≈` lowest | straw-man guard: reported, never compared-against alone |

### 6.2 Hypothesis-level predictions, detectable-effect statements, and falsification conditions

- **H3 (primary efficiency axis):** Predicted: Δ(N=1) ≤ 0 in ALL families (single-use never pays); Δ(N=25) > 0 in EX **iff** conversion-stage F2 ≥ 0.90; monotone improvement in N. Detectable: $ deltas ≥ ~25% of the NL-opt arm's per-task cost at n=50. Falsification (registry H3): (a) Δ(N) ≤ 0 at every declared N, or (b) Δ(1) > 0, or (c) no significant N×arm interaction — any of these falsifies H3 as registered.
- **UNL-replay guard (P2):** if conversion-stage F2 < 0.80 on EX, predicted Δ(N) < 0 at every N; registered NOW so the failure, if observed, is diagnostic (localizes the wall at conversion economics, C-007) rather than surprising.
- **Conversion-loss localization (P3):** predicted F2 conversion-stage unit losses concentrate in `modality`, `preference_order`, `exclusion` — NOT in `entity_ref`/`quantity_unit`. Test: per-unit-type recovery rates from the F2 audit (≥20% stratified sample per cell, §3.2). Falsified if loss concentrates in the "easy" unit classes instead.
- **H1 (central):** support in a family requires ALL FOUR plan §4.4 conditions: (1) SIR beats the **strongest** baseline arm (highest F1 among the three baselines, determined per family from data — comparator rule fixed in advance) on $/task with paired-bootstrap 95% CI excluding zero; (2) F1 non-inferiority within δ_F1; (3) replication (§8); (4) red-team survival (P4 phase). Any failure ⇒ no H1 support from that family. H0 stands unless ≥1 family passes all four.
- **H4 / silent-error (P5):** predicted: silent-error fraction (validation-passed but F1-failed) SIR < both NL arms in CP; **NO significant SIR-over-JSON silent-error advantage in TU** (JSON already validates — that comparison is the adversarial control separating "structure helps detection" from "primitive-vocabulary guide-rails help detection"). Falsified per registry: reduction absent, fully explained by JSON arm, or bought below δ_F1.
- **H2 / variance (P4, CP module only):** predicted SIR run-to-run dispersion < both NL arms at comparable mean F1; **partial survival required vs JSON arm** — if SIR ≈ JSON dispersion, the effect is attributed to generic structuring and H2 is recorded as weakened (registry falsification criterion). Module: 20 stratified CP items × 3 arms (NL-opt, JSON, SIR) × 5 repetitions @ T=0.7, seeds {101,…,105}; metric: per-item modal-answer agreement rate + outcome entropy. Detectable: agreement-rate gaps ≥ 15 points.
- **F3 (P7):** SIR F3 ≥ 0.90 with failures concentrated at unknown/branch nodes. Falsified if F3 < 0.90 or failures distribute uniformly.
- **Oracle contrast (only if D-1 approved, diagnostic):** hand-authored-SIR cells expected to show the F2-conversion gap recovered; if oracle ≈ converted-SIR, converter quality is exonerated and any deficit is representation-intrinsic.

## 7. Statistical analysis plan

Paired item-level bootstrap (10,000 resamples, seed 20260824), two-sided α=.05, on per-item paired differences (SIR − comparator) for F1 and for $/task at each N. Comparator = strongest baseline arm per family per the fixed rule above; all four arms fully reported regardless (no suppression). Report unconditional (per dispatched task) AND conditional (per successful task) statistics everywhere (§1.7). Results presented as the Pareto plane ($/task vs F1) per family; scalar ratios are never decision statistics. Replication for H1-condition-3: three-fold item-split analysis (sign consistency of the delta across folds) PLUS a stochastic-replication module — 10 stratified items × 3 repetitions @ T=0.7 (seeds 201–203) for SIR vs strongest baseline in EX and TU. Exclusion policy: any excluded run needs written justification in the experiment record + CLAIM_LEDGER flag via Director transcription; nothing drops silently.

## 8. Protocol discipline (binding)

1. **Stopping rule:** fixed-n (50 items × 4 arms × 3 families); NO interim peeking at primary endpoints; no alpha-spending boundary declared (none may be invented later). External-abort (API outage) ⇒ resume from last completed cell, interruption logged; queue anomalies >3× median re-run with both readings kept (§1.5).
2. **Model pinning:** ONE primary model family, exact versioned API id + tokenizer id recorded in the manifest before the first scored call; no mid-experiment model/price-vector switch (a forced switch ⇒ all cells restart). Candidate selection is decision **D-2** (Director, at run time, constrained to: single family, version-dated, stable API). Converter model = executor model, T=0 (D-4 default; a different-family converter would double as a mini-portability probe and is NOT assumed).
3. **Converter fidelity first-class:** conversions.csv per plan §5; K_err and conversion-stage F2 reported as headline results, not footnotes; every conversion error charged end-to-end to the SIR arm; the F2 conversion-vs-behavioral gap is the registered instrument for attributing loss to pipeline stages.
4. **Symmetric NL treatment:** NL arms' fixed blocks split and amortized over the same N (§1.4 symmetry rule); NL-opt receives engineering effort attested equal to the SIR arm's; NL retries metered identically; NL-plain is reported but no claim ever rests on it alone (Protocol §4).
5. **No test-set tuning / unblinding:** checkers, gold answers, δ margins, F3 threshold, comparator rule, and analysis notebook are frozen by this document and the W0 gates. Between first scored call and unblinding: no arm-prompt edits, no threshold moves, no checker changes, no item swaps (item-bank defects discovered mid-run are logged and analyzed as-is; prospective-only fixes noted for E2). **Unblinding = first execution of the analysis notebook on complete results/E1/ files.** The only permitted pre-unblinding model contact is the W0e smoke test: ≤4 calls, logged as smoke, excluded from every statistic by pre-declaration (plumbing check, not data).
6. **Asset integrity:** every F-block, the converter prompt, the item-generator script, and the checker suite are committed under `experiments/e1_assets/` with sha256 hashes recorded in the manifest before the first scored call; any hash mismatch at analysis time voids the affected cell.

## 9. Pre-run gates (all must pass before the first scored API call)

- **W0a** Assets authored + committed + hashed (all F-blocks within §3.1 caps; generator script; checkers).
- **W0b** F2 content-unit annotation from source+gold only, annotator blind to arm structure; unit ids + checker↔unit traceability table complete (plan §3.2).
- **W0c** Item bank rendered (50×3), CP satisfiability guard passed, gold/checker round-trip self-test green (checker(gold)=1.0 on every item).
- **W0d** Manifest initialized: model id/version/date, tokenizer id, price vector + retrieval URL + date, seeds, N/N_conv declarations, asset hashes.
- **W0e** Smoke test ≤4 calls, logged, discarded.
- **W0f** Director countersignature on this document; D-1..D-4 resolved.

## 10. Budget fit

Run-volume estimate: 600 primary executor calls + ~150–450 converter calls (incl. repairs) + 300 (H2 module) + 120 (stochastic replication) + ≤4 smoke ≈ **≤1,475 calls**, well within typical pilot spend; the binding resource is P3 agent-hours (9.0 allocated; ~1.5–2.0 consumed by this registration ⇒ ~7.0 remain for W0a–W0e asset build + run supervision + analysis). Asset build is the risk line (est. 3.5–4.5 h); if it exceeds 5.0 h, escalate to Director before runs (threshold approach to the 36 h hard-cap warning at 36.0 h cumulative currently at 16.5+2.0=18.5 h — no conflict yet).

## Appendix A — proposed governance edits (NOT applied by this engagement; Director/Curator disposition)

1. `decisions/` entry draft for D-1 (if approved): *"E1 adds a fifth, non-confirmatory diagnostic column (SIR-oracle, hand-authored payloads, 20-item subsample/family, conversion costs excluded and reported separately) per MEASUREMENT_PLAN §4.1; confirmatory claims remain restricted to the four BENCHMARK_DESIGN §1 arms."*
2. MEASUREMENT_PLAN §1.9: recommend a one-line errata pointer ("illustrative arithmetic superseded by §1.4; see P2_SYNTHESIS §5") — editorial only, no formula change (§1.4 is correct and is the sole basis of this registration).
3. OPEN_QUESTIONS.md OQ4/OQ5/OQ8 rows: propose adding "discriminating evidence source: E1 per experiments/E1_PRE_REGISTRATION.md §6" once countersigned (Curator pass).

## Appendix B — decisions requested from Director

- **D-1:** Approve SIR-oracle diagnostic sub-condition as §3.3 specifies? (Default if unanswered: omit; caveat logged in FINAL_REPORT.)
- **D-2:** Pin the primary model family + exact version at run time (constraints in §8.2). Default: cheapest stable frontier-tier API accessible to the lab; single family only.
- **D-3:** Confirm H5/paraphrase stays in E2 (recommended — E1 power is reserved for the registered endpoints). Default: E2.
- **D-4:** Confirm converter model = executor model (recommended for clean K_err attribution). Default: same model.

---

**Engagement accounting (per directive footer):**

- **hours_spent:** 1.5 h (context reconstruction: charter docs, measurement plan, architecture, registries, ledger, protocol, brief; composition of this registration). Within the ≤2.0 h envelope. Coordinator-session overhead excluded. STATUS/WORKERS transcription left to Director per the concurrent-write process rule (STATUS.md session note 2026-08-24).
- **files_written:** `experiments/E1_PRE_REGISTRATION.md` (line count recorded by `wc -l` immediately after this write; single file — no other repo file touched, per hard prohibitions).
- **decisions_deferred:** D-1 (oracle column), D-2 (model pinning), D-3 (paraphrase placement), D-4 (converter identity). No other decision was deferred; every remaining choice is frozen above. Explicitly NOT deferred: relation-label set (frozen §4 — csir0 debt #2 discharged), δ_F1/δ_F3 margins (frozen §5), N/N_conv declarations (frozen §3.2), comparator rule (frozen §7).
