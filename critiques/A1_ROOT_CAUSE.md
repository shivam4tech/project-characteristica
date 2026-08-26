# A1 Root Cause — CSIR-SIR arm: repair-limit hits everywhere, yet clean flags & ~0 scores

**Status:** COMPLETE (2026-08-25, raw-transcript audit per E1_RESULTS_INTERIM.md §6 item 2)
**Scope:** 150 admitted CSIR-SIR primary cells (interim snapshot counted 143: EX 50 + CP 43 + TU 50), plus h2/repl spot-checks. All findings reproduce population-wide, not by sampling.

## VERDICT

**BOTH — two independent defects, cleanly separable:**

1. **A1-as-stated (telemetry contradiction) is an INSTRUMENTATION BUG**, and it is the *analysis surface*, not the pipeline, that lied. The CSV telemetry was correct and self-consistent all along (`conv_errors='json:no JSON object found'`, `kerr_flag=True`, `doc_valid=False` on 149/149 failing cells). The raw-transcript outcome blocks say the opposite (`conv_errors=""`, `kerr_flag=False`, `doc_valid=True`) **by construction**: `sir_finish()` persists the raw file inside `finish()` *before* overwriting the three converter-health fields on the returned dict. Divergence measured: **150/150** primary raw blocks carry stale defaults while their CSV rows carry real values; tonight's repl raw files show the same staleness (bug is live, present since commit 52f7549, i.e., before the first scored call — not a mid-run change).
2. **Beneath it sits a GENUINE total conversion failure — but NOT "valid-but-semantically-wrong" documents.** In 149/150 cells the converter produced **no parseable document at all**: 445/448 convert calls returned `p_out≈2048` (= `MAX_TOKENS`) with **empty `content`** — the output budget is exhausted before any visible text is emitted. `extract_json` fails ("no JSON object found") on every attempt; at T=0 all three attempts are identical, so the repair loop can never help. The executor then received literally `CSIR/0 DOCUMENT:\n{}` and answered UNKNOWN-flooded artifacts → scores ≈ 0. The anomaly's second hypothesis ("docs schema-valid but semantically wrong") is **refuted**: the single schema-valid document ever produced (EX-04-05) scored **0.8125** with most gold fields correct — when a doc exists, the pipeline works.

The interim dichotomy ("either attempts are mis-instrumented or failures were absorbed silently") resolves as: attempt counting was correct, failures were *loudly* recorded in outcomes.csv, and only the raw-block flag copies were silently stale.

## Code-path trace (experiments/harness/)

