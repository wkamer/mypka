# B-031 Proposal v0.2 — Claude Code Session Context Hygiene Protocol

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Supersedes:** B-031 v0.1 (2026-06-03)

---

## Change Log (v0.1 → v0.2)

| # | Correction applied |
|---|---|
| 1 | `/compact` / `/close-session` / new session relationship corrected — `/compact` is proactive mid-session maintenance, not the default end-of-item action |
| 2 | Operational thresholds refined — 600K / 700K / 800K boundaries defined; 1M boundary framed as failure condition, not operating condition |
| 3 | Output minimization strengthened — long command output goes to deliverable file, not chat; chat returns only fixed 6-item summary |
| 4 | `/clear` guidance tightened — only in exploratory sessions with no active task, no pending writes, no audit trail obligation |
| 5 | Implementation made execution-ready — exact SOP filename, full SOP content, exact SOP-index row, exact GL-005 pointer with line reference, exact CLAUDE.md pointer with section reference, changelog entries, post-checks, rollback method |
| 6 | Phasing defined — B-031A (SOP + SOP-index) and B-031B (GL-005 and CLAUDE.md pointers) |
| 7 | Owner and Maintainer terminology verified |

---

## 1. Problem

During B-021B execution, the Claude Code session accumulated context from multiple proposal revisions, full file read-backs pasted in chat, inline execution reports, and long command output. The session reached the 1M token boundary mid-execution.

At that point, `/compact` failed with:

```
API Error: Usage credits required for 1M context · turn on usage credits at
claude.ai/settings/usage, or use --model to switch to standard context
```

The session could not be compacted. Work was interrupted mid-state. This is an execution risk: if a session overflows during active file writes or an open audit trail, termination leaves the system in a partially committed state.

---

## 2. Why Late `/compact` Is Unsafe

`/compact` summarizes the conversation via the Claude API. The summarization step requires a model that supports the current context size.

| Context size | `/compact` behavior |
|---|---|
| Under ~800K tokens | Works on standard context model — free |
| ~800K–1M tokens | May work, increasingly unreliable |
| At or above 1M tokens | Requires 1M-context model — usage credits required |

Late compaction also risks losing execution state: mid-execution detail (file paths, pending audit rows, open verification steps) may not survive aggressive summarization.

**Conclusion:** 1M tokens is a failure condition, not an operating condition. Context hygiene must be proactive.

---

## 3. Tool Roles — Corrected

Three tools serve distinct purposes and must not be conflated:

| Tool | Purpose | When to use |
|---|---|---|
| `/compact` | Proactive mid-session context reduction | When context grows during ongoing work within the same session — before it becomes a problem |
| `/close-session` | Governance closure | When a task is complete, audit trail is written, and the session is genuinely done |
| New Claude Code session | Clean start for the next task | Default after `/close-session` — every new B-item gets a fresh session |

**The default end-of-item flow:**
`/close-session` → start new Claude Code session with minimal handoff context.

`/compact` is not the default end-of-item action. It is used when continuing within the same session before context gets too large — for example, between a proposal revision and its execution within one session.

---

## 4. Operational Thresholds

### 4.1 Context size thresholds

| Threshold | Action |
|---|---|
| ~600K tokens | Run `/compact` if continuing in the same session. Safe to defer briefly if a natural pause is imminent. |
| ~700K tokens | Run `/compact` before starting any new work. Do not begin a new task block without compacting first. |
| ~800K tokens | Stop starting new work. Either `/close-session` and start a new session, or compact immediately and assess whether to continue. |
| 1M tokens | Failure condition. `/compact` at this point requires usage credits. Do not allow sessions to reach this boundary. |

### 4.2 Session size limits

| Condition | Rule |
|---|---|
| One large B-item (multi-step execution, large files) | One per Claude Code session |
| Two small B-items (single-step, small deliverables) | Maximum per session, only if context remains clearly under 600K after the first item |
| Context indicator at or above 600K after first item | Do not start a second item regardless of item size — close and hand off |

### 4.3 End-of-item default flow

```
Task complete → audit trail written → /close-session → new Claude Code session
```

