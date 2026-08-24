"""E1 Family EX item builder (pre-reg §2.1). Template idx 0 = verbatim pre-reg instance."""
import datetime as _dt
from checkers import norm_txt

ANCHOR = _dt.date(2026, 8, 24)   # fixed header date, all items (§2)
HDR = "Today is 2026-08-24 (Monday)."

NAMES20 = ["Priya", "Sam", "Marta", "Dana", "Marco", "Jelena", "Tomas", "Aiko", "Ravi", "Lena",
           "Omar", "Ingrid", "Chen", "Fatima", "Diego", "Sanne", "Kwame", "Mira", "Paulo", "Hana"]
SERVICES12 = ["checkout-service", "auth-service", "search-api", "billing-worker", "cart-service",
              "inventory-sync", "profile-api", "media-proxy", "webhook-relay", "notify-hub",
              "ledger-api", "session-store"]
COMPANIES8 = ["Nordika GmbH", "Acme Logistics", "Brightpath Media", "Helios Energy",
              "Quill & Co", "Vantor Systems", "Bluepine Retail", "Osaka Freight"]
WEEKDAYS = {"Thursday": 4, "Tuesday": 2, "Wednesday": 3, "Friday": 5}

EX01_FIELDS = ["a1_owner", "a1_action", "a1_deadline", "a1_priority",
               "a2_owner", "a2_action", "a2_constraint",
               "a3_owner", "a3_action", "a3_deadline", "a3_priority",
               "guard_target", "guard_condition", "guard_type"]
EX02_FIELDS = ["incident_id", "service", "symptom", "t_open", "blast_region", "blast_share",
               "rollback_deploy_id", "rollback_time", "suspected_cause", "status_page_time",
               "enterprise_email_required", "exception_company", "exception_notify"]
EX03_FIELDS = ["rent_due_day", "fee_amount_usd", "fee_trigger_days", "prohibition_paint",
               "prohibition_sublet", "pet_weight_limit_kg", "consent_escape",
               "notice_hours", "notice_exception"]
EX04_FIELDS = ["ship_date", "pickup_start", "pickup_end", "cargo1_name", "cargo1_qty",
               "cargo1_unit", "cargo1_weight_each_kg", "cargo2_name", "cargo2_qty",
               "cargo2_unit", "cargo2_weight_total_kg", "handling_exclusion",
               "docs_deadline_date", "roll_to_date", "docs_filed_date", "condition_triggered"]
EX05_FIELDS = ["category", "version", "symptom_condition", "tier", "seats",
               "deadline_day", "deadline_month", "mitigations_tried", "priority", "exec_visible"]

UNITS_EX = {  # W0b content-unit annotation: fid -> unit type (from §2.1 headers)
    **{f: "entity_ref" for f in ["a1_owner", "a2_owner", "a3_owner", "service",
                                 "incident_id", "exception_company", "cargo1_name", "cargo2_name"]},
    **{f: "temporal_qualifier" for f in ["a1_deadline", "a3_deadline", "t_open", "rollback_time",
                                         "status_page_time", "ship_date", "pickup_start",
                                         "pickup_end", "docs_deadline_date", "roll_to_date",
                                         "docs_filed_date", "notice_hours", "fee_trigger_days"]},
    **{f: "quantity_unit" for f in ["blast_share", "fee_amount_usd", "pet_weight_limit_kg",
                                    "cargo1_qty", "cargo1_weight_each_kg", "cargo2_qty",
                                    "cargo2_weight_total_kg", "seats", "rent_due_day"]},
    **{f: "exclusion" for f in ["a2_constraint", "handling_exclusion", "prohibition_paint",
                                "prohibition_sublet"]},
    **{f: "modality" for f in ["consent_escape", "notice_exception", "condition_triggered"]},
    **{f: "priority_preference" for f in ["a1_priority", "a3_priority", "priority", "exec_visible"]},
    "guard_target": "entity_ref", "guard_condition": "conditional_constraint",
    "guard_type": "modality", "symptom": "entity_ref", "rollback_deploy_id": "entity_ref",
    "suspected_cause": "entity_ref", "enterprise_email_required": "exclusion",
    "exception_notify": "exception_of_exclusion", "category": "entity_ref",
    "version": "entity_ref", "symptom_condition": "conditional_constraint",
    "tier": "entity_ref", "deadline_day": "designed_unknown_flag",
    "deadline_month": "designed_unknown_flag", "mitigations_tried": "entity_ref",
}

def _ordinal(n):
    return {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}[n]

