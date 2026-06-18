---
description: Close the day completely — session logs, delegations, sweep, SOP check, DR check, archive deliverables, mirror to markdown. No confirmation needed.
allowed-tools: Bash Read Write Edit mcp__todoist__get_tasks_list mcp__todoist__update_tasks mcp__todoist__close_tasks
---

# /close-end-of-day-routine

Execute directly without asking for confirmation. Writes everything done today.

---

## Database Routing Rule

| Domain | Database |
|---|---|
| Team operations, delegations, learnings | `Team Knowledge/team-knowledge.db` |
| Personal life, goals, habits | `PKM/personal.db` |
| Kamer E-commerce | `Team Knowledge/Kamer E-commerce/kamer e-commerce.db` |
| Geldstroom Regie | `Team Knowledge/Geldstroom Regie/geldstroom-regie.db` |

---

## Step 1 — Session logs

Determine which databases apply based on what was done today. INSERT one `session_logs` row per relevant database:

| Field | Description |
|---|---|
| `session_date` | today |
| `session_title` | short descriptive title |
| `topics` | 2–4 comma-separated tags |
| `summary` | 3–5 sentences: what was done, decisions, deliverables |
| `decisions` | bullet list |
| `actions_taken` | bullet list |
| `delegations` | specialist + task, or "None" |
| `open_items` | unresolved threads |

Skip existing logs for today.

---

## Step 2 — Write delegations

For each delegation today, INSERT into `/opt/myPKA/Team Knowledge/team-knowledge.db`:
- `agent_learnings`: `agent_slug`, `what_worked`, `what_to_improve`, `session_log_id`
- `delegation_outcomes`: `to_agent`, `brief_summary`, `outcome`, `session_log_id`

Skip if no delegations.

---

## Step 3 — Team learning

If a new pattern or team-level insight emerged: INSERT one `team_log` row into `/opt/myPKA/Team Knowledge/team-knowledge.db`:
`entry_type = "learning"`, `content` = one sentence.

Skip if nothing notable.

---

## Step 4 — Sweep open items

For each unresolved thread or follow-up: INSERT one `team_tasks` row in the correct database:
`title`, `assignee` (or NULL), `priority=3`, `source="sweep"`.

---

## Step 5 — Mirror session logs

Mirror each session log from today to:
`Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md`

Create the directory if it does not exist.

---

## Step 6 — Archive reviewed Deliverables

Check `Deliverables/` for subfolders marked as reviewed. Move to `Deliverables/Archive/`.

---

## Step 7 — SOP check

If a new repeatable process emerged today: create a SOP file in the correct domain SOPs folder. Write without asking.

---

## Step 8 — Disaster Recovery check

Triggers (one is enough):
- New plugin, MCP server, or CLI tool installed
- New API key or credential added
- settings.json or .mcp.json changed
- New slash command created
- New hook configured

If yes: open `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`, update the relevant step(s) and the *Last updated* line. Write without asking.

If no: skip silently.

---

## Closing

Show a short checklist of what was written (databases, files, mirrors). Then:

> ✅ **Day closed.**
> Type `/clear` to wipe context and keep the console open.

No further output after this. Session is done.
