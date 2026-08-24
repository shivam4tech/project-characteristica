# Assessment: Is "human-intent → semantic-IR → model/tool-adapter" a technically meaningful analogy to compiler IR design?

- **Worker:** W18-IR (Compiler / IR Researcher), expedition CE-01
- **Date:** 2026-08-24
- **Inputs read:** WORKER_BRIEF_COMMON.md; LAB_CHARTER.md; RESEARCH_QUESTION.md (working architecture + H1/H0); RESEARCH_PROTOCOL.md §§1–10; agents/ORGANIZATION.md §9
- **Question addressed:** Does compiler/IR engineering provide technically meaningful, *borrowable* mechanisms for the proposed pipeline `Human Intent → Natural Language → Semantic Intermediate Representation (SIR) → Model/Tool Adapter → LLM/Tool`, and where does the analogy break?
- **Status:** FINAL — all sections populated 2026-08-24 (write-as-you-go per brief).

---

## 0. TL;DR verdict (to be finalized after source work)

**VERDICT: Meaningful but partial — copy the *process*, drop the *promise*.** The analogy holds **as engineering discipline**: of eleven mechanisms assessed (§2), typing/validation (M2), provenance diagnostics (M8), adapter abstraction (M9), and test-suite-driven development (M10) transfer cleanly because they need no formal source semantics to pay off. It fails **as a guarantee-bearing translator** on two hard disanalogies (§3): intent has no formal source semantics (D1) hence no definable equivalence relation or correctness spec (D2); CompCert's machine-checked preservation proof [S3] has no statable counterpart here, and AMR evidence shows structural-match metrics passing human-agreement ceilings while still distorting meaning [S7]. Two further findings should steer design: (i) the amortization argument inverts — front-end diversity (user phrasings) is unbounded, so the SIR pays off only as a validated checkpoint contract (cacheable/resumable/auditable/test seam), never as a translation pivot (§4b); (ii) the "compiler layer" is cheap in logic precisely because the LLM absorbs the front end, so its real cost is contract maintenance — ~10–14 engineer-days one-off plus a permanent ~20%-of-velocity golden-suite tax (§4). E1 should implement R1–R10, ban correctness-guarantee language, and refuse any hand-written NL-parsing detour.

## 1. Preconditions that make compiler IR design work (baseline for the comparison)

### 1.1 Eight preconditions that make compiler IR design work

**P1. Formal specification at both ends.** A compiler translates *between* two languages each fixed by a complete grammar and a formal semantics. LLVM IR is a precisely specified, typed, SSA-based language intended as "the common code representation" shared by many front ends [S1]; the machine side is pinned by ISA/ABI specifications. Without both ends pinned there is nothing to translate between — only transformation.

**P2. A definable equivalence relation.** Compiler correctness is even *statable* only because observable behavior is defined: CompCert's guarantee is a machine-checked proof "that the generated executable code behaves exactly as prescribed by the semantics of the source program" [S3]. Equivalence gives every transform a binary oracle.

**P3. Deterministic, total decision points.** Parsing resolves syntactic ambiguity once, mechanically, via the grammar; instruction selection pattern-matches over a finite instruction set through documented phases (SelectionDAG select, scheduling, register allocation) [S2]. Every lowering decision terminates and is repeatable.

**P4. Closed construct sets.** Finite AST node kinds and finite target instruction sets make exhaustive case analysis — and hence machine-checked proof — tractable [S3]. Nothing enters the system without a grammar rule.

**P5. Slow-moving, versioned targets.** ISAs and ABIs evolve over years, and each backend declares which target revision it supports via target-description classes [S2]. Interfaces are stable enough to build against.

**P6. Post-hoc instance checkability.** Even where general proofs are impractical, a *particular* translation is checkable: regression suites, differential testing, and translation validation all exploit the fact that equivalence on an instance is decidable.

**P7. Amortization economics.** One stable IR serves N front ends × M back ends [S1]; this is what repays the multi-year investment in IR design. That the bargain is fragile is shown by MLIR: created (2019) because a single LLVM-level IR could not serve ML/graph workloads, requiring whole new "dialect" machinery [S8] — even the cheap-looking center is expensive to get wrong.

