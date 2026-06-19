# Todoist archive/unarchive scripts + API token setup
**Date:** 2026-05-01
**DB row:** team-knowledge.db session_logs id=5

## Summary
Added two persistent scripts to Core/Scripts: archive_project.py and unarchive_project.py, both using the Todoist Sync API v1 project_archive and project_unarchive commands. The TODOIST_API_TOKEN was stored in ~/.claude/settings.json under the env section so it is available to all shell sessions without appearing in chat. Both scripts were tested successfully on P - NEW START.

## Decisions
- Todoist archiving uses Sync API, not REST v2 (which lacks the endpoint)
- Token stored in ~/.claude/settings.json env section

## Actions taken
- Created Core/Scripts/archive_project.py
- Created Core/Scripts/unarchive_project.py
- Added TODOIST_API_TOKEN to ~/.claude/settings.json

## Delegations
None

## Open items
None
