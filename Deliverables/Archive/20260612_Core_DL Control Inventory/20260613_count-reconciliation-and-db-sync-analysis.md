# DL Control: Count Reconciliation and DB Sync Analysis

**Date:** 2026-06-13
**Session:** session_logs id 210 continued
**Scope:** Read-only inventory reconciliation — no writes, no archive actions

---

## 1. Count mismatch: 24 active D-folders vs 48 non-archived DB rows

The two numbers measure different things.

- **24** = physical folders currently on disk in `Deliverables/` (not in `Archive/`)
- **48** = DB rows in `deliverable_lifecycle` where `state != 'archived'` after applying all known exclusions (IDs 2, 3, 6, 7, 8, 18, 19, 45, 46, 60, 61, 62, 63, 67, 68 and the source deliverable `20260530_Core_UMC diagnose en aanbevelingen`)
- **64** = total non-archived rows before exclusions

The gap is explained by a single root cause: **the DB `state` column was never updated after physical archive actions were executed.** 28 items have been physically moved to `Deliverables/Archive/` but their DB `state` still reads `ready` or `active`.

---

## 2. Reliable classification field: `state_gl017`

The `state` column in `deliverable_lifecycle` does not reflect physical archive reality. The `state_gl017` column is accurate.

Cross-check result:

| state_gl017 value | DB row count | Physical location |
|---|---|---|
| `active` | 8 | ACTIVE_FOLDER (on disk) |
| `pending_lifecycle_decision` | 16 | ACTIVE_FOLDER (on disk) |
| `archived` | 40 | IN_ARCHIVE or NO_FOLDER |

8 + 16 = **24 — exact match with physical active folder count.**

All 40 rows with `state_gl017=archived` have no active physical folder. 39 are confirmed in `Deliverables/Archive/`; 1 is unlocated (see section 5).

---

## 3. DB state sync gap: 28 items

The following 28 items have `state_gl017=archived`, physical folder confirmed in `Deliverables/Archive/`, but DB `state != 'archived'`:

IDs: 4, 9, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 43, 44, 47, 48, 49, 51, 54, 64, 65, 66, 70, 71

**This is a DB sync task, not an archive proposal.** The physical action is already complete. What is missing is setting `state='archived'` and `state_changed_at` on each of these rows.

---

## 4. Archive proposals eligible now: zero

After full reconciliation and exclusion of all Category D items, retain items, and items without an owner decision, zero items are eligible for a new archive proposal at this time. Breakdown:

| Group | Count | Reason not eligible |
|---|---|---|
| DB sync needed (already in Archive) | 28 | Physical action done — DB update required, not archive |
| Category D (pending_lifecycle_decision) | 12 | No lifecycle decision made |
| Retain decision on record | 2 | Owner decided retain |
| Active D-folder, no decision | 4 | No archive decision made |
| Review required | 2 | Special cases (IDs 53 and 72) |
| **Total** | **48** | |

---

## 5. Special cases requiring resolution before any action

**ID 72 — 20260612_Core_DL Batch 2 Process Artifacts Archive Proposal**
- `state_gl017=archived`, but physical folder not found in active `Deliverables/` or in `Deliverables/Archive/`
- `owner_decision` records a misclassification: "G2 artifact, file moved to 20260612_Core_DL Control Inventory"
- Physical location of the file must be verified before any DB update is applied to this row

**ID 53 — 20260608_Core_DL Granularity Assessment**
- `state_gl017=active`, physical folder present on disk
- `owner_decision`: "Owner approved v02 for implementation 2026-06-08"
- DB notes confirm implementation is complete, but DB `state` remains `active`
- May be archive-eligible, but requires explicit Owner decision before any state change

---

## 6. Next possible write action

A DB state sync write plan for the 28 confirmed items (section 3).

This is not archive execution. It is a DB update only: `SET state='archived', state_changed_at=datetime('now')` for each of the 28 IDs. No folder moves. No new archive actions.

Write plan must be persisted as a file before Owner authorization is requested. ID 72 must be verified before inclusion or explicit exclusion from the sync plan.

---

Delivered on: 2026-06-13
Delivered at: Deliverables/20260612_Core_DL Control Inventory/
