---
description: Records everything done in this session — session log, open items, graduation candidates. Can be called at any moment, also multiple times per day.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__create_tasks mcp__todoist__update_tasks
---

# /close-session

Records everything done in this session. Can be called at any moment, also multiple times per day.

---

## Database Routing Rule

| Domain | Database |
|---|---|
| Personal life, goals, habits | `PKM/personal.db` |
| Team operations, learnings, infra | `Team Knowledge/team-knowledge.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |

---

## Step 1 — Compile session log

Based on the conversation context, determine:

| Field | Value |
|---|---|
| `session_date` | today |
| `session_title` | short descriptive title of what was done |
| `topics` | 2–4 tags |
| `summary` | 2–4 sentences: what was done, decisions, deliverables |
| `decisions` | key decisions made |
| `actions_taken` | what was executed |
| `open_items` | anything unresolved |
| `domain` | personal / team / ke / gr |
| `db` | personal / team / ke / gr |

If a session_log already exists for today with the same title: add a suffix, e.g., `(2)`.

---

## Step 1b — Present write plan and wait for Owner confirmation

Present the complete write plan to the Owner:

| Write | Purpose |
|---|---|
| session_logs → [db] | Session log storage |
| Markdown mirror: `Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md` | Filesystem mirror |
| `active-context.md` update | Last session + open items |
| Open items: [X tasks / none] | Todoist + team_tasks (if applicable) |
| Team learning: [yes / no] | team_log row (if applicable) |

Ask: "Confirmed — proceed?"

Wait for explicit Owner confirmation before executing.

---

## Step 2 — Store session log + markdown mirror + active-context

**2a — Write session log to database:**

```python
import sqlite3
from datetime import date

db_paths = {
    'personal': '/opt/myPKA/PKM/personal.db',
    'team':     '/opt/myPKA/Team Knowledge/team-knowledge.db',
    'ke':       '/opt/myPKA/Team Knowledge/Kamer E-commerce/kamer e-commerce.db',
    'gr':       '/opt/myPKA/Team Knowledge/Geldstroom Regie/geldstroom-regie.db',
}

db = db_paths['<domain>']  # replace with actual domain
conn = sqlite3.connect(db)
c = conn.cursor()
c.execute('''INSERT INTO session_logs
    (session_date, session_title, topics, summary, decisions, actions_taken, open_items, agent_slug)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (
    str(date.today()),
    '<session_title>',
    '<topics>',
    '<summary>',
    '<decisions>',
    '<actions_taken>',
    '<open_items>',
    'larry'
))
conn.commit()
print('OK, id:', c.lastrowid)
conn.close()
```

**2b — Write markdown mirror:**

Create file at `Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md` with:
- Title, date, agent, domain
- What happened, decisions, actions taken, open items

**2c — Update active-context.md:**

Edit `Team Knowledge/Core/active-context.md`:
- `## Last session` → today's date + one-sentence summary
- `## Open items` → update to reflect current open state

---

## Step 3 — Open items sweep

For each unresolved thread, decision, or follow-up from this session:
- Create a Todoist task if it is an owner action
- INSERT a `team_tasks` row if it is a delegation or internal action
- Skip if everything is resolved

---

## Step 4 — /improve-system (optional)

If this was a significant session — system changes, new rules, structural decisions, or patterns repeating across sessions — run `/improve-system`.

Skip silently for routine sessions.

---

## Step 5 — Team learning (optional)

If a new pattern or insight emerged that affects team level: INSERT one `team_log` row in `/opt/myPKA/Team Knowledge/team-knowledge.db`. Otherwise skip silently.

---

## Closing

Display a short checklist:

```
✓ session_logs → [database] (id X)
✓ Markdown mirror: Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md
✓ active-context.md updated
✓ Open items: [X tasks / None]
✓ /improve-system: [run / skipped]
```

Then: no further output.
