# glm_pilot_appendix/index.md — Quarantined `z-ai/glm-5.2:free` pilot set (Amendment-2)

**Quarantine rule:** every raw_outputs cell whose file mtime < 2026-08-25 00:35 IST belongs to the
glm-5.2 pilot population and is EXCLUDED from all primary statistics in `../E1_RESULTS.md`.
Attribution method: mtime rule (operator-directed); the frozen outcome schema carries no
`"model"` field, so record-level marking per Amendment-2 condition 1 is unavailable.

## Preserved files (`raw/`, verbatim copies taken 01:24 IST 2026-08-25)

| source path (raw_outputs/…) | mtime | arm | family | item | transport_fail | gate | score |
|---|---|---|---|---|---|---|---|
| CSIR-SIR/EX/EX-01-00.json | 08-24 17:22 | CSIR-SIR | EX | EX-01-00 | False | False | 0.3571 |
| NL-plain/TU/TU-01-00.json | 08-24 17:22 | NL-plain | TU | TU-01-00 | True | False | 0.0 |
| NL-opt/TU/TU-01-00.json | 08-24 17:22 | NL-opt | TU | TU-01-00 | True | False | 0.0 |
| JSON/TU/TU-01-00.json | 08-24 17:22 | JSON | TU | TU-01-00 | True | False | 0.0 |

All four derive from the UNSCORED smoke era (pre-declaration §8.5; DEV-5/DEV-6/DEV-7 context) —
they are provenance specimens, not statistics.

## Destroyed-by-overwrite disclosure

The frozen runner persists each item to a deterministic path (`raw_outputs/<arm>/<family>/<item>.json`)
and rewrites it in place on every pass; no versioning exists. Consequence for this appendix:

- Pass 1 (glm, scored dispatches 17:47–18:00 + smoke-era stragglers): **87 files on disk at 22:33 IST**
  (NL-plain 51 · NL-opt 33 · JSON 2 · CSIR-SIR 1).
- Pass 2 (glm, 22:28–~00:44): 72 outcomes completed; same paths rewritten.
- Pass 3 (ox-alpha, from 00:44): progressively overwrote the same paths again (~150 items/h — much
  faster than the congested glm pool).

Net effect: **the glm-5.2 SCORED pilot payloads no longer exist on disk.** The quarantine set is
therefore metadata-only: the counts above plus pace records in `../INTERRUPTION_LOG.md` #3.
The Amendment-2 condition-2 robustness check (glm-vs-ox-alpha agreement on re-run overlapping
cells) is impossible unless cells are deliberately re-run under a restored glm pin.

## Per-arm×family glm pilot counts at last observation (metadata only)

| arm.family | files seen (passes 1–2) | status at 01:26 IST |
|---|---|---|
| NL-plain.EX | ~50 | overwritten by ox-alpha (n=50 primary) |
| NL-opt.EX | ~33→49 | overwritten by ox-alpha (n=50 primary) |
| NL-plain.{CP,TU}, others | sparse | not reached / overwritten |
| JSON.EX, CSIR-SIR.* | ≤2 each | smoke-era only |

No glm-vs-ox-alpha numeric comparison is reported anywhere in E1_RESULTS.md.