Brief the new session with: task ID, approved proposal reference, current execution state (what is done, what is pending).

---

## 5. Output Minimization Rules

### 5.1 What goes to file (mandatory)

- All proposals (all versions)
- All execution reports and closure reports
- All backlog registrations
- Long command output (>30 lines) required for audit evidence
- Full file read-backs referenced for verification
- Code blocks longer than 20 lines

### 5.2 What goes in chat (only)

Chat output must contain exactly these six items:

1. Deliverable path
2. Status (DONE / BLOCKED / FAILED / PARTIAL)
3. Short summary (3–5 lines maximum)
4. Deviations
5. Blockers
6. Recommended next step

No full proposals, no full execution reports, no full file read-backs, no long code blocks, no long command output in chat — unless Owner explicitly requests it in that turn.

### 5.3 Long command output for audit evidence

If long command output (logrotate dry-run, rsync output, grep results) is required as evidence, write it into the deliverable file under a dedicated section. Reference the section in chat. Do not paste the output in chat.

### 5.4 Verification read-backs

When verifying a file after a write, quote only the relevant lines (≤10 lines) as evidence. Do not read back the full file in chat.

### 5.5 Owner-requested exceptions

If Owner explicitly requests full content in chat in a given turn, paste it once and run `/compact` immediately afterward.

---

## 6. `/clear` Guidance

`/clear` is not part of normal audit execution.

`/clear` may only be used when all of the following are true:

- No active task is in progress
- No approved execution is pending
- No file writes are pending
- No audit trail obligation is open
- The session is purely exploratory (research, brainstorming, no deliverables)

If any of the above conditions is not met: do not use `/clear`.

If in doubt: do not use `/clear`.

---

## 7. Recommended Storage Location

**Option C — new SOP + one-line pointers in GL-005 and CLAUDE.md.**

Rationale:
- The protocol is procedural (when, what, what not) — SOP format is correct.
- GL-005 governs engineering behavior; a pointer there makes the rule visible to all technical agents.
- CLAUDE.md governs Larry's live operational rules; a pointer there makes the session boundary rules active.
- Neither GL-005 nor CLAUDE.md should contain the full protocol — they reference the SOP.

---

## 8. Proposed Implementation

### 8.1 SOP file

**Filename:** `SOP-014_Claude Code session context hygiene.md`

**Path:** `Team Knowledge/Core/SOPs/SOP-014_Claude Code session context hygiene.md`

**Full content:**

```markdown
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
```

---

### 8.2 SOP-index update

Add one row to the SOP-index table in `Team Knowledge/Core/SOPs/SOP-index.md`:

```
| Claude Code Session Context Hygiene | `Team Knowledge/Core/SOPs/SOP-014_Claude Code session context hygiene.md` | Proactive context hygiene rules for Claude Code sessions — thresholds, tool roles, output minimization, session boundaries |
```

---

### 8.3 GL-005 pointer

**File:** `Team Knowledge/Core/Guidelines/GL-005_AI Engineering Operating System.md`

**Insertion location:** After line 129 (after the `**Never:**` line in `## Development rules`), before the `---` separator at line 131.

**Exact text to add:**

```
**Context hygiene:** See SOP-014 Claude Code session context hygiene. Compact proactively — never reach 1M tokens. Deliverables to file; chat returns path, status, summary, deviations, blockers, next step only.
```

**Changelog entry to add to GL-005:**

```
- 2026-06-03 (Larry, B-031B): Context hygiene pointer added to Development rules. References SOP-014. Approved by Owner Walter Kamer.
```

---

### 8.4 CLAUDE.md pointer

**File:** `CLAUDE.md`

**Insertion location:** In `## Operational Conventions (Always Active)`, as a new subsection after the existing `### Scripts & Engineering` subsection and before `### Google, Sheets & Email`.

**Exact text to add:**

```markdown
### Session Context Hygiene

See `[[SOP-014_Claude Code session context hygiene]]`. Default end-of-item flow: `/close-session` → new Claude Code session. Run `/compact` at ~600K tokens when continuing in the same session; mandatory at ~700K; stop new work at ~800K. One large B-item per session. Chat output: path, status, summary, deviations, blockers, next step only — no full deliverables in chat.
```

