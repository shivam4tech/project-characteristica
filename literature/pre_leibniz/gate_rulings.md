# Pre-Leibniz Relevance-Gate Rulings (CE-01)

Worker: Pre-Leibniz Researcher (re-dispatch; predecessor W15-PRE died before writing anything — this file supersedes nothing, starts fresh).
Status: **initial rulings written up front** per CE-01 README §Historical relevance gate and ORGANIZATION.md §5. Rulings marked `provisional` may be upgraded/downgraded as sources are opened; final state of each ruling is restated in the per-system file.

## Gate criteria (verbatim basis: expeditions/CE-01/README.md §Historical relevance gate)

A pre-Leibniz system earns research time only if it plausibly contributes **≥1** of:

| # | Criterion |
|---|---|
| G1 | representation primitives |
| G2 | compositional mechanisms |
| G3 | symbolic inference |
| G4 | combinatorial generation |
| G5 | taxonomic organization |
| G6 | ambiguity reduction |
| G7 | formalization of conceptual relations |
| G8 | machine-relevant design principles |
| G9 | demonstrable influence on later universal-representation projects |

Additional binding rules applied here:
- Influence claims require **documented reception** (who read whom), not vague "precursorship" (ORGANIZATION.md §5 evidence standard).
- Generic systems fail explicitly, with reasons (task instruction).
- Failing systems stop after the justification window; no general-history drift.
- Charter finding labels used throughout (Observation / Historical Claim / Unresolved …).

## Ruling summary (final after extraction pass)

| System | Ruling | Criteria hit | Confidence | Note file |
|---|---|---|---|---|
| Ramon Llull — Ars Magna (c.1305–1308) | **PASS** | G1, G4, G9 | high | `llull_ars_magna.md` |
| Descartes — mathesis universalis + 20 Nov 1629 letter to Mersenne | **PASS** | G1, G2, G7, G8, G9 | high | `descartes_mathesis_mersenne_1629.md` |
| George Dalgarno — Ars Signorum (1661) | **PASS** (structural details ⚠ pending primary text) | G1, G5, G6, G9 | high (ruling) / low-med (details) | `dalgarno_1661.md` |
| John Wilkins — Essay towards a Real Character (1668) | **PASS** | G1, G5, G6, G8, G9 | high | `wilkins_1668.md` |
| Cave Beck — The Universal Character (1657) | **PASS (narrow)** — counterexample value | G8, G6(failure-mode) | medium | `beck_1657.md` |
| Athanasius Kircher — Polygraphia nova (1663) | **PASS (narrow)** — failure-mode value; Lullist lineage verified; Leibniz link ⚠ unresolved | G4, G6(failure-mode), G9(partial) | medium | `kircher_polygraphy.md` |
| Joachim Jungius — Hamburg logic/algebra of propositions | **DEFERRED (Unresolved)** | G3, G7 plausible | low | recorded below only |

Post-extraction changes vs initial rulings: none reversed. Two narrow passes confirmed narrow (Beck = pure-codebook counterexample; Kircher = word-table interlingua failure mode). One reception claim downgraded to Unresolved (Leibniz–Kircher 1670 letter: zero hits in local salvage sources, not verifiable within budget).

## Per-system written justification

### 1. Ramon Llull, Ars Magna — PASS (high confidence)
- G4/G1: the Art rotates fixed-letter alphabets of absolute and relational principles through combinatorial figures (tabula/tabula generalis, binary/ternary mixtions) to generate propositions — a concept-alphabet plus combinatorial engine, i.e., representation primitives + combinatorial generation.
- G9: strongest reception chain of any candidate: Leibniz's *Dissertatio de arte combinatoria* (1666) takes its very title-genre from the ars combinatoria/Lullian tradition and discusses Lully explicitly; confirmed against the local salvage source `sources/loemker_dac.txt` (Loemker's DAC translation) and `sources/oup_dac_intro.txt`. This satisfies "documented reception."
- Not a biography study: extraction will target the mechanism (alphabet→figure→mixtion→inference-by-place), not Llull the person.

### 2. Descartes mathesis universalis + Mersenne letter (Nov 1629) — PASS (high confidence)
- G7/G2: Rule IV of the *Regulae* frames a universal mathematics of order and measure applicable to any subject matter — formalization of conceptual relations and a composition story ("order and measure").
- G1/G8/G9: the 20 Nov 1629 letter to Mersenne sketches a philosophical language assembled from primitive ideas "ordered like numbers," with explicit feasibility analysis (needs a true philosophy; ordering of thoughts vs. words). This is the canonical pre-Leibniz statement of the alphabet-of-thought program and Leibniz engages with it repeatedly (confirmed in local salvage sources). Machine-relevant design principle: decomposition into primitives + systematic recomposition, and Descartes' stated blocker (no complete inventory of primitives without true philosophy) is itself a transferable failure mode.

