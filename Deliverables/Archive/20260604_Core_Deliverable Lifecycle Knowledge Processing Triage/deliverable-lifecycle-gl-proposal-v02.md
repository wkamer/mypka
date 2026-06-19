# Proposal: GL-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving

**File:** `Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-gl-proposal-v02.md`
**Date:** 2026-06-05
**Prepared by:** Larry, Team Orchestrator
**Proposal version:** v02
**Supersedes:** `deliverable-lifecycle-gl-proposal-v01.md`
**Status:** Proposal-only — awaiting Owner approval

**Governance:** This document is read-only. No GL file creation, index update, or any system change may be executed without explicit Owner Walter Kamer approval of this proposal. This is a proposal document only.

---

## Revision Notes: v01 to v02

| # | Amendment | Sections affected in GL content |
|---|---|---|
| 1 | Lifecycle state model fixed. One primary state only. Authoritative and Processed moved to lifecycle markers. Pre-acceptance states moved to context-only sub-section (3.1). Post-acceptance primary states in sub-section (3.2). Lifecycle markers defined in new sub-section (3.3). | Section 3 (complete rewrite); P1, P4 revised |
| 2 | Scope tightened. GL-017 now explicitly governs post-acceptance lifecycle only. Pre-acceptance states listed as context-only with their governing instruments. | Section 2 revised; Section 3.1 new |
| 3 | Lifecycle state is recorded in execution reports, not written into source files. New principle P13 added. | P13 new |
| 6 | Cross-domain tightened. P6 revised: one canonical home; other domains receive references not copies; duplicate extraction requires explicit Owner approval. P12 revised to align. | P6 revised; P12 revised |
| 8 | Index row format verified. Verification note added to Section 5. Risk entry added. | Section 5; Section 10 |

Amendments 4, 5, and 7 apply primarily to SOP-017 and have no direct impact on GL-017 content.

---

## 1. Confirmed GL Number

**GL-017**

Confirmed from `Team Knowledge/Core/Guidelines/gl-index.md` on 2026-06-04. The current highest GL number is GL-016. GL-017 is the next available number.

> **Implementation note:** Re-confirm `gl-index.md` immediately before file creation at the time of implementation to ensure GL-017 has not been taken.

---

## 2. Proposed Filename

`GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`

---

## 3. Proposed Canonical Path

`Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`

---

## 4. Exact GL Content

The content between the markers below is the exact text to be written to the GL file if this proposal is approved. No variation, paraphrasing, or partial execution is permitted. Implementation executes exactly this content.

---

[BEGIN GL-017 FILE CONTENT]

# GL-017: Deliverable Lifecycle, Knowledge Processing, and Archiving

**File:** `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`
**Owner:** Walter Kamer
**Maintainer:** Larry, Team Orchestrator
**Status:** Active
**Version:** 1.0
**Created:** 2026-06-05

---

## 1. Purpose

This guideline defines the principle layer for the myPKA AI team deliverable lifecycle. It governs the post-acceptance phase: what happens to a deliverable after the Owner makes an acceptance decision. It establishes:

- The primary states a deliverable can occupy after acceptance
- The lifecycle markers that record what has been done to a deliverable
- The protections that apply to deliverables carrying the Authoritative marker
- The prerequisites that gate lifecycle processing
- The principles that govern knowledge extraction, archiving, and cross-domain routing

This guideline is the upstream principle for SOP-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure), which defines how to execute lifecycle decisions. This guideline does not define procedures. This guideline is downstream of GL-016 (Review Gate for Governance-Relevant Deliverables), which defines the prerequisite review gate. This guideline is not a substitute for SOP-015 (Proposal Iteration Protocol for System File Changes), which governs the creation and iteration of GLs, SOPs, Workstreams, and AGENT.md files.

---

## 2. Scope

This guideline governs the post-acceptance lifecycle of deliverables produced by the myPKA AI team, including proposals, execution reports, status reports, closure reports, triage reports, decision packets, and working artifacts.

