---
name: project_daily_planning_state
description: State of the daily planning scripts and skill after session 24-05 — fully rebuilt and tested
metadata:
  node_type: memory
  type: project
  originSessionId: e1b074ce-75a2-4a0a-94fe-eb29c96aa0ec
---

Daily planning flow is rebuilt and ready for daily use. PPM + BPM (Steps 1-8).

**Scripts — ready**
- `dp_fetch.py` — fetches completed, open, projects + writes label cache (dp_task_labels.json)
- `dp_step1.py` — Review: 3 sections x 3 tiers; label cache for completed tasks; `@label` parsing as fallback
- `dp_step2.py` — Goals/Project alignment; writes dp_goals.json
- `dp_step3.py` — Plan: 4 blocks; Type column removed; Do Date on all blocks; suffixed with for postponed
- `dp_status.py` — Day status: reads dp_plan.json, filters on planning labels + due = target, fetches fresh completed

**Label architecture**
- `highlight` — Highlight of the Day (max 1)
- `support` — Support Task (max 3)
- `committed` — Buffer task in committed plan (added during Commit in Step 4)
- `postponed` — once postponed, never deleted (visible in Step 3 + dp_status)

**Skill — start-daily-planning-v3.md**
- Step 1 target = always today (review of today)
- Step 3 target = planning target (today or tomorrow based on time)
- Postpone = shift due date + add `postponed` label
- Commit = `committed` label on buffer tasks + due = target + fresh fetch → dp_plan.json
- Output always verbatim as own text — no introduction

**Known open issues**
- `committed` labels from previous day are not automatically cleaned up on new planning
- BPM in dp_step2.py: PPM_GOALS_DIR still hardcoded (BPM goals not yet fully working)
- dp_status.py: standalone script, no skill trigger

**Why:** Session fully rebuilt after architecture problem (bash tool output not visible as markdown).
**How to apply:** On new session start directly with /start-daily-planning-v3 — all scripts are correct.
