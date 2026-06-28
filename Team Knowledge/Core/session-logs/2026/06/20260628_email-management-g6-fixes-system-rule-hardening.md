# Email Management G6 fixes + system rule hardening

**Date:** 2026-06-28
**Agent:** Larry
**Domain:** Team
**DB id:** 261

## What happened

G6 review of Email Management Slice 3 surfaced four interaction design failures. Quinn wrote a corrective interaction spec (`Quinn-interaction-spec-slice3-fixes.md`). Devon fixed all four issues (687 lines changed, 72 tests green).

Separately, the G6 session exposed two system rule gaps that were corrected: Quinn activation was on-demand and therefore skippable, and the Codex invocation pattern in Devon and Kai AGENT.md was wrong (they were pointing to an internal runtime they cannot call directly).

## Decisions

- Quinn is mandatory after G2 for all UI features — on-demand activation was insufficient; the G6 rejection proved the gap
- Devon and Kai must spawn `codex:codex-rescue` via the Agent tool — they cannot invoke `codex:codex-cli-runtime` directly (that is an internal contract inside the rescue subagent)
- Cleo does not need Codex enforcement — reverted

## Actions taken

- Quinn wrote `Deliverables/20260626_Email_Management_Prototype/Quinn-interaction-spec-slice3-fixes.md`
- Devon fixed 4 G6 issues in `EmailTriage.jsx` and `email_management.py` (commit `a4ff3af`)
  - Issue 1: log reloads from backend on accordion open; loading/error states; aria-live region
  - Issue 2: log entries timestamp-first (DD Mon YYYY HH:MM), newest at top
  - Issue 3: +Task/+Event rows persist to backend on click; auto-focus on name field
  - Issue 4: resolved state shows static text with submitted name; (untitled)/(no date) fallbacks
- Updated `CLAUDE.md` with Quinn mandatory rule (commit `24c477c`)
- Updated `CLAUDE.md` and Devon/Kai `AGENT.md` with corrected Codex invocation pattern (commit `ca60ade`)
- Reverted Cleo `AGENT.md` (same commit)
- Codex-first as hard mechanical step enforced in Devon and Kai `AGENT.md` (commits `faf82fb`, `936f4d3`)

## Open items

- Dashboard default password (admin/admin) — still not changed
