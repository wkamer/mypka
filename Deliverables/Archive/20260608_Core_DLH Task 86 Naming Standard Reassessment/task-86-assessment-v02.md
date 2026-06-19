# Task 86 — Naming Standard Reassessment: Governance Landing Locations

**Task:** Task 86 — Naming standard: reassess governance landing locations after architecture decision
**Status:** Complete — proposals produced
**Produced by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Basis:** Task 85 Owner decision: Model A (Folder per artifact) confirmed as canonical unit.
Workstream code convention adopted going forward.

---

## Correction Note

**Corrects:** task-86-assessment.md (v01)
**Reason:** Section 3 contained unsafe placeholder wording ("ID=48... wait, proposal v01 was
registered separately — see deliverable_lifecycle for the correct ID"). Placeholder language
is not acceptable in a governance deliverable. Replaced with an audit-safe statement.
**Scope of change:** Section 3, Superseded paragraph only. All other content unchanged.

---

## 1. Assessment Scope

Task 86 was created to block implementation of the naming and versioning standards until the
architecture question (Task 85) was resolved. The question: do the naming standards need to
change based on the canonical unit-of-work model selected?

Task 85 resolved: Model A confirmed. Assessment complete.

---

## 2. Confirmed Governance Landing Locations

The landing locations from Naming Proposal v01 are confirmed correct for Model A, with one
addition: GL-004 is a new target for the workstream code convention.

| Change | Target instrument | Status vs Proposal v01 |
|---|---|---|
| Deliverable folder naming (Model A confirmation) | GL-001 | Confirmed — same as v01, now includes workstream code |
| Workstream code naming convention | GL-001 | New — not in proposal v01 (Model A was unconfirmed) |
| Deliverable file naming (files within a folder) | GL-001 | Confirmed — same as v01 |
| Versioning syntax (`v01/v02`) | GL-001 | Confirmed — same as v01 |
| Same-folder vs. new-folder rule | GL-001 | Confirmed — same as v01 |
| Correction Note requirement | GL-001 | Confirmed — same as v01 |
| Workstream code path example | GL-004 | New — minor additive amendment to Deliverables section |
| English-language rule for governance content | GL-014 | Out of scope for this proposal — Task 77 separate track |
| Correction versioning rule (broad scope) | SOP-015 | Out of scope for this proposal — Task 78 separate track |
| Artifact type taxonomy definition | SOP-017 | Out of scope for this proposal — Task 87 separate track |

---

## 3. What Changes vs Proposal v01

**Added:**
- GL-001 now includes the workstream code convention as part of the Deliverables Folder
  Naming section. This was not possible in proposal v01 because the architecture model
  had not been confirmed.
- GL-004 is a new target. The Deliverables section in GL-004 receives a minor additive
  amendment: the format string is updated to show the optional workstream code segment,
  and the examples are updated to English Title Case.

**Unchanged:**
- The file naming rules and versioning rules from proposal v01 carry forward unchanged.
- GL-014 (Task 77) and SOP-015 (Task 78) remain separate, subsequent tracks.

**Superseded:**
- Naming Standardization Proposal v01 (2026-06-07, folder:
  `20260607_Core_Deliverable Lifecycle Naming Artifact Standardization Proposal/`) is
  superseded by the GL Amendment Proposal v01 produced in this session. Naming
  Standardization Proposal v01 should be marked `superseded` in `deliverable_lifecycle`
  after its correct lifecycle row is verified. Do not guess the lifecycle ID.

---

## 4. Scope of the GL Amendment Proposal

The companion deliverable (`20260608_Core_DLH GL-001 and GL-004 Amendment Proposal v01/`)
contains:
- Exact amendment text for GL-001 (three new sections)
- Exact amendment text for GL-004 (Deliverables section update)
- Pre-check results
- Post-check plan
- Batch-stop rules

This proposal covers Task 75 in full and adds the workstream code as a new standard.
Tasks 77 and 78 remain open and require separate proposals.

---

## 5. Task Routing After This Assessment

| Task | Status | Next action |
|---|---|---|
| Task 75 | Open | Unblocked — implement via GL Amendment Proposal v01 after Owner authorization |
| Task 77 | Open | Separate proposal required (GL-014) — next track |
| Task 78 | Open | Separate proposal required (SOP-015) — next track |
| Task 86 | Completed | This document |
| Task 87 | Open | Artifact_type migration sequence — follow after naming standard is implemented |

---

*Delivered on: 2026-06-08*
*Delivered at: Deliverables/20260608_Core_DLH Task 86 Naming Standard Reassessment/task-86-assessment-v02.md*
