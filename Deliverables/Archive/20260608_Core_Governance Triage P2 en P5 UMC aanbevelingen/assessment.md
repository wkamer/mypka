# Governance Triage Assessment
## UMC Diagnosis Recommendations P2 and P5

**Prepared by:** Larry, Team Orchestrator  
**Date:** 2026-06-08  
**Source deliverable:** `Deliverables/20260530_Core_UMC diagnose en aanbevelingen/rapport.md`  
**Eligibility context:** `Deliverables/20260608_Core_UMC Archive Eligibility Analysis 20260530/analysis.md`  
**Scope:** Read-only assessment. No files modified. No databases modified. No tasks created. No system files updated.

---

## Purpose

The archive eligibility analysis established that P2 (Delegation Model) and P5 (Periodic Validation) are not captured in the active knowledge architecture and must be formally retained before the source deliverable can be archived.

This assessment determines the governance classification, recommended destination, and required route for each item before any retention or implementation action is authorized.

---

## Frameworks Applied

| Framework | Role in this assessment |
|---|---|
| GL-022 — Learning Candidate Lifecycle | Determines whether an item qualifies as an LC, at what level, and with what triage routing |
| GL-018 — Idea Routing and Implementation Governance | Determines whether a proposal is required, what impact label applies, and what route governs implementation |
| GL-014 — AI Team Governance | Defines which actions require explicit Owner approval vs. which may proceed independently |

---

## Item 1 — P2: Delegation Model

### 1. Structural or session-specific?

**Structural.**

P2 describes a permanent change to the operational model governing how all 14 specialist agents interact with the UMC at session close. The affected components are:

- CLAUDE.md — UMC section (session-close write_summary instruction)
- All 14 AGENT.md files — UMC section content
- close-session skill — must implement the composite summary per active domain
- GL-013 — Memory Core Architecture (authoritative spec for UMC operational model)

None of these changes are scoped to a single session. The change is system-wide and permanent.

---

### 2. Graduation Candidate, Learning Candidate, both, or neither?

**Neither — confirmed structural change.**

GL-022 Section 2 defines three levels:

- Level 1: autonomous behavioral change, never registered as an LC.
- Level 2: registered in `learning_candidates`, may be escalated to `graduation_candidate` at triage.
- Level 3: confirmed structural change requiring SOP-019, never entered as an LC record.

The criterion for Level 2 is: "not yet a confirmed structural change requiring SOP-019."

P2 does not meet the Level 2 criterion. The architectural gap is confirmed, the affected system files are identified, and the required changes are specific and non-speculative. A third party reading any of the 14 AGENT.md files today would find no UMC write instruction at all — the old instruction was removed, the replacement was never written. This is a confirmed gap in the system specification, not an uncertain behavioral observation.

The LC track (including the Graduation Candidate escalation path) does not apply. P2 routes outside the LC lifecycle.

**Classification under GL-018:** This is an S7-class idea (structural system change) with Medium impact (affects 14 AGENT.md files, close-session skill, CLAUDE.md, and GL-013; no data loss risk; reversible). Under GL-018 P5, a Medium-impact idea requires a proposal and Review Gate before implementation.

---

### 3. Recommended destination

A formal proposal document, to be prepared by Kai (technical specification) and reviewed by Nolan (AGENT.md and GL impact), before Owner authorization. The proposal must specify:

1. The replacement operational model: what specialists do (handoff note to session context) vs. what the close-session routine does (composite UMC summary per active domain with correct source_type per GL-015 §3).
2. The exact changes to CLAUDE.md, AGENT.md template, close-session skill, and GL-013.
3. Backward compatibility: whether existing sessions with the old pattern require remediation or are covered by the GL-015 §5.1 non-remediation principle.

Once accepted by the Owner: implementation per standard GL-018 route.

---

### 4. Rationale

The observation originated in a formal diagnosis report by a specialist (Kai). The gap is confirmed through structural evidence: AGENT.md files have no UMC section, no replacement model exists anywhere in the knowledge architecture, and CLAUDE.md still references write_summary as an agent responsibility. Left unaddressed, any future AGENT.md revision or specialist onboarding will recreate the old broken pattern (or produce no UMC write guidance at all, which is the current state).

A proposal is the appropriate governance instrument because the change touches system-critical files (AGENT.md × 14, CLAUDE.md, GL-013) and requires Owner authorization per GL-014 Section 1.

---

### 5. Proposal required before implementation?

**Yes.** All target files require explicit Owner approval per GL-014 Section 1 ("Only after explicit Owner approval" category). No implementation action — not a single file write, no CLAUDE.md edit, no close-session skill change — may proceed without an accepted proposal and Owner confirmation.

---

### 6. Recommendation: Retain, Implement, Defer, or Reject?

**Retain.**

The knowledge in P2 represents a confirmed unresolved architectural gap. Archiving the source deliverable before this gap is formally routed would destroy the specification record. The recommendation must be formally retained by registering the gap in the governance queue (a deliverable-lifecycle item or a formal proposal brief) before archive proceeds.

Implementation timing is a separate Owner decision. This assessment does not recommend immediate implementation — only that the routing is formally established so the knowledge is not lost.

---

## Item 2 — P5: Periodic Validation Cron

### 1. Structural or session-specific?

