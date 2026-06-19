# Lifecycle Sweep Runner Design v01

**Document type:** Design artifact — implementation blueprint
**Status:** Active
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Write plan:** `lifecycle-sweep-runner-design-write-plan-v02.md`
**Governing design:** `lifecycle-sweep-model-design-v03.md`
**DB:** `team-knowledge.db`

---

## 1. Purpose

This document specifies the exact SQL queries, conflict detection logic, and output
assembly procedure for the LC sweep and DL sweep executed at /close-session.

This is a read-only design. No mutations are defined here. All queries are SELECT only.

---

## 2. Confirmed Schema Inputs

### 2.1 learning_candidates

Fields used in sweep queries:

| Field | Type | Notes |
|---|---|---|
| `id` | INTEGER | Row identifier |
| `title` | TEXT | Displayed in output |
| `flagged_by` | TEXT | Displayed in output |
| `flagged_at` | TEXT | Date field — NULL guard required before julianday() |
| `status` | TEXT | `captured`, `triaged`, `processed`, `closed` |
| `triage_routing` | TEXT | `graduation_candidate`, `standard`, `urgent`, or NULL |
| `triaged_at` | TEXT | Date field — NULL guard required before julianday() |
| `processed_at` | TEXT | NULL = not yet processed |
| `resolved_at` | TEXT | NULL = not yet resolved |
| `max_days_captured` | INTEGER | Default 3, adjustable per row |

### 2.2 deliverable_lifecycle

Fields used in sweep queries:

| Field | Type | Notes |
|---|---|---|
| `id` | INTEGER | Row identifier |
| `artifact_name` | TEXT | Displayed in output |
| `artifact_type` | TEXT | Displayed in output |
| `state` | TEXT | `active`, `ready`, `archived`, `closed` |
| `state_gl017` | TEXT | May be NULL — explicit handling required |
| `owner_decision` | TEXT | May be NULL; known enum: `confirmed`, `deferred`, `rejected` |
| `processed_at` | TEXT | NULL = processing not recorded |
| `registered_at` | TEXT | Date field — NULL guard required before julianday() |
| `owner_decision_at` | TEXT | Date of decision if recorded |

---

## 3. LC Sweep Queries

Exclusion filter applied before all categories:
`status NOT IN ('processed', 'closed')`

Categories are evaluated in priority order. A row matched by a higher-priority category
is excluded from lower-priority evaluation.

### 3.1 Urgent

```sql
SELECT id, title, flagged_by, flagged_at, status
FROM learning_candidates
WHERE status NOT IN ('processed', 'closed')
  AND triage_routing = 'urgent'
  AND resolved_at IS NULL
ORDER BY flagged_at ASC;
```

### 3.2 Graduation Candidate

```sql
SELECT id, title, flagged_by, flagged_at, status
FROM learning_candidates
WHERE status NOT IN ('processed', 'closed')
  AND triage_routing = 'graduation_candidate'
  AND resolved_at IS NULL
ORDER BY flagged_at ASC;
```

### 3.3 Overdue for Triage

NULL guard: `flagged_at IS NOT NULL` prevents julianday() from returning NULL and
silently dropping rows. Rows with NULL `flagged_at` that would otherwise qualify route
to NOT CLASSIFIABLE.

```sql
SELECT id, title, flagged_by, flagged_at, max_days_captured,
       CAST(julianday('now') - julianday(flagged_at) AS INTEGER) AS days_open
FROM learning_candidates
WHERE status = 'captured'
  AND (triage_routing IS NULL OR triage_routing NOT IN ('urgent', 'graduation_candidate'))
  AND flagged_at IS NOT NULL
  AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) >= max_days_captured
ORDER BY days_open DESC;
```

### 3.4 Stalled at Triaged

Threshold: 7 calendar days without `processed_at`. OD-1 resolved 2026-06-15.
NULL guard: `triaged_at IS NOT NULL`.

```sql
SELECT id, title, triaged_at,
       CAST(julianday('now') - julianday(triaged_at) AS INTEGER) AS days_waiting
FROM learning_candidates
WHERE status = 'triaged'
  AND processed_at IS NULL
  AND triaged_at IS NOT NULL
  AND CAST(julianday('now') - julianday(triaged_at) AS INTEGER) >= 7
ORDER BY days_waiting DESC;
```

### 3.5 Pending

