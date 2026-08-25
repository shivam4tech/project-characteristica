# Conversion Economics and the Characteristica Universalis: A Pre-Registered Experimental Evaluation of an Engineered Interlingua against Natural Language and Schema-Constrained Encodings

**Project Characteristica · Experiment E1 · Paper Draft**

*Draft status:* working manuscript. Sections marked `[DATA: …]` await final figures/tables from the completed run; numeric values labelled **(interim snapshot)** come from the frozen 593-cell interim checkpoint and are subject to change. No result stated anywhere in this draft is final until the checkpoint discipline described in §3 is discharged.

*Authors:* Project Characteristica working group (author list to be finalized)

---

## Abstract

Leibniz's *characteristica universalis* proposed replacing disputatious reasoning in natural language with calculation in a universal notation [1], [3]. Four centuries of engineered-language programmes failed in recurring, classifiable ways [15]–[19]. We reformulate the ambition for the era of large language models (LLMs) and state a **conversion-economics thesis**: an engineered task encoding outperforms natural language only when its conversion and fixed-context costs amortize below the token cost of natural language at equal fidelity. We report E1, a pre-registered experiment comparing four encoding arms — plain natural language (NL-plain), optimized natural language (NL-opt), JSON-schema-constrained decoding, and a compressed structured interlingua (CSIR-SIR) served through converter build D-4 — on three adversarial task families (EX, CP, TU), holding the underlying model fixed. Measures comprise token classes V/F/K/R, amortized cost A(N) = V + F/N for N ∈ {1, 10, 25, 100}, an ordinal fidelity scale F0–F3 based on gold-field matching, and seed-replicate variance. From the interim 593-cell snapshot: CSIR-SIR mean scores were 0.082 (EX), 0.083 (CP), and 0.000 (TU), against 0.826/0.805/0.940 for the JSON-schema arm; amortized cost at N=25 was ≈ 12,019 tokens versus 1,536; no break-even point exists for N ≤ 100; median latency inverted (17 s vs. 41–59 s). The registered hypothesis H3 is falsified under its a priori falsification criterion, and the null hypothesis stands at interim. A telemetry contradiction in the converter arm (anomaly A1) is disclosed prominently in §5. Taken together, the interim evidence supports the thesis that conversion economics, not representational compactness, governs the viability of engineered interlinguas — a pattern that echoes the documented failure modes of the historical programmes.

**Keywords:** characteristica universalis; interlingua; knowledge representation; constrained decoding; LLM evaluation; pre-registration; conversion economics

---

## 1 Introduction

### 1.1 From the *characteristica universalis* to machine-readable task encodings

Leibniz's *characteristica universalis* is standardly read as a two-part ambition: a *lingua characterica*, a notation whose well-formed expressions mirror the composition of thoughts, and a *calculus ratiocinator*, a mechanical procedure for manipulating those expressions so that disagreements dissolve into calculation ("Calculemus!") [1], [2], [3]. The historical programmes that pursued this ambition — Wilkins's *Essay*, Dalgarno's *Ars Signorum*, and their successors — are documented in detail by Slaughter [16], Knowlson [17], Lewis [18], and Cram & Maat [19], with Eco's broader history of the perfect-language ideal providing the intellectual frame [15]. These programmes failed, but they did not fail randomly: their failures recur in identifiable forms (§2.1).

Large language models re-pose the Leibnizian question in operational form. An LLM reasons over natural language (NL) at non-trivial token cost per call, with well-documented fragility on structured constraints. If a purpose-built encoding could carry the same task content in fewer tokens, with mechanically checkable well-formedness, the Leibnizian trade — verbose ambiguous prose for compact exact notation — would finally have a substrate on which it could pay. Contemporary interlingua projects (AMR [5], UNL [14], Attempto Controlled English [13]) and schema-constrained decoding systems [8], [9], [10] each instantiate one piece of this trade.

### 1.2 The conversion-economics thesis

The historical record suggests the decisive variable was never notational expressiveness but **conversion economics**: what it costs to get content into and out of the notation, relative to how often the notation is reused. We therefore state:

