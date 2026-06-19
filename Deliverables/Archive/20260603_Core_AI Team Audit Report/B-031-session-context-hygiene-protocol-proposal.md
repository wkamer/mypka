# B-031 Proposal — Claude Code Session Context Hygiene Protocol

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Problem

During B-021B execution, the Claude Code session accumulated context from multiple proposal revisions (v0.1 → v0.3), full file read-backs, execution reports and inline pasted deliverables. The session reached the 1M token boundary mid-execution.

At that point, `/compact` failed with:

```
API Error: Usage credits required for 1M context · turn on usage credits at
claude.ai/settings/usage, or use --model to switch to standard context
```

The session could not be compacted without enabling paid usage credits. The session continued without compaction, which increased the risk of losing context mid-task and made subsequent compaction attempts more expensive or impossible.

This is an execution risk, not just a comfort issue: if context overflows during an active implementation (file writes in progress, audit trail pending), the session terminates mid-state.

---

## 2. Why Late `/compact` Is Unsafe

`/compact` works by sending the full conversation to the Claude API for summarization. That summarization step itself requires a model that supports the current context size.

| Context size | `/compact` behavior |
|---|---|
| Under ~800K tokens | Works on standard context model — free |
| ~800K–1M tokens | May still work, increasingly slow |
| At or above 1M tokens | Requires a 1M-context model — usage credits required |

The consequence: `/compact` used as a rescue action after the session is already too large requires the same resource it was supposed to avoid paying for. It is not a reliable recovery mechanism.

Late compaction also carries a secondary risk: the summarization of a very large context may lose detail. Mid-execution state (pending file writes, audit trail rows not yet committed) may not survive the summary.

**Conclusion:** Context hygiene must be proactive. The session must never reach 1M tokens as a normal operating condition.

---

## 3. Proposed Context Hygiene Rule

**Rule:** Context hygiene is a first-class operational constraint. Every agent and every session must treat context size as a finite resource. Compaction, output minimization, and session boundaries are mandatory hygiene — not optional when convenient.

This rule has two components:
- **Session discipline:** when to compact and when to start a new session.
- **Output minimization:** what goes in chat vs. what goes to file.

---

## 4. Operational Thresholds

### 4.1 Compaction triggers

| Trigger | Action |
|---|---|
| After every completed B-item (execution report confirmed) | Run `/compact` |
| After every large deliverable (closure report, backlog registration) | Run `/compact` |
| After every full file read-back of a large file (>100 lines) | Run `/compact` if session is active |
| Claude Code context indicator reaches ~600K tokens | Run `/compact` immediately, before starting the next task |
| Claude Code context indicator reaches ~700K tokens | Run `/compact` — mandatory, do not defer |

### 4.2 Session boundaries

| Condition | Action |
|---|---|
| Maximum 2 B-items per Claude Code session | Start new session after the second item is closed |
| After execution report is written and confirmed | Start new session before beginning next B-item |
| After closure report | Start new session |
| After backlog registration | Start new session if session is already ~2 items deep |

### 4.3 When NOT to rely on `/compact`

- Never use `/compact` as the primary strategy for managing a session that has already grown large.
- Never defer compaction to end-of-session when mid-session compaction was available.
- Never run multiple large file read-backs without an intermediate compact.

---

## 5. Output Minimization Rules

### 5.1 What goes to file

All of the following must be written to a deliverable file, not pasted in chat:

- Proposals (all versions)
- Execution reports
- Closure reports
- Backlog registrations
- Full file read-backs referenced for verification
- Large code blocks (>20 lines)
- Full logrotate output, script output, or tool output over ~30 lines

### 5.2 What goes in chat

Chat output must contain only:

- Deliverable path
- Status (DONE / BLOCKED / FAILED)
- Short summary (3–5 lines maximum)
- Deviations
- Blockers
- Next step

### 5.3 Explicit exceptions

The Owner may request that a deliverable be pasted in chat for review. In that case, paste the content once and immediately run `/compact` afterward.

### 5.4 Inline read-backs

When verifying a file after a write, do not read it back in full in chat. Confirm specific lines or criteria by quoting only the relevant excerpt (≤10 lines).

---

## 6. Tool Usage Guide

### `/compact`
**Use when:** Context exceeds 600K tokens, or after every completed task block.
**Effect:** Summarizes the full conversation into a compressed context. Loses fine detail; major decisions are preserved.
**Constraint:** Must be used before reaching 1M tokens. At 1M+, usage credits are required.

### `/close-session`
**Use when:** Session is genuinely complete — all tasks done, audit trail written, no open writes pending.
**Effect:** Runs the full session close routine (session log, UMC summary, open items sweep).
**Note:** Do not substitute `/compact` for `/close-session`. They serve different purposes.

### New Claude Code session
**Use when:** Starting a new B-item after the previous one is closed and reported. After 2 B-items in one session regardless of size. After a context limit interruption.
**Effect:** Fresh context, zero accumulation risk.
**Note:** Brief the new session with: task ID, approved proposal version, current execution state.

### `/clear`
**Use when:** A side conversation or exploratory exchange produced significant context that is not relevant to the current task.
**Effect:** Clears the current conversation. Use with caution — clears all context including pending state.
**Constraint:** Only use if no writes are pending and audit trail is complete.

---

## 7. Recommended Storage Location

Three options are considered.

