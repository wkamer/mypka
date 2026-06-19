# Proposal: GL-017 — Deliverable Lifecycle, Knowledge Processing, and Archiving

**File:** `Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-gl-proposal-v01.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Proposal version:** v01
**Status:** Proposal-only — awaiting Owner approval

**Governance:** This document is read-only. No GL file creation, index update, or any system change may be executed without explicit Owner Walter Kamer approval of this proposal. This is a proposal document only.

---

## 1. Confirmed GL Number

**GL-017**

Confirmed from `Team Knowledge/Core/Guidelines/gl-index.md` on 2026-06-04. The current highest GL number is GL-016. GL-017 is the next available number.

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
**Created:** 2026-06-04

---

## 1. Purpose

This guideline defines the principle layer for the myPKA AI team deliverable lifecycle. It establishes:

- The states a deliverable can occupy after production
- The protections that apply to authoritative sources
- The prerequisites that gate lifecycle processing
- The principles that govern knowledge extraction, archiving, and cross-domain routing

This guideline is the upstream principle for SOP-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure), which defines how to execute lifecycle decisions. This guideline does not define procedures. This guideline is downstream of GL-016 (Review Gate for Governance-Relevant Deliverables), which defines the prerequisite review gate.

---

## 2. Scope

This guideline applies to all deliverables produced by the myPKA AI team, including proposals, execution reports, status reports, closure reports, triage reports, decision packets, and working artifacts, that have passed the review gate per GL-016 and have received an Owner acceptance decision.

Deliverables that have not yet passed the review gate are governed exclusively by GL-016 and SOP-016. This guideline does not apply to them.

---

## 3. Lifecycle States

A deliverable occupies exactly one primary state at any time. States are not assigned automatically. Each state transition requires either an Owner decision or an orchestrator action with Owner confirmation. State transition procedures are defined in SOP-017.

| State | Definition | Entry condition | Exit path |
|---|---|---|---|
| Draft | Being prepared; not yet submitted for review | Agent begins producing the deliverable | Submitted for review |
| Under Review | Review gate is active per GL-016 and SOP-016 | Deliverable submitted for Owner review | Owner decision |
| Approved | Proposal approved for execution; execution not yet begun | Owner approves execution | Execution begins |
| Executed | Implementation complete; execution report produced | Execution report produced | Execution report enters review gate |
| Accepted as Done | Owner has accepted the deliverable outcome | Owner decision after review gate passes | Processing decision required per SOP-017 |
| Authoritative | Designated as the canonical reference for a topic | Owner or orchestrator designates with Owner confirmation; cannot be auto-assigned | Explicit supersession or archiving via formal proposal |
| Processed | Knowledge extracted to PKM, BKM, or agent_learnings | Processing executed with explicit Owner approval | Content lives in target system; source deliverable retained |
| Superseded | Replaced by a newer version; preserved but no longer current | Newer version accepted as Done | Archived or retained as historical record |
| Archived | Moved to Archive folder; no longer in active use | Processing decision via formal proposal; all references preserved before move | Retained in archive indefinitely; never deleted |
| Parked | Acknowledged but not actioned | Owner selects park as a lifecycle decision | Owner re-opens or explicitly closes |
| Deferred | Valid but postponed; not in active lifecycle | Owner selects defer as a lifecycle decision | Owner activates in a future session |

---

## 4. Core Principles

**P1: Every accepted deliverable receives a lifecycle decision.**
The state Accepted as Done is not a terminal state. It opens a processing decision. That decision may result in any lifecycle state, including retain in place. The decision itself is required. A processing action is not automatically required.

**P2: Review Gate completion is required before lifecycle processing.**
No processing action, archiving, knowledge extraction, or state transition to Accepted as Done may begin before the deliverable has passed the review gate per GL-016 and SOP-016. A deliverable that has not passed the review gate is not eligible for lifecycle processing.

**P3: Not every deliverable becomes knowledge.**
A deliverable may receive a lifecycle decision of retain in place or superseded without any knowledge extraction. The absence of extraction is a valid outcome. Knowledge extraction is not required by default.

**P4: Authoritative sources are protected.**
A deliverable designated as Authoritative may not be deleted, moved, renamed, or archived without a formal proposal and explicit Owner approval. This protection survives project closure, session boundaries, and agent changes.

**P5: Knowledge extraction follows GL-015 domain routing.**
All writes to PKM, BKM, agent_learnings, personal.db, team-knowledge.db, kamer e-commerce.db, or geldstroom-regie.db as part of lifecycle processing must follow GL-015 (Memory Domain Routing Protocol). GL-015 defines the routing destination. This guideline adds the Owner approval gate on top of GL-015 routing. Both apply simultaneously.

**P6: Personal and business processing are both supported.**
A deliverable may be processed into personal knowledge (PKM), business knowledge (BKM), or both, subject to individual Owner approval for each processing destination. The lifecycle protocol does not restrict processing to a single domain.

**P7: No automatic PKM or BKM extraction.**
No write to PKM or BKM occurs automatically as a result of a deliverable reaching any lifecycle state. Every extraction requires explicit Owner approval for that specific write.

**P8: No automatic backlog creation.**
Identifying a deliverable as a backlog candidate does not create a backlog entry. The candidate must be surfaced to the Owner, who decides whether to register it.

**P9: No automatic database writes.**
No write to personal.db, team-knowledge.db, kamer e-commerce.db, geldstroom-regie.db, or any UMC or memory-db system occurs as a result of lifecycle processing without explicit Owner approval.

**P10: No automatic AGENT.md updates.**
A lesson learned may be proposed from a deliverable, but it must not be written to agent_learnings or any AGENT.md file without explicit Owner approval and the appropriate procedure per SOP-015.

**P11: No automatic archiving or file moves.**
Moving a deliverable to an Archive folder or any other location requires a formal proposal specifying source path, target path, reason, reference preservation plan, rollback plan, and post-check plan. All references to the deliverable must be identified and preserved before any file is moved.

**P12: Cross-domain knowledge is surfaced before second-domain processing.**
If extracted content is relevant to more than one domain, it must be surfaced to the Owner before any second-domain write or duplicated processing. The SSOT Golden Rule applies: every fact lives in exactly one place. Cross-domain access uses references, not copies.

---

## 5. Relationship to Existing Instruments

**GL-015 (Memory Domain Routing Protocol)**
GL-015 is the authoritative routing standard for all agent write operations. This guideline references GL-015 for all database write routing decisions and does not override GL-015. Any conflict between lifecycle processing routing and GL-015 is resolved by GL-015. No change to GL-015 is required or included in this protocol.

**GL-016 (Review Gate for Governance-Relevant Deliverables)**
GL-016 defines the prerequisite review gate. Accepted as Done is the post-review-gate state and is the entry condition for this lifecycle protocol. This guideline is downstream of GL-016. GL-016 may optionally reference GL-017 as the downstream lifecycle instrument in a future update; that update is a separate decision item and is not part of this guideline.

**SOP-016 (Review Gate Procedure for Governance-Relevant Deliverables)**
SOP-016 governs the review gate procedure. SOP-016 must complete before any lifecycle processing begins. SOP-016 may optionally reference SOP-017 as the downstream lifecycle procedure in a future update; that update is a separate decision item and is not part of this guideline.

**SOP-015 (Proposal Iteration Protocol for System File Changes)**
All formal proposals for GL or SOP creation, including the proposal that established this guideline, follow SOP-015 discipline: versioned proposals, Revision Notes per review round, Owner approval gating, and execution against the approved version only. When lifecycle processing produces a new GL, SOP, or AGENT.md update, SOP-015 governs that creation.

**SOP-017 (Deliverable Lifecycle, Knowledge Processing, and Archiving Procedure)**
SOP-017 is the operational counterpart to this guideline. SOP-017 defines trigger moments, the processing destination catalog, decision rules R1 through R10, domain routing aligned with GL-015, safeguards, and worked examples. SOP-017 must not be implemented before GL-017 exists. SOP-017 references GL-017 as the upstream principle. SOP-017 does not redefine the principles in this guideline.

---

## 6. Optional Future Updates to Existing Instruments

The following updates to existing instruments are identified as potential future decisions. They are not part of this guideline and must not be executed as part of this guideline's implementation:

- GL-016 may be updated to reference GL-017 as the downstream lifecycle instrument.
- SOP-016 may be updated to reference SOP-017 as the downstream lifecycle procedure.

These are separate decision items requiring separate Owner approval.

---

## 7. Knowledge Currency

**Refresh trigger:** New deliverable types are introduced to the myPKA AI team workflow that are not covered by the lifecycle states in Section 3, or a processing destination in SOP-017 is retired or added.

**Refresh owner:** Larry, Team Orchestrator.

**Last reviewed:** 2026-06-04.

[END GL-017 FILE CONTENT]

---

## 5. Exact gl-index.md Update Text

The following row is to be appended to the GL table in `Team Knowledge/Core/Guidelines/gl-index.md` immediately after the GL-016 row, if this proposal is approved. No other rows in gl-index.md are to be modified.

Row to append:

```
| GL-017 | [[GL-017_Deliverable Lifecycle Knowledge Processing and Archiving]] | Principle: accepted deliverables require a lifecycle decision — lifecycle states, authoritative source protection, knowledge extraction prerequisites, and cross-domain routing principles |
```

---

## 6. Pairing Notes

This proposal is paired with SOP-017 proposal (`deliverable-lifecycle-sop-proposal-v01.md`).

**Separation of concerns:**
- GL-017 defines principles: lifecycle states, authoritative source protections, prerequisites, and cross-domain routing principles.
- SOP-017 defines procedures: trigger moments, decision rules R1 through R10, processing flows, domain routing table, safeguards checklist, and worked examples.
- The two documents do not duplicate each other.

**Recommended execution order:**
GL-017 must be implemented and post-checked before SOP-017 is implemented. SOP-017 references GL-017 as the upstream principle. Without GL-017, the lifecycle states and principles that SOP-017 references are not formally established. This is the same pattern as GL-016 and SOP-016: principle first, procedure after post-checks pass.

**If GL-017 is approved but SOP-017 is not yet approved:**
GL-017 is complete and operative on its own. It establishes the lifecycle framework and protections. SOP-017 provides the operational execution layer, but GL-017 is valid and useful without SOP-017 existing.

**Cross-references if both are approved:**
- GL-017 Section 5 references SOP-017 as the operational counterpart. This is an anticipatory reference that resolves when SOP-017 is created.
- SOP-017 references GL-017 as the upstream principle document.

---

## 7. Implementation Scope

If this proposal is approved, exactly the following actions are in scope:

1. Create `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md` with the exact content from Section 4.
2. Append the GL-017 row to `Team Knowledge/Core/Guidelines/gl-index.md` per Section 5.
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

1. Read back `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md`. Confirm all sections, principles, and the lifecycle states table match the approved content in Section 4 exactly.
2. Read back `Team Knowledge/Core/Guidelines/gl-index.md`. Confirm the GL-017 row is present, correctly formatted, and no other rows were modified.
3. Confirm no other files were modified during implementation.
4. Confirm no database writes occurred.
5. Report post-check result to Owner: file path, GL number, index row, confirmation of no side effects, and readiness to proceed to SOP-017 if Owner selects Option B.

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| GL-017 number taken between proposal preparation and implementation | Re-confirm gl-index.md immediately before file creation during implementation |
| GL content inadvertently contains procedural content | Section 4 contains lifecycle states and principles only. No trigger moments, decision rules, or processing steps are present. Reviewer should flag any procedural content before approving |
| SOP-017 referenced before SOP-017 exists | GL-017 Section 5 uses an anticipatory reference. GL-017 is complete and valid without SOP-017. The reference resolves when SOP-017 is created |
| Optional future updates (GL-016, SOP-016) executed automatically as part of implementation | Section 6 and Section 8 both explicitly mark these as excluded |
| Owner approves GL-017 and proceeds to SOP-017 without waiting for post-checks | Post-check plan (Section 9) must be executed and reported to Owner before SOP-017 work begins |

---

## 11. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-017 implementation only. SOP-017 proposal reviewed separately at a later time. |
| **B** | Approve paired implementation. GL-017 implemented first. SOP-017 implemented after GL-017 post-checks are confirmed to Owner. |
| **C** | Request amendments. Specify which sections require changes. A v02 will be prepared per SOP-015. |
| **D** | Defer. |
| **E** | Reject. |

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-gl-proposal-v01.md*
