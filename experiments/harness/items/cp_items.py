"""E1 Family CP item builder (pre-reg §2.2). Template idx 0 = verbatim instance.
CP draws are brute-force satisfiability-checked at build time (reject+redraw)."""
import itertools, datetime as _dt
from checkers import norm_txt
from ex_items import HDR

def build_cp(rng):
    items = []
    # ---------------- CP-01 room-day scheduling ----------------
    for i in range(10):
        for attempt in range(200):
            capA = 10 if i == 0 else 8 + rng.randint(0, 4)      # caps ±2-ish around base
            capB = 4 if i == 0 else 3 + rng.randint(0, 3)
            capC = 8 if i == 0 else 6 + rng.randint(0, 4)
            ppl_a = capC - rng.randint(0, 2)
            ppl_c = rng.randint(2, min(4, capB))
            ppl_d = 6 if i == 0 else rng.randint(5, min(9, max(capA, capB, capC) - 1))
            quiet_on = rng.choice(["Atlas", "Borel"])
            rooms = [{"name": "Atlas", "cap": capA, "projector": False,
                      "quiet": quiet_on == "Atlas"},
                     {"name": "Borel", "cap": capB, "projector": False,
                      "quiet": quiet_on == "Borel"},
                     {"name": "Cyrus", "cap": capC, "projector": True, "quiet": False}]
            inst = _cp1_inst(i, rooms, ppl_a, ppl_c, ppl_d)
            if _cp1_sat(rooms, ppl_a, ppl_c, ppl_d):
                items.append(inst); break
        else:
            raise RuntimeError("CP-01 unsat after 200 draws")
    # ---------------- CP-02 allocation ----------------
    for i in range(10):
        skills = {"Ana": ["python", "sql"], "Ben": ["rust", "python"],
                  "Chao": ["sql", "rust"]}
        tsk_sk = {"T1": ["python"], "T2": ["python", "sql"], "T3": ["sql"],
                  "T4": ["rust"], "T5": []}
        for attempt in range(300):
            pts = {"T1": 3, "T2": 5, "T3": 2, "T4": 8, "T5": 1} if i == 0 else \
                  {t: rng.randint(1, 8) for t in ("T1", "T2", "T3", "T4", "T5")}
            if i == 0:
                # DEV-1 (W0c-stage, pre-first-scored-call): pre-reg §2.2 CP-02 worked
                # instance is INFEASIBLE as transcribed (T2->Ana forced; T1+T4=11 >
                # Ben cap 9; T4=8 > Chao cap 5). Minimal repair: Ben cap 9 -> 11.
                # All other values verbatim. Logged in manifest + RESULTS deviations.
                caps = {"Ana": 6, "Ben": 11, "Chao": 5}
            else:
                share = int(round(sum(pts.values()) / 3))
                caps = {e: share + rng.randint(-1, 2) for e in
                        ("Ana", "Ben", "Chao")}
            ok_assign = any(_cp2_feasible(asg, pts, caps, tsk_sk, skills)
                            for asg in itertools.product(["Ana", "Ben", "Chao"], repeat=5))
            if ok_assign:
                items.append(_cp2_inst(i, pts, caps)); break
        else:
            raise RuntimeError("CP-02 unsat after 300 draws")
    # ---------------- CP-03 release checklist ----------------
    for i in range(10):
        pricing = True if i % 2 else False     # half mention pricing (i==0: False, per pre-reg)
        ver = "v2.7.0" if i == 0 else f"v{rng.randint(1,5)}.{rng.randint(0,9)}.{rng.randint(0,9)}"
        items.append(_cp3_inst(i, ver, pricing))
    # ---------------- CP-04 seating ----------------
    import string
    for i in range(10):
        n = 8 if i == 0 else rng.randint(6, 10)
        labels = list(string.ascii_uppercase[:n])
        if i > 0:                       # isomorphic relabeling
            perm = labels[:]; rng.shuffle(perm)
            m = dict(zip(labels, perm))
        else:
            m = {g: g for g in labels}
        host = m["A"]                    # 'fixed host' relabeled too
        cons = {"AB": (m["A"], m["B"]), "CD": (m["C"], m["D"]), "EF": (m["E"], m["F"]),
                "GH_soft": (m["G"], m["H"]) if n >= 8 else None}
        sat = _cp4_sat(n, labels, cons)
        assert sat, "CP-04 draw unsat"
        items.append(_cp4_inst(i, n, host, cons, labels))
    # ---------------- CP-05 budget allocation ----------------
    for i in range(10):
        T = 12000 if i == 0 else rng.randrange(8000, 20001, 500)
        P = {"total": T,
             "infra_floor": 4000 if i == 0 else int(round(T * 0.33 / 100) * 100),
             "training_cap": 3000 if i == 0 else int(round(T * 0.25 / 100) * 100),
             "ev_tool_cap": 5000 if i == 0 else int(round(T * 0.42 / 100) * 100),
             "veto_cap": 6000 if i == 0 else int(round(T * 0.50 / 100) * 100),
             "training_pref": 1500 if i == 0 else int(round(T * 0.125 / 100) * 100),
             "headroom_min": 250, "infra_headroom": 1000}
        assert _sat_budget(P), "budget unsat"
        items.append(_cp5_inst(i, P))
    return items

