"""E1 frozen checkers + tolerant NL parser (declared per pre-reg §3).

One source of truth consumed by BOTH the item generator (W0c self-test:
checker(gold)=1.0 on every item) and the runner. No edits after first scored
call (pre-reg §8.5). All scoring fully programmatic — no LLM judges (§5).
"""
import json, re

# --------------------------------------------------------------- normalize --
UNK_TOKENS = {"unknown", "unk", "n/a", "na", "null", "none", "unspecified",
              "not specified", "not stated", "missing", "clarify", "?",
              "unassigned", "not assigned", "someone", "anyone", "anybody"}

def _s(v):
    if v is None: return ""
    if isinstance(v, bool): return "true" if v else "false"
    return str(v).strip()

def norm_txt(v):
    v = _s(v).lower().replace("_", " ")
    v = re.sub(r"[^a-z0-9.\-:/+ ]", " ", v)
    return re.sub(r"\s+", " ", v).strip()

def norm_date(v):
    v = _s(v)
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", v)
    if m:
        return "%s-%02d-%02d" % (m.group(1), int(m.group(2)), int(m.group(3)))
    m2 = re.search(r"(\d{4})[/.](\d{1,2})[/.](\d{1,2})", v)
    if m2:
        return "%s-%02d-%02d" % (m2.group(1), int(m2.group(2)), int(m2.group(3)))
    return None

def norm_time(v):
    v = _s(v).lower()
    m = re.search(r"(\d{1,2}):(\d{2})", v)
    if m: return "%02d:%02d" % (int(m.group(1)) % 24, int(m.group(2)))
    m = re.search(r"\b(\d{1,2})(\d{2})\s*(am|pm)?\b", v)
    if m and m.group(3):
        h = int(m.group(1)) % 12 + (12 if m.group(3) == "pm" else 0)
        return "%02d:%02d" % (h, int(m.group(2)))
    return None

def norm_num(v):
    v = _s(v).replace(",", "")
    m = re.search(r"-?\d+(?:\.\d+)?", v)
    return float(m.group(0)) if m else None

def is_unk(v):
    n = norm_txt(v)
    return (not n) or any(t == n or t in n for t in ("unknown", "unspecified", "not specified",
                                                     "not stated", "n/a", "missing"))

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january","february","march","april","may","june","july","august",
     "september","october","november","december"])}
for abbr, full in [("jan",1),("feb",2),("mar",3),("apr",4),("jun",6),("jul",7),
                   ("aug",8),("sep",9),(" sept",9),("oct",10),("nov",11),("dec",12)]:
    MONTHS[abbr.strip()] = full

# ------------------------------------------------------------ field match ---
def fields_match(fid, gold, ans, spec):
    """spec per field: {type: date|time|num|enum|txt|list|bool|money, tol?, tol_rel?,
    aliases?: [..], window?: [lo,hi] (dates), unk_ok?: bool}"""
    t = spec.get("type", "txt")
    ga, aa = _s(gold), _s(ans)
    if isinstance(gold, (int, float)) and not isinstance(gold, bool):
        na = norm_num(aa)
        if na is None: return False
        if spec.get("tol_rel"): return abs(na - float(gold)) <= spec["tol_rel"] * abs(float(gold))
        return abs(na - float(gold)) <= spec.get("tol", 0.5)
    if t == "num":
        ng, na = norm_num(ga), norm_num(aa)
        if ng is None or na is None: return False
        if spec.get("tol_rel"): return abs(na - ng) <= spec["tol_rel"] * abs(ng)
        return abs(na - ng) <= spec.get("tol", 0.5)
    if t == "bool":
        g = norm_txt(ga) in ("true", "yes", "1") if ga else bool(gold)
        a = norm_txt(aa) in ("true", "yes", "1")
        return g == a
    if t == "date":
        if spec.get("unk_gold"):
            return is_unk(aa)          # gold itself undetermined -> credit only an unknown-flag
        ng = norm_date(ga); na = norm_date(aa)
        if ng and na:
            if ng != na and spec.get("window"):
                lo, hi = spec["window"]
                return lo <= na <= hi
            return ng == na
        return is_unk(aa) and is_unk(ga)
    if t == "datetime":
        ng_d, na_d = norm_date(ga), norm_date(aa)
        ng_t, na_t = norm_time(ga), norm_time(aa)
        ok_d = (ng_d == na_d) if (ng_d and na_d) else (is_unk(aa) and is_unk(ga))
        ok_t = (ng_t == na_t) if (ng_t and na_t) else False
        return ok_d and ok_t
    if t == "list":
        gset = {norm_txt(x) for x in (gold if isinstance(gold, list) else re.split(r"[;,]", ga))}
        aset = {norm_txt(x) for x in (ans if isinstance(ans, list) else re.split(r"[;,]", aa))}
        gset.discard(""); aset.discard("")
        if not gset: return not aset or is_unk(aa)
        hit = sum(1 for g in gset if any(_alias_hit(g, a) for a in aset))
        return hit >= max(1, int(round(0.99 * len(gset))))   # all gold elements present
    if t == "money":
        ng, na = norm_num(ga), norm_num(aa)
        return ng is not None and na is not None and abs(na - ng) <= spec.get("tol", 0.5)
    # txt / enum
    if spec.get("unk_gold"):
        return is_unk(aa)
    g = norm_txt(ga); a = norm_txt(aa)
    if not g: return is_unk(aa) or not a
    for cand in [a] + [norm_txt(x) for x in spec.get("aliases", [])]:
        if cand and _alias_hit(g, cand): return True
    return False