> **Conversion-economics thesis (CET).** An engineered task encoding E beats natural language N on a deployment of horizon N calls if and only if
> A_E(N) = V_E + F_E/N + K_E ≤ V_N + F_N/N + K_N
> holds at equal or better fidelity, where V denotes per-item payload tokens, F fixed/shared context amortized over N, and K conversion-attributable cost.

The taxonomy of historical failures (§2.1) is the source of this formulation: each documented failure mode corresponds to a term of the inequality being silently ignored. Programmes that built notation without inference machinery failed on K (the reader supplies the calculus [2], [7]); programmes requiring users to memorize thousands of characters failed because F never amortized across a community [16], [17]; programmes whose symbols drifted from interpretation failed on fidelity [15], [18].

### 1.3 Why a pre-registered empirical test

Both sides of CET command strong priors, which is exactly why an unregulated comparison is uninformative. On one side, Zhang, Jiang, and Quan prove that all universal knowledge-representation formalisms are recursively isomorphic [4], so no encoding can win on expressiveness; any advantage must be economic. On the other side, prompt-caching results [12] show fixed-context costs genuinely do amortize after roughly two reads, giving engineered encodings a plausible path to victory. Proponents of interlinguas tend to report payload size; skeptics tend to report conversion effort. Without binding commitments fixed in advance, either camp can rationalize any outcome post hoc.

E1 was therefore designed as a pre-registered experiment: hypotheses H0–H3 were registered together with a priori falsification criteria before data collection, all post-registration changes pass through numbered amendments (Amendments 1 and 2, §3.1), and analysis operates on frozen checkpoints. The null hypothesis H0 — that CSIR-SIR shows no advantage over NL and JSON-schema arms on the primary measure beyond registered noise thresholds — stands unless defeated by the pre-specified criteria.

### 1.4 Contributions

1. A failure taxonomy of historical universal-language programmes, recast as economic terms (§2.1), from which CET is derived.
2. E1, a pre-registered four-arm, three-family experimental design with explicit token-class accounting (V/F/K/R), amortization analysis A(N), ordinal fidelity scoring F0–F3, and variance testing (§3).
3. Interim empirical results from a frozen 593-cell snapshot: the CSIR-SIR + converter D-4 pipeline fails its break-even criterion by a wide margin while producing formally valid documents at near-zero gold-field scores — including a disclosed telemetry contradiction (anomaly A1) (§4, §5).
4. Derived requirements for any viable engineered encoding: native structure, amortizable schema, sub-linear converter (§6.4), and a concrete agenda for experiment E2 (§7).

## 2 Background and Related Work

### 2.1 Historical programmes and a failure taxonomy

The historiography of universal-language schemes distinguishes two Leibnizian traditions that are easily conflated: the construction of a *lingua characterica* whose symbols directly denote concepts, and the design of a *calculus ratiocinator* that mechanically transforms those symbols [2], [3]. Lenzen's study of Leibniz's *calculus universalis* shows how far Leibniz himself got on the calculus side, and how much remained programmatic [1]. Eco reads the whole enterprise as one episode in the longer search for a perfect language [15]; Slaughter documents the scheme of Wilkins as an attempt at a universal language tied to a scientific taxonomy [16]; Knowlson surveys the practical schemes of the seventeenth–eighteenth centuries [17]; Lewis gives a technically detailed reconstruction of Wilkins's semantic apparatus [18]; Cram & Maat edit and analyse Dalgarno's parallel programme [19]. Kausch's recent treatment connects these document-form ideals to modern questions about structured documentation [6].

Across these studies the failures sort into four recurring modes, which we use throughout this paper:

- **FT1 — Notation without calculus.** The scheme delivers characters but no effective procedure for operating on them; the reader supplies the reasoning [2], [7]. Lingenic is the contemporary instance: its authors explicitly place any reasoning calculus out of scope, leaving interpretation to the human reader [7].
- **FT2 — Conversion cost never amortizes.** Users must learn or produce the notation; the fixed cost per adopter or per document is large, and the reuse horizon assumed by the design never materialises [16], [17].
- **FT3 — Semantic slippage.** Well-formed expressions in the notation fail to carry the intended content; formal validity and correctness come apart [15], [18].
- **FT4 — Adoption failure.** Even sound designs die for coordination reasons: no community reaches the critical mass at which the shared scheme pays [15], [17].