### runner.py — `run_arm` CSIR-SIR branch (L191–216)
- Converter loop (L195–214): `cidx` 1→3 (`REPAIR_LIMIT=2` ⇒ ≤3 calls). Payload = `F_CONV + SOURCE INTENT + REQUIRED OUTPUT ARTIFACT`; repairs append `"Your previous document FAILED VALIDATION:\n- <derrs>"`.
- Per attempt: `call("CSIR-SIR::conv", …)` (L204) → `rec(...)` logs attempt with `note=` carrying the **pre-call** error list (L205, so att2/att3 notes prove att1/att2 had already failed) → `extract_json` (L209, regex `\{.*\}` needs a closing brace) → `validate_csir` (L210) → break if clean **or** limit hit (L213 `if not derrs or cidx > CFG.REPAIR_LIMIT`).
- Then `return sir_finish(..., cand, derrs or [], q)` (L216). Transport-fail on a convert call breaks early with `cand=None`, `derrs=None` → recorded as empty errors (h2's `n_conv=1, kerr=False, doc_valid=False` rows are exactly this path).

### runner.py — `sir_finish` (L218–242): where A1 was born
```python
out = finish(arm, item, rep, temperature, attempts, art, perr)   # L238: raw JSON WRITTEN HERE
out["conv_errors"] = ";".join(cerrs)[:400]                       # L239: correction applied…
out["kerr_flag"]   = bool(cerrs)                                 # L240: …only to the RETURNED dict
out["doc_valid"]   = bool(cand_doc) and not cerrs                # L241
```
But `finish()` (L244–293) sets defaults at **L279–281** (`conv_errors=""`, `kerr_flag=False`, `doc_valid=True`) and **persists the transcript at L286–288** with those defaults still in place. The corrected values land in `outcomes.csv` (via `run_batch.emit`) but **never** in `raw_outputs/**.json`. Consequences:
- Any consumer of raw outcome blocks sees the clean-flag signature regardless of what actually happened → the interim analysis (footer: "Sources: raw_outputs/*/*/*.json") saw exactly that and raised A1.
- `n_conv_attempts` (L276) is computed inside `finish()` and is therefore **trustworthy** — which is why the contradiction looked impossible.
- Dead code L290–292 (`if arm=="CSIR-SIR" ... pass`): no CSIR doc path is persisted either way.
- Latent secondary gap (did not fire in E1): `validate_csir` (L106–151) checks version/speech_act shape/kind whitelist/spans well-formedness/ref integrity/acyclicity/depth, but a document with **empty `nodes`/`edges` passes with zero errors** — no minimum-content or intent-coverage gate, despite the docstring promising "span coverage". Also irrelevant here (nothing ever reached it), but should be fixed before any re-run.

### fblocks.py — converter/executor prompt contract ("F_SIR" = F_CONV + F_EXEC pair)
- **F_CONV (L55–103)**: full CSIR/0 v0.1.0 serializer spec — closed 12-kind Tier-A vocabulary, Tier-B lexicon entries, THE SEVEN RELATION LABELS with one reading each (L59–66), exact JSON shape (L68–73), kind fields (L75), mandatory policies: per-node span citation (1), branch-or-unknown ambiguity policy (2), exclusions/negation/modality/preference as own nodes (3), referential integrity/depth≤3/acyclic (4), **"Represent ALL task-relevant content … recoverable from the document alone"** (5), plus one worked example. This is a large, demanding contract; faithful documents for these items plausibly exceed a 2048-token output budget (the worked example alone is ~700 tokens), which is what makes the cap binding.
- **F_EXEC (L106–117)**: "Treat the document as the SOLE source of truth — the original source text is unavailable"; values must trace to nodes; unknown:true stays UNKNOWN; rule 5: work with what validated, never fabricate. With `cand=None` the executor input is `"CSIR/0 DOCUMENT:\n{}"` + validator report `- json:no JSON object found` (L219–223) — so ≈0 scores are the executor *correctly* reporting an information-free input (TU-03-04 says so verbatim: *"The CSIR/0 document is empty and validation reported 'no JSON object found'"*).

### config.py — repair settings
- `REPAIR_LIMIT = 2` (L55) ⇒ ≤3 converter calls/cell ⇒ `n_conv_attempts=3` ⇔ attempts 1–2 both failed extraction/validation. All 149 failing cells sit at exactly 3.
- `MAX_TOKENS = 2048` (L37), uniform across arms and stages (frozen parity); `TEMPERATURE = 0.0` (L36) ⇒ repairs are deterministic re-runs, structurally unable to escape a truncation/budget failure.
- Result: each cell burned K ≈ 3×(p_in≈1,649 + 2,048) ≈ **11.1k tok/item** of real, metered spend producing zero documents (matches interim K≈11,110).

## Population forensics (all 150 primary cells)

| Measurement | Value |
|---|---|
| Raw-block `(doc_valid,kerr,err)` vs CSV row | diverge on **149/149** failing cells (raw always "clean", CSV always `False/True/json:no JSON object found`) |
| Convert attempts | 448 total; **445 with empty `content`**, 446 at `p_out=2048` |
| Last-attempt replay through `extract_json`+`validate_csir` | 149× ValueError("no JSON object found"), 1× parses **clean** |
| Non-empty convert contents anywhere | 3/448: EX-04-05 att1 (4,992 chars → valid doc); EX-05-04 att2 (5,637 chars, truncated mid-string → JSON syntax error); TU-04-06 att2 (1,097 chars, parsed but node `kind:"orderedBefore"` — an §4 *edge label* used as node kind → correctly rejected) |
| Schema-validation events ever | 2 (one pass, one kind-error). The §4 relation-label gate was effectively never exercised. |

## Cell evidence (6 raw JSONs across families)

| cell | family/template | conv attempts | what actually happened | exec artifact | score | CSV flags (true state) |
|---|---|---|---|---|---|---|
| CP-01-01 | CP/CP-01 | 3×2048 tok, all empty | no doc; exec guessed schedule strings | `{"schedule":[…4×UNKNOWN lines]}` (strings, not dicts) | 0.0 (checker_exception, anomaly A2) | kerr=T, dv=F |
| CP-03-00 | CP/CP-03 | 3×2048, empty | no doc | `{"steps":["UNKNOWN"]}` | 0.43 (partial credit for shape; 4 hard violations) | kerr=T, dv=F |
| EX-02-01 | EX/EX-02 | 3×2048, empty | no doc; 3 identical exec repairs | 14 fields, all UNKNOWN | 0.0 | kerr=T, dv=F |
| **EX-04-05** | EX/EX-04 | **1 shot, 4,992 chars** | **only real doc of the run**: 30 nodes/15 edges, `validate_csir=[]`, labels {hasArg6, modifies4, constrains1, orderedBefore1, quantifiesOver1, requestsOutput1, excludes1} — §4-conformant | fields mostly correct (ship_date ✓, cargo ✓✓; pickup times ✗) | **0.8125** | kerr=F, dv=T |
| TU-01-00 | TU/TU-01 | 3×2048, empty | no doc | `{"calls":[]}` | 0.0 | kerr=T, dv=F |
| TU-03-04 | TU/TU-03 | 3×2048, empty | no doc; executor states "document is empty…" | `{"clarify":{"missing":[…],"question":"The CSIR/0 document is empty…"}}` | 0.0 | kerr=T, dv=F |

Raw-file spot-check: all six raw blocks record `doc_valid=True/kerr=False/conv_errors=""` — including for the five cells whose CSV rows say the opposite; repl files `CP-01-00_r0/r1.json` show the same staleness tonight.

## Pre-reg §4 relation-label contract check
E1_PRE_REGISTRATION.md §4 (L117–131) freezes the seven-label closed vocabulary with single readings; `validate_csir._RELS` implements exactly that whitelist, and F_CONV teaches the same seven. The one complete document (EX-04-05) uses only whitelisted labels with plausible readings; the single near-miss (TU-04-06) used `orderedBefore` as a node *kind* and was rejected. **No evidence of systematic relation-label misuse — the contract was simply never reached.** §3.1's "never silently repaired" was honored in the CSV (failures propagated into the executor prompt); the silence lived only in the raw-block flag copies.

## Impact

**Survives as-is:**
- Effectiveness ordering on this pipeline configuration: SIR 0.08/0.07/0.00 vs JSON 0.83/0.81/0.94 — H1 condition-(2) non-inferiority fails in all families; H0 favored. TU adversarial loss (P6) confirmed (0/50 >0).
- Cost arithmetic: K ≈ 11.1k tok/item is real metered spend (provider usage fields), Δ(N)<0 at every N; no break-even on the registered grid; H3 falsifier shape matched. CET negative result stands *for a converter that cannot emit documents under the pinned output cap*.
- Baseline arms (NL-plain/NL-opt/JSON) untouched by A1; latency rows; anomalies A2/A4/A5 as recorded.

**Must be re-scoped / corrected:**
- Paper §4.1/§6.2 claim "formally valid documents at near-zero gold-field scores" (FT3 silent-error framing) — **false premise**: 149/150 cells contain no document. Retract/reword to "conversion-stage non-production".
- Interim H4 read ("docs validate 100% → silent-error rate near-maximal") — invalid; derived from stale raw flags. H4 unevaluable in this run (no docs to be silent errors about).
- `doc_valid`/`kerr_flag`/`conv_errors` semantics: CSV `kerr_flag=True` means "extraction failed", never "schema repair failed" (zero schema-repair events occurred).
- F2/F3 remain uncomputable (no documents) — not an instrument gap anymore but a pipeline outcome.
- A1 itself: close as resolved-instrumentation + genuine-upstream-failure; log in DEVIATIONS.md.

## Recommended fix
1. **Code (one-line-class fix):** in `sir_finish`, apply the three field-overwrites *before* persistence — e.g. pass `cerrs`/`cand_doc` into `finish()` and set them at L279–281, or move the raw write after the overrides. Add an invariant assertion (`kerr_flag == bool(conv_errors)` and `doc_valid == (cand is not None and not cerrs)`) plus a regression test feeding synthetic cerrs.
2. **Backfill (no API needed):** replay `extract_json`+`validate_csir` over every existing `attempts[stage=='convert']` to regenerate truthful flags in all raw files; deterministic, already validated on the 150-cell census above.
3. **Converter capacity (requires amendment, else SIR re-run is meaningless):** the failure is `MAX_TOKENS=2048` exhausted before visible output (mechanism consistent with hidden reasoning-token burn; `finish_reason`/`usage.reasoning_tokens` were not logged — log them to confirm). Raise the convert-stage cap (e.g. ≥8k; prefer a global amendment to preserve arm parity) and/or add compact-serialization guidance; keep T=0.
4. **Analysis hygiene:** compute all health metrics from `outcomes.csv` (single source of truth) or from backfilled raws; fix `validate_csir`'s vacuous-pass on empty graphs before any re-run.

**Re-run needed: YES — SIR arm only** (all four arms × 3 families, or at minimum the registered primary matrix for CSIR-SIR), after fix 3, if any claim about the CSIR/0 representation itself is to stand. Current SIR data measures only "ox-alpha cannot emit a compliant CSIR/0 doc under a 2,048-token cap," which the baselines never tested.