def _alias_hit(g, a):
    if g == a: return True
    if len(g) > 3 and (g in a or a in g): return True
    gw, aw = set(g.split()), set(a.split())
    return bool(gw) and gw <= aw

# ------------------------------------------------- tolerant NL parser -------
FIELD_LINE = re.compile(r"^\s*[-*•]?\s*([A-Za-z0-9_ ]{2,40}?)\s*[:=\-]+\s*(.+?)\s*$")

def nl_parse(item, raw):
    """Frozen tolerant parser shared by both NL arms. Returns dict artifact."""
    fields = {}
    # try JSON blob first
    m = re.search(r"\{.*\}", raw, re.S)
    if m:
        try:
            obj = json.loads(m.group(0))
            if isinstance(obj, dict):
                flat = obj.get("fields", obj)
                if isinstance(flat, dict):
                    fields.update({norm_txt(k).replace(" ", "_"): v for k, v in flat.items()})
        except Exception:
            pass
    aliases = item.get("field_aliases", {})
    want = set(item.get("field_ids", []))
    for ln in raw.splitlines():
        mm = FIELD_LINE.match(ln)
        if not mm: continue
        key = norm_txt(mm.group(1)).replace(" ", "_")
        val = mm.group(2).strip()
        if key in want and key not in fields:
            fields[key] = val
        else:
            for fid, al in aliases.items():
                if fid not in fields and key in {norm_txt(x).replace(" ", "_") for x in al}:
                    fields[fid] = val
    return {"fields": fields}

# ------------------------------------------------------------- EX scorer ----
def ex_score(item, art):
    gold, specs = item["gold"]["fields"], item["gold"]["specs"]
    got = art.get("fields", {})
    matched = 0
    detail = {}
    for fid, spec in specs.items():
        ok = fields_match(fid, gold.get(fid), got.get(fid, ""), spec)
        detail[fid] = ok
        matched += bool(ok)
    return matched / len(specs), detail

# ------------------------------------------------------------- CP scorer ----
def _meetings(art):
    out = {}
    for e in art.get("schedule", []):
        name = norm_txt(e.get("meeting", ""))
        out[_match_key(name)] = {
            "room": norm_txt(e.get("room", "")),
            "start": norm_time(str(e.get("start", ""))),
            "end": norm_time(str(e.get("end", "")))}
    return out

def _mins(t):
    if not t: return None
    h, m = t.split(":")
    return int(h) * 60 + int(m)

def _match_key(name, aliases=None):
    for k, pat in MEET_KEYS.items():
        if pat in name: return k
    return name