# ---------------------------------------------------------------- CP-01 -----
def _cp1_inst(i, rooms, ppl_a, ppl_c, ppl_d):
    rtxt = "; ".join(f"{r['name']}(cap {r['cap']}" + (", projector" if r["projector"] else "")
                     + (", quiet room" if r["quiet"] else "") + ")" for r in rooms)
    src = (f"{HDR}\nRooms: {rtxt}. Bookable grid 09:00–17:00 in 30-min slots; lunch "
           f"12:00–13:00 is blacked out. Schedule:\n(a) Sprint review, {ppl_a} people, needs a "
           f"projector, 90 minutes; the organizer is unavailable the 15 minutes right before it "
           f"(prep buffer).\n(b) 1:1 Maya/Sam, 30 minutes; neither Maya nor Sam is available "
           f"09:00–11:00.\n(c) Vendor call, {ppl_c} people; a quiet room is preferred (soft).\n"
           f"(d) Incident retro, {ppl_d} people; must start after the sprint review ends.")
    q = ("Produce a scheduling artifact: one line per meeting as "
         "'meeting=<name> room=<name> start=HH:MM end=HH:MM' for meetings a-d, satisfying every "
         "hard constraint. Meetings may run in parallel only in different rooms.")
    cons = [{"id": "h1_dur_a", "hard": True}, {"id": "h2_projector_a", "hard": True},
            {"id": "h3_capacity", "hard": True}, {"id": "h4_lunch", "hard": True},
            {"id": "h5_org_buffer", "hard": True}, {"id": "h6_avail_b", "hard": True},
            {"id": "h7_precedence_d", "hard": True}, {"id": "h8_grid", "hard": True},
            {"id": "h9_complete", "hard": True}, {"id": "s1_quiet_c", "hard": False}]
    return {"id": f"CP-01-{i:02d}", "family": "CP", "template": "CP-01", "idx": i,
            "source_text": src, "question": q, "field_ids": [], "field_aliases": {},
            "units": {}, "params": {"rooms": rooms, "ppl_a": ppl_a, "ppl_c": ppl_c,
                                    "ppl_d": ppl_d, "dur_a": 90, "buffer": 15,
                                    "blk_start": 540, "blk_end": 660},
            "gold": {"constraints": cons}}

def _cp1_sat(rooms, ppl_a, ppl_c, ppl_d):
    """Brute force: place a(90m),b(30m),c(60m),d(60m) on the 30-min grid."""
    slots90 = [(s, s + 90) for s in range(540, 1021 - 90, 30)]
    slots30 = [(s, s + 30) for s in range(540, 1021 - 30, 30)]
    slots60 = [(s, s + 60) for s in range(540, 1021 - 60, 30)]
    proj = [r for r in rooms if r["projector"]]
    if not proj or proj[0]["cap"] < ppl_a: return False
    for ra in rooms:
        if ra["cap"] < ppl_a: continue
        for sa, ea in slots90:
            if _hits_lunch(sa, ea): continue
            for rb in rooms:
                if rb["cap"] < 2: continue
                for sb, eb in slots30:
                    if _hits_lunch(sb, eb): continue
                    if not (sb > ea or eb + 15 <= sa): continue   # organizer buffer+overlap
                    if sb < 660 and eb > 540: continue            # 09:00-11:00 blocked
                    for rc in rooms:
                        if rc["cap"] < ppl_c: continue
                        for sc, ec in slots60:
                            if _hits_lunch(sc, ec): continue
                            for rd in rooms:
                                if rd["cap"] < ppl_d: continue
                                for sd, ed in slots60:
                                    if _hits_lunch(sd, ed): continue
                                    if sd < ea: continue          # precedence d after a
                                    if _pair_clash(ra, sa, ea, rb, sb, eb) or \
                                       _pair_clash(ra, sa, ea, rc, sc, ec) or \
                                       _pair_clash(ra, sa, ea, rd, sd, ed) or \
                                       _pair_clash(rb, sb, eb, rc, sc, ec) or \
                                       _pair_clash(rb, sb, eb, rd, sd, ed) or \
                                       _pair_clash(rc, sc, ec, rd, sd, ed):
                                        continue
                                    return True
    return False

