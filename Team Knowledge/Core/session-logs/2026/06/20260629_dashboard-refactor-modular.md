# Dashboard refactor: modular structure + dev workflow

**Date:** 2026-06-29
**Agent:** Larry
**Domain:** Team

## What happened

Conversation started with excluding Team Inbox from git. Owner identified that dashboard development was too slow and token-heavy — Devon was burning too many tokens per feature because EmailTriage.jsx (756 lines) and email_management.py (750 lines) were monoliths with no orientation document.

Devon analysed the codebase and executed a full modular refactor via Codex. Frontend split into components/EmailTriage/ (7 files) + api/ layer. Backend split into a proper package (routes, models, db, ai, executors, serializers). ARCHITECTURE.md created. 43 backend tests green, frontend build clean (38 modules).

Side conversation: owner explored the mypka-cockpit (Team Inbox) to understand if it was relevant. Conclusion: cockpit is a PKM reader, not a dashboard replacement. Stack comparison showed both use React+Vite+Tailwind; cockpit is Node.js backend vs FastAPI. Decision: keep current stack, fix the structure.

## Decisions

- Keep FastAPI+React stack — switching to full-JS not worth the migration cost for an existing project.
- Refactor for modularity instead of stack change — per-domain files, not monoliths.
- Devon must proactively maintain ARCHITECTURE.md going forward without being asked.

## Actions taken

- Team Inbox added to .gitignore
- Dashboard refactor executed via Codex: 18 new frontend files, backend package, ARCHITECTURE.md
- Devon AGENT.md updated: codebase navigability rule added
- All committed and pushed (commits 4565471, ee1e671)

## Open items

None.