def build_ex(rng):
    items = []
    # ---------------- EX-01 meeting actions ----------------
    for i in range(10):
        if i == 0:
            o1, o2, task1, task2 = "Priya", "Sam", "rerun the load-test", "migration plan"
            wd = "Thursday"
        else:
            o1, o2 = rng.sample(NAMES20, 2)
            task1 = rng.choice(["rerun the load-test", "refresh the dashboards",
                                "replay the failed jobs", "rerun the perf suite"])
            task2 = rng.choice(["migration plan", "rollback plan", "capacity plan", "comms plan"])
            wd = rng.choice(list(WEEKDAYS))
        dl = ANCHOR + _dt.timedelta(days=(WEEKDAYS[wd] - 1) % 7)
        win_hi = ANCHOR + _dt.timedelta(days=7)
        src = (f"{HDR}\nMarta: the beta launch slipped again. {o1}, you own the {task1} before "
               f"{wd}. Someone must tell the client — but do NOT promise a date in that note. "
               f"{o2} drafts the {task2} next week, low urgency. Nobody touches the staging "
               f"cluster until {o1}'s tests pass.")
        gold_fields = {"a1_owner": o1, "a1_action": task1, "a1_deadline": dl.isoformat(),
                       "a1_priority": None, "a2_owner": None, "a2_action": "tell the client",
                       "a2_constraint": "no date promise", "a3_owner": o2,
                       "a3_action": f"draft the {task2}", "a3_deadline": win_hi.isoformat(),
                       "a3_priority": "low", "guard_target": "staging cluster",
                       "guard_condition": f"{o1} tests pass", "guard_type": "negated modification"}
        specs = {"a1_owner": {"type": "txt"}, "a1_action": {"type": "txt"},
                 "a1_deadline": {"type": "date"}, "a1_priority": {"type": "txt", "unk_gold": True},
                 "a2_owner": {"type": "txt"}, "a2_action": {"type": "txt"},
                 "a2_constraint": {"type": "txt"},
                 "a3_owner": {"type": "txt"}, "a3_action": {"type": "txt"},
                 "a3_deadline": {"type": "date", "window": [str(ANCHOR), str(win_hi)]},
                 "a3_priority": {"type": "txt"}, "guard_target": {"type": "txt"},
                 "guard_condition": {"type": "txt"}, "guard_type": {"type": "txt"}}
        items.append(_mk("EX", "EX-01", i, src, gold_fields, specs))
    # ---------------- EX-02 incident report ----------------
    symptoms = ["returning 502s", "throwing 500s", "timing out", "dropping connections"]
    causes = ["uncached config reload in gateway v2.4.1", "connection-pool exhaustion after deploy",
              "cache stampede on session lookup", "retry storm from a misconfigured client",
              "disk latency on the log volume"]
    for i in range(10):
        svc = SERVICES12[0] if i == 0 else rng.choice(SERVICES12)
        sym = symptoms[0] if i == 0 else rng.choice(symptoms)
        share = 8 if i == 0 else rng.randint(2, 15)
        comp = COMPANIES8[0] if i == 0 else rng.choice(COMPANIES8)
        d_open = _dt.date(2026, 8, 14) if i == 0 else rng.choice(
            [_dt.date(2026, 8, d) for d in (11, 12, 13, 14, 15, 17, 18)])
        if i == 0:
            h0, m0 = 9, 12
        else:
            h0, m0 = rng.randint(7, 16), rng.choice([5, 12, 21, 33, 40])
        t_open = _dt.datetime.combine(d_open, _dt.time(h0, m0))
        t_det = t_open + _dt.timedelta(minutes=rng.randint(-17, -5))
        t_rb = t_open + _dt.timedelta(minutes=rng.randint(15, 25))
        t_ok = t_rb + _dt.timedelta(minutes=9 if i == 0 else rng.randint(5, 15))
        dep_d = d_open - _dt.timedelta(days=1)
        dep_k = 7 if i == 0 else rng.randint(1, 12)
        src = (f"{HDR}\nPagerDuty #{4412 if i == 0 else 4000 + rng.randint(1, 999)} opened "
               f"{t_open:%Y-%m-%d %H:%M} UTC: {svc} {sym} for ~{share}% of EU traffic since "
               f"{t_det:%H:%M} UTC. On-call J. Okafor rolled back deploy {dep_d:%Y-%m-%d}.{dep_k} "
               f"at {t_rb:%H:%M} UTC; error rate at baseline by {t_ok:%H:%M} UTC. Suspected cause: "
               f"{causes[0] if i == 0 else rng.choice(causes)}. Status page updated "
               f"{t_det:%H:%M} UTC. No enterprise email required per runbook §4 — except the "
               f"account manager for {comp} must be notified directly.")
        pid = re_search_id(src)
        gold_fields = {"incident_id": pid, "service": svc, "symptom": sym,
                       "t_open": f"{t_open:%Y-%m-%d %H:%M} UTC", "blast_region": "EU",
                       "blast_share": share / 100.0, "rollback_deploy_id":
                           f"{dep_d:%Y-%m-%d}.{dep_k}",
                       "rollback_time": f"{t_rb:%Y-%m-%d %H:%M} UTC",
                       "suspected_cause": causes[0] if i == 0 else _cause_in(src, causes),
                       "status_page_time": f"{t_det:%Y-%m-%d %H:%M} UTC",
                       "enterprise_email_required": False, "exception_company": comp,
                       "exception_notify": True}
        specs = {"incident_id": {"type": "txt"}, "service": {"type": "txt"},
                 "symptom": {"type": "txt"}, "t_open": {"type": "datetime"},
                 "blast_region": {"type": "enum"}, "blast_share": {"tol_rel": 0.25},
                 "rollback_deploy_id": {"type": "txt"}, "rollback_time": {"type": "datetime"},
                 "suspected_cause": {"type": "txt"},
                 "status_page_time": {"type": "datetime"},
                 "enterprise_email_required": {"type": "bool"},
                 "exception_company": {"type": "txt"}, "exception_notify": {"type": "bool"}}
        items.append(_mk("EX", "EX-02", i, src, gold_fields, specs))
    # ---------------- EX-03 lease clause ----------------
    for i in range(10):
        fee, grace = (45, 5) if i == 0 else (rng.randrange(20, 205, 5), rng.randint(3, 7))
        wkg = 20 if i == 0 else rng.randrange(15, 45, 5)
        hrs = 24 if i == 0 else rng.choice([12, 24, 48])
        day = 1 if i == 0 else rng.randint(1, 5)
        src = (f"{HDR}\nTenant shall remit rent on the {_ordinal(day)} day of each month. Late "
               f"payments incur a ${fee} fee after a {grace}-day grace period. Tenant may not "
               f"paint, sublet, or keep pets exceeding {wkg} kg without written consent. Landlord "
               f"must give {hrs} hours' notice before entry, except in emergencies.")
        gold_fields = {"rent_due_day": day, "fee_amount_usd": fee, "fee_trigger_days": grace,
                       "prohibition_paint": True, "prohibition_sublet": True,
                       "pet_weight_limit_kg": wkg, "consent_escape": True,
                       "notice_hours": hrs, "notice_exception": "emergencies"}
        specs = {"rent_due_day": {}, "fee_amount_usd": {}, "fee_trigger_days": {},
                 "prohibition_paint": {"type": "bool"}, "prohibition_sublet": {"type": "bool"},
                 "pet_weight_limit_kg": {}, "consent_escape": {"type": "bool"},
                 "notice_hours": {}, "notice_exception": {"type": "txt"}}
        items.append(_mk("EX", "EX-03", i, src, gold_fields, specs))
    # ---------------- EX-04 shipment consolidation ----------------
    crate_goods = ["tile", "lumber", "marble slabs", "steel fittings", "cladding panels"]
    pallet_goods = ["grout", "sand", "adhesive", "sealant", "packaging stock"]
    for i in range(10):
        order_no = 8841 if i == 0 else 8000 + rng.randint(100, 899)
        ship = ANCHOR
        n_cr = 12 if i == 0 else rng.randint(6, 20)
        w_ea = 240 if i == 0 else rng.randrange(60, 800, 20)
        w_pl = 380 if i == 0 else rng.randrange(200, 800, 20)
        g1 = crate_goods[0] if i == 0 else rng.choice(crate_goods)
        g2 = pallet_goods[0] if i == 0 else rng.choice(pallet_goods)
        ws, we = "10:00", "12:00"
        ddl = _dt.date(2026, 8, 21)
        roll = _dt.date(2026, 8, 31)
        filed = _dt.date(2026, 8, 19)
        src = (f"{HDR}\n(1) Dana, warehouse: \"Order #{order_no} ships Monday 2026-08-24. "
               f"Contents: {n_cr} crates of {g1} at {w_ea} kg each, one pallet of {g2}, "
               f"{w_pl} kg. Do not stack pallets.\" (2) Marco, freight: \"Carrier pickup window "
               f"{ws}–{we} local. If customs docs are not filed by Friday 2026-08-21 17:00 UTC, "
               f"roll the shipment to Monday 2026-08-31.\" (3) Dana: \"Customs invoice filed "
               f"{filed:%Y-%m-%d}.\"")
        gold_fields = {"ship_date": ship.isoformat(), "pickup_start": ws, "pickup_end": we,
                       "cargo1_name": g1, "cargo1_qty": n_cr, "cargo1_unit": "crates",
                       "cargo1_weight_each_kg": w_ea, "cargo2_name": g2, "cargo2_qty": 1,
                       "cargo2_unit": "pallet", "cargo2_weight_total_kg": w_pl,
                       "handling_exclusion": "no pallet stacking",
                       "docs_deadline_date": ddl.isoformat(), "roll_to_date": roll.isoformat(),
                       "docs_filed_date": filed.isoformat(), "condition_triggered": False}
        specs = {"ship_date": {"type": "date"}, "pickup_start": {"type": "time"},
                 "pickup_end": {"type": "time"}, "cargo1_name": {"type": "txt"},
                 "cargo1_qty": {}, "cargo1_unit": {"type": "enum"}, "cargo1_weight_each_kg": {},
                 "cargo2_name": {"type": "txt"}, "cargo2_qty": {},
                 "cargo2_unit": {"type": "enum"}, "cargo2_weight_total_kg": {},
                 "handling_exclusion": {"type": "txt"}, "docs_deadline_date": {"type": "date"},
                 "roll_to_date": {"type": "date"}, "docs_filed_date": {"type": "date"},
                 "condition_triggered": {"type": "bool"}}
        items.append(_mk("EX", "EX-04", i, src, gold_fields, specs))
    # ---------------- EX-05 ticket triage ----------------
    feats = [("export invoices", "export-bug"), ("generate reports", "reporting-bug"),
             ("sync contacts", "sync-bug"), ("import orders", "import-bug"),
             ("render statements", "statement-bug")]
    mit_sets = [["clearing cache", "switching from Safari to Chrome"],
                ["restarting the app"], ["clearing cache", "trying incognito mode"],
                ["updating drivers", "switching browsers"]]
    for i in range(10):
        feat, cat = feats[0] if i == 0 else feats[rng.randrange(len(feats))]
        ver = "3.2.1" if i == 0 else f"v{rng.randint(2,4)}.{rng.randint(0,9)}.{rng.randint(0,9)}"
        pages = 50 if i == 0 else rng.randrange(30, 85, 5)
        seats = 200 if i == 0 else rng.choice([100, 150, 250, 300, 400])
        dom = 28 if i == 0 else rng.randint(20, 28)
        mits = mit_sets[0] if i == 0 else rng.choice(mit_sets)
        mit_txt = ", ".join(mits[:-1]) + (" and " + mits[-1] if len(mits) > 1 else "")
        src = (f"{HDR}\nSubject: Cannot {feat}. Since upgrading to {ver} last week, the feature "
               f"spins forever on records over ~{pages} pages. Enterprise plan, ~{seats} seats. "
               f"This blocks our month-end close, due on the {dom}th. Tried {mit_txt}. Please "
               f"treat as urgent — our CEO is asking.")
        gold_fields = {"category": cat, "version": ver.lstrip("v"),
                       "symptom_condition": f"pages > {pages}", "tier": "Enterprise",
                       "seats": seats, "deadline_day": dom, "deadline_month": None,
                       "mitigations_tried": [norm_txt(m) for m in mits],
                       "priority": "urgent", "exec_visible": True}
        specs = {"category": {"type": "txt"}, "version": {"type": "txt"},
                 "symptom_condition": {"type": "txt"}, "tier": {"type": "txt"},
                 "seats": {"tol_rel": 0.25}, "deadline_day": {},
                 "deadline_month": {"unk_gold": True},
                 "mitigations_tried": {"type": "list"}, "priority": {"type": "txt"},
                 "exec_visible": {"type": "bool"}}
        items.append(_mk("EX", "EX-05", i, src, gold_fields, specs))
    return items

def re_search_id(src):
    m = _ID_RE.search(src)
    return m.group(1) if m else ""

def _cause_in(src, causes):
    for c in causes:
        if c.split()[0] in src:
            return c
    return causes[0]

import re as _re
_ID_RE = _re.compile(r"PagerDuty #(\d+)")

def _mk(fam, tpl, idx, src, gold_fields, specs):
    ids = list(gold_fields.keys())
    q = ("Produce the extraction answer artifact for the source above. Emit exactly these field "
         "ids, one per line as 'field_id: value' (lists comma-separated; use UNKNOWN where the "
         "source does not determine a value): " + ", ".join(ids) + ".")
    return {"id": f"{tpl}-{idx:02d}", "family": fam, "template": tpl, "idx": idx,
            "source_text": src, "question": q, "field_ids": ids,
            "field_aliases": {}, "units": {f: UNITS_EX.get(f, "entity_ref") for f in ids},
            "gold": {"fields": gold_fields, "specs": specs},
            "params": {}}
