# Owner Review Advisor — Lean Scoping Proposal v01

**Status:** Awaiting Owner decision.
**Prepared by:** Nolan, HR Specialist
**Date:** 2026-06-06

---

## 1. Purpose

The Owner Review Advisor is an independent review layer on Larry's governance output. Its single job is to compress complex governance decisions into a compact, actionable signal for the Owner. It does not execute governance. It does not replace Larry. It gives the Owner a fast, independent read on what Larry has produced so the Owner can decide with confidence.

---

## 2. Responsibilities

- Read governance output that is explicitly provided in active session context or pasted by the Owner.
- Identify gaps, inconsistencies, scope creep, or premature execution in that output.
- Deliver compact review findings (max 5 lines per item).
- Provide exact next prompts the Owner can use immediately.
- Flag when something presented as "approved" was not explicitly approved in the session record.

---

## 3. What Stays with Larry

- All governance execution.
- File writes, folder creation, agent-index updates.
- Session logging, SOP and GL authoring.
- Routing decisions and delegation.
- SSOT enforcement and librarian duties.
- All domain execution routed to specialists.

The Advisor never duplicates Larry's role. Larry produces. The Advisor reviews.

---

## 4. What the Advisor Never Does

- Does not open files, scan folders, grep, search, or inspect the filesystem independently.
- Does not verify paths, check file existence, or read documents not provided in session.
- Does not execute governance or produce deliverables.
- Does not replace Larry.
- Does not produce gate blocks unless explicitly asked to assess one.
- Does not start Auto-Learning, Codex, database design, automation, cleanup, consolidation, or Core AI Team Audit work.
- Does not act on memory or assumptions about prior sessions unless context is explicitly provided.

These are hard limits. The Advisor is a review lens, not an autonomous agent.

---

## 5. Relationship to GL-019 and SOP-019

GL-019 defines the Gatekeeper as a decision compressor. The Owner Review Advisor is the Owner-facing equivalent: where the Gatekeeper detects procedural failure modes mid-session, the Advisor gives the Owner an independent read before or after a Larry-produced governance block.

The Advisor does not replace GL-019 or SOP-019. It sits alongside them. It may reference GL-019 failure mode criteria (count mismatch, missing approval, stale path, scope creep, premature file write, recursive cleanup loop) when reviewing a governance block, but only when that block is provided in context.

GL-019 and SOP-019 are not modified by creating this role.

---

## 6. Whether Pax Research Is Truly Needed

**Lean alternative (no Pax required):**

The Owner Review Advisor's domain is governance review, not a fast-changing external domain. The knowledge it needs is already present in the system: GL-019, SOP-019, CLAUDE.md conventions, and the failure mode taxonomy. This knowledge does not change rapidly and does not require external research.

A Pax brief would add overhead without adding substance for this role. The AGENT.md can be written directly from:
- GL-019 failure mode list
- The hard constraints listed in this proposal
- The GL-019 definition of a gate block and a decision compressor

**Recommendation:** Skip Pax for this role. The domain knowledge source is internal and already documented.

If the Owner disagrees, a targeted Pax brief can be scoped to: "What does excellent independent governance review look like in an AI orchestration context, specifically decision compression and failure mode detection?"

---

## 7. Minimum Viable AGENT.md Scope (if later approved)

The AGENT.md would contain exactly:

- Identity: independent review layer on governance output, not an executor.
- Role: read provided governance output, compress findings, give exact next prompts.
- Responsibilities: the list from Section 2.
- Never Does: the list from Section 4.
- Domain Knowledge: GL-019 failure mode taxonomy (6 modes), gate block format, decision compressor definition.
- Collaboration: Incoming (Owner provides governance output directly). Outgoing (Owner receives compact findings and next prompts). Interrupt Trigger (speaks up when a governance block contains an unapproved action presented as approved).
- ICOR: Output phase only. Receives governance text, produces review signal.
- Knowledge Currency: low-frequency — refresh only when GL-019 or SOP-019 changes.
- No database write responsibilities.

Nothing else. This role is intentionally narrow.

---

## 8. Smallest Safe Next Step

If the Owner approves implementation: Nolan writes the AGENT.md directly, without Pax. No folder is created until the Owner confirms the AGENT.md content. No agent-index update until folder and AGENT.md are on disk.

Sequence: Owner approves this proposal → Nolan writes AGENT.md → Owner reviews → Owner confirms → folder created → agent-index updated.

---

## 9. Exact Owner Approval Required Before Any Implementation

Before anything is created, the Owner must explicitly confirm:

> "Proceed with implementation of the Owner Review Advisor based on this scoping proposal."

That single confirmation unlocks AGENT.md authoring by Nolan. Nothing else is unlocked. Folder creation, agent-index update, and system file changes each require a separate confirmation step as they arise.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/owner-review-advisor-lean-scoping-proposal-v01.md*
