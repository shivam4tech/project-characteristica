# Post-Leibniz Formal Systems — Protocol §2 Extractions (CE-01 / WS-POSTL)

Worker: W17-POSTL (Post-Leibniz / Formal Systems Researcher, ORGANIZATION.md §7)
Date: 2026-08-24 · Status: IN PROGRESS (write-as-you-go)

Method note: One Protocol §2 extraction per system, written immediately after studying that system
(checkpoint discipline, WORKER_BRIEF_COMMON.md). Every claim carries a finding label (LAB_CHARTER.md
authorized set), a source opened and inspected (Protocol §1 — search snippets alone are not evidence),
and confidence. Each extraction answers the worker-specific questions: which Leibnizian ambition was
preserved vs abandoned, what problem forced the abandonment, what limitation remains today.

Leibnizian baseline used throughout (from the charter/RESEARCH_QUESTION framing, pending the Leibniz
Researcher's deeper extraction in `literature/leibniz_extraction.md`): the characteristica universalis /
calculus ratiocinator package bundles several separable ambitions —

- **A1 lingua characterica**: a written language whose expressions *display* the conceptual content of
  thoughts (not merely encode them), suitable for expressing any human thought;
- **A2 calculus ratiocinator**: inference as calculation — disputes settled by "Calculemus!";
- **A3 alphabet of human thoughts**: a finite inventory of primitive concepts from which all others compose;
- **A4 universality of scope**: covering *all* human reasoning/knowledge, not one domain;
- **A5 usability**: a script humans can actually read/write fluently (Leibniz stressed ease of the
  characters, cf. his remarks on Chinese characters and on the deaf/mute learning by characters).

Historical caveat (to be reconciled with W9-LEIBNIZ): whether A1 and A2 were one project or two readings
of Leibniz is exactly what the Frege–Schröder polemic contested (see §0 below).

---

## Source register (local to this file; Curator may promote to BIBLIOGRAPHY.md)

| ID | Citation | Type/Tier | Where examined | Reliability |
|---|---|---|---|---|
| S-P1 | Frege, G. (1879), *Begriffsschrift*; Eng. trans. S. Bauer-Mengelberg in van Heijenoort (ed.), *From Frege to Gödel*, Harvard UP, 1967, pp. 5–82 | primary-text / primary | Preface + van Heijenoort's introduction, via archive.org scan (`gottlob-frege-begriffsschrift-english`) | high |
| S-P2 | Bertran-San Millán, J. (2021), "Lingua characterica and calculus ratiocinator: The Leibnizian background of the Frege–Schröder polemic", *Review of Symbolic Logic* 14(2), June 2021 | paper / peer-reviewed / secondary | Title, abstract, §1 (via author-hosted PDF) | high |

---
## §0. Context: the lingua characterica vs calculus ratiocinator polemic [Historical Claim]

**Claim.** After the publication of *Begriffsschrift*, Frege and Ernst Schröder accused each other of
having produced "merely a calculus ratiocinator," each claiming his own system as the better realization
of Leibniz's ideal language. This was not a squabble over notation but a genuine fork in how one reads
the Leibnizian package — and it recurs in every post-Leibniz system below.
Source: S-P2 (title/abstract/§1); confidence **high**.

What the fork consists of (per S-P2):
- **Schröder's reading** — logic first as *calculus*: Schröder's construction of the algebra of relatives
  fits a project of reducing any mathematical concept to the notion of relative (binary relation);
  from that stance he judged the formal system of *Begriffsschrift* incapable of such reduction, hence
  "a mere calculus ratiocinator" in reverse — an unusable calculus without algebraic power.
- **Frege's reading** — logic first as *language*: Frege took Boolean logic to be an abstract logical
  theory inadequate for rendering specific scientific content (it manipulates class/proposition terms
  while their inner structure stays opaque); he demanded a script that *displays* conceptual content.
- Crucially (S-P2): even Frege's *Begriffsschrift* "did not constitute a complete lingua characterica
  by itself" in Frege's own view — it was a tool to be applied discipline by discipline; and Frege's
  lingua-characterica ambition was independent of his later logicist programme.
- Van Heijenoort (1967b) canonized the two sides as "logic as language vs logic as calculus"; S-P2's
  contribution is showing both men claimed BOTH ideals and each found the other's realization wanting.

[Observation, conf. med] The polemic therefore already shows the Leibnizian package is *decomposable*:
its language half (displaying content) and its calculation half (mechanical inference) can be pursued,
and evaluated, separately. Every system below picks a point on this trade-off surface. This decomposition
is directly relevant to H1/H0: a modern SIR proposal must state which half it optimizes and pay for the other.

Interpretation for CE-01: the historical record treats "universal language" and "inference calculus" as
separable deliverables whose unification was attempted at most twice (Frege's *Begriffsschrift*; arguably
Leibniz himself) and never stabilized. Relevance: Operational Questions 1–2, 9.

---

## §1. Gottlob Frege, *Begriffsschrift* (1879) [Historical Claim]

**Protocol §2 extraction.** Sources: S-P1, S-P2; confidence **high** unless marked otherwise.

| Field | Extraction |
|---|---|
| objective | A *Begriffsschrift*, "formula language of pure thought modelled upon the language of arithmetic": a script that makes logical form visible so that any dispute can be decided by checking a written derivation (A2), while *displaying* rather than merely encoding the function/argument structure of thoughts (partial A1). |
| primitive units | Object vs. concept/function; the judgeable content; the judgment (content stroke + judgment stroke); identity; negation and the conditional as the two basic operations on contents; *generality* introduced by the concavity-with-German-letter device — i.e., quantification is primitive, not built from a variable-binding convention bolted onto syllogistic. |
| representation | Two-dimensional ideographic notation: arguments embedded under function signs in a branching 2-D layout, so scope and subordination of concepts are visible spatially; linearization into ordinary print is lossy. |
| composition | Function/argument composition throughout: a concept is a function from objects to truth values; nested embeddings express multiple generality and relational structure (ancestral defined in §26 of BS as a second-order construction). |
| inference | Axiomatic-deductive: small set of basic laws + substitution/modus ponens; proofs drawn as vertical trees where every line names its premises — inference becomes checkable calculation (A2 delivered). |
| ambiguity handling | Eliminated by construction: every sign gets its meaning by explicit introduction; no equivocation possible inside the script; scope is graphic, not conventional. |
| extensibility | By definition within the script, discipline by discipline — arithmetic first (*Grundlagen*/*Grundgesetze*). Per S-P2: Frege held BS "did not constitute a complete lingua characterica by itself"; it is an instrument to be *applied*. |
| claimed universality | "Pure thought" as such — maximal logical universality — yet Frege's own practice narrows it to logic + mathematics; the A3 alphabet-of-thoughts project (decomposing *all* empirical concepts) is silently dropped. |
| known limitations | (i) Notation so unwieldy that even allies abandoned it (Russell/Peano re-notated); (ii) no equational/algebraic manipulation — Schröder's polemical charge that BS cannot reduce concepts to relatives (S-P2, §0 above); (iii) the system as extended in *Grundgesetze* is inconsistent (Russell's paradox). |
| failure mode | Adoption failure through usability (A5 sacrificed for expressive transparency), plus formal collapse at maximum strength. |
| modern analogue | First-order/predicate logic itself; the annotated proof-tree with explicit dependencies survives in proof assistants (Isabelle, Lean, Coq). |
| candidate experimental implication | Testable display-vs-encode claim: does a representation whose surface structure mirrors compositional semantic structure (Fregean display) raise LLM reasoning fidelity vs. a flat/encoded format of equal information? Directly measurable under Protocol §5. |

**Preserved vs abandoned:** preserved A2 completely (first real calculus ratiocinator with relational
power); A1 partially (logical form displayed; empirical concepts untouched); abandoned A3 (no alphabet of
human thoughts), A4-in-Leibniz's-sense (all knowledge reduced to logic+arithmetic only), A5 (usability).

**Forcing problem:** multiple generality and relational inference were inexpressible in both the syllogistic
catalog and Boolean equations; capturing them forced Frege to quantify over functions, which in turn
forced the 2-D display of function/argument structure — the very feature that made the script unlearnable
as a working language.

**Remaining limitation today:** nobody reasons *in* the notation; we reason in its linearized descendants.
The display half of Frege's ambition survives only inside machine-checked proofs, not in human-facing
scripts. [Observation, conf. med]

<!-- §1 end -->

## §2. Peano / Russell — Logicism and *Principia Mathematica* (1889–1913) [Historical Claim]

**Protocol §2 extraction.** Source: S-P4 (incl. Russell 1903 preface quoted there); confidence **high**.

| Field | Extraction |
|---|---|
| objective | Logicism: prove "that all pure mathematics deals exclusively with concepts definable in terms of a very small number of fundamental concepts, and that all its propositions are deducible from a very small number of fundamental logical principles" (Russell 1903: xv, quoted in S-P4). Universality re-scoped: not all thought, but all mathematics. Peano's complementary aim: a linear symbolic notation good enough for publishing rigorous mathematics. |
| primitive units | Propositions and propositional functions; classes; relations (PM built on a *logic of relations*, unlike Frege's function/object core); primitives reduced to negation, disjunction, universal quantification (+ identity); Peano's dots, ⊃, ∨, ~(x) conventions. |
| representation | Linear typographic notation deliberately optimized for typesetting and reading — the anti-Begriffsschrift choice on A5/usability. |
| composition | Explicit definitions ("definitions in use") plus the theory of descriptions: surface-denoting phrases are contextually defined away into quantified forms — composition proceeds by meaning-preserving paraphrase into canonical form. |
| inference | Axiom systems + formal rules; fully numbered derivations (∗1–∗563 across 3 volumes); famously hundreds of pages to reach ∗54·43 (1+1=2) — inference as industrial-scale calculation. |
| ambiguity handling | Contextual (paraphrastic) definition of descriptions; type discipline blocks grammatically well-formed but meaningless formulas ("the paradox is ruled out on the basis of the theory of types", S-P4). |
| extensibility | By definition within the system, but every extension must respect the ramified type hierarchy; impredicative steps require the axiom of reducibility. |
| claimed universality | All of pure mathematics from logic alone; explicitly NOT natural language or empirical science. |
| known limitations | Axioms of reducibility and infinity are needed and are widely disputed as logical truths (Wittgenstein/Ramsey line reported in S-P4); Gödel's incompleteness then caps the program formally; ~2000 pages for elementary arithmetic shows the usability ceiling. |
| failure mode | The base "logic" turns out to smuggle in substantive existence/comprehension assumptions — universality of the foundation collapses from inside. |
| modern analogue | Type-theoretic foundations (Church; Coq/Lean/Isabelle libraries); the definitional-from-primitives style survives in ontology engineering. |
| candidate experimental implication | Measure the *checkability overhead*: what fraction of an LLM's chain-of-thought can be upgraded to machine-checkable steps (PM-style derivation discipline) before token cost outweighs accuracy gains (Protocol §5/§6)? |

**Preserved vs abandoned:** preserved A2 at unprecedented scale, and A4 narrowed-but-honestly
(mathematics only); abandoned A1 entirely (Peano–Russell notation is conventional shorthand, nothing is
"displayed"), A3 (primitives are logical, not conceptual atoms of all knowledge), A5-in-full (still nobody
could work fluently in PM).

**Forcing problem:** Russell's own paradox forced stratification of the universe into types; ramification
then blocked ordinary mathematical induction until patched by reducibility + infinity axioms — so the price
of consistency was giving up the self-evidence ("logicalness") of the foundation. Consistency pressure, not
expressivity, is what broke the universal claim.

**Remaining limitation today:** no derivation of mathematics from *pure* logic exists (neologicism
continues with weaker claims); and the linear-notation choice settled the Frege–Schröder polemic by
fiat: modern logic is calculus-shaped syntax with none of the display ambition.

<!-- §2 end -->

## §3. Boole–Schröder Algebra of Logic (1847–1910) [Historical Claim]

**Protocol §2 extraction.** Sources: S-P3; S-P2 (polemic context). Confidence **high**.

| Field | Extraction |
|---|---|
| objective | Recast logic as symbolic algebra. Boole's three-step method (verbatim structure in S-P3): "1. Translate the logical data into suitable equations; 2. Apply algebraic techniques to solve these equations; 3. Translate this solution, if possible, back into the original language." Schröder's *Vorlesungen über die Algebra der Logik* (1890–1905) systematized this into a general algebraic theory and proposed the notation as a *pasigraphy* — a universal written scientific language (S-P3, citing Peckhaus/Legris). |
| primitive units | Classes under extensional semantics; operations ∩, ∪, complement; constants 0/1; from Peirce on, subsumption (≤) replaces equality as primitive; binary relations with composition and converse (Vol. III). |
| representation | Equations/negated equations over class-terms; laws as identities; strictly linear algebraic notation. |
| composition | Term formation by the algebraic operations only — no analysis of a class-term's inner conceptual structure (the opacity Frege attacked, cf. §0). |
| inference | Algorithmic manipulation: development/expansion theorems, Boole's Elimination Theorem (substitute 0/1 in all ways, multiply instances = 0); Schröder's parametric solution of relational equations (precursor of Skolem functions, S-P3). Inference is genuinely calculational — the strongest A2 delivery before PM. |
| ambiguity handling | None inside the calculus: natural language is translated manually; "if possible" in step 3 concedes that results may be *uninterpretable* — meaning lives outside the formalism. |
| extensibility | By algebraic generalization: Jevons' total operations, Peirce's subsumption lattices and Σ/Π quantifiers, Schröder's relatives; abstract axiomatization (Huntington), models (Stone). |
| claimed universality | Boole: a "science of reasoning" replacing the syllogistic catalog; Schröder: foundations of mathematics from the relation calculus + pasigraphic universality (S-P3, Brady). |
| known limitations | Partial operations and uninterpretable terms in Boole's original; Schröder proved equations alone cannot express "Some X is Y" (negated equations needed); distributivity subtleties (non-distributive lattices); expressive ceiling: relation algebra ≡ first-order logic with 3 variables (Korselt/Tarski-Givant, S-P3). |
| failure mode | Lost the institutional contest to PM-style logic after WWI (Hilbert switched camps, S-P3); its universal-language claim died while its mathematics thrived. |
| modern analogue | Boolean algebra (circuits, query optimization), relational algebra (SQL), Tarski & Givant *Set Theory Without Variables*; Skolem 1919 Horn-clause procedure anticipates Datalog (S-P3). |
| candidate experimental implication | Constraint-satisfaction probe: do LLMs satisfy constraints more reliably when given an algebraic/equational normal form than equivalent prose? Cheap Protocol §7 cross-task test. |

**Preserved vs abandoned:** preserved A2 maximally (inference as literal algebraic calculation) and a
partial A5 (linear, learnable notation); abandoned A1 (class terms are opaque — nothing displayed), A3
(classes are extensions, not conceptual atoms), A4-in-full (valid reasoning forms only, no world knowledge).

**Forcing problem:** mechanizing inference required reducing all content to extensional class operations;
that made the calculus powerful but severed the connection between derivational steps and conceptual
meaning — exactly the "merely a calculus ratiocinator" charge traded across the polemic (§0).

**Remaining limitation today:** the algebra survives everywhere as machinery, but as a *representation for
human thought* it was never resurrected; its quantifier-free, equation-only style cannot host ordinary
propositions without lossy manual translation.

<!-- §3 end -->

## §4. Carnap, *Logical Syntax of Language* (1934/1937) [Historical Claim]

**Protocol §2 extraction.** Source: S-P5 (SEP *Rudolf Carnap*, incl. LSS §17 quotation). Confidence **high**.

| Field | Extraction |
|---|---|
| objective | Philosophy recast as "the logical syntax of the language of science": design and compare formal languages instead of searching for the correct world-language. Note the arc (S-P5): Carnap's *Aufbau* project was explicitly a "Leibnizian, deductive system of knowledge … unified *deductively*, as Leibniz—and Frege—had envisaged"; LSS begins as the search for a *single standard language of science*. |
| primitive units | Purely syntactic items: symbols, formulas, derivation rules, formation/transformation rules; logical vs. descriptive vocabulary; the two worked-out exemplars Language I (constructivist/finitary) and Language II (classical). |
| representation | A language IS its syntax — everything about meaning, reference, truth is bracketed (semantics admitted only in the 1940s turn reported by S-P5). |
| composition | Formation rules inside each language; cross-language relations handled as definability/translatability statements in a metalanguage. |
| inference | Each language carries its own consequence relation; there is no privileged logic to import. |
| ambiguity handling | Philosophical disputes dissolved by translating them into the "formal mode of speech" (statements about words, not things); pseudo-problems diagnosed as syntactic confusions. |
| extensibility | Institutionalized: the **principle of tolerance** — "In logic there are no morals. Everyone is welcome to set up his logic, i.e., his form of language, as he pleases" (LSS §17, quoted in S-P5). |
| claimed universality | The old universality is *renounced*: S-P5 states outright that "this new pluralism undermined the initial premise of the entire Syntax book". What remains universal is the *metalogical* standpoint — any proposed language form falls under general syntax. |
| known limitations | Syntax cannot recover truth/reference/meaning (hence Carnap's own later semantic turn); tolerance supplies no criterion for choosing among frameworks; Gödelian results (which S-P5 notes shaped LSS) show a fixed object language cannot host its own consistency/truth apparatus. |
| failure mode | Self-subversion: the programme launched to find the language of science ends certifying that no such unique language exists; choice becomes pragmatic, external to logic. |
| modern analogue | Programming-language and schema ecosystems: JSON-Schema/OpenAPI/protobuf-style pluralism, DSL proliferation, formal-methods stacks — engineering tolerance without a canon. |
| candidate experimental implication | Treat representation comparison itself as the deliverable: run identical tasks through ≥2 candidate representations and report per-framework trade-offs (Protocol §§7–8) — Carnapian tolerance operationalized as benchmarking protocol. |

**Preserved vs abandoned:** preserved A2 (each language still a calculus) and A4 only in metamorphosed,
metalogical form (universality of the *theory of languages*, not of a language); abandoned A1 entirely
(syntax displays nothing about content), A3 (no conceptual alphabet), the *single*-language ideal of
Leibniz's characteristica, and A5-as-human-usability (languages built for science, not fluency).

**Forcing problem:** two pressures converged: (i) Gödel/Tarski — no sufficiently rich fixed language can
contain its own semantic machinery, so "the" universal language is impossible from within; (ii) the
existence of rival consistent logics made any prohibition arbitrary — hence conventions without morals.

**Remaining limitation today:** framework-choice has no rational criterion even now (S-P5 documents the
still-live regress problem for choosing frameworks); every representation project inherits this gap.

<!-- §4 end -->

## §5. Attempto Controlled English (ACE, 1990s–present) [Historical Claim]

**Protocol §2 extraction.** Sources: S-P6 (Fuchs et al., Reasoning Web 2005 school chapter — opened in full);
S-P7 (Fuchs 2016, *Reasoning in ACE: Non-Monotonicity*, CNL workshop — abstract + conclusions inspected).
Confidence **high**.

| Field | Extraction |
|---|---|
| objective | A knowledge-representation language "with an English syntax … readable by humans and machines": a "precisely defined subset of full English that can automatically and unambiguously be translated into full first-order logic" (S-P6). Used as specification language, KR language, and interface to formal systems. |
| primitive units | Predefined function words + user-defined content words; sentences of form subject + verb + complements + adjuncts; composite sentences by coordination/subordination/quantification/negation; yes/no and wh-query sentences; anaphora restricted to previously introduced NPs. |
| representation | Attempto Parsing Engine maps each text deterministically to a **discourse representation structure** (Kamp & Reyle), a variant of FOL in a *flat/reified* notation: few predefined predicates (`object`, `property`, `predicate`, `quantity`…) with word constants as arguments. |
| composition | Text = sequence of interrelated sentences accumulated into ONE fixed discourse context; "No further context exists" (S-P6). Plurals handled by lattice-theoretic group objects inside extended DRSs. |
| inference | External reasoner **RACE** (Otter/Satchmo core): consistency checking, theorem deduction, query answering, each proof justified back in ACE. Expressive power ≡ FOL; later non-monotonic add-ons (negation-as-failure, defaults, abduction) per S-P7. |
| ambiguity handling | Three documented means (S-P6): (1) ambiguous constructs excluded, unambiguous alternatives provided; (2) remaining constructs interpreted deterministically by a few rules; (3) user accepts the assigned reading or rephrases. E.g. ACE has no passive voice at all. Every sentence treated as unambiguous even if readers perceive otherwise. |
| extensibility | Lexicon extensible via editor; BUT "the Attempto system is not associated with any specific application domain … By itself it does not contain any knowledge of application domains, of formal methods, or of the world in general. Thus users must explicitly define domain knowledge … Words … are processed … as uninterpreted syntactic elements" (S-P6). |
| claimed universality | Universality redefined: not all thought, but all *FOL-expressible* content under an English-like surface. A4 survives only as "equivalent to full first-order logic." |
| known limitations | Learnability admitted: "ACE seems completely natural, but is in fact a formal language that must be learned" (1–2 days for rules, more for fluency — S-P6); imperatives and `should`/`may` modals have no logical representation in the reasoner (S-P7); RACE's auxiliary axioms raise "what RACE should actually deduce … may be highly debatable" (S-P7). |
| failure mode | Authoring-burden adoption trap: the language's honesty about being formal means writers still carry the formalization load; project stayed academic-niche despite semantic-web ambitions (S-P6 conclusion). |
| modern analogue | Other CNLs (PENG ASP, SBVR, ACE-based AceWiki/AceRules); and implicitly every structured-prompt / schema-prompt scheme offered to LLMs — ACE is the cleanest historical prototype of "structured input that models can parse." |
| candidate experimental implication | ACE-style CNL as a *baseline arm* in our experiments: compare ordinary-NL prompt vs optimized-NL vs CNL vs JSON on accuracy + token cost + paraphrase robustness (Protocol §§4–6). ACE literature already reports the learnability cost we must amortize per §6. |

**Preserved vs abandoned:** preserved A5 better than any system since Leibniz himself (genuine
human-readability) and A2 up to FOL equivalence; abandoned A4 (explicitly a subset; zero world knowledge),
A3 (content words uninterpreted — the alphabet-of-thoughts idea inverted: syntax universal, lexicon
user-supplied), and A1 (meaning lives in the DRS, not in displayed surface).

**Forcing problem:** deterministic, unambiguous machine translation was impossible over full English;
tractable parsing + decidable-enough reasoning forced the controlled subset, and the residual ambiguities
were legislated away by fiat interpretation rules rather than resolved semantically.

**Remaining limitation today:** the human still does the formalization — ACE moves, rather than removes,
Leibniz's analysis burden; and 30 years on there is no large-body usage demonstrating fluent writing at
scale.

<!-- §5 end -->

## §6. UNL — Universal Networking Language (1996– ) [Historical Claim]

**Protocol §2 extraction.** Sources: S-P8 (Boguslavsky et al., COLING 2000 — ETAP-3 UNL module paper,
opened in full); S-P9 (UNDL Foundation, UNLwiki *Universal Words*, official documentation, opened).
Confidence **high**.

| Field | Extraction |
|---|---|
| objective | Interlingua to "break down or at least drastically lower the language barrier for the Internet users" (S-P8): encode each document once in UNL, deconvert into any natural language. Launched under UN University auspices, 1996, proposed by H. Uchida. |
| primitive units | **Universal Words** (nodes): English-label concepts with constraint suffixes (`bucket(icl>container)`), internally numeric-ID'd, permanent vs temporary; **Universal Relations** (binary labelled arcs: agt, obj, tim…); **Universal Attributes** (`@past`, `@entry`…) for grammatical categories (S-P9). |
| representation | Directed graph/hypergraph per text; closed-class meanings become attributes/relations, open-class meanings become UWs; non-lexicalizable concepts expand into sub-graphs ("hyper-nodes"); unsaturated deixis gets pro-UW `00` (S-P9). |
| composition | Graph composition governed by an **UNL Knowledge Base** defining admissible binary relation pairs — the KB "is expected to map everything that we know about the world" (S-P9, their own words). Closest living mutation of Leibniz's A3 alphabet-of-thoughts. |
| inference | **None.** UNL ships no consequence relation, no proof procedure — pure representation/interchange format. All "processing" happens in per-language converters using external machinery (ETAP-3 needed its full MT stack + lexical functions just to realize one relation as a preposition, S-P8). |
| ambiguity handling | Explicitly *not* automated: "the procedure of producing a UNL text is not supposed to be fully automatic … an interactive process with the labor divided between the computer and a human expert ('writer') in UNL" who corrects errors and eliminates residual ambiguities (S-P8). |
| extensibility | New temporary UWs freely creatable; universality redefined as "uniform identifiers" usable by all, NOT semantic primitives common to all languages (S-P9 — explicit departure from A3-as-primitives). |
| claimed universality | Maximal of any system here: sufficient expressive power for "relevant information conveyed by natural languages," targeting all UN member languages (S-P8). |
| known limitations | Enconversion quality bottleneck; English-biased labels; no semantics of inference; the KB-completeness assumption is heroic; after the UNU/IAS phase the programme shrank to foundation/maintenance status with no large deployed corpus. |
| failure mode | Economic collapse of human-in-the-loop encoding: interactive writer-editing makes per-document cost scale like skilled translation, destroying the original value proposition. |
| modern analogue | AMR/UMR abstract meaning representations; RDF/knowledge-graph interchange; today's neural "pivot/interlingua" claims in multilingual LLMs. |
| candidate experimental implication | Round-trip fidelity protocol: encode → decode → score semantic fidelity against source (Protocol §5 metric). UNL history predicts loss concentrates in saturation/context-dependent material — testable with LLM-based encoders. |

**Preserved vs abandoned:** preserved A4 as the *boldest* claim on record (all natural-language content),
A1 weakly (graphs do display relational structure), and a transformed A3 (KB-indexed UWs as the
alphabet of thought — minus the claim that primitives are shared across languages); abandoned A2
completely — the only system in this file with NO calculus — and A5 (raw UNL is unreadable without
tooling).

**Forcing problem:** automatic high-quality enconversion from arbitrary NL proved out of reach; the
salvage move — certified human UNL "writers" — traded the automation dream for editorial labour, which
then killed adoption. The interlingua was never the bottleneck; getting *into* it was.

**Remaining limitation today:** inherited intact by AMR: no reliable autonomous encoder exists; every
interlingua proposal since faces the identical conversion-economics wall.

<!-- §6 end -->

## §7. Description Logics / OWL (1980s–present) [Historical Claim]

**Protocol §2 extraction.** Sources: S-P10 (W3C *OWL 2 Primer*, Second Edition, W3C Recommendation —
opened); S-P11 (Baader & Nutt, "Basic Description Logics", *DL Handbook* ch. 2 — key passages inspected).
Confidence **high**.

| Field | Extraction |
|---|---|
| objective | A "computational logic-based language" for web knowledge: represent "rich and complex knowledge about things, groups of things, and relations between things" so programs can "verify the consistency of that knowledge or … make implicit knowledge explicit" (S-P10). The calculus ratiocinator reborn as a network service. |
| primitive units | Classes, object/data properties, individuals, datatypes; TBox terminological axioms vs ABox assertions (DL inheritance per S-P11). |
| representation | Ontologies serialized in multiple syntaxes over global IRIs; formal model-theoretic semantics in two views: OWL 2 DL (decidable) vs OWL 2 Full (S-P10 §9). |
| composition | Concept constructors: intersection/union/complement, existential/universal restrictions (`someValuesFrom`/`allValuesFrom`), cardinality, role chains; subsumption hierarchy is *inferred from definitions*, not asserted IS-A links ("unlike IS-A links in Semantic Networks … subsumption relationships are inferred", S-P11). |
| inference | Decidable reasoning services: classification/subsumption, instance checking, consistency, entailment — tableau-family reasoners (HermiT/Pellet/FaCT++ lineage). Inference is calculation again, but only within the chosen expressive fragment. |
| ambiguity handling | Not resolved — made exact and partial: open-world assumption (missing info ≠ false), no unique-names assumption ("OWL does not make the assumption that different names are names for different individuals", S-P10). Ambiguity is pushed into ontology engineering choices. |
| extensibility | Three tractable profiles — EL (big terminologies), QL (query/RDF-friendly), RL (rule/forward-chaining-friendly) — a Carnapian tolerance internalized inside one standard (S-P10 §10); rules via SWRL live outside the decidability guarantee. |
| claimed universality | Universal scope claim re-scoped once more: all *machine-processable world knowledge*, not thought. Expressive power deliberately bounded by the "trade-off between the expressivity of DLs and the complexity of their reasoning problems … one of the most important issues in DL research" (S-P11). |
| known limitations | Monotonic only: no defaults, closed-world or non-monotonic reasoning, uncertainty, or processes/actions in core OWL; worst-case complexity high (up to ExpTime); content vocabulary remains uninterpreted labels (URIs name, don't analyze — no A3); ontology-engineering burden on humans. |
| failure mode | Expressive adequacy vs tractability tension fragments the standard into profiles; adoption plateaued outside biomedicine; the LLM era largely routed around the symbolic stack entirely. |
| modern analogue | Knowledge graphs + SHACL shapes; biomedical ontologies (SNOMED CT ≈ EL profile); neuro-symbolic hybrids trying to bolt LLMs onto DL reasoners. |
| candidate experimental implication | Use DL reasoners as *ground-truth entailment oracles*: generate NL vs structured statements of identical facts, measure whether the structured form raises LLM entailment accuracy or merely shifts errors (Protocol §§4–5, §7 cross-task). |

**Preserved vs abandoned:** preserved A2 for a decidable fragment (the most successful realization of
Calculemus in this file) and A4 re-scoped to machine-processable knowledge at planetary scale; abandoned
A1 (nothing displayed), A5 (unreadable to non-logicians), A3 (labels without conceptual decomposition),
and — critically — Leibniz's single-language universality, traded away profile by profile for decidability.

**Forcing problem:** web scale demanded guaranteed-terminating, interoperable reasoning; undecidability
of unrestricted FOL forced the fragment-by-fragment design, i.e., the universality of scope was paid out
as the price of mechanical inference. This is the §0 trade-off surface rendered as W3C engineering.

**Remaining limitation today:** monotonicity + uninterpreted vocabulary + human authoring cost; the same
analysis-burden wall that stopped UNL and ACE, now with a reasoner attached.

<!-- §7 end -->

---

## §8. Synthesis across the seven systems [Observation, conf. med]

Reading §1–§7 against the A1–A5 grid of the header:

1. **No system maximizes more than two ambitions.** Frege: A2+A1(partial). Boole–Schröder: A2+A5(partial).
   Peano–Russell: A2 only. Carnap: A2 + metalogical-A4. ACE: A5+A2(≤FOL). UNL: A4+A1(graph display).
   DL/OWL: A2(decidable fragment)+A4(machine knowledge). The §0 trade-off surface is empirically
   confirmed as a *forcing structure*, not a matter of taste or era.
2. **The recurring killer is conversion/authoring economics, not formal weakness.** UNL needed certified
   human writers; ACE admits being "a formal language that must be learned"; OWL needs professional
   ontology engineers; even PM took hundreds of pages for 1+1=2. Every system that demanded humans
   internalize the representation failed to scale; every system that survived does so as machinery
   (Boolean algebra, SQL, reasoners), not as language.
3. **A3 (alphabet of human thoughts) has no successful heir in 250 years** — dropped by Frege, absent in
   PM, forbidden by Carnap's tolerance, inverted by ACE (uninterpreted content words), mutated into UNL's
   KB-indexed UWs and stalled there. Per Protocol §3, any SIR proposal resting on primitive-concept
   decomposition carries this prior-art record and must answer it explicitly.
4. For H1/H0: the historical record predicts our experiments will find gains concentrated where a
   representation *pays* for what it abandons (e.g., structured formats may help machine checking while
   costing tokens and paraphrase robustness). Protocol §§5–6 metrics map exactly onto the axes above.

---

### Source register additions (this continuation; IDs cited in §1–§7)

| ID | Citation | Type/Tier | Where examined | Reliability |
|---|---|---|---|---|
| S-P3 | Burris, S. & Legris, J., "The Algebra of Logic Tradition", *Stanford Encyclopedia of Philosophy* (subst. rev. Feb 2021) | encyclopedia / reputable secondary | Full entry incl. §1–§7, §10–§11 via plato.stanford.edu | high |
| S-P4 | Linsky, B. & Irvine, A.D., "*Principia Mathematica*", *Stanford Encyclopedia of Philosophy* (rev. Mar 2026); quoting Russell 1903, xv | encyclopedia / reputable secondary | Overview + §1–§2 via plato.stanford.edu | high |
| S-P5 | Leitgeb, H. & Carus, A., "Rudolf Carnap", *Stanford Encyclopedia of Philosophy* (rev. Jul 2026); quoting Carnap, *LSS* §17 | encyclopedia / reputable secondary | §§1.1–1.3, §4 area via plato.stanford.edu | high |
| S-P6 | Fuchs, N.E., Höfler, S., Kaljurand, K., Rinaldi, F., Schneider, G. (2005), "Attempto Controlled English: A Knowledge Representation Language Readable by Humans and Machines", Reasoning Web Summer School 2005 | paper / peer-reviewed venue | Opened in full via attempto.ifi.uzh.ch PDF (cached) | high |
| S-P7 | Fuchs, N.E. (2016), "Reasoning in Attempto Controlled English: Non-Monotonicity", CNL 2016 workshop | paper / workshop | Abstract, proof sketch, conclusions via attempto.ifi.uzh.ch PDF text | med-high |
| S-P8 | Boguslavsky, I., Frid, N., Iomdin, L., Kreidlin, L., Sagalova, I., Sizov, V. (2000), "Creating a Universal Networking Language Module within an Advanced NLP System", COLING 2000 | paper / peer-reviewed | Opened in full via MT Archive PDF (cached) | high |
| S-P9 | UNDL Foundation, "Universal Words", UNLwiki official documentation | official technical documentation | Page opened via unlarchive.org (cached) | high |
| S-P10 | Hitzler, P., Krötzsch, M., Parsia, B., Patel-Schneider, P.F., Rudolph, S. (eds.) (2012), *OWL 2 Web Ontology Language Primer* (2nd ed.), W3C Recommendation | official technical documentation / standard | Head + §9/§10 references + unique-names passage via w3.org (cached) | high |
| S-P11 | Baader, F. & Nutt, W., "Basic Description Logics", ch. 2 of Baader et al. (eds.), *The Description Logic Handbook*, CUP 2003 | book chapter / peer-reviewed | Key passages (expressivity–complexity trade-off; inferred vs asserted subsumption) via handbook copies online | high |

---

## Worker report (W17-POSTL continuation)

- **hours_spent:** ~1.4 of 1.5 budget (source gathering ≈ 35 min; writing §1–§8 ≈ 50 min).
- **files_written:** `literature/post_leibniz/formal_systems_extraction.md` only — appended §1–§7 extractions,
  §8 synthesis, register additions S-P3…S-P11, this report (67 → ~380 lines; existing content untouched).
- **top_findings:**
  1. All seven systems confirm the §0 fork as a hard trade-off: none preserves display (A1) + full calculus
     (A2) + universality (A4) together; OWL is the cleanest case of buying decidability by fragmenting scope.
  2. The dominant failure mode across eras is **conversion/authoring economics** (UNL writers → ACE learning
     curve → ontology engineering), making Protocol §6 overhead accounting the historically validated metric.
  3. A3 (alphabet of thoughts) has no surviving realization; UNL's UW+KB was its last serious mutation.
     Prior-art exposure for any Characteristica proposal built on conceptual primitives.
- **escalations:** (i) header caveat stands — reconcile A1/A2-one-project-or-two reading with W9-LEIBNIZ;
  §1–§4 supply the post-Leibniz side. (ii) Interactive browser unusable this session (needs remote-debugging
  approval popup) — all sources fetched via extraction backends instead; no coverage lost except that W3C
  *owl2-overview* refused scraping and the Primer was used instead. (iii) Only finding labels already present
  in the file ([Historical Claim], [Observation]) were used; LAB_CHARTER authorized set should be checked by
  Curator if stricter labeling is required.

