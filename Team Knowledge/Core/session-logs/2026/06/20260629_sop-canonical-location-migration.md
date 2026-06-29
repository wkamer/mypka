# Session Log — SOP Canonical Location Migration
Date: 2026-06-29
Agent: Larry
Domain: Team
DB id: 269

---

## What happened

Produced two review deliverables: a CLAUDE.md runtime clarity review and a SOP canonical location review. Iris governance review identified a missing Phase 2 trigger in Option B. After Owner decision, executed a bounded Step 1 + Step 2 migration: Team Knowledge/SOPs/ is now the canonical SSOT for team-wide SOPs. 13 SOPs, SOP-index, and Archive moved from Core/SOPs; 14 reference files updated; empty Core/SOPs removed. GL-004 scaffold note corrected. CLAUDE.md runtime cleanup deferred to next session.

---

## Decisions

1. `Team Knowledge/SOPs/` is canonical SSOT for team-wide SOPs (replaces `Team Knowledge/Core/SOPs/`).
2. Devon AGENT.md Codex enforcement line stays — agent-local safety rule, not an SSOT conflict.
3. GL-004 scaffold note correction accepted as within authorized GL-004 edit scope.
4. CLAUDE.md runtime cleanup deferred to next session.
5. Iris LC flag accepted: canonical-declaration-before-migration requires explicit Phase 2 trigger — governance pattern to formalize.

---

## Actions taken

- Created `Team Knowledge/Core/Reviews/20260629_claude-md-runtime-clarity-review-v01.md`
- Created `Team Knowledge/Core/Reviews/20260629_sop-canonical-location-review-v01.md`
- Ran Iris governance review (subagent) — Phase 2 trigger gap identified and resolved
- Created `Team Knowledge/SOPs/` folder
- Updated `CLAUDE.md` Where Things Live: added `Team-wide SOPs → Team Knowledge/SOPs/` row
- Updated `GL-004_Canonical paths.md`: SOPs path changed to `Team Knowledge/SOPs/`; scaffold note updated
- Moved 13 SOPs + SOP-index.md + Archive/ from `Core/SOPs/` to `SOPs/`
- Updated 14 reference files:
  - 5 AGENT.md files: Nolan, Iris, Devon, Sloane, Pax
  - GL-010, GL-014
  - 3 Documents: 00_START_HERE, Governance Pack Design Decisions, Governance Pack Regression Test Reference
  - `.claude/commands/improve-system.md`, `.claude/commands/close-end-of-day-routine.md`
  - `SOPs/SOP-index.md`, `SOPs/Archive/SOP-017_...md`
- Removed empty `Team Knowledge/Core/SOPs/` folder

---

## Open items

- **CLAUDE.md runtime cleanup** — next session. Use `Team Knowledge/Core/Reviews/20260629_claude-md-runtime-clarity-review-v01.md`. New canonical SOP path is `Team Knowledge/SOPs/`. (team_task 113)
- **Governance pattern: canonical-declaration-before-migration** — Iris LC flag. Formalize in a GL file when Owner decides. (team_log 139)
