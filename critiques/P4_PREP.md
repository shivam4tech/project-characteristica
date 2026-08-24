# P4_PREP.md — Pre-P4 Red-Team & Verification Protocol

Project Characteristica · CE-01 · prepared 2026-08-25 (IST)

Purpose: written BEFORE inspecting P4 result files so acceptance criteria cannot
drift toward whatever the data shows. Scope: E1 (4 arms × 3 families × 50 items),
metrics per MEASUREMENT_PLAN §1.4 (V/F/K/R token classes, amortization
N ∈ {1,10,25,100}) + fidelity F0–F3; temp=0; fixed seeds; Amendment-2 re-pin to
stealth/ox-alpha (~90 glm-5.2 pilot cells quarantined by mtime cutoff
2026-08-25 00:35 IST); converter=executor same model (D-4); oracle column
omitted (D-1).

## 1 Design-stage red-team checklist

Each §9 item gets one specific, testable objection or an explicit N/A with
reason. "Testable" = a concrete check a reviewer can run on design docs,
raw cells, or recomputation.

**S1.1 Semantic loss.**
Objection: the NL→CSIR→SIR→converter path can silently drop entities,
attributes, or constraints; the converter may paper over gaps instead of
failing loudly.
Test: sample ≥20 converted inputs per family; diff converter output against
the NL source for named-entity and constraint counts. If ≥10% of items in any
family lose an entity/constraint, semantic-loss is a live confound. Cross-check
against fidelity F0–F3 rates — fidelity should predict loss; fidelity high +
loss found = fidelity metric itself is broken.

**S1.2 Unfair baselines.**
Objection: CSIR arm may have absorbed more prompt-engineering effort than the
NL baselines, making the comparison effort-confounded rather than
representation-driven.
Test: require documented tuning-iteration parity (NL-opt must receive at least
as many optimization rounds as the CSIR arm); spot-check the 10 worst NL-opt
failures for trivially fixable prompt defects. Undocumented asymmetry ⇒ flag.

**S1.3 Hidden overhead.**
Objection: D-4 makes the CSIR arm's true cost include converter tokens
(V/F/K/R of every conversion pass). If converter cost is booked outside §1.4,
the headline "net-of-overhead" claim is false advertising.
Test: recompute CSIR-arm costs folding converter tokens into K/R classes;
check whether reported net benefit flips sign at any N ∈ {1,10,25,100}. A flip
that the report hides ⇒ reject cost claims.

**S1.4 Leakage.**
Objection: TU adversarial items may leak gold answers or tool behavior into
prompts; D-1 omitted the oracle column but residue may persist elsewhere.
Test: grep all raw prompt fields for gold-answer substrings and any oracle
column remnants; zero tolerance in every arm. Any hit invalidates that family.

**S1.5 Overfitting.**
Objection: the same team/model designed, piloted, and evaluated on the 50-item
sets; items may have been shaped around known model weaknesses.
Test: compare item IDs used by the ~90 quarantined glm-5.2 pilot cells (mtime
cutoff 2026-08-25 00:35 IST) against final eval item IDs. Any overlap between
pilot-informed selection and the eval set requires explicit holdout argument;
silent reuse ⇒ overfitting objection stands.

**S1.6 Model-dependence (P8).**
N/A as an internal-validity objection *because* Amendment-2 re-pinned all
reported cells to stealth/ox-alpha and quarantined glm-5.2 pilot data;
internal validity is protected by construction. Residual issue is external:
all conclusions are single-model and P4 text must scope claims accordingly
(checked as wording gate G6/§4, not as a test).

**S1.7 Prior art.**
Deferred to §3 stubs (CC1–CC3 closest systems, searches, kill-criteria).

**S1.8 Scalability.**
Objection: amortization N ∈ {1,10,25,100} is asserted, not measured; break-even
N* may be fragile to schema growth.
Test: sensitivity check — scale SIR/schema size ×3 on a sample and see whether
N* moves by ~an order of magnitude. If break-even exists only below realistic
task-mix N for the deployment story, the scalability objection stands and CC2
must be scoped down.

**S1.9 Expressiveness limits.**
Objection: SIR may not natively represent constraint types appearing in CP
(or structures in EX/TU), forcing lossy workarounds.
Test: inventory constraint types across the 50 CP items; classify each as
SIR-native vs workaround-encoded. >20% workaround share ⇒ expressiveness-limit
caveat mandatory in P4 conclusions.

