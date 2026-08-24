# Leibniz Extraction: characteristica universalis + calculus ratiocinator

Worker: W14-LEIBNIZ (CE-01) · Role spec: agents/ORGANIZATION.md §6 · Schema: RESEARCH_PROTOCOL.md §2
Status: IN PROGRESS — written incrementally per passage analyzed (checkpoint discipline).

## 0. Scope and method

- **Objective:** Full Protocol §2 extraction of Leibniz's characteristica universalis / calculus
  ratiocinator as an engineering system (mechanisms, not biography): primitive-concept handling,
  composition operation, truth theory, inference rules; what failed mechanically vs philosophically.
- **Primary sources:** Gerhardt (ed.), *Die philosophischen Schriften*, vol. 4 (1880) and vol. 7 (1890).
  Downloaded as Internet Archive djvu.txt OCR:
  - `literature/leibniz/sources/gp4_djvu.txt` (identifier `diephilosophisch0004leib`)
  - `literature/leibniz/sources/gp7_djvu.txt` (identifier `diephilosophisch0007leib`)
  - Method note: the 1860s Fraktur German editorial apparatus OCRs poorly; the Latin and French
    primary texts are set in Antiqua and OCR readably with noise (rn→m, u/n flips, doubled spaces).
    Quotes below are verbatim from the OCR except that obvious OCR letter-errors inside quoted
    words are corrected in [brackets]; each quote carries the printed page number observed in the
    file adjacent to it, so GP page cites are empirically verified against this scan where marked "page seen".
  - Known limitation: Gerhardt vol. 7 does NOT contain the *Generales inquisitiones* (1686) under
    that name; its full text reached print only via Couturat 1903 (confirmed by SEP, "Leibniz's
    Influence on 19th Century Logic"). Gerhardt printed excerpts under other titles in vol. 7.
    Gen.Inq.-derived content here therefore comes either from those vol.-7 excerpts or is marked SECONDARY.
- **Secondary scholarship:** W. Lenzen's reconstruction (IEP article "Leibniz: Logic", authored by
  Lenzen; Handbook of the History of Logic vol. 3, 2004) — used only in §3, every claim there marked SECONDARY.
- Finding labels per LAB_CHARTER.md; confidence low/med/high.

## 1. Source map (passages extracted, with location verified in the IA scans)

| # | Text | Date | GP cite | Verified in scan? |
|---|------|------|---------|-------------------|
| P1 | Letter to Oldenburg (lingua realis, filum meditandi) | Dec. 1677 | VII 12–15 | yes (pp. 12–15 markers seen) |
| P2 | Guilielmi Pacidii initia et specimina Scientiae Generalis ("calculemus") | ~1678–79 | VII 124–126 | yes (125, 126 markers seen) |
| P3 | Discours touchant la méthode de la certitude et l'art d'inventer | 1677–78 | VII 174–183 | yes (173–183 markers seen) |
| P4 | Characteristic-numbers fragment (before Dialogus) | 1677–78 | VII ~188 f. | partial (189 marker seen) |
| P5 | Dialogus | Aug. 1677 | VII 190–192 | yes (190, 191 markers seen) |
| P6 | De organo sive arte magna cogitandi (item XIV) | ~1678–80? | VII ~198–204 | partial (198?, 203 markers seen; title line not cleanly OCR'd) |
| P7 | Specimen calculi universalis + Ad specimina addenda | 1679? | VII 218–227 | yes (217–227 markers seen) |
| P8 | Difficultates quaedam logicae (item XVII) | 1679? | VII ~211 f. | yes (210 marker seen) |
| P9 | Item XIX piece incl. struck-through title "Non inelegans specimen demonstrandi in abstractis" | 1690 | VII 228–235 | yes (229 marker seen; Gerhardt footnote on struck title seen) |
| P10 | Alphabetum cogitandi / catalogus generum passage (De synthesi et analysi universali context) | 1683? | VII ~292 ff. | partial |
| P11 | Meditationes de cognitione, veritate et ideis | 1684 | IV 422–423 | yes (Acta-piece region seen; page-marker OCR patchy) |
| P12 | Discours de métaphysique, §24 (demonstration vi formae) | 1686 | IV ~429 f. | yes (text seen; exact page split med-high) |

Note: item XI material (alphabet of human thoughts, characteristic numbers, statics of reasons) is
extracted under P3b/P4; the GP IV printing of the Dialogus de connexione (IV 424 f.) was NOT separately
extracted — the same dialogue is fully handled from the vol.-7 printing at P5.


## 2. Passage-by-passage extraction

### P1 — Letter to Oldenburg, Hannover late Dec. 1677 (GP VII 12–15)

**Verbatim (GP VII 14–15; page markers "14", "15" seen in scan):**

> "Illud autem quantivis pretii erit, quod in hac lingua nemo de argumento scribere poterit quod
> non intelligat. Si facere conabitur, aut ipse se nugari agnoscet et lector quoque, aut discet
> inter scribendum, scriptum enim et meditatio pari passu ibunt, vel ut rectius dicam, **scriptura
> erit meditandi filum**. ... Post tot de inventione, de Methodo, de Logica scriptores etiam
> optimos desideratur semperque desiderabitur filum meditandi, donec **Lingua realis** constituetur.
> Filum autem Meditandi voco quandam sensibilem et velut mechanicam mentis directionem quam
> stolidissimus quisque agnoscat. ... [bridge analogy:] Pontem noctu transituro regulam hanc
> praescribere possum ut recta procedat nec in dextram sinistramve evagetur, si salutem suam amat;
> huic praecepto poterit ille satisfacere magna cura et industria adhibita, sed si munita utrinque
> pontis latera erunt, aberit periculum et sollicitudo. Omnia ordine instituenda esse, nihil nisi
> datum distinctumque certum admittendum esse, difficultatem in partes distribuendam, medium
> tenendum, finem respici debere, rectam rationem semper exaudiendam: haec sunt praecepta
> philosophorum, egregia quidem illa, sed quibus fere non nisi a magnis viris quadam potius naturae
> et institutionis bonitate, quam vi methodi paretur. Filum autem meditandi semel datum efficiet
> ut determinata ratione in plerisque progredi possimus ... Tum denique enim vero evigilabunt
> homines, cum non difficilius videbitur ratiocinari quam loqui ... Non tubi, non microscopia
> tantum oculis adjecere, quantum istud cogitandi instrumentum capacitas dedisset."

- **[Historical Claim] The "real language" is specified as an *error-preventing guide rail*, not merely a notation.**
  The bridge-railing analogy states the design goal precisely: ordinary method-advice works only for
  "great minds" (natura/institutione); the lingua realis must make correct procedure *mechanical*
  ("velut mechanicam mentis directionem") so that anyone cannot stray ("aberit periculum").
  Mechanism = externalized structure constrains the walker; the constraint does the work talent used to do.
  Label: Historical Claim. Source: GP VII 14–15 (IA scan gp7_djvu.txt). Confidence: high.
- **[Observation] "Scriptura erit meditandi filum" — writing as the *thread* of thinking**: reasoning and
  writing proceed pari passu; the representation is the running medium of thought, not a post-hoc encoding.
  This is the earliest clear statement in our sources of the interface claim that matters for this lab:
  the representation *is* the reasoning channel. Label: Observation. Confidence: high.
- **[Observation] Success criterion stated as a *comprehension check*:** "nemo de argumento scribere
  poterit quod non intelligat" — nobody can write anything unintelligible to themselves or readers;
  nonsense becomes self-detecting ("ineptiae sese ipsae prodent"). A falsifiable property of a good SIR:
  malformed input is visibly malformed. Label: Observation. Confidence: high.
- Relevance to Project Characteristica: this is Leibniz's *interface* argument (representation as
  prosthesis that changes who can reason reliably), directly analogous to schema-constrained prompting.

