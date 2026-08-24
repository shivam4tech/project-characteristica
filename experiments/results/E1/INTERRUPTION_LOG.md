# E1 INTERRUPTION LOG + ESCALATION (written at stop)

**Time:** 2026-08-24 ~17:35 IST · **Status:** SCORED RUNS NOT STARTED — external abort, §8.1 class.

## What happened (timeline)
1. W0a/W0d assets committed+hashed (`experiments/e1_assets/`, `results/E1/manifest.json`);
   F-block caps verified within §3.1 budgets (85/120, 449/450, 389/700, 1368/1400, 295/350).
2. Banks rebuilt seed 20260824 after generator repairs (DEVIATIONS DEV-2/5); self-test
   checker(gold)=1.0 on ALL 150 items → W0c GREEN. W0b traceability 620 rows.
3. UNSCORED smoke executed ×4 (2 calls/arm each, excluded from statistics by pre-declaration):
   - RUN 1: exposed missing TU registry → DEV-5 repair.
   - RUN 2: registry fix verified (JSON arm gate-pass on TU); exposed NL-parser gap → DEV-6 repair;
     first transient HTTP 402 observed.
   - RUN 3: JSON/TU cell returned empty content ×3 attempts → diagnosed HTTP 402 Payment Required.
     All other cells parsed/scored normally → harness structurally sound (SIR conv→validate→exec→
     parse→score chain exercised end-to-end with real docs).
   - RUN 4: launched with transport-retry policy (DEV-7); aborted mid-flight when 402 persisted.
