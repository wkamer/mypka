---
description: Start the daily Afternoon Routine — process inbox, delegate, reassess the day.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__create_tasks mcp__todoist__close_tasks mcp__claude_ai_Gmail__search_threads mcp__claude_ai_Gmail__get_thread
---

# /start-afternoon-routine

Guide the owner through the Afternoon Routine. Run when the Deep Work session is done — typically mid-afternoon. No fixed time required.

Show this overview first:

> **Afternoon Routine**
> 1. 📥 Inbox check — Gmail, Team Inbox, Todoist Inbox
> 2. 🤝 Delegations — what goes to the team?
> 3. 🎯 Reassess the day — Highlight done?
> 4. 📊 Goal signal — movement on Goals?
> 5. 💪 Growth signal — moved / learned / eaten / slept?

Then start Step 0 immediately.

---

## Step 0 — Consistency check previous routine

Query `PKM/personal.db` → `session_logs`:
```sql
SELECT id, summary FROM session_logs
WHERE session_date = date('now') AND session_title = 'Morning Routine'
LIMIT 1;
```

**Found:** mention briefly — "Morning Routine done today." Continue to Step 1.

**Not found:** reflect briefly and open:
- Note that the Morning Routine was not closed today.
- Ask: "What held you back — no time, forgot, or didn't feel useful?"
- Wait for answer. Log the answer as `open_items` in a short `session_logs` row with `session_title = 'Morning Routine — missed'` and `summary = owner's answer`.
- Continue with the Afternoon Routine. No judgement, no repetition.

---

## Step 1 — Inbox check (10 min)

Check the inboxes:

1. `Team Inbox/Personal/` — new files?
2. Gmail — unread threads (via `search_threads` with `is:unread in:inbox`)
3. Todoist Inbox — loose items not yet routed

Process what can be processed:
- Tasks → `👤 PERSONAL` or delegate via team_tasks. For each new task: estimate Speedy (<15 min) or Task (15 min – 3 hrs), show proposal, wait for confirmation. For Speedy: add label `speedy`.
- Info → correct SSOT in PKM
- Noise → ignore or archive

Report: "X items processed, Y delegated, Z open."

---

## Step 2 — Delegations (5 min)

Are there tasks that belong to a specialist?

- Personal execution work → Sienna
- Journaling input → Penn
- Kamer E-commerce → via Larry to Sasha/Vera
- Geldstroom Regie → Finn

Create a `team_tasks` row in the correct database for each delegation.

---

## Step 3 — Reassess the day (5 min)

Show today's Highlight (⭐).

Ask: "Is the Highlight done? If not — can it still happen today or does it move?"

- Done → close the task in Todoist
- Not yet → leave it, no action needed
- Moving → reschedule to tomorrow with new due date

Also check: have unexpected tasks come in that displaced the Highlight? If so — flag the pattern if it recurs.

---

## Step 4 — Goal signal (2 min)

Quick check: has there been movement on any of the Goals today?

| Goal | Movement today? |
|---|---|
| G-Scheiding afronden | yes / no |
| G-Nieuwe eigen plek | yes / no |
| G-Geldstroom Regie validatie | yes / no |

If a Goal has had no movement for multiple days: flag it directly. Not as criticism — as a signal.

---

## Step 5 — Growth signal (max 2 min)

Ask one focused question across the four growth axes:

> "Did you move / learn something / eat as intended / sleep well today?"

Wait for answer. Log in `PKM/personal.db` table `daily_growth` (column: `afternoon_checkin`). If an axis has been red for 3+ days: flag it briefly — as a signal, not as criticism.

---

## Missed day

No retrospective. Just run today. The routine comes back every day.

---

## Closing

Say: "Type `/close-afternoon-routine` to close the Afternoon Routine and write everything away."
