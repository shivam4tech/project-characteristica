# Research Protocol

## 1. Source Discipline

Historical and technical claims must be linked to identifiable sources.

Prefer, where possible:

1. primary sources
2. peer-reviewed papers
3. books from reputable academic publishers
4. official technical documentation
5. reputable secondary scholarship

Search-result snippets alone are not sufficient evidence.

Every important claim should record:

- claim
- source
- location/page/section when available
- confidence
- interpretation
- relevance to Project Characteristica

## 2. Historical Extraction Rule

Historical research must not end with summary.

For every relevant historical system, extract:

- objective
- primitive units
- representation mechanism
- composition mechanism
- inference mechanism
- ambiguity handling
- extensibility
- claimed universality
- known limitations
- failure mode
- modern analogue
- candidate experimental implication

## 3. Prior-Art Rule

Before labeling anything potentially novel, search for existing work in:

- semantic parsing
- meaning representation
- formal semantics
- knowledge representation
- ontologies
- knowledge graphs
- compiler intermediate representations
- prompt compression
- structured prompting
- tool/function calling
- program synthesis
- neuro-symbolic AI
- representation learning
- interlingua systems
- controlled natural languages
- formal logic
- machine-to-machine communication

Potential novelty must survive an independent prior-art review.

## 4. Experimental Baselines

Every experiment must compare against at least one strong natural-language baseline.

When practical, compare against:

- ordinary natural-language prompt
- optimized natural-language prompt
- structured JSON or schema prompt
- proposed Characteristica representation

Do not compare only against intentionally weak prompts.

## 5. Core Metrics

Measure as applicable:

- input tokens
- output tokens
- total tokens
- task accuracy
- semantic fidelity
- completion rate
- latency
- API/inference cost
- conversion overhead
- model-specific adaptation overhead
- robustness to paraphrase
- portability across models
- portability across tasks
- human readability where relevant

## 6. Compression Accounting

Never report token savings without accounting for necessary representation instructions.

If the model requires a schema definition, grammar explanation, decoder prompt, few-shot examples, or adapter prompt, their cost must be included or amortized explicitly.

## 7. Generalization

A representation should not be considered broadly useful based on one task family.

Whenever feasible, test distinct task classes such as:

- extraction
- classification
- retrieval
- planning
- reasoning
- coding
- tool use
- constraint satisfaction
- document analysis

## 8. Cross-Model Testing

Whenever feasible, test the same representation against multiple independently developed model families.

Model-specific adapters are allowed, but the underlying semantic representation must remain stable for a cross-model portability claim.

## 9. Red-Team Requirement

Important positive findings must be reviewed by an agent tasked to disprove them.

The red team should search for:

- semantic loss
- unfair baselines
- hidden overhead
- benchmark leakage
- task-specific overfitting
- model-specific dependence
- prior art
- scalability problems
- undecidability or expressiveness limitations
- misleading metrics

## 10. Decision Standard

CE-01 does not need to produce a finished language.

It succeeds if it produces enough evidence for a defensible GREEN, AMBER, or RED decision.

A GREEN recommendation should ideally contain at least one of:

- reproducible efficiency gain
- reproducible reliability gain
- meaningful cross-model portability
- a technically plausible underexplored mechanism
- a candidate representation architecture surviving red-team scrutiny

A RED recommendation should identify clearly why continued research is unlikely to be worthwhile.