A deliverable enters the scope of this guideline at the moment the Owner makes an explicit acceptance decision following the review gate per GL-016 and SOP-016. Before that moment, a deliverable is governed by GL-016, SOP-016, and SOP-015 as applicable. This guideline does not govern pre-acceptance phases.

---

## 3. Lifecycle Overview

This section is divided into three parts: pre-acceptance context states (not governed by GL-017), post-acceptance primary states (governed by GL-017), and lifecycle markers (governed by GL-017).

### 3.1 Pre-Acceptance States — Context Only

The following states exist before the Owner acceptance decision. GL-017 does not govern them. They are listed here for orientation only. The authoritative instruments for each state are noted.

| State | Definition | Governing instrument |
|---|---|---|
| Draft | Being prepared; not yet submitted for review | Agent conventions; GL-005 |
| Under Review | Review gate active; Owner review in progress | GL-016 and SOP-016 |
| Approved | Proposal approved for execution; execution not yet begun | SOP-015 |
| Executed | Implementation complete; execution report produced | SOP-015 and execution discipline |

### 3.2 Post-Acceptance Primary States — Governed by GL-017

After the Owner acceptance decision, a deliverable holds exactly one primary state at any time. Primary state transitions require either an Owner decision or an orchestrator action with Owner confirmation. State transition procedures are defined in SOP-017.

Adding a lifecycle marker (Section 3.3) does not change the primary state. Only the transitions defined in this table change the primary state.

| State | Definition | Entry condition | Exit path |
|---|---|---|---|
| Accepted as Done | Owner has accepted the deliverable outcome; lifecycle decision required per SOP-017 | Owner decision after review gate passes per GL-016 and SOP-016 | Primary state remains Accepted as Done when markers are added. Transitions to Superseded, Archived, Parked, or Deferred only via explicit Owner decision or orchestrator action with Owner confirmation |
| Superseded | Replaced by a newer accepted version; preserved but no longer current | Newer version accepted as Done; Owner decision or orchestrator action with Owner confirmation per SOP-017 | Archived or retained indefinitely as historical record |
| Archived | Moved to Archive folder per formal proposal; no longer in active use | Formal proposal with complete reference preservation plan approved by Owner per SOP-017 EX-6 | Retained indefinitely; never deleted |
| Parked | Acknowledged but not actioned | Owner selects park as a lifecycle decision | Owner re-opens or explicitly closes |
| Deferred | Valid but postponed; not in active lifecycle | Owner selects defer as a lifecycle decision | Owner activates in a future session |

### 3.3 Lifecycle Markers — Governed by GL-017

Lifecycle markers are additive designations that coexist with the primary state. A deliverable may hold multiple markers simultaneously. Markers record what has been done to or decided about a deliverable after acceptance. They do not replace the primary state.

Marker assignment requires either Owner confirmation or an orchestrator action with Owner confirmation. Markers are not assigned automatically.

| Marker | Definition | Assignment | Removal |
|---|---|---|---|
| Authoritative | Designated as the canonical reference for a specific topic | Owner or orchestrator with Owner confirmation; cannot be auto-assigned | Removed when a newer version takes over the designation, requiring explicit Owner decision. Removal of this marker does not delete the deliverable; it is retained |
| Processed | One or more approved processing actions have been executed (extraction to PKM, BKM, or agent_learnings); multiple events accumulate | Assigned after each approved processing action | Not removed; each event is recorded in the execution report |
| Indexed | Recorded as a named reference for a specific topic in the execution report; no separate file write unless Owner approves an exact target | Assigned when the orchestrator records the reference in the execution report | Not removed |
| Knowledge Extracted | Content extracted to PKM or BKM under Owner approval; a subset of Processed | Assigned after an approved PKM or BKM write | Not removed |
| Reference Preserved | References to this deliverable have been identified and documented in the execution report | Assigned when reference identification is complete and recorded | Not removed |

---

## 4. Core Principles

