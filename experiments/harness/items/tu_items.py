"""E1 Family TU item builder (pre-reg §2.3). Template idx 0 = verbatim instance.
Anchor date fixed 2026-08-24 for all items."""
import datetime as _dt
from ex_items import HDR

EMAILS8 = ["gunnar@example.com", "petra@example.com", "oskar@example.com",
           "lina@example.com", "mateo@example.com", "yuki@example.com",
           "zara@example.com", "finn@example.com"]
TITLES6 = ["nightly export failing", "billing sync lagging", "search indexer crash",
           "webhook retries exhausted", "queue backlog growing", "cache eviction storm"]
COMPS4 = ["pipelines", "billing", "search", "gateway"]
PEOPLE6 = ["priya", "sam", "dana", "marco", "ingrid", "omar"]
ROOMS3 = ["Atlas", "Borel", "Cyrus"]

def build_tu(rng):
    items = []
    # ---------------- TU-01 control single call ----------------
    starts = [(14 * 60, "14:00"), (10 * 60 + 30, "10:30"), (15 * 60, "15:00"),
              (9 * 60 + 30, "09:30"), (16 * 60, "16:00"), (11 * 60, "11:00"),
              (13 * 60 + 30, "13:30")]
    day_words = {"tomorrow": "2026-08-25", "today": "2026-08-24"}
    for i in range(10):
        room = ROOMS3[0] if i == 0 else rng.choice(ROOMS3)
        sm, stxt = starts[0] if i == 0 else rng.choice(starts)
        em = sm + 60
        etxt = _plus60(stxt)
        n = 8 if i == 0 else rng.randint(4, 12)
        proj = True if i == 0 else rng.random() < 0.5
        dw = "tomorrow" if i == 0 else rng.choice(list(day_words))
        date_iso = day_words[dw]
        src = (f"{HDR}\nBook the {room} room {dw} {stxt}–{etxt_fmt(stxt)} for {n} people"
               + ("; projector needed." if proj else "."))
        q = ("Emit the ordered tool-call list for the request above as JSON "
             '{"calls":[{"tool":...,"args":{...}}]}. Times as minutes since midnight; dates ISO.')
        gold_calls = [{"tool": "calendar.book",
                       "args": {"room_id": room.lower(), "date": date_iso, "start_min": sm,
                                "end_min": em, "attendee_count": n,
                                "needs_projector": proj}}]
        items.append(_mk("TU-01", i, src, q, {"expect": "actions", "calls": gold_calls},
                         {"room": room.lower(), "date_iso": date_iso, "start_min": sm,
                          "end_min": em, "attendees": n, "projector": proj}))
    # ---------------- TU-02 sequenced pair ----------------
    sevs = ["S2", "S1", "S3"]
    duedays = {"Friday": "2026-08-28", "Wednesday": "2026-08-26"}
    for i in range(10):
        sev = "S2" if i == 0 else rng.choice(sevs)
        title = TITLES6[0] if i == 0 else rng.choice(TITLES6)
        comp = COMPS4[0] if i == 0 else rng.choice(COMPS4)
        who = PEOPLE6[0] if i == 0 else rng.choice(PEOPLE6)
        recip = "ops@corp.example" if i == 0 else rng.choice(
            ["ops@corp.example", "sre@corp.example", "support@corp.example"])
        dw, due = ("Friday", "2026-08-28") if i == 0 else rng.choice(list(duedays.items()))
        subj = f"{title} {sev}"
        src = (f"{HDR}\nFile an {sev} tracker ticket titled '{title}', component {comp}, assignee "
               f"{who}, due {dw}. Then email {recip} about it — subject '{subj}', reference the "
               f"ticket id in the body, high priority.")
        q = ("Emit the ordered tool-call list for the request above as JSON "
             '{"calls":[{"tool":...,"args":{...}}]}. Dates ISO; ordering matters.')
        gold_calls = [{"tool": "tracker.create",
                       "args": {"title": title, "severity": sev, "component": comp,
                                "assignee": who, "due_date": due}},
                      {"tool": "mail.send",
                       "args": {"to": [recip], "subject": subj, "priority": "high",
                               "body": f"Tracker ticket {sev} '{title}' filed in {comp}; "
                                       f"assigned to {who}, due {due}. See tracker for the ticket id."}}]
        items.append(_mk("TU-02", i, src, q,
                         {"expect": "ordered_actions", "calls": gold_calls},
                         {"severity": sev, "title": title, "component": comp,
                          "assignee": who, "recipient": recip, "due_iso": due}))
    # ---------------- TU-03 underspecified -> clarify ----------------
    asks = [("send the quarterly numbers to the board",
             "quarterly numbers", "board"),
            ("share the roadmap deck with the investors",
             "roadmap deck", "investors"),
            ("post the churn metrics to the partners committee",
             "churn metrics", "partners committee"),
            ("email the new pricing sheet to the customer advisory board",
             "pricing sheet", "customer advisory board")]
    for i in range(10):
        req, what, aud = asks[0] if i == 0 else asks[i % len(asks)]
        verb = rng.choice(["Send", "Forward", "Share", "Email"]) if i else "Send"
        src = f"{HDR}\n{verb} the {what} to the {aud}."
        q = ('Emit the ordered tool-call list for the request above as JSON '
             '{"calls":[...]}; if information needed for a call is missing use '
             '{"clarify":{"missing":[...],"question":"..."}} instead; if a capability does not '
             'exist use {"unavailable":[...]}.')
        items.append(_mk("TU-03", i, src, q,
                         {"expect": "clarify",
                          "missing_required": ["recipient address", "content source"]},
                         {"what": what, "audience": aud}))
    # ---------------- TU-04 capability gap ----------------
    for i in range(10):
        oid = 8841 if i == 0 else rng.randint(1000, 9999)
        src = (f"{HDR}\nCancel order #{oid} and issue a refund to the original card.")
        q = ('Emit the ordered tool-call list for the request above as JSON '
             '{"calls":[{"tool":...,"args":{...}}]}; if a requested capability does not exist '
             'use {"unavailable":["..."]}. Do not invent tools.')
        items.append(_mk("TU-04", i, src, q,
                         {"expect": "cancel_plus_unavailable"},
                         {"order_id": oid}))
    # ---------------- TU-05 filtered multi-step ----------------
    statuses = ["processing", "packed", "queued"]
    afters = ["2026-06-01", "2026-05-15", "2026-07-01"]
    for i in range(10):
        em = EMAILS8[0] if i == 0 else rng.choice(EMAILS8)
        status = statuses[0] if i == 0 else rng.choice(statuses)
        after = afters[0] if i == 0 else rng.choice(afters)
        src = (f"{HDR}\nLook up orders for {em} placed after {after} still in '{status}', and "
               f"cancel the oldest one.")
        q = ('Emit the ordered tool-call list for the request above as JSON '
             '{"calls":[{"tool":...,"args":{...}}]}. Ordering matters; reference prior results '
             'where needed.')
        gold_calls = [{"tool": "orders.lookup",
                       "args": {"customer_email": em, "status_filter": status,
                                "placed_after": after}},
                      {"tool": "orders.cancel", "args": {"selection": "argmin placement_date"}}]
        items.append(_mk("TU-05", i, src, q,
                         {"expect": "ordered_actions", "calls": gold_calls},
                         {"email": em, "status": status, "placed_after": after}))
    return items

