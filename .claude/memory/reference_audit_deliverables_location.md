---
name: reference_audit_deliverables_location
description: "All AI team audit execution results go to the central audit report folder, not a separate deliverable folder per item"
metadata: 
  node_type: memory
  type: reference
  originSessionId: bd8fdb6f-da76-4b2f-b172-a8409f629938
---

All audit execution reports (B-NNN execution reports, proposals, verification reports) go to:

`Deliverables/20260603_Core_AI Team Audit Report/`

Filename convention: `B-NNN-execution-report.md` (lowercase, hyphens).

**This folder is temporary** — it exists only for the duration of the AI team audit. Final destination will be determined when the audit is complete.

**Why:** Owner corrected this during B-031B — a separate folder per B-item is wrong. All audit artefacts live in one central temporary folder for the duration of the audit.

**How to apply:** Never create a new `Deliverables/YYYYMMDD_Core_B-NNN .../` folder for audit work. Always write directly to the central audit folder above. When the audit is fully complete, ask the owner where the artefacts should move.