**P1: Every accepted deliverable receives a lifecycle decision.**
The primary state Accepted as Done is the entry point for lifecycle processing. It is not a terminal state. It opens a processing decision. That decision may keep the primary state as Accepted as Done (with lifecycle markers added as applicable) or transition the primary state to Superseded, Archived, Parked, or Deferred. Adding a marker does not change the primary state; only the transitions in Section 3.2 do. The lifecycle decision itself is required. A processing action is not automatically required.

**P2: Review Gate completion is required before lifecycle processing.**
No processing action, archiving, knowledge extraction, or state transition to Accepted as Done may begin before the deliverable has passed the review gate per GL-016 and SOP-016. A deliverable that has not passed the review gate is not eligible for lifecycle processing.

**P3: Not every deliverable becomes knowledge.**
A deliverable may receive a lifecycle decision of retain in place or Superseded without any knowledge extraction. The absence of extraction is a valid outcome. Knowledge extraction is not required by default.

**P4: Deliverables carrying the Authoritative marker are protected.**
A deliverable carrying the Authoritative marker may not be deleted, moved, renamed, or archived without a formal proposal and explicit Owner approval. Removal of the Authoritative marker (for example when a newer version takes over the designation) does not delete the deliverable; the file is retained. These protections survive project closure, session boundaries, and agent changes.

**P5: Knowledge extraction follows GL-015 domain routing.**
All writes to PKM, BKM, agent_learnings, personal.db, team-knowledge.db, kamer e-commerce.db, or geldstroom-regie.db as part of lifecycle processing must follow GL-015 (Memory Domain Routing Protocol). GL-015 defines the routing destination. This guideline adds the Owner approval gate on top of GL-015 routing. Both apply simultaneously.

**P6: Personal and business processing are both supported; cross-domain routing must be explicit.**
A deliverable may be processed into personal knowledge (PKM) or business knowledge (BKM). When content appears relevant to more than one domain, one domain is selected as the canonical home and other domains receive references to that location rather than extracted copies. Cross-domain candidates must be surfaced to the Owner before any routing decision. Duplicate extraction across multiple domains requires explicit Owner approval for each additional domain and must align with GL-015. The SSOT Golden Rule governs: every fact lives in exactly one place.

**P7: No automatic PKM or BKM extraction.**
No write to PKM or BKM occurs automatically as a result of a deliverable reaching any lifecycle state or receiving any marker. Every extraction requires explicit Owner approval for that specific write.

**P8: No automatic backlog creation.**
Identifying a deliverable as a backlog candidate does not create a backlog entry. The candidate must be surfaced to the Owner, who decides whether to register it.

**P9: No automatic database writes.**
No write to personal.db, team-knowledge.db, kamer e-commerce.db, geldstroom-regie.db, or any UMC or memory-db system occurs as a result of lifecycle processing without explicit Owner approval.

**P10: No automatic AGENT.md updates.**
A lesson learned may be proposed from a deliverable, but it must not be written to agent_learnings or any AGENT.md file without explicit Owner approval and the appropriate procedure per SOP-015.

**P11: No automatic archiving or file moves.**
Moving a deliverable to an Archive folder or any other location requires a formal proposal specifying source path, target path, reason, reference preservation plan, rollback plan, and post-check plan. All references to the deliverable must be identified and documented before any file is moved.

**P12: SSOT applies to all extracted knowledge.**
Extracted knowledge lives in exactly one canonical location. Cross-domain access uses references to the canonical location, not copies of the content. When lifecycle processing touches content relevant to more than one domain, one home domain is chosen and all other domains link to it. No duplicate extraction may occur without explicit Owner approval documenting the exception and confirming alignment with GL-015.

**P13: Lifecycle state is recorded in execution reports, not written into source files.**
A deliverable's primary state and lifecycle markers are established and recorded in the execution report for the lifecycle action that assigned them. Writing a visible state indicator into the source deliverable file (for example adding a STATUS: Superseded header) is a separate, explicit write action that requires Owner approval. The execution report is the authoritative governance record of the deliverable's current state and markers. The absence of a visible status note in a source file does not mean the state is unknown.

