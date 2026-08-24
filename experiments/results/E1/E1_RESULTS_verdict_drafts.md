> **STATUS 01:35 IST 08-25:** SUPERSEDED — all three blocks are now INCORPORATED in `E1_RESULTS.md`
> (header mixed-batch note, §8 H3 verdict, §8 H5 N/A note) on the Amendment-2 basis. Kept for provenance.

# E1_RESULTS.md — prepared insertions for the completing session

_Drafted 2026-08-25 ~01:30 IST (WS-E1EXEC wait/analysis pass). `make_results.py` does NOT emit
these three blocks. After a clean make_results run on complete data: insert (i) immediately after
the P8-flag line in the header; append (ii) and (iii) at the end of §8 (before the H1/H0 section
or directly after it — order within §8 is not load-bearing, completeness is). Do NOT alter any
auto-generated number or verdict line._

## (i) Mixed-batch header note — insert after the P8 flag blockquote

**Mixed-batch note:** scored calls span an operator key/quota reset (the 2026-08-24 evening
session died on the OpenRouter daily quota; the operator reset it and dispatch resumed). Pre-reset
and post-reset calls are pooled in every statistic below: identical pinned model
`z-ai/glm-5.2:free` (Amendment-1 selection applied once; no re-selection), identical seeds
(banks seed 20260824; H2 module seeds {101,…,105}; stochastic-replication seeds {201,202,203}),
identical decoding (primary T=0; registered T=0.7 modules only), identical harness asset hashes
across the boundary. The reset is transport-class only (§8.1 external-abort class); no protocol
parameter changed across the batch seam. See also DEVIATIONS DEV-7/DEV-8 and INTERRUPTION_LOG #3.

## (ii) H3 reuse-gating verdict block — append to §8

### H3 — reuse-gating (primary efficiency axis; falsification conditions verbatim from pre-reg §6.2)

- Observed Δ(N) = $(N)_baseline − Total_SIR(N, N_conv=1) ≡ **$0.000000 at every declared N ∈ {1,
  10, 25, 100}** (zero price vector, Amendment-1 condition #5; §1.4 formulas unchanged).
- Condition (a) "Δ(N) ≤ 0 at every declared N": arithmetically **SATISFIED** (0 ≤ 0 everywhere).
- Condition (b) "Δ(1) > 0": **NOT observed** ($0).
- Condition (c) "no significant N×arm interaction": **not testable** on an all-zero instrument.
- Verdict: **FALSIFIED AS REGISTERED on the $ endpoint** — falsification condition (a) holds as
  stated. Scope caveat: this is falsification-by-instrument under a degenerate $ axis ("no
  detectable gain"), NOT affirmative evidence that reuse gains are absent (plan §4.5 ceiling).
  Token-amortization diagnostics A(N) = V_in + V_out + E[R] + F/N per arm×family are reported in
  §2 alongside (symmetry rule respected); the H3 object survives in token terms for E1b.

## (iii) H5 paraphrase note — append to §8

### H5 — paraphrase robustness: **N/A IN E1 BY DESIGN**

- D-3 (registered pre-run, Appendix A / DEVIATIONS DEV-8 context): paraphrase arm DEFERRED TO E2
  before any scored call. No paraphrase data exist in E1; the H5 discriminator is therefore
  **not evaluable in this experiment**. No verdict is issued and none is invented; E2 inherits
  the prediction unchanged.

_Footnote to add with (ii)/(iii): verdicts above evaluate falsification conditions EXACTLY as
stated in pre-reg §6.2; where an endpoint is degenerate ($≡0) or absent (paraphrase), that fact
is reported as the outcome rather than re-wording the prediction._
