# Deliverable Lifecycle Phase 1 — Smoke Test / Operational Validation Proposal

**Status:** Proposal only. No execution until Owner authorizes.
**Date:** 2026-06-07
**Author:** Larry

---

## Test Scope

Validates the Phase 1 implementation of the Deliverable Lifecycle as built in this session.

**In scope:**
- `deliverable_lifecycle` table in `team-knowledge.db`: existence and schema
- Safe insertion of temporary test records with `[SMOKE TEST]` marker
- Detection by the Deliverables pending count query in `/close-session` Step 1
- Sweep behavior for a record with `state = 'ready'` and `registered_at` older than 7 days
- Sweep behavior for a deferred record regardless of age
- All 4 Owner decision paths: confirm, defer, reject, correct
- State and field update behavior per decision
- `team_tasks` row insertion on confirm
- Cleanup of all test records
- Confirmation that personal routines contain no Deliverable Lifecycle logic
- Confirmation that no real deliverables are archived, extracted, or moved

**Out of scope:**
- Phase 2 automation (physical archiving, file movement, extraction)
- Any system file modifications
- Any personal routine modifications
- Any real deliverable processing

---

## Schema Under Test

Table: `deliverable_lifecycle` in `Team Knowledge/team-knowledge.db`

| # | Column | Type | NOT NULL | Default |
|---|---|---|---|---|
| 1 | `id` | INTEGER | — | PRIMARY KEY |
| 2 | `artifact_name` | TEXT | yes | — |
| 3 | `artifact_type` | TEXT | yes | — |
| 4 | `state` | TEXT | yes | `'ready'` |
| 5 | `proposed_destination` | TEXT | — | — |
| 6 | `destination_domain` | TEXT | — | — |
| 7 | `processing_notes` | TEXT | — | — |
| 8 | `superseded_by` | TEXT | — | — |
| 9 | `source_session` | TEXT | — | — |
| 10 | `agent` | TEXT | — | — |
| 11 | `registered_at` | TEXT | yes | `CURRENT_TIMESTAMP` |
| 12 | `state_changed_at` | TEXT | — | — |
| 13 | `processed_at` | TEXT | — | — |
| 14 | `owner_decision` | TEXT | — | — |
| 15 | `owner_decision_at` | TEXT | — | — |

---

## Test Steps

### Step 1 — Schema Verification (read-only)

Query `PRAGMA table_info(deliverable_lifecycle)` on `team-knowledge.db`.

**Expected result:** 15 columns. Column names, types, NOT NULL flags, and defaults match the table above exactly. No extra columns. No missing columns.

---

### Step 2 — Existing Records Baseline (read-only)

Count total rows in `deliverable_lifecycle`. Record the count and the distribution of `state` values.

**Expected result:** 21 rows. All have `state = 'ready'` or `state = 'active'`. No rows with `state = 'archived'`. Baseline recorded; no changes made.

---

### Step 3 — Deliverables Pending Count Query (read-only)

Run the count query as defined in `/close-session` Step 1:

```sql
SELECT COUNT(*) FROM deliverable_lifecycle
WHERE state = 'ready'
AND (
    registered_at < datetime('now', '-7 days')
    OR owner_decision = 'deferred'
)
```

**Expected result:** Returns a count greater than 0, reflecting the real `ready` records older than 7 days already in the table. This count is the pre-test baseline.

---

### Step 4 — Test Record A: Old Ready (write)

Insert one test record:

| Field | Value |
|---|---|
| `artifact_name` | `[SMOKE TEST] Artifact A — old ready — delete after validation` |
| `artifact_type` | `smoke-test` |
| `state` | `ready` |
| `registered_at` | `datetime('now', '-8 days')` |
| `proposed_destination` | `no real destination` |
| `destination_domain` | `Core` |
| `source_session` | `2026-06-07-smoke-test` |
| `agent` | `larry` |

**Expected result:** INSERT succeeds. Row retrievable. `registered_at` is 8 days in the past. Count is now baseline + 1.

---

### Step 5 — Deliverables Pending Detection (read-only)

Re-run the count query from Step 3.

**Expected result:** Count is baseline + 1. Record A is detected because `state = 'ready'` AND `registered_at < datetime('now', '-7 days')`.

---

### Step 6 — Sweep Display Verification (read-only)

Run the full sweep query as defined in `/close-session` Step 3c:

