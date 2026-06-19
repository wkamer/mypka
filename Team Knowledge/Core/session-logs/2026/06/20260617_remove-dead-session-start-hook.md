# Remove dead SessionStart hook

**Date:** 2026-06-17
**Agent:** Larry
**Domain:** Team

## What happened

Session start hook was failing at every session open because `/opt/mypka-memory/venv/bin/python` no longer exists. Investigation confirmed both the venv at `/opt/mypka-memory/` and the entire `memory-db` integration folder are gone. Owner decided to remove the hook entirely.

## Decisions

- Remove dead SessionStart hook from `.claude/settings.json`
- Do not restore the memory-db integration

## Actions taken

- Removed `SessionStart` block from `/opt/myPKA/.claude/settings.json`

## Open items

None
