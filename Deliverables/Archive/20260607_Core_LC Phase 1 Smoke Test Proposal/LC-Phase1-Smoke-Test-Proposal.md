# LC Phase 1 Smoke Test — Operational Validation Proposal

**Status:** Proposal only. No execution until Owner authorizes.
**Date:** 2026-06-07
**Author:** Larry
**Related:** [[GL-022_Learning Candidate Lifecycle]], [[SOP-019_Governance Gate Protocol]]

---

## Test Scope

Validates Phase 1 implementation of GL-022 Learning Candidate Lifecycle as delivered in W-1 through W-5.

**In scope:**
- learning_candidates table: existence, schema, accessibility
- Insertion and retrieval of one temporary test record
- /close-session LC scan detection behavior
- Overdue candidate surfacing behavior
- Owner decision handling: approve, reject, promote
- Cleanup of all test records after validation
- Confirmation that personal routines contain no LC logic

**Out of scope:**
- Phase 2 automation
- Future sweep extensions beyond /close-session
- Personal routine behavior changes
- Any system file modifications

---

## Test Steps

### Step 1 — Schema Verification (read-only)

Query `team-knowledge.db`: confirm `learning_candidates` table exists and all columns match GL-022 specification.

**Expected columns:** `id`, `candidate_text`, `source_agent`, `status`, `created_at`, `review_due`, `reviewed_at`, `decision`, `promoted_to`

**Expected result:** Table present. All 9 columns match. No extra columns. No missing columns.

---

### Step 2 — Test Record Insertion (write)

Insert one row with the following values:

| Field | Value |
|---|---|
| candidate_text | `[SMOKE TEST] Temporary test candidate — delete after validation` |
| source_agent | `larry` |
| status | `pending` |
| review_due | `2026-06-07` (today — immediately overdue) |

**Expected result:** INSERT succeeds. Row is retrievable. All field values match what was inserted.

---

### Step 3 — LC Scan Detection (read-only)

Run the LC scan query as defined in /close-session: retrieve rows where `status = 'pending'` and `review_due <= today`.

**Expected result:** The test record from Step 2 appears in the result set.

---

### Step 4 — Surfacing Behavior Verification (read-only)

Confirm the overdue candidate surfaces with the correct fields: `candidate_text`, `source_agent`, `created_at`, `review_due`.

**Expected result:** Output matches the surfacing format defined in GL-022. No missing fields. No extra fields.

---

### Step 5 — Owner Decision: Approve (write)

Update the test record: `status = 'approved'`, `decision = 'approved'`, `reviewed_at = datetime('now')`.

**Expected result:** Row updated correctly. `reviewed_at` is set. No other rows are affected.

---

### Step 6 — Owner Decision: Reject (write)

Insert a second test record (marker: `[SMOKE TEST] Reject path`). Update: `status = 'rejected'`, `decision = 'rejected'`, `reviewed_at = datetime('now')`.

**Expected result:** Row updated correctly. `reviewed_at` is set. No other rows are affected.

---

### Step 7 — Owner Decision: Promote (write)

Insert a third test record (marker: `[SMOKE TEST] Promote path`). Update: `status = 'promoted'`, `decision = 'promoted'`, `promoted_to = 'SOP-XXX (smoke test reference)'`, `reviewed_at = datetime('now')`.

**Expected result:** Row updated correctly. `promoted_to` field is populated. No other rows are affected.

---

### Step 8 — Personal Routine Verification (read-only)

Check the following skill files for any LC-related logic (scan, flag, surfacing):
- `/close-morning-routine`
- `/start-morning-routine`
- `/start-daily-planning`
- `/start-afternoon-routine`
- `/close-afternoon-routine`

**Expected result:** No LC references found in any personal routine skill. LC logic is present only in `/close-session`.

---

### Step 9 — Cleanup (write)

Delete all rows where `candidate_text LIKE '%SMOKE TEST%'`.

Confirm: 0 rows remain with that marker.

**Expected result:** Database restored to pre-test state. No schema changes. No file changes. No routine modifications.

---

## Expected Results Summary

| Step | Area | Expected |
|---|---|---|
| 1 | Schema | Table exists, 9 columns match GL-022 |
| 2 | Insert | Row inserted, all fields correct |
| 3 | LC scan | Test record detected as overdue |
| 4 | Surfacing | Output format matches GL-022 |
| 5 | Approve | Status updated, reviewed_at set |
| 6 | Reject | Status updated, reviewed_at set |
| 7 | Promote | Status updated, promoted_to populated |
| 8 | Personal routines | No LC references found |
| 9 | Cleanup | All SMOKE TEST rows deleted, 0 remaining |

---

## Required Owner Authorization

**Read-only steps (1, 3, 4, 8):** May proceed without separate write authorization. These steps do not modify any data or files.

**Write steps (2, 5, 6, 7, 9):** Require explicit Owner authorization before execution.

The Owner may authorize all write steps in one confirmation, or step by step. Either is acceptable.

---

## Owner Answer Format

The Owner answers with exactly one of:

- **Yes** — execute all steps in sequence, cleanup included.
- **No** — do not execute.
- **Correction** — adjust this proposal before execution.

No open questions during execution. Every write step is described above in full.

---

## Rollback / Cleanup Plan

All test records inserted during the smoke test carry the marker `[SMOKE TEST]` in `candidate_text`.

**Primary cleanup:** Step 9 deletes all such rows via `DELETE WHERE candidate_text LIKE '%SMOKE TEST%'`.

**Fallback (if execution fails midway):**
```sql
DELETE FROM learning_candidates WHERE candidate_text LIKE '%SMOKE TEST%';
```
Run this directly on `team-knowledge.db` to restore the database to pre-test state.

No schema changes occur. No files are modified. No routines are changed. The smoke test is fully contained to temporary data rows in `learning_candidates`.

---

Delivered on: 2026-06-07
Delivered at: 17:00
