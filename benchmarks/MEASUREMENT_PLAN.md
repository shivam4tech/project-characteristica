# MEASUREMENT_PLAN.md — CE-01 Cost & Semantic-Fidelity Measurement Plan

**Owner:** W16-INFOTH (Information Theory / Compression Researcher), workstream WS-INFOTH
**Date:** 2026-08-24 · **Status:** P1 deliverable — binding for E1 pre-registration
**Mandate source:** `agents/ORGANIZATION.md` §10; `RESEARCH_PROTOCOL.md` §§5–6; `benchmarks/BENCHMARK_DESIGN.md` §3 ("semantic fidelity … fixed by the measurement plan, OQ12"); `OPEN_QUESTIONS.md` OQ12 (fidelity operationalization) and OQ8 (conversion-overhead protocol).

**Note on labels:** Per worker brief, empirical/methodological claims below carry charter finding labels + source + confidence. Design prescriptions (formulas, procedures) are not truth-claims and are unlabeled; they become binding only when the Experimental Engineering Lead adopts them in an experiment pre-registration.

---

## 0. Purpose and scope

This plan fixes, **before any data collection**, (a) exactly what counts toward "cost" in every CE-01 comparison, (b) how "semantic fidelity" is operationalized so it is measurable and hard to game (OQ12), (c) why naive token-counting is rejected as an efficiency metric, and (d) the measurement protocol for pilot experiment E1 (candidate SIR vs strong NL prompting baselines). It is representation-agnostic: it does not assume or design any SIR format (P1 no-design rule); whatever candidate the Chief Scientist registers in P2 will be measured by these rules unchanged.

Binding constraints honored: charter principles 7–9 and anti-goals ("equating short prompts with semantic efficiency", "optimizing exclusively for token count", "hiding complexity in compilers or adapters"); Protocol §4 (strong baselines mandatory), §5 (metric list), §6 (never report token savings without accounting for representation instructions); BENCHMARK_DESIGN §1 (four arms), §3 (required measurements), §4 (fairness rules), §5 (pre-registration before execution).

---

## 1. What counts as cost

Every quantity below is metered **per arm, per task item, per attempt**, logged to the run manifest (§5), and reported for all arms including unfavorable ones. "Attempt" = one API request; retries are new attempts and their costs count (§1.7).

### 1.1 Token costs

| Symbol | Quantity | Definition |
|---|---|---|
| `V_in` | Variable input tokens | All request input on a given attempt **minus** the fixed instruction block `F`: task payload, source text/inputs, conversation history when applicable |
| `F` | Fixed instruction tokens | Schema definition, grammar/format rules, decoder instructions, few-shot examples — i.e., everything in a prompt that is identical across items of the same condition. Counted at full length on every request that carries them |
| `V_out` | Output tokens | Model-generated response tokens, including any required reformatting/self-check preamble the condition's own instructions induce |
| `R` | Retry tokens | Tokens consumed by attempts triggered by parse/validation failure of a prior attempt |

Raw token counts are recorded **per model tokenizer actually used** (tokenizer id logged in manifest). Because tokenizers differ across model families, cross-model comparisons are made in the normalized units of §1.6 and §2 (objection 1), never raw tokens alone.

### 1.2 Conversion overhead (Protocol §6; OQ8)

The SIR arm's pipeline is Human Intent → NL → **conversion** → SIR → model. The conversion stage is a first-class cost object:

- `K_tok` — converter input+output tokens (if the converter is an LLM call: its own `V_in/V_out/F_conv/R_conv`, all metered identically).
- `K_time` — converter wall-clock latency.
- `K_err` — converter error rate: fraction of conversions failing validation or losing content units per the F2 audit (§3.2). Conversion errors are charged to the SIR arm end-to-end, never silently repaired.
- `K_human` — human authoring minutes if any condition assumes hand-authored payloads (logged, reported, not folded into $ metrics — see §1.8).

**Charging rule:** conversion cost is charged per-query (`K`) unless converter output is genuinely reusable across queries sharing one intent template, in which case `K/N_conv` with the reuse count `N_conv` **pre-declared in the registration** (default `N_conv = 1`; never chosen after seeing results). Both charging modes are reported.

### 1.3 Adapter / model-adaptation overhead

Any per-model wrapping needed to make the same underlying representation consumable (adapter preamble, model-specific format hints) counts as fixed cost `F_adapter` and is amortized over the same declared reuse count as `F`. Protocol §8 allows model-specific adapters but requires the underlying representation to stay stable; the plan enforces this by logging an adapter-content hash per model family — differing adapters must be disclosed in the results manifest.