MEET_KEYS = {"a": "sprint review", "b": "1:1", "c": "vendor", "d": "retro"}

def _overlap(s1, e1, s2, e2):
    return (s1 is not None and e1 is not None and s2 is not None and e2 is not None
            and s1 < e2 and s2 < e1)

def cp_eval_constraint(cid, inst, art):
    """Evaluate one constraint of item `inst` against artifact `art`."""
    P = inst["params"]
    if inst["template"] == "CP-01":
        M = _meetings(art)
        need = {"a", "b", "c", "d"}
        if cid == "h9_complete":
            return need <= set(M.keys())
        for k in need:
            if k not in M: return False
        rooms = {norm_txt(r["name"]): r for r in P["rooms"]}
        def R(k):
            rm = M[k]["room"]
            for nm, r in rooms.items():
                if nm in rm or rm in nm: return r
            return None
        if cid == "h1_dur_a":
            return abs((_mins(M["a"]["end"]) or 0) - (_mins(M["a"]["start"]) or 0) - P["dur_a"]) <= 15
        if cid == "h2_projector_a":
            r = R("a"); return bool(r and r.get("projector"))
        if cid == "h3_capacity":
            for k, pplkey in [("a", "ppl_a"), ("b", 2), ("c", "ppl_c"), ("d", "ppl_d")]:
                ppl = P["ppl_a"] if k == "a" else (P["ppl_c"] if k == "c" else P["ppl_d"])
                if k == "b": ppl = 2
                r = R(k)
                if not r or r["cap"] < ppl: return False
            return True
        if cid == "h4_lunch":
            return not any(_overlap(_mins(M[k]["start"]), _mins(M[k]["end"]), 720, 780) for k in need)
        if cid == "h5_org_buffer":
            sa, ea = _mins(M["a"]["start"]), _mins(M["a"]["end"])
            sb, eb = _mins(M["b"]["start"]), _mins(M["b"]["end"])
            # organizer attends both: b may not overlap a NOR intrude into a's 15-min prep buffer
            return (eb <= sa - P["buffer"]) or (sb >= ea)
        if cid == "h6_avail_b":
            sb, eb = _mins(M["b"]["start"]), _mins(M["b"]["end"])
            return not _overlap(sb, eb, P["blk_start"], P["blk_end"])
        if cid == "h7_precedence_d":
            return (_mins(M["d"]["start"]) or 0) >= (_mins(M["a"]["end"]) or 0)
        if cid == "h8_grid":
            for k in need:
                s, e = _mins(M[k]["start"]), _mins(M[k]["end"])
                if s is None or e is None or s < 540 or e > 1020 or s % 30 or e % 30 or e <= s:
                    return False
            return True
        if cid == "s1_quiet_c":
            r = R("c"); return bool(r and r.get("quiet"))
    if inst["template"] == "CP-02":
        A = {norm_txt(k).upper(): norm_txt(v).capitalize() for k, v in art.get("assign", {}).items()}
        order = [norm_txt(x).upper() for x in art.get("order", [])]
        if cid == "h2_coverage":
            return all(t in A for t in P["tickets"])
        for t in P["tickets"]:
            if t not in A: return False
        eng_sk = P["eng_skills"]
        if cid == "h1_skills":
            for t, who in A.items():
                sk = eng_sk.get(who)
                if sk is None: return False
                need = P["ticket_skills"][t]
                if not set(need) <= set(sk): return False
            return True
        if cid == "h5_t4_restriction":
            return A.get("T4") in P["t4_allowed"]
        if cid == "h3_caps":
            load = {}
            for t, who in A.items():
                load[who] = load.get(who, 0) + P["points"][t]
            return all(load[e] <= P["caps"][e] for e in P["caps"])
        if cid == "h4_t1_before_t3":
            return ("T1" in order and "T3" in order and order.index("T1") < order.index("T3"))
        if cid == "s1_t2_early":
            return "T2" in order and order.index("T2") <= P["early_pos"]
        if cid == "s2_balance":
            load = {}
            for t, who in A.items():
                load[who] = load.get(who, 0) + P["points"][t]
            ls = sorted(load.values())
            return (ls[-1] - ls[0]) <= P["balance_gap"]
        if cid == "s3_low_switching":
            cnt = {}
            for _, who in A.items():
                cnt[who] = cnt.get(who, 0) + 1
            return max(cnt.values()) <= P["max_tickets_pp"]
    if inst["template"] == "CP-03":
        steps = [norm_txt(s) for s in art.get("steps", [])]
        import re as _re
        def find(word):
            pat = _re.compile(r"\b" + word.replace(" ", r"\s+") + r"\b")
            for i, st in enumerate(steps):
                if pat.search(st): return i
            return None
        i_branch = find("branch")
        i_dry = find("dry run")
        if i_dry is None: i_dry = find("migration")
        def find_tag():
            for i, st in enumerate(steps):
                if _re.search(r"\btag\b|\btagging\b|tag\s+v?\d", st) and "staging" not in st:
                    return i
                if _re.search(r"\btag\b", st): return i
            return None
        i_tag = find_tag()
        i_notes = find("notes")
        i_play = find("playbook") if find("playbook") is not None else find("support")
        i_ann = find("announce")
        if i_ann is None: i_ann = find("public")
        i_legal = find("legal") if find("legal") is not None else find("sign off")
        n_dry = sum(1 for st in steps
                    if _re.search(r"dry[\s-]?run", st) or ("migration" in st and "dry" in st))
        if cid == "h1_branch_first":
            return i_branch is not None and all(i_branch <= i for i in
                                                [x for x in (i_dry, i_tag, i_notes, i_play, i_ann) if x is not None])
        if cid == "h2_dry_before_tag":
            return i_dry is not None and i_tag is not None and i_dry < i_tag
        if cid == "h3_retry_bound":
            return n_dry <= 2
        if cid == "h4_notes_after_tag":
            return i_notes is not None and i_tag is not None and i_notes > i_tag
        if cid == "h5_announce_after_playbook":
            return (i_ann is None) or (i_play is not None and i_ann > i_play)
        if cid == "h6_legal_conditional":
            if P["pricing_in_changelog"]:
                return i_legal is not None
            return True
        if cid == "h7_tag_gate":
            return i_tag is not None      # tagging happens iff dry-run clean; clean path assumed, retry already bounded
    if inst["template"] == "CP-04":
        seq = [norm_txt(x).upper() for x in art.get("seating", [])]
        n = P["n_guests"]
        PR = P["pairs"]
        (a1, a2), (c1, c2), (e1, e2) = PR["AB"], PR["CD"], PR["EF"]
        gh = PR.get("GH")
        if cid == "h1_all_seated_once":
            return len(seq) == n and len(set(seq)) == n and set(seq) == set(P["guests"])
        if cid == "h2_host_seat1":
            return len(seq) >= 1 and seq[0] == P["host"]
        def adj(i, j): return (i - j) % n in (1, n - 1)
        pos = {g: i for i, g in enumerate(seq)} if len(seq) == len(set(seq)) else {}
        if cid == "h3_not_adj_AB":
            return a1 in pos and a2 in pos and not adj(pos[a1], pos[a2])
        if cid == "h4_not_adj_CD":
            return c1 in pos and c2 in pos and not adj(pos[c1], pos[c2])
        if cid == "h5_adj_EF":
            return e1 in pos and e2 in pos and adj(pos[e1], pos[e2])
        if cid == "s1_GH_pref":
            return bool(gh) and gh[0] in pos and gh[1] in pos and not adj(pos[gh[0]], pos[gh[1]])
    if inst["template"] == "CP-05":
        a = {}
        for k in ("infra", "tooling", "training", "events"):
            v = art.get(k)
            a[k] = float(v) if isinstance(v, (int, float)) else norm_num(v)
        if any(v is None for v in a.values()): return False
        T = P["total"]
        if cid == "h1_sum_exact": return abs(sum(a.values()) - T) < 0.01
        if cid == "h2_infra_floor": return a["infra"] >= P["infra_floor"]
        if cid == "h3_training_cap": return a["training"] <= P["training_cap"]
        if cid == "h4_ev_tool_cap": return a["events"] + a["tooling"] <= P["ev_tool_cap"]
        if cid == "h5_veto": return max(a.values()) <= P["veto_cap"]
        if cid == "s1_training_pref": return a["training"] >= P["training_pref"]
        if cid == "s2_events_headroom": return P["ev_tool_cap"] - (a["events"] + a["tooling"]) >= P["headroom_min"]
        if cid == "s3_infra_headroom": return a["infra"] <= P["infra_floor"] + P["infra_headroom"]
    return False

