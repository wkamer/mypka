# Write Proposal — GL-013 Additions P2 and P5 (v02)

**Prepared by:** Larry, Team Orchestrator  
**Date:** 2026-06-08  
**Revision:** v01 → v02. W-1 and W-2 translated into English. No scope changes.  
**Authorized by retention assessment:** `Deliverables/20260608_Core_Retention Assessment P2 P5 UMC/assessment.md`  
**Target file:** `Team Knowledge/Core/Guidelines/GL-013_Memory Core Architecture.md`  
**Scope:** Two append-only additions to GL-013. No existing content modified or removed.

---

## Write Plan

| # | Action | Location | Trigger |
|---|---|---|---|
| W-1 | Append new section "Operational Model — Specialist UMC Writes" | After the existing `## Beheer` section | Owner: yes |
| W-2 | Append new section "Known Gaps and Future Enhancements" | After W-1 (end of file) | Owner: yes, same write action |

Both additions are appended to the end of the file. No existing lines are changed.

---

## W-1 — Exact Text to Append (P2)

```
---

## Operational Model — Specialist UMC Writes

Specialists are invoked within Larry's session. They have no session boundary of their
own and therefore cannot call `write_summary` autonomously when finishing a task.

**How it works:**
- When a specialist completes a substantive task, she writes one handoff note to the
  session context (e.g., "Sasha completed Shopify product sync").
- The close-session routine reads the handoff notes and writes one composite UMC summary
  per domain active in the session, with the correct `source_type` per domain.
  See [[GL-015_Memory Domain Routing Protocol]] §3 for the canonical domain and
  source_type values per specialist.

The `## UMC` section is absent from individual AGENT.md files for this reason.
The close-session routine is the sole write point for `memory_summaries` originating
from specialist work.
```

---

## W-2 — Exact Text to Append (P5)

```
---

## Known Gaps and Future Enhancements

### UMC Activity Monitoring

No mechanism currently exists to detect whether the UMC is receiving writes. A domain
can go silent without detection.

Requirement: a weekly automated check that counts UMC entries per domain per week and
sends an alert to Discord or Team Inbox when any domain has received no new entries for
7 or more days. Owner: Kai.
```

---

## Post-Write Verification

After writing: Larry reads back the final 40 lines of GL-013 and confirms both sections
are present and correctly formatted before reporting completion to the Owner.

---

## Effect on Archive Eligibility

After W-1 and W-2 are written and verified:

- P2 (Delegation Model) is captured in GL-013. No unique knowledge remains in the source deliverable for this item.
- P5 (Periodic Validation) is captured in GL-013. No unique knowledge remains in the source deliverable for this item.
- The source deliverable `20260530_Core_UMC diagnose en aanbevelingen` becomes safe to archive.

---

## Owner Decision Required

**Approve this write proposal: yes / no / correction.**

A "yes" authorizes Larry to execute W-1 and W-2 in a single write action and perform the post-write read-back.

No other actions are authorized by this approval.

---

Delivered on: 2026-06-08  
Delivered at: (session)
