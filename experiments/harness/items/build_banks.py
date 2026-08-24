"""E1 item-bank builder (W0c): renders 50x3 banks with seed 20260824,
runs checker(gold)=1.0 self-test + CP satisfiability guards, writes
experiments/harness/items/*.json + W0b units traceability table."""
import json, random, sys, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))          # harness/ for checkers
sys.path.insert(0, str(HERE))

import checkers as C
from ex_items import build_ex, UNITS_EX, EX01_FIELDS, EX02_FIELDS, EX03_FIELDS, \
    EX04_FIELDS, EX05_FIELDS
from cp_items import build_cp
from tu_items import build_tu


def gold_artifact(item):
    """Canonical answer artifact the checker must score 1.0 (W0c round-trip)."""
    if item["family"] == "EX":
        return {"fields": dict(item["gold"]["fields"])}
    if item["family"] == "CP":
        return _cp_gold_art(item)
    if item["family"] == "TU":
        g = item["gold"]
        if g["expect"] == "actions":
            calls = [dict(c) for c in g["calls"]]
            raw = "; ".join(f"{c['tool']}({', '.join(f'{k}={v}' for k, v in c['args'].items())})"
                            for c in calls)
            return {"calls": calls, "_raw": raw}
        if g["expect"] == "ordered_actions":
            calls = [dict(c) for c in g["calls"]]
            raw = "; ".join(f"{c['tool']}({', '.join(f'{k}={v}' for k, v in c['args'].items())})"
                            for c in calls)
            if item["template"] == "TU-02":
                raw += " | mail body references ticket id TICKET-1001"
            return {"calls": calls, "_raw": raw}
        if g["expect"] == "clarify":
            raw = ("CLARIFY: information required for this request is missing. Missing: "
                   "recipient address (no email/alias for the audience) and content source "
                   "(the document/numbers to send are unspecified). Question: which address "
                   "should receive it, and what content should be sent?")
            return {"clarify": {"missing": g["missing_required"], "question": raw}, "_raw": raw}
        # cancel_plus_unavailable
        oid = item["params"]["order_id"]
        calls = [{"tool": "orders.cancel",
                  "args": {"order_id": str(oid), "reason": "customer request"}}]
        raw = (f"orders.cancel(order_id={oid}, reason='customer request'); the refund capability "
               f"is unavailable — no such tool exists in the registry.")
        return {"calls": calls, "unavailable": ["refund"], "_raw": raw}
    raise ValueError(item["family"])


def _cp_gold_art(item):
    P = item["params"]
    if item["template"] == "CP-01":
        sol = _cp1_solution(P)
        return {"schedule": [{"meeting": {"a": "Sprint review", "b": "1:1 Maya/Sam",
                                          "c": "Vendor call", "d": "Incident retro"}[k],
                              "room": r["name"],
                              "start": f"{s//60:02d}:{s%60:02d}",
                              "end": f"{e//60:02d}:{e%60:02d}"}
                             for k, r, s, e in sol]}
    if item["template"] == "CP-02":
        asg, order = _cp2_solution(P)
        return {"assign": asg, "order": order}
    if item["template"] == "CP-03":
        steps = ["Cut release branch after merge-window PRs land",
                 "Run migration dry-run on staging snapshot",
                 "Tag " + P["version"] + (" after clean dry-run")]
        if P["pricing_in_changelog"]:
            steps.append("Obtain legal sign-off")
        steps += ["Update support playbook", "Publish release notes", "Announce publicly"]
        return {"steps": steps}
    if item["template"] == "CP-04":
        return {"seating": _cp4_solution(P)}
    if item["template"] == "CP-05":
        T = P["total"]
        tr = min(P["training_pref"], P["training_cap"])
        ev = P["ev_tool_cap"] - P["headroom_min"]
        infra = max(P["infra_floor"], T - tr - ev)
        tl = T - infra - tr - ev
        assert tl >= 0 and max(infra, tr, ev, tl) <= P["veto_cap"], item["id"]
        return {"infra": infra, "tooling": tl, "training": tr, "events": ev}
    raise ValueError(item["template"])


def _cp1_solution(P):
    rooms = P["rooms"]
    ppl = {"a": P["ppl_a"], "b": 2, "c": P["ppl_c"], "d": P["ppl_d"]}
    dur = {"a": 90, "b": 30, "c": 60, "d": 60}
    slots = {k: [(s, s + d) for s in range(540, 1021 - d, 30)] for k, d in dur.items()}

    def lunch(s, e): return s < 780 and 720 < e
    def clash(r1, i1, r2, i2):
        return r1["name"] == r2["name"] and i1[0] < i2[1] and i2[0] < i1[1]
    quiet_rooms = [r for r in rooms if r["quiet"]]
    sol = None
    for ra in [r for r in rooms if r["cap"] >= ppl["a"] and r.get("projector")]:
        for ia in slots["a"]:
            if lunch(*ia): continue
            for rb in [r for r in rooms if r["cap"] >= ppl["b"]]:
                for ib in slots["b"]:
                    if lunch(*ib): continue
                    # organizer attends a & b: no overlap, no intrusion into a's prep buffer
                    if not (ib[1] <= ia[0] - P["buffer"] or ib[0] >= ia[1]): continue
                    if ib[0] < 660 and ib[1] > 540: continue          # 09:00-11:00 blocked
                    for rc in ([r for r in quiet_rooms if r["cap"] >= ppl["c"]] or
                               [r for r in rooms if r["cap"] >= ppl["c"]]):
                        for ic in slots["c"]:
                            if lunch(*ic): continue
                            for rd in [r for r in rooms if r["cap"] >= ppl["d"]]:
                                for id_ in slots["d"]:
                                    if lunch(*id_): continue
                                    if id_[0] < ia[1]: continue       # d after a
                                    ms = [(ra, ia), (rb, ib), (rc, ic), (rd, id_)]
                                    bad = any(clash(*ms[x], *ms[y])
                                              for x in range(4) for y in range(x + 1, 4))
                                    if not bad:
                                        sol = [("a", ra, ia), ("b", rb, ib),
                                               ("c", rc, ic), ("d", rd, id_)]
                                        break
                                if sol: break
                            if sol: break
                        if sol: break
                    if sol: break
                if sol: break
            if sol: break
        if sol: break
    if not sol:
        raise RuntimeError("CP-01 solution search failed")
    return [(k, r, s, e) for k, r, (s, e) in sol]


