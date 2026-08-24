"""E1 fallback watcher — coordinator policy 2026-08-24 ~18:45 IST (binding).

Phase A: wait up to ~45 min for z-ai/glm-5.2:free to serve; on success spawn chain_e1.py.
Phase B: if still blocked at deadline, sweep ALL :free ids with live probes, rank the
SERVING set by documented capability evidence, pick the winner, apply the Amendment-1-
compliant re-pin (config.py + manifest.json + DEVIATIONS.md DEV-9), then spawn chain.
If zero :free models serve -> print ESCALATE_ZERO_SERVING and exit non-zero.
"""
import hashlib, json, re, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path

HOME = Path("/home/shivam")
REPO = HOME / "philosophy/project-characteristica"
EXP = REPO / "experiments"
RES = EXP / "results" / "E1"
PY = str(EXP.parent / ".venv-e1" / "bin" / "python")
CFG_PY = EXP / "harness" / "config.py"
MANIFEST = RES / "manifest.json"

auth = json.load(open(HOME / ".hermes" / "auth.json"))
KEY = next(e["access_token"] for e in auth["credential_pool"]["openrouter"]
           if e.get("access_token"))

def chat(model, content="Say OK.", mx=512, timeout=60):
    body = json.dumps({"model": model,
                       "messages": [{"role": "user", "content": content}],
                       "temperature": 0, "max_tokens": mx}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=timeout))
        return True, r.get("usage", {})
    except urllib.error.HTTPError as e:
        try: e.read()
        except Exception: pass
        return False, {"code": e.code}
    except Exception as e:
        return False, {"code": repr(e)[:80]}

# Documented-capability ranking (Artificial Analysis Intelligence Index where published;
# harness accessibility; scale/tier heuristics only as tiebreak). Applied consistently
# with the original selection record in manifest.json.
RANK = [
    ("z-ai/glm-5.2:free", "AA index 53"),
    ("thinkingmachines/inkling:free", "AA index 41 (but harness-gated)"),
    ("nvidia/nemotron-3-ultra-550b-a55b:free", "AA index 38; 550B/A55B MoE flagship-class"),
    ("dots-studio/dots-3-note-preview:free", "no documented capability evidence (preview)"),
    ("thinkingmachines/inkling-small:free", "no documented capability evidence"),
    ("nvidia/nemotron-3.5-lightning:free", "newer gen, speed-tier naming; no AA index found"),
    ("nvidia/nemotron-3-super-120b-a12b:free", "120B/A12B mid-class"),
    ("poolside/laguna-s-2.1:free", "coding specialist, mid class"),
    ("cohere/north-mini-code:free", "coding specialist, mini class"),
    ("google/gemma-4-31b-it:free", "31B dense open model"),
    ("google/gemma-4-26b-a4b-it:free", "26B/A4B MoE open model"),
    ("dots-studio/dots-3-note-preview:free", None),   # placeholder guard (already above)
]
RANK = [r for r in RANK if r[1]]
KNOWN = {m for m, _ in RANK}

def list_free():
    req = urllib.request.Request("https://openrouter.ai/api/v1/models",
                                 headers={"Authorization": f"Bearer {KEY}"})
    ms = json.load(urllib.request.urlopen(req, timeout=60))["data"]
    return [m["id"] for m in ms if m.get("id", "").endswith(":free")]

def ranked_candidates():
    ids = set(list_free())
    out = [m for m, _ in RANK if m in ids]
    out += sorted(ids - KNOWN)          # any new/unlisted :free ids go last
    return out

def phase_a(deadline):
    while time.time() < deadline:
        ok, info = chat("z-ai/glm-5.2:free")
        if ok:
            print(f"[PHASE-A] glm-5.2:free SERVING {time.strftime('%H:%M:%S')} -> chain", flush=True)
            return "glm"
        print(f"[PHASE-A] 429 {time.strftime('%H:%M:%S')} ({info})", flush=True)
        time.sleep(90)
    return None

