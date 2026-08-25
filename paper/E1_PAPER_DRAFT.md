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

<!-- SECTION-2 -->

## 3 Methods

<!-- SECTION-3 -->

## 4 Results

<!-- SECTION-4 -->

## 5 Threats to Validity

<!-- SECTION-5 -->

## 6 Discussion

<!-- SECTION-6 -->

## 7 Conclusion and Future Work

<!-- SECTION-7 -->

## References

<!-- REFS -->