### P2 — Guilielmi Pacidii initia et specimina Scientiae Generalis, item VII (GP VII 124–126)

**Verbatim (GP VII 125–126; markers "126" and running header "Guilielmi Pacidii initia..." seen):**

> "...quo semper homines ratiocinationes suas in omni argumento ad calculi formam exhibere
> controversiasque omnes finire possunt, ut non jam clamoribus rem agere necesse sit, sed alter
> alteri dicere possit: **calculemus**. Et cum ab utraque parte rationes validae erunt, quod fit in
> rebus concretis, ubi utrinque commoda atque incommoda reperiuntur, modus habebitur magnitudinem
> cujusque explorandi atque aestimandi, ut comparatis utrinque velut accepti expensique Tabulis de
> summa potioris pronuntietur. Haec sunt illa pondera, hi moduli, quibus ratio uti dixit poeta,
> sed hactenus eorum nulla exactis nec signatis publicave auctoritate aut certa nota comprobatis."

- **[Historical Claim] "Calculemus" includes a *decision/valuation* calculus, not just deduction.**
  Where both sides have valid reasons ("in rebus concretis"), the art must provide "modus magnitudinem
  cujusque explorandi aestimandique" — weighing commoda/incommoda like debit/credit ledgers
  ("accepti expensique Tabulis"). The popular caricature stops at dispute-ending calculation;
  the primary text extends it to graded comparison of pros/cons — i.e., scoring, not only proof.
  Label: Historical Claim. Confidence: high. Source: GP VII 125–126 scan.
- **[Observation] Leibniz flags the missing piece himself:** these weights exist so far "nulla exactis
  nec signatis ... certa nota comprobatis" — no exact signed units of value were established.
  This is a self-diagnosed gap: the calculus for *magnitude of reasons* was never constructed.
  Label: Observation. Confidence: high.
- Relevance: modern analogue = utility/scoring functions over structured arguments; also the honest
  observation that a representation system without its measure terms is incomplete.

### P4 — Characteristic-number fragment immediately before the Dialogus (GP VII ~188–189)

**Verbatim (scan offset before item XII heading; page marker "189"/"191" region seen):**

