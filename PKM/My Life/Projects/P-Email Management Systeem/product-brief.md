# Product Brief — Email Management System (Inbox Zero)

**Version:** 0.2 (post-first-build UX feedback)
**Last updated:** 2026-06-25
**Owner:** Walter Kamer
**Strategist:** Phoebe

---

## Purpose

Build a personal email triage dashboard that surfaces Gmail inbox emails in an inbox-style list, allows quick review per email, and (future) captures triage decisions per message. The system eliminates manual inbox scanning and replaces it with a structured, decision-first interface.

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

### Feature 2 — Accordion detail panel

Clicking an email row expands an inline accordion panel directly below that row.

**Behavior:**
- Clicking a collapsed row expands it; clicking again collapses it
- Only one accordion open at a time (opening a second closes the first)
- Expanded panel content: empty placeholder for now — triage fields to be defined in next iteration
- The accordion expand/collapse animation must be functional; content is intentionally blank in MVP

**Acceptance criteria:**

| # | Criterion |
|---|-----------|
| AC-6 | Clicking a collapsed email row expands an accordion panel below it |
| AC-7 | Clicking an expanded email row collapses the panel |
| AC-8 | Opening a second accordion closes the previously open one |
| AC-9 | The expanded panel is visually distinct from the list row (e.g. indented or bordered) |
| AC-10 | The panel content area is empty in MVP — no triage fields yet |
| AC-11 | Accordion expand/collapse works without page reload |

---

## Out of scope for MVP

- Triage actions (archive, label, reply, snooze)
- Triage detail fields inside the accordion panel
- Multi-select or bulk actions
- Search or filter
- Mobile / responsive layout
- Read/unread state visualization

---

## Open questions

None — scope is clear for current build iteration.

---

## Revision log

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-25 | Initial scope — project created |
| 0.2 | 2026-06-25 | UX feedback integrated: inbox two-line format + accordion mechanic; AC-1 through AC-11 added |
