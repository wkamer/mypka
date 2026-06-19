# Sienna session start wiring

**Date:** 2026-06-18
**Agent:** Larry
**Domain:** Team

---

## What happened

Diagnosed why Sienna's proactive session start was not firing after two commits added Session Start instructions to her AGENT.md. Both commits only changed the AGENT.md — no invocation mechanism was created. Sienna was never actually spawned at session open.

## Decisions

Both session start paths now delegate to Sienna:
- `/start-morning-routine` Step 2 — spawns `sienna` subagent before session context summary
- `CLAUDE.md` Session Rhythm step 2 — replaced Larry's manual Team Inbox check with Sienna delegation

## Actions taken

- Edited `/opt/myPKA/.claude/commands/start-morning-routine.md` — Step 2 now invokes `sienna` subagent with full Session Start brief
- Edited `/opt/myPKA/CLAUDE.md` — Session Rhythm step 2 now delegates to Sienna instead of Larry checking Team Inbox himself
- Updated `feedback_plan_before_execute.md` memory — added Karpathy verification rule: diagnose → verify → propose → confirm → execute

## Open items

None
