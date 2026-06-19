# Write Plan: Close-Session Skill Update (Step 2)

**Date:** 2026-06-15
**Authorized by:** Owner (explicit, 2026-06-15)
**Status:** Pending skill-edit authorization

---

## Context

The Close-Session Enforcement Rule was added to CLAUDE.md on 2026-06-15. It defines minimum required write plan elements for every governed session close. Three of those requirements are not yet present in the close-session skill.

This write plan documents the additive edits needed to align the skill with the rule.

---

## Target file

`/opt/myPKA/.claude/commands/close-session.md`

---

## Scope

Additive edits only. Three locations. No structural change. No content removed.

---

## Change 1 — Step 1b write plan table: add Markdown mirror row

**Location:** Section `## Step 1b — Present write plan and wait for Owner confirmation`, write plan table.

**Insert after the `session_logs → [db]` row:**

```
| Markdown mirror: Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md | Filesystem mirror of session log (mandatory per Close-Session Enforcement Rule) |
```

**Before (table excerpt):**
```
| session_logs → [db] | Session log storage |
| UMC → memory_summaries | Context compaction |
```

**After (table excerpt):**
```
| session_logs → [db] | Session log storage |
| Markdown mirror: Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md | Filesystem mirror of session log (mandatory per Close-Session Enforcement Rule) |
| UMC → memory_summaries | Context compaction |
```

---

## Change 2 — Step 1b write plan table: add scope exclusions row

**Location:** Same table as Change 1, after the last existing row (`Deliverable Lifecycle sweep`).

**Append:**

```
| Scope exclusions: [list writes NOT covered by this plan, or "none"] | Explicit boundary statement per Close-Session Enforcement Rule |
```

**Before (table excerpt, last rows):**
```
| LC triage updates: [X overdue_for_triage / none] | learning_candidates status → 'triaged' in team-knowledge.db (if applicable) |
| Deliverable Lifecycle sweep: [X items / none] | deliverable_lifecycle state updates (if applicable) |
```

**After (table excerpt, last rows):**
```
| LC triage updates: [X overdue_for_triage / none] | learning_candidates status → 'triaged' in team-knowledge.db (if applicable) |
| Deliverable Lifecycle sweep: [X items / none] | deliverable_lifecycle state updates (if applicable) |
| Scope exclusions: [list writes NOT covered by this plan, or "none"] | Explicit boundary statement per Close-Session Enforcement Rule |
```

---

## Change 3 — Closing checklist: add Markdown mirror path and deviations

**Location:** Section `## Closing`, ✓ checklist.

**Insert after the `UMC → memory_summaries` line and before `Open items`:**

```
- ✓ Markdown mirror: Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md
- ✓ Deviations: [none / list any write that deviated from the authorized plan]
```

**Before (checklist):**
```
- ✓ session_logs → [database] (id X)
- ✓ UMC → memory_summaries (id X) + daily-routines feed
- ✓ Open items: [X tasks / None]
- ✓ Graduation candidates: [X proposed / None]
- ✓ Deliverable Lifecycle sweep: [X items / None]
```

**After (checklist):**
```
- ✓ session_logs → [database] (id X)
- ✓ UMC → memory_summaries (id X) + daily-routines feed
- ✓ Markdown mirror: Team Knowledge/Core/session-logs/YYYY/MM/YYYYMMDD_<slug>.md
- ✓ Deviations: [none / list any write that deviated from the authorized plan]
- ✓ Open items: [X tasks / None]
- ✓ Graduation candidates: [X proposed / None]
- ✓ Deliverable Lifecycle sweep: [X items / None]
```

---

## Verification plan

After execution: read back the three changed locations in `close-session.md` and confirm:
- Markdown mirror row is present in Step 1b table
- Scope exclusions row is present in Step 1b table
- Markdown mirror and Deviations lines are present in Closing checklist
- No other content was changed

---

## Scope exclusions

- No CLAUDE.md edit
- No new D-folder
- No routing
- No Learning Candidate writes
- No Deliverable Lifecycle sweep
- No dashboard work
- No team_task changes
- No session_log INSERT
- No UMC write

---

## Authorization status

Write plan written: 2026-06-15
Skill edit: **not yet authorized**
