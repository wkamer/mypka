# Owner Decision Package — DL Hardening Phase C

**Date:** 2026-06-08
**Prepared by:** Larry
**Iris review:** Accept (see `review-dl-hardening-phase-c-v01.md`)
**Status:** Awaiting Owner authorization — no implementation active

---

## What Phase C proposes

Phase C implements the Owner visibility layer on top of the existing deliverable_lifecycle registry (Phases A and B completed).

**Four actions:**

1. **Schema addition** — two new columns in `deliverable_lifecycle`: `workstream_code` and `state_gl017`
2. **Data alignment** — populate `state_gl017` from existing `state` values; populate `workstream_code` for known workstreams; correct `artifact_type` mismatches for 9 existing rows
3. **CLAUDE.md addition** — Larry registers every new primary deliverable in `deliverable_lifecycle` at folder creation (exact text in Section 2.3 of the proposal)
4. **Reporting script** — Kai builds `generate_deliverable_index.py`; Larry runs it at every session start; output is `Deliverables/INDEX.md`

No governance amendments. No changes to GL-017, SOP-017, GL-016, SOP-019, GL-001, or GL-004.

---

## Iris verdict

**Accept** — the proposal is sound.

**Iris risk flag:** The artifact_type migration (Section 2.2) is declared deterministic (no per-row Owner decision required), but the Owner is asked to confirm the mapping table is correct. If the Owner approves without reviewing the mapping table row by row, misclassified rows execute automatically. The only recovery gate is C-4's row-count check, which catches deletions but not wrong classifications.

**Iris smallest safe next step:** Owner reviews the artifact_type mapping table in Section 2.2 of the proposal row by row before authorizing.

---

## Artifact_type mapping table (from proposal Section 2.2 — review before authorizing)

| Current value | Affected folder | Correct type |
|---|---|---|
| `status_report` | `20260607_Core_LC Batch 1 Execution Report` | `execution_report` |
| `status_report` | `20260607_Core_LC Batch 2 Execution Report` | `execution_report` |
| `status_report` | `20260607_Core_LCL Session Start Verification` | `verification_report` |
| `status_report` | `20260607_Core_Post-SOP-019 Session Start Verification` | `verification_report` |
| `status_report` | `20260607_Core_Final Governance State Verification` | `verification_report` |
| `proposal` | `20260607_Core_LC Batch 1 Write-List` | `write_list` |
| `proposal` | `20260607_Core_LC Batch 2 Write-List` | `write_list` |
| `proposal` | `20260607_Core_LC Triage Write-Plan` | `write_list` |
| `proposal` | `20260606_Core_LC Lifecycle Phase 1 Write-List v05` | `write_list` |
| `triage_document` | `20260604_Core_Architecture Triage Memory Domain Routing` | `assessment` |

---

## Three authorization items (from proposal Section 8)

| Item | Description | Owner answer |
|---|---|---|
| 1 | Authorize Phase C implementation — steps C-1 through C-8 as specified | yes / no / correction |
| 2 | Authorize CLAUDE.md registration discipline addition — exact text in Section 2.3 | yes / no / correction |
| 3 | Confirm Task 87 artifact_type migration — mapping table above is correct | yes / no / correction |

---

## GL-021 reminder

Iris review is advisory only. It does not substitute for Owner authorization. These are two sequential gates. Authorization for implementation requires explicit Owner confirmation — separate from and subsequent to this Iris review.

---

## Exact next prompt (from Iris — copy verbatim when ready)

> "Larry, ik geef goedkeuring voor Phase C Proposal v02 in twee afzonderlijke beslissingen. Beslissing 1: ik keur het voorstel goed zoals beschreven, inclusief de CLAUDE.md-toevoeging (Section 2.3) en de Task 87 artifact_type-mapping (Section 2.2) als correct. Beslissing 2 volgt als aparte bevestiging zodra ik de mapping tabel heb doorgenomen. Nog geen schrijfautorisatie voor implementatie — wacht op mijn expliciete go voor executie."

---

Delivered on: 2026-06-08
Delivered at: `Deliverables/20260608_Core_DL Hardening Phase C Proposal v01/owner-decision-package-phase-c-v01.md`
