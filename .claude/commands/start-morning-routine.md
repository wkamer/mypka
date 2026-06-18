---
description: Start the daily Morning Routine — Brain Zen, Miracle Roadmap, inbox and session context. Goal check and Highlight → /start-daily-planning.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__get_tasks mcp__todoist__create_tasks
---

# /start-morning-routine

Guide the owner through the Morning Routine. Step by step, wait for input where asked. KISS.

Show this overview first:

> **Morning Routine**
> 1. 🧠 Brain Zen — clear your head
> 2. 🗺️ Miracle Roadmap — track progress
> 3. 📥 Session context — last log + inboxes + open tasks
> 4. 📅 Planning check — confirm or set Highlight for today

Then start Step 0 immediately.

---

## Step 0 — Consistency check previous routine

Query `PKM/personal.db` → `session_logs`:
```sql
SELECT id, summary FROM session_logs
WHERE session_date = date('now', '-1 day') AND session_title = 'End-of-Day Routine'
LIMIT 1;
```

**Found:** mention briefly — "Yesterday closed cleanly." Continue to Step 1.

**Not found:** reflect briefly and open:
- Note that the End-of-Day Routine was not closed yesterday.
- Ask: "What held you back yesterday — no time, forgot, or didn't feel useful?"
- Wait for answer. Log the answer as `open_items` in a short `session_logs` row with `session_title = 'End-of-Day Routine — missed'`, `session_date = yesterday`, and `summary = owner's answer`.
- Continue with the Morning Routine. No judgement, no repetition.

---

## Step 1 — Brain Zen

Ask: "What's on your mind? Dump it here."

Wait for input. For each item:
1. Estimate: **Speedy** (<15 min) or **Task** (15 min – 3 hrs)
2. Show proposal: "→ [task name] — Speedy / Task (reason)"
3. Wait for owner confirmation (yes / correct)
4. Create in Todoist `👤 PERSONAL`. For Speedy: add label `speedy`.

Then say: "Head clear."

---

## Step 1b — Miracle Roadmap progress

Calculate today's target: **84 + number of days since 10 May 2026**.

Ask: "Miracle Roadmap — target today: lesson [X]. Which lesson are you on?"

Wait for answer. Show briefly: "Progress: lesson [Y] of target [X]. [Behind / On track / Ahead]."

No discussion. Just record and move on.

---

## Step 2 — Session context and open tasks

Fetch recent context from `PKM/personal.db`:

```python
import sqlite3

conn = sqlite3.connect('/opt/myPKA/PKM/personal.db')
c = conn.cursor()
c.execute('''SELECT session_date, session_title, summary
             FROM session_logs
             ORDER BY session_date DESC, id DESC
             LIMIT 3''')
for row in c.fetchall():
    print(f"{row[0]} — {row[1]}: {(row[2] or '')[:120]}")
conn.close()
```

Check all inboxes:
- `Team Inbox/Personal/` — new files?
- `Team Inbox/Kamer E-commerce/` — new files?
- `Team Inbox/Geldstroom Regie/` — new files?
- Todoist Inbox — loose items to route

Check open `team_tasks` in `PKM/personal.db` — what is still running?

Report in max 5 lines. No extended analysis.

---

## Step 3 — Daily Planning check

Check whether a task with label `highlight` and Due Date today exists in Todoist.

**Highlight found:** mention it briefly — "⭐ [task name] is your Highlight for today." Ask: "Does this planning still hold, or is there reason to adjust?"

**No highlight:** note that no valid planning exists for today. Run `/start-daily-planning` for today. Use the same steps but with today's date instead of tomorrow.

---

## Closing

Say: "Type `/close-morning-routine` to close the Morning Routine and write everything away."
