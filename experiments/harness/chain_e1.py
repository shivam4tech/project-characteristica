"""E1 chain driver: primary -> comparator pick -> repl(EX) -> repl(TU) -> h2 -> f3,
invoking the frozen runner modes in sequence with checkpoint-resume semantics.
No post-hoc filtering; each stage appends incrementally (BATCH_FLUSH=10).
"""
import csv, json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path

EXP = Path("/home/shivam/philosophy/project-characteristica/experiments")
RES = EXP / "results" / "E1"
PY = str(EXP.parent / ".venv-e1" / "bin" / "python")
RUNNER = str(EXP / "harness" / "runner.py")
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin:/usr/local/bin",
       "HOME": "/home/shivam", "LANG": "C.UTF-8"}

def sh(args):
    print("==>", " ".join(args), flush=True)
    return subprocess.run([PY] + args, cwd=str(EXP), env=ENV).returncode

def latest_valid(rows):
    best = {}
    for r in sorted(rows, key=lambda r: r.get("ts", "")):
        if r.get("transport_fail") != "True":
            best[(r["arm"], r["item_id"])] = r
    return best

def strongest_baseline():
    """pre-reg §7 fixed comparator rule on PRIMARY gate success."""
    fp = RES / "outcomes.csv"
    if not fp.exists(): return {}
    lv = latest_valid(list(csv.DictReader(open(fp))))
    g = defaultdict(lambda: [0, 0.0])
    for (arm, iid), r in lv.items():
        c = g[(arm, r["family"])]
        c[0] += 1
        c[1] += 1.0 if r["gate_pass"] == "True" else 0.0
    comp = {}
    order = {a: i for i, a in enumerate(["NL-plain", "NL-opt", "JSON"])}
    for fam in ("EX", "CP", "TU"):
        cands = []
        for arm in ("NL-plain", "NL-opt", "JSON"):
            n, s = g.get((arm, fam), [0, 0.0])
            if n:
                cands.append((s / n, arm))
        if cands:
            comp[fam] = max(cands)[1]
    return comp

def count_done():
    fp = RES / "outcomes.csv"
    if not fp.exists(): return 0
    return len(latest_valid(list(csv.DictReader(open(fp)))))

t0 = time.time()
# 1) primary
rc = sh(["harness/runner.py", "primary"])
print(f"[chain] primary rc={rc} done={count_done()}/600 ({time.time()-t0:.0f}s)", flush=True)

comp = strongest_baseline()
print("[chain] comparators:", comp, flush=True)

# 2) stochastic replication vs strongest baseline, EX and TU separately (§7)
for fam in ("EX", "TU"):
    b = comp.get(fam, "JSON")
    rc = sh(["harness/runner.py", "repl", "--families", fam, "--comparator", b])
    print(f"[chain] repl[{fam} vs {b}] rc={rc}", flush=True)

# 3) H2 variance module (order after repl: both T=0.7; registered endpoints equal priority;
#    h2 placed second only because repl depends on primary-derived comparators)
rc = sh(["harness/runner.py", "h2"])
print(f"[chain] h2 rc={rc}", flush=True)

# 4) F3 round-trip probe over valid SIR docs
rc = sh(["harness/runner.py", "f3"])
print(f"[chain] f3 rc={rc}", flush=True)

# 5) full analysis assembly
rc = sh(["harness/make_results.py"])
print(f"[chain] analysis rc={rc}", flush=True)
print(f"[chain] COMPLETE in {(time.time()-t0)/60:.1f} min", flush=True)
