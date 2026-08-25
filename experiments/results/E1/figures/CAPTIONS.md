# E1 publication figures — captions

Generated from `experiments/results/E1/outcomes.csv` (620 rows) by `experiments/results/E1/figures/src/make_figures.py`.
All quantities are computed from the CSV at generation time; no hand-entered numbers.
Telemetry-valid rows: 600; transport failures without telemetry: 20 (CSIR-SIR/EX: 10, NL-plain/TU: 10).
Palette: Okabe-Ito (colorblind-safe). All PNGs rendered at 150 dpi.

## fig_scores_by_arm_family.png

**Figure 1 — Mean task score by arm and family.** Bars show mean score per arm within each family (EX extraction, CP compliance, TU transformation); black dots are the individual cell outcomes (one dot per item x template cell; n = 50 cells per arm x family, except CSIR-SIR/EX and NL-plain/TU where reruns give 60). JSON attains the highest means (EX 0.83, CP 0.81, TU 0.94). The CSIR-SIR pipeline scores near zero everywhere — EX 0.07, CP 0.07 — and is exactly 0.00 on all 50 TU cells (annotated): its convert-then-execute cascade never yields a passing transformation. Scores are continuous rubric scores in [0,1]; no error bars are drawn (distributions are shown as raw points instead).

## fig_cost_amortization.png

**Figure 2 — Cost amortization: net-of-overhead tokens per item vs reuse depth N.** Solid curves plot the amortization model $A(N)=V+F/N$ with per-item variable tokens $V=v_{\mathrm{in}}+v_{\mathrm{out}}$ and framework/format overhead $F=f_{\mathrm{tok}}+f_{\mathrm{conv}}+f_{\mathrm{exec}}$, each an empirical mean over telemetry-valid cells (600 rows; 20 transport failures carry no telemetry and are excluded). Knowledge ($K$) and retrieval ($R$) tokens do not enter the model and are reported as actuals in the inset table. Even under the most charitable reading — the dashed CSIR-SIR curve treats only the one-time knowledge-base build ($K_{build}$ = 3,704 tok/item) as amortizable while its per-item re-injection ($K_{reinj}$ = 7,408) and retrieval ($R$ = 374) recur at every $N$ — CSIR-SIR remains above every baseline curve for all $N \leq 100$: it never breaks even. Under the plain formula (solid orange) it appears cheap only because the dominant $K$ class is omitted. Log-log axes.

## fig_cost_decomposition.png

**Figure 3 — Token-cost decomposition per item (class means over telemetry-valid cells).** Stacks show mean tokens per item in five classes: variable prompt/response ($V$), framework/format/conversion/execution ($F$), knowledge-base build ($K$: $k_{in}+k_{out}$), knowledge re-injection ($K$: $k_{rin}+k_{rout}$), and retrieval ($R$). CSIR-SIR spends 13,943 tokens/item in total — 7.8x NL-plain (1,793) — with 11,112 of it in the $K$ class alone; 53% of its budget is knowledge re-injection that recurs on every item and cannot be amortized. Baseline arms consume no knowledge tokens ($K=0$). Segment labels are means in tokens.

## fig_latency_cdf.png

**Figure 4 — Empirical CDF of end-to-end latency (`lat_total_ms`) per arm.** Telemetry-valid cells only (n = 150 per arm; 20 transport-failed cells lack timing and are excluded). The latency inversion: CSIR-SIR is the *fastest* arm despite being the least accurate — median 17 s vs 40 s (NL-plain), 29 s (JSON) and 59 s (NL-opt) — roughly 1.7x faster than the fastest competent baseline. Its heavy tail still reaches 2 min. Speed is purchased by skipping verification, not by efficiency: nearly all CSIR-SIR outputs fail scoring (Fig. 1). Log-scale abscissa.

## fig_fidelity_rates.png

**Figure 5 — Format-fidelity ($F_0$) pass rate per arm and family.** $F_0$ checks that the produced artifact parses and satisfies the output contract (`f0_ok`), independent of content quality. All baseline arms hold $F_0 = 1.00$ on EX and TU except NL-plain on TU (0.83); CSIR-SIR degrades hardest on EX (0.73), showing its converter frequently violates even the output format before any semantic evaluation. Denominators match Fig. 1 cell counts; transport failures count as $F_0$ failures (they are recorded outcomes).

## fig_h2_variance.png — NOT PRODUCED (data gap)

The H2/P4 test requires repeated outcomes at temperature 0.7 (a populated `rep` field). In the current outcomes file, `rep` is empty in all 620 rows and `temperature` is 0.0 throughout, so there are no repetitions to estimate variance from. Per the analysis plan this figure is skipped gracefully; it should be regenerated from this script once temp-0.7 replication runs land in outcomes.csv.