```sql
SELECT id, artifact_name, artifact_type, proposed_destination,
       CAST(julianday('now') - julianday(registered_at) AS INTEGER) AS days_open
FROM deliverable_lifecycle
WHERE state = 'ready'
AND (
    registered_at < datetime('now', '-7 days')
    OR owner_decision = 'deferred'
)
ORDER BY days_open DESC
```

**Expected result:** Record A appears in the result set. All 5 selected fields are populated. `days_open` = 8. Real records also appear; no real record is modified.

---

### Step 7 — Owner Decision: Confirm (write)

Apply the `confirm` decision to Record A:

```sql
UPDATE deliverable_lifecycle
SET owner_decision = 'confirmed',
    owner_decision_at = datetime('now')
WHERE id = <Record A id>
```

Then insert a `team_tasks` row for the processing delegation:

```sql
INSERT INTO team_tasks (title, assignee, priority, source, tags, session_id)
VALUES ('[SMOKE TEST] Process deliverable: Artifact A', 'larry', 2,
        'delegation', 'deliverable-lifecycle', '2026-06-07-smoke-test')
```

**Expected result:** `owner_decision = 'confirmed'` on Record A. `owner_decision_at` set. `state` remains `'ready'` (Phase 2 not yet implemented). `team_tasks` row inserted with SMOKE TEST marker. No other rows affected.

---

### Step 8 — Test Record B: Recent, Then Deferred (write)

Insert a second test record with a recent `registered_at` to test the deferred resurfacing path:

| Field | Value |
|---|---|
| `artifact_name` | `[SMOKE TEST] Artifact B — defer path — delete after validation` |
| `artifact_type` | `smoke-test` |
| `state` | `ready` |
| `registered_at` | `datetime('now')` (today) |
| `source_session` | `2026-06-07-smoke-test` |
| `agent` | `larry` |

Confirm Record B does NOT appear in the sweep (too recent — less than 7 days old, no prior defer decision).

Then apply the `defer` decision:

```sql
UPDATE deliverable_lifecycle
SET owner_decision = 'deferred',
    owner_decision_at = datetime('now')
WHERE id = <Record B id>
```

Re-run the sweep query.

**Expected result:** Before defer: Record B absent from sweep. After defer: Record B surfaces via the `OR owner_decision = 'deferred'` path despite being less than 7 days old. `state` remains `'ready'`. No other rows affected.

---

### Step 9 — Test Record C: Reject (write)

Insert a third test record:

| Field | Value |
|---|---|
| `artifact_name` | `[SMOKE TEST] Artifact C — reject path — delete after validation` |
| `artifact_type` | `smoke-test` |
| `state` | `ready` |
| `registered_at` | `datetime('now', '-8 days')` |
| `source_session` | `2026-06-07-smoke-test` |
| `agent` | `larry` |

Apply the `reject` decision:

```sql
UPDATE deliverable_lifecycle
SET owner_decision = 'rejected',
    state = 'archived',
    state_changed_at = datetime('now'),
    owner_decision_at = datetime('now')
WHERE id = <Record C id>
```

Re-run the sweep query.

**Expected result:** `state = 'archived'` on Record C. `owner_decision = 'rejected'`. `state_changed_at` set. Record C no longer appears in the sweep (excluded because `state != 'ready'`). No other rows affected.

---

### Step 10 — Test Record D: Correct (write)

Insert a fourth test record:

| Field | Value |
|---|---|
| `artifact_name` | `[SMOKE TEST] Artifact D — correct path — delete after validation` |
| `artifact_type` | `smoke-test` |
| `state` | `ready` |
| `registered_at` | `datetime('now', '-8 days')` |
| `source_session` | `2026-06-07-smoke-test` |
| `agent` | `larry` |

Apply the `correct` decision with a correction note:

```sql
UPDATE deliverable_lifecycle
SET processing_notes = '[SMOKE TEST] Correction note: proposed destination corrected',
    owner_decision_at = datetime('now')
WHERE id = <Record D id>
```

**Expected result:** `processing_notes` updated. `owner_decision_at` set. `state` unchanged (`'ready'`). `owner_decision` column remains NULL (correct — `correct` path does not write `owner_decision`). Record D remains in sweep (still `state = 'ready'` and older than 7 days). No other rows affected.

---

### Step 11 — Personal Routine Verification (read-only)

Search the following skill files for any Deliverable Lifecycle references (keywords: `deliverable_lifecycle`, `DL pending`, `Step 3c`):

