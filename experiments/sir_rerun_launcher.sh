#!/bin/bash
# SIR-arm re-run launcher: waits out 429 congestion (probe every 5 min), then runs the 150-cell re-run.
cd /home/shivam/philosophy/project-characteristica/experiments
PY=.venv-e1/bin/python
export PYTHONDONTWRITEBYTECODE=1

echo "[sir-rerun] $(date +%H:%M:%S) probing ox-alpha availability..."
for i in $(seq 1 36); do   # up to 3 hours of waiting
  $PY - <<'EOF'
import json, urllib.request, sys
from pathlib import Path
auth=json.load(open(Path.home()/".hermes"/"auth.json"))
key=next(e["access_token"] for e in auth["credential_pool"]["openrouter"] if e.get("access_token"))
body=json.dumps({"model":"stealth/ox-alpha","messages":[{"role":"user","content":"Say OK."}],"max_tokens":8192}).encode()
req=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",data=body,
    headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
try:
    urllib.request.urlopen(req,timeout=30)
    sys.exit(0)
except Exception:
    sys.exit(1)
EOF
  if [ $? -eq 0 ]; then
    echo "[sir-rerun] $(date +%H:%M:%S) serving — launching re-run"
    break
  fi
  echo "[sir-rerun] probe $i: congested, waiting 5 min"
  sleep 300
done

# Run the SIR re-run: primary mode restricted to CSIR-SIR arm via env override is not supported,
# so use repl-style targeted run: run each family's SIR jobs through the runner's resume logic.
$PY harness/runner.py rerun_sir
echo "[sir-rerun] exit=$?"
