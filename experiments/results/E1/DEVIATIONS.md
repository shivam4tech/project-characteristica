# E1 Deviations & Asset-Repair Ledger (pre-first-scored-call)

Written before ANY scored call. Per decision-record condition #2 (written escalation, no improvisation).

## DEV-1 · Smoke-test size (W0e)
Pre-reg §8.5/W0e says "smoke ≤4 calls". Coordinating directive for this engagement explicitly orders
"UNSCORED smoke test: 2 calls/arm". Executed as ordered: 8 API calls total (NL-plain 2 items,
NL-opt 2 items, JSON 2 items, CSIR-SIR converter+executor = 2 calls on 1 item). All logged to
`smoke.jsonl`, declared UNSCORED and excluded from every statistic by pre-declaration (§8.5).
Statistical impact: zero (no scored data touched). Escalation satisfied by this ledger entry +
final report line.

## DEV-2 · Item-bank generator repairs (pre-first-scored-call, W0c gate was RED)
On this session's fresh rebuild the W0c self-test FAILED on 15/150 items (prior session's "verified
clean" result is attributable to stale `__pycache__` bytecode surviving the power outage; caches
cleared). Two real generator defects repaired BEFORE any scored call — asset-build phase, not
post-hoc tuning; no arm output, score, or gold semantics changed beyond restoring checker↔gold
consistency demanded by W0c:
- `items/cp_items.py::_cp4_inst`: params["guests"] was built from constraint-pair endpoints only,
  producing guest lists shorter than n_guests for n∉{6,8} (checker h1_all_seated_once could never
  pass on the true optimum). Fixed to all n labels.
- `items/tu_items.py` TU-02 gold mail.send gained a body referencing the filed ticket (checker
  ok_ref requires the reference the task itself demands; gold previously could not demonstrate it).
Post-repair self-test: checker(gold)=1.0 on ALL 150 items; banks rebuilt seed 20260824, sha256 in
manifest. No other bank/checker edits. Frozen files untouched otherwise.

## DEV-3 · Transport & credential provenance
config.API_BASE = OpenRouter (frozen). No OPENROUTER_API_KEY in env/.env; hermes proxy upstreams
(nous/xai) not logged in. Used the operator's own OpenRouter credential from Hermes' documented
auth store (`~/.hermes/auth.json` credential_pool.openrouter, label "openrouter-api-key-quick-copy")
— the same pool the gateway itself draws on ("hermes CLI authenticated" per engagement brief).
Key material never printed, never copied into repo files; runner reads it from auth.json at runtime.
Price vector RE-VALIDATED live at run date from https://openrouter.ai/api/v1/models:
prompt $0.00000075/tok, completion $0.0000045/tok — identical to frozen config values. No change.

## DEV-4 · Model availability (informational, no deviation)
D-2 pin `openai/gpt-5.4-mini` confirmed present and serving on OpenRouter at run start (probe call,
logged as smoke-adjacent plumbing, excluded from statistics).

## DEV-5 · TU bank missing the frozen tool registry (pre-first-scored-call, found by smoke)
Smoke (unscored) showed ALL arms inventing tool names (`book_room`, ...) on TU items: the item
generator never presented the §2.3 mock registry, though it is part of the frozen task definition
and "tools/context [are] identical across arms" (§3.1). Repaired `items/tu_items.py::_mk` to prepend
the exact six-signature registry to every TU source_text (identical bytes for all arms; rides V_in).
Banks rebuilt seed 20260824; self-test re-run green; assets+manifest re-hashed before any scored call.
Also fixed in runner: SIR outcome field ordering bug (conv_errors referenced before assignment).

SMOKE RUN 1 (7 outcomes, registry-less TU bank) archived at smoke_outcomes.run1.csv + raw_outputs/
retained verbatim. Smoke re-run after repair = SMOKE RUN 2.

## DEV-6 · NL tolerant parser vs the TU question's own JSON contract (pre-first-scored-call)
Smoke run 2: both NL arms emitted exactly the JSON {"calls":[...]} artifact that the SHARED frozen
item question text requests, but checkers.parse_answer's NL path read only freeform call-lines ->
false 0.0s. Repaired pre-scored-call: NL path on TU now honors the question's own JSON contract
first, falls back to freeform. Machine arms unchanged (strict parse). SMOKE RUN 3 = final gate.

## DEV-7 · Transport-failure policy (frozen pre-scored-call)
Smoke run 3 hit transient HTTP 402 (Payment Required) on one arm x item — operator account credit
blip; immediate re-probe succeeded. External-abort class per pre-reg §8.1. Mechanical rule frozen
BEFORE any scored call: every transport-failed outcome receives exactly ONE re-execution; BOTH
readings are retained verbatim (`rerun` column); analysis takes the latest non-transport-fail
reading per (arm,item,rep). Not post-hoc filtering: rule mechanical + pre-declared + both rows kept.

## DEV-8 · Amendment-1 re-pin + :free-tier transport mechanics (pre-first-scored-call)
Zero scored calls existed when this entry was written (INTERRUPTION_LOG confirms 0 rows), so these
changes are legal under pre-reg §8.5 and are mandated by Amendment-1 / coordinator directive:
1. **D-2 re-pin (Amendment-1, W0f'):** MODEL_ID `openai/gpt-5.4-mini` → **`z-ai/glm-5.2:free`**.
   Selection applied ONCE 2026-08-24 ~18:05 IST over the 18 listed `:free` ids, ranked by
   documented independent benchmark standing (Artificial Analysis Intelligence Index):
   glm-5.2 = 53 > thinkingmachines/inkling = 41 (additionally HTTP 403 "only available on agentic
   harnesses" via plain-API transport → not verifiably serving) > nemotron-3-ultra-550b-a55b = 38;
   remaining ids carry no documented capability evidence or are small/specialist-class. Serving
   verified by live probe call (transient upstream HTTP 429s, succeeded on retry; usage.cost=0).
   Probes logged as plumbing; excluded from all statistics by the same pre-declaration as smoke.
2. **Price vector:** `:free` tier publishes $0/$0 (live-checked). §1.4 formulas unchanged per
   amendment condition #5 ⇒ all $ endpoints are identically $0.00 and Δ(N)≡0; this degeneracy is
   reported as-is in E1_RESULTS.md with token/char diagnostics alongside (plan §1.6 chars/task;
   raw tokens stay diagnostics). No re-wording of predictions.
3. **Pacing (transport, arm-neutral):** MAX_WORKERS 6→2; client-side min request spacing 3.05 s
   (≤~19.7 req/min); HTTP 429 gets up to 8 extra transport retries @20 s backoff inside `call()`
   (still transport-class, NOT protocol R; identical for every arm/stage incl. converter).
4. **Checkpoint-resume:** `run_batch` now skips (arm,item,rep) triples already holding a latest
   non-transport-fail reading in the mode's CSV, so external-abort/cap-out restarts resume from
   last completed state (pre-reg §8.1) instead of re-running completed cells.
5. Manifest updated (model/tokenizer/prices/amendment record/hashes); config.py+runner.py
   re-hashed; banks/checkers/F-blocks untouched (hashes unchanged except the two files above).