**S1.10 Misleading metrics.**
Objection: net-of-overhead cost alone misleads when arms sit at different
fidelity tiers, and any cost figure cherry-picks its most favorable N.
Test: verify every cost figure in P4 is paired with its F0–F3 distribution;
reject cross-arm cost comparisons at unequal fidelity; reject any metric quoted
at only one N when the sign of the result varies across {1,10,25,100}.

## 2 Results verification protocol

Independent recomputation plan. Do NOT trust stored aggregates; rebuild from
raw detail fields + gold. Log every recomputation (per-cell diff) in a scratch
ledger beside this file before rendering any verdict.

**S2.1 Cell sampling (≥10 required).**
Pick 12 cells: one per arm×family combination (4 arms × 3 families = 12),
guaranteeing full strata coverage, plus 3 reserves: highest-cost cell,
lowest-cost cell, and one cell whose mtime sits nearest the quarantine cutoff.
15 total ≥ 10 required. If any sampled cell lacks raw detail files → immediate
fabrication signal (see S2.3) and resample replacement within same stratum.

**S2.2 Recompute scores.**
For each sampled cell: load raw detail record + gold; recompute the family's
score from detail fields (attempt-by-attempt where applicable) independently of
any stored score column. Stored vs recomputed mismatch beyond rounding (>0.5%)
⇒ error signal; systematic direction (always favoring CSIR arm) ⇒ escalate to
full audit of that arm.

**S2.3 Recompute §1.4 costs.**
From raw v/f/k/r token-class fields per cell, recompute net-of-overhead cost at
N ∈ {1,10,25,100} exactly as MEASUREMENT_PLAN §1.4 specifies (including
converter-side tokens for the CSIR arm per D-4). Compare against reported
tables; tolerance = rounding only. Also recompute N* (break-even) from the
recomputed curves; if reported N* disagrees with recomputed N*, cost section is
rejected regardless of direction.

**S2.4 Fabrication signals (any hit ⇒ escalate to full audit).**
- identical latencies across cells, especially across different-length outputs
  (temp=0 explains equal outputs across repeats, never equal wall-times)
- scores exactly matching gold without recorded attempts/steps
- missing raw files for claimed table rows (row exists in aggregate, no payload)
- v/f/k/r fields absent, zero, or null while totals are claimed
- token counts identical across items with visibly different output lengths
- byte-identical detail payloads attributed to different items
- cell mtimes before 2026-08-25 00:35 IST on runs claimed as stealth/ox-alpha
  (quarantine violation — glm-5.2 residue per Amendment-2)
- aggregate statistics irreconcilable with recomputed cell values beyond
  rounding

**S2.5 TU-not-softened check.**
Pull prediction P6 wording verbatim from pre-registration. Compare each
reported TU verdict against P6: classification labels, severity language, and
counts must match verbatim or via explicitly registered mapping. Any rewording
that downgrades severity (e.g., "adversarial predicted-loss confirmed" →
"some deviations observed"), re-bases the comparator post hoc, or converts a
failed adversarial prediction into a partial-pass ⇒ softening ⇒ gate G5 trips
(§4). This check runs on ALL TU verdicts, not just sampled cells.

## 3 Prior-art challenge stubs

For each candidate contribution from P2 synthesis: closest systems, what to
search, and the kill-criteria that would demote the claim. Run these searches
during P4 review, not before results are trusted.

**S3.1 CC1 — "CSIR/0 guide-rail effect": structured form shifts failures from
silent-wrong to detected.**
- Closest systems: schema-constrained decoding (Synchromesh/CSG, Outlines,
  Guidance), OpenAI/Anthropic JSON-mode + validator layers, function-calling
  retry/validation loops, grammar-constrained generation literature.
- What to search: "schema-constrained decoding"; "structured output LLM error
  detection"; "JSON mode validation failure rates"; "constrained decoding
  silent failure reduction".
- Kill-criteria: prior work already quantifies structured-form shifting
  silent-wrong → detected failures ⇒ CC1 demotes from contribution to
  confirmation. Survives only if the mechanism is shown to be the SIR layer's
  semantics (not surface-grammar constraints), with a measurable difference vs
  plain schema/JSON arms — i.e., the JSON-schema arm is itself the critical
  control; CC1 dies if CSIR ≈ JSON-schema on detected-vs-silent split.