def cp_score(item, art):
    tot = sat = hard_bad = 0
    detail = {}
    for c in item["gold"]["constraints"]:
        ok = cp_eval_constraint(c["id"], item, art)
        detail[c["id"]] = ok
        tot += 1; sat += bool(ok)
        if c["hard"] and not ok: hard_bad += 1
    return sat / tot, {"hard_violations": hard_bad, **detail}

# ------------------------------------------------------------- TU scorer ----
TOOL_RE = re.compile(r"([a-zA-Z_.]+)\((.*)\)\s*;?\s*$")

def parse_calls(raw):
    calls = []
    for m in re.finditer(r"([a-zA-Z_.]+)\s*\(([^()]*)\)", raw):
        tool = m.group(1)
        argstr = m.group(2)
        args = {}
        depth = 0; cur = ""; parts = []
        for ch in argstr:
            if ch == "[" : depth += 1
            if ch == "]": depth -= 1
            if ch == "," and depth == 0:
                parts.append(cur); cur = ""
            else: cur += ch
        if cur.strip(): parts.append(cur)
        for p in parts:
            if "=" in p:
                k, _, v = p.partition("=")
                args[norm_txt(k).replace(" ", "_")] = v.strip().strip("'\"")
        calls.append({"tool": tool, "args": args})
    return calls

