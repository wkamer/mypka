# Sienna proactive upgrades + journal folder cleanup

**Date:** 2026-06-18
**Agent:** larry
**Domain:** team

## What happened

Deleted 15 orphaned journal folders (one per agent, each containing only _template.md, never git-tracked). Updated Sienna AGENT.md in two commits: she now proactively checks Gmail inbox and Team Inbox at session start, reads active goals as a baseline, and flags mid-session when work drifts from active goals. Goal-drift trigger fires once, then waits.

## Decisions

- Sienna proactive on inbox and goal-watching at session start.
- One-flag rule for goal drift: she names it once and waits for owner response.

## Actions taken

- Deleted 15 `journal/` folders across all agent directories.
- Sienna AGENT.md: added Session Start inbox + goal baseline (commit 53320cb).
- Sienna AGENT.md: added goal-drift interrupt trigger (commit f6b7a58).

## Open items

None.