def _pair_clash(r1, s1, e1, r2, s2, e2):
    return r1["name"] == r2["name"] and s1 < e2 and s2 < e1
def _hits_lunch(s, e): return s < 780 and 720 < e

# ---------------------------------------------------------------- CP-02 -----
def _cp2_feasible(asg, pts, caps, tsk_sk, skills):
    load = {e: 0 for e in caps}
    for t, who in zip(("T1", "T2", "T3", "T4", "T5"), asg):
        if not set(tsk_sk[t]) <= set(skills[who]): return False
        load[who] += pts[t]
    return all(load[e] <= caps[e] for e in caps)

def _cp2_inst(i, pts, caps):
    src = (f"{HDR}\nAssign five tickets to engineers. Tickets: T1(python,{pts['T1']} pts), "
           f"T2(python+sql,{pts['T2']} pts), T3(sql,{pts['T3']} pts), T4(rust,{pts['T4']} pts), "
           f"T5(any skill,{pts['T5']} pts). Engineers: Ana(python, sql, capacity {caps['Ana']} "
           f"pts), Ben(rust, python, capacity {caps['Ben']} pts), Chao(sql, rust, capacity "
           f"{caps['Chao']} pts). HARD: every ticket assigned exactly once; skill matches; "
           f"per-person point loads stay within capacity; T4 goes to Ben or Chao only; T1 "
           f"completes before T3 starts (give an execution order of the tickets). SOFT, ranked "
           f"lexicographically: 1) T2 early in the execution order, 2) even load balance across "
           f"engineers, 3) minimize per-person context switches.")
    q = ("Produce the allocation artifact as JSON with keys 'assign' (ticket->person) and "
         "'order' (execution order list of ticket ids).")
    cons = [{"id": "h1_skills", "hard": True}, {"id": "h2_coverage", "hard": True},
            {"id": "h3_caps", "hard": True}, {"id": "h4_t1_before_t3", "hard": True},
            {"id": "h5_t4_restriction", "hard": True}, {"id": "s1_t2_early", "hard": False},
            {"id": "s2_balance", "hard": False}, {"id": "s3_low_switching", "hard": False}]
    return {"id": f"CP-02-{i:02d}", "family": "CP", "template": "CP-02", "idx": i,
            "source_text": src, "question": q, "field_ids": [], "field_aliases": {},
            "units": {},
            "params": {"tickets": ["T1", "T2", "T3", "T4", "T5"],
                       "ticket_skills": {"T1": ["python"], "T2": ["python", "sql"],
                                         "T3": ["sql"], "T4": ["rust"], "T5": []},
                       "points": pts, "caps": caps,
                       "eng_skills": {"Ana": ["python", "sql"], "Ben": ["rust", "python"],
                                      "Chao": ["sql", "rust"]},
                       "t4_allowed": ["Ben", "Chao"], "early_pos": 1, "balance_gap": 2,
                       "max_tickets_pp": 2},
            "gold": {"constraints": cons}}

# ---------------------------------------------------------------- CP-03 -----
def _cp3_inst(i, ver, pricing):
    price_note = ("The changelog currently mentions pricing." if pricing else
                  "The current changelog draft does NOT mention pricing.")
    src = (f"{HDR}\nRelease checklist for {ver}: Cut the release branch only after all "
           f"merge-window PRs have landed. A migration dry-run against a staging snapshot must "
           f"precede tagging. Tag {ver} only if the dry-run is clean; otherwise fix forward and "
           f"retry the dry-run once (maximum one retry). Publish release notes after tagging. Do "
           f"NOT announce publicly before the support playbook is updated. Legal sign-off is "
           f"needed only if the changelog mentions pricing; {price_note}")
    q = ("Produce the plan artifact: an ordered list of steps (one step per line) that executes "
         "this checklist correctly, including any conditional handling.")
    cons = [{"id": "h1_branch_first", "hard": True}, {"id": "h2_dry_before_tag", "hard": True},
            {"id": "h3_retry_bound", "hard": True}, {"id": "h4_notes_after_tag", "hard": True},
            {"id": "h5_announce_after_playbook", "hard": True},
            {"id": "h6_legal_conditional", "hard": True}, {"id": "h7_tag_gate", "hard": True}]
    return {"id": f"CP-03-{i:02d}", "family": "CP", "template": "CP-03", "idx": i,
            "source_text": src, "question": q, "field_ids": [], "field_aliases": {},
            "units": {}, "params": {"pricing_in_changelog": pricing, "version": ver},
            "gold": {"constraints": cons}}