REFUND_HALLUC = re.compile(r"(refund|reimburse)", re.I)
UNAVAIL_WORDS = re.compile(r"(unavailable|not supported|does not support|no capability|"
                           r"cannot issue|can't issue|cannot process|can't process|"
                           r"no such (tool|capability|function)|unable to (issue|refund)|"
                           r"capability gap|not available)", re.I)

def _arg(args, *keys):
    for k in keys:
        for ak, av in args.items():
            if k in ak: return av
    return ""

def tu_score(item, art):
    """Returns (score∈{0,1}, detail). TU items are pass/fail per registered rules."""
    g = item["gold"]; tpl = item["template"]
    raw = art.get("_raw", "")
    calls = art.get("calls") or parse_calls(raw)
    tools = [c["tool"].lower() for c in calls]
    det = {"n_calls": len(calls)}
    if tpl == "TU-03":
        clar = art.get("clarify")
        missing = " ".join(map(str, (clar or {}).get("missing", []))) if isinstance(clar, dict) else ""
        blob = raw.lower() + " " + missing.lower()
        asked = bool(clar) or re.search(r"\bclarif|\bneed.{0,20}(address|recipient)|"
                                       r"which (email|address)|who.*(board|recipient)", blob)
        recip = re.search(r"(address|recipient|email|where|whom|which board)", blob)
        cont = re.search(r"(content|numbers|data|document|attach|what (should|to) send|source)", blob)
        ok = bool(asked and recip and cont)
        return (1.0 if ok else 0.0), {**det, "asked": bool(asked), "recip": bool(recip), "content": bool(cont)}
    if tpl == "TU-04":
        cancels = [c for c in calls if "cancel" in c["tool"]]
        oid = str(item["params"]["order_id"]).lstrip("#")
        good_cancel = any(norm_txt(_arg(c["args"], "order")).lstrip("#") == norm_txt(oid) for c in cancels)
        hall = [c for c in calls if REFUND_HALLUC.search(c["tool"])]
        sig = bool(art.get("unavailable")) or bool(UNAVAIL_WORDS.search(raw))
        ok = good_cancel and sig and not hall
        return (1.0 if ok else 0.0), {**det, "cancel_ok": good_cancel, "gap_signal": sig,
                                      "hallucination": bool(hall)}
    if tpl == "TU-01":
        books = [c for c in calls if "calendar.book" in c["tool"] or c["tool"].endswith("book")]
        if not books: return 0.0, {**det, "why": "no book call"}
        c = books[0]
        P = item["params"]
        ok_room = norm_txt(P["room"]) in norm_txt(_arg(c["args"], "room"))
        d = norm_date(_arg(c["args"], "date")); ok_date = (d == P["date_iso"])
        sm = norm_num(_arg(c["args"], "start")) or _mins(norm_time(_arg(c["args"], "start")))
        em = norm_num(_arg(c["args"], "end")) or _mins(norm_time(_arg(c["args"], "end")))
        ok_s = sm == P["start_min"]; ok_e = em == P["end_min"]
        ok_n = (norm_num(_arg(c["args"], "attendee")) or -1) == P["attendees"]
        pj = norm_txt(_arg(c["args"], "projector"))
        ok_p = (pj in ("true", "yes", "1")) == P["projector"]
        ok = all([ok_room, ok_date, ok_s, ok_e, ok_n, ok_p]) and len(books) == 1
        return (1.0 if ok else 0.0), {**det, "room": ok_room, "date": ok_date, "start": ok_s,
                                      "end": ok_e, "count": ok_n, "proj": ok_p}
    if tpl == "TU-02":
        creates = [i for i, c in enumerate(calls) if "tracker.create" in c["tool"]]
        mails = [i for i, c in enumerate(calls) if "mail.send" in c["tool"] or "send" in c["tool"]]
        if not creates or not mails: return 0.0, {**det, "why": "missing call"}
        ok_order = creates[0] < mails[0]
        c = calls[creates[0]]; P = item["params"]
        ok_sev = norm_txt(_arg(c["args"], "severity")).upper() == P["severity"]
        ok_title = norm_txt(P["title"])[:12] in norm_txt(_arg(c["args"], "title"))
        ok_comp = norm_txt(P["component"]) in norm_txt(_arg(c["args"], "component"))
        ok_asg = norm_txt(P["assignee"]) in norm_txt(_arg(c["args"], "assignee"))
        ok_due = norm_date(_arg(c["args"], "due")) == P["due_iso"]
        m = calls[mails[0]]
        blob = " ".join(str(v) for v in m["args"].values()).lower()
        ok_ref = ("ticket" in blob) or bool(re.search(r"[a-z]+-?\d{2,}", blob))
        ok_prio = norm_txt(_arg(m["args"], "priority")) == "high"
        ok_to = norm_txt(P["recipient"]) in norm_txt(_arg(m["args"], "to"))
        ok = all([ok_order, ok_sev, ok_title, ok_comp, ok_asg, ok_due, ok_ref, ok_prio, ok_to])
        return (1.0 if ok else 0.0), {**det, "order": ok_order, "sev": ok_sev, "title": ok_title,
                                      "comp": ok_comp, "asg": ok_asg, "due": ok_due,
                                      "ref": ok_ref, "prio": ok_prio, "to": ok_to}
    if tpl == "TU-05":
        looks = [i for i, c in enumerate(calls) if "lookup" in c["tool"]]
        cans = [i for i, c in enumerate(calls) if "cancel" in c["tool"]]
        if not looks or not cans: return 0.0, {**det, "why": "missing call"}
        ok_order = looks[0] < cans[0]
        l = calls[looks[0]]; P = item["params"]
        ok_mail = norm_txt(P["email"]) in norm_txt(_arg(l["args"], "customer", "email"))
        ok_st = norm_txt(P["status"]) in norm_txt(_arg(l["args"], "status"))
        pa = norm_date(_arg(l["args"], "placed", "after"))
        ok_pa = (pa == P["placed_after"]) or norm_txt(str(P["placed_after"])) in norm_txt(_arg(l["args"], "placed"))
        ok = ok_order and ok_mail and ok_st and ok_pa
        return (1.0 if ok else 0.0), {**det, "order": ok_order, "email": ok_mail,
                                      "status": ok_st, "after": ok_pa}
    return 0.0, {**det, "why": "unknown template"}

