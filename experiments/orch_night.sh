#!/bin/bash
# Overnight orchestrator: chain ALL remaining E1 stages with zero idle.
# Waits for primary runners to exit, then runs h2, repl, f3 in sequence.
cd /home/shivam/philosophy/project-characteristica/experiments
PY=.venv-e1/bin/python
export PYTHONDONTWRITEBYTECODE=1

echo "[orch] $(date +%H:%M:%S) waiting for primary runners to finish..."
# Wait until fewer than 2 primary runners remain (both done or crashed)
while [ "$(ps aux | grep 'runner.py primary' | grep -v grep | wc -l)" -ge 2 ]; do
  sleep 120
done
echo "[orch] $(date +%H:%M:%S) primaries finished. Stage sweep begins."

for stage in h2 repl f3; do
  echo "[orch] $(date +%H:%M:%S) starting stage: $stage"
  $PY harness/runner.py $stage >> results/E1/orch_stages.log 2>&1
  echo "[orch] $(date +%H:%M:%S) stage $stage exit=$?"
done

echo "[orch] $(date +%H:%M:%S) ALL STAGES COMPLETE"