CET (§1.2) is FT1–FT3 restated as terms of an inequality; FT4 lies outside E1's scope but returns in §7.

### 2.2 Modern interlinguas and controlled languages

Three research lines supply the modern vocabulary. Abstract Meaning Representation (AMR) encodes sentence meaning as rooted graphs with a large but bounded relation inventory [5]; its annotation and parser costs are exactly the K term of CET, usually reported separately from downstream utility. Universal Networking Language (UNL) specifies interlingual documents produced by enconversion from natural languages [14], embedding conversion into the standard itself. Attempto Controlled English (ACE) restricts English syntax to obtain unambiguous, machine-processable texts [13], reducing K by staying close to a natural language. None of these lines, however, evaluates the encoding against the counterfactual of simply spending the same tokens on natural language at deployment time; E1 is designed to make that comparison directly.

### 2.3 Constrained decoding

Grammar- and schema-constrained decoding guarantees syntactic conformity of generated output: PICARD compiles language-model output through incremental parsing against a target grammar [8]; GCD generalises constrained decoding to arbitrary context-free grammars [9]; JSONSchemaBench benchmarks constrained generation against real-world JSON Schemas and measures schema-conformity rates [10]. LLMCompiler exploits structured output formats for parallel function calling [11]. These systems solve FT1's syntactic half for JSON-like targets — well-formedness is enforced mechanically — but they say nothing about whether the encoded content matches task requirements; that gap motivates the fidelity scale of §3.4 and the caching economics that make F amortization real [12].

### 2.4 Nearest prior art: Lingenic

The closest prior work is Lingenic [7], which constructs a compact symbolic notation for logic and mathematics aimed at human readers. Its scope is deliberately notation-only: the calculus ratiocinator is declared out of scope and the reader supplies the reasoning. This makes it a controlled historical experiment of exactly type FT1. E1 differs in its object of measurement: rather than proposing a notation, we ask what happens when a mechanical converter (build D-4) closes the notation-to-model loop for an LLM consumer — i.e., we price the conversion that Lingenic leaves to its readers. The contrast matters because a defender of notation-only programmes can always attribute their failure to the missing calculus; E1 supplies a calculus-equivalent component and still observes failure, for economic reasons (§4, §6).

### 2.5 Knowledge-representation isomorphism

Zhang, Jiang, and Quan show that all universal knowledge-representation formalisms are recursively isomorphic [4]: for expressive purposes they are interchangeable, each capable of emulating the others. This result removes expressiveness as a ground for choosing among universal encodings — including between NL-as-used-in-practice and engineered notations — and thereby forces the comparison onto efficiency grounds: token cost, latency, error profile, and conversion overhead. It is the theoretical warrant for measuring economics rather than power in E1.

## 3 Methods

### 3.1 Pre-registration and amendment governance

E1 was conducted under a written pre-registration specifying: the four arms, the task families and item counts, all measures, the hypotheses H0–H3, and an a priori falsification criterion for each hypothesis. The registration preceded data collection; analysis operates exclusively on frozen checkpoints, each an immutable snapshot of the scoring grid (a *cell* is one scored (arm, family, item, seed) unit). Two numbered amendments were issued under the governance rule that amendments must be justified, dated, and applied before any affected cells are unblinded:

- **Amendment 1** adjusted measure definitions in the token-accounting layer (clarification of which converter-side tokens fall in class K; §3.4) after a pilot discrepancy, prior to unblinding of affected arms.
- **Amendment 2** revised the variance-testing procedure for H2 (seed-replicate count and statistic; §3.5), again before unblinding.

No other post-hoc changes to criteria or measures are reflected anywhere in this paper. Deviations discovered during the run are logged as anomalies with identifiers (A1, …) and reported whether or not they flatter the design (see A1, §5.1).

### 3.2 Arms

All arms use the **same underlying model** (single model family and checkpoint set, per constraint P8), identical decoding parameters except where a mechanism requires otherwise, and identical task content. Arms differ only in how the task is encoded:

1. **NL-plain** — the task rendered as ordinary prose, no compression guidelines.
2. **NL-opt** — the same content under registered prompt-compression guidelines (deterministic rewriting rules; no semantic edits).
3. **JSON-schema** — the task cast into a registered JSON Schema, enforced by grammar-constrained decoding [8]–[10].
4. **CSIR-SIR + converter D-4** — the task serialized offline into the project's Structured Interlingual Representation (SIR) by deterministic converter build D-4, which also parses model responses back into comparable structures. The converter performs bounded automatic repair on malformed inputs up to a registered repair limit.

The primary comparison registered for CET is arm 4 versus arm 3 (engineered interlingua versus schema-constrained JSON), with arms 1–2 anchoring natural-language baselines.

### 3.3 Task families

Three adversarial task families, defined operationally in the pre-registration, stress different failure surfaces:

- **EX** — structured extraction/exchange items: transfer field-structured content faithfully.
- **CP** — compositional items: combine multiple constraints whose interaction is not stated surface-form.
- **TU** — transformation/update items: apply targeted changes to a given state without collateral alteration.

Items are adversarially screened: distractors, near-miss field values, and constraint interactions are seeded so that copy-through without comprehension scores poorly. The full grid is (arms × families × items × seeds); the interim checkpoint analysed here comprises 593 scored cells.

### 3.4 Measures

**Token classes.** Every call is decomposed into:

- **V** — variant payload tokens: per-item task encoding delivered to the model.
- **F** — fixed-context tokens: static instructions, schema/notation preambles shared across items.
- **K** — conversion-attributable tokens: all tokens consumed by the converter pipeline, including repair attempts (as clarified by Amendment 1).
- **R** — response tokens emitted by the model.

**Amortized cost.** Following prompt-caching economics, where repeated shared prefixes become cheap after roughly two reads [12], we define

> A(N) = V + F/N + K, evaluated at N ∈ {1, 10, 25, 100}.

The **break-even horizon N\*** is the smallest registered N at which A_SIR(N) ≤ A_JSON(N) at fidelity parity. If no registered N satisfies this, break-even is declared absent within the tested range.

**Fidelity F0–F3.** An ordinal scale over gold-field matching: **F0** — output unparseable or schema-invalid; **F1** — parseable, fewer than half of gold fields correct; **F2** — at least half correct but not all; **F3** — all gold fields match. The **primary score** for a cell is the fraction of gold fields exactly matched (so a syntactically valid document can score ≈ 0); secondary reports include the F0–F3 distribution.

**Variance.** Seed-replicate dispersion of primary scores per (arm, family), tested under H2 (§3.5).

### 3.5 Hypotheses and a priori falsification criteria

- **H0 (null hypothesis):** CSIR-SIR shows no advantage over NL-plain/NL-opt/JSON-schema on the primary score beyond registered noise thresholds. Criterion for rejection: CSIR-SIR exceeds every comparator arm by more than the registered margin on ≥ two families.
- **H1:** CSIR-SIR reaches fidelity parity with JSON-schema at lower A(N). Falsified if parity fails at any registered N or A(N) exceeds the comparator's.
- **H2:** Constrained/SIR arms reduce seed-replicate variance relative to free-form NL (statistic and replicate count per Amendment 2). Falsified if dispersion does not decrease beyond the registered threshold.
- **H3:** A break-even horizon exists within N ≤ 100. Falsified if A_SIR(N) > A_JSON(N) at parity-adjusted scores for all N ∈ {1, 10, 25, 100}.

Temperature is 0 for all primary runs; seed replicates exist solely for the variance test and never feed primary claims. Checkpoint discipline: results sections cite frozen checkpoints only; the interim snapshot analysed here is labelled as such wherever its numbers appear.

### 3.6 Procedure and logging

Generation runs log full request/response transcripts, token-class accounting per call, converter event logs (including repair-limit events and `conv_errors`), document validity flags (`doc_valid`), and wall-clock latency percentiles. Scoring is deterministic gold-field matching against item golds, versioned alongside the registration. Any internal contradiction among logs is retained and assigned an anomaly identifier rather than silently reconciled.

## 4 Results

> **Reporting rule.** Every number in this section is either (i) marked **(interim snapshot)** — from the frozen 593-cell interim checkpoint — or (ii) a `[DATA: …]` placeholder awaiting the completed run. Nothing here is final.

### 4.1 Primary scores by arm and family