4. Account diagnosis via `GET /auth/key` (operator's own pooled credential, label sk-or-v1-5c9…):
   `usage: $0.161`, `limit: None`, **`is_free_tier: True`** → the Hermes-managed OpenRouter key has
   NO credit line; paid-model calls 402 once the small initial balance (~$0.16) was consumed.

## Classification
External abort (billing), pre-reg §8.1 — NOT a structural failure of the harness. Smoke evidence:
pipeline executes, parses, meters tokens/$, scores, writes incrementally. Zero scored calls were
made, therefore no data exist, therefore NO prediction verdicts are reported (pre-reg forbids
verdicts without the fixed-n data; none will be invented).

## Escalation (decision-record condition #2 — written)
**Needed from Director/operator (any ONE):**
(a) Add credit to the existing OpenRouter key (recommended: ~$10–15 covers the full ≤1,475-call
    plan at the pinned vector p_in=$0.75/M, p_out=$4.50/M ≈ $2–4 typical spend), OR
(b) supply another credited key for the SAME pinned model id `openai/gpt-5.4-mini` (D-2/§8.2:
    single family, version-dated; switching model or aggregator is a protocol change requiring a
    countersigned amendment), OR
(c) rule on an amendment changing the D-2 pin (would restart all cells from zero per §8.2).
Not viable without ruling: opencode-zen upstream (403), nous/xai proxy upstreams (not logged in),
stale INFERX/TOKENROUTER/ZENMUX keys (domains do not resolve).

## Resume procedure (one command once credits exist)
```
cd experiments && PYTHONDONTWRITEBYTECODE=1 ../.venv-e1/bin/python harness/runner.py primary   # 600 calls
# then: h2 → repl (--comparator per analysis rule) → f3 → harness/analysis.py (+analysis2 verdicts)
```
No re-smoke needed (W0e satisfied, runs 1–4 logged). Manifest/banks/hashes are final; runner,
checkers, F-blocks frozen — NO further edits permitted after the first scored call lands.

## State at stop
- Scored rows in outcomes.csv: **0** (file absent). H2/repl/f3: not run.
- Files ready: runner.py (all modes), analysis.py part 1, DEVIATIONS.md DEV-1..DEV-7,
  manifest.json, e1_assets/*, banks/*.json, raw_outputs/ (smoke only, verbatim).

---

# INTERRUPTION #2 — 2026-08-24 ~18:00–18:45 IST · upstream `:free` pool outage

## What happened (post-Amendment-1)
1. Amendment-1 applied pre-first-scored-call (DEV-8): pin re-selected ONCE → `z-ai/glm-5.2:free`
   (verified serving by probe at selection time, 17:5x IST). Config/manifest updated, pacing +
   checkpoint-resume added, all BEFORE the first scored dispatch.
2. `runner.py primary` dispatched 17:47–18:00 IST against the amended pin. During this window the
   slug's ONLY free upstream (`Decart`, per GET /models/…​/endpoints) returned sustained
   `upstream_429` / "temporarily rate-limited upstream" (`limit_source=upstream_provider_shared_pool`).
   Zero outcomes completed (outcomes.csv absent, no new raw_outputs). No daily-quota block was
   observed — error metadata attributes everything to the shared free provider pool.
3. Runner stopped cleanly at ~18:00 (§8.1 external-abort class: API outage). A probe watcher
   (90 s cadence) observed continuous HTTP 429 from 18:03 through 18:42+ IST.
4. **Checkpoint state:** zero completed (arm,item,rep) cells ⇒ resume re-runs all 600 primary
   jobs; nothing partial to discard. Auto-chain watcher armed: on first serving probe it spawns
   `chain_e1.py` = primary → repl(EX,TU vs §7 comparators) → h2 → f3 → make_results
   (analysis.py + analysis2.py), each stage appending incrementally with BATCH_FLUSH=10.

## Classification & escalation status
External abort (provider outage), pre-reg §8.1 — not a structural failure; NOT a protocol
deviation (no harness/prompt/threshold/item changes post-dispatch; DEV-8 items were all
pre-first-scored-call). No model switch: Amendment-1 condition 1 forbids re-selection after the
rule was applied once; transient congestion does not unselect the pinned slug.

## Resume procedure (unchanged, one command)
```
cd experiments && PYTHONDONTWRITEBYTECODE=1 ../.venv-e1/bin/python harness/chain_e1.py
```
(or `harness/runner.py primary` alone; resume logic skips completed cells.)

---

# INTERRUPTION #3 — 2026-08-24 22:28 → 08-25 01:30 IST · WS-E1EXEC wait/analysis pass

## What happened
1. Watchdog respawned `chain_e1.py` 22:28 IST after a serving probe passed; second respawn at
   00:44 IST. Between 22:28–01:14, workers completed 72 primary outcomes (raw_outputs verbatim),
   pace 0–19 items/hour (z-ai/glm-5.2:free shared-pool congestion bursts).
2. **FATAL OPERATIONAL DEFECT IDENTIFIED (evidence-based, root-caused):** `outcomes.csv` does not
   exist despite >10 completed outcomes in EVERY pass tonight (87-item pass 1, 72-item pass 2).
   Cause: `runner.py` `emit()` (L347-348) acquires the non-reentrant `threading.Lock` and then
   calls `_flush()` (L352-356) which re-acquires the SAME lock ⇒ permanent deadlock the moment
   the batch buffer reaches `BATCH_FLUSH=10`. Verified live via /proc: main thread futex-blocked,
   both worker threads in socket poll. Consequences: CSV never flushed (final force-flush is
   unreachable past the wedge); primary stage never exits; repl/h2/f3/make_results never launch;
   every watchdog respawn re-runs all 600 jobs from scratch (resume reads ONLY the CSV that can
   never be written). The chain as currently frozen can NEVER complete.
3. Scored-data impact: NONE lost irrecoverably — every attempt is retained verbatim under
   raw_outputs/<arm>/<family>/<item>.json including the full outcome dict; the CSV is a derived
   index. No scoring/verdict was possible tonight (no analyzable outcomes.csv), so NO prediction
   verdicts are issued here (pre-reg forbids verdicts without fixed-n data; none invented).

## Classification
Operational defect in transport/buffering infrastructure (DEV-8 pacing/checkpoint code path),
external-abort class §8.1; NOT an arm-treatment, prompt, threshold, item, or scoring change.
Written escalation per decision-record condition #2.

## Required before any further scored dispatch (Director/operator ruling)
(a) **One-line mechanical fix** (recommended): `lock = threading.Lock()` → `threading.RLock()`
    in `run_batch` (equivalently: move the `_flush()` call outside the `with lock:` block).
    Measurement-neutral; log as DEVIATIONS DEV-9 with hash refresh of runner.py only.
(b) OPTIONAL salvage (avoids ~27 h re-run at observed 20–25 items/h): audited one-shot script to
    rebuild `outcomes.csv` from raw_outputs JSONs (`outcome` field carries every OUT_FIELDS value;
    `ts` from file mtime; `rerun` inferable from duplicate (arm,item,rep) presence + mtime order;
    latest-mtime non-transport-fail reading wins per DEV-7). Rebuilt rows must be marked as
    reconstructed in a ledger note. Otherwise accept full re-run.
(c) After fix (+ optional rebuild): single restart of `chain_e1.py`; verify `[primary] …/600
    flushed` lines appear within ~10 outcomes; stages then auto-chain through `make_results`.

## State at 01:30 IST handoff
- Processes ALIVE: chain gen-3 (bash 137322 / python 137651 / runner primary 137652, started
  00:44) — wedged at buffer=10 since ~00:50; workers may keep rewriting raw_outputs until their
  600-job queue drains, then hang harmlessly. Safe to kill before applying fix (a).
- Primary progress on disk: 87 raw JSONs (pass 1) with 72 rewritten (pass 2); 0 CSV rows.
- Watch cadence used: 16 × sleep-540 polls (protocol cap 18) 22:47–01:14 IST.

## Prepared next-step artifacts (for the completing session)
`E1_RESULTS_verdict_drafts.md` (this directory) holds: (i) mixed-batch header note text
(pre/post key-reset calls pooled; same pin/seeds/temp-0), (ii) H3 reuse-gating verdict block,
(iii) H5 paraphrase N/A note — the three additions `make_results.py` does not emit itself.
After a clean make_results run: insert (i) after the P8 flag line, append (ii)+(iii) to §8.
