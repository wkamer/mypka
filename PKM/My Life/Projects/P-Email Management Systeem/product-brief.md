# Product Brief — Email Management System (Inbox Zero)

**Version:** 0.3 (Feature Brief — accordion triage content + approval flow)
**Last updated:** 2026-06-26
**Owner:** Walter Kamer
**Strategist:** Phoebe

---

## Purpose

Build a personal email triage dashboard that surfaces Gmail inbox emails in an inbox-style list, allows quick review per email, and captures triage decisions per message. The system eliminates manual inbox scanning and replaces it with a structured, decision-first interface.

---

## Problem Statement (v0.3 iteration)

The owner processes his inbox daily. Every email has already been AI-triaged: it has a classification (Action or FYI), a summary, and zero or more suggested actions (Todoist task, Calendar event, Archive). The accordion is built but empty. There is no way to see that triage output or act on it. Approved actions never land in his system.

The gap: the owner opens an email, sees nothing, and has to go back to Gmail. The accordion content is missing.

---

## User Value (observable)

After this iteration, the owner can:

1. Open the dashboard, expand an email, and immediately read what the AI concluded without opening Gmail.
2. See the suggested actions and approve them with one click per action.
3. Watch approved actions appear in Todoist, Calendar, or Gmail archive — without switching apps.
4. Move through the full inbox in the dashboard, email by email, until processed.

Observable signal: the owner completes a full inbox session without leaving the dashboard.

---

## MVP Scope

### Feature 1 — Inbox-style email list

Display Gmail inbox emails in a two-line-per-row list format.

**Row structure (per email):**
- Line 1: From field (sender name or address)
- Line 2: Subject + date/time received (right-aligned or appended)

**Behavior:**
- List is scrollable
- Emails are ordered by received date descending (newest first)
- No threading — each email is a flat row
- No actions on the list row itself (no buttons, no swipe)

**Acceptance criteria:**

| # | Criterion |
|---|-----------|
| AC-1 | Each email renders as exactly two lines: line 1 = sender (From field), line 2 = subject |
| AC-2 | Date/time received is visible on line 2 (same row as subject) |
| AC-3 | List is sorted newest first by default |
| AC-4 | The list renders without horizontal scrolling on a standard desktop viewport |
| AC-5 | Sender name is used when available; raw address is fallback |

---

### Feature 2 — Accordion shell

Clicking an email row expands an inline accordion panel directly below that row.

**Behavior:**
- Clicking a collapsed row expands it; clicking again collapses it
- Only one accordion open at a time (opening a second closes the first)
- Accordion expand/collapse works without page reload

**Acceptance criteria:**

| # | Criterion |
|---|-----------|
| AC-6 | Clicking a collapsed email row expands an accordion panel below it |
| AC-7 | Clicking an expanded email row collapses the panel |
| AC-8 | Opening a second accordion closes the previously open one |
| AC-9 | The expanded panel is visually distinct from the list row (e.g. indented or bordered) |
| AC-10 | ~~The panel content area is empty in MVP~~ — superseded by Feature 3 |
| AC-11 | Accordion expand/collapse works without page reload |

---

### Feature 3 — Accordion triage content and approval flow

The accordion panel shows the AI triage output for the open email and lets the owner approve or decline each suggested action. Approved actions are written to the target system immediately.

**Panel structure (top to bottom):**
1. Classification badge — Action or FYI
2. AI summary — one or two sentences, read-only
3. Suggested actions — zero or more rows, each with Approve and Decline

**Action row structure:**
- Label describing the action (e.g. "Create Todoist task: Follow up with supplier" or "Archive email")
- Approve button
- Decline button

**Behavior:**
- Approving a Todoist action: calls the backend, creates the task in Todoist, marks the action row as approved
- Approving a Calendar action: calls the backend, creates the event in Google Calendar, marks the action row as approved
- Approving an Archive action: calls the backend, archives the email in Gmail, marks the action row as approved
- Declining any action: marks the action row as declined, no external write
- After the owner has approved or declined all actions on an email, the email row in the list is visually marked as processed (e.g. dimmed or with a checkmark)
- If an email has zero suggested actions, the panel shows classification and summary only — no action rows

**Acceptance criteria:**

| # | Criterion |
|---|-----------|
| AC-12 | The expanded accordion panel displays the AI-generated email summary as read-only text |
| AC-13 | The classification (Action or FYI) is displayed as a badge at the top of the accordion panel |
| AC-14 | Each suggested action appears as a labeled row with an Approve button and a Decline button |
| AC-15 | Approving a Todoist action creates the task in Todoist; the action row shows a confirmed state immediately |
| AC-16 | Approving a Calendar action creates the event in Google Calendar; the action row shows a confirmed state immediately |
| AC-17 | Approving an Archive action archives the email in Gmail; the action row shows a confirmed state immediately |
| AC-18 | Declining an action marks that action row as declined with no write to any external system |
| AC-19 | Once every action row is either approved or declined, the email row in the inbox list is visually marked as processed |
| AC-20 | If an email has zero suggested actions, the accordion panel shows only the classification and summary — no action rows |

---

## Scope Boundary — what is IN for this iteration

- Display AI classification and summary inside the accordion
- Display suggested actions (Todoist, Calendar, Archive) as approvable rows
- Approve flow: write to Todoist, Google Calendar, or Gmail Archive via existing backend
- Decline flow: mark as declined, no write
- Visual processed state on the email row after all actions are resolved

---

## Non-goals — explicitly OUT for this iteration

- Creating or editing actions manually (owner cannot add or change suggested actions)
- Editing the AI summary
- Replying to or forwarding emails
- Snoozing emails
- Labeling or starring
- Multi-select or bulk approve
- Search or filter
- Error retry UI (backend errors are out of scope for now)
- Mobile / responsive layout
- Read/unread state visualization
- Undo after approval

---

## Open questions

None. Scope is clear for this build iteration.

---

## Revision log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-25 | Initial scope — project created |
| 0.2 | 2026-06-25 | UX feedback integrated: inbox two-line format + accordion mechanic; AC-1 through AC-11 added |
| 0.3 | 2026-06-26 | Feature Brief for accordion triage content and approval flow; problem statement, user value, scope boundary, non-goals, AC-12 through AC-20 added |
