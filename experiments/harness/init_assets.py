"""E1 W0a/W0d: commit asset copies + sha256 manifest before first scored call."""
import hashlib, json, shutil, sys, datetime
from pathlib import Path

REPO = Path("/home/shivam/philosophy/project-characteristica")
EXP = REPO / "experiments"
ASSETS = EXP / "e1_assets"
RESULTS = EXP / "results" / "E1"

COPY = {
    "fblocks.py": EXP / "harness" / "fblocks.py",
    "config.py": EXP / "harness" / "config.py",
    "checkers.py": EXP / "harness" / "checkers.py",
    "items_ex_items.py": EXP / "harness" / "items" / "ex_items.py",
    "items_cp_items.py": EXP / "harness" / "items" / "cp_items.py",
    "items_tu_items.py": EXP / "harness" / "items" / "tu_items.py",
    "items_build_banks.py": EXP / "harness" / "items" / "build_banks.py",
    "runner.py": EXP / "harness" / "runner.py",
    "banks_ex_bank.json": EXP / "harness" / "items" / "banks" / "ex_bank.json",
    "banks_cp_bank.json": EXP / "harness" / "items" / "banks" / "cp_bank.json",
    "banks_tu_bank.json": EXP / "harness" / "items" / "banks" / "tu_bank.json",
}

sys.path.insert(0, str(EXP / "harness"))
import fblocks, tiktoken

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    RESULTS.mkdir(parents=True, exist_ok=True)
    hashes = {}
    for name, src in COPY.items():
        dst = ASSETS / name
        shutil.copy2(src, dst)
        hashes[name] = sha(dst)
    # tokenizer counts of F-blocks (binding caps check, o200k_base)
    enc = tiktoken.get_encoding("o200k_base")
    ftok = {k: len(enc.encode(v)) for k, v in
            {"F_NLp": fblocks.F_NLP, "F_NLo": fblocks.F_NLO, "F_js": fblocks.F_JS,
             "F_conv": fblocks.F_CONV, "F_exec": fblocks.F_EXEC}.items()}
    caps = fblocks.CAPS
    cap_check = {k: {"tokens": ftok[m], "cap": c, "within": ftok[m] <= c}
                 for m, (k, c) in zip(["F_NLp", "F_NLo", "F_js", "F_conv", "F_exec"], caps.items())}
    import config as CFG
    manifest = {
        "experiment": "E1 efficiency/fidelity pilot (CE-01/P3)",
        "prereg": "experiments/E1_PRE_REGISTRATION.md (FROZEN)",
        "decision_record": "experiments/E1_DECISION_RECORD.md",
        "decisions": {"D-1": "oracle OMITTED", "D-2": "single family pinned below",
                      "D-3": "paraphrase deferred to E2", "D-4": "converter model == executor model"},
        "model_id": CFG.MODEL_ID, "tokenizer_id": CFG.TOKENIZER_ID,
        "price_vector": CFG.PRICE_VECTOR, "price_source_url": CFG.PRICE_SOURCE_URL,
        "price_retrieval_date": CFG.PRICE_RETRIEVAL_DATE,
        "price_live_check_2026-08-24": {"prompt": 0.00000075, "completion": 0.0000045,
                                         "source": "https://openrouter.ai/api/v1/models"},
        "decoding": {"temperature_primary": 0.0, "temperature_modules_T0.7": [101,102,103,104,105],
                     "max_tokens": CFG.MAX_TOKENS, "repair_limit": CFG.REPAIR_LIMIT},
        "seeds": {"bank_gen": CFG.GEN_SEED, "bootstrap": CFG.BOOTSTRAP_SEED,
                  "H2": CFG.H2_SEEDS, "replication": CFG.REPL_SEEDS},
        "N_values": CFG.N_VALUES, "N_conv_values": CFG.N_CONV_VALUES, "primary_N": CFG.PRIMARY_N,
        "delta_F1": CFG.DELTA_F1, "delta_F3": CFG.DELTA_F3,
        "arms": CFG.ARMS, "families": CFG.FAMILIES,
        "fblock_token_counts_o200k": ftok, "fblock_cap_check": cap_check,
        "asset_sha256": hashes,
        "manifest_written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "smoke_declaration": "W0e smoke UNSCORED, excluded from all statistics by pre-declaration",
        "transport": "OpenRouter /chat/completions with operator credential from Hermes auth store",
    }
    fp = RESULTS / "manifest.json"
    if fp.exists():
        sys.exit("REFUSING to overwrite existing manifest.json (already initialized)")
    fp.write_text(json.dumps(manifest, indent=1))
    print("manifest written:", fp)
    print("cap_check:", json.dumps(cap_check))
    bad = [k for k, v in cap_check.items() if not v["within"]]
    print("caps within budget:", not bad, bad or "")

if __name__ == "__main__":
    main()