# ---------------------------------------------------------------- CP-04 -----
def _cp4_sat(n, labels, cons):
    others = [g for g in labels if g != cons.get("host")]
    for perm in itertools.permutations(labels[1:]):
        seq = (labels[0],) + perm          # host fixed at seat 1 handled by caller mapping
        pos = {g: i for i, g in enumerate(seq)}
        def adj(x, y): return (pos[x] - pos[y]) % n in (1, n - 1)
        a, b = cons["AB"]; c, d = cons["CD"]; e, f = cons["EF"]
        if adj(a, b) or adj(c, d) or not adj(e, f): continue
        return True
    return False

def _cp4_inst(i, n, host, cons, labels):
    guests = ", ".join(labels)
    soft_line = (f" SOFT: {cons['GH_soft'][0]} prefers not to sit beside "
                 f"{cons['GH_soft'][1]}.") if cons["GH_soft"] else ""
    src = (f"{HDR}\nSeat {n} dinner guests ({guests}) around a round table with {n} seats, seat 1 "
           f"through seat {n}; seats {n} and 1 are adjacent. The host, {host}, is fixed at seat 1. "
           f"HARD: {cons['AB'][0]} is not adjacent to {cons['AB'][1]}; {cons['CD'][0]} is not "
           f"adjacent to {cons['CD'][1]}; {cons['EF'][0]} must be adjacent to {cons['EF'][1]}."
           + soft_line)
    q = ("Produce the seating artifact: the guest order for seats 1..%d as one line, e.g. "
         "'seating: G, A, ...' (guest at seat 1 first)." % n)
    cons_l = [{"id": "h1_all_seated_once", "hard": True}, {"id": "h2_host_seat1", "hard": True},
              {"id": "h3_not_adj_AB", "hard": True}, {"id": "h4_not_adj_CD", "hard": True},
              {"id": "h5_adj_EF", "hard": True}]
    if cons["GH_soft"]:
        cons_l.append({"id": "s1_GH_pref", "hard": False})
    letters = sorted(labels)   # ALL n guests (constraint endpoints alone under-count n∉{6,8})
    return {"id": f"CP-04-{i:02d}", "family": "CP", "template": "CP-04", "idx": i,
            "source_text": src, "question": q, "field_ids": [], "field_aliases": {},
            "units": {}, "params": {"n_guests": n, "host": host, "guests": letters,
                                    "pairs": {"AB": cons["AB"], "CD": cons["CD"],
                                              "EF": cons["EF"], "GH": cons["GH_soft"]}},
            "gold": {"constraints": cons_l}}

# ---------------------------------------------------------------- CP-05 -----
def _sat_budget(P):
    T = P["total"]
    tr = P["training_pref"]
    infra = max(P["infra_floor"], T - tr - P["ev_tool_cap"] + P["headroom_min"])
    if infra > P["veto_cap"]: return False
    rest = T - infra - tr
    ev = P["ev_tool_cap"] - P["headroom_min"]; tl = rest - ev
    return 0 <= tl and ev + tl <= P["ev_tool_cap"] and max(infra, tr, ev, tl) <= P["veto_cap"]

def _cp5_inst(i, P):
    src = (f"{HDR}\nAllocate €{P['total']:,} across four budget lines: infra, tooling, training, "
           f"events. HARD constraints: infra ≥ €{P['infra_floor']:,}; training ≤ 25% of the total "
           f"(≤ €{P['training_cap']:,}); events + tooling combined ≤ €{P['ev_tool_cap']:,}; the "
           f"four lines must sum to exactly €{P['total']:,}; no single line may exceed "
           f"€{P['veto_cap']:,} (lead veto). SOFT preferences, ranked lexicographically: 1) "
           f"training ≥ €{P['training_pref']:,}; 2) leave at least €{P['headroom_min']:,} of "
           f"unused events+tooling headroom; 3) keep infra headroom small — infra ≤ "
           f"€{P['infra_floor'] + P['infra_headroom']:,}.")
    q = ("Produce the allocation artifact as JSON: exactly the four keys infra, tooling, "
         "training, events with euro amounts as numbers summing to the total.")
    cons = [{"id": "h1_sum_exact", "hard": True}, {"id": "h2_infra_floor", "hard": True},
            {"id": "h3_training_cap", "hard": True}, {"id": "h4_ev_tool_cap", "hard": True},
            {"id": "h5_veto", "hard": True}, {"id": "s1_training_pref", "hard": False},
            {"id": "s2_events_headroom", "hard": False}, {"id": "s3_infra_headroom", "hard": False}]
    return {"id": f"CP-05-{i:02d}", "family": "CP", "template": "CP-05", "idx": i,
            "source_text": src, "question": q, "field_ids": [], "field_aliases": {},
            "units": {}, "params": P, "gold": {"constraints": cons}}
