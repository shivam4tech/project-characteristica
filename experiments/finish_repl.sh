#!/bin/bash
# Resilient repl finisher: waits out upstream 429 congestion, resumes runner until repl complete.
cd /home/shivam/philosophy/project-characteristica/experiments
PY=.venv-e1/bin/python
export PYTHONDONTWRITEBYTECODE=1

TARGET=$(grep -c "" results/E1/repl_outcomes.csv)
echo "[repl-fin] start: $((TARGET-1)) rows done"

for attempt in 1 2 3 4 5 6; do
  echo "[repl-fin] attempt $attempt at $(date +%H:%M:%S)"
  $PY harness/runner.py repl --families EX,CP,TU
  ROWS=$(grep -c "" results/E1/repl_outcomes.csv)
  echo "[repl-fin] after attempt $attempt: $((ROWS-1)) rows"
  # repl target: 2 reps x 3 families x 50 items = 300 rows + header
  if [ "$ROWS" -ge 301 ]; then
    echo "[repl-fin] COMPLETE at $((ROWS-1)) rows"
    break
  fi
  echo "[repl-fin] cooling down 5 min before next attempt..."
  sleep 300
done
echo "[repl-fin] done at $(date +%H:%M:%S)"
