---
description: Close the Morning Routine — write session log and Miracle Roadmap progress to personal.db. No confirmation needed.
allowed-tools: Bash Read Write Edit
---

# /close-morning-routine

Execute directly without asking for confirmation. Writes everything done during the Morning Routine.

---

## Step 1 — Write session log

Compile the summary: Brain Zen items (tasks created), Miracle Roadmap progress (lesson X of target Y).

INSERT into `PKM/personal.db` → `session_logs`:

```python
import sqlite3
from datetime import date

conn = sqlite3.connect('/opt/myPKA/PKM/personal.db')
c = conn.cursor()
c.execute('''INSERT OR IGNORE INTO session_logs
    (session_date, session_title, topics, summary, agent_slug)
    VALUES (?, ?, ?, ?, ?)''', (
    str(date.today()), 'Morning Routine', 'routine, morning',
    '<summary>', 'larry'
))
conn.commit()
print('OK, id:', c.lastrowid)
conn.close()
```

If a Morning Routine log for today already exists: skip.

---

## Step 2 — Write Miracle Roadmap progress

UPDATE `PKM/personal.db` → `daily_growth` for today:
- Set `miracle_roadmap_les` = the lesson the owner is on (from the Morning Routine)
- If the row does not exist yet: INSERT with today's date

---

## Step 3 — Sweep Brain Zen items

Check whether all Brain Zen items from this session are in Todoist as a task or created as a Calendar event. If not: create them without asking.

---

## Closing

Show a short checklist of what was actually written, for example:
- ✓ session_logs → personal.db (id X)
- ✓ daily_growth.notes (Miracle Roadmap lesson X/target Y) → personal.db
- ✓ Brain Zen sweep: [X tasks in Todoist, Y events in Calendar]

Then:

> ✅ **Morning Routine closed.**
> Type `/compact` to compress context for the next session.

No further output after this. Session is done.