```sql
SELECT id, title, flagged_at,
       CAST(julianday('now') - julianday(flagged_at) AS INTEGER) AS days_open
FROM learning_candidates
WHERE status = 'captured'
  AND (triage_routing IS NULL OR triage_routing NOT IN ('urgent', 'graduation_candidate'))
  AND flagged_at IS NOT NULL
  AND CAST(julianday('now') - julianday(flagged_at) AS INTEGER) < max_days_captured
ORDER BY days_open DESC;
```

### 3.6 CONFLICT

```sql
SELECT id, title, status, resolved_at
FROM learning_candidates
WHERE resolved_at IS NOT NULL
  AND status NOT IN ('processed', 'closed');
```

### 3.7 NOT CLASSIFIABLE (LC)

Any row meeting the exclusion filter (`status NOT IN ('processed', 'closed')`) that:
- is not matched by Urgent, Graduation Candidate, CONFLICT, AND
- has `flagged_at IS NULL` (cannot compute age) AND status is `captured` or `triaged`

These rows surface in NOT CLASSIFIABLE because age-based classification is impossible
without a valid date.

---

## 4. DL Sweep Queries

Exclusion filter applied before all categories:
`state NOT IN ('archived', 'closed')`

STATE CONFLICT and NOT CLASSIFIABLE detection runs before named category assignment.
A row matched by STATE CONFLICT or NOT CLASSIFIABLE is not assigned to a named category.

### 4.1 STATE CONFLICT (runs first)

Condition: both `state` and `state_gl017` are known and they disagree.

```sql
SELECT id, artifact_name, artifact_type, state, state_gl017, owner_decision
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND state_gl017 IS NOT NULL
  AND state != state_gl017
ORDER BY id ASC;
```

Current live rows in this bucket: ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59.
**OD-3 open:** these rows are surfaced without auto-classification until OD-3 (state
conflict precedence) is resolved.

### 4.2 NOT CLASSIFIABLE — unknown state_gl017

Condition: `state_gl017 IS NULL`. Cannot determine conflict or agreement.

```sql
SELECT id, artifact_name, artifact_type, state, owner_decision
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND state_gl017 IS NULL
ORDER BY id ASC;
```

Label in output: `[NOT CLASSIFIABLE — state_gl017 unknown]`

### 4.3 NOT CLASSIFIABLE — unknown owner_decision value

Condition: `owner_decision` is not NULL and not in the known enum
(`confirmed`, `deferred`, `rejected`), and row is not already in STATE CONFLICT.

```sql
SELECT id, artifact_name, artifact_type, state, owner_decision
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND state_gl017 IS NOT NULL
  AND state = state_gl017
  AND owner_decision IS NOT NULL
  AND owner_decision NOT IN ('confirmed', 'deferred', 'rejected')
ORDER BY id ASC;
```

Label in output: `[NOT CLASSIFIABLE — owner_decision value not in enum]`

### 4.4 Open Execution

Excluded from STATE CONFLICT (only rows where state = state_gl017 or state_gl017 IS NULL
are eligible — but STATE CONFLICT rows are already separated above, so this is clean).

```sql
SELECT id, artifact_name, artifact_type, state, owner_decision_at,
       registered_at,
       CASE
         WHEN state = 'ready' AND registered_at IS NOT NULL
              AND julianday('now') - julianday(registered_at) >= 7
         THEN '[OVERDUE]'
         WHEN state = 'ready' AND registered_at IS NOT NULL
         THEN '[WITHIN THRESHOLD]'
         ELSE ''
       END AS urgency
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND owner_decision = 'confirmed'
  AND processed_at IS NULL
  AND NOT (state_gl017 IS NOT NULL AND state != state_gl017)
ORDER BY registered_at ASC;
```

### 4.5 Carry-Forward

OD-2 resolved 2026-06-15: Carry-Forward = `owner_decision IS NULL` AND `state IN ('active', 'ready')`.

```sql
SELECT id, artifact_name, artifact_type, state, registered_at,
       CAST(julianday('now') - julianday(registered_at) AS INTEGER) AS days_open
FROM deliverable_lifecycle
WHERE state IN ('active', 'ready')
  AND owner_decision IS NULL
  AND NOT (state_gl017 IS NOT NULL AND state != state_gl017)
  AND state_gl017 IS NOT NULL
ORDER BY registered_at ASC;
```

### 4.6 Deferred

```sql
SELECT id, artifact_name, artifact_type, state, owner_decision_at, registered_at,
       CAST(julianday('now') - julianday(registered_at) AS INTEGER) AS days_open,
       CASE
         WHEN state = 'ready' AND registered_at IS NOT NULL
              AND julianday('now') - julianday(registered_at) >= 7
         THEN '[OVERDUE]'
         WHEN state = 'ready' AND registered_at IS NOT NULL
         THEN '[WITHIN THRESHOLD]'
         ELSE ''
       END AS urgency
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND owner_decision = 'deferred'
  AND NOT (state_gl017 IS NOT NULL AND state != state_gl017)
ORDER BY registered_at ASC;
```

