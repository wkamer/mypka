---
description: Close the Afternoon Routine — write session log, delegations, and Goal movement to the correct databases. No confirmation needed.
allowed-tools: Bash Read Write Edit
---

# /close-afternoon-routine

Execute directly without asking for confirmation. Writes everything done during the Afternoon Routine.

---

## Database Routing Rule

| Domain | Database |
|---|---|
| Personal life, goals, habits | `PKM/personal.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |
| Team operations, delegations | `Team Knowledge/team-knowledge.db` |

---

## Step 1 — Write session log

INSERT into `PKM/personal.db` → `session_logs`:
- `session_date` = today
- `session_title` = "Afternoon Routine"
- `topics` = "routine, afternoon"
- `summary` = Summary of inbox processing (X items), delegations (Y), Highlight status, Goal movement per goal.

If an Afternoon Routine log for today already exists: skip.

---

## Step 2 — Write delegations

For each delegation made during the Afternoon Routine:
- INSERT a `team_tasks` row in the correct database (routing rule above)
- Fields: `title`, `assignee`, `priority=3`, `source="afternoon-routine"`

Skip if no delegations.

---

## Step 3 — Write Goal movement

UPDATE `PKM/personal.db` → `daily_growth` for today:
- Set `afternoon_checkin` = growth signal answer from the owner
- If the row does not exist yet: INSERT with today's date

---

## Closing

Show a short checklist of what was actually written, for example:
- ✓ session_logs → personal.db (id X)
- ✓ daily_growth.afternoon_checkin → personal.db
- ✓ team_tasks → [database] (X delegations)

Then:

> ✅ **Afternoon Routine closed.**
> Type `/compact` to compress context for the next session.

No further output after this. Session is done.
