# Write Plan — OD-2 Owner Decision Mapping Proposal

**Document type:** Write plan — governance artifact
**Status:** Pending Owner authorization
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Governing rule:** Governance Deliverable File-First Rule (CLAUDE.md) + GL-021

---

## 1. Objective

Produce a persisted OD-2 mapping proposal artifact that:
- Maps all live `owner_decision` values to DL sweep categories
- Proposes the OD-2 resolution for Carry-Forward classification
- Surfaces STATE CONFLICT and NOT CLASSIFIABLE items for Owner awareness
- Does not execute any DB changes

---

## 2. Target File

| Field | Value |
|---|---|
| Path | `Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-od2-owner-decision-mapping-v01.md` |
| Action | New file |
| New D-folder | No |
| DB changes | None — proposal artifact only |

---

## 3. Input Data

### 3.1 Sweep-relevant rows

Rows where `state NOT IN ('archived', 'closed')`. Total: 27.

### 3.2 Live owner_decision values and counts

| Value | Count |
|---|---|
| `archived_cleanup_no_active_need` | 12 |
| `deferred` | 8 |
| NULL | 4 |
| `retain` | 1 |
| `accepted_done` | 1 |
| free-text (`misclassified GL-017: G2 artifact, file moved to 20260612_Core_DL Control Inventory`) | 1 |

### 3.3 Affected row ids per value

| Value | Row ids |
|---|---|
| `archived_cleanup_no_active_need` | 10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59 |
| `deferred` | 5, 12, 18, 19, 45, 46, 58, 67 |
| NULL | 52, 69, 73, 74 |
| `retain` | 50 |
| `accepted_done` | 14 |
| free-text | 72 |

---

## 4. Proposed Content of the Mapping Proposal Artifact

The proposal artifact (`lifecycle-sweep-model-design-od2-owner-decision-mapping-v01.md`)
will contain the following sections.

### Section 1 — OD-2 Question

> Is Carry-Forward a structured `owner_decision` value, an annotation in `processing_notes`,
> or defined by NULL `owner_decision`? Without this, Carry-Forward cannot be auto-classified.

### Section 2 — Proposed OD-2 Resolution

**Proposal:** Carry-Forward = `owner_decision IS NULL` AND `state IN ('active', 'ready')`.

Rationale:
- NULL is the natural state of an artifact that has been acknowledged but not formally
  actioned. It requires no new value, no schema change, and no annotation.
- All 4 NULL rows in the sweep scope fit this semantics: no decision has been made.
- This definition is the least-invasive resolution and is consistent with the design
  model in Section 3.2 of `lifecycle-sweep-model-design-v02.md`.

**No new `owner_decision` value is required.**
**No new `state` value is required.**
**No schema change is required.**

### Section 3 — Full Classification Mapping

| owner_decision | Proposed DL sweep category | Row ids | Notes |
|---|---|---|---|
| NULL | Carry-Forward | 52, 69, 73, 74 | Proposed OD-2 definition |
| `deferred` | Deferred | 5, 12, 18, 19, 45, 46, 58, 67 | Structured value, known enum |
| `archived_cleanup_no_active_need` | STATE CONFLICT | 10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59 | state=ready vs state_gl017=archived inconsistency |
| `accepted_done` | STATE CONFLICT | 14 | state=active vs state_gl017=closed inconsistency |
| `retain` | NOT CLASSIFIABLE | 50 | Not in known owner_decision enum |
| free-text | NOT CLASSIFIABLE | 72 | Not in known enum |

**Open Execution:** no rows (no `confirmed` value in sweep scope).
**Excluded:** no rows (no `rejected` value in sweep scope).
**Not-blocker:** no rows (no structured value exists for this category yet).

### Section 4 — STATE CONFLICT Group: Observation

13 rows (12 + 1) surface as STATE CONFLICT. These are not resolvable by OD-2 alone.
They require a separate Owner decision on:
- Which field takes precedence when `state` and `state_gl017` conflict
- Whether the 12 `archived_cleanup_no_active_need` rows are treated as Excluded
  (Owner decision = no active need) or as STATE CONFLICT pending state correction

This is flagged in the proposal for Owner awareness. No action is proposed or scoped
within this write plan or its resulting artifact.

### Section 5 — MAC-DL-2 Impact

If OD-2 is resolved as proposed (Carry-Forward = NULL owner_decision):
- MAC-DL-2 becomes active
- The `[REQUIRES VERIFICATION — OD-2 OPEN]` placeholder is replaced by the active
  Carry-Forward category in the sweep output
- A subsequent v03 of `lifecycle-sweep-model-design.md` would incorporate the resolution
  (not scoped in this write plan)

### Section 6 — Owner Decision Required

The proposal presents two questions for Owner confirmation:

**Q1:** Do you accept `owner_decision IS NULL` as the definition of Carry-Forward?

**Q2 (awareness only — no action required now):** The 13 STATE CONFLICT rows require
a separate decision on `state` vs `state_gl017` precedence. Do you want this scoped
as a follow-up OD, or deferred?

---

## 5. File Verification Criteria

After writing the proposal artifact, verify:

| # | Criterion | Pass condition |
|---|---|---|
| V-1 | File exists | `lifecycle-sweep-model-design-od2-owner-decision-mapping-v01.md` present on disk |
| V-2 | Size > 0 | Non-empty file |
| V-3 | Contains OD-2 proposed resolution | Text `owner_decision IS NULL` present |
| V-4 | Contains classification mapping table | Section with all 6 value rows present |
| V-5 | Contains STATE CONFLICT observation | Section 4 present |
| V-6 | No DB change instructions | File contains no SQL INSERT, UPDATE, or DELETE |

All 6 criteria must pass. Any failure = stop, report to Owner.

---

## 6. Explicit Exclusions

| Exclusion |
|---|
| No DB writes of any kind |
| No `deliverable_lifecycle` INSERT or UPDATE |
| No `team_tasks` update (97 remains open) |
| No edit to `lifecycle-sweep-model-design-v02.md` |
| No new D-folder |
| No schema changes |
| No cleanup, archiving, or lifecycle state changes |
| No governance amendments |
| No dashboard work |

---

## 7. Execution Sequence (post-authorization)

1. Write `lifecycle-sweep-model-design-od2-owner-decision-mapping-v01.md`
2. Verify V-1 through V-6
3. Report to Owner: file path, verification results
4. No further actions

---

*Write plan persisted: 2026-06-15*
*Awaiting Owner verification and authorization before any execution.*