### 4.7 Excluded

No live rows currently (`owner_decision = 'rejected'` not present in sweep-relevant rows).
Section shown as empty in output.

```sql
SELECT id, artifact_name, artifact_type, state, owner_decision_at
FROM deliverable_lifecycle
WHERE state NOT IN ('archived', 'closed')
  AND owner_decision = 'rejected'
  AND NOT (state_gl017 IS NOT NULL AND state != state_gl017)
ORDER BY id ASC;
```

### 4.8 Not-blocker

No structured `owner_decision` value defined for this category. Section shown as
`— no items — (pending OD resolution)` until a structured value is defined.

---

## 5. Category Priority and De-duplication

### LC Sweep

Priority order: Urgent > Graduation Candidate > Overdue for Triage > Stalled at Triaged > Pending.

A row is assigned to the first category it matches. Remaining rows not matching any
named category route to NOT CLASSIFIABLE (except CONFLICT which runs independently).

### DL Sweep

STATE CONFLICT runs first. Any row with `state_gl017 IS NOT NULL AND state != state_gl017`
is placed in STATE CONFLICT and excluded from all named category queries.

Rows with `state_gl017 IS NULL` are placed in NOT CLASSIFIABLE (unknown) and excluded
from named category queries.

Within named categories: a structured `owner_decision` value (`confirmed`, `deferred`,
`rejected`) takes precedence over Carry-Forward (NULL). Open Execution is evaluated
before Carry-Forward.

---

## 6. OVERDUE Urgency Attribute (DL)

Applied inline per item in any DL named category where `state = 'ready'`:
- `[OVERDUE]` — `registered_at IS NOT NULL` AND `julianday('now') - julianday(registered_at) >= 7`
- `[WITHIN THRESHOLD]` — `registered_at IS NOT NULL` AND `julianday('now') - julianday(registered_at) < 7`
- No attribute — `registered_at IS NULL`

---

## 7. Output Assembly Format

### LC Output

```
Learning Candidate Lifecycle Sweep — [date]
[X] items in scope

URGENT:
| # | LC-ID | Title | Flagged by | Flagged on | Status |
— no items — (if empty)

GRADUATION CANDIDATE:
| # | LC-ID | Title | Flagged by | Flagged on | Status |
— no items — (if empty)

OVERDUE FOR TRIAGE (action required this session):
| # | LC-ID | Title | Flagged by | Flagged on | Days |
— no items — (if empty)

STALLED AT TRIAGED:
| # | LC-ID | Title | Triaged on | Days waiting |
— no items — (if empty)

PENDING (informational):
| # | LC-ID | Title | Flagged on | Days |
— no items — (if empty)

[CONFLICT — requires verification]:
— no items — (if empty)

[NOT CLASSIFIABLE]:
— no items — (if empty)
```

### DL Output

```
Deliverable Lifecycle Sweep — [date]
[X] items in scope

OPEN EXECUTION (confirmed — awaiting processing completion):
| # | ID | Artifact | Type | Confirmed on | Urgency |
— no items — (if empty)

CARRY-FORWARD (on radar — no formal decision):
| # | ID | Artifact | Type | Days open |
— no items — (if empty)

DEFERRED (Owner said later):
| # | ID | Artifact | Type | Days open | Deferred on | Urgency |
— no items — (if empty)

EXCLUDED (out of scope by Owner decision):
| # | ID | Artifact | Type | Excluded on |
— no items — (if empty)

NOT-BLOCKER (informational):
— no items — (pending OD resolution for structured value)

[STATE CONFLICT — requires verification] (OD-3 open):
| # | ID | Artifact | state | state_gl017 | owner_decision |
— no items — (if empty)

[NOT CLASSIFIABLE]:
| # | ID | Artifact | Reason |
— no items — (if empty)
```

---

## 8. OD-3 Blocker Note

STATE CONFLICT section for DL sweep surfaces 13 rows without classifying them
(ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59).

**OD-3 (open):** State conflict precedence — which field governs when `state` and
`state_gl017` disagree on the same row? Until OD-3 is resolved:
- Rows remain in STATE CONFLICT section.
- No auto-classification of these rows.
- No state corrections executed.

When OD-3 is resolved, the precedence rule will be embedded in the runner and the
design updated to v02.

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-runner-design-v01.md*