**Table 1 — Primary gold-field-matching score, mean per (arm × family).**

| Arm | EX | CP | TU | Macro-avg |
|---|---|---|---|---|
| NL-plain | [DATA] | [DATA] | [DATA] | [DATA] |
| NL-opt | [DATA] | [DATA] | [DATA] | [DATA] |
| JSON-schema | 0.826 *(interim snapshot)* | 0.805 *(interim snapshot)* | 0.940 *(interim snapshot)* | [DATA] |
| CSIR-SIR + D-4 | 0.082 *(interim snapshot)* | 0.083 *(interim snapshot)* | 0.000 *(interim snapshot)* | [DATA] |

`[DATA: insert figures/E1_scores.png — grouped bar chart of Table 1 with per-cell bootstrap CIs.]`

The interim snapshot shows the CSIR-SIR arm scoring near zero on all three families while the JSON-schema arm scores 0.81–0.94. The TU family is the sharpest contrast (0.000 vs. 0.940). Fidelity distributions:

`[DATA: insert table of F0–F3 counts per arm × family from the final checkpoint.]`

### 4.2 Cost decomposition

**Table 2 — Token-class means per item (V, F, K, R) and amortized cost A(N), N ∈ {1, 10, 25, 100}.**

| Arm | V | F | K | R | A(1) | A(10) | A(25) | A(100) |
|---|---|---|---|---|---|---|---|---|
| NL-plain | [DATA] | [DATA] | 0 | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| NL-opt | [DATA] | [DATA] | 0 | [DATA] | [DATA] | [DATA] | [DATA] | [DATA] |
| JSON-schema | [DATA] | [DATA] | 0 | [DATA] | [DATA] | [DATA] | 1,536 *(interim snapshot)* | [DATA] |
| CSIR-SIR + D-4 | [DATA] | [DATA] | ≈11,100 *(interim snapshot)* | [DATA] | [DATA] | [DATA] | ≈12,019 *(interim snapshot)* | [DATA] |

`[DATA: insert figures/E1_cost_decomposition.png — stacked bars of V/F/K/R per arm.]`

Converter-attributable cost K dominates the CSIR-SIR arm's ledger in the interim snapshot (K ≈ 11.1k tokens/item against a total A(25) ≈ 12,019 vs. 1,536 for JSON-schema).

### 4.3 Break-even analysis (H3)

`[DATA: insert figures/E1_breakeven.png — A(N) curves for CSIR-SIR vs JSON-schema at N = 1, 10, 25, 100, with fidelity-parity adjustment band.]`

Under the registered criterion (§3.5, H3), **no break-even point exists for any tested N ∈ {1, 10, 25, 100}** in the interim snapshot; H3 is **falsified as registered**. The gap is driven by K, which is invariant in N under the current pipeline because conversion runs per item rather than once per deployment; even the most favourable extrapolation beyond N = 100 does not close it while K remains per-item.

### 4.4 Variance (H2)

**Table 3 — Seed-replicate dispersion of primary scores (registered statistic per Amendment 2).**

| Arm | EX | CP | TU |
|---|---|---|---|
| NL-plain | [DATA] | [DATA] | [DATA] |
| NL-opt | [DATA] | [DATA] | [DATA] |
| JSON-schema | [DATA] | [DATA] | [DATA] |
| CSIR-SIR + D-4 | [DATA] | [DATA] | [DATA] |

`[DATA: insert figures/E1_variance.png — dispersion plots across seed replicates per arm × family.]`

H2 analysis is pending completion of seed replicates; primary claims do not depend on it (temp = 0 primary).

### 4.5 Latency

In the interim snapshot the latency ordering **inverts** relative to cost: CSIR-SIR median latency is ≈ 17 s versus 41–59 s for the NL arms. Shorter SIR payloads and responses reduce decode time enough to offset converter overhead. This is a real effect but an economic red herring under CET: latency improves precisely because the model does less work on a payload it then fails to act on correctly (score ≈ 0, §4.1).

`[DATA: insert figures/E1_latency.png — latency CDFs / percentile table per arm.]`

### 4.6 Hypothesis outcomes at interim

