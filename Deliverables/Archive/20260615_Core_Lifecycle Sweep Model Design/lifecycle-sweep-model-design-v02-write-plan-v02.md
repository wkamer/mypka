# Write Plan — lifecycle-sweep-model-design-v02.md (v02 van dit write plan)

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Supersedes:** lifecycle-sweep-model-design-v02-write-plan-v01.md (Section 6 corrected)
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021

---

## 1. Objective

Produce `lifecycle-sweep-model-design-v02.md` in the existing deliverable folder, incorporating Owner decision OD-1 and activating MAC-LC-4.

---

## 2. Target File

| Field | Value |
|---|---|
| Path | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-v02.md` |
| Action | New file — v01 untouched |
| New D-folder | No |
| Source | v01 (`lifecycle-sweep-model-design-v01.md`) as base |

---

## 3. Owner Decision to Incorporate

| Code | Decision |
|---|---|
| OD-1 | Stalled-at-Triaged threshold = **7 calendar days**. A `triaged` LC with `processed_at IS NULL` and `triaged_at` >= 7 calendar days ago is classified as Stalled at Triaged. |

---

## 4. Changes from v01 to v02

Three targeted changes only. All other content carried forward verbatim.

### 4.1 Header block

| Field | v01 | v02 |
|---|---|---|
| Version | v01 | v02 |
| Status | Active | Active |
| Supersedes | — | v01 (`lifecycle-sweep-model-design-v01.md`) |
| Predecessor | Chat-only design session 2026-06-15 | v01 + OD-1 Owner decision 2026-06-15 |

### 4.2 Section 2.2 — Field Mapping (Stalled at Triaged row)

| Field | v01 | v02 |
|---|---|---|
| threshold column for Stalled at Triaged | `threshold — see OD-1` | `triaged_at >= 7 calendar days AND processed_at IS NULL` |

### 4.3 Section 7 — MAC-LC-4

| Field | v01 | v02 |
|---|---|---|
| MAC-LC-4 criterion | `Stalled at Triaged is inactive and shown as [THRESHOLD NOT DEFINED — INACTIVE] until OD-1 is resolved` | `Stalled at Triaged contains items with status = 'triaged' AND processed_at IS NULL AND triaged_at >= 7 calendar days ago. Shown as active. Items ordered by triaged_at ascending.` |

### 4.4 Section 8 — Open Owner Decisions

- OD-1 moved from Open to Resolved:

| Code | Decision | Resolution |
|---|---|---|
| OD-1 | Stalled-at-Triaged threshold | 7 calendar days. Owner confirmed 2026-06-15. |

- OD-2 remains open, unchanged from v01.

---

## 5. File Verification Criteria

After writing `lifecycle-sweep-model-design-v02.md`, verify all of the following before proceeding to any DB write:

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-v02.md` present on disk |
| V-2 | File size > 0 | Non-empty file |
| V-3 | v01 untouched | `lifecycle-sweep-model-design-v01.md` is byte-identical to its pre-write state |
| V-4 | Header says v02 supersedes v01 | First section of v02 contains supersession declaration |
| V-5 | OD-1 threshold = 7 calendar days | Section 8 resolved decisions contains `7 calendar days` |
| V-6 | MAC-LC-4 active | Section 7 MAC-LC-4 row contains active criterion, no `[THRESHOLD NOT DEFINED]` text |
| V-7 | OD-2 still open | Section 8 open decisions still contains OD-2 |

All 7 criteria must pass. Any failure = stop, report to Owner before any DB write.

---

## 6. Lifecycle Artifact Handling for v02

### 6.1 Confirmed semantics

`deliverable_lifecycle` registers artifacts, not folders. Row id 73 registers the artifact
`lifecycle-sweep-model-design-v01`. It does not cover v02.

### 6.2 Precedent from live DB

| id | artifact_name | state | owner_decision |
|---|---|---|---|
| 66 | 20260608_Core_Phase 1 Proposal R1 R5 v01 | archived | archive |
| 68 | 20260608_Core_Phase 1 Proposal R1 R5 v02 | archived | Archived in Batch 2... |

v01 and v02 of the same document are registered as separate rows. This is the established
pattern in `deliverable_lifecycle`.

### 6.3 The `superseded_by` field

`superseded_by TEXT` exists in the `deliverable_lifecycle` schema. It is currently NULL on
row id 73. This field is designed to link a superseded artifact to its successor.

### 6.4 Conclusion

A separate row for v02 is required. Row id 73 (v01) must also be updated to record that it
is superseded.

### 6.5 Planned DB actions (post file-verification, in sequence)

**Action A — INSERT new row for v02**

```sql
INSERT INTO deliverable_lifecycle (
    artifact_name, artifact_type, state, destination_domain,
    state_gl017, workstream_code, registered_at
) VALUES (
    'lifecycle-sweep-model-design-v02',
    'proposal',
    'active',
    'core',
    'active',
    NULL,
    datetime('now')
);
```

**Action B — UPDATE id 73 to record supersession**

```sql
UPDATE deliverable_lifecycle
SET superseded_by = 'lifecycle-sweep-model-design-v02',
    state = 'archived',
    state_changed_at = datetime('now')
WHERE id = 73;
```

Note on Action B: the state transition for id 73 (`active` → `archived`) follows the
precedent of id 66 (v01 archived when v02 exists). This is a proposed state. If Owner
prefers a different state value for superseded artifacts, Action B must be corrected before
execution.

**Action C — Close team_tasks 96**

```sql
UPDATE team_tasks
SET status = 'completed', completed_at = datetime('now')
WHERE id = 96;
```

Executed only after V-1 through V-7 all pass AND Actions A and B succeed.

### 6.6 Execution sequence

1. All 7 file verification criteria pass
2. Action A (INSERT v02 row)
3. Action B (UPDATE id 73 superseded_by + state)
4. Action C (close team_tasks 96)
5. Report to Owner: file path, verification results, new row id, id 73 updated, task 96 closed

If any step fails: stop at that step, report exact failure, do not proceed to subsequent steps.

---

## 7. Explicit Exclusions

The following actions are out of scope. None will be performed:

- No new D-folder creation
- No schema changes
- No cleanup actions
- No archiving actions beyond Action B state update on id 73
- No governance amendments
- No dashboard work
- No other lifecycle updates
- No writes to any table other than `deliverable_lifecycle` (Actions A and B) and `team_tasks` (Action C)
- No changes to any file other than the new v02 file

---

*Write plan v02 persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
