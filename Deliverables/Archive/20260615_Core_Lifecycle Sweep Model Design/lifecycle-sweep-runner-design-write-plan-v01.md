# Write Plan — Lifecycle Sweep Runner Design v01

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021 + GL-023
**Governing design:** `lifecycle-sweep-model-design-v03.md`

---

## 1. GL-023 Active Gate

**Interview:** Sweep runner design document specifying SQL queries, conflict detection,
and output assembly for both LC and DL sweeps. For any agent or script executing the
/close-session sweep steps. Out of scope: actual Python implementation, DB writes,
schema changes, state corrections, cleanup, archiving, OD-3 resolution, new D-folder.

**Spec:** New file `lifecycle-sweep-runner-design-v01.md` in existing D-folder. Contains
confirmed SQL per category, conflict detection logic, output format. No code execution,
no mutations.

**Verify plan:** String search confirms all 5 LC + all 5 DL + STATE CONFLICT + NOT
CLASSIFIABLE sections present. Confirms no INSERT/UPDATE/DELETE in file. Confirms OD-3
flagged as blocker.

**Tool check:** Write tool for creation; ctx_execute string search for coverage
verification.

**Murphy scan:** Field name typo referencing non-existent schema column. Mitigation:
all field names cross-checked against confirmed schemas in this session before writing.
Rollback: file is read-only design, no DB state; delete and rewrite.

---

## 2. Target File

| Field | Value |
|---|---|
| Path | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-runner-design-v01.md` |
| Action | New file |
| New D-folder | No |
| DB changes | None |

---

## 3. Confirmed Schema Inputs

### 3.1 learning_candidates (team-knowledge.db)

Fields used in sweep queries:
`id`, `title`, `flagged_by`, `flagged_at`, `status`, `triage_routing`, `triaged_at`,
`processed_at`, `resolved_at`, `max_days_captured`, `created_at`

### 3.2 deliverable_lifecycle (team-knowledge.db)

Fields used in sweep queries:
`id`, `artifact_name`, `artifact_type`, `state`, `state_gl017`, `owner_decision`,
`processed_at`, `registered_at`, `owner_decision_at`

---

## 4. Proposed Content of the Runner Design Document

### Section 1 — LC Sweep Queries

One SELECT per category, executed in priority order. Results are categorized and de-duped:
higher-priority category wins.

| Category | Query logic |
|---|---|
| Urgent | `status NOT IN ('processed','closed') AND triage_routing = 'urgent' AND resolved_at IS NULL` |
| Graduation Candidate | `status NOT IN ('processed','closed') AND triage_routing = 'graduation_candidate' AND resolved_at IS NULL` |
| Overdue for Triage | `status = 'captured' AND triage_routing NOT IN ('urgent','graduation_candidate') AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_captured` |
| Stalled at Triaged | `status = 'triaged' AND processed_at IS NULL AND CAST(julianday('now') - julianday(triaged_at) AS INTEGER) >= 7` |
| Pending | `status = 'captured' AND triage_routing NOT IN ('urgent','graduation_candidate') AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) < max_days_captured` |
| CONFLICT | `resolved_at IS NOT NULL AND status NOT IN ('processed','closed')` |
| NOT CLASSIFIABLE | Any row not matched by any of the above |

Exclusion filter applied to all: `status NOT IN ('processed','closed')` before category
assignment. Processed and closed rows never appear in output.

### Section 2 — DL Sweep Queries

One SELECT per category. STATE CONFLICT detection runs before category assignment.

| Category | Query logic |
|---|---|
| Open Execution | `state NOT IN ('archived','closed') AND owner_decision = 'confirmed' AND processed_at IS NULL` |
| Carry-Forward | `state IN ('active','ready') AND owner_decision IS NULL` |
| Deferred | `state NOT IN ('archived','closed') AND owner_decision = 'deferred'` |
| Excluded | `state NOT IN ('archived','closed') AND owner_decision = 'rejected'` (no live rows) |
| Not-blocker | No structured value defined — shown as empty pending OD resolution |
| STATE CONFLICT | `state NOT IN ('archived','closed') AND state != state_gl017` — OD-3 open, no auto-classification |
| NOT CLASSIFIABLE | `owner_decision` not in known enum AND not NULL AND no STATE CONFLICT |

Exclusion filter applied to all: `state NOT IN ('archived','closed')`.

### Section 3 — Category Priority and De-duplication

LC sweep: priority order is Urgent > Graduation Candidate > Overdue > Stalled > Pending.
If a row matches two categories, the higher-priority category wins.

DL sweep: STATE CONFLICT check runs first. A row with `state != state_gl017` is placed
in STATE CONFLICT regardless of `owner_decision`. Any structured `owner_decision` takes
precedence over Carry-Forward for rows without a state conflict.

### Section 4 — OVERDUE Urgency Attribute (DL)

Applied inline per item in any DL category:
`[OVERDUE]` if item is in `ready` state and `julianday('now') - julianday(registered_at) >= 7`.
`[WITHIN THRESHOLD]` if < 7 days.

### Section 5 — Output Assembly

LC output: build five category blocks + CONFLICT + NOT CLASSIFIABLE. Each block header
always present even when empty (`— no items —`). Items sorted by days open descending.

DL output: build five category blocks + STATE CONFLICT + NOT CLASSIFIABLE. Same empty
block rule. OVERDUE attribute appended inline per item.

### Section 6 — OD-3 Blocker Note

STATE CONFLICT section for DL sweep surfaces 13 rows without classifying them
(ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59). OD-3 (state conflict
precedence) must be resolved before these rows can be auto-classified. Until then,
they are surfaced as-is for Owner awareness.

---

## 5. File Verification Criteria

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | Path present on disk |
| V-2 | Size > 0 | Non-empty |
| V-3 | All 5 LC categories covered | Sections for Urgent, Graduation Candidate, Overdue, Stalled, Pending present |
| V-4 | All 5 DL categories covered | Sections for Open Execution, Carry-Forward, Deferred, Excluded, Not-blocker present |
| V-5 | STATE CONFLICT and NOT CLASSIFIABLE present | Both sections present in DL query spec |
| V-6 | No SQL mutations | File contains no INSERT, UPDATE, or DELETE statements |
| V-7 | OD-3 flagged | Text referencing OD-3 as blocker for STATE CONFLICT resolution present |

All 7 criteria must pass. Any failure = stop, report to Owner.

---

## 6. Explicit Exclusions

| Exclusion |
|---|
| No Python script or executable code |
| No DB writes of any kind |
| No deliverable_lifecycle INSERT or UPDATE |
| No team_tasks update |
| No new D-folder |
| No schema changes |
| No cleanup, archiving, or lifecycle state changes |
| No corrections to the 13 STATE CONFLICT rows |
| No CLAUDE.md, GL, SOP, or AGENT.md edits |

---

## 7. Execution Sequence (post-authorization)

1. Write `lifecycle-sweep-runner-design-v01.md`
2. Verify V-1 through V-7
3. Report to Owner: file path, verification results
4. No further actions

---

*Write plan persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