---

## 5. Relationship to Existing Instruments

**GL-015 (Memory Domain Routing Protocol)**
GL-015 is the authoritative routing standard for all agent write operations. This guideline references GL-015 for all database write routing decisions and does not override GL-015. Any conflict between lifecycle processing routing and GL-015 is resolved by GL-015. No change to GL-015 is required or included in this protocol.

**GL-016 (Review Gate for Governance-Relevant Deliverables)**
GL-016 defines the prerequisite review gate. Accepted as Done is the post-review-gate primary state and is the entry point for this lifecycle protocol. This guideline is downstream of GL-016. GL-016 may optionally reference GL-017 as the downstream lifecycle instrument in a future update; that update is a separate decision item and is not part of this guideline.

**SOP-016 (Review Gate Procedure for Governance-Relevant Deliverables)**
SOP-016 governs the review gate procedure. SOP-016 must complete before any lifecycle processing begins. SOP-016 may optionally reference SOP-017 as the downstream lifecycle procedure in a future update; that update is a separate decision item and is not part of this guideline.

**SOP-015 (Proposal Iteration Protocol for System File Changes)**
All formal proposals for GL or SOP creation, including the proposal that established this guideline, follow SOP-015 discipline: versioned proposals, Revision Notes per review round, Owner approval gating, and execution against the approved version only. When lifecycle processing results in a new GL, SOP, Workstream, or AGENT.md update, SOP-015 governs that creation. SOP-015 applies regardless of whether the update was triggered by a lifecycle processing decision.

**SOP-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure)**
SOP-017 is the operational counterpart to this guideline. SOP-017 defines trigger moments, the processing destination catalog, decision rules R1 through R10, domain routing aligned with GL-015, safeguards, explicit rules, and worked examples. SOP-017 must not be implemented before GL-017 exists. SOP-017 references GL-017 as the upstream principle. SOP-017 does not redefine the principles or state model in this guideline.

---

## 6. Optional Future Updates to Existing Instruments

The following updates to existing instruments are identified as potential future decisions. They are not part of this guideline and must not be executed as part of this guideline's implementation:

- GL-016 may be updated to reference GL-017 as the downstream lifecycle instrument.
- SOP-016 may be updated to reference SOP-017 as the downstream lifecycle procedure.

These are separate decision items requiring separate Owner approval.

---

## 7. Knowledge Currency

**Refresh trigger:** New deliverable types are introduced to the myPKA AI team workflow that are not covered by the post-acceptance primary states in Section 3.2, or a lifecycle marker in Section 3.3 needs to be added, revised, or retired.

**Refresh owner:** Larry, Team Orchestrator.

**Last reviewed:** 2026-06-05.

[END GL-017 FILE CONTENT]

---

## 5. Exact gl-index.md Update Text

The following row is to be appended to the GL table in `Team Knowledge/Core/Guidelines/gl-index.md` immediately after the GL-016 row, if this proposal is approved. No other rows in gl-index.md are to be modified.

Row to append:

```
| GL-017 | [[GL-017_Deliverable Lifecycle Knowledge Processing and Archiving]] | Principle: accepted deliverables require a lifecycle decision — post-acceptance primary states, lifecycle markers, authoritative source protection, knowledge extraction prerequisites, and cross-domain routing principles |
```

**Format verification:** The row format above was verified against `gl-index.md` as read on 2026-06-04 in the current session. The existing format is: `| Nr | [[wikilink]] | description |`. Implementation must re-confirm the existing gl-index.md format immediately before appending, as the format is the authoritative source.

---

## 6. Pairing Notes

This proposal is paired with SOP-017 proposal (`deliverable-lifecycle-sop-proposal-v02.md`).

**Separation of concerns:**
- GL-017 defines principles: post-acceptance primary states, lifecycle markers, core principles P1 through P13, authoritative source protections, and cross-domain routing principles.
- SOP-017 defines procedures: trigger moments, decision rules R1 through R10, processing flows, domain routing table, safeguards checklist, explicit rules EX-1 through EX-7, worked examples, and execution report requirements.
- The two documents do not duplicate each other.

