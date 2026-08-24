"""E1 harness configuration — pins, seeds, paths, price vector.

Frozen per experiments/E1_PRE_REGISTRATION.md (W0f-countersigned) and
experiments/E1_DECISION_RECORD.md. No value here may change after the first
scored call (pre-reg §8.5).
"""
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]          # project-characteristica/
HARNESS = Path(__file__).resolve().parent
ASSETS = REPO / "experiments" / "e1_assets"
RESULTS = REPO / "experiments" / "results" / "E1"

# ---------------- D-2 model pin (single family, version-dated, stable API) ---
# Rationale recorded in manifest: cheapest stable frontier-tier API accessible
# to the lab with PUBLISHED per-token pricing (required for $ endpoints;
# stealth/ox-alpha publishes no pricing -> $ endpoints would be degenerate).
MODEL_ID = "openai/gpt-5.4-mini"
TOKENIZER_ID = "o200k_base (tiktoken; gpt-5.4-mini server tokenizer approximated for F/V split only; authoritative counts are provider usage fields)"
PRICE_VECTOR = {"p_in_usd_per_token": 0.00000075,   # $0.75 / 1M input
                "p_out_usd_per_token": 0.0000045}   # $4.50 / 1M output
PRICE_SOURCE_URL = "https://openrouter.ai/api/v1/models"
PRICE_RETRIEVAL_DATE = "2026-08-24"
API_BASE = "https://openrouter.ai/api/v1"

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
MAX_WORKERS = 6             # transport concurrency (same window/endpoint all arms)
BATCH_FLUSH = 10            # incremental write granularity (decision record #1)

def ensure_dirs():
    for d in (ASSETS, RESULTS, HARNESS):
        d.mkdir(parents=True, exist_ok=True)