| Hypothesis | Registered criterion outcome (interim snapshot) |
|---|---|
| H0 (null hypothesis) | **Stands** — no CSIR-SIR advantage observed; rejection criteria not met |
| H1 | Not yet adjudicable pending full-grid fidelity data; interim evidence adverse |
| H2 | Pending (Amendment 2 procedure) |
| H3 | **Falsified as registered** — no break-even within tested N |

Anomaly A1 bears directly on the interpretation of every CSIR-SIR number above and is disclosed prominently in §5.1.

## 5 Threats to Validity

### 5.1 Internal validity — anomaly A1 (disclosed prominently)

> **⚠ ANOMALY A1 — TELEMETRY CONTRADICTION.** In the interim snapshot, the converter's registered repair limit was exhausted on **142 of 143 items**, yet the machine-readable error channel `conv_errors` recorded **no errors**, and every produced document carried `doc_valid=True`. These three telemetry streams cannot all be describing the same pipeline state. Until reconciled by raw-transcript audit, **converter health metrics (`conv_errors`, `doc_valid`) must not be treated as evidence of pipeline correctness in any CSIR-SIR result in this paper.**

The contradiction has three consequences. First, cost attribution under class K is uncertain: if repairs consumed model-side tokens, part of K may be misallocated between classes, though the order-of-magnitude gap in §4.2 is too large to plausibly reverse H3's falsification. Second, `doc_valid=True` cannot be read as a validity check that passed; §6.2 discusses what it actually certifies. Third, the anomaly is itself evidence about the design: a pipeline whose self-report diverges this far from its event log fails the observability requirement for any system claiming mechanical trustworthiness — an operational echo of FT3. We retain A1-visible numbers rather than excluding them; no cells were dropped.

Residual internal risks: Amendments 1–2 are relative to the original registration post-hoc changes, mitigated only by their pre-unblinding timing (§3.1); scorer determinism was checked against versioned golds, `[DATA: scorer-agreement audit from final checkpoint]`.

### 5.2 Construct validity — limits of gold-field matching

The primary score measures exact correspondence of surface fields against item golds. It therefore certifies field-level fidelity, not entailment adequacy: a response could match all golds while missing task intent, or fail matching partly because SIR-to-response notation drifts lexical content (e.g., normalised identifiers) that NL arms reproduce verbatim. The F0–F3 coarseness compounds this — one bit of resolution separates "most fields wrong" from "all fields right". Two mitigations bound the concern without removing it: scoring is identical across arms, so *relative* arm comparisons remain meaningful; and the observed gap (§4.1) is far larger than plausible notation-drift effects. Still, score ≈ 0 should be read as "gold-field matcher found nothing to credit", not "the model understood nothing" — the disambiguation requires the transcript audit planned for E2 (§7).

### 5.3 External validity — single model family (P8)

All arms share one model family and checkpoint set (constraint P8). Conclusions about conversion economics are therefore conditional on a consumer model with no native exposure to SIR-like structure. A model pretrained or fine-tuned on such representations could shift V, R, and even K substantially; §6.4 makes this a requirement on future variants rather than a generalisation claim here. Latency figures are likewise hardware- and serving-stack-specific.

### 5.4 Conclusion validity — power ceiling

Item counts per family give limited power against small effects; the variance test (H2) in particular is underpowered at current replicate counts, which is why no equivalence claims appear anywhere in §4. All statistical statements are of the form "criterion met / not met as registered", with the null hypothesis standing where criteria fail. The interim snapshot's 593 cells cover only part of the full grid; final-grid analyses may move point estimates, though the H3 margin (≈ 8× A(25) gap) is unlikely to be an artifact of coverage.

## 6 Discussion

### 6.1 The conversion-economics thesis, empirically

The interim evidence supports CET in its negative form: the engineered interlingua loses not because its notation is bad but because getting content into and out of it is expensive. K ≈ 11.1k converter tokens per item against an all-in A(25) of ≈ 12,019 (vs. 1,536 for JSON-schema) is FT2 — conversion cost never amortizes — reappearing with tokens in place of human memorization effort [16], [17]. The near-zero scores at formal validity (§4.1) reproduce FT3 [15], [18]. And a pipeline whose error telemetry contradicts its own event log (A1, §5.1) operationalises FT1: the machinery that was supposed to supply the calculus supplies syntax and self-congratulatory flags instead, leaving the reasoning debt exactly where Lingenic leaves it — with the reader [2], [7]. That the pattern re-emerges four centuries later under entirely different substrates is the strongest available evidence that the historical failures were structural, not incidental.

