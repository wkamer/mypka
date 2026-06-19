# Write Plan — lifecycle-sweep-model-design-v03.md

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021

---

## 1. Objective

Produce `lifecycle-sweep-model-design-v03.md` in the existing deliverable folder,
incorporating the accepted OD-2 resolution and registering OD-3 as a new open decision.

---

## 2. Target File

| Field | Value |
|---|---|
| Path | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-v03.md` |
| Action | New file — v02 untouched |
| Source | v02 (`lifecycle-sweep-model-design-v02.md`) as base |
| New D-folder | No |

---

## 3. Owner Decisions to Incorporate

| Code | Decision | Status |
|---|---|---|
| OD-2 | Carry-Forward = `owner_decision IS NULL` AND `state IN ('active', 'ready')` | Accepted 2026-06-15 |
| OD-3 | State conflict precedence for `deliverable_lifecycle` rows where `state` and `state_gl017` disagree | New open decision — register only, no resolution |

---

## 4. Changes from v02 to v03

Four targeted changes only. All other content carried forward verbatim from v02.

### 4.1 Header block

| Field | v02 | v03 |
|---|---|---|
| Version | v02 | v03 |
| Supersedes | v01 | v02 (`lifecycle-sweep-model-design-v02.md`) |
| Predecessor | v01 + OD-1 Owner decision 2026-06-15 | v02 + OD-2 Owner decision 2026-06-15 |

### 4.2 Section 3.2 — Field Mapping (Carry-Forward row)

| Field | v02 | v03 |
|---|---|---|
| `owner_decision` column for Carry-Forward | `NULL or unknown` | `IS NULL` |
| Notes column for Carry-Forward | `See OD-2 — no confirmed structured value yet` | `OD-2 resolved: NULL = no formal Owner decision` |

### 4.3 Section 7 — MAC-DL-2

| Field | v02 | v03 |
|---|---|---|
| MAC-DL-2 criterion | `Carry-Forward shown as [REQUIRES VERIFICATION — OD-2 OPEN] until OD-2 is resolved` | `Carry-Forward contains items with owner_decision IS NULL AND state IN ('active', 'ready'). Shown as active. Items ordered by registered_at ascending.` |

### 4.4 Section 8 — Owner Decisions

- OD-2 moved from Open to Resolved:

| Code | Decision | Resolution |
|---|---|---|
| OD-2 | Carry-Forward structure | `owner_decision IS NULL` AND `state IN ('active', 'ready')`. No new value, no schema change. Owner confirmed 2026-06-15. |

- OD-3 added as new open decision:

| Code | Decision | Blocks |
|---|---|---|
| OD-3 | State conflict precedence: which field governs when `state` and `state_gl017` disagree on the same row? Without a precedence rule, 13 rows cannot be auto-classified. | STATE CONFLICT resolution for ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59 |

---

## 5. File Verification Criteria

After writing `lifecycle-sweep-model-design-v03.md`, verify all before any DB write:

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | `lifecycle-sweep-model-design-v03.md` present on disk |
| V-2 | Size > 0 | Non-empty file |
| V-3 | v02 untouched | `lifecycle-sweep-model-design-v02.md` present and unmodified (15,351 bytes) |
| V-4 | Header declares v03 supersedes v02 | First section contains supersession declaration referencing v02 |
| V-5 | Section 3.2 Carry-Forward owner_decision = IS NULL | Text `IS NULL` in Carry-Forward field mapping row |
| V-6 | MAC-DL-2 active — no REQUIRES VERIFICATION text | MAC-DL-2 row contains active criterion, no `[REQUIRES VERIFICATION` text |
| V-7 | OD-2 in Resolved section | Section 8 resolved decisions contains OD-2 with `owner_decision IS NULL` |
| V-8 | OD-3 in Open section | Section 8 open decisions contains OD-3 with state conflict precedence |

All 8 criteria must pass. Any failure = stop, report to Owner before any DB write.

---

## 6. Lifecycle Artifact Handling for v03

### 6.1 Confirmed semantics

`deliverable_lifecycle` registers artifacts, not folders. Row id 74 registers
`lifecycle-sweep-model-design-v02`. It does not cover v03.

### 6.2 Precedent

Separate rows for versioned artifacts: ids 66/68 (v01/v02 of Phase 1 Proposal) and
ids 73/74 (v01/v02 of Lifecycle Sweep Model Design). A separate INSERT for v03 is required.

### 6.3 Planned DB actions (post file-verification, in sequence)

**Action A — INSERT new row for v03**

```sql
INSERT INTO deliverable_lifecycle (
    artifact_name, artifact_type, state, destination_domain,
    state_gl017, workstream_code, registered_at
) VALUES (
    'lifecycle-sweep-model-design-v03',
    'proposal',
    'active',
    'core',
    'active',
    NULL,
    datetime('now')
);
```

**Action B — UPDATE id 74: superseded_by only, no state change**

```sql
UPDATE deliverable_lifecycle
SET superseded_by = 'lifecycle-sweep-model-design-v03'
WHERE id = 74;
```

State of id 74 (`active`) remains unchanged. Any state transition for superseded artifacts
requires a separate explicit Owner decision.

**Action C — Close team_tasks 97**

```sql
UPDATE team_tasks
SET status = 'completed', completed_at = datetime('now')
WHERE id = 97;
```

Executed only after V-1 through V-8 all pass AND Actions A and B succeed.

### 6.4 Execution sequence

1. All 8 file verification criteria pass
2. Action A (INSERT v03 row)
3. Action B (UPDATE id 74 superseded_by only)
4. Action C (close team_tasks 97)
5. Report to Owner: file path, verification results, new row id, id 74 superseded_by set, task 97 closed

If any step fails: stop at that step, report exact failure, do not proceed to subsequent steps.

---

## 7. Explicit Exclusions

| Exclusion |
|---|
| No new D-folder |
| No schema changes |
| No cleanup actions |
| No archiving actions |
| No state change on id 74 or any other row |
| No corrections to the 13 STATE CONFLICT rows |
| No governance amendments |
| No dashboard work |
| No writes beyond Actions A, B, C above |
| No changes to any file other than the new v03 file |

---

*Write plan persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