- `/opt/myPKA/.claude/commands/close-morning-routine.md`
- `/opt/myPKA/.claude/commands/start-morning-routine.md`
- `/opt/myPKA/.claude/commands/start-daily-planning.md`
- `/opt/myPKA/.claude/commands/start-afternoon-routine.md`
- `/opt/myPKA/.claude/commands/close-afternoon-routine.md`

**Expected result:** No Deliverable Lifecycle references found in any personal routine. Deliverable Lifecycle logic is present only in `/close-session`.

---

### Step 12 — Real Deliverable Integrity Check (read-only)

Query:
```sql
SELECT COUNT(*), state FROM deliverable_lifecycle
WHERE artifact_name NOT LIKE '%SMOKE TEST%'
GROUP BY state
```

**Expected result:** 21 real records. State distribution unchanged from Step 2 baseline. No real record has `owner_decision` set or `state` changed.

---

### Step 13 — Cleanup (write)

Delete all test records:

```sql
DELETE FROM deliverable_lifecycle
WHERE artifact_name LIKE '[SMOKE TEST]%'
```

Delete the test `team_tasks` row:

```sql
DELETE FROM team_tasks
WHERE title LIKE '[SMOKE TEST]%'
AND source = 'delegation'
AND tags = 'deliverable-lifecycle'
```

**Expected result:** 0 rows remain with `[SMOKE TEST]` prefix in `artifact_name`. Total count in `deliverable_lifecycle` returns to 21. No test `team_tasks` rows remain. Schema unchanged.

> **Note:** Use `[SMOKE TEST]%` (bracket-prefix), not `%SMOKE TEST%` (substring). SQLite `LIKE` is case-insensitive for ASCII — the substring pattern would also match real deliverable records whose folder names contain "Smoke Test". The bracket-prefix matches only records explicitly marked during the smoke test.

---

## Expected Results Summary

| Step | Area | Expected |
|---|---|---|
| 1 | Schema | 15 columns match exactly |
| 2 | Baseline | 21 records, state distribution recorded |
| 3 | Count query | Returns count > 0 (real ready records detected) |
| 4 | Insert Record A | Row inserted, `registered_at` = 8 days ago |
| 5 | Detection | Count = baseline + 1 |
| 6 | Sweep display | Record A surfaces, `days_open` = 8, all fields populated |
| 7 | Confirm | `owner_decision = 'confirmed'`, `team_tasks` row created |
| 8 | Defer | Record B absent before defer, surfaces after defer |
| 9 | Reject | `state = 'archived'`, Record C absent from sweep |
| 10 | Correct | `processing_notes` set, Record D still in sweep |
| 11 | Personal routines | No Deliverable Lifecycle references found |
| 12 | Real integrity | 21 real records unchanged |
| 13 | Cleanup | 0 SMOKE TEST rows, count = 21 |

---

## Required Owner Authorization

**Read-only steps (1, 2, 3, 5, 6, 11, 12):** No write authorization required.

**Write steps (4, 7, 8, 9, 10, 13):** Require explicit Owner authorization before execution.

The Owner may authorize all write steps in one confirmation before execution begins.

---

## Owner Answer Format

The Owner answers with exactly one of:

- **Yes** — execute all steps in sequence, cleanup included
- **No** — do not execute
- **Correction** — adjust this proposal before execution

No open questions will be asked during execution. Every write step is fully specified above. Cleanup (Step 13) is unconditional — it runs regardless of intermediate step outcomes.

---

## Rollback / Cleanup Plan

All test records carry `[SMOKE TEST]` in `artifact_name`. The `team_tasks` test row carries `[SMOKE TEST]` in `title`.

**Primary cleanup (Step 13):**
```sql
DELETE FROM deliverable_lifecycle WHERE artifact_name LIKE '[SMOKE TEST]%';
DELETE FROM team_tasks WHERE title LIKE '[SMOKE TEST]%' AND tags = 'deliverable-lifecycle';
```

**Fallback (if execution fails midway):** Run the two DELETE statements above directly on `team-knowledge.db`.

> **Note:** Use `[SMOKE TEST]%` (bracket-prefix), not `%SMOKE TEST%`. The substring pattern is case-insensitive and will match real deliverable records containing "Smoke Test" anywhere in their name.

No schema changes occur at any point. No files in `Deliverables/` are modified, moved, or deleted. No personal routine skill files are modified. The smoke test is fully contained to temporary rows in `deliverable_lifecycle` and one row in `team_tasks`.

---

Delivered on: 2026-06-07
Delivered at: 2026-06-07
