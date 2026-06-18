---
description: Close the day — digital wrap-up, reflect, plan tomorrow, log session.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__close_tasks
---

# /start-end-of-the-day-routine

Close the day deliberately. Digital and physical. KISS.

Show this overview first:

> **End-of-Day Routine**
> 1. 💻 Digital close — Highlight + tasks + Goal movement
> 2. 🪞 Day reflection — one thing that went well
> 3. 📅 Daily Planning — set up tomorrow (`/start-daily-planning`)
> 4. 🚶 Physical close — screen off, move, evening for yourself
> 5. 🔒 Close the day — `/close-end-of-day-routine`

Then start Step 0 immediately.

---

## Step 0 — Consistency check previous routine

Query `PKM/personal.db` → `session_logs`:
```sql
SELECT id, summary FROM session_logs
WHERE session_date = date('now') AND session_title = 'Afternoon Routine'
LIMIT 1;
```

**Found:** mention briefly — "Afternoon Routine done today." Continue to Step 1.

**Not found:** reflect briefly and open:
- Note that the Afternoon Routine was not closed today.
- Ask: "What held you back — no time, forgot, or didn't feel useful?"
- Wait for answer. Log the answer as `open_items` in a short `session_logs` row with `session_title = 'Afternoon Routine — missed'` and `summary = owner's answer`.
- Continue with the End-of-Day Routine. No judgement, no repetition.

---

## Step 1 — Digital close

Goal movement today? One sentence per goal:
- G-Scheiding: moved / not moved
- G-Nieuwe eigen plek: moved / not moved
- G-Geldstroom Regie: moved / not moved

If a Goal has not moved for multiple days: flag it.

No task management here. Everything around tasks — Highlight, open tasks, overdue — is in `/start-daily-planning` (Step 3).

---

## Step 2 — Day reflection

Ask: "One thing that went well today?"

Wait for answer. Confirm briefly. No analysis.

Then trigger `/journal` immediately — always, without asking.

---

## Step 3 — Daily Planning

This is the default moment for Daily Planning. Planning is set up for the next calendar day.

Say: "Time to set up tomorrow deliberately."

Run `/start-daily-planning` directly as part of this routine. Then continue to Step 4.

---

## Step 4 — Physical close

Remind the owner:
- Short movement or walk
- Something for yourself tonight

Ask: "What are you doing for yourself tonight?"

Wait for answer. Confirm. No judgement.

---

## Step 5 — Close the day

Say: "Type `/close-end-of-day-routine` to definitively close the day and write everything away."
