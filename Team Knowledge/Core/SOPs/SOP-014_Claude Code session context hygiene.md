# SOP-014 — Claude Code Session Context Hygiene

**Scope:** All agents running in Claude Code
**Maintainer:** Larry
**Status:** Active

---

## Purpose

Prevent Claude Code sessions from reaching the 1M token boundary during active
audit or implementation work. Late compaction at 1M tokens requires usage credits
and is not a reliable recovery strategy. Context hygiene must be proactive.

---

## Tool roles

| Tool | Purpose | When to use |
|---|---|---|
| `/compact` | Proactive mid-session context reduction | When context grows during ongoing work — before it becomes a problem |
| `/close-session` | Governance closure | When a task is complete and audit trail is written |
| New session | Clean start for the next task | Default after `/close-session` — every new B-item gets a fresh session |

The default end-of-item flow:
`/close-session` → start new Claude Code session with minimal handoff context.

`/compact` is not the default end-of-item action. It is used when continuing within
the same session before context grows too large.

---

## Context size thresholds

| Threshold | Action |
|---|---|
| ~600K tokens | Run `/compact` if continuing in the same session |
| ~700K tokens | Run `/compact` before starting any new work — mandatory |
| ~800K tokens | Stop starting new work — close session or compact immediately |
| 1M tokens | Failure condition — do not allow sessions to reach this boundary |

---

## Session size limits

One large B-item per Claude Code session.
Two small B-items only if context remains clearly under 600K after the first.
If context is at or above 600K after the first item: close and hand off.

---

## End-of-item default flow

Task complete → audit trail written → /close-session → new Claude Code session.

Brief the new session: task ID, approved proposal reference, execution state
(what is done, what is pending).

---

## Output minimization

**Write to file:** proposals, execution reports, closure reports, code blocks
over 20 lines, command output over 30 lines required as audit evidence.

**In chat only:** deliverable path, status, short summary (3–5 lines), deviations,
blockers, recommended next step.

Do not paste full proposals, reports, file read-backs or long output in chat unless
Owner explicitly requests it. If requested, paste once and run `/compact` immediately.

For verification read-backs: quote only the relevant excerpt (≤10 lines).

---

## `/clear` guidance

`/clear` is not part of normal audit execution.

Use only when: no active task, no approved execution pending, no file writes pending,
no audit trail obligation open, session is purely exploratory.

If any condition above is not met: do not use `/clear`. If in doubt: do not use `/clear`.

---

## Changelog

- 2026-06-03 (Larry, B-031A): Created. Approved by Owner Walter Kamer.