def etxt_fmt(stxt):
    return _plus60(stxt)

def _plus60(t):
    h, m = map(int, t.split(":"))
    tot = h * 60 + m + 60
    return f"{tot // 60:02d}:{tot % 60:02d}"

TU_REGISTRY = (
    "Available tools (mock registry):\n"
    "calendar.book(room_id, date, start_min, end_min, attendee_count, needs_projector: bool)\n"
    "mail.send(to: [], cc: [], subject, body, priority in {low, normal, high})\n"
    "tracker.create(title, severity in {S1,S2,S3,S4}, component, assignee, due_date)\n"
    "tracker.update(ticket_id, status, comment)\n"
    "orders.lookup(customer_email?, order_id?, status_filter?, placed_after?)\n"
    "orders.cancel(order_id, reason)\n")

def _mk(tpl, idx, src, q, gold, params):
    # registry is part of the frozen task definition (pre-reg §2.3); identical
    # bytes ride V_in for every arm equally ("tools/context identical", §3.1)
    body = src.split("\n", 1)
    src2 = body[0] + "\n" + TU_REGISTRY + (body[1] if len(body) > 1 else "")
    return {"id": f"{tpl}-{idx:02d}", "family": "TU", "template": tpl, "idx": idx,
            "source_text": src2, "question": q, "field_ids": [], "field_aliases": {},
            "units": {}, "gold": gold, "params": params}