**Structural.**

P5 proposes adding a recurring automated UMC health check: a weekly job that counts UMC entries per domain, compares against a minimum activity threshold, and posts an alert when any domain goes silent for 7+ days. This is new infrastructure (new script, new cron or n8n job, new alert integration). It operates independently of individual sessions.

---

### 2. Graduation Candidate, Learning Candidate, both, or neither?

**Learning Candidate with Graduation Candidate routing — secondary; primary route is GL-018.**

The underlying observation — the team has no visibility into whether the UMC is receiving writes, and a domain could go silent without detection — qualifies as a Level 2 Learning Candidate under GL-022 Section 2. The observation was encountered during Kai's diagnosis execution. A third party reading AGENT.md would not predict that this monitoring gap exists. The observation is not yet a confirmed structural change (no implementation decision has been made); it is a flagged gap requiring Owner routing.

However, the primary and more direct route is GL-018. P5 is an enhancement idea that proposes creating a new system component. GL-018 P2 is satisfied: the idea requires creating a script, a cron job, and an alert integration. A proposal is the required governance instrument.

If captured as an LC: `learning_scope = tooling`, `triage_routing = graduation_candidate`, `processed_outcome = backlog_item`. The LC would reach `processed` status when a formal proposal brief exists, and `closed` when the Owner has made a routing decision (implement, defer, or reject).

The LC capture is optional and secondary. The governance path is GL-018.

---

### 3. Recommended destination

Two parallel actions, each requiring separate authorization:

**A — Knowledge retention (immediate priority):**  
Add a "Future Enhancements" subsection to GL-013 (Memory Core Architecture) documenting the P5 requirement: what is monitored (entry count per domain per week), the threshold (7-day silence trigger), and the alert target (Discord or Team Inbox). This ensures the requirement survives independent of whether it is ever implemented, and prevents it from decaying to zero if the source deliverable is archived.

This requires Owner authorization per GL-014 (GL-013 is a system file).

**B — Implementation route (deferred until Owner decides):**  
When the Owner chooses to proceed with implementation: GL-018 routing as a Low-to-Medium impact idea (new monitoring script; no modification of existing behavior; reversible). A lightweight proposal (Route B conditions may apply per GL-018 P6 exception) documenting the script specification, cron schedule, alert format, and ownership (Kai).

---

### 4. Rationale

P5 is not urgent. No current failure results from the absence of UMC monitoring. The risk is gradual: a domain could go silent without detection, and the team would only notice at the next session or never. The diagnosis report provided the threshold logic (7-day silence window) which is the specific knowledge that would be lost upon archive.

The knowledge retention action (GL-013 Future Enhancements) is separated from the implementation route because the Owner may choose to defer or reject implementation while still needing the requirement documented. A team_tasks row alone is insufficient for knowledge retention because task rows can be closed or pruned without the rationale surviving.

---

### 5. Proposal required before implementation?

**Yes.** Creating a new cron job, monitoring script, and alert integration creates a new system component. GL-014 requires Owner approval. GL-018 P2 threshold is met. A proposal (potentially lightweight per Route B conditions) is required before Kai writes a single line of code.

---

### 6. Recommendation: Retain, Implement, Defer, or Reject?

**Defer with knowledge retention.**

P5 is a legitimate enhancement with a clear specification. It is not urgent. The appropriate disposition is:

1. Retain the requirement by documenting it in GL-013 (requires Owner authorization before execution).
2. Defer implementation until the Owner decides to route it through GL-018.

This is distinct from "reject." The recommendation in the source deliverable is sound. The question of when to implement is a capacity and priority decision for the Owner, not a governance deficiency.

---

## Summary Table

| # | Item | Structural | LC / GC | Primary route | Proposal required | Recommendation |
|---|---|---|---|---|---|---|
| P2 | Delegation Model | Yes | Neither (Level 3 equivalent) | GL-018 proposal (Medium impact) | Yes | Retain — register in governance queue before archive |
| P5 | Periodic Validation | Yes | LC optional (GC routing, backlog_item outcome) | GL-018 proposal (Low-Medium impact) | Yes | Defer + retain via GL-013 Future Enhancements |

---

## Open Item: Deliverable Lifecycle Registration

This deliverable (`20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen`) was not registered in `deliverable_lifecycle` at creation. The Owner's scope constraint for this session ("Do not modify databases") blocked the mandatory INSERT. Registration is required before session close.

**Pending action:** Larry to register this deliverable (artifact_type: `triage_document`, destination_domain: `Core`, state_gl017: `active`, workstream_code: `DLH`) upon Owner authorization to write to the database.

---

## Next Decision Required from Owner

For each item, one decision is needed:

**P2:**  
a) Authorize Larry to route P2 to Kai and Nolan for proposal preparation.  
b) Defer — flag as open item without active routing.  
c) Reject — close the gap as-is; document the decision.

**P5:**  
a) Authorize Larry to update GL-013 with a Future Enhancements entry (knowledge retention only, no implementation).  
b) Authorize Larry to route P5 to Kai for a lightweight proposal (retention + implementation path).  
c) Defer — no action at this time.  
d) Reject — document the decision.

Neither decision authorizes implementation. Both are classification and routing decisions only.

---

Delivered on: 2026-06-08  
Delivered at: (session)
