# Ramon Llull — Ars Magna / Ars generalis ultima (c.1305–1308)

**Gate ruling: PASS (high confidence)** — criteria G1 (representation primitives), G4 (combinatorial generation), G9 (documented influence on Leibniz). Full ruling: `gate_rulings.md`.

## Relevance justification

The Art is a concept-alphabet plus a mechanical combination engine aimed at generating and testing propositions in every field — i.e., representation primitives + combinatorial generation, exactly the mechanisms CE-01's genealogy targets. Influence is documented, not assumed:

- Leibniz's *Dissertatio de arte combinatoria* (1666) works inside the ars combinatoria genre descended from Llull; the DAC's own introduction situates it against the Lullist tradition (OUP intro, `sources/oup_dac_intro.txt` lines 585–588: "Ramón Lull … credited as a founding father of combinatory and as a source for Leibniz's ideas on combinatorial art").
- Transmission channel documented: Alsted's *Clavis Artis Lullianae* (1609), "well-known to the young Leibniz" (OUP intro lines 691–693, 707–723); Seth Ward's 1654 statement of the program quotes the resolve-concepts-to-symbols logic (OUP intro lines 661–674).
- The DAC itself cites a commentary on the *Ars magna* (Loemker DAC translation, `sources/loemker_dac.txt` line ~409: Bernhard Lavintheta's commentary on the Ars magna of Lully).

## Protocol §2 extraction

| Field | Content | Source | Conf. |
|---|---|---|---|
| **Objective** | A "science of all sciences": general art to answer questions and produce new truths in every field *without appeal to authority*; originally built for interfaith persuasion (ars iudicandi + ars inveniendi). | OUP intro pp.7–8 (lines 589–624); SEP §5.7.4 (Ars generalis ultima 13–2/13–3: solve problems "by providing reasons according to the process of this art") | high |
| **Primitive units** | Fixed lettered alphabets: nine absolute principles (goodness, greatness, eternity, power, wisdom, will, virtue, truth, glory — divine-dignity derived), nine relative principles (difference, concordance, contrariety, beginning, middle, end, majority, equality, minority), ten questions, subjects (God, angel, man, …), virtues/vices. Letters B,C,D,… stand 1:1 for these. | OUP intro lines 589–597 ("first concepts … nine in number … properties of God"); SEP §§3.1, 5.1–5.2 | high |
| **Representation mechanism** | Latin-alphabet letters denote concepts; combinatorial figures (A, S, T, V, X-Y-Z) drawn as circles/triangles with connecting chords externalize the allowed pairwise/ternary relations between principles. Meaning is fixed by the Art's own *definitions* section, not by usage. | SEP §5.1 ("components … definitions, principles, rules, figures, and alphabet") and §5.2 figure descriptions | high |
| **Composition mechanism** | Rotating concentric discs ("circles") around an axle generate all combinations of letters across discs (binary mixtions with two circles, ternary with three, …); the *tabula generalis* crosses question × subject × principle to form terms and propositions. Composition = exhaustive cross-product of the alphabets. | OUP intro lines 589–617; SEP §5.2 | high |
| **Inference mechanism** | Concordance-testing: each letter takes a place/role (e.g., agent vs actee in Figure T's triangles); a combination is accepted when the assigned principles are concordant and rejected when contrary. Validity is checked against the Art's definitional network, not experience. Questions (utrum, quid, quare…) drive application treatises. | SEP §§5.2.1–5.2.4, 5.7.4; OUP intro line 618–620 ("manipulating a few discs … discover new truths") | medium |
| **Ambiguity handling** | Eliminated by fiat: each letter has exactly one definition inside the Art; no homonymy admitted. Ambiguity reappears whenever real-world referents outrun the definitions. | SEP §3.1 definitions practice | medium |
| **Extensibility** | Application treatises (*Ars medicinae*, etc.) re-map the same alphabet onto new domains; the primitive set itself is closed and theological — new subject matter must be forced through the existing nine-plus-nine principles. | OUP intro lines 621–624; SEP §5 (quaternary vs ternary phases) | high |
| **Claimed universality** | All complex concepts of all created things reproducible from the first concepts; general theory of principles of all sciences, "intermediate between logic and metaphysics." | OUP intro lines 616–624 | high |
| **Known limitations** | Primitives chosen a posteriori from Christian theology; combinatorics enumerates symbol pairs, not senses; no syntax beyond pairing/placement; acceptance depends entirely on granting the definitions; empirically sterile outside theology/law-style topical reasoning. | OUP intro lines 625–631 (17th-c. critics saw scholastic logic as too formal; Lullists answered with "real properties"); SEP §5.7 | medium |
| **Failure mode** | Combinatorial generation without semantic grounding: exhaustive mixing yields plausible-looking pairings whose truth is untested — mechanical concordance ≠ validity. Coverage-by-permutation substitutes for content. | Synthesis of above (my analysis) | medium |
| **Modern analogue** | Exhaustive attribute-cross-product generation in symbolic AI (feature-grid enumeration, early semantic-network combination engines); a-priori-top-ontology coverage strategies (Cyc-style) that fix primitives first and force domains through them; mechanically, the rotating discs are a hardware implementation of itertools.product over a closed concept inventory. | My analysis; OUP intro framing of Lullism→encyclopedism→universal language triad | medium |
| **Candidate experimental implication** | Restricting an LLM's intermediate vocabulary to a small declared principle set with role slots (Llull-style) should help *only* where the task genuinely decomposes into those primitives (theology-like closed domains) and hurt on open-domain tasks. Pre-registerable as: closed-primitive constrained decoding vs free-text on closed-taxonomy QA vs open QA; measures accuracy and semantic-fidelity trade-off. | My analysis (feeds hypothesis registry via Historical Foundations Lead) | low |

## Sources

1. Priani, E., "Ramon Llull," Stanford Encyclopedia of Philosophy (2025), §§3.1, 5.1–5.2, 5.7.4 — cached full text: `/home/shivam/.hermes/cache/web/plato.stanford.edu-9be5705928.md`.
2. Mugnai, M., Introduction to G.W. Leibniz, *Dissertatio de Arte Combinatoria* (OUP, corrected proof 2020), pp. 7–10 — local: `literature/pre_leibniz/sources/oup_dac_intro.txt` lines 585–723.
3. Loemker, Leroy (trans.), Leibniz's DAC — local: `sources/loemker_dac.txt` line ~409 (Lull commentary citation).
