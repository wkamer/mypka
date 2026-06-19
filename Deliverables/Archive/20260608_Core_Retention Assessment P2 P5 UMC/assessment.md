# Retention Assessment — P2 and P5
## Source: 20260530_Core_UMC diagnose en aanbevelingen

**Prepared by:** Larry, Team Orchestrator  
**Date:** 2026-06-08  
**Scope:** Knowledge retention required for archive eligibility. No governance routing. No implementation analysis.

---

## P2 — Delegation Model

### 1. Knowledge lost if archived today

The specification of what replaces the removed write_summary instruction in AGENT.md.

Specifically:
- Specialists do not have their own session boundaries and therefore cannot call write_summary autonomously. This is the architectural reason the UMC section was removed from all 14 AGENT.md files.
- The intended replacement: when a specialist finishes a substantive task, she writes a one-line handoff note to session context. The close-session routine reads the handoff notes and writes one composite UMC summary per domain active in the session, with the correct source_type per GL-015 §3.

Without this, there is no specification anywhere for how UMC writes should work for specialists. Any future AGENT.md revision or specialist onboarding has no reference.

### 2. Minimum retention action

Add one short section to GL-013 (Memory Core Architecture) stating:
- Why specialists do not write to UMC directly (no session boundary).
- What the operational model is: handoff note to session context, composite summary by close-session per active domain.
- Which source_type applies per specialist (pointer to GL-015 §3).

No new document needed. No proposal text. A 6-to-10-line operational note in the existing architecture document is sufficient.

### 3. Proposed landing location

**GL-013 — Memory Core Architecture**, new section: "Specialist UMC Write Protocol."

GL-013 is the authoritative document for UMC architecture decisions. This is the natural home.

### 4. Safe to archive after landing?

**Yes.** Once the specification is in GL-013, the source deliverable carries no unique knowledge on this item.

---

## P5 — Periodic Validation

### 1. Knowledge lost if archived today

The requirement specification for UMC health monitoring:
- What to monitor: entry count per domain per week.
- Threshold: alert when any domain goes silent for 7+ days.
- Alert target: Discord or Team Inbox.
- Rationale: no current mechanism detects UMC write failures or domain silence.

This threshold and target do not appear anywhere else in the knowledge architecture.

### 2. Minimum retention action

Add one short note to GL-013 (Memory Core Architecture) under a "Known Gaps" or "Future Enhancements" subsection stating the requirement, the threshold (7 days), and the alert target.

This is a requirement note, not implementation instructions. Three to five lines.

### 3. Proposed landing location

**GL-013 — Memory Core Architecture**, subsection: "Known Gaps and Future Enhancements."

Same document as P2. Both items belong to the UMC architecture layer.

### 4. Safe to archive after landing?

**Yes.** Once the threshold and alert target are recorded in GL-013, the source deliverable carries no unique knowledge on this item.

---

## Combined Assessment

Both items land in GL-013. Two short additions to one document. After both are written, the source deliverable `20260530_Core_UMC diagnose en aanbevelingen` becomes safe to archive.

The source deliverable contains additional content (UMC table inventory, agent coverage audit, root cause analysis) that is diagnostic in nature and does not need to be retained in the active knowledge architecture. That content is historical record, not operational specification. It is appropriate archive material.

**Blocker for archive eligibility: GL-013 additions not yet written.**  
**Action required: Owner authorization to write to GL-013.**

---

Delivered on: 2026-06-08  
Delivered at: (session)
