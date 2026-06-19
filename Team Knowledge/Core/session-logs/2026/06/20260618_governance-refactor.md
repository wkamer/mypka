# Governance refactor — simplified to 4-component framework

**Date:** 2026-06-18
**Agent:** Larry
**Domain:** Team

---

## What happened

Ran /improve-system audit. Found:
- Dead entries in SOP-index (SOP-007, SOP-015old, SOP-016, SOP-017, SOP-019) and GL-index (GL-013, GL-015, GL-016, GL-017, GL-018, GL-019, GL-022) — all cleaned.
- Broken governance framework: SOP-018 (active) referenced SOP-016, SOP-017, and GL-015 as required companion sources — all three archived.
- Feedback propagation gaps: communicatie_verzender rule missing from Sienna AGENT.md; health_resources_ke rule missing from Lena AGENT.md.

After full analysis of the governance stack (GL-016 through GL-022, SOP-015 through SOP-019), concluded the framework was over-engineered for a solo-owner AI team. Replaced with a 4-component framework.

## Decisions

- Governance simplified to: GL-014 + GL-021 + GL-023 + SOP-015 + Iris
- SOP-018 (Idea-to-Implementation, S1-S10 scenarios, DP-1 through DP-6) archived — routing logic already in CLAUDE.md
- GL-020 (Intent Classification Taxonomy, CAT-1 through CAT-6) archived — not referenced in daily operations
- Deliverable lifecycle rule consolidated into SOP-015 (one line)
- All other governance docs (SOP-015old/016/017/019, GL-016/017/018/019/022) confirmed permanently archived

## Actions taken

- Cleaned SOP-index: removed 5 archived entries
- Cleaned GL-index: removed 7 archived entries
- Wrote `SOP-015_System File Change Proposal Procedure.md` — 1-page, 4-step procedure
- Archived SOP-018 and GL-020
- Updated GL-021: removed dead cross-references (GL-020, SOP-019, GL-019), updated CAT-3 language to plain English
- Updated GL-014: fixed UMC reference in §7 SSOT hierarchy
- Added SOP-015 to SOP-index
- Nolan updated Iris AGENT.md: removed archived refs, added SOP-015 invocation rule, updated source basis

## Open items

- team_task 103: Nolan — add communicatie_verzender rule to Sienna AGENT.md
- team_task 104: Nolan — add health_resources_ke rule to Lena AGENT.md
