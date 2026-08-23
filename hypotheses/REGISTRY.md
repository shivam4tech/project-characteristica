# Hypothesis Registry

Canonical registry of hypotheses. Statuses: `registered` → `under-investigation` → `supported` / `falsified` / `unresolved`. Only falsifiable hypotheses are admitted; each must name experiments able to discriminate it from alternatives.

---

## H1 — Central Hypothesis

- **Statement:** For at least some broad classes of AI tasks, a model-independent semantic intermediate representation can communicate equivalent task intent more efficiently and/or reliably than conventional natural-language prompting, after accounting for representation-conversion overhead.
- **Motivation:** Working architecture in `RESEARCH_QUESTION.md`; charter's core hypothesis; recurring historical ambition (Llull → Leibniz → symbolic logic → interlinguas → semantic representations) that has never been decisively tested against *modern strong* prompting baselines.
- **Falsification criteria:** Across all pre-registered task families in a methodologically clean pilot (strong baselines: ordinary NL, optimized NL, structured JSON/schema; full overhead accounting per Protocol §6), no condition shows a material advantage on any registered metric that survives red-team review — i.e., H0 cannot be rejected for every tested class. A single failed task family does not falsify ("some broad classes"); failure across all tested classes does, subject to the scope caveat below.
- **Measurable variables:** input/output/total tokens; API/inference cost; latency; task accuracy/success rate; semantic fidelity (operationalized per OQ12); conversion overhead (tokens+time+error); adapter overhead; robustness to paraphrase; cross-model delta; cross-task delta.
- **Predicted outcomes if true:** ≥1 task family shows net gain (typically consistency/fidelity or multi-turn/tool-call token efficiency) that holds against optimized-NL baseline and replicates across seeds; gains survive inclusion of one-time schema/conversion amortization over realistic reuse counts.
- **Strongest competing explanation:** Any apparent advantage is explained by prompt engineering quality (the JSON/schema baseline captures everything an SIR offers), or by hidden overhead making net effect ≤ 0 once conversion is honestly counted.
- **Discriminating experiments:** E1 efficiency/fidelity pilot (2–3 task families × 4 arms); E2 robustness/portability probe (paraphrase sets, ≥2 model families) if E1 shows signal.
- **Scope caveat:** Falsification within CE-01 applies to tested task families and models only; generalization claims beyond them require new registration.
- **Status:** `registered` (untested)
- **Registered:** Expedition initialization (CE-01)

## H0 — Null Hypothesis

- **Statement:** After accounting for conversion, decoding, schema overhead, model adaptation, and performance loss, semantic intermediate representations provide no meaningful general advantage over strong natural-language prompting.
- **Motivation:** Default skeptical position; charter principle "compression must account for decoding and translation overhead" makes this the conservative prior given decades of interlingua/formal-representation shortfalls outside narrow domains.
- **Falsification criteria:** A pre-registered experiment demonstrates a material, replicable net advantage for an SIR over the strongest NL baseline in ≥1 broad task family, surviving red-team review of baselines and overhead accounting.
- **Measurable variables:** identical to H1 (same experiments discriminate both).
- **Predicted outcomes if true:** All four arms statistically indistinguishable after overhead accounting; or apparent SIR gains fully absorbed by the optimized-JSON arm; conversion overhead ≥ savings in all conditions.
- **Strongest competing explanation:** n/a (null), but its own strongest rival is that pilot scale (2–3 task families) lacks power to detect small real effects — hence verdict language must distinguish "no evidence of advantage at CE-01 scale" from "advantage impossible."
- **Discriminating experiments:** shared with H1 (E1/E2).
- **Status:** `registered` (untested)

---

## Derived sub-hypotheses

_To be registered during P2 synthesis by the Chief Scientist via the Curator, each following the same template. Candidates anticipated (not yet registered):_

- H2 (candidate): compositional primitive vocabularies improve *consistency* (variance reduction) even where mean accuracy is unchanged.
- H3 (candidate): conversion overhead amortizes favorably only under reuse (multi-turn / repeated task templates) — predicting an interaction between reuse count and net benefit.

## Registration rules

1. New hypotheses enter as `registered` with all fields filled before related work begins.
2. Status changes require citing the discriminating experiment record(s).
3. Sub-hypotheses must trace to ≥1 mechanism claim in `CLAIM_LEDGER.md`.