### 1.4 Amortization rules and formulas

Per-arm, per-query amortized cost at declared reuse count `N` (tokens):

```
A(N) = V_in + V_out + E[R] + F/N
```

Dollar cost using the price vector `(p_in, p_out)` recorded per model at run date (§1.6):

```
$(N) = p_in·(V_in + F/N + E[R_in]) + p_out·(V_out + E[R_out])
```

End-to-end SIR arm total (converter included):

```
Total_SIR(N, N_conv) = $(N)_SIR + K(N_conv)
```

Net advantage vs baseline arm `B`:

```
Δ(N) = $(N)_B − Total_SIR(N, N_conv)
```

**Break-even reuse count:** smallest integer `N*` with `Δ(N*) > 0`. Every efficiency claim reports the full curve `Δ(N)` for `N ∈ {1, 10, 25, 100}`, not a single favored point. This makes hypothesis H3-candidate (registry: gains exist only under reuse) directly testable from E1 data.

**Symmetry rule (BENCHMARK_DESIGN §4.3):** NL arms get identical treatment — their own reusable blocks (system persona, standing instructions, examples) are also split into `F_NL` / `V_NL` and amortized over the same declared `N`. One-sided amortization is prohibited.

### 1.5 Latency

Measured end-to-end through the full pipeline: request dispatch → last response token received; for the SIR arm this includes the conversion stage. Report p50 and p95 per arm; time-to-first-token separately where the API exposes it. All arms measured in the same time window, same region/endpoint, same concurrency; queue-time anomalies (>3× median) are re-run and both readings logged.

Latency matters independently of tokens because structured payloads can change decoding behavior (long constrained generations, speculative formats); a token-saving representation that adds a serial conversion round-trip can lose net latency. No latency claim may be derived from token counts; only measured wall clock counts.

### 1.6 API/inference cost

Dollar cost computed from the provider's published per-token prices for the exact model version tested, with the price vector + retrieval date + source URL recorded in the run manifest. Declared policies: caching disabled or cold-cache measurement (declare which, apply to all arms equally); batch discounts unused; output/input price asymmetry handled explicitly by the formula in §1.4 (output-token prices commonly exceed input by a large factor — recording the actual vector at run time is mandatory rather than assuming a constant).

Because raw tokens are not comparable across model families (different tokenizers/vocabularies), the canonical normalized cost units for cross-model claims are: **USD per task** and **characters per task**, with raw tokens reported alongside for diagnostics only.

### 1.7 Failure costs

Parse failures, schema-validation failures, and malformed outputs are counted as failures (BENCHMARK_DESIGN §3) **and** their token/latency/$ cost stays in the arm's totals via expected retry cost `E[R]`. Dropping failed runs from cost averages while keeping them out of success rates — either direction — is prohibited; report both unconditional (per dispatched task) and conditional (per successful task) statistics.

### 1.8 What does *not* count (exclusions)

