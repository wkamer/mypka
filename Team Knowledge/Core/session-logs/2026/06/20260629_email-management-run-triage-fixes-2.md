# Session Log — Email management: Run Triage slice, triage fixes, infrastructure (2)

**Date:** 2026-06-29
**Agent:** Larry
**Domain:** Team
**DB id:** 268

---

## What happened

Built Slice 5 Run Triage button with loading/error/empty/success states. Fixed three bugs discovered post-delivery: frontend pending filter was too broad (triage_error emails showing in Pending section), Gmail sync was limited to UNREAD only (changed to all INBOX, maxResults 50), and a critical AI subprocess bug — the Claude CLI was picking up CLAUDE.md from the repo root, loading the Larry orchestrator context, and refusing all email bodies as prompt injection attempts. Every email got triage_error as a result. Fixed by running the subprocess from `cwd="/"`. Added passwordless sudoers rule so agents can restart the backend without a terminal prompt.

## Decisions

- Devon stays in the routing loop — Larry never spawns Codex directly
- One brief = one task, run in parallel for speed (violated this session — caused 17-min build times)
- Sudoers rule scoped to one command only (`systemctl restart mypka-dashboard-backend`)
- All AI subprocesses calling the Claude CLI must use `cwd="/"` to avoid picking up project CLAUDE.md

## Actions taken

- Quinn spec Slice 5 Run Triage → `Quinn-interaction-spec-slice5-run-triage.md`
- Sloane G4 brief Slice 5 → `Sloane-g4-brief-slice5-run-triage.md`
- Devon built Slice 5 — Run Triage button, aria-live, loading/error/empty states (commit 551dcd6)
- Devon fixed status alias in serializer + verified ordering (commit e3c61c6)
- Devon fixed pending filter + Gmail scope (INBOX, maxResults 50) + ordering rollback (commit d8f3d2a)
- Devon fixed AI subprocess cwd + triage_error retry with OR REPLACE (commit 7ae893b)
- Kai added `/etc/sudoers.d/mypka-dashboard` — passwordless backend restart for admin user
- Backend restarted with new code live

## Open items

- **Owner action:** Click Run Triage in live dashboard — confirm 30 emails process correctly after cwd fix
- Context discipline violated this session — /compact must run after each task block