**P8. Locality of reasoning.** Types plus SSA give every rewrite local validity conditions; passes compose because each preserves the same global invariant (source semantics). This is what lets hundreds of engineers add passes without stepping on each other.

### 1.2 Baseline check for the proposed pipeline

Of the eight, the `Intent → SIR → Adapter` pipeline today satisfies **none fully**: P1 fails at the source end (intent has no formal semantics, §3-D1), P2 has no counterpart (no equivalence relation, §3-D2), P3–P4 fail (ambiguity is pervasive and the construct space is open-ended), and P5/P7 hold only analogically (provider APIs are versioned but volatile; front-end diversity — users' phrasings — is unbounded). Any borrow must therefore survive without these supports, which drives the overhead column in §2.

## 2. Mechanism-by-mechanism assessment (borrowables + overhead)

Eleven compiler mechanisms were assessed for borrowability. "Borrow" = adopt the mechanism *as engineering practice* in the CE-01 pipeline; every row carries its overhead because none of the §1 preconditions fully hold here.

| # | Compiler mechanism | Role in compilers | Borrowable analogue for CE-01 | Overhead / limit of the borrow |
|---|---|---|---|---|
| M1 | Tiered representations (LLVM IR → SelectionDAG → MachineInstr → MCInst) [S2] | Staged lossy refinement between well-defined levels | Two tiers at E1: raw utterance+context vs validated plan/call-graph | Each tier needs schema + validator + dump/debug format; tier-mapping docs rot fast. Hard cap at 2 tiers until measured pain |
| M2 | Typed core representation [S1] | Ill-typed programs rejected before anything runs | JSON-Schema-typed tool-call plans; validate before execution | Schema maintenance is permanent; coercion rules ("3" vs 3) must be written down or LLM output drifts; version skew across adapters |
| M3 | SSA / single assignment | Every value defined once; def-use chains explicit | Unique IDs per entity/slot; explicit referent table for coreference | Entity resolution is unsolved at needed scale; merge points (a clarification overriding a slot) need φ-node-like precedence rules made explicit |
| M4 | Canonicalization passes | Collapse equivalent forms to one form to shrink downstream cases | Normalize only uncontroversial slots: dates, units, enums, IDs | Safe ONLY where equivalence is uncontroversial. Paraphrase collapsing is unsafe (§3-D3/D5); keep raw span alongside canonical value |
| M5 | Local guarded rewrites (peephole) | Micro-transformations with local validity predicates | Deterministic post-fixes on LLM output (default-filling, arg reordering), each behind a predicate | Guards themselves need tests; unguarded "helpful" rewrites are the classic silent-corruption source — exactly the UB-style bug class compilers engineer against |
| M6 | Pass manager / composable pipeline [S2] | Ordered, individually testable stages | Middleware chain: validate → enrich → route → execute → verify | Ordering constraints become hidden coupling; once >~5 stages, pass dependencies must be declared explicitly |
| M7 | Cost models guiding transforms [S2] | Choose among *equally correct* implementations (selection, scheduling, regalloc) | Choosing cheaper/faster tools, batching strategy | No correctness dimension to trade: all candidate calls are "correct"; costs ($, latency, tokens) are empirical and drift. Log first, model later |
| M8 | Diagnostics pointing at source spans | Errors cite exact source locations | Every SIR node carries char-spans of the utterance; clarification questions quote the span | Span bookkeeping through every transform; any transform that drops provenance silently kills the clarification UX |
| M9 | Backend abstraction via target-description classes [S2] | One IR, many targets, fixed interfaces | Provider adapters behind one plan IR | Lowest-common-denominator effect; provider-specific extensions leak as "intrinsics" — budget an escape hatch + per-adapter conformance suite |
| M10 | Regression suites / test-suite-driven development | Primary safety net wherever proofs are impractical | Golden-intent suite: utterance → expected adapter call traces, run in CI | Corpus curation is permanent work (~20% of velocity); must cover ambiguity clusters, not just happy paths |
| M11 | Versioned IR evolution / dialects [S8] | MLIR's answer to one-size-fits-all IR failing | semver'd SIR schema; adapters declare a supported range | Needs migration tooling old→new version and a deprecation policy from day one, or stored/cached plans break on every schema bump |

**Assessment.** Highest value-per-cost borrows: **M2, M8, M9, M10** (typing, provenance, adapter abstraction, golden suite) — they deliver compiler-engineering benefits *without* needing P1–P4. Conditional borrows: M1, M4, M6, M11 (useful but each invites over-engineering). Weakest borrows: **M3** (entity/coreference resolution has no reliable mechanical equivalent) and **M7** (no analytic cost model exists for meaning-level choices).

## 3. Disanalogies

Six disanalogies, ordered by severity. D1–D2 break the *translator* reading of the analogy; D3–D5 break the *deterministic-pipeline* reading; D6 is a survivable engineering tax.

**D1. Intent has no formal source semantics.** The strongest known program for formalizing natural-language meaning — Montague semantics — succeeds only by explicitly constructing small fragments with model-theoretic interpretations and a compositionality principle designed into them; it is a property achieved per-fragment, not a discovered property of language [S4]. Everyday intent ("clean this up", "make it faster") is indexical, context-bound, and vague in ways no fragment covers. A compiler front end maps syntax to meaning-bearing structure because meaning is defined on the target side of that map; here nothing downstream of the utterance is defined.

**D2. No equivalence relation → no correctness spec.** CompCert's guarantee is statable because "behaves exactly as prescribed by the semantics of the source program" fixes preservation [S3]. For intent→SIR there is no definition of "same meaning", hence no oracle and no statable correctness claim. The nearest proxies are structural-overlap metrics like smatch [S6] — and Opitz & Frank show parsers scoring *above* estimated human inter-annotator agreement still emit meaning-distorting errors humans rate unacceptable (acceptability as low as 0.58–0.69 on literary text) [S7]. Structural match ≠ meaning preserved. Consequence: any "semantics-preserving normalization" claim about our pipeline is marketing, not engineering.

**D3. Ambiguity is pervasive and often irreducible.** Compilers disambiguate deterministically at parse time or reject the input. Natural language carries lexical, structural, and scope ambiguities where the readings are *genuinely different intentions*, not noise: Montague handles scope ("every man loves a woman") by giving the sentence two distinct derivations — two meanings [S4]. Resolution needs world knowledge or a question to the user; i.e., interaction, which the compiler pipeline structurally lacks.

**D4. The source is not authoritative.** A compiler takes the input program as ground truth. An utterance underdetermines the user's goal: users omit constraints, misremember state, revise mid-sentence. The "front end" cannot be a faithful reader because there is nothing fully determined to be faithful *to*. This is requirements elicitation, not translation — and it means even a perfect SIR captures a *hypothesis about intent*, never intent itself.

**D5. No human-grade agreement even on the target representation.** For AMR — the closest existing artifact to an "SIR" — trained annotators converge only gradually toward consensus, and a dedicated metric (smatch) was needed merely to *measure* their agreement; within the founding IAA study agreement improved over time but required a consensus annotation as reference [S6]; later work treats parser scores at the level of human IAA as a warning sign about measurement validity rather than evidence of solved parsing [S7]. If expert humans cannot reliably produce identical graphs, "the correct SIR for utterance u" does not exist in anything like the compiler sense.

**D6. Open world on both sides.** Compiler universes are closed: fixed ISA, fixed language standard, changes gated by standards bodies. Tool ecosystems, vocabularies, and user phrasings grow continuously and ungated. The SIR must therefore evolve without breaking stored plans — a permanent versioning burden compilers feel only across major releases (cf. MLIR's dialect machinery as the institutional response [S8]).

**Net effect:** D1+D2 kill the guarantee-bearing-translator reading outright; D3+D4+D5 mean the pipeline must be interactive and probabilistic rather than deterministic; D6 is real but manageable with M11-style discipline.

## 4. Where the complexity hides: explicit costing of the "compiler layer"

The "compiler layer" of the proposal = everything between raw utterance and adapter invocation: schema, validation, canonicalization, provenance, repair loop, routing, versioning.

**Two structural observations first.**

**(a) The complexity moved into the LLM.** In a real compiler the front end (parsing messy source into well-formed IR) is a major cost center. Here the LLM *is* the front end; our code never parses language. So our layer is thin in transformation logic but heavy in **contract**: schema definition, validation, provenance bookkeeping, and above all the test corpus that substitutes for the missing oracle (D2).

**(b) The amortization argument inverts.** A compiler IR pays off because N bounded front ends meet M bounded back ends at a stable center (P7). Here front-end diversity is unbounded (every user phrasing), so the SIR cannot pay off as a *translation pivot*. It pays off only as a machine-readable **checkpoint contract**: a cacheable, resumable, auditable, testable seam between fuzzy input and typed execution. Design for checkpoint value, not translation fidelity.

### Cost table (E1-scale estimates, single engineer)

| Component | Compiler analogue | One-off build | Ongoing load | Failure mode if skipped |
|---|---|---|---|---|
| SIR schema + docs + examples | IR spec (LangRef-style) [S1] | 3–5 d | ~0.5 d/mo churn | prompts and adapters silently diverge |
| Validation + bounded repair loop | semantic analysis / error recovery | 2–3 d | low once built | malformed plans reach tools; failures debugged by users |
| Provenance spans on every node | debug info (DWARF-analogue) | 1–2 d | threading discipline everywhere | clarifications can't cite text; debugging blind |
| Golden-intent suite in CI | regression suites / test-driven dev | 2–3 d + authoring 50–100 cases | **~20% of velocity, permanently** | regressions ship invisibly; refactoring freezes |
| Adapter conformance suite | backend test suites | ~1 d per adapter | per provider API change | provider drift breaks production quietly |
| Schema versioning policy + migrations | ABI stability / deprecation policy | 0.5–1 d | per schema bump | cached/stored plans unusable after each change |
| Cost/routing model | codegen cost models [S2] | deferred — log-only first | trivial logging infra | premature routing optimizes guesses |

One-off total ≈ **10–14 engineer-days** plus corpus authorship; steady-state load ≈ **15–25% of team velocity**, dominated by test-corpus curation rather than code. 

**Calibration from compiler history:** even the "cheap stable center" took years — LLVM IR has evolved since the early 2000s [S1], and MLIR was founded (~2019) specifically because one IR could not serve new domains, requiring dialect machinery as the fix [S8]. Expect breaking SIR-schema changes in the first six months regardless of design care; budget semver + migrations now (M11). 

**Explicit warning:** if anyone proposes replacing the LLM front end with hand-written NL parsing rules ("just grammar it"), the cost profile flips to full-parser economics — permanent grammar maintenance against an unbounded phrasing long tail, with worse coverage than the LLM. Refuse that path; the LLM-as-unreliable-front-end + validated-checkpoint architecture is precisely what keeps our compiler layer affordable.

## 5. Recommendations to CE-01

Ten recommendations for E1 design, each traceable to §2/§3/§4. Ordered roughly by priority.

**R1. Make the SIR a validated checkpoint contract, not a translation target.** JSON-Schema-validate every LLM-emitted plan before anything executes (M2). On validation failure run a bounded repair loop: ≤2 re-prompt attempts, then surface a targeted clarification to the user. This is parser error-recovery posture applied to an unreliable front end. *(Addresses D4, costs in §4.)*

**R2. Replace the impossible oracle with a task-level golden suite.** Since semantic equivalence is undefinable (D2), define acceptance operationally: N golden utterances → expected adapter call traces (tool, args, order), executed in CI on every schema/prompt change. All quality claims become "passes suite X vN" — measurable, falsifiable, honest. Borrow M10 wholesale; this is the single most important borrow.

**R3. Cap tiering at two levels.** Utterance+context (immutable, stored raw) and validated plan/call-graph. No intermediate "semantic layer" until measured pain demands it — MLIR exists because premature one-size IR fails [S8], but dialect proliferation is also a cost (M1 overhead). Add a level only when two concrete consumers need different views.

**R4. Type every slot; make unknowns explicit.** Every tool argument typed; missing information encoded as explicit `unknown` + `ask_user` flag, never silently defaulted or omitted (M2/M5). Silent defaults are the pipeline's undefined behavior: they execute *confidently wrong*.

**R5. Mandatory provenance spans.** Every SIR node cites char-spans of the source utterance that justify it (M8). Clarification questions quote the span ("by 'soon' here — did you mean Friday?"). Any transform that cannot preserve spans must be redesigned; provenance loss = diagnosability death.

**R6. Canonicalize conservatively; keep derivational history.** Normalize only uncontroversial equivalences (dates, units, enums, IDs) (M4). Do NOT collapse paraphrases or resolve ambiguity silently — distinct readings are distinct intentions (D3); where ambiguity is detected, either branch explicitly or ask. Store the raw utterance immutably next to every canonical form.

**R7. semver the schema from day one; adapters declare supported ranges.** With migration tooling and a deprecation policy (M11), because breaking schema changes will happen in the first six months (§4 calibration). Cached/resumed plans carry their schema version.

**R8. Per-adapter conformance suites + escape hatch.** Each provider adapter gets its own conformance test against the SIR version range (M9); provider-specific capabilities get an explicit extension mechanism ("intrinsics") rather than polluting the core schema.

**R9. Log costs now; optimize routing later.** Record latency/tokens/$ per stage from day one; build no cost-driven tool-routing until there is data (M7). In compilers cost models choose among correct implementations; here there is no correctness floor, so the model needs empirical grounding even more.

**R10. Enforce a three-part rule for every new SIR construct:** merge requires (a) producer guidance (prompt/schema doc showing when the LLM emits it), (b) consumer code (an adapter or analyzer that reads it), (c) a test exercising both. This pass-manager-style discipline prevents dead-schema growth — the SIR's equivalent of "no pass without a consumer".

**Anti-recommendation.** Do not attempt formal semantics for the SIR at E1 (no denotational model, no equivalence proof — D1/D2 make it unstatable). The engineering budget goes to R2's empirical oracle instead; that is what actually catches meaning-distorting errors [S7].

## 6. Sources

References below were opened and read during this assessment (2026-08-24). `amr.isi.edu` itself was unreachable from this environment (blocked as private-network address), so AMR claims are anchored in the ACL Anthology papers instead.

- **[S1]** LLVM Language Reference Manual — https://llvm.org/docs/LangRef.html — LLVM IR as typed SSA "common code representation"; precise per-instruction semantics; basis for P1, P7, M2.
- **[S2]** The LLVM Target-Independent Code Generator — https://llvm.org/docs/CodeGenerator.html — layered lowering pipeline (LLVM IR → SelectionDAG → MachineInstr → MCInst), target-description classes, documented phases/cost heuristics; basis for P3, P5, M1, M6, M7, M9.
- **[S3]** CompCert project page — https://compcert.org/ — machine-checked proof that generated code behaves "exactly as prescribed by the semantics of the source program"; basis for P2, P6, D1–D2.
- **[S4]** Montague Semantics (Stanford Encyclopedia of Philosophy) — https://plato.stanford.edu/entries/montague-semantics/ — model-theoretic semantics for constructed fragments; compositionality as designed principle; scope ambiguity via distinct derivations; basis for D1, D3.
- **[S5]** Banarescu et al. 2013, "Abstract Meaning Representation for Sembanking" (LAW 7) — https://aclanthology.org/W13-2322/ — founding AMR paper (landing page/metadata inspected); AMR as the closest existing artifact to an "SIR".
- **[S6]** Cai & Knight 2013, "Smatch: an Evaluation Metric for Semantic Feature Structures" (ACL) — https://aclanthology.org/P13-2131/ — smatch metric; alignment problem NP-complete; IAA study design (annotators converge gradually toward consensus annotation); basis for D5.
- **[S7]** Opitz & Frank 2022, "Better Smatch = Better Parser? AMR evaluation is not so simple anymore" (Eval4NLP) — https://aclanthology.org/2022.eval4nlp-1.4/ — parsers surpass estimated human IAA yet emit meaning-distorting errors; human acceptability 0.58–0.69 on Little Prince; high SMATCH does not imply better quality; basis for D2, D5.
- **[S8]** MLIR Rationale — https://mlir.llvm.org/docs/Rationale/Rationale/ — multi-level IR motivated by single-IR failure for new domains; dialects/extensibility machinery; basis for P7, M11, R3, R7.