**Recommended execution order:**
GL-017 must be implemented and post-checked before SOP-017 is implemented. SOP-017 references GL-017 for the lifecycle state model and core principles. Without GL-017, those references are unresolved. This is the same pattern as GL-016 and SOP-016.

**If GL-017 is approved but SOP-017 is not yet approved:**
GL-017 is complete and operative on its own. It establishes the lifecycle framework and protections. SOP-017 provides the operational execution layer, but GL-017 is valid without SOP-017 existing.

**Cross-references if both are approved:**
- GL-017 Section 5 references SOP-017 as the operational counterpart. This is an anticipatory reference that resolves when SOP-017 is created.
- SOP-017 references GL-017 as the upstream principle document.

---

## 7. Implementation Scope

If this proposal is approved, exactly the following actions are in scope:

1. Create `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md` with the exact content from Section 4.
2. Append the GL-017 row to `Team Knowledge/Core/Guidelines/gl-index.md` per Section 5, after re-confirming the existing format.
3. Read back both files to confirm contents match the approved proposal exactly.
4. Report post-check result to Owner.

No other actions are in scope.

---

## 8. Explicit Exclusions

The following are explicitly excluded from GL-017 implementation:

- Creating SOP-017 (separate proposal requiring separate Owner approval)
- Updating GL-016
- Updating SOP-016
- Updating GL-015
- Updating SOP-015
- Updating CLAUDE.md
- Writing to any database (personal.db, team-knowledge.db, kamer e-commerce.db, geldstroom-regie.db, UMC, memory-db)
- Updating any AGENT.md file
- Processing any existing deliverable into PKM or BKM
- Archiving any existing deliverable
- Creating any backlog item
- Writing team_tasks or team_log entries

---

## 9. Post-Check Plan

After GL-017 is implemented, the following checks are performed before declaring implementation complete:

1. Read back `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`. Confirm all sections, principles (P1 through P13), and all three lifecycle overview sub-sections (3.1, 3.2, 3.3) match the approved content in Section 4 exactly.
2. Read back `Team Knowledge/Core/Guidelines/gl-index.md`. Confirm the GL-017 row is present, correctly formatted, and no other rows were modified.
3. Confirm no other files were modified during implementation.
4. Confirm no database writes occurred.
5. Report post-check result to Owner: file path, GL number, index row, confirmation of no side effects, and readiness to proceed to SOP-017 if Owner selects Option B.

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| GL-017 number taken between proposal preparation and implementation | Re-confirm gl-index.md immediately before file creation during implementation |
| gl-index.md format changed between proposal preparation and implementation | Implementation must re-confirm the existing format before appending; the proposed row format is based on the format read on 2026-06-04 |
| GL content inadvertently contains procedural content | Section 4 contains lifecycle overview and principles only. No trigger moments, decision rules, or processing steps are present. Reviewer should flag any procedural content before approving |
| SOP-017 referenced before SOP-017 exists | GL-017 Section 5 uses an anticipatory reference. GL-017 is complete and valid without SOP-017. The reference resolves when SOP-017 is created |
| Optional future updates (GL-016, SOP-016) executed automatically | Section 6 and Section 8 both explicitly mark these as excluded |
| Owner approves GL-017 and proceeds to SOP-017 without waiting for post-checks | Post-check plan (Section 9) must be executed and reported to Owner before SOP-017 work begins |

---

## 11. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-017 implementation only. SOP-017 proposal reviewed separately at a later time. |
| **B** | Approve paired implementation. GL-017 implemented first. SOP-017 implemented after GL-017 post-checks are confirmed to Owner. |
| **C** | Request amendments. Specify which sections require changes. A v03 will be prepared per SOP-015. |
| **D** | Defer. |
| **E** | Reject. |

---

*Delivered on: 2026-06-05*
*Delivered at: Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-gl-proposal-v02.md*