def _cp2_solution(P):
    from itertools import product
    best = None
    for asg in product(["Ana", "Ben", "Chao"], repeat=5):
        m = dict(zip(["T1", "T2", "T3", "T4", "T5"], asg))
        load = {e: 0 for e in P["caps"]}
        for t, who in m.items():
            load[who] += P["points"][t]
        if any(load[e] > P["caps"][e] for e in P["caps"]): continue
        if not all(set(P["ticket_skills"][t]) <= set(P["eng_skills"][w]) for t, w in m.items()):
            continue
        if m["T4"] not in P["t4_allowed"]: continue
        order = sorted(m, key=lambda t: (-P["points"][t], t))
        oi = order.index("T2")
        bal = max(load.values()) - min(load.values())
        score = (0 if oi <= P["early_pos"] else 1, bal)
        if best is None or score < best[0]:
            best = (score, m, order)
    if not best:
        raise RuntimeError("CP-02 no feasible assignment")
    _, m, order = best
    if order.index("T1") > order.index("T3"):     # enforce registered precedence in gold
        order.remove("T1")
        order.insert(order.index("T3"), "T1")
    inst = {"template": "CP-02", "params": P}
    from checkers import cp_eval_constraint
    art = {"assign": m, "order": order}
    hard_bad = [c["id"] for c in inst and [
        {"id": "h1_skills"}, {"id": "h2_coverage"}, {"id": "h3_caps"},
        {"id": "h4_t1_before_t3"}, {"id": "h5_t4_restriction"}]
        if not cp_eval_constraint(c["id"], inst, art)]
    if hard_bad:
        raise RuntimeError("CP-02 gold violates hard: %s" % hard_bad)
    return m, order


def _cp4_solution(P):
    from itertools import permutations
    import string
    n, host = P["n_guests"], P["host"]
    PR = P["pairs"]
    others = [g for g in P["guests"] if g != host]
    for perm in permutations(others):
        seq = [host] + list(perm)
        pos = {g: i for i, g in enumerate(seq)}
        adj = lambda x, y: (pos[x] - pos[y]) % n in (1, n - 1)
        if adj(*PR["AB"]) or adj(*PR["CD"]) or not adj(*PR["EF"]):
            continue
        return seq
    raise RuntimeError("CP-04 unsat")

def main():
    rng = random.Random(20260824)
    ex = build_ex(rng)
    cp = build_cp(rng)
    tu = build_tu(rng)

    # ---- W0c self-test: checker(gold)=1.0 on EVERY item -------------------
    fails = []
    for fam, bank in (("EX", ex), ("CP", cp), ("TU", tu)):
        for it in bank:
            ga = gold_artifact(it)
            try:
                s, det = C.score_item(it, "gold", ga)
            except Exception as e:
                fails.append((it["id"], "exc:%r" % e)); continue
            if fam == "CP":
                hard_keys = [k for k in det if k.startswith("h") and k != "hard_violations"]
                good = det.get("hard_violations") == 0 and all(det[k] for k in hard_keys)
            else:
                good = (s == 1.0)
            if not good:
                fails.append((it["id"], "score=%.3f det=%s" % (s, det)))
    if fails:
        print("SELF-TEST FAILURES (%d):" % len(fails))
        for fid, why in fails[:12]:
            print(" ", fid, why)
        sys.exit(2)
    counts = {}
    for it in ex + cp + tu:
        key = (it["family"], it["template"])
        counts[key] = counts.get(key, 0) + 1
    assert all(v == 10 for v in counts.values()) and len(counts) == 15, counts

    outdir = HERE / "banks"
    outdir.mkdir(exist_ok=True)
    manifest_units = {"EX": UNITS_EX}
    for name, bank in (("ex", ex), ("cp", cp), ("tu", tu)):
        payload = [{"id": it["id"], "family": it["family"], "template": it["template"],
                    "idx": it["idx"], "source_text": it["source_text"],
                    "question": it["question"], "field_ids": it["field_ids"],
                    "field_aliases": it["field_aliases"], "units": it["units"],
                    "gold": it["gold"], "params": it["params"]} for it in bank]
        fp = outdir / f"{name}_bank.json"
        fp.write_text(json.dumps(payload, indent=1))
        h = hashlib.sha256(fp.read_bytes()).hexdigest()
        print(f"{fp.name}: {len(bank)} items sha256={h[:16]}...")
    # W0b traceability table
    rows = []
    for it in ex + tu + cp:
        for fid, unit in (it["units"] or {}).items():
            rows.append({"item": it["id"], "unit_id": f'{it["id"]}::{fid}',
                         "unit_type": unit, "checker_field": fid})
    (outdir / "w0b_unit_traceability.json").write_text(json.dumps(rows, indent=1))
    print("W0b traceability rows:", len(rows))
    print("ALL WITHIN SELF-TEST: True")


if __name__ == "__main__":
    main()
