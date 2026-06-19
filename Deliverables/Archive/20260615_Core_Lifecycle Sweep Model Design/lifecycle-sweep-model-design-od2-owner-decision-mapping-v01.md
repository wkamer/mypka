# OD-2 Owner Decision Mapping Proposal v01

**Document type:** Proposal — design artifact
**Status:** Pending Owner decision
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Write plan:** `lifecycle-sweep-model-design-od2-owner-decision-mapping-write-plan-v01.md`
**Governing design:** `lifecycle-sweep-model-design-v02.md`

---

## 1. OD-2 Question

> Is Carry-Forward a structured `owner_decision` value, an annotation in `processing_notes`,
> or defined by NULL `owner_decision`? Without this, Carry-Forward cannot be auto-classified.

This proposal answers that question based on the live `deliverable_lifecycle` data as of 2026-06-15.

---

## 2. Proposed OD-2 Resolution

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

---

## 3. Full Classification Mapping

Sweep-relevant rows: `state NOT IN ('archived', 'closed')`. Total: 27.

| owner_decision | Proposed DL sweep category | Row ids | Notes |
|---|---|---|---|
| NULL | Carry-Forward | 52, 69, 73, 74 | Proposed OD-2 definition |
| `deferred` | Deferred | 5, 12, 18, 19, 45, 46, 58, 67 | Structured value, known enum |
| `archived_cleanup_no_active_need` | STATE CONFLICT | 10, 11, 13, 16, 36, 40, 41, 42, 55, 56, 57, 59 | state=ready vs state_gl017=archived inconsistency |
| `accepted_done` | STATE CONFLICT | 14 | state=active vs state_gl017=closed inconsistency |
| `retain` | NOT CLASSIFIABLE | 50 | Not in known owner_decision enum |
| free-text (`misclassified GL-017: G2 artifact, file moved to 20260612_Core_DL Control Inventory`) | NOT CLASSIFIABLE | 72 | Not in known enum |

**Open Execution:** no rows — no `confirmed` value in sweep scope.
**Excluded:** no rows — no `rejected` value in sweep scope.
**Not-blocker:** no rows — no structured value exists for this category yet.

---

## 4. STATE CONFLICT Group: Observation

13 rows surface as STATE CONFLICT (12 + 1). These are not resolvable by OD-2 alone.

**Group A (12 rows):** `owner_decision = 'archived_cleanup_no_active_need'`, `state = 'ready'`,
`state_gl017 = 'archived'`. The `owner_decision` value signals no active need, but `state`
has not been updated to reflect this. Per Section 6 of `lifecycle-sweep-model-design-v02.md`,
state vs state_gl017 conflict routes to `[STATE CONFLICT]` section — no category assignment
until resolved.

**Group B (1 row, id 14):** `owner_decision = 'accepted_done'`, `state = 'active'`,
`state_gl017 = 'closed'`. Same conflict pattern.

A separate Owner decision is required to resolve these 13 rows. Two sub-questions:
- Which field takes precedence when `state` and `state_gl017` conflict?
- Should the 12 Group A rows be treated as Excluded (Owner said no active need) or held
  in STATE CONFLICT pending a `state` correction?

This is flagged for Owner awareness. No action is proposed or scoped within this document.

---

## 5. MAC-DL-2 Impact

If OD-2 is resolved as proposed (Carry-Forward = `owner_decision IS NULL`):
- MAC-DL-2 becomes active.
- The `[REQUIRES VERIFICATION — OD-2 OPEN]` placeholder in the sweep output is replaced
  by the active Carry-Forward category showing the 4 NULL rows.
- A subsequent version of `lifecycle-sweep-model-design.md` would incorporate this
  resolution. That versioning is not scoped in this document.

---

## 6. Owner Decisions Required

**Q1 — OD-2 resolution (primary):**
Do you accept `owner_decision IS NULL` AND `state IN ('active', 'ready')` as the
definition of Carry-Forward?

**Q2 — STATE CONFLICT group (awareness only — no action required now):**
The 13 STATE CONFLICT rows require a separate precedence decision. Do you want this
scoped as a follow-up open decision (OD-3), or deferred to a later session?

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-od2-owner-decision-mapping-v01.md*
