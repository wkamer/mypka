# Improvement Candidate: Post-Implementation Assurance Checklist for Governance Specs

**Type:** Governance improvement candidate
**Origin:** Track 1 reactive cleanup — session 2026-06-16
**Status:** Captured, not implemented
**Captured by:** Larry

---

## Problem Statement

After implementing a governance spec into CLAUDE.md (or any system file), myPKA has no forced post-implementation assurance path. Cleanup obligations exist but are not enforced:

- `deliverable_lifecycle` metadata fields (agent, source_session) may remain NULL
- `team_tasks` rows for the implementation work may remain open
- `Deliverables/INDEX.md` may be stale

In the Track 1 session (2026-06-16), all three gaps were found and repaired reactively. Without the explicit Track 1 check, they would have persisted undetected.

**Concrete evidence:**
- `deliverable_lifecycle` id 76: `agent` was NULL, `source_session` was NULL
- `team_tasks` id 99: remained open after implementation was complete
- `Deliverables/INDEX.md`: not refreshed after new D-folder was created

---

## Proposed Future Improvement

Add a mandatory post-implementation assurance checklist to CLAUDE.md (or a new SOP) that triggers automatically after any governance spec is implemented into a system file. The checklist enforces: (1) close the originating `team_tasks` row, (2) complete `deliverable_lifecycle` metadata fields (agent, source_session, state_changed_at), (3) refresh `Deliverables/INDEX.md`, and (4) confirm to the owner with a brief verification report. This turns post-implementation cleanup from a reactive discovery step into a mandatory, sequenced assurance obligation that runs every time without exception.

---

## Why Separate From Track 1

Track 1 was reactive: it verified and repaired the specific gaps found for D-folder id 76. It did not change any system behavior. Track 2 changes system behavior: it adds an enforced structural path so these gaps cannot occur again for any future governance spec implementation. Track 1 had a defined scope (one D-folder), a known endpoint (all gaps closed), and no new system components. Track 2 requires at least one new system component (a checklist rule in CLAUDE.md or a new SOP) and applies to all future implementations, not just this one.

---

## Smallest Next Step

When ready to implement Track 2: run GL-023 in full, write the spec, present to owner for authorization, then implement as a CLAUDE.md section or SOP.

---

Captured on: 2026-06-16
Captured at: session — Proactive Larry Trigger Library and Pre-Action Gate (Track 2 split)