---

## 9. Phasing

### Option A — Two phases (recommended)

**B-031A:** Create SOP-014 and update SOP-index.
- Files modified: `SOP-014_Claude Code session context hygiene.md` (new), `SOP-index.md` (one row added)
- Rollback: delete SOP-014, remove row from SOP-index

**B-031B:** Add pointers to GL-005 and CLAUDE.md.
- Files modified: `GL-005_AI Engineering Operating System.md` (one pointer line + changelog), `CLAUDE.md` (one subsection added)
- Depends on: B-031A complete
- Rollback: remove the added line from GL-005 and the added subsection from CLAUDE.md

**Rationale for two phases:** SOP-014 must exist before GL-005 and CLAUDE.md can reference it meaningfully. Two-phase execution also limits blast radius — if B-031B is rejected, the SOP still exists and is reachable via SOP-index.

### Option B — Single execution pass

Create SOP-014, update SOP-index, add GL-005 pointer, add CLAUDE.md subsection in one pass.
- Acceptable if Owner confirms all four files in a single approval.
- Higher blast radius but fewer context switches.

---

## 10. Post-Checks

After B-031A:

| Check | Method |
|---|---|
| `SOP-014_Claude Code session context hygiene.md` exists | `ls Team Knowledge/Core/SOPs/SOP-014*` |
| SOP-index contains SOP-014 row | Read SOP-index, confirm row present |
| SOP-014 is readable and complete | Read file, confirm all sections present |

After B-031B:

| Check | Method |
|---|---|
| GL-005 contains context hygiene pointer after `**Never:**` line | Read GL-005 lines 127–135, confirm pointer present |
| GL-005 changelog contains B-031B entry | Read GL-005 changelog section |
| CLAUDE.md contains `### Session Context Hygiene` subsection | Read CLAUDE.md, confirm subsection present |
| No other GL-005 or CLAUDE.md content was modified | Read both files in full; confirm only intended additions are present |

---

## 11. Rollback Methods

**B-031A rollback:**

```bash
rm "Team Knowledge/Core/SOPs/SOP-014_Claude Code session context hygiene.md"
# Remove the SOP-014 row from SOP-index.md using Edit tool
```

**B-031B rollback:**

```
# Remove the context hygiene pointer line from GL-005 Development rules section using Edit tool
# Remove the ### Session Context Hygiene subsection from CLAUDE.md using Edit tool
```

No database changes are made in either phase. No rollback needed for databases.

---

## 12. Risks and Owner Decisions Required

| # | Risk | Owner decision required |
|---|---|---|
| 1 | CLAUDE.md subsection placement — inserted after Scripts & Engineering, before Google/Sheets. Owner may prefer a different location. | Confirm placement or specify alternative |
| 2 | GL-005 pointer line is a new paragraph after `**Never:**` — may affect section flow if Owner prefers it elsewhere in the section | Confirm placement or specify alternative |
| 3 | Two-phase vs single-pass: two phases are recommended but add session overhead | Confirm Option A (two phases) or Option B (single pass) |
| 4 | Output minimization rule may conflict with Owner workflow — Owner sometimes wants full content pasted for review | Confirm: is the "paste once on explicit request, then compact" exception sufficient? |

---

## 13. Approval Gate

Owner Walter Kamer must explicitly approve before any file is modified.

**Approve B-031A only:**
Larry creates `SOP-014_Claude Code session context hygiene.md` and updates `SOP-index.md`. No GL-005 or CLAUDE.md changes.

**Approve B-031A + B-031B (Option A — recommended):**
Larry executes B-031A first, confirms, then executes B-031B (GL-005 pointer + CLAUDE.md subsection).

**Approve single-pass (Option B):**
Larry executes all four file changes in one pass.

**Reject:**
Proposal archived. No files modified.

No partial execution. No file is modified until the Owner has confirmed which option applies.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-031-session-context-hygiene-protocol-proposal-v02.md`*
