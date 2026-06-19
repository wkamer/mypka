# Write Plan — lifecycle-sweep-model-design-v02.md

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
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
| `flagged_at` / `max_days_captured` column for Stalled at Triaged | `threshold — see OD-1` | `triaged_at >= 7 calendar days AND processed_at IS NULL` |

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

After writing `lifecycle-sweep-model-design-v02.md`, verify all of the following before proceeding:

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-v02.md` present on disk |
| V-2 | File size > 0 | Non-empty file |
| V-3 | v01 untouched | `lifecycle-sweep-model-design-v01.md` is byte-identical to its pre-write state |
| V-4 | Header says v02 supersedes v01 | First section of v02 contains supersession declaration |
| V-5 | OD-1 threshold = 7 calendar days | Section 8 resolved decisions contains `7 calendar days` |
| V-6 | MAC-LC-4 active | Section 7 MAC-LC-4 row contains active criterion, no `[THRESHOLD NOT DEFINED]` text |
| V-7 | OD-2 still open | Section 8 open decisions still contains OD-2 |

All 7 criteria must pass. Any failure = stop, report to Owner before proceeding.

---

## 6. Lifecycle Artifact Handling for v02

`deliverable_lifecycle` row id 73 covers the D-folder `20260615_Core_Lifecycle Sweep Model Design/`.
v02 is a G2 artifact (new file inside an existing G1 folder).
The Deliverable Lifecycle rules require INSERT only at G1 folder creation.

**Decision:** No new `deliverable_lifecycle` INSERT for v02. No UPDATE to row id 73 is mandated by the rules.

If Owner instructs otherwise: execute per instruction, log as deviation.

---

## 7. team_tasks 96 — Close Condition

`UPDATE team_tasks SET status='completed', completed_at=datetime('now') WHERE id=96`

**Executed only when:**
1. All 7 file verification criteria pass (Section 5), AND
2. Lifecycle artifact handling is confirmed (Section 6 — no INSERT, no UPDATE)

If any verification criterion fails: do not close task 96. Report to Owner.

---

## 8. Explicit Exclusions

The following actions are out of scope for this write plan. None of these will be performed:

- No new D-folder creation
- No schema changes
- No cleanup actions
- No archiving actions
- No governance amendments
- No dashboard work
- No other lifecycle updates beyond what is stated in Sections 6 and 7
- No writes to `deliverable_lifecycle`
- No writes to `team_tasks` (other than id 96 after verification passes)
- No changes to any other file

---

## 9. Execution Sequence (post-authorization)

1. Write `lifecycle-sweep-model-design-v02.md`
2. Verify V-1 through V-7
3. Confirm lifecycle artifact handling (no INSERT, no UPDATE)
4. SET team_tasks 96 status = 'completed'
5. Report to Owner: file path, verification results, task 96 closed

---

*Write plan persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
