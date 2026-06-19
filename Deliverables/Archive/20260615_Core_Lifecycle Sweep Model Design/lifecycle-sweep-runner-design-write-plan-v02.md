# Write Plan — Lifecycle Sweep Runner Design v01 (write plan v02)

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Supersedes:** lifecycle-sweep-runner-design-write-plan-v01.md
**Correction:** LC NULL routing bug + DL state_gl017 NULL handling
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021 + GL-023
**Governing design:** `lifecycle-sweep-model-design-v03.md`

---

## 1. GL-023 Active Gate

**Interview:** Sweep runner design document specifying SQL queries, conflict detection,
and output assembly for both LC and DL sweeps. For any agent or script executing the
/close-session sweep steps. Out of scope: actual Python implementation, DB writes,
schema changes, state corrections, cleanup, archiving, OD-3 resolution, new D-folder.

**Spec:** New file `lifecycle-sweep-runner-design-v01.md` in existing D-folder. Contains
confirmed SQL per category with NULL-safe comparisons, conflict detection logic, output
format. No code execution, no mutations.

**Verify plan:** String search confirms all 5 LC + all 5 DL + STATE CONFLICT + NOT
CLASSIFIABLE sections present. Confirms corrected NULL-safe query syntax present.
Confirms no INSERT/UPDATE/DELETE in file. Confirms OD-3 flagged and state_gl017 NULL
handling explicitly documented.

**Tool check:** Write tool for creation; ctx_execute string search for coverage
and NULL-safe syntax verification.

**Murphy scan:** Two known SQL NULL traps already identified and corrected in this
write plan (triage_routing NOT IN, state_gl017 != comparison). Additional trap:
julianday() returns NULL if the date field is NULL or malformed — queries must handle
NULL flagged_at / triaged_at / registered_at gracefully. Design document must note
this and specify COALESCE or IS NOT NULL guard where applicable.

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

## 4. Corrections from Write Plan v01

### 4.1 LC — NULL routing bug (Overdue for Triage and Pending)

**v01 (incorrect):**
```
triage_routing NOT IN ('urgent','graduation_candidate')
```

**v02 (corrected):**
```
(triage_routing IS NULL OR triage_routing NOT IN ('urgent','graduation_candidate'))
```

**Why:** In SQLite, `NULL NOT IN (...)` evaluates to NULL, not TRUE. A `captured` LC
with no `triage_routing` set would silently fail to match and disappear from both
Overdue for Triage and Pending. The corrected form explicitly includes NULL rows.

### 4.2 DL — state_gl017 NULL handling in STATE CONFLICT

**v01 (incomplete):**
```
state != state_gl017
```

**v02 (corrected — split into two explicit rules):**

| Condition | Routing | Reason |
|---|---|---|
| `state_gl017 IS NOT NULL AND state != state_gl017` | STATE CONFLICT | Known disagreement between two known values |
| `state_gl017 IS NULL AND state NOT IN ('archived','closed')` | NOT CLASSIFIABLE | Classification state unknown — cannot determine conflict or agreement |

**Why:** `state != state_gl017` returns NULL when `state_gl017 IS NULL`, causing the
row to silently disappear. A row with NULL `state_gl017` cannot be placed in STATE
CONFLICT (no disagreement can be confirmed) but must not disappear — it routes to NOT
CLASSIFIABLE.

---

## 5. Proposed Content of the Runner Design Document

### Section 1 — LC Sweep Queries

Exclusion filter applied before all categories: `status NOT IN ('processed','closed')`.

| Category | Query logic |
|---|---|
| Urgent | `status NOT IN ('processed','closed') AND triage_routing = 'urgent' AND resolved_at IS NULL` |
| Graduation Candidate | `status NOT IN ('processed','closed') AND triage_routing = 'graduation_candidate' AND resolved_at IS NULL` |
| Overdue for Triage | `status = 'captured' AND (triage_routing IS NULL OR triage_routing NOT IN ('urgent','graduation_candidate')) AND flagged_at IS NOT NULL AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_captured` |
| Stalled at Triaged | `status = 'triaged' AND processed_at IS NULL AND triaged_at IS NOT NULL AND CAST(julianday('now') - julianday(triaged_at) AS INTEGER) >= 7` |
| Pending | `status = 'captured' AND (triage_routing IS NULL OR triage_routing NOT IN ('urgent','graduation_candidate')) AND flagged_at IS NOT NULL AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) < max_days_captured` |
| CONFLICT | `resolved_at IS NOT NULL AND status NOT IN ('processed','closed')` |
| NOT CLASSIFIABLE | Any row in scope not matched by any of the above |