# ------------------------------------------------------- dispatch + parse ---
def parse_answer(item, arm, raw):
    """arm->artifact. Machine arms strict-parse; NL arms via frozen tolerant parser."""
    fam = item["family"]
    if arm in ("JSON", "CSIR-SIR"):
        m = re.search(r"\{.*\}", raw, re.S)
        if not m: raise ValueError("no JSON object found")
        obj = json.loads(m.group(0))
        return machine_shape(fam, obj, raw)
    if fam == "EX":
        return nl_parse(item, raw)
    art = {"_raw": raw}
    if fam == "CP":
        art.update(nl_parse_cp(raw))
    elif fam == "TU":
        # DEV-6 pre-scored-call repair: the shared item question itself requests the
        # JSON {"calls":[...]} contract, so the tolerant NL parser honors that first
        # and falls back to freeform call-lines. Machine arms remain strict-parse.
        m = re.search(r"\{.*\}", raw, re.S)
        if m:
            try:
                obj = json.loads(m.group(0))
                if isinstance(obj, dict) and "calls" in obj:
                    return machine_shape(fam, obj, raw)
            except Exception:
                pass
        art["_raw"] = raw
    return art

def machine_shape(fam, obj, raw):
    if fam == "EX":
        return {"fields": obj.get("fields", obj if isinstance(obj, dict) else {})}
    if fam == "CP":
        art = {}
        if "schedule" in obj: art["schedule"] = obj["schedule"]
        if "assign" in obj: art["assign"] = obj["assign"]
        if "order" in obj: art["order"] = obj["order"]
        if "steps" in obj: art["steps"] = obj["steps"]
        if "seating" in obj: art["seating"] = obj["seating"]
        if all(k in obj for k in ("infra", "tooling", "training", "events")): art.update(obj)
        return art
    if fam == "TU":
        art = {"calls": obj.get("calls", []),
               "_raw": raw}
        if "clarify" in obj: art["clarify"] = obj["clarify"]
        if "unavailable" in obj: art["unavailable"] = obj["unavailable"]
        return art
    return obj