**S3.2 CC2 — reuse-gated net benefit N* break-even for representation
schemas.**
- Closest systems: prompt-compression amortization studies (LLMLingua et al.),
  few-shot exemplar/schema caching, KV-cache & template-cache reuse economics
  in serving stacks.
- What to search: "amortized prompt overhead break-even"; "prompt compression
  cost amortization N uses"; "schema caching LLM cost"; "representation
  switching cost language model".
- Kill-criteria: an existing published N*-style break-even formalism for
  representation-schema overhead ⇒ CC2 becomes arithmetic on a known frame.
  Survives only if the reuse-gating structure (per-item conversion cost paid
  per use vs reusable schema asset amortized across N) is itself novel, or if
  measured N* values for this regime are absent from the literature.

**S3.3 CC3 — unoccupied SIR layer between NL prompting and compiler IRs.**
- Closest systems: AMR / PMB semantic banks, UNL interlingua,
  Penman/DMR, abstract dialog-act intermediates, Lingenic SSRN 6291378
  (notation-only, no empirical system).
- What to search: "interlingua as LLM intermediate representation"; "AMR
  prompting large language models"; "UNL interlingua neural"; "semantic
  intermediate representation LLM planning compilation"; "human-readable IR
  prompt format".
- Kill-criteria: any documented system using a human-readable interlingua as
  the working format between NL prompts and compiler-style IRs WITH empirical
  LLM evaluation ⇒ occupancy claim false. Notation-only precedents (SSRN
  6291378) weaken novelty but don't kill it unless paired with evaluation;
  CC3 must then be reworded from "unoccupied" to "first evaluated", which is a
  weaker claim P4 must not paper over.

## 4 Go/no-go gates for P4

REJECT all P4 results if ANY gate trips. No partial acceptance — results stand
or fall together.

- **G1 Coverage:** <80% cells complete per arm×family block (<40/50 items in
  any of the 12 blocks) ⇒ REJECT.
- **G2 Arm presence:** any arm missing entirely ⇒ REJECT.
- **G3 Fidelity integrity:** fidelity-gate structural failures unexplained
  (F0–F3 structural failures without registered cause) ⇒ REJECT.
- **G4 Deviation discipline:** unregistered deviations beyond DEVIATIONS.md +
  Amendments 1–2 ⇒ REJECT.
- **G5 TU wording:** TU verdict softened vs pre-registration wording (per
  §2.5 verbatim check against P6) ⇒ REJECT.
- **G6 Quarantine compliance** (Amendment-2): any reported cell attributed to
  stealth/ox-alpha with mtime before cutoff 2026-08-25 00:35 IST (glm-5.2
  residue) ⇒ REJECT.
- **G7 Converter accounting** (D-4): CSIR-arm costs computed without
  executor-side converter V/F/K/R tokens ⇒ REJECT cost claims (and headline
  benefit claims that depend on them).
- **G8 Oracle residue** (D-1): any prompt/detail payload referencing omitted
  oracle-column contents ⇒ REJECT affected family; whole E1 if leakage spans
  arms.

Verdict format: ACCEPT / REJECT + gate IDs + evidence pointers (file paths,
cell IDs, diff lines from the §2 ledger).

## Reviewer checklist

- [ ] §1 objections each mapped to a concrete §2 test or explicitly N/A'd
- [ ] 12 stratified cells (+3 reserves) recomputed: scores AND §1.4 costs
- [ ] Recomputed N* compared against reported N*
- [ ] Fabrication-signal sweep (§2.4) run over ALL claimed rows, not only samples
- [ ] Every cell mtime checked against quarantine cutoff 2026-08-25 00:35 IST
- [ ] TU verdicts compared VERBATIM against prediction P6 wording (all cells)
- [ ] Gates G1–G8 each evaluated; verdict recorded with evidence pointers
- [ ] CC1–CC3 prior-art searches executed; kill-criteria assessed and logged
- [ ] No headline metric quoted without its F0–F3 pairing or at cherry-picked N
- [ ] Single-model scope (stealth/ox-alpha only) stated in P4 conclusions