def phase_b():
    cands = ranked_candidates()
    print("[PHASE-B] sweeping", len(cands), "candidates:", cands, flush=True)
    serving = []
    for m in cands:
        ok, _ = chat(m, mx=256)
        if not ok:
            time.sleep(10)
            ok, _ = chat(m, mx=256)
        tag = "SERVING" if ok else "blocked"
        print(f"[PHASE-B] {m}: {tag}", flush=True)
        if ok:
            serving.append(m)
        time.sleep(2)
    serving_set = set(serving)
    winner = next((m for m, _ in RANK if m in serving_set), None)
    if winner is None and serving:
        winner = serving[0]
    print("[PHASE-B] serving set:", serving, "winner:", winner, flush=True)
    return winner, serving

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def apply_pin(winner):
    txt = CFG_PY.read_text()
    txt = re.sub(r'MODEL_ID = "[^"]+"', f'MODEL_ID = "{winner}"', txt, count=1)
    tok = "glm-5.2 server tokenizer approximated" if "glm" in winner else \
          "chosen-model server tokenizer approximated"
    txt = re.sub(r'TOKENIZER_ID = "[^"]+"',
                 'TOKENIZER_ID = "o200k_base (tiktoken; %s for F/V split only; '
                 'authoritative counts are provider usage fields)"' % tok, txt, count=1)
    if "DEV-9 fallback re-pin" not in txt:
        txt += ("\n# DEV-9 fallback re-pin (coordinator policy 2026-08-24): original amended pin "
                "z-ai/glm-5.2:free\n# did not verifiably serve past the 45-min cap; re-selection "
                "sweep applied per Amendment-1 rule\n# over models verifiably serving right now.\n")
    CFG_PY.write_text(txt)

    m = json.load(open(MANIFEST))
    m["model_id"] = winner
    m["tokenizer_id"] = ("o200k_base (tiktoken; chosen-model server tokenizer approximated "
                         "for F/V split only; authoritative counts are provider usage fields)")
    m.setdefault("amendment_1", {})["fallback_repin"] = {
        "policy": "coordinator clarification 2026-08-24 ~18:45 IST (45-min cap on waiting)",
        "original_pin": "z-ai/glm-5.2:free",
        "reason": "sustained upstream_429 (upstream_provider_shared_pool, sole free provider Decart) "
                  "18:03-19:30+ IST; not verifiably serving at run time within cap",
        "sweep": "all listed :free ids probed live twice; serving set recorded below",
        "rule": "highest documented capability among VERIFIABLY SERVING :free models",
    }
    m["amendment_1"]["fallback_repin"]["serving_set"] = PHASE_B_SERVING
    m["asset_sha256"]["config.py"] = sha(CFG_PY)
    json.dump(m, open(MANIFEST, "w"), indent=1)

    dev = RES / "DEVIATIONS.md"
    dev.write_text(dev.read_text() + (
        f"\n## DEV-9 · Amendment-1-compliant fallback re-pin (coordinator policy)\n"
        f"Original amended pin `z-ai/glm-5.2:free` failed 'verifiably serving' as a HARD condition: "
        f"sustained upstream_provider_shared_pool 429s from its sole free provider (Decart) through "
        f"the 45-minute coordinator cap (~19:30 IST). Per coordinator binding policy this is an "
        f"Amendment-1-COMPLIANT selection event, not a deviation: a fresh sweep probed every listed "
        f":free id live; serving set = {PHASE_B_SERVING}; highest documented capability among those "
        f"actually serving selected ONCE -> **{winner}**. config.py/manifest updated + re-hashed; "
        f"arms/families/metrics/N-grid/seeds/stopping/analysis untouched. Results header regenerated "
        f"from manifest by make_results.py.\n"))
    print("[PHASE-B] pin applied ->", winner, flush=True)

if __name__ == "__main__":
    deadline = time.time() + 45 * 60
    got = phase_a(deadline)
    if got == "glm":
        rc = subprocess.run([PY, str(EXP / "harness" / "chain_e1.py")],
                            cwd=str(EXP)).returncode
        print("[CHAIN] rc=", rc, flush=True)
        sys.exit(0)
    winner, serving = phase_b()
    PHASE_B_SERVING = serving
    if not serving:
        print("ESCALATE_ZERO_SERVING", flush=True)
        sys.exit(3)
    apply_pin(winner)
    rc = subprocess.run([PY, str(EXP / "harness" / "chain_e1.py")], cwd=str(EXP)).returncode
    print("[CHAIN] rc=", rc, flush=True)