### Option A — GL-005 (AI Engineering Operating System)
**For:** The output minimization rules and the "context hygiene as first-class constraint" principle.
**Rationale:** GL-005 governs all engineering behavior. Context hygiene is an engineering discipline. Output minimization rules belong alongside the existing Development rules and Production safety sections.
**Risk:** GL-005 is already large. Adding a new section increases length.

### Option B — CLAUDE.md (Larry's operational rules)
**For:** The operational thresholds (600K/700K triggers, 2-item-per-session rule, session boundary rules).
**Rationale:** CLAUDE.md contains Larry's live operational rules. Session discipline is Larry's responsibility as session author. These rules are only meaningful in the context of Larry's orchestration.
**Risk:** CLAUDE.md is long. Adding more operational rules risks being missed in practice.

### Option C — New SOP (Recommended)
**For:** The complete protocol as a standalone SOP.
**Rationale:** An SOP is atomic, referenceable, and readable by any agent. The protocol is procedural (when to act, what to do, what not to do) — this fits the SOP format exactly. GL-005 and CLAUDE.md can reference the SOP rather than duplicate it.
**Filename:** `SOP-NNN_Claude Code session context hygiene.md`
**Plus:** Add a one-line reference in GL-005 §Development rules and one-line reference in CLAUDE.md §Operational Conventions.

### Recommendation
**Option C** — new SOP, plus one-line pointers in GL-005 and CLAUDE.md.

---

## 8. Proposed Rule Text

### 8.1 SOP body (proposed)

```markdown
# SOP-NNN — Claude Code Session Context Hygiene

**Scope:** All agents running in Claude Code
**Maintainer:** Larry
**Status:** Active

---

## Purpose

Prevent Claude Code sessions from reaching the 1M token boundary during active
audit or implementation work. Late compaction at 1M tokens requires usage credits
and is not a reliable recovery strategy.

---

## Rule

Context hygiene is a first-class operational constraint. Context size is treated as a
finite resource. Compaction, output minimization, and session boundaries are mandatory
hygiene — not optional when convenient.

---

## Compaction triggers

Run `/compact` after every completed B-item or large deliverable.
Run `/compact` when context reaches ~600K tokens — mandatory at ~700K.
Never defer compaction to end-of-session when mid-session compaction was available.
Never use `/compact` as a rescue action after reaching 1M tokens.

---

## Session boundaries

Maximum 2 B-items per Claude Code session.
Start a new session after an execution report or closure report is confirmed.
Brief the new session: task ID, approved proposal version, current execution state.

---

## Output minimization

Write to file: proposals, execution reports, closure reports, large code blocks (>20 lines),
tool output over ~30 lines.

In chat: path, status (DONE/BLOCKED/FAILED), 3–5 line summary, deviations, blockers, next step.

Do not paste full file read-backs in chat. Quote only the relevant excerpt (≤10 lines) for verification.

---

## Tool usage

| Tool | Use when |
|---|---|
| `/compact` | Context >600K tokens, or after every completed task block |
| `/close-session` | Session complete — all tasks done, audit trail written, no pending writes |
| New session | After 2 B-items, after a closure report, after any context limit interruption |
| `/clear` | Only if no writes are pending and audit trail is complete |
```

### 8.2 Pointer for GL-005 (proposed addition to §Development rules)

```
Context hygiene: see SOP-NNN Claude Code session context hygiene. Compact proactively
after every task block. Output to file, not chat.
```

### 8.3 Pointer for CLAUDE.md (proposed addition to §Operational Conventions)

```
Session context hygiene: see SOP-NNN_Claude Code session context hygiene. Run /compact
after every completed B-item. Maximum 2 B-items per session. Deliverables to file only —
chat contains path, status, summary, deviations, blockers, next step.
```

---

## 9. Risks and Owner Decisions Required

| # | Risk | Owner decision required |
|---|---|---|
| 1 | SOP number not yet assigned — the sop-index must be read to determine the correct NNN | Larry reads sop-index before writing SOP |
| 2 | Pointer placement in GL-005 — must not disrupt existing section flow | Owner confirms placement (after Development rules or new section?) |
| 3 | Pointer placement in CLAUDE.md — must not duplicate existing rules already in memory | Owner confirms placement |
| 4 | Output minimization rule could conflict with Owner preferences — Owner sometimes wants full content pasted for review | Owner confirms: is the "paste on explicit request" exception sufficient? |
| 5 | `/clear` guidance may be too permissive — clearing context during execution is destructive | Owner confirms: include or exclude `/clear` from the SOP? |

---

## 10. Approval Gate

Owner Walter Kamer must explicitly approve one of the following before any file is modified:

**A — Approve as proposed (Option C: SOP + pointers in GL-005 and CLAUDE.md)**
Execution proceeds: Larry reads sop-index, creates SOP file, adds pointer lines to GL-005 and CLAUDE.md.

**B — Approve SOP only (no GL-005 or CLAUDE.md changes)**
Only the SOP file is created. Agents must discover it by reading the SOP index.

**C — Approve GL-005 addition only (no separate SOP)**
The full rule text is added to GL-005 as a new section. No SOP file.

**D — Approve CLAUDE.md addition only**
The operational thresholds are added to CLAUDE.md. No SOP, no GL-005 change.

**E — Reject**
Proposal is archived. No files are modified.

No partial execution. No file is modified until the Owner has confirmed which option applies.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-031-session-context-hygiene-protocol-proposal.md`*