NULL guard note: `flagged_at IS NOT NULL` and `triaged_at IS NOT NULL` guards added to
prevent julianday() returning NULL and silently dropping rows. Any row with a NULL
date field that would otherwise qualify for Overdue, Stalled, or Pending routes to
NOT CLASSIFIABLE.

### Section 2 — DL Sweep Queries

Exclusion filter applied before all categories: `state NOT IN ('archived','closed')`.
STATE CONFLICT and NOT CLASSIFIABLE detection runs before category assignment.

| Category | Query logic |
|---|---|
| STATE CONFLICT (runs first) | `state NOT IN ('archived','closed') AND state_gl017 IS NOT NULL AND state != state_gl017` |
| NOT CLASSIFIABLE — unknown state_gl017 | `state NOT IN ('archived','closed') AND state_gl017 IS NULL` |
| NOT CLASSIFIABLE — unknown owner_decision | `state NOT IN ('archived','closed') AND owner_decision IS NOT NULL AND owner_decision NOT IN ('confirmed','deferred','rejected') AND NOT (state_gl017 IS NOT NULL AND state != state_gl017)` |
| Open Execution | `state NOT IN ('archived','closed') AND owner_decision = 'confirmed' AND processed_at IS NULL` — excluded from STATE CONFLICT |
| Carry-Forward | `state IN ('active','ready') AND owner_decision IS NULL` — excluded from STATE CONFLICT |
| Deferred | `state NOT IN ('archived','closed') AND owner_decision = 'deferred'` — excluded from STATE CONFLICT |
| Excluded | `state NOT IN ('archived','closed') AND owner_decision = 'rejected'` — excluded from STATE CONFLICT (no live rows currently) |
| Not-blocker | No structured value defined — section shown as empty pending OD resolution |

Priority rule: STATE CONFLICT takes precedence over category assignment. A row in
STATE CONFLICT is not assigned to any named category regardless of `owner_decision`.

### Section 3 — Category Priority and De-duplication

LC sweep: priority order is Urgent > Graduation Candidate > Overdue > Stalled > Pending.
A row matching multiple categories appears only in the highest-priority category.

DL sweep: STATE CONFLICT runs first. Any row with a confirmed state conflict is removed
from category assignment. Within named categories, structured `owner_decision` takes
precedence over Carry-Forward (NULL).

### Section 4 — OVERDUE Urgency Attribute (DL)

Applied inline per item in any DL named category:
`[OVERDUE]` if `state = 'ready'` and `registered_at IS NOT NULL` and
`julianday('now') - julianday(registered_at) >= 7`.
`[WITHIN THRESHOLD]` if < 7 days.
No attribute if `registered_at IS NULL`.

### Section 5 — Output Assembly

LC output: five category blocks + CONFLICT + NOT CLASSIFIABLE. Each block header always
present, even when empty (`— no items —`). Items sorted by days open descending.

DL output: five category blocks + STATE CONFLICT + NOT CLASSIFIABLE. Same empty block
rule. OVERDUE attribute appended inline per item. NOT CLASSIFIABLE includes both
unknown-state_gl017 rows and unknown-owner_decision rows, labeled by sub-type.

### Section 6 — OD-3 Blocker Note

STATE CONFLICT section for DL sweep surfaces 13 rows without classifying them
(ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59). OD-3 (state conflict
precedence) must be resolved before these rows can be auto-classified. Until then,
they are surfaced as-is for Owner awareness.

---

## 6. File Verification Criteria

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | Path present on disk |
| V-2 | Size > 0 | Non-empty |
| V-3 | All 5 LC categories covered | Urgent, Graduation Candidate, Overdue, Stalled, Pending present |
| V-4 | All 5 DL categories covered | Open Execution, Carry-Forward, Deferred, Excluded, Not-blocker present |
| V-5 | STATE CONFLICT and NOT CLASSIFIABLE present | Both sections present in DL query spec |
| V-6 | No SQL mutations | No INSERT, UPDATE, or DELETE in file |
| V-7 | OD-3 flagged | Text referencing OD-3 as blocker present |
| V-8 | NULL-safe LC routing | `(triage_routing IS NULL OR triage_routing NOT IN` present in Overdue and Pending queries |
| V-9 | state_gl017 NULL handling explicit | Both `state_gl017 IS NOT NULL AND state != state_gl017` and `state_gl017 IS NULL` routing documented |

All 9 criteria must pass. Any failure = stop, report to Owner.

---

## 7. Explicit Exclusions

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

## 8. Execution Sequence (post-authorization)

1. Write `lifecycle-sweep-runner-design-v01.md`
2. Verify V-1 through V-9
3. Report to Owner: file path, verification results
4. No further actions

---

*Write plan v02 persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
