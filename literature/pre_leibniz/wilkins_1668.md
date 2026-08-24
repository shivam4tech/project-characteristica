# John Wilkins — An Essay towards a Real Character and a Philosophical Language (1668)

**Gate ruling: PASS (high confidence)** — criteria G1, G5, G6, G8 (machine-relevant design principles: self-interpreting characters, canonical IDs), G9. Ruling basis: `gate_rulings.md`.

## Relevance justification

The *Essay* is the most fully engineered pre-Leibniz representational artifact: a 40-genus taxonomic tree of everything, rendered into syllabic characters whose form decomposes along the definition path, plus a matching spoken language and grammar. It is the reference comparator for Leibniz's characteristica discussions and the direct ancestor of "canonical identifier + typed taxonomy" designs. Studied as mechanism (tree → character formation → transcription tables), not biography.

## Protocol §2 extraction

| Field | Content | Source | Conf. |
|---|---|---|---|
| **Objective** | A real character (written signs denoting things/concepts directly, not words of any natural language) plus a philosophical language matching it; remedy the "curse of Babel" and standardize scientific nomenclature in the Royal Society milieu. | Essay structure; historiography via aidaneid site citing Slaughter 1982 | high |
| **Primitive units** | 40 genera spanning "Transcendental, Substance, Accident" (full genus list reproduced from Essay p.23: Things, Word/Discourse, Creator, World, Element, Stone, Metal, Herb-types ×4, Tree, Insect, Fish, Bird, Beast, Parts/Magnitude/Space/Measure under Quantity, Natural Powers … up to XL Ecclesiastical Relation) → subdivided into differences → species. Counts per modern tabulation: 59 genera incl. sub-entries, 310 differences, 3,820 radicals, of which 2,036 species (site tally incl. oppositions/affinities; headline traditional count: ~40 genera / 252 differences / ~2030 species). | aidaneid.github.io reproduction of Essay p.23 + its counts page (opened); Google Books scans of Essay pp.395, 404 linked there | high |
| **Representation mechanism** | Syllabic characters: initial letters/syllable encode genus, next marks difference, final marks species; separate short strokes for 48 grammatical particles; opposite notions get systematic character inversion; pronunciation mirrors inscription (character is speakable). Transposition tables handle proper names/eccentric terms cipher-style. | aidaneid site (characters/pronunciation pages, opened summary view); Essay p.23 table | med-high |
| **Composition mechanism** | Concatenation mirrors taxonomic descent — a character visually/audibly decomposable into its full definition path ("self-interpreting characters," Ward's program executed). Compound notions = composed radicals + particles. | Ward quotation in OUP intro lines 665–674 (program Wilkins executes); aidaneid pages | high |
| **Inference mechanism** | None formal. Value claimed is translational/transcriptive regularity, not proof; a grammar volume handles syntax separately. | My analysis | high |
| **Ambiguity handling** | Uniqueness by construction: one concept ↔ one character within the tables; homonymy/polysemy suppressed by assigning each sense its own species slot. Residual ambiguity re-enters where nature resists the tree (contested differentiae). | My analysis; Borges' critique below | med |
| **Extensibility** | Prepared mechanisms: radical slots for "eccentrics," transposition ciphers for names, affixes for derivatives — but new *kinds* require tree surgery, which cascades through characters. | My analysis | med |
| **Claimed universality** | The tables enumerate "all" things/kinds; the character suffices for international written communication independent of tongue. | Essay title/promises; historiography | high |
| **Known limitations** | Taxonomy arbitrariness (Borges: "there is no classification of the universe that is not arbitrary and conjectural"); empirical taxonomy abandoned it — John Ray compiled species tables under Wilkins' scheme then turned to empirical systematics instead (Language Log discussion of Borges essay, comment thread w/ Wilson citation); unwieldy pronunciation; adoption ≈ zero. | LanguageLog p.49359 (opened via search result); Borges essay linked therein | med-high |
| **Failure mode** | Naturalist-semantics collapse: forcing all kinds into one contested tree makes maintenance cost unbounded and every revision a rewrite — the canonical failure mode of totalizing ontologies. Also learnability ceiling: even enthusiasts needed the folio at hand. | Synthesis | high |
| **Modern analogue** | Wikidata QIDs / DBpedia URIs as "real characters" (language-neutral canonical IDs whose composition encodes type paths); WordNet/YAGO taxonomies; faceted classifications; Dewey-style notational systems. Wilkins' bet = canonical IDs reduce ambiguity and translation overhead — exactly testable today. | My analysis | med |
| **Candidate experimental implication** | Wilkins-arm pilot: replace entity mentions in prompts with canonical typed IDs (QID-like) vs plain text vs Beck-style bare numeric codes; measure token cost, semantic fidelity, paraphrase robustness, cross-model portability. Prediction: IDs help disambiguation but pay an inventory/schema overhead — quantifying that trade IS the CE-01 question in miniature. | My analysis | low |

## Documented reception (G9)

- Standard point of comparison in Leibniz scholarship on universal characters; Leibniz's era knew the Essay. ⚠ Exact Leibniz locus (New Essays III discussions) to be pinned by the Leibniz Researcher — confidence medium pending citation.
- Reception inside natural history documented (Ray episode above) — influence beyond language design.

## Sources

1. Aidan Wakely-Mulroney, "The Universal Language of John Wilkins" (aidaneid.github.io) — general-scheme page reproducing Essay p.23 (40 genera, opened this run), counts page (59/310/3820/2036, citing Slaughter 1982 p.177 for Paschall's 1678 revision proposal).
2. Liberman, M., Language Log post 49359 (1 Dec 2020) quoting Borges, "El idioma analítico de John Wilkins" — arbitrariness critique; Ray anecdote in comments.
3. Primary text locations verified via linked scans: Google Books, *An Essay Towards a Real Character* pp. 23, 395, 404.
