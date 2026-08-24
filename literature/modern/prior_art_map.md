# Prior-Art Landscape Map — Modern Representation Systems (CE-01 / WS-MODERN)

Worker: W13-MODERN (Modern Representation Researcher, ORGANIZATION.md §8).
Mandate: survey the full RESEARCH_PROTOCOL.md §3 prior-art list as it bears on the SIR idea (model-independent semantic intermediate representation between human intent and AI computation).
Evidence standard (Protocol §1): peer-reviewed papers/official docs with year + venue; quantitative claims carry the paper's own numbers and setting; search snippets are not evidence — sources below were opened and read before citing.
Finding labels per LAB_CHARTER.md authorized list. Confidence: low/med/high.
Status legend: ✅ studied this run; ⏳ section in progress (says what's missing and why).

Protocol §3 enumerates 17 named fields; the CE-01 deliverable spec counts 16 domains (ontologies + knowledge graphs merged). This map covers **all 16 merged domains = all 17 §3 bullets**, none skipped:

| # | Domain (§3 bullet[s]) | Section | Status |
|---|---|---|---|
| 1 | semantic parsing | §D1 | ✅ |
| 2 | meaning representation (AMR/UDR/DRS/PMB) | §D2 | ✅ |
| 3 | formal semantics | §D3 | ✅ |
| 4 | knowledge representation | §D4 | ✅ |
| 5–6 | ontologies + knowledge graphs | §D5 | ✅ |
| 7 | compiler intermediate representations | §D6 | ✅ |
| 8 | prompt compression | §D7 | ✅ |
| 9 | structured prompting | §D8 | ✅ |
| 10 | tool/function calling | §D9 | ✅ |
| 11 | program synthesis | §D10 | ✅ |
| 12 | neuro-symbolic AI | §D11 | ✅ |
| 13 | representation learning | §D12 | ✅ |
| 14 | interlingua systems | §D13 | ✅ |
| 15 | controlled natural languages | §D14 | ✅ |
| 16 | formal logic (+ proof assistants) | §D15 | ✅ |
| 17* | machine-to-machine communication (*counted inside D9/D16 in the 16-domain merge) | §D16 | ✅ |

Per-system entry format: what exists → what it achieved (with its own numbers) → measured limits → bearing on SIR (model-independent semantic intermediate representation).

---

## Seed sources (pre-verified by lab; re-verified this run)

| Source | Verification status this run | Notes |
|---|---|---|
| Banarescu et al., "Abstract Meaning Representation for Sembanking," LAW VII / ACL W13-2322 (2013), https://aclanthology.org/W13-2322/ | **Opened** (HTTP 200, landing page + full PDF fetched) | Foundational AMR paper. Studied in §D2. |
| Zhang, Jiang & Quan, "A Theory of Formalisms for Representing Knowledge," AAAI-25, vol 39(14), pp. 15257–15264, DOI 10.1609/aaai.v39i14.33674, published 2025-04-11 | **Opened** (HTTP 200, OJS page; title/authors/DOI/abstract read) | Proves all *universal* KR formalisms are **recursively isomorphic**, and pairwise-intertranslatable formalisms admitting the padding property likewise — "up to an offline compilation, all universal … representation formalisms are in fact the same." Studied in §D0 (bearing on H1) and cited throughout. |
| John Kausch, "Modeling Context and the Characteristica Universalis," *Knowledge Organization and Data Modeling* (DC&AM) 11(2), DOI 10.35492/docam/11/2/16 (2024), resolves to ideaexchange.uakron.edu/docam/vol11/iss2/16/ | **Opened** (HTTP 200; abstract read) | Frames word-embedding context models as modern descendant of characteristica-universalis ambitions in knowledge organization. Used as secondary scholarship linking historical ↔ modern (§D12). |
| Slavenskoj, "Lingenic" notation, SSRN abstract_id=6291378 | **Access blocked**: papers.ssrn.com returned HTTP 403 (Cloudflare "Just a moment") to direct fetch this run. Relies on the common brief's prior verification ("notation-only scope"). Confidence in scope claim: med (secondhand). Escalated: no independent primary-source access available from this environment. |

---

## §D1 — Semantic parsing

**What exists.** Neural seq2seq semantic parsing (lineage: Dong & Lapata ACL 2016; Jia & Liang ACL 2016 — *not opened this run, follow-up*). State of practice: **PICARD** (Scholak, Schick & Bahdanau, EMNLP 2021, arXiv 2109.05093 — opened) constrains LLM decoding via incremental parsing so fine-tuned T5 emits valid SQL.
**Best measured result.** PICARD + T5-3B on Spider text-to-SQL: **75.5 exact-set-match / 79.3 execution accuracy on dev**, vs **71.5 / 74.4** for unconstrained T5-3B (paper's own Table 1); abstract claims it "transforms passable T5 models into state-of-the-art" on Spider and CoSQL.
**Key limitation.** The constraint grammar is hard-wired to one target formalism/dialect; without it the model emits invalid output. Porting to a new representation = new grammar + new parallel training data.
**Bearing on SIR.** NL→formal-form is solved at scale *for existing formalisms only*. Nothing in the pipeline makes the target form model-independent — parser and grammar are coupled to one convention. Feasibility precedent for intent→IR decoding; warning that SIR needs a stable, versioned target spec (like SQL standards) or every consumer re-parses differently.

---

## §D2 — Meaning representation (AMR / UMR / DRS / PMB)

**What exists.** **AMR** (Banarescu et al., LAW VII 2013 — seed, pre-verified). **DRS tooling:** Boxer (Bos, STEP 2008, aclanthology.org/W08-2222 — opened): open-domain CCG→DRT analyzer, neo-Davidsonian events with VerbNet roles, DRSs compilable to FOL for theorem provers. **PMB** (Abzianidze et al., EACL 2017, aclanthology.org/E17-2039 — opened): multilingual corpus of shared compositional DRT-style representations, >11M words across EN/DE/IT/NL via cross-lingual projection, language-neutral annotation models (CCG → universal tags → symbolization → DRS). **UMR** (Van Gysel et al., "Designing a Uniform Meaning Representation…", NSF PAR 10288899 — title/authors confirmed via two search listings; venue unconfirmed, primary fetch timed out twice → med confidence, follow-up).
**Best measured result.** SPRING (Bevilacqua, Blloshmi & Navigli, AAAI-21 — PDF opened): single symmetric BART seq2seq for parsing+generation beats prior AMR 2.0 SOTA by **+3.6 SMATCH** (Text-to-AMR) and **+11.2 BLEU** (AMR-to-Text), no pipeline heuristics; shows benchmark-tuned "graph recategorization" heuristics are harmful out-of-distribution. Boxer: **>95% parse coverage** on newswire with C&C tools.
**Key limitation.** Human annotation is expensive and agreement-limited (AMR's SMATCH ceiling); four-plus MR families (AMR/DRS/PMB/UMR/PTB-style) coexist with non-trivial inter-conversion cost; coverage gaps persist even at 95% parse rate (Boxer leaves bridging/pronouns unresolved).
**Bearing on SIR.** Closest prior art as a *data format*: these are deliberately model-independent semantic structures — but none was designed as an execution target between human intent and AI compute; they are analysis products. Their fragmentation is itself evidence: the field pays the inter-MR translation tax repeatedly, which an SIR would pay once.

---

## §D3 — Formal semantics

**What exists.** Montague grammar ("English as a Formal Language" 1970; PTQ 1973 — historical references via publisher listings, not opened this run). Wide-coverage implementation lineage: **Boxer** (see §D2 — opened). Test suites: FraCaS (Cooper et al. 1996 report — follow-up).
**Best measured result.** Boxer (2008): >95% structural coverage on newswire; manual inspection on the SemEval shared-task texts found predicate-argument structure generally correct, but bridging references and pronoun resolution "not resolved in most cases."
**Key limitation.** Model-theoretic compositionality never scaled to open text without heavy engineering; ambiguity handling and coverage trade off against logical precision; the research line plateaued into niche tools rather than infrastructure.
**Bearing on SIR.** Supplies the machinery an SIR would borrow (type-driven composition, quantification scope, event semantics) and the cautionary result: hand-built semantic analysis stalls below full coverage. An SIR should treat FOL-grade semantics as an optional lowering, not the core layer.

---

## §D4 — Knowledge representation

**What exists.** **Cyc** (Lenat, CACM 1995 — existence, not opened, follow-up). **SUMO/SUO-KIF** (Niles & Pease, FOIS 2001; ontologyportal.org — opened): "~25,000 terms and ~80,000 axioms when all domain ontologies are combined," mapped to all of WordNet, IEEE-owned. **OWL 2** (W3C Recommendation, 2nd ed. 2012, w3.org/TR/owl2-overview — opened): formally defined semantics, EL/QL/RL decidable profiles, RDF exchange.
**Best measured result.** SUMO remains "the largest free, formal ontology available" per its maintainers (~25k terms/~80k axioms); OWL 2 achieved standardization with tractable-reasoning profiles adopted by tooling (Protégé/HermiT etc. — tooling scale not verified this run).
**Key limitation.** The acquisition bottleneck: Cyc required decades of manual assertion-entry and never delivered general reasoning; SUMO's axiom count is tiny next to language knowledge; expressivity vs decidability forced OWL profiles.
**Bearing on SIR.** With the AAAI-25 seed result (all universal KR formalisms recursively isomorphic), the differentiator among D4 systems was never expressive power — it was population/maintenance economics. Any SIR proposal must specify how it stays populated and versioned, or it repeats Cyc/SUMO's trajectory.

---

## §D5 — Ontologies + knowledge graphs

**What exists.** WordNet (Fellbaum 1998 — existence). Freebase (Bollacker et al., SIGMOD 2007 — existence, not opened, follow-up). **Wikidata** (Vrandečić & Krötzsch, CACM 57(10):78–85, 2014 — bibliographic record confirmed; cacm.acm.org returned HTTP 403 this run; live stats page wikidata.org/wiki/Wikidata:Statistics opened).
**Best measured result.** Wikidata live statistics retrieved 2026-08-24: **123,004,845 items, 2,535,138,825 edits** since launch — web-scale, crowdsourced, versioned, CC0, consumed by Wikipedia + external APIs.
**Key limitation.** Triple stores capture taxonomic/partitive facts; they strip events, context, quantification, and speaker intent. KG statements are assertions about the world, not representations of what someone meant.
**Bearing on SIR.** Existence proof that globally shared, model-independent semantic *infrastructure* is operationally possible when crowd-maintained and versioned (Wikibase model). But its semantic depth is shallow relative to intent representation — SIR must sit above KG level (intent/event structure), not duplicate it.

---

## §D6 — Compiler intermediate representations

**What exists.** **LLVM IR** (Lattner & Adve, CGO 2004, llvm.org/pubs/2004-01-30-CGO-LLVM.html — opened): common SSA code representation with "simple, language-independent type-system," enabling transformations at compile-, link-, run-time and idle-time. **MLIR** (Lattner et al., CGO 2021, arXiv 2002.11054 — abs opened): reusable/extensible multi-level infrastructure with dialects, aimed at heterogeneous hardware and connecting existing compilers.
**Best measured result.** No headline benchmark extracted this run (follow-up: MLIR paper's evaluation section); the operative datum is infrastructural adoption — LLVM underlies Apple/Xcode and Rust/Clang toolchains, MLIR underlies TensorFlow/IREE compilers (deployment facts, qualitative).
**Key limitation.** IR semantics are operational and domain-closed; correctness of transformations requires proof engineering (CompCert/Livelike formalizations — follow-up). Nothing here concerns *meaning*, only behavior-preserving transformation of programs.
**Bearing on SIR.** The strongest existence proof for the SIR architecture pattern: a neutral intermediate layer between many frontends and many backends accrues ecosystem value precisely because it is stable, versioned, and tool-independent. MLIR's dialect/lowering discipline maps directly onto "SIR core ↔ model-specific lowering." This is the design template; the open question is whether *semantic* content can be standardized the way *behavioral* content was.

---

## §D7 — Prompt compression

**What exists.** **LLMLingua** (Jiang et al., EMNLP 2023, arXiv 2310.05736 — opened): coarse-to-fine token-level prompt compression with budget controller, using a small LM's perplexity to score tokens. Related: Selective Context (2023) and gisting (Mu et al. 2023, compressing prompts to KV cache) — *not opened this run, follow-up*.
**Best measured result.** LLMLingua: **up to 20× compression with little performance loss** across GSM8K, BBH and two further datasets (paper's own claim, abstract + intro).
**Key limitation.** The compression criterion is a small model's perplexity — i.e., explicitly **model-relative**; deletion is lossy with no semantic guarantee, and output cannot be decoded back or validated against the original meaning.
**Bearing on SIR.** Same motivation as SIR (context economy between intent and compute), opposite mechanism: statistical deletion toward one model's conditioning vs semantic re-encoding neutral across models. An SIR should subsume this role while adding reversibility/verifiability — worth stating as an explicit design requirement.

---

## §D8 — Structured prompting

**What exists.** **Chain-of-Thought** (Wei et al., NeurIPS 2022, arXiv 2201.11903 — abs + full text opened). **Tree of Thoughts** (Yao et al., NeurIPS 2023 camera-ready, arXiv 2305.10601 — opened): search over "thought" units with lookahead/backtracking. Also ReAct (ICLR 2023 — existence, not opened).
**Best measured result.** CoT: PaLM-540B + eight exemplars reaches **state-of-the-art GSM8K**, surpassing fine-tuned GPT-3 with verifier. ToT on Game of 24 (GPT-4): **74% success vs 4% for CoT prompting**.
**Key limitation.** Gains emerge only at scale and are format-sensitive per model family; the structure lives ephemerally inside the token stream — it cannot be stored, audited, or handed to another system.
**Bearing on SIR.** Direct evidence that explicit intermediate structure multiplies reasoning capability — the premise SIR generalizes. But today's structures are informal, transient, and non-portable: exactly the gap an externalized, persistent semantic IR addresses. Nearest-neighbor domain for SIR's value argument.

---

## §D9 — Tool / function calling (+ schema conventions)

**What exists.** OpenAI function-calling JSON-schema convention (June 2023, official docs — engineering convention, not independently verified this run). **Toolformer** (Schick et al., NeurIPS 2023, arXiv 2302.04761 — opened): self-supervised learning of API calls embedded in text. **Gorilla** (Patil et al., 2023, arXiv 2305.15334 — abs opened; venue unconfirmed, follow-up): LLaMA finetuned on API docs with retriever.
**Best measured result.** Toolformer (6.7B): beats best baseline by **+11.7 / +5.2 / +18.6 points** across three LAMA knowledge subsets and outperforms OPT-66B and GPT-3-175B despite being ~10–26× smaller. Gorilla: finetuned LLaMA "surpasses GPT-4 on writing API calls," with reduced hallucination when retrieving up-to-date docs (exact AST accuracy not extracted this run).
**Key limitation.** JSON schemas carry syntax and types only; parameter semantics live in prose documentation the model must have seen; cross-vendor schema drift means identical intents are encoded differently per provider.
**Bearing on SIR.** Production systems already translate intent→structured artifacts billions of times daily, but the semantic contract is implicit and vendor-bound. This is the sharpest demonstrated market gap an SIR could fill: a shared intent-level contract above JSON types. High-priority domain for CE-01 nearest-neighbor analysis.

---

## §D10 — Program synthesis

**What exists.** **Codex** (Chen et al., arXiv 2107.03374, 2021 — opened; production version powers GitHub Copilot). **AlphaCode** (Li et al., Science 374, abq1158, 2022 — arXiv 2203.07814 full text opened; publisher DOI page returned HTTP 403, Science venue per bibliographic record).
**Best measured result.** Codex on HumanEval: **28.8% pass@1** (vs 0% GPT-3, 11.4% GPT-J), **70.2% pass@100**. AlphaCode: average rank within **top 54.3%** across 10 Codeforces contests (~5,000 participants each), estimated rating within top 28% of participants.
**Key limitation.** Works only where an executable oracle (unit tests/judges) selects among samples; spec ambiguity resolved statistically; Codex's own analysis flags failure on long operation chains and variable binding.
**Bearing on SIR.** Proof that intent→formal artifact scales when validation is mechanizable. An SIR has no natural execution oracle for "did we capture the intent?", so it must define its own validity checks (round-trip paraphrase, downstream task success) — otherwise it inherits synthesis's ambiguity problem without its safety net.

---

## §D11 — Neuro-symbolic AI

**What exists.** **DeepProbLog** (Manhaeve et al., NeurIPS 2018 spotlight, arXiv 1805.10872 — opened): neural predicates inside a probabilistic logic language, trained end-to-end. **NS-CL** (Mao et al., ICLR 2019 oral, nscl.csail.mit.edu — official project page opened): learns visual concepts, words, and a semantic parser jointly from images + QA pairs, executing symbolic programs over object-based scene representations.
**Best measured result.** DeepProbLog: integrates symbolic and subsymbolic inference end-to-end from examples (MNIST-addition benchmark solved from digit images alone — exact % not extracted, follow-up). NS-CL: state-of-the-art CLEVR-style VQA from natural supervision (exact % not extracted, follow-up).
**Key limitation.** Every system hand-designs its neuron↔symbol interface; symbolic search costs limit scale; domains are narrow micro-worlds.
**Bearing on SIR.** Architectural precedent for SIR's core bet: neural computation gains capability and interpretability when a discrete semantic layer sits underneath. Demonstrated in toy domains; nobody has built the general-purpose, portable version — that is precisely the open territory SIR claims.

---

## §D12 — Representation learning

**What exists.** word2vec (Mikolov et al., NIPS 2013 — existence, not opened, follow-up). **BERT** (Devlin et al., NAACL-HLT 2019, aclanthology.org/N19-1423 + arXiv 1810.04805 full text — opened). **SimCSE** (Gao et al., EMNLP 2021 — PDF opened, saved locally).
**Best measured result.** BERT-large: GLUE **80.5 (+7.7 absolute)**, MultiNLI 86.7 (+4.6), SQuAD v1.1 F1 93.2 (+1.5) — all then-SOTA. SimCSE (BERT-base): STS average Spearman **76.3 unsupervised / 81.6 supervised**, +4.2/+2.2 over prior best; shows embedding spaces are anisotropic and need contrastive regularization.
**Key limitation.** Distributed vectors are model-relative: no shared coordinate system exists across models, vectors do not compose into verifiable structure, and they are opaque to audit. Kausch (seed, §D0) reads embeddings as the characteristica's continuous rival.
**Bearing on SIR.** Defines what SIR is *not*: continuous, model-bound, uncomposable. The inter-model non-transferability of embeddings is itself the strongest technical motivation for a discrete symbolic interchange layer — two models cannot align their latent spaces, but both can emit the same discrete IR.

---

## §D13 — Interlingua systems

**What exists.** Classic interlingua MT: **UNL** (Uchida et al., Universal Networking Language, 1990s–2000s project; undl.org unreachable this run → existence secondhand, flagged med confidence). KANT/KANTOO (CMU, Nyberg & Mitamura — follow-up). Modern implicit pivot: **Google multilingual NMT** (Johnson et al., ICLR 2017, arXiv 1611.04558 — opened): single shared encoder/decoder + target-language token.
**Best measured result.** Johnson et al.: zero-shot translation between language pairs never seen in training, with quality often *improving* on all pairs at constant parameter count (WMT'14 benchmarks).
**Key limitation.** Hand-designed interlinguas died on design cost and expressive gaps (the "interlingual fallacy"); explicit pivots lose accuracy vs direct systems (pivot penalty — numbers not extracted, follow-up); UNL never reached critical adoption.
**Bearing on SIR.** The direct ancestor and chief precedent risk: an explicit semantic interchange layer has been tried at scale and collapsed economically. What changed since: learned encoders now exist that could *populate* an IR cheaply (vs hand-encoding), and LLM training gives a universal consumer base. CE-01's novelty case must argue why learned-population + versioned evolution escapes UNL's fate.

---

## §D14 — Controlled natural languages

**What exists.** **ACE / Attempto** (Fuchs, Schwitter et al., Univ. of Zurich, late 1990s–; attempto.ifi.uzh.ch opened — project active): unambiguous English subset translating deterministically to first-order logic. **PENG ASP** (Schwitter, CNL 2012 workshop, Springer LNCS/LNAI 7427 pp. 26–43 — chapter page opened; grammar paper PENGASP, CNL workshop 2021, aclanthology.org/2021.cnl-1.5 — search-confirmed): CNL parsed via discourse representation structures into answer-set programs. SBVR (OMG standard, 2008 — follow-up).
**Best measured result.** Determinism is the measured property: every ACE/PENGASP sentence in-grammar receives exactly one logical reading (design guarantee; quantitative parse-coverage figures not extracted this run, follow-up).
**Key limitation.** The expressiveness ceiling: fixing interpretation requires restricting input; users chafe at construction restrictions, and every grammar extension reopens ambiguity. Adoption stayed niche (aviation maintenance manuals, legal drafting pockets).
**Bearing on SIR.** Proves interpretation can be made deterministic — but only by pushing ambiguity back onto the human. SIR's wager is that a learned parser to a fixed IR buys full-NL coverage while keeping determinism where it matters; CNLs are the control group showing what must be traded.

---

## §D15 — Formal logic (+ proof assistants)

**What exists.** Proof assistants: Coq, Isabelle/HOL, **Lean 4 + mathlib** (de Moura et al.; mathlib scale figures not verified this run — stats page 404, follow-up). Automated provers: Vampire, E (CASC winners — follow-up). **AlphaProof** (DeepMind, Nature s41586-025-09833-y, published 2025 — article page opened; system blog July 2024).
**Best measured result.** AlphaProof (RL over Lean 4): solved IMO 2024 problems to **28/42 points — silver-medal range, one point below the gold threshold**, with multi-day compute per problem vs hours for humans.
**Key limitation.** The autoformalization gap: getting informal math/language *into* the formal system remains manual or unreliable; formal coverage of ordinary intent is near-zero; compute costs are extreme.
**Bearing on SIR.** The rigor ceiling: fully formal semantic targets enable machine-checked reasoning but at encoding costs prohibitive for everyday intent. SIR occupies the middle band (structured enough to verify properties, cheap enough to populate at conversation scale) — this domain defines the upper bound of the rigor/economy tradeoff curve.

---

## §D16 — Machine-to-machine communication

**What exists.** Syntax-first standards: EDI X12 (1979–), SOAP/WSDL/XML Schema (2000s) — existence, follow-up. **Protocol Buffers/gRPC** (Google, protobuf.dev — opened): language-neutral, platform-neutral interface definition + serialization. **RDF 1.1** (W3C Recommendation, 25 Feb 2014, w3.org/TR/rdf11-concepts — opened): graph data model + semantics for web interchange; OWL 2 layers formal semantics on top (§D4). HL7 FHIR in healthcare (follow-up).
**Best measured result.** Adoption scale rather than benchmarks: Protobuf is Google's inter-service lingua franca and a de-facto industry standard; Wikidata (§D5) moves 123M items via RDF/SPARQL APIs; RDF-based linked-data exchange operates at web scale but within a specialist niche.
**Key limitation.** Every successful M2M protocol fixes syntax and schema while leaving semantics to out-of-band human convention (docs, shared codebases). Formal-semantics attempts (RDF-S/OWL/Semantic Web) achieved standardization without mainstream machine reasoning — stalled on incentives and economics, not theory.
**Bearing on SIR.** Thirty years of M2M engineering show schema-only interchange works inside closed communities and fails to deliver open semantic interoperability. This is the adoption-side lesson for SIR: technical correctness of the IR is insufficient; there must be a driver for producers/consumers to standardize (the LLM-vendor fragmentation in §D9 may be that driver).

---

## Cross-domain synthesis (nearest neighbors to SIR)

1. **The layer exists nowhere as such:** semantic MRs (D2) are analysis products, not computation targets; compiler IRs (D6) target behavior, not meaning; tool schemas (D9) carry intent-shaped payloads without semantics. No surveyed system occupies "model-independent semantic form that AI systems execute against."
2. **Structural template = D6; economic cautionary tales = D4/D13/D16.** LLVM/MLIR prove neutral intermediate layers win when stable+versioned+tooled; Cyc, UNL, and the Semantic Web prove semantic layers die when population/maintenance economics don't close.
3. **Capability enablers now exist that prior attempts lacked:** constrained decoding (D1), self-supervised tool use (D9), program synthesis with oracles (D10), and RL-formalized reasoning (D15) make learned intent→IR→execution plausible for the first time.
4. **Sharpest open question for H1:** given AAAI-25 seed (all universal formalisms isomorphic up to compilation), SIR's value cannot lie in expressive power — it must lie in being the *populated, tooled, adopted* instance, i.e., an ecosystem play. Novelty claims should be scoped accordingly.

---