- One-time human engineering of prompts/schemas/parsers (real cost, but identical-in-kind across serious arms; instead each arm's engineering effort is disclosed qualitatively per BENCHMARK_DESIGN §4.2).
- Infrastructure identical across arms (SDK, harness compute).
- Human authoring minutes (`K_human`) are disclosed but excluded from $ metrics, since no arm in E1 assumes sustained hand-authoring; if a future expedition assumes operator-authored SIRs, `K_human` becomes a first-class metric there.

### 1.9 Worked example (illustrative numbers only, not predictions)

Suppose for one extraction item: NL-opt arm `V_in=420, F_NL=150, V_out=180`; SIR arm `V_in=140, F_sir=600, V_out=120`; LLM converter `K_tok(in,out)=310+95`; prices `p_in=$1/M, p_out=$4/M`.

- `N=1`: NL-opt ≈ (420+150)·1e-6·$1 + 180·1e-6·$4 = $0.00129/query. SIR ≈ (140+600)·1e-6·$1 + 120·1e-6·$4 + (310+95)·1e-6·$1 ≈ $0.00194/query → **SIR loses** despite a 40% smaller payload.
- `N=25`, converter reused per template (`N_conv=10`): SIR ≈ (140+600/25)·1e-6·$1 + 120·1e-6·$4 + 405/10·1e-6·$1 ≈ $0.00067/query → SIR wins ~1.9× **if** fidelity holds.

The example shows the plan's central point: sign and size of the advantage are functions of `N`, `N_conv`, and fidelity — none of which a payload-token comparison reveals.

---

## 2. Critique of naive token-counting

**Claim (Observation).** Raw prompt-token counts are invalid as a measure of "semantic efficiency" for the SIR question, on at least eight independent grounds. Confidence: high. Source: this section's arguments; charter anti-goals ("equating short prompts with semantic efficiency", "optimizing exclusively for token count") already prohibit the practice; each ground below is independently checkable.

1. **Tokens are model-relative, not a substance.** Different model families use different vocabularies/tokenizers; the same string yields different token counts under different tokenizers, so "the SIR uses 40% fewer tokens" is ill-defined until a tokenizer is named, and any such ratio generally fails to transfer across families. A representation whose advantage exists only under one vendor's tokenizer is tokenizer-fit, not semantic compression — and would contradict the model-independence claim under test (OQ6). *Prescription:* raw tokens are diagnostics per tokenizer id; cross-model claims use $/task and chars/task.

2. **Token count measures length, not information.** Information-theoretically, cost-of-transmission is governed by code length relative to a distribution, not symbol count: predictable symbols carry little information, dense ones much. A 600-token schema that fully determines output structure may convey more task-relevant constraint than 150 free-text tokens, and vice versa. No token count distinguishes these. The honest framing is description length of the intent under an agreed code (MDL-style), which for our purposes decomposes into the metered objects of §1 rather than a single number.

3. **Format overhead is asymmetric and confounds structure with waste.** Punctuation-heavy serializations (JSON/XML) tokenize wastefully, so structured arms get inflated apparent input costs for reasons unrelated to their semantics; conversely, whitespace-clever formats look cheap while possibly degrading decoder reliability. Comparing arms on raw tokens rewards serialization tricks — an optimization orthogonal to the SIR hypothesis.

4. **The decoder side is ignored.** A prompt is not a message in a pipe; it is a conditioning object for a stochastic decoder. Equal-length prompts are not equally *usable*: what matters is whether task-relevant meaning survives into behavior. Hence efficiency must be joint — cost per unit of delivered, checked fidelity (§4.4 decision rule) — never length alone.

5. **Output tokens dominate many tasks and are priced differently.** In generation-heavy families the response, not the prompt, drives $ and latency; input-only savings claims mislead. Input/output price asymmetry means total-token comparisons also misweight actual dollars (§1.4 formula handles this explicitly).

6. **Fixed costs exist on both sides; amortization is a first-class variable.** Schema/decoder blocks (`F`) are amortizable fixed costs, but so are NL prompts' reusable components. Reporting payload savings without declaring `N` and charging `F/N` (Protocol §6 violation) can manufacture arbitrary "efficiency". Conversely, honest amortization over large `N` is exactly where an SIR could legitimately win — the plan makes the reuse curve, not a point estimate, the reported object.

7. **Redundancy in NL is functional, not waste.** Natural language's paraphrase-ability and local redundancy act like channel coding for an unreliable decoder: they make intent robust to wording, omissions, and model quirks. Aggressive compression removes exactly this slack, so shorter inputs can be *less* reliable per token spent. Related hypothesis registered below (§3.5, H-C2): compressed representations should degrade more under paraphrase — testable in E2.

8. **Single-number summaries invite gaming.** Any scalar "compression ratio" can be maximized by degenerate encodings unless fidelity is gated first. The plan therefore gates all efficiency claims on pre-registered fidelity non-inferiority margins (§4.4).

**Known Prior Art (contextual, verified metadata only).** Token-level prompt compression aimed directly at inference cost already exists as a research area — e.g., LLMLingua, "Compressing Prompts for Accelerated Inference of Large Language Models," EMNLP 2023 (arXiv:2310.05736; venue/title verified from arXiv record 2026-08-24). Its performance figures are NOT cited here: full text has not been read in this workstream; quantitative reuse belongs to WS-MODERN's prior-art map (Protocol §3 domain: prompt compression). Relevance: the field's existence shows "shorter prompts at preserved quality" is occupied territory; CE-01's differentiator must be *representation-level* claims (structure, portability, compositionality), measured with full conversion accounting — which is precisely what this plan meters.

**What replaces naive counting:** the joint statistic of §4.4 — amortized end-to-end $ (and latency) per dispatched task, gated by non-inferiority on operationalized fidelity — reported as a Pareto plane (cost vs fidelity), with all four BENCHMARK_DESIGN arms present.

---

## 3. Semantic fidelity operationalization (resolves OQ12's definition stage)

**Design commitment.** "Semantic fidelity" is not one metric but a four-layer stack, F0→F3, each mechanically scorable or auditable, with F1 primary and the others diagnostic/gating. The stack is fixed **before** data collection; changing it after seeing results invalidates the run (BENCHMARK_DESIGN §4.5–4.6).

### 3.1 The fidelity stack

| Layer | Question answered | Measurement | Role |
|---|---|---|---|
| **F0 format validity** | Did the arm produce an in-contract output at all? | Binary: parses + conforms to that arm's declared output contract | Gate: F0 fail ⇒ task scored as failure; never dropped |
| **F1 task correctness** | Is the answer right? | Pre-registered checker per family: programmatic exact/constraint checks where possible; anchored rubric only where no checker is constructible (rubric + anchors fixed pre-run) | **Primary endpoint** for effectiveness |
| **F2 content-unit preservation** | Did task-relevant meaning survive conversion/execution? | Audit metric on ≥20% stratified sample per cell (§3.2) | Diagnostic: separates converter loss from decoder loss |
| **F3 round-trip stability** | Does the representation survive encode→decode→encode? | Canonical-normalization equality of SIR vs SIR′ after decode(SIR)→NL′→re-encode; non-identical cases go to the equivalence panel (§3.3) | Diagnostic: representation self-consistency |

Rationale: F1 alone cannot say *where* meaning was lost (conversion vs decoding); F2 attributes loss to pipeline stages; F3 detects representations whose decoding is unstable even when single-pass outputs look fine.

### 3.2 Content-unit annotation protocol (F2)

Before any model call, each task item's source intent is decomposed into atomic **content units** from a closed taxonomy:

`entity` · `relation/predicate` · `quantity+unit` · `temporal qualifier` · `constraint (hard/soft)` · `quantifier scope` · `modality/certainty` · `negation` · `priority/preference order` · `output-shape requirement` · `speech-act/intent type` · `audience/style constraint` · `exclusion (what NOT to do)`

Rules:
1. Units are extracted **from the source intent + gold answer only**, by annotators (or procedure) blind to which arms will run — units must not be derived from any arm's output, which would make fidelity self-fulfilling.
2. Each unit gets an id and the gold answer must reference the units it exercises (checker↔unit traceability).
3. Two scores are computed on sampled items: **conversion fidelity** = fraction of units recoverable from the SIR payload alone (attributes loss to NL→SIR conversion), and **end-to-end behavioral fidelity** = fraction of units correctly reflected in the final output (includes decoder-side loss). Their difference localizes where meaning died.
4. Unit taxonomy extensions mid-experiment are prohibited; if a unit type is discovered missing, it is logged as an incident, applied prospectively only, and disclosed.

### 3.3 Judge policy (where human-scale grading is impossible)

For open-ended families where no programmatic checker exists:
- Minimum two judges from **independent model families**, neither being a tested model where avoidable; judge prompts published verbatim in the experiment record.
- Position-swap mitigation for pairwise judging; verbosity and self-preference biases are known failure modes of LLM-as-judge (**Known Prior Art:** Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 D&B, arXiv:2306.05685 — position, verbosity, self-enhancement biases documented; abstract verified 2026-08-24).
- Inter-judge agreement reported; all disagreements plus a random 10% of agreements go to human adjudication within budget; judge-vs-human agreement rate is itself reported.
- Per charter anti-goal, LLM agreement is treated as **fallible measurement instrument**, never as evidence of truth; rubric anchors and gold answers outrank judges wherever they conflict.

### 3.4 Gaming-resistance argument

The operationalization resists the known gaming routes: (i) checkers/rubrics/margins frozen before data collection (BENCHMARK_DESIGN §4.4–4.5); (ii) content units derived blind from source+gold, so arms cannot inflate their own fidelity scores; (iii) parse failures count as failures *and* their cost stays in totals (§1.7), so reformatting loops can't hide losses; (iv) efficiency claims require pre-registered non-inferiority margin δ (§4.4), so tiny fidelity collapses can't buy token wins; (v) symmetric engineering/amortization rules prevent straw-manning baselines; (vi) all conditions reported including unfavorable families; (vii) judge prompts and adjudication rates published; (viii) conversion errors charged to the SIR arm end-to-end — an ideal hand-authored SIR can never silently stand in for the real pipeline.

### 3.5 Theoretical limits registered as claims

- **Claim H-C1 (Observation).** Perfect losslessness is not a coherent target for arbitrary intents: deciding semantic equivalence of expressive representations is undecidable in general (standard computability results — equivalence of programs/formulas in sufficiently expressive systems; Rice-style arguments). Confidence: high. Source: standard computability theory; implication drawn here. *Consequence:* fidelity is necessarily defined relative to a bounded content-unit taxonomy over a declared task distribution — exactly what §3.2 does — and any claim of "no material semantic loss" must name its taxonomy and distribution.
- **Claim H-C2 (Hypothesis, candidate for registry alongside H3-candidate).** Because NL redundancy functions as error-correction for a noisy decoder (§2 ground 7), compressed/structured intents will show larger performance deltas under paraphrase than plain NL. Confidence: medium. Testable: E2 paraphrase sets; would explain any pattern where SIR wins clean-room accuracy but loses robustness.

---

## 4. Measurement protocol for E1 (efficiency/fidelity pilot)

E1 is the discriminating experiment for H1/H0 (`hypotheses/REGISTRY.md`) and the evidence source for OQ4/OQ5/OQ8. This section defines its measurement skeleton; the Experimental Engineering Lead instantiates it in `experiments/E1_PRE_REGISTRATION.md` — including predicted outcomes — **before** any run (BENCHMARK_DESIGN §5).

### 4.1 Arms

Per BENCHMARK_DESIGN §1, all four mandatory arms: **NL-plain**, **NL-optimized**, **JSON/schema** (schema instructions included in `F`), **Characteristica SIR** (schema/decoder instructions included in `F`; conversion stage per §1.2).

Proposed addition — **SIR-oracle** diagnostic sub-condition: same SIR payloads but authored by template/hand, conversion cost and errors excluded from its totals (reported separately). Purpose: decompose any observed effect into *representation-intrinsic* vs *pipeline-attributable* — without it, a null result cannot distinguish "bad representation" from "lossy converter," and a positive one can't show the pipeline preserves the gain. Requires Director ruling since BENCHMARK_DESIGN §1 fixes four arms (escalation E2 below); if disallowed, run it as a post-hoc diagnostic clearly labeled non-confirmatory.

### 4.2 Task families (recommendation; final choice gated on P2)

Selection rule is fixed by BENCHMARK_DESIGN §2: families where P1/P2 mechanism claims predict differential advantage **plus ≥1 family where the SIR is predicted to lose**. Because those mechanism claims do not exist yet (P1 running concurrently), this plan recommends provisionally:

1. **Extraction** (structured fields from messy text) — fidelity vs compactness directly observable via F1/F2.
2. **Constraint satisfaction or planning** (constraints + preferences) — compositionality/quantifier-scope stress; exercises the F2 units that most plausibly differ between NL and structure.
3. **Tool use / function calling** — adversarial family: native structured territory where JSON baselines are strongest, so SIR predicted to lose (falsification value).

Marked provisional pending P2 mechanism claims; if P2 predicts differently, the pre-registration follows BENCHMARK_DESIGN's rule, not this list.

### 4.3 Metering procedure

Every request logs to the manifest (§5): arm, item id, paraphrase flag, attempt index, model id/version/date, tokenizer id, temperature/max_tokens/seed, per-attempt input/output tokens split into `V`/`F` components, latency (p50/p95 computed at analysis), parse status, checker outcome, fidelity grades where sampled, price vector used with retrieval date. Converter calls log identically under the SIR arm with `stage=convert`.

### 4.4 Endpoints and decision rule

Primary effectiveness endpoint: **F0-gated F1 success rate** per cell. Primary efficiency endpoints: amortized end-to-end $ per dispatched task at declared reuse counts `N ∈ {1, 25}` (both reported; `N_conv` default 1), plus p95 latency. Secondary/diagnostic: raw token splits, F2/F3 audits, robustness delta on paraphrase variants.

**H1 support in a task family requires ALL of:**
1. SIR arm beats the **strongest** baseline arm on the primary efficiency endpoint with bootstrap 95% CI excluding zero (item-level paired bootstrap);
2. fidelity non-inferiority: F1(SIR) ≥ F1(strongest baseline) − δ, δ pre-registered per family (default 5 points; tighter for programmatic-checker families);
3. replication across ≥3 seeds/task-splits (or deterministic runs across 3 item shuffles);
4. survival of red-team review of overhead accounting and baseline strength (Protocol §9).

Any failure ⇒ no H1 support from that family. H0 stands unless ≥1 family passes all four (registry falsification criteria). Results are reported as a Pareto plane ($ per task vs F1 success) per family; scalar ratios are not decision statistics.

### 4.5 Sample size and power honesty

Computed for two independent proportions (α=.05 two-sided, power=.80, base rate ≈0.7): minimum detectable difference ≈ 33 pts at n=30/cell, ≈ 26 pts at n=50/cell, ≈ 20 pts at n=80/cell (computed 2026-08-24; paired designs improve on this and should be preferred — record the actual analysis plan in the pre-registration). *Consequence:* CE-01-scale pilots can only detect large effects; verdict language must say "no detectable advantage at CE-01 scale," never "no advantage" (already flagged in H0's registry entry). Recommend ≥50 items/family/cell with paired item-level analysis.

### 4.6 Stopping rule

Fixed-n design; no interim peeking for the primary endpoint (optional pre-registered alpha-spending boundary allowed only if declared before the run). Runs aborted for external causes (API outage) restart from the last completed cell; aborts logged.

### 4.7 Predicted outcomes to register before running

The pre-registration must state, per arm × family: predicted sign on success, cost, latency, and which F2 unit types are expected lost in conversion — even where the prediction is "no difference." For the adversarial family (§4.2), the registered prediction is an SIR loss; a win there is high-value and will be red-teamed hardest.

### 4.8 What E1 does *not* measure (deferred)

Cross-model portability (OQ6) and full paraphrase-robustness curves (H-C2) belong to E2 unless budget permits adding ≥1 second model family to E1; the pre-registration declares which. Human readability is reported qualitatively only (Protocol §5 lists it "where relevant"); no readability score is invented.

---

## 5. Reporting requirements and result schema

Raw outputs land in `results/E1/`: `runs.csv` (one row per attempt, manifest fields of §4.3), `conversions.csv` (converter attempts + validation status), `fidelity_audit.csv` (F2 unit ids × items × stages), `manifest.json` (models, prices+sources, tokenizer ids, seeds, N/N_conv declarations, software versions). Analysis notebook/script must run top-to-bottom on these files alone. Every excluded run needs written justification in the experiment record + flag in `CLAIM_LEDGER.md` (via Director transcription per STATUS.md session note).

---

## 6. Limitations of this plan (honest scope)

- The plan is representation-agnostic by design; concrete `F` sizes, converter error rates, and δ calibration can only be validated once a candidate SIR exists (P2). Values proposed here are defaults, not empirical claims.
- Price vectors drift; all $ results are date-stamped to their recorded vectors and never compared across dates.
- Power ceiling (§4.5): small real advantages (<10 pts) are invisible at CE-01 scale regardless of arm count.
- F2 taxonomy is necessarily incomplete for unforeseen intent types (mitigation: incident logging, prospective extension).
- Judge-based grading inherits known judge biases despite mitigations (§3.3); human adjudication coverage is budget-limited.

## 7. Claim register (for Curator/Director transcription into CLAIM_LEDGER.md)

| ID | Label | Claim | Confidence | Source |
|---|---|---|---|---|
| C-INFOTH-1 | Observation | Raw token counts are invalid cross-model efficiency metrics (8 grounds, §2) | High | This doc §2; charter anti-goals |
| C-INFOTH-2 | Observation | Lossless semantic preservation is undecidable for arbitrary intents; fidelity must be taxonomy-relative (§3.5 H-C1) | High | Standard computability theory |
| C-INFOTH-3 | Hypothesis | Compressed/structured intents degrade more than plain NL under paraphrase (redundancy-as-channel-coding) (§3.5 H-C2) — candidate sub-hypothesis alongside H3 | Medium | This doc §2.7, §3.5 |
| C-INFOTH-4 | Known Prior Art | Token-level prompt compression for inference acceleration exists as a field; LLMLingua (EMNLP 2023, arXiv:2310.05736) verified metadata-only; figures deferred to WS-MODERN | High (existence) / n.a. (figures) | arXiv record, retrieved 2026-08-24 |
| C-INFOTH-5 | Known Prior Art | LLM-as-judge carries position/verbosity/self-enhancement biases → multi-family judges + human adjudication required (§3.3) | High | Zheng et al., NeurIPS 2023 D&B, arXiv:2306.05685, abstract verified |

**Handoff:** metrics + decision rule → Experimental Engineering Lead for `experiments/E1_PRE_REGISTRATION.md`; H-C2 → Chief Scientist/Curator as candidate derived hypothesis; prior-art pointers → Modern Representation Researcher / Prior-Art Investigator.

*End of measurement plan. Written incrementally in four checkpointed stages per worker brief.*



