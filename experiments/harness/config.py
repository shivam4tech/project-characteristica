"""E1 harness configuration — pins, seeds, paths, price vector.

Frozen per experiments/E1_PRE_REGISTRATION.md (W0f-countersigned) and
experiments/E1_DECISION_RECORD.md, AS AMENDED by experiments/E1_AMENDMENT_1.md
(D-2 revised, countersigned W0f' 2026-08-24). No value here may change after the first
scored call (pre-reg §8.5).
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]          # project-characteristica/
HARNESS = Path(__file__).resolve().parent
ASSETS = REPO / "experiments" / "e1_assets"
RESULTS = REPO / "experiments" / "results" / "E1"

# ---------------- D-2 model pin (single family, version-dated, stable API) ---
# AMENDMENT-1 (W0f', 2026-08-24): pin = highest-capability OpenRouter :free-tier
# model verifiably serving at run time, selected ONCE, used for ALL arms
# identically (converter = executor, D-4 preserved). Selection record: of the 18
# :free ids listed by GET /api/v1/models at 2026-08-24 ~18:0x IST, ranked by
# independent benchmark standing (Artificial Analysis Intelligence Index):
# glm-5.2 (53) > thinkingmachines/inkling (41; also harness-gated HTTP 403 via
# plain-API transport -> not verifiably serving) > nemotron-3-ultra-550b (38);
# remaining ids have no documented capability evidence or are small/specialist.
# z-ai/glm-5.2:free verified serving via live probe (transient upstream 429s,
# success on retry; logged as plumbing, excluded from statistics).
MODEL_ID = "stealth/ox-alpha"  # Amendment-2 (2026-08-25): uniform re-pin after operator key reset restored ox-alpha quota
TOKENIZER_ID = "o200k_base (tiktoken; glm-5.2 server tokenizer approximated for F/V split only; authoritative counts are provider usage fields)"
PRICE_VECTOR = {"p_in_usd_per_token": 0.0,          # :free tier — published $0/$0
                "p_out_usd_per_token": 0.0}         # => §1.4 $ endpoints degenerate (reported as such)
PRICE_SOURCE_URL = "https://openrouter.ai/api/v1/models"
PRICE_RETRIEVAL_DATE = "2026-08-24"
API_BASE = "https://openrouter.ai/api/v1"
AMENDMENT_REF = "experiments/E1_AMENDMENT_1.md (W0f' 2026-08-24): D-2 revised to OpenRouter :free tier"

# ---------------- decoding params (identical all arms) -----------------------
TEMPERATURE = 0.0
MAX_TOKENS = 2048
SEED_PRIMARY = None          # provider seed param; set post-smoke if accepted
GEN_SEED = 20260824          # item bank generator (pre-reg §2)
BOOTSTRAP_SEED = 20260824    # §7 paired bootstrap
H2_SEEDS = [101, 102, 103, 104, 105]     # variance module, T=0.7
REPL_SEEDS = [201, 202, 203]             # stochastic replication, T=0.7

N_VALUES = [1, 10, 25, 100]
N_CONV_VALUES = [1, 10]      # N_conv=10 curves labeled PROJECTED (§3.2)
PRIMARY_N = [1, 25]

DELTA_F1 = {"EX": 3.0, "CP": 4.0, "TU": 3.0}   # percentage points (§5)
DELTA_F3 = 0.90                                 # round-trip stability (§5)

FAMILIES = ["EX", "CP", "TU"]
ARMS = ["NL-plain", "NL-opt", "JSON", "CSIR-SIR"]
N_ITEMS_PER_TEMPLATE = 10   # 5 templates x 10 = 50 items/family

REPAIR_LIMIT = 2            # <=2 repair re-prompts, metered as R / R_conv
MAX_WORKERS = 2             # paced for :free tier (DEV-8, pre-first-scored-call)
BATCH_FLUSH = 10            # incremental write granularity (decision record #1)
RATE_MIN_INTERVAL_S = 3.05  # client-side throttle: <=~19.7 requests/min (DEV-8)
RETRY_429_MAX = 8           # transport-class retries for HTTP 429 w/ 20 s backoff (DEV-8)

def ensure_dirs():
    for d in (ASSETS, RESULTS, HARNESS):
        d.mkdir(parents=True, exist_ok=True)