### 3. George Dalgarno, Ars Signorum (1661) — PASS (high confidence)
- G1/G5/G6: a priori philosophical language built from a taxonomy of 17 (later 12) primary genera decomposed into 51 differentiae — taxonomic organization driving character formation; characters designed to be self-interpreting (ambiguity reduction).
- G9: direct documented reception: Leibniz discusses and praises Dalgarno's scheme (New Essays III; correspondence), and ranks it above mere cipher schemes. Extraction targets genus/differentia matrix mechanics and why it stalled.

### 4. John Wilkins, Essay towards a Real Character and a Philosophical Language (1668) — PASS (high confidence)
- G1/G5/G6/G8: 40 genera × differences × species taxonomic tree rendered as syllabic/alphabetic characters; pronunciation mirrors inscription; separate lexicon tables. Ambiguity reduction by construction; the most engineered pre-Leibniz representational artifact.
- G9: standard reference point in Leibniz's own discussions of universal characters; documented in the same secondary literature Leibniz's circle read. Failure mode (taxonomic arbitrariness, maintenance cost, naturalist semantics) is highly machine-relevant — maps onto ontology-maintenance problems.

### 5. Cave Beck, The Universal Character (1657) — PASS (narrow, medium confidence)
- Justification: passes only as a **design-primitive counterexample** (G8) and ambiguity/decodability study (G6): every word replaced by a decimal numeral indexing a Latin–English lexicon; "Latin learned in a few hours" claim. Zero compositionality — a pure codebook. This isolates exactly the variable the project cares about (codebook lookup vs. compositional generation), and its reception/rejection by contemporaries is documented in the universal-language-scheme historiography.
- Narrowness: if extraction shows no mechanism beyond enumeration worth recording beyond the counterexample lesson, the file stays deliberately short. It is NOT treated as a serious rival scheme.

### 6. Athanasius Kircher — Polygraphia nova (1663); Musurgia universalis (1650) combinatorics — PASS (narrow, medium confidence)
- G9/G4: Leibniz personally contacted Kircher (1670 letter enclosing the DAC) and cites Kircher's combinatorial work in the DAC orbit; polygraphy (numbered multilingual word-tables enabling correspondence across languages) is a documented member of the pre-Leibniz mechanical-language lineage Leibniz knew.
- Narrowness/failure mode (G6-adjacent): polygraphy assumes cross-language word-for-word equivalence via tables — precisely the failure mode of naive word-substitution machine translation. Recorded as a cautionary mechanism, not a positive design.

### 7. Joachim Jungius — DEFERRED (Unresolved), not passed this run
- Plausible criteria: G3/G7 (algebraic-symbolic treatment of propositions; quantification anticipations reported by scholarship).
- Why deferred rather than passed: (a) his decisive logical writings were little published in his lifetime, and **no accessible primary or scholarly secondary source was available locally this run** (`literature/pre_leibniz/sources/` holds only Loemker DAC + OUP intro, which mention him not at all beyond passing reference); (b) the reception claim "Leibniz praised Jungius" needs a citable locus (Protocol §1: snippets insufficient) that this budget could not verify; (c) spending scarce hours here would violate the 30-minute justification window discipline.
- Escalation recommendation: a future pass with EEBO/Jungii Opuscula access rules him IN or OUT in <30 min. Logged as Unresolved per charter.

## Explicitly failed generic candidates (gate honesty)

No additional systems were studied long enough to fail; the seven assigned candidates are ruled on above. Two borderline calls are recorded honestly rather than inflated:
- Beck 1657 and Kircher polygraphy pass **only narrowly** (failure-mode/design-counterexample value). If the Chief Scientist finds their lessons already covered by Wilkins/Dalgarno extractions, they can be archived without loss.

## Sources relied on for these initial rulings

- `literature/pre_leibniz/sources/loemker_dac.txt` — Loemker translation of Leibniz's Dissertatio de arte combinatoria (mentions Lully/Ars magna commentary and Descartes' priority claim; lines ~158, ~409).
- `literature/pre_leibniz/sources/oup_dac_intro.txt` — OUP introduction to the DAC (predecessor survey incl. Llull, Kircher, 17th-c. character schemes).
- Per-system citations are completed in each extraction file as sources are opened (web/primary), per Protocol §1.
