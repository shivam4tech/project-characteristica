# Athanasius Kircher — Polygraphia nova et universalis (1663)

**Gate ruling: PASS (narrow), medium confidence** — G4 (combinatorial-art framing, Lullist lineage), word-table interlingua failure-mode lesson (G6-adjacent), G9 partial (Lullism documented; Leibniz personal link NOT verified this run — flagged). Ruling basis: `gate_rulings.md`. Narrow pass: recorded as cautionary mechanism, not positive design.

## Relevance justification

Polygraphia nova ("directed from the combinatorial art," per its own subtitle) is a documented member of the mechanical-language lineage the 17th century handed to Leibniz: a tabular pasigraphy in which 1048 multilingual synonym groups are keyed by two-part codes so correspondents sharing no language can exchange letters. It matters to CE-01 as the era's cleanest demonstration that a shared lexicon + function markers *without composition* fails — precisely the failure mode of word-substitution machine translation and of naive prompt-codebooks. Its combinatorial self-presentation also documents how "art of combination" branding traveled from Llull into applied schemes.

## Protocol §2 extraction

| Field | Content | Source | Conf. |
|---|---|---|---|
| **Objective** | Written communication between peoples sharing no language; originated in Emperor Ferdinand III's request for "a kind of lingua universalis"; distributed 1663 as diplomatic gift copies to European rulers, some with an *arca steganographica* (chest of encoding tallies). | Wikipedia, "Polygraphia Nova" (opened this run, citing Fletcher's Kircher study pp.187, 264–291) | high |
| **Primitive units** | Word-level synonym groups: 1048 multilingual groups over 32 pages of tables alphabetized by the Latin column (e.g., magnitudo/grandezza/grandeur/grandeza/Grösse); each group carries a two-part code — Roman numeral = meaning group, Arabic numeral = grammatical function (noun/verb/adjective variant of the group's sense). | Wikipedia §Section one (opened) | high |
| **Representation mechanism** | Encode native text → sequence of code pairs; reader decodes via the same tables into their language. Lineage acknowledged: Tironian notes tradition via "Gustavus Selenus" (Duke Augustus of Brunswick-Lüneburg, 1624); Sections II–III add letter↔Latin-word ciphers based on Trithemius; appended universal dictionary makes the kit workable without extra manuscripts. | Wikipedia §§Background, Section one–three | high |
| **Composition mechanism** | None beyond word-for-word substitution plus grammatical-function marking. No syntax layer, no morphological generation. | My analysis of scheme structure | high |
| **Inference mechanism** | None. | Same | high |
| **Ambiguity handling** | The Roman/Arabic split partially disambiguates polysemy across languages (same sense-group, different grammatical role) — an early feature-tagged interlingua index. Word-level equivalence across languages is nonetheless assumed wholesale. | My analysis from the table mechanics | med |
| **Extensibility** | Table/dictionary append only; no generative capacity; every new word is a new row everywhere the book is copied. | My analysis | high |
| **Claimed universality** | Correspondents "in any part of the world" can exchange letters "without speaking each other's languages" (Kircher's own introduction claim). | Wikipedia §Introduction summary | high |
| **Known limitations** | No evidence any ruler ever used it for translation; sole documented use: Juan Caramuel y Lobkowitz's August 1663 letter acknowledging the copy (Fletcher p.283). Errors found already in the 1661 arca sent to Archduke Charles Joseph; usability without the manual was poor — motivating the 1663 standard edition. | Wikipedia §§Legacy, Background | high |
| **Failure mode** | **Word-for-word equivalence fallacy**: cross-language meaning ≠ per-word synonymy; idiom, syntax, and pragmatics have no representation, so output decodes as stilted gloss at best. Plus distribution-as-gift ≠ adoption — a working artifact nobody used. | Synthesis of above | high |
| **Modern analogue** | 1950s rule-based word-substitution MT; bilingual-concordance phrasebooks; interlingual concept-number dictionaries; the cautionary ancestor of why interlingua MT needed structural analysis (transfer/interlingua debates). | My analysis | med |
| **Candidate experimental implication** | Machine-relevant principle extracted: shared vocabulary + role tags do not substitute for compositional structure. Testable as a pilot arm (word-ID + POS tags vs structured SIR vs plain NL on a translation/paraphrase-fidelity task): predicts Kircher-style arms collapse on idiomatic/compositional items while paying full lexicon overhead. | My analysis | low |

## Reception notes (honest scoping)

- Kircher's Lullism is independently documented: his Springer-profiled student Kaspar Schott "inherited his yearning for universality from his Lullistic teacher Athanasius Kircher"; Kircher's titles self-brand as universal (*Musurgia universalis* 1650, *Ars magna sive combinatoria* 1670 with its "nothing more beautiful than to know everything" maxim). This secures the G4/Lullian-combinatorics linkage. (Springer, Poiesis & Praxis, Schott article — opened.)
- ⚠ **Unverified this run:** the frequently reported direct Leibniz→Kircher contact (1670 letter enclosing the DAC). Local salvage sources contain zero Kircher/Mersenne mentions (grepped). Logged as Unresolved per charter; does not affect the narrow pass, which rests on the mechanism + Lullist lineage + historiographic placement.

## Sources

1. Wikipedia, "Polygraphia Nova" — opened in full this run (structure, counts, Ferdinand III origin, Selenus/Tironian lineage, Caramuel letter, arca errors; underlying scholarship: Fletcher, *A Study of the Life and Works of Athanasius Kircher*, Brill).
2. Krämer/Steinmetz-type survey: "Kaspar Schott's 'encyclopedia of all mathematical sciences'," *Poiesis & Praxis* (Springer, DOI 10.1007/s10202-011-0090-1) — opened via search result; Kircher-Lullism + universal-branding evidence.
3. EMLO, Bodleian: Correspondence of Athanasius Kircher catalogue entry referencing "Kircher's universal polygraphy" (search-result metadata only — not deep-read).