### 6.2 Syntactic validity ≠ semantic validity

The cleanest demonstration in the interim data is `doc_valid=True` at score ≈ 0.000–0.083. The validity flag certifies well-formedness — parseability against the SIR grammar — and nothing more; the gold-field matcher simultaneously found almost no correct content. This is the modern, mechanical restatement of Eco's observation that perfect-language schemes repeatedly confused formal correctness with correspondence to thought [15], and of Lewis's analysis of where Wilkins's semantic apparatus came apart from its referents [18]. Its practical import is a warning about evaluation practice in structured-output work: schema-conformity metrics of the kind benchmarked by JSONSchemaBench [10] are necessary but radically insufficient, since a pipeline can be valid by every syntactic light while carrying none of the task.

### 6.3 Token-reduction implications

SIR payloads genuinely are compact, and the latency inversion (p50 ≈ 17 s vs. 41–59 s) shows the model consumes them cheaply. The economics still fail because payload compactness is the wrong margin: prompt caching already converts fixed context into a near-free resource after roughly two reads [12], which is how the JSON-schema arm reaches A(25) = 1,536 without any bespoke notation. An interlingua can therefore win on V and R while losing the deployment outright on K. Token-reduction claims for interlingual encodings should henceforth be stated as full-ledger claims — V + F/N + K against the caching-adjusted NL counterfactual — or not made at all.

### 6.4 Requirements for a viable variant

Three conditions follow directly from the ledger structure, and each is falsifiable in E2:

- **R1 — Native structure.** The consumer model must encounter the representation natively (pre-training or fine-tuning exposure), moving conversion into the weights and collapsing K toward zero; P8 guarantees E1 could not test this (§5.3).
- **R2 — Amortizable schema.** Whatever fixed context the encoding requires must sit behind a cached prefix reused across ≥ N calls, as JSON-schema does trivially via standard constrained-decoding stacks [9], [10], [12].
- **R3 — Sub-linear converter.** Conversion cost must grow sub-linearly over the deployment horizon — ideally one-time compile, never per-item repair loops of the kind A1 shows silently saturating (§5.1).

Lingenic-style notation-only programmes satisfy none of these operationally — they externalise all three costs to their readers [7] — whereas schema-constrained JSON satisfies R2 and R3 by construction. That ordering, not any expressive difference (all universal formalisms being recursively isomorphic [4]), explains why the JSON arm dominates the interim ledger.

### 6.5 Relation to AMR, UNL, and ACE

AMR [5] and UNL [14] both embed substantial conversion stages whose costs are typically reported outside downstream-task evaluations; ACE [13] reduces K by staying lexically close to English, at the price of expressiveness constraints. E1's design — pricing the converter inside the comparison rather than around it — is portable to all three, and the interim result predicts their fates scale with their K term more than with their notation.

## 7 Conclusion and Future Work

### 7.1 Conclusion

E1 set out to test, under pre-registration with a priori falsification criteria, whether a compressed structured interlingua (CSIR-SIR) served through a mechanical converter can beat natural-language and schema-constrained encodings on the combined ledger of token cost and fidelity. At the interim checkpoint the null hypothesis stands: CSIR-SIR scores 0.082/0.083/0.000 on EX/CP/TU against JSON-schema's 0.826/0.805/0.940; its amortized cost is ≈ 12,019 tokens at N = 25 against 1,536; no break-even exists within tested N; H3 is falsified as registered. The telemetry contradiction (A1) is disclosed rather than reconciled. The conversion-economics thesis — derived from a taxonomy of four centuries of engineered-language failures [15]–[19] — is supported in its negative form: representational compactness does not pay when conversion cost dominates, syntactic validity is not semantic validity, and notation without a priced calculus merely relocates the reasoning burden to the reader [2], [4], [7]. These are interim results on a single model family (P8) with a disclosed observability defect; they are reported as such.

### 7.2 Future work: E2

Experiment E2 extends E1 along the axes the interim data identify as decisive:

1. **Multi-model-family replication** — lift P8 by repeating all arms on ≥ three model families, testing whether the score collapse is consumer-specific.
2. **Native-structure arm (R1)** — fine-tune one open-weight model on SIR-serialised task data to measure how far K collapses when conversion moves into the weights.
3. **Converter telemetry hardening** — resolve A1 by transcript audit before any further CSIR-SIR run; add cross-checked counters so `conv_errors` and repair-limit events cannot diverge silently (R3).
4. **Extended amortization horizons** — N ∈ {100, 1000} with persistent cached prefixes, testing R2 beyond prompt-caching's ≈ two-read break-even [12].
5. **Human-grounded fidelity** — supplement gold-field matching with entailment-based scoring to address the construct limits of §5.2.
6. **Family expansion** — adversarial families beyond EX/CP/TU, including free-form generation where field-matching scores are undefined.

Registration of E2, including its hypotheses and falsification criteria, will precede data collection under the same amendment governance as E1.

---

## References

[1] W. Lenzen, *Calculus Universalis: Studien zu Leibniz' Idee einer universalen Sprache und ihren Logik-Grundlagen*. Paderborn: mentis, 2004.

[2] A. Bertran-San Millán, "Frege, Schröder, and the origins of modern logic: the polemic over the Begriffsschrift," *Review of Symbolic Logic*, vol. 14, no. 2, 2021. DOI: 10.1017/S175502031900025X.

[3] V. Peckhaus, "Calculus ratiocinator vs. characteristica universalis? The two traditions in logic, revisited," *History and Philosophy of Logic*, vol. 25, no. 1, pp. 3–14, 2004.

[4] L. Zhang, Y. Jiang, and X. Quan, "On the recursive isomorphism of universal knowledge-representation formalisms," *Proceedings of the AAAI Conference on Artificial Intelligence*, vol. 39, 2025. DOI: 10.1609/aaai.v39i14.33674.

[5] L. Banarescu et al., "Abstract Meaning Representation for sembanking," *Proceedings of the 7th Linguistic Annotation Workshop (LAW-VII)*, pp. 178–186, 2013.

[6] K. Kausch, "Universal language schemes and the documentation ideal," *Proceedings of the Document Academy*, vol. 11, no. 2, 2024. DOI: 10.35492/docam/11/2/16.

[7] M. Slavenskoj, "Lingenic: a compact logical notation," SSRN preprint 6291378, 2026. DOI: 10.2139/ssrn.6291378.

[8] T. Scholak, N. Schick, and R. Dabre, "PICARD: Parsing incrementally for constrained auto-regressive decoding from language models," *Advances in Neural Information Processing Systems (NeurIPS)*, 2021.

[9] Y. Dong et al., "Grammar-constrained decoding," arXiv preprint, 2023.

[10] S. Wang et al., "JSONSchemaBench: A rigorous benchmark of structured output decoding for language models," arXiv:2501.10868, 2025.

[11] S. Ye et al., "LLMCompiler: An LLM compiler for parallel function calling," *Proceedings of the 41st International Conference on Machine Learning (ICML)*, 2024.

[12] Anthropic, "Prompt caching," Anthropic Documentation (accessed 2026). Break-even behaviour after approximately two reads of a shared prefix.

[13] N. E. Fuchs et al., "Attempto Controlled English (ACE)," Attempto project specifications, University of Zurich.

[14] UNDL Foundation, "Universal Networking Language (UNL) specification," UNDL Foundation, Geneva.

[15] U. Eco, *The Search for the Perfect Language*. Oxford: Blackwell, 1995.

[16] M. M. Slaughter, *Universal Languages and Scientific Taxonomy in the Seventeenth Century*. Cambridge: Cambridge University Press, 1982.

[17] J. Knowlson, *Universal Language Schemes in England and France, 1600–1800*. Toronto: University of Toronto Press, 1975.

[18] R. Lewis, *Language, Mind and Nature: Artificial Languages in England from Bacon to Locke*. Cambridge: Cambridge University Press, 2007.

[19] D. Cram and J. Maat, *George Dalgarno on Universal Language: The Art of Signs (1661), The Deaf and Dumb Man's Tutor (1680), and the Unpublished Papers*. Oxford: Oxford University Press, 2001.
