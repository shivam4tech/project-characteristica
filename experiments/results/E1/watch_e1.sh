#!/bin/bash
# Phase W watcher v2: 18 cycles x sleep 540, early exit if runner processes gone.
# Progress = raw_outputs mtimes after chain restart (22:28), since re-run overwrites paths.
cd /home/shivam/philosophy/project-characteristica || exit 9
for i in $(seq 1 18); do
  sleep 540
  n=$(ps aux | grep -E 'runner\.py|chain_e1\.py' | grep -v grep | wc -l)
  f=$(find experiments/results/E1/raw_outputs -type f -newermt '2026-08-24 22:28' 2>/dev/null | wc -l)
  echo "cycle=$i procs=$n done_since_restart=$f/600 $(date +%H:%M)"
  if [ "$n" -eq 0 ]; then echo "EARLY_EXIT procs_gone at cycle $i"; exit 0; fi
done
echo "CYCLES_EXHAUSTED procs still alive"
