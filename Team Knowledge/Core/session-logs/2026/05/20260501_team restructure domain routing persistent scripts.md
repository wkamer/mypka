# Team restructure, domain routing, and persistent scripts

**Date:** 2026-05-01
**DB row:** team-knowledge.db › session_logs › id=4
**Topics:** team-structure, infrastructure, sienna, scripts

## Summary

Hired Sienna as Personal Assistant and placed her in Personal/Team/ for clean domain separation with a boundary rule against acting in Kamer E-commerce. Redesigned task management so tasks route to the domain they serve rather than to a single team-knowledge.db; team-knowledge.db is now infrastructure-only and hidden from /start-session. Renamed business.db to kamer e-commerce.db and updated all references. Built five persistent Python scripts in Core/Scripts/ (add_task, update_task, complete_task, delete_task, session_open) replacing throwaway inline scripts. Documented the two-system distinction: Todoist for owner tasks, team_tasks for AI delegations — never mirrored.

## Decisions

- Sienna lives in Personal/Team/ — personal domain is self-contained and detachable
- Tasks route to the domain they serve, not the specialist doing the work
- team-knowledge.db team_tasks = infrastructure only, not shown at /start-session
- Todoist and team_tasks are separate systems — never mirror one into the other
- business.db renamed to kamer e-commerce.db
- Persistent scripts replace throwaway Python for all DB operations
- Sienna never acts in Kamer E-commerce domain
- Gmail MCP stays read-only for now

## Actions Taken

- Hired Sienna via Nolan; CLAUDE.md written in Personal/Team/
- Created Personal/Team/team-index.md
- Updated Core/Team/agent-index.md
- Updated Larry's CLAUDE.md (Sienna routing, task management rule rewrite, personal domain routing)
- Renamed business.db → kamer e-commerce.db; updated CLAUDE.md, start-session.md, close-session.md, settings.local.json
- Created Core/Scripts/: add_task.py, update_task.py, complete_task.py, delete_task.py, session_open.py
- Updated start-session.md to call session_open.py
- Removed /close-session auto-exit (Step 12)
- Updated Sienna's CLAUDE.md with Gmail triage workflow and domain boundary

## Delegations

- Nolan: hire Personal PA → reworked (placement + title corrected post-hire)
- Pax: research GongRzhe/Gmail-MCP-Server → success
- Sienna: process Personal/Inbox/ → success
- Sienna: process personal Gmail inbox → partial (read-only scope)

## Open Items

- No dedicated Kamer E-commerce specialist yet

---

*Delivered on: 2026-05-01*
*Delivered at: Core/Knowledge/session-logs/*