def nl_parse_cp(raw):
    art = {}
    sched = []
    for ln in raw.splitlines():
        m = re.search(r"(sprint review|retro|incident retro|vendor|1:1|one-on-one).*?"
                      r"(atlas|borel|cyrus).*?(\d{1,2}:\d{2}).*?(\d{1,2}:\d{2})", ln, re.I)
        if m:
            sched.append({"meeting": m.group(1), "room": m.group(2),
                          "start": norm_time(m.group(3)), "end": norm_time(m.group(4))})
    if sched: art["schedule"] = sched
    asg = {}
    for m in re.finditer(r"\b(T[1-5])\s*(?:->|:|=|to)\s*(Ana|Ben|Chao)\b", raw, re.I):
        asg[m.group(1).upper()] = m.group(2).capitalize()
    if asg: art["assign"] = asg
    om = re.search(r"(?:order|sequence)\s*[:=]\s*(.+)", raw, re.I)
    if om:
        art["order"] = re.findall(r"T[1-5]", om.group(1).upper())
    seats = re.findall(r"\b(?:seat\s*\d+\s*[:=\-]\s*)?([A-H])\b(?=[,\s)]|$)", raw)
    if "seating" not in art and len(seats) >= 5:
        art["seating"] = seats
    bud = {}
    for k in ("infra", "tooling", "training", "events"):
        m = re.search(rf"{k}\W{{0,5}}(?:€|\$)?\s*([\d.,]+)", raw, re.I)
        if m: bud[k] = norm_num(m.group(1))
    if len(bud) == 4: art.update(bud)
    steps = []
    for ln in raw.splitlines():
        s = ln.strip()
        if re.match(r"^\d+[.)]", s) or re.match(r"^[-*•]", s):
            steps.append(re.sub(r"^[\d.)\-*•\s]+", "", s))
    if steps: art["steps"] = steps
    return art

def score_item(item, arm, art):
    fam = item["family"]
    if fam == "EX": return ex_score(item, art)
    if fam == "CP": return cp_score(item, art)
    return tu_score(item, art)