> "Finge ipsi Numeros characterísticos illos, tantoporo mirabiles, jam dari, observalaque illorum
> generali proprietate quadam, tales numeros qualescunque ei proprietati congruentes interim
> assumo, iisque adhibitis statim mirabili ratione omnes regulas Logicas per numeros demonstro
> et ostendo, quomodo cognosci possit an argumentationes quaedam sint in forma bonae."
> [preceded by:] "...rerum connexionem paucarum rerum ad aliis diversissimam in Numero,
> characterísticos dare difficilemium est, ideo elegans ... artificium excogitavi, (ut ostendi
> possit, quod raliocinaliones per numeros comprobare liceat." [OCR noisy]

- **[Historical Claim] Arithmeticization of logic by characteristic numbers**: assign each primitive
  concept a number such that concept-containment becomes numerical divisibility (the full scheme,
  with primes assigned to simples and products to composites, recurs across the corpus); then every
  rule of logic becomes a provable theorem about numbers ("omnes regulas Logicas per numeros
  demonstrare"), and validity checking becomes arithmetic. Label: Historical Claim. Confidence: high
  (text seen in vol. 7 immediately preceding Dialogus; the prime/divisibility elaboration is in the
  same cluster of fragments — see P6/P10 for the alphabet/catalog side).
- **[Observation] This is reduction-of-representation to computation**: validity is decidable by a
  mechanical operation (divide) on encoded objects. It is the first concrete instance in our sources
  of "encode semantics so that inference = arithmetic." Label: Observation. Confidence: high.
- Failure hook (developed in §5): the scheme requires the *complete list of primitives* and their
  independence (coprimality) — exactly what Leibniz never had; see P10 where he says vulgar genera
  are "non recte constituta".

### P5 — Dialogus (August 1677) (GP VII 190–192)

**Verbatim (markers "190"/"191"/"192" region seen; Gerhardt's manuscript note "Cum DEUS elucidat et
cogitationem exercet, ut mundus" seen in footnote):**

> A. "Si filum tibi daretur, quod ita fleetere debeas, ut in se redeat, ut quantum plurimum potest
> spatii comprehendat, quomodo id fleeteres?" B. "in orbem; ostendunt enim Geometrae circulum esse
> capacissimum figurarum ejusdem ambitus ..." A. "Hoccine verum esse putas, etiamsi a te non
> cogitetur?" B. "Imo, antequam vel Geometrae id demonstrassent, vel homines observassent." ...
> A. "Ergo in rebus, non in cogitationibus veritatem ac falsitatem esse putas." ... B. "cogor fateori."
> ... A. "Videsne ergo veritatem esse propositionum seu cogitationum, sed possibilium..."
> [on definitions:] A. "Nonne definitio est principium demonstrationis? B. Fateor... A. Talium ergo
> propositionum veritas pendet ex definitionibus. B. Concedo. A. At definitiones pendent ab arbitrio
> nostro..." B. "cogitationes fieri possunt sine vocabulis." A. "At non sine aliis signis. Tentas
> quaeso an ullum Arithmeticum calculum instituere possis sine signis numeralibus." B. "Valde me
> perturbas, neque enim putabam characteres vel signa ad rationcinandum tam necessaria esse."
> A. "Imo si characteres absessent, numquam quicquam distincte cogitaremus, neque ratiocinaremur."
> [on diagrams:] A. "...sciendum est etiam has figuras habendas pro characteribus, neque enim
> circulus in charta descriptus verus est circulus, neque id opus est, sed sufficit eum a nobis pro
> circulo haberi." B. "Habet tamen similitudinem quandam cum circulo, eaque certe arbitraria non est.
> A. Fateor, ideoquo utilissimi characterum sunt figurae."

- **[Historical Claim] Truth theory in the Dialogus**: truths are properties of *possible propositions*,
  not of things nor of actual mental acts ("veritatem esse propositionum seu cogitationum, sed
  possibilium"); truth has its ground in the nature of things AND the thinker jointly ("necesse est
  meam et rerum de quibus cogito naturam talem esse..."). Definitions are principles of demonstration
  but their truth does not hang on arbitrary naming — same geometry for Greeks/Latins/Germans.
  Label: Historical Claim. Confidence: high.
- **[Historical Claim] Strong symbol-dependence thesis**: no distinct thought or reasoning without
  signs ("si characteres absessent, numquam quicquam distincte cogitaremus, neque ratiocinaremur");
  even geometric figures function as characters — and the drawn circle need not be a true circle,
  it suffices that we take it as one. This grounds the characteristica psychologically: signs are not
  labels for thoughts already formed; they are the vehicle that makes thoughts distinct at all.
  Label: Historical Claim. Confidence: high.
- **[Observation] Iconicity carve-out**: B objects that the drawing's similitude to the circle is
  "arbitraria non est," and A concedes analogical characters are maximally useful ("ideoquo
  utilissimi characterum sunt figurae"). So the sign system is NOT purely conventional/arbitrary:
  Leibniz explicitly admits resemblance-based signs alongside arbitrary ones. Design principle:
  choose signs whose structure mirrors what they represent where possible. Label: Observation.
  Confidence: high.
### P3 — Discours touchant la méthode de la certitude et l'art d'inventer, item X (GP VII 174–183)

**Verbatim (GP VII 179–181; page markers seen):**

> "Or les repertoires sont de deux sortes ... Je crois que le premier genre de Repertoires pourroit
> etre Alphabetique, mais le second sera plustost systematique, en fournissant la matiere prochaine
> de l'arrangement d'un Systeme accompli, qui outre les assertions, en contiendra encor les raisons
> ou preuves. ... L'ordre scientifique parfait est celuy, où les propositions sont rangées suivant
> leur demonstrations les plus simples, et de la maniere qu'elles naissent les unes des autres ...
> On peut meme dire que les Sciences s'abregent en s'augmentant, qui est un paradoxe tres veritable,
> car plus on decouvre des verites et plus un est en estat d'y remarquer une suite reglé et de se
> faire des propositions tousjours plus universelles dont les autres ne sont que des exemples ou
> corollaires, de sorte qu'il se pourra faire qu'un grand volume de ceux qui nous ont precedé se
> reduira avec le temps a deux ou trois theses generales."

- **[Observation] Knowledge-compilation thesis**: sciences shrink as they grow — accumulated volumes
  compress into a few general theses because more discovered truths enable more universal propositions
  covering the rest as corollaries. Representation goal = maximally general compressed core plus a
  derivation discipline, not an ever-larger encyclopedia. Label: Observation. Confidence: high.
- Relevance: anticipates compression-with-recoverability as the measure of representation quality;
  directly parallel to Protocol §6 accounting (what must be carried so everything else is recoverable).

### P3b — Item XI (Latin text accompanying German report "die Characteristica Universalis betreffend"), GP VII 184–190

**Verbatim — origin and alphabet of human thoughts (GP VII 185 f.; markers seen):**

> "...dubitabationem aliquando movebam de praedicamentis. Dicebam enim quemadmodum haberentur
> praedicamenta seu classes notionum simplicium, ita debere haberi novum praedicamentorum genus,
> in quo et propositiones ipsae seu termini complexi ordine naturali dispositae haberentur ...
> Incidi necessario in hanc contemplationem admirandam, quod scilicet excogitari posset quoddam
> **Alphabetum cogitationum humanarum**, et quod literarum hujus Alphabeti combinatione et
> vocabulorum ex ipsis factorum analysi **omnia et inveniri et dijudicari possent**."

**Verbatim — scope of the remaining task and the timetable (same fragment, GP VII 187):**

> "Itaque nunc nihil aliud opus est, ut Characteristica, quam quantum ad Grammaticam linguae tam
> mirabilitis dictionariumque plerisque frequentioribus suffeceturum satis est, constituatur, vel
> quod idem est, ut **Numeri idearum omnium characteristici habeantur**. ... Aliquot **selectos
> homines rem intra quinquennium absolvere posse puto; intra biennium autem doctrinas, magis in vita
> frequentatas, id est Moralem et Metaphysicam, irrefragabili calculo exhibebunt.** Numeris autem
> plerarumque notionum characteristici semel constitutis habebit Genus Humanum **Organon novum**,
> plus multo mentis potentiam aucturum, quam ultra optica oculos juverunt ..."

**Verbatim — weighing reasons; probabilities; statics (GP VII 188 f.; marker "189" seen):**

> "Qui vero in aliqua deliberatione totam utrinque Tabulam accepti et expensi subducere, id est
> commoda et incommoda non tantum numerare, sed et recte ponderare possit, vix quisquam est. Itaque
> duo qui disputant, ferme mihi duobus mercatoribus similes videntur, qui sibi mutuo ex multis
> capitibus debitores essent, sed nollent unquam ad generale cujusdam bilancis examen venire ...
> Sic ipsi nunquam litem terminabunt. Idque haectenus in plerisque controversiis, ubi res liquida
> (id est ad numeros revocata) non est, fieri mirari non debemus. Nunc vero characteristica nostra
> cuncta ad numeros revocabit, et ut ponderari etiam rationes queant, velut quoddam staticae genus
> dabit. Nam etiam **probabilitates calculo et demonstrationi subjecturunt**, cum aestimari semper
> possit, quodnam ex datis circumstantiis probabiliss sit futurum."

- **[Historical Claim] The characteristica has two halves and they are equated**: (i) an alphabet of
  human thoughts whose letter-combinations generate concepts and whose analyses judge them
  ("inveniri et dijudicari"); (ii) characteristic NUMBERS for all ideas ("quod idem est"). Notation and
  arithmetic encoding are one project: the dictionary/grammar suffices iff the numbers exist.
  Label: Historical Claim. Confidence: high.
- **[Historical Claim] Explicit engineering estimate**: 5 selected people, 5 years for the whole;
  morality and metaphysics in 2 years with infallible calculation. This is the ambition-vs-
  implementation anchor point for §5. Label: Historical Claim. Confidence: high.
- **[Observation] Disputes persist because there is no common audit**: disputants are like merchants
  with mutual debts refusing a joint balance-sheet ("generale bilancis examen"); controversies last
  where the matter is not "liquida," i.e., not reduced to numbers. Remedy named: a *statics* that
  weighs reasons, including PROBABILITIES subjected to calculus. So the full program = deduction +
  weighted decision theory. Label: Observation. Confidence: high.
- Relevance: the balance-sheet framing matches modern evaluation of structured debate/argument mining;
  the probability clause makes Leibniz's target closer to calibrated scoring than to proof alone.

### P6 — Item XIV: De organo sive arte magna cogitandi (GP VII ~198–204)

**Verbatim — the exact language / Adamic language passage (GP VII 198 f.; between page anchors):**

> "Si daretur vel **lingua quaedam exacta** (quam quidam Adamicam vocant) vel saltem genus scripturae
> vere philosophicae, qua notiones revocarentur ad **Alphabetum quoddam cogitationum humanarum**,
> omnia quae ex datis ratione assequi, inveniri possent quodam genere calculi, ponendo ac resolvendo
> problemata arithmetica aut geometrica. Atque ea vera foret sive Cabala vocabulorum mysticorum,
> sive Arithmetica numerorum Pythagoricorum, sive **Characteristica Magorum hoc est Sapientum**."
> [He adds that he glimpsed this almost as a boy and sketched it in his youthful Dissertatio de arte
> combinatoria:] "Possibile esse, imo facile et intra aliquot annos ab aliquot intelligentibus
> conspirantibusque pro suo primo gradu absolvendum, geometrica sane certitudine possum demonstrare."

**Verbatim — necessary vs contingent truths as commensurable vs incommensurable numbers (GP VII 200; marker "200" seen):**

> "Discrimen inter veritates necessarias et contingentes vere idem est, quod inter numeros
> commensurabiles et incommensurabiles: ut enim in numeris commensurabilibus resolutio fieri potest
> in communem mensuram, ita in veritatibus necessariis demonstratio sive reductio ad veritates
> identicas locum habet. At quemadmodum in surdis rationibus resolutio procedit in infinitum, et
> acceditur quidem utcunque ad communem mensuram, ac series quaedam obtinetur, sed interminata, ita
> eodem pariter processu **veritates contingentes infinita analysi indigent, quam solus Deus
> transire potest**. Unde ab ipso solo a priori ac certo cognoscuntur ... Atque haec est radix
> contingentiae, nescio an haetenus explicata a quoquam."

**Verbatim — error theory / design spec (GP VII 200 f.):**

> "...ut redeam ad expressionem cogitationum per characteres, ita sentio numquam controversias finiri
> neque sectis silentium imponi posse, nisi a ratiocinationibus complicatis ad calculos simplices, a
> vocabulis vagae incertaeque significationis ad characteres determinatos revocemur. Id scilicet
> efficiendum est, ut **omnis paralogismus nihil aliud sit quam error calculi**, et ut sophisma, in
> hoc novae scripturae genere expressum, revera nihil aliud sit quam **soloecismus vel barbarismus**,
> ex ipsis grammatices hujus philosophicae legibus facile refutandus."

**Verbatim — organon and Chinese-characters analogy (GP VII 203; running header "XIV." and marker seen):**

> "...si inventio Telescopiorum et Microscopiorum tantum cognitioni naturae lucis attulit, facilo
> intelligi potest, quantum praestare debeat novum hoc **organon**, quo ipso mentis oculus, quantum
> in humana potestate est, instruitur. ... Quemadmodum tarnen apud Sinenses ferunt, qui aliquot
> characterum millena norint, eum plerissima scribere posse, caeteris magis reconditis vel cuique
> proprio artifici vel majori Magistro servatis, ita hic quoque, proportiona progressuum sive hominis
> cujusque sive totius generis humani, fructus quoque artis una major sentietur."

- **[Historical Claim] Inference mechanism specified as reduction**: reasoning becomes a calculus by
  resolving complicated ratiocinations into simple calculations and vague words into determinate
  characters; success criterion = every fallacy is either a computational error or a syntactic
  ill-formedness (solecism/barbarism) detectable by the grammar's own laws. This is the clearest
  single-sentence spec of the calculus ratiocinator in the corpus. Label: Historical Claim.
  Confidence: high.
- **[Historical Claim] Truth theory completed by infinite analysis**: necessary truths = finite
  reduction to identities (like commensurable numbers); contingent truths require infinite analysis,
  traversable only by God. Contingency is thus defined REPRESENTATIONALLY (as analytic unboundedness),
  not metaphysically. Label: Historical Claim. Confidence: high.
- **[Observation] Primitive-concept handling admits two tiers**: the alphabet targets simples, but the
  Chinese analogy concedes a working system can proceed with thousands of unanalyzed characters
  reserved for specialists ("caeteris ... cuique proprio artifici servatis") — i.e., Leibniz explicitly
  allows an extendable lexicon of opaque technical terms alongside analyzed ones. Label: Observation.
  Confidence: high.
- Relevance: the paralogism-as-calculation-error criterion is exactly the modern formal-verification /
  type-checking pitch; the infinite-analysis clause is the earliest representational account of why
  empirical matters resist symbolic settlement (cf. undecidability/truncation in practice).

### P7 — Specimen calculi universalis + Ad specimen addenda, item XVIII (GP VII 218–227)

**Verbatim — the formal system (GP VII 218–220; markers seen):**

> "(1) Propositio Universalis affirmativa hoc loco a nobis sic exprimetur: **a est b**, sive (Omnis)
> homo est animal. Itaque semper intelligemus praefixum signum universale. Propositiones negatives,
> et particulares et hypotheticas nunc non attingemus.
> (2) Propositio per se vera: **ab est a**, sive (Omne) animal rationale est animal. [also ab est b;
> a est a]
> (3) Consequentia per se vera: Si a est b et b est c, Ergo a est c ...
> (5) Propositio vera est, quae ex positis et per se veris per consequentias oritur. Nota: etsi
> propositiones quaedam pro hominum arbitrio assumantur, ut definitiones terminorum, inde tarnen
> oritur veritas minime arbitraria ... Quemadmodum in numeris apparet, quorum signa et periodi
> decadicae hominum voluntate constituta sunt, calculi inde deducti significant absolute veritates
> ... **Utile autem ad scientias ita assumi characteres, ut ex paucis assumtis multa facile duci
> possint, quod fit si simplicissimis cogitandi elementis characteres assignentur.**
> (6) Si quid substitui ubique salva veritate potest in locum alterius, alterum vicissim ubique
> substitui potest in locum ipsius ... [proof by reductio]
> (7) **Eadem sunt quorum unum in alterius locum substitui potest, salva veritate**, ut Triangulum
> et Trilaterum ...
> (8) Omnes propositiones (universales affirmativae, de quibus solis hoc loco agimus) in quas
> ingreditur litera data a, possunt reduci ad has formas: a est cd | ab est e | c est a ..." 

**Verbatim — composition algebra and the semantic rule (Addenda, GP VII 223–224; markers seen):**

> "Si a est b, et d est c, tum ad erit bc. [proved by chaining substitutions]
> Generaliter si sint quotcunque propositiones: a est b, c est d, e est f, inde fieri poterit una:
> ace est bdf, per additionem illinc subjectorum, hinc praedicatorum.
> **Omnia haec facile demonstrantur hoc uno tantum posito, subjectum esse ut continens, praedicatum
> ut contentum simultaneum seu conjunctivum**, vel contra: subjectum esse ut contentum, praedicatum
> ut continens alternativem seu disjunctivum."
> [Gerhardt's summary of the manuscript:] "Terminus est a . b . ab . bed . ut homo . animal .
> animal rationale . rationale mortale visibile." [Postulatum:] letters may be assumed equivalent to
> one or more letters ("Homo idem quod animal rationale").

- **[Historical Claim] Composition operation = term juxtaposition (multiplication)**: concepts combine
  by concatenation (homo.animal = animal rationale); a term is a product of simpler terms; universal
  affirmation "a est b" means a's product includes b's factors — subject contains predicate
  conjunctively (INTENSIONAL reading), with an alternative disjunctive/extensional reading explicitly
  allowed ("vel contra"). Both semantics stated side by side in one sentence. Label: Historical Claim.
  Confidence: high.
- **[Historical Claim] Inference rules**: (i) self-true propositions ab ⊇ a, ab ⊇ b (simplification);
  (ii) transitivity a→b, b→c ⇒ a→c (Barbara); (iii) composition a→b & d→c ⇒ ad→bc; (iv) multi-premise
  aggregation ace ⊇ bdf; (v) substitution of equivalents salva veritate everywhere, with identity
  DEFINED as mutual substitutability ((7)); proofs themselves executed by rewriting/substitution — the
  calculus is its own metatheory in miniature. Label: Historical Claim. Confidence: high.
- **[Observation] Scope restriction declared inside the system**: only universal affirmative
  propositions handled; "propositiones negativas et particulares et hypotheticas nunc non
  attingemus" — negation, existential import, and conditionals deferred (negatives appear only later
  via non-a terms in the Addenda). Label: Observation. Confidence: high.
- **[Observation] Anti-conventionalist clause**: definitions may be chosen arbitrarily but the derived
  truths are "minime arbitraria" — decimal digits are conventional while arithmetic results are not.
  Plus the compression principle: choose characters for the SIMPLEST elements of thinking so that few
  assumptions yield many consequences. Label: Observation. Confidence: high.
- Relevance: this is a term logic with set-like composition but intensional reading — closest single
  ancestor of both Boolean algebra and description-logic style containment; the explicit dual reading
  prefigures intensional/extensional duality in KR.

### P8 — Difficultates quaedam Logicae solutu dignae, item XVII (GP VII 211–213)

**Verbatim (markers "210"/"212" seen):**

> "Difficultates quaedam Logicae solutu dignae occurrerunt: qui fit quod in singularibus procedit
> oppositio: Petrus Apostolus est indes, et Petrus Apostolus non est indes, cum tarnen opponatur
> alias universalis affirmativa et particularis negativa? An dicemus, singulare aequivalere
> particulari et universali? Recte. ... Major liaec est difficultas: quod conversio recepta videtur
> aliquando inducere falsum. Nempe conversio per accidens universalis affirmativae in casu tali:
> omnis ridens est homo, Ergo quidam homo est ridens; nam prior vera est etiamsi nullus homo rideret,
> at posterior vera non est, nisi aliquis homo actu rideat. **Prior loquitur de possibilibus,
> posterior de actualibus.** At non occurrit difficultas similis, si teneas in terminis possibilium,
> v.g. omnis homo est animal, Ergo quoddam animal est homo. Dicendum ergo conclusionem: quidam homo
> est ridens, esse verum **in regione idearum**, scu si ridens sumas pro quadam specie Entis
> possibilis ... vera erit propositio, etiamsi nullus rideat existat."
> [on dictum de omni:] "omnis homo est animal, idem est quod A homo est animal, B homo est animal,
> C homo est animal, et ita in caeteris ... [his old reduction:] Universalis Affirmativa: omne A est
> B, id est aequivalent AB et A."

- **[Historical Claim] Existential commitment solved possibilistically**: conversion failures come
  from mixing actual with possible readings; keep ALL terms in the register of possibilia ("in regione
  idearum") and the inference holds even if no laughing man exists. Quantification ranges over
  possible beings; actual existence enters only outside the conceptual calculus. Singulars count as
  both universal and particular. Label: Historical Claim. Confidence: high.
- **[Observation] Dictum de omni as expansion over indefinite individuals**: a universal is shorthand
  for a conjunction over A,B,C,... individuals; his "old reduction" defines omne A est B as equivalence
  of AB and A (containment as product-absorption). Label: Observation. Confidence: high.
- Failure hook for §5: the possibilist fix preserves validity only by making the calculus about a
  platonic concept-space; anything involving actuality (existence claims, perception, indexicals)
  leaves the system — the boundary Leibniz never crossed formally.

### P9 — Item XIX (struck-through title "Non inelegans specimen demonstrandi in abstractis"), GP VII 228–235

Gerhardt footnote (seen at p.229): Leibniz first headed the piece "Non inelegans specimen
demonstrandi in abstractis", then crossed the title out; manuscript later revised.

**Verbatim — plus-minus axioms (GP VII 230 f.; markers seen):**

> "Def. 6. Si nihil aliquod pluribus simul positis aut remotis coincidere ponatur, plura illa dicuntur
> constituere, unum autem constitutum. Schol. Hinc omnia quidem inexistentia sunt constituentia, sed
> non contra, ut A - A oo A', utique non inest A in A.
> Def. 8. Compensatio est, cum idem ponitur et detrahitur in eodem ... Destruccio est cum quid ob
> compensationem abjicitur, ut non amplius exprimatur et pro M - M ponendo Nihil.
> Axioma 1. Si idem secum ipso sumatur, nihil constituitur novum, seu **A + A oo A**. Schol. Equadem
> in numeris 2 + 2 faciunt 4 ... sed tune bini additi sunt alii a prioribus; si iidem essent, nihil
> novi prodiret, et perinde esset ac si jactu ex tribus ovis jactare vellemus sex, numerando primum
> 3 ova, deinde uno sublato residua 2, ac deindo uno rursus sublato residuum 1.
> Axioma 2. Si idem ponitur et detrahitur, quiequid inde in alio constituitur, coincidit Nihilo. Seu
> **A - A oo Nihilo**.
> Postulatum 1. Plura quaecunque simul sumi possunt ad unum constituendum, ut si sint A et B, potest
> inde fieri A + B, quod appellari potest L.
> Postulatum 2. Detrahere aliquid A ab eo, cui inest ... invenire Residuum L - A. Schol. Opus hujus
> postulati postea modum dabimus inveniendi differentiam inter duo quorum unum alteri inest ... seu
> modum inveniendi A - A, seu A + B - A, licet saltem dentur A et B, non vero B."
> [Theorems, each proved by substitution:] THEOR. I "Quae sunt eadem uni tertio, eaedem sunt inter
> se"; THEOR. III "Si eidem addantur coincidentia, fiunt coincidentia" (A+C oo B+C); **THEOR. IV
> "Contentum contenti est contentum continentis"** (transitivity of containment); scholium (p.229):
> "Non omne inexistens est pars, nec omne continens est totum, ex.gr. quadratum inscriptum et
> diameter circulo inest; et quadratum quidem est pars circuli, diameter vero non est pars ejus."

- **[Historical Claim] A genuine axiomatic system with a NEGATIVE operation**: idempotence (A+A=A,
  defended with the double-counting-of-eggs example), compensation A−A=Nihil, unrestricted
  composition (any plurality sums to one term), and subtraction as a partial operation whose domain
  problem Leibniz flags himself ("invenire differentiam ... licet saltem dentur A et B, non vero B").
  Theorems proven purely by definitional substitution. Label: Historical Claim. Confidence: high.
- **[Observation] Mereology kept separate from containment**: inexistence ≠ parthood (the inscribed
  square/diameter example) — containment is finer-grained than spatial part-whole; Leibniz notes the
  accurate notion of totum/pars needs further explanation "quod non est hujus loci." Label: Observation.
  Confidence: high.
- Relevance: this is the direct ancestor reading of Boolean algebra (Lenzen SECONDARY §3 confirms
  deductive equivalence); the flagged subtraction-domain problem is a real partiality bug he diagnosed
  before Russell-style paradoxes existed.

### P10 — De Synthesi et Analysi universali seu Arte inveniendi et judicandi (GP VII 292 ff.)

**Verbatim (GP VII 292–294; markers "293"/"294" seen; treatise heading confirmed in scan):**

> "Videbatur autem mihi res universaliter fore in potestate, si, haberentur prius praedicamenta vera
> simplicium terminorum et ad ea obtinenda constitueretur novum quoddam velut **Alphabetum
> cogitandi**, seu catalogus summorum (vel pro summis assumtorum) generum, ut a, b, c, d, e, f, ex
> quorum combinatione fierent inferiores notiones. Sciendum eritn est genera sibi mutuo differentias
> praestare, omnemque differentiam posse concipi ut genus et omne genus ut differentiam, et tam recte
> dici animal rationale, quam si fingere licet, rationale animale. Cum vulgaria vero genera species
> sua combinatione non exhibeant, concludebam **non recte constituta esse**, et quidem genera summis
> proxime inferiora forent biniones, ut ab, ac, bd, cf; genera tertii gradus forent terniones, ut
> abc, bdf, et ita porro. ... [for species y = abcd, convertible predicates are only] lx, bw, cr, ds,
> Ir, mq, np [binion/ternion products containing all four primes]. ... **Primae notiones quarum
> combinatione fiunt caeterae aut sunt distinctae aut confusae; distinctae quae per se intelliguntur,
> ut Ens; confusae (et tarnen clarae) quae per se percipiuntur, ut coloratum, quod non possumus
> alteri explicare nisi monstrando**, nam etsi sua natura sit resolubile cum causam habeat, nullis
> tamen notis separatiin explicabilibus describi agnosceqiie satis potest a nobis, sed confuse
> tantum cognoscitur nec proinde definitionem capit nominalem. Nominalis definitio consistit in
> enumeratione notarum seu requisitorum ad rem ab aliis omnibus distinguendam sufficientium, ubi si
> requisita requisitorum semper quaerantur, veniendum erit tandem ad **notiones primitivas quae
> requisitis vel absolute vel a nobis satis explicabilibus carent**. ... Porro omnes Notiones derivatae
> oriuntur ex combinatione primitivarum ... verum cavendum est, ne combinationes sint inutiles,
> conjungendo ea quae sunt **incompatibilia inter se, quod non nisi experimento vel resolutione in
> distinctas simplices judicari potest**. Id vero in definitionibus realibus condendis diligenter
> observandum est, ut constet esse possibiles seu notiones ex quibus constant inter se conjungi
> posse."

- **[Historical Claim] Primitive-concept handling, final form**: primitives split into DISTINCT
  (self-intelligible, e.g. Ens) and CONFUSED-but-clear (perceived only, e.g. coloratum) which admit no
  nominal definition and can be taught only ostensively ("nonisi monstrando"). Analysis iterates
  "requisites of requisites" until primitives lacking explicable requisites are reached. So the
  alphabet is NOT assumed wholly analyzable: some terminals are sensory-demonstrative. Label:
  Historical Claim. Confidence: high.
- **[Historical Claim] Composition must pass a possibility check**: derived notions = combinations of
  primitives, but incompatible combinations are forbidden and compatibility "can only be judged by
  EXPERIMENT or resolution into distinct simples"; real definitions must certify composibility.
  Generation without a well-formedness filter produces garbage — stated by Leibniz himself. Label:
  Historical Claim. Confidence: high.
- **[Observation] Verdict on existing taxonomies**: vulgar genera are "wrongly constituted" because
  species are not their combinations; genus/differentia are relative roles (any difference can be a
  genus, any genus a difference: "animal rationale" = "rationale animale"). Convertible predicates of
  y=abcd computed combinatorially. Label: Observation. Confidence: high.
- Relevance: (a) ostensive primitives anticipate grounded/perceptual symbols — a representation can't
  be fully verbal; (b) the compatibility check anticipates constraint typing/composibility testing in
  ontology engineering; (c) the "vulgar genera are wrong" charge warns against adopting folk categories
  as primitive vocabulary.

### P11 — Meditationes de cognitione, veritate et ideis (Acta Eruditorum 1684) (GP IV 422–423)

**Verbatim (GP IV 422; scan gp4_djvu.txt, Acta-piece region verified):**

> "Et certe cum notio [tabel]lae composita est, non possumus omnes ingredientes eam notiones simul
> cogitare: ubi tamen hoc licet, vel saltem in quantum licet, cognitionem voco intuitivem. **Notionis
> distinctae primitivae non alia datur cognitio, quam intuitiva, ut compositarum plerunque cogitatio
> non nisi symbolica est.** Ex his jam patet, nos eorum quoad quae distingto cognoscimus, ideas non
> percipere, nisi quatenus cogitatione intuitiva utimur. Et sano contingit, ut nos saepo falso
> credamus habere in animo ideas rerum, cum falso supponimus aliquos terminos, quibus utimur, jam a
> nobis fuisse explicatos: nec verum aut certe ambiguitati obnoxium est, quod ajunt aliqui, non posse
> nos de re aliqua dicere, intelligendo quod dicimus, quin ejus habeamus ideam. Saepe enim vocabula
> ista singula utcunque intelligimus, aut nos ante intellexisse meminimus..."

- **[Historical Claim] Cognitive budget behind the notation**: composite notions cannot be thought
  all-at-once; their thought is SYMBOLIC; only distinct PRIMITIVES are known intuitively. We routinely
  believe we have ideas because we remember having once explained our words — verbal fluency masquerades
  as ideation. The characteristica is precisely the remedy: force analysis so symbols track ideas.
  Label: Historical Claim. Confidence: high.
- Relevance: names the exact failure mode of unstructured prompting — fluent symbol manipulation over
  unanalyzed terms — and gives the historical warrant for requiring primitive-grounded schemas.

### P12 — Discours de métaphysique §24 (1686) (GP IV ~429 f.)

**Verbatim (scan gp4_djvu.txt, Discours region; page marker ~430 area):**

> "Nee minus abuti video nostri temporis homines jactato illo principio: Qui clare et distincte de
> re aliqua percipio, id est verum seu de ea enuntiabile. Saepe enim clara et distincta videntur
> hominibus temero judicantibus, quae obscura et confusa sunt. Inutile ergo axioma est, nisi clari
> et distincti criterii adhibeantur, quae tradidimus, et nisi constet de veritate idearum. ... firma
> autem demonstratio est, quae praescriptam a Logica formam servat, non quasi semper ordinarios
> Scholarum more Syllogismis opus sit ..., sed ita statuem ut argumentatio concludat **vi formae**,
> qualis argumentationis in forma deductae conceptae exemplum, **etiam calculum aliquem legittimum
> esse dixeris**; itaquo nee praetermittenda est aliqua praemissa necessaria, et omnes praemissae jam
> ante vel demonstratae esse debent, vel saltem instar hypothesos assumtae, quo casu et conclusio
> hypothetica est."

- **[Historical Claim] Calculation = valid form**: a legitimate calculation is an argument concluding
  by the force of FORM ("vi formae"); soundness requires premises previously demonstrated or honestly
  assumed as hypotheses (making conclusions hypothetical). Clear-and-distinct perception is rejected
  as a truth criterion unless criteria + idea-truth are secured. Label: Historical Claim. Confidence:
  high (text verified in vol. 4 scan; standard cite GP IV 429–430, page marker region consistent).
- Relevance: states the contract of any SIR: outputs are conditional on inputs; no representation
  magic — garbage in, hypothetical out. Directly usable against overclaims for structured prompting.

## 3. SECONDARY: Lenzen's four-calculi reconstruction

**Source:** W. Lenzen, "Leibniz: Logic," Internet Encyclopedia of Philosophy (peer-reviewed),
https://iep.utm.edu/leib-log/ (fetched 2026-08-24), summarizing Lenzen 1990, 2004a (= "Leibniz's
Logic," Handbook of the History of Logic vol. 3), 2004b. EVERYTHING IN THIS SECTION IS SECONDARY.

- **[Known Prior Art, SECONDARY] The fragments form four reconstructible calculi:** (1) the algebra of
  concepts L1 — deductively equivalent to the Boolean algebra of sets; (2) quantificational system L2,
  where "indefinite concepts" function as quantifiers ranging over CONCEPTS (second-order);
  (3) a propositional calculus of strict implication obtained by the strict analogy between concept-
  containment and proposition-inference; (4) the Plus-Minus-Calculus, a theory of set-like containment,
  addition, and subtraction. Confidence: high (secondary consensus per Lenzen).
- **[Historical Claim, SECONDARY] Historiography of failure**: Couturat (1903, who first printed most
  fragments incl. Generales inquisitiones) judged Leibniz's logic "largely failed" and the intensional
  approach "necessarily bound to fail"; Kneale & Kneale 1962: Leibniz "never succeeded in producing a
  calculus which covered even the whole theory of the syllogism"; Liske 1994, Swoyer 1995, Schupp 2000
  argue the intensional conception breeds inconsistency. Rehabilitation line: Dürr 1930, Rescher 1954,
  Kauppi 1960 → Poser 1969, Ishiguro 1972, Rescher 1979, Burkhardt 1980, Schupp 1982, Mugnai 1992;
  systematic reconstruction only from Lenzen 1990 onward. Confidence: high (as report of scholarship).
- **[Observation, SECONDARY] L1 mechanics**: identity axiomatized by reflexivity + substitutivity
  (IDEN 1–2); NO primitive disjunction — it is defined away (A∨B =df ~(~A·~B)); conjunction is
  composition. Extensional interpretation possible because Leibniz's extensions range over POSSIBLE
  individuals ("the region of ideas"), not actual ones — matching P8's possibilist fix read formally.
- **[Observation, SECONDARY] L2 mechanics**: 'A is B' rendered 'A = BY' with Y an indefinite concept;
  negation laws require an explicit POSSIBILITY side-condition (A∉B ↔ ∃Y(P(YA) ∧ YA∈~B)) — i.e.,
  witness terms must be compatible/possible, formalizing P10's composibility check; containment gets a
  universal quantifier reading (CONT 4: A∈B ↔ ∀Y(Y∈A→Y∈B)). NEG 9 (contraposition-with-complement)
  holds only for individual concepts — a scope bug Leibniz himself located.
- **[Observation, SECONDARY] Plus-minus subtleties**: subtraction is NOT generally the converse of
  addition ((A+B)−B = A fails in general); cancellation works only when the subtracted term is
  "uncommunicating" (non-overlapping) with the rest — MINUS 4. Confirms P9's flagged partiality as a
  genuine, later-diagnosed feature rather than sloppiness.
- **[Observation, SECONDARY] Strict implication**: 'If A then B' true iff consequent contained in
  antecedent; p⊃q =df ¬◇(p∧¬q); the same containment semantics runs concepts AND propositions AND
  (via deontic reduction O(α) ↔ □v(α)) norms — one operator family across three domains.
- **Assessment for CE-01**: even the maximally charitable modern reconstruction yields systems that
  are (a) sound and complete ONLY relative to an intended model of all possible individuals, (b)
  second-order once quantification enters, (c) partial on subtraction/cancellation. The engineering
  lesson is not "Leibniz failed" but "concept-containment calculi scale exactly as far as the
  primitive vocabulary and possibility oracle do."

## 4. Protocol §2 extraction schema — characteristica universalis / calculus ratiocinator

| Schema field | Extraction (primary-source grounded; cites = GP vol/page per §2) |
|---|---|
| **Objective** | A written medium in which reasoning proceeds by deterministic calculation: end disputes by "calculemus" (P2, VII 125); make correct procedure mechanical for ordinary minds (P1, VII 14–15); every fallacy a calculation error or grammatical ill-formedness (P6, VII 200–201); also weigh commoda/incommoda and probabilities — a statics of reasons (P2/P3b, VII 125, 188 f.). |
| **Primitive units** | Alphabet of human thoughts: catalog of summ genera a,b,c,... whose combinations yield all other notions (P3b VII 185; P6 VII 198 f.; P10 VII 292 f.). Primitives come in two kinds: DISTINCT simples (self-intelligible, e.g., Ens) and CONFUSED-clear sensibles (e.g., coloratum) definable only ostensively (P10 VII 293 f.; cf. P11 IV 422: primitives known only intuitively, composites only symbolically). Unanalyzed technical characters explicitly tolerated (Chinese analogy, P6 VII 203). |
| **Representation mechanism** | Concepts = products of primitives (Terminus est a.b.ab.bcd, Addenda VII 223–224); arithmetic encoding: characteristic numbers, primes for simples, products for composites so containment ⇔ divisibility (P3b VII 187; P4 VII 189 f.). Signs may be arbitrary OR iconic — diagrams count as characters and their similitude is "non arbitraria" (P5 VII 192). |
| **Composition mechanism** | Juxtaposition/multiplication of terms (ab); unrestricted aggregation of any plurality into one constituent (Postulatum 1, P9 VII 230); dual readings admitted: conjunctive/intensional (subject contains predicate) vs disjunctive/extensional (subject contained in predicate), stated in one sentence (Addenda VII 224; cf. Lenzen SECONDARY §3 on intension/extension duality). Composition is idempotent (A+A=A, egg scholium P9 VII 230). Constraint: combinations must pass a POSSIBILITY/composibility check by experiment or analysis before counting as real definitions (P10 VII 294). |
| **Inference mechanism** | Rewriting system: self-true propositions ab⊇a, ab⊇b; Barbara-transitivity; composition a→b ∧ d→c ⇒ ad→bc; multi-premise aggregation ace⊇bdf; substitution of equivalents salva veritate everywhere, identity DEFINED as mutual substitutability (P7 VII 218–224). Proofs executed by substitution chains (Th. I–V, P9 VII 231 f.). Validity checkable arithmetically on characteristic numbers (P4 VII 190). Scope: universal affirmatives only at first; negatives via non-a terms later; particulars/hypotheticals deferred (P7 VII 218). |
| **Ambiguity handling** | Replace vague words with determinate characters ("a vocabulis vagae incertaeque significationis ad characteres determinatos", P6 VII 200); singulars treated as both universal and particular (P8 VII 211); actual vs possible readings separated — keep terms "in regione idearum" (P8 VII 211 f.); genus/differentia roles made relative, vulgar categories declared wrongly constituted (P10 VII 292 f.). |
| **Extensibility** | Open lexicon of unanalyzed specialist characters alongside analyzed core (Chinese analogy P6 VII 203); nominal definitions = sufficient mark-enumerations, always revisable downward toward primitives (P10 VII 294); sciences compress into fewer general theses over time (P3 VII 180 f.); new truths become corollaries — growth by generalization, not accumulation. |
| **Claimed universality** | ALL human thoughts generated by combination + analysis ("omnia et inveniri et dijudicari possent", P3b VII 185); everything derivable "quodam genere calculi" like arithmetic/algebra problems (P6 VII 198); extends beyond deduction to probability and deliberative weighing (statics of reasons, P3b VII 188 f.; P2 VII 125 f.); missionary/geopolitical hopes attached (P3b VII 189). |
| **Known limitations (self-declared)** | Weights for reasons lack exact signed units ("nulla ... certa nota comprobatis", P2 VII 126); characteristic numbers hard to construct ("characteristicos dare difficillimum est", P3b VII 189); contingent truths need infinite analysis — untraversable except by God (P6 VII 200); compatibility of combinations decidable only by experiment or analysis (P10 VII 294); composite notions unthinkable all-at-once — symbolic thought unavoidable (P11 IV 422); primitives include non-definable sensibles (P10 VII 293 f.). |
| **Failure mode** | See §5. |
| **Modern analogue** | Boolean algebra / term logic (Lenzen SECONDARY: L1 ≡ Boolean algebra); description-logics & concept-containment KR; knowledge-graph ontology engineering (primitive vocabulary + composibility checks ≈ consistency checking); interlingua MT; type systems & proof assistants (fallacy-as-type-error ≈ paralogismus-as-error-calculi); decision/calibration layers over structured arguments ≈ statica rationum; schema-constrained LLM prompting as the interface-level echo of scriptura-erit-meditandi-filum. |
| **Candidate experimental implication** | E1-relevant: test whether a small closed primitive vocabulary + product-style composition (typed conjunction) with an explicit composibility/well-formedness gate measurably improves LLM task fidelity or error detectability over free-form prompting at matched token cost (Protocol §§5–6 accounting); measure whether malformed SIR inputs are more detectable than malformed NL (P1's "ineptiae sese ipsae prodent"). |

## 5. Failure analysis: what failed mechanically vs philosophically

### 5.1 Mechanical failures (engineering, in his own texts)

1. **The primitive inventory never existed.** Every mechanism above is parameterized by the alphabet
   of primitives; Leibniz repeatedly asserts its feasibility but never produces more than toy fragments
   (number tables for small concept sets). His own verdict on existing taxonomies — species are NOT
   combinations of the received genera (P10 VII 292 f.) — applies to every candidate vocabulary he
   had. [Historical Claim, high]
2. **The possibility oracle was never mechanized.** Composibility of primitives "non nisi experimento
   vel resolutione ... judicari potest" (P10 VII 294): the well-formedness gate itself requires either
   empirical experiment or completed analysis — i.e., the two things the calculus was supposed to
   replace. This is circularity at the heart of generation. [Historical Claim, high]
3. **Arithmetic encoding stalls on coprimality.** Divisibility-based validity checking needs
   independent primes for independent concepts; assigning them presupposes knowing which concepts are
   disjoint — again the missing analysis. Characteristic numbers stay "mirabiles" hypotheticals
   (P4 VII 189 f.: "Finge ... jam dari"). [Historical Claim, high]
4. **Subtraction/partiality.** The plus-minus calculus's difference operation has a domain problem
   Leibniz flags himself (find A−B given only A,B, P9 VII 230); cancellation requires disjointness
   (MINUS 4, Lenzen SECONDARY §3). Negative information (what a concept EXCLUDES) resists product
   representation — the same wall Boolean algebra later solved with complements against a universe,
   which Leibniz's system lacks. [Historical Claim, high]
5. **Coverage gaps deferred, never closed.** Negatives/particulars/hypotheticals excluded from the
   Specimen outright (P7 VII 218); relations never enter the object language (no relational terms in
   any extracted fragment — containment is binary and monadic); indexicals, tense, and actual
   existence handled only by stepping outside to metaphysics (infinite analysis, P6 VII 200).
   [Historical Claim, high]

### 5.2 Philosophical failures (of the ambition, not the implementation)

1. **Universality claim outruns the truth theory.** The calculus covers necessary/conceptual truth;
   contingent matters require infinite analysis knowable only to God (P6 VII 200). So the domain where
   disputes actually persist (facts, values, concrete deliberation) is exactly the domain the calculus
   cannot settle — yet the "calculemus" rhetoric promises settlement there too (weighing commoda,
   probabilities, P2/P3b). The program conflates two different calculi: deduction (delivered, in
   embryo) and valuation (never delivered — he says so himself, P2 VII 126). [Historical Claim, high]
2. **Symbol-dependence cuts both ways.** The Dialogus proves thought needs signs (P5 VII 191 f.);
   Meditationes proves symbolic cognition of composites is unavoidable and can degenerate into
   word-fluency mistaken for ideation (P11 IV 422). A notation therefore does not guarantee
   understanding; without the analysis discipline it AMPLIFIES the illusion. The characteristica
   assumed its own abuse case away. [Historical Claim, high]
3. **Ostensive residue.** Primitives include confused-clear sensibles teachable only by showing
   (coloratum, P10 VII 293 f.) — the alphabet cannot be purely combinatorial; some terminals point at
   experience. Universality of the FORM survives, universality of the VOCABULARY cannot. 
   [Historical Claim, high]
4. **Social assumptions.** "5 selected men, 5 years" (P3b VII 187) presumes both a complete analysis
   team and adoption authority (missionary scenario, P3b VII 188 f.); the system's value depends on
   community-wide uptake and shared primitives — an organizational dependency no notation alone
   provides. [Observation, high]

### 5.3 What did NOT fail

The formal core survived red-team scrutiny across three centuries: L1 is Boolean-equivalent, L2
anticipates quantification over concepts, strict implication anticipates modal logic, the PM-calculus
anticipates set algebra with diagnosed limits (Lenzen SECONDARY §3). The failure was not the
calculus ratiocinator but the characteristica's premise that a finished primitive inventory of
EVERYTHING (including values and facts) is obtainable by five people in five years.

## 6. Machine-relevant design principles memo (handoff: Historical Foundations Lead; failure modes → Red Team)

1. **Guide-rail principle** (P1): a representation earns its cost when structure prevents deviation,
   not when it shortens text; evaluate by error-prevention for weaker operators, not elegance.
2. **Self-detecting malformation** (P1, P6): target representations where ill-formed intent is
   syntactically conspicuous ("sophisma = soloecismus"); measurable as malformed-input rejection rate.
3. **Two-layer vocabulary** (P6 Chinese analogy, P10): analyzed primitive core + licensed opaque
   technical terms; do not demand total analysis — demand declared analysis status per term.
4. **Composibility gate** (P10, Lenzen L2 NEG 8): generation must be paired with a possibility/
   compatibility check; unconstrained combination produces confident nonsense.
5. **Dual reading made explicit** (P7 VII 224): pick and DECLARE intensional vs extensional reading
   per predicate; silent switching between them is the historical source of paradox charges.
6. **Deduction vs valuation separation** (P2, P3b, §5.2.1): do not market a proof calculus as a
   decision procedure; if weights/probabilities are needed, they are a separate component with its own
   units — Leibniz's own admission that these lacked exact signs is the cautionary precedent.
7. **Compression-by-generalization** (P3): represent knowledge as few maximal generals + recovery
   discipline; account for recovery overhead per Protocol §6.
8. **Conditional-output honesty** (P12): conclusions inherit hypothesis status of premises; any SIR
   should carry premise-status (demonstrated vs assumed) through inference.

## 7. Gaps and escalations

- **Generales inquisitiones (1686)** — Leibniz's maturest logical manuscript — is NOT in Gerhardt vols
  4/7 (first printed Couturat 1903; confirmed SEP). All Gen.Inq.-derived mechanisms here enter via
  Lenzen SECONDARY §3 only. Escalate: if Historical Foundations Lead wants Gen.Inq. primary extraction,
  assign a follow-up worker with Couturat Opuscules (IA has scans) or Schupp's edition.
- **Vol.-4 page-marker OCR is patchy** around the Discours region; P12 cite given as standard location
  consistent with observed markers, confidence noted med-high rather than high on exact page split.
- Item XIV's precise printed title could not be isolated from OCR noise; content attribution
  ("De organo sive arte magna cogitandi") follows Gerhardt's item numbering (XIV) and running headers
  seen in scan; flag low confidence on the TITLE string, high on the passage locations.
- Not attempted within budget: Dissertatio de arte combinatoria (1666) deep extraction — covered by
  pre-Leibniz worker's salvage assets (literature/pre_leibniz/sources/loemker_dac.txt); correspondence
  with Duke Johann Friedrich (GP I 363 ff.) and letter to Gallois — outside vols 4/7.

## 8. Run summary

- hours_spent: ~3.5 (honest estimate: ~0.4 doc/scope setup; ~1.6 source acquisition + page-map
  calibration + passage extraction; ~0.3 secondary; ~1.2 writing/analysis/finalization)
- files_written:
  - literature/leibniz_extraction.md (716 lines) — this file
  - literature/leibniz/sources/gp4_djvu.txt, gp7_djvu.txt (downloaded IA scans, 1.6 MB each; sources,
    not authored content)
  - literature/leibniz/sources/probe.py (scratch locator script, kept for reproducibility)
- top_findings:
  1. "Calculemus" in the primary text includes probabilistic/valuational weighing (statics of
     reasons), not just deduction — and Leibniz himself records that the needed value-units were
     never constructed (GP VII 125–126, 188 f.).
  2. The calculus ratiocinator's actual delivered mechanism is a substitution rewriting system over
     term-products with a declared intensional/extensional dual semantic clause (GP VII 224), plus
     self-flagged partiality bugs (subtraction domain, VII 230).
  3. Truth theory is representational: necessary = finite reduction to identities; contingent =
     infinite analysis (God-only) — contingency DEFINED as analytic unboundedness (GP VII 200).
  4. Primitive handling is explicitly two-tier (distinct vs confused-ostensive) with a mandatory
     composibility gate judged by experiment or analysis — i.e., the system's own well-formedness
     oracle is outside the calculus (GP VII 293 f.).
  5. Ambition-vs-implementation anchor: "5 selected men, 5 years" for the whole alphabet +
     characteristic numbers (GP VII 187); nothing near this was built, while the formal core
     independently proved durable (Lenzen's Boolean-equivalence result).
- escalations: Gen.Inq. primary-text gap (needs Couturat/Schupp follow-up); item-XIV title-string
  uncertainty; Discours vol.-4 page-marker OCR patchiness (all logged in §7).


