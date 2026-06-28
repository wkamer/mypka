# Interaction Spec — Email Management Slice 3 Fixes

**Author:** Quinn  
**Date:** 2026-06-28  
**Status:** Ready for Devon  
**Trigger:** G6 rejection — four issues raised by owner  
**References:** pitch-v1.md, G4-slice3-brief.md, EmailTriage.jsx

---

## Purpose

This spec corrects four interaction design failures identified at G6 review. All four are component state and interaction design problems that were not covered in the original interaction spec. Devon should read this spec before writing a single line of code to fix the rejected slice.

The user outcome this spec serves: the owner can open and reopen an email's accordion at any point during a triage session and always see an accurate, persistent record of what was approved, when it was approved, and what the approved items were named.

---

## Issue 1 — Execution log is persistent across accordion open/close

### Root cause (observed, not specced)

The current `ActionsPanel` component mounts when the accordion opens and unmounts when it closes. The execution log lives in local component state (`useState`). When the accordion closes, the component unmounts and the log state is destroyed. When the accordion reopens, the component remounts with an empty log, even if approvals occurred in a prior open session.

### Correct behavior

**When the accordion opens:**

1. The panel enters a loading state. The loading indicator appears in the log section's position (not in the actions section). Loading text: "Loading log..."
2. The frontend fetches all previously approved log entries for this email from the backend. This is a separate concern from fetching actions — actions describe what the owner can do, log entries describe what the owner has done.
3. When the fetch resolves successfully, the log section renders with all persisted entries. If the fetch resolves with zero entries, the log section is not rendered (matching the existing rule: log is not shown before any approval has occurred).
4. When the fetch fails, the actions panel is still usable. The log section shows a single line in muted error styling: "Execution log unavailable." No retry button — the owner can continue working; log entries from this session will still append in-memory.

**When the owner approves an action in the current session:**

5. The new log entry is appended immediately to the in-panel display (no round-trip required). The entry also persists to the backend so it is available on next accordion open. If the backend persist call fails, the entry remains visible in the current session (in-memory) but a silent error is logged to the browser console. The owner is not interrupted.

**Log section — empty state:**

The log section is not rendered at all when there are no entries. No "No log entries yet" placeholder. This matches the G2 pitch: log appears only after the first approval.

**Log section — loaded state:**

Entries render in reverse chronological order (newest at top). See Issue 2 for exact entry format.

**Log section — error state:**

Single muted line: "Execution log unavailable." The actions panel and all approve/decline/add controls remain fully functional.

### Accessibility

The log section is a live region (`aria-live="polite"`, `aria-label="Execution log"`). When a new entry is prepended in the current session, screen readers announce the new entry without interrupting the owner's current action.

---

## Issue 2 — Log entries: date/time first, newest on top

### Entry format — task approved

```
[DD Mon YYYY HH:MM]  Task [name] created
```

Example: `28 Jun 2026 14:03  Task Stuur datum door aan Remko created`

### Entry format — event approved

```
[DD Mon YYYY HH:MM]  Event [name] — [datetime] added to calendar
```

Example: `28 Jun 2026 14:07  Event Broederweekend inplannen — 12 Jul 2026 10:00 added to calendar`

### Rules

- The date/time component is always the first element in the entry. It is never at the end.
- Date/time format for the log timestamp: `DD Mon YYYY HH:MM` (e.g., "28 Jun 2026 14:03"). Two-digit day, three-letter month abbreviation, four-digit year, 24-hour time. This is a read-only display value — not a datetime-local input.
- The `[name]` token is the value present in the name field at the moment Approve was clicked. If the owner edited the AI suggestion, the edited value appears. If the owner left the field unchanged, the AI suggestion appears. See Issue 4 for manually added rows.
- The `[datetime]` token for event entries is the value present in the datetime field at the moment Approve was clicked.
- Entries are ordered newest at top. When a new entry is appended in the current session, it is prepended to the list, pushing older entries down.
- When entries are loaded from the backend on accordion open, they arrive pre-sorted newest-first. The frontend does not re-sort.

### Ordering behavior — edge cases

**When a new entry is added during the current session:** it prepends to the rendered list immediately. It does not animate in. It becomes the first visible entry.

**When the log contains a mix of entries loaded from backend and entries added in the current session:** the in-session entry is already the newest, so prepending it is correct. The two populations do not need to be merged or re-sorted.

**When the accordion is reopened after new approvals were added in a prior session:** the backend returns all entries sorted newest-first. The frontend renders them in that order without modification.

### Accessibility

Each entry row has no interactive elements. The log section heading "Execution log" is a visible label and also the `aria-label` on the live region container. Individual entries are plain text — no special ARIA roles required.

---

## Issue 3 — Manually added rows cannot be canceled

### Behavior

When the owner clicks +Task or +Event, a new action row is created immediately. There is no way to remove that row except by resolving it (Approve or Decline).

**There is no cancel button.** The row does not have an X, a dismiss icon, or any control whose purpose is to remove the row without resolving it.

**There is no dismiss gesture.** Clicking outside the row, pressing Escape, or navigating away within the panel does not remove the row.

**Keyboard Escape does not remove the row.** If the owner presses Escape while focus is inside a manually added row's name field, the default browser behavior (clear field value) may apply to the text input, but the row itself remains. The row is not closed or removed by any keyboard shortcut.

### Why the row is permanent until resolved

The row is committed to the backend immediately when +Task or +Event is clicked, before the owner has typed anything. It exists as a real backend record with status "pending". Removing it from the UI without resolving it would create an orphaned backend record, or require a DELETE call that the spec does not support. The owner always has Decline as a fast resolution that takes one click.

Decline on a manually added row is not a cancel — it is a resolution decision. The row moves to a declined muted state and remains visible in the actions panel. The distinction matters: the owner can see that they considered and declined the item, rather than seeing it silently disappear.

### What happens when the owner opens a different accordion row

1. The current accordion closes.
2. The `ActionsPanel` component unmounts.
3. The manually added pending row is already persisted in the backend (from the POST that fired on +Task/+Event click).
4. When the owner later reopens the original email's accordion, the panel remounts, fetches actions, and the pending row reappears with its status "pending" and its current name field value (see note below).

**Name field value on reload:** the backend stores the name that was submitted at the time of the last edit. If the owner typed a partial name before switching accordions, that partial name is what the backend holds (assuming Devon's PATCH sends the current name value on each keystroke — if not, the name field on reload shows whatever was last persisted). Devon must ensure that the backend stores the most recent name value so the reload is lossless.

**If the owner has NOT typed any name before switching accordions:** the name field is empty on reload. The owner can continue typing when they return.

### Unsaved name field — edge case table

| Owner action | Name field state on next open |
|---|---|
| Typed a name, then opened different accordion | Name the owner typed (if persisted on each keystroke or on field blur) |
| Typed a name, then closed browser tab | Name the owner typed (if persisted) |
| Opened +Task but typed nothing, then opened different accordion | Empty name field |
| Typed a name, then approved the row | Row shows in Approved state with name — see Issue 4 |

### Accessibility

The +Task and +Event buttons are standard button elements, keyboard-reachable via Tab. After the owner activates either button, focus moves to the name field of the newly added row. This is the correct behavior — the owner can immediately type without additional navigation.

When focus is in the name field of a manually added row, pressing Escape does not remove the row or move focus away. The default input field behavior for Escape (browser-specific, may clear the field) is acceptable; row dismissal is not.

---

## Issue 4 — Resolved state displays the submitted name

### Problem

After approving a manually added task, the resolved row shows blank where the name should appear. The root cause: manually added rows are created with `name: null` in the backend. The edit state is initialized to empty string. The resolved display reads from the action object's name property, which remains null, and the empty string initialization wins — resulting in a blank display.

### Correct behavior — resolved row layout

A resolved row (status: "approved" or "declined") shows two things:

1. The action type label ("Task" or "Event") — same as the pending row.
2. The name as static text — not an editable input, not a disabled input. The name is rendered as plain text with the same styling as a label. It is always visible and never blank (see fallback below).

A resolved row does NOT show:
- An editable text input (the input is replaced by static text in the resolved state)
- An editable datetime input for Event rows (replaced by static text showing the datetime value)
- Approve/Decline buttons

### What name is displayed in the resolved state

**AI-suggested row (approved):** the name the owner submitted at the moment of approval. If the owner edited the AI suggestion before clicking Approve, the edited value is shown. If the owner left it unchanged, the AI suggestion is shown.

**AI-suggested row (declined):** the name that was in the field at the moment of decline. The owner may have edited the name before deciding to decline. Show that value.

**Manually added row (approved):** the name the owner typed and submitted at the moment of approval. This is NOT the AI suggestion (there is none). It is NOT the initial null/empty state. It is the value the owner entered.

**Manually added row (declined):** the name the owner typed before clicking Decline, or empty if they declined without entering a name.

### Empty name fallback

If the submitted name is empty (the owner approved or declined without typing anything), the resolved row shows a fallback label in muted styling: "(untitled)". This prevents the blank row that caused the G6 rejection. The log entry for an approved row with no name reads:

- Task: `28 Jun 2026 14:03  Task (untitled) created`
- Event: `28 Jun 2026 14:07  Event (untitled) — [datetime] added to calendar`

### Resolved state for Event rows

An approved or declined Event row shows:

- Action type: "Event"
- Name: static text (the submitted name or "(untitled)")
- Datetime: static text (the submitted datetime value, formatted as `DD Mon YYYY HH:MM`, or "(no date)" if no value was submitted)
- Status badge: "Approved" (green) or "Declined" (muted)

### Summary table: what the resolved state shows

| Row type | Resolved state content |
|---|---|
| AI-suggested task, approved | Type: "Task" — Name: submitted name — Badge: "Approved" |
| AI-suggested task, declined | Type: "Task" — Name: name at time of decline — Badge: "Declined" |
| AI-suggested event, approved | Type: "Event" — Name: submitted name — Datetime: submitted datetime — Badge: "Approved" |
| AI-suggested event, declined | Type: "Event" — Name: name at time of decline — Datetime: datetime at time of decline — Badge: "Declined" |
| Manually added task, approved | Type: "Task" — Name: owner-typed name or "(untitled)" — Badge: "Approved" |
| Manually added task, declined | Type: "Task" — Name: owner-typed name or "(untitled)" — Badge: "Declined" |
| Manually added event, approved | Type: "Event" — Name: owner-typed name or "(untitled)" — Datetime: owner-typed datetime or "(no date)" — Badge: "Approved" |
| Manually added event, declined | Type: "Event" — Name: owner-typed name or "(untitled)" — Datetime: owner-typed datetime or "(no date)" — Badge: "Declined" |

### Accessibility

The resolved row is not interactive. The type label, name text, datetime text (event rows), and status badge are plain text. No ARIA role changes required. The disabled input pattern used in the current implementation is replaced by static text — this is better for screen readers because disabled inputs are commonly announced as unavailable for interaction, which creates noise.

---

## Nielsen's 10 Heuristics Self-Review

This review was run against the spec above before delivery.

**H1 — Visibility of system status**  
Issue 1 fix adds a loading state for the log fetch and an error state when the fetch fails. The owner always knows whether the log is loading, loaded, or unavailable. The immediate in-panel log entry on approval (Issue 2 fix) confirms the action was registered. Pass.

**H2 — Match between system and real world**  
Log entry language ("Task [name] created", "Event [name] added to calendar") matches real-world outcome language. Timestamp-first format (Issue 2 fix) matches how people read historical records. Pass.

**H3 — User control and freedom**  
Issue 3 deliberately restricts the owner's ability to remove a manually added row without taking action. This is a tension point. The rationale is that Decline gives a one-click escape, the row is not a trap, and the restriction prevents orphaned backend records. The resolved declined state is not a punishment — it is a record of a deliberate choice. This tension is documented. The spec does not remove Decline as an escape path. Acceptable.

**H4 — Consistency and standards**  
All log entries follow the same `[timestamp]  [action description]` format. Resolved rows for task and event follow the same layout pattern. Newest-first ordering matches standard log and feed conventions (Gmail, Slack, terminal output). Pass.

**H5 — Error prevention**  
The empty name fallback "(untitled)" prevents blank resolved rows. The loading state on log fetch prevents the owner from acting on stale data. The immediate POST on +Task/+Event prevents row loss on accordion close. Pass.

**H6 — Recognition over recall**  
Timestamp first in log entries (Issue 2 fix): the owner reads context before content. Name visible in resolved state (Issue 4 fix): the owner recognizes what they approved without reconstructing it from memory. Pass.

**H7 — Flexibility and efficiency**  
No changes to the approve/decline flow. The +Task/+Event buttons with auto-focus on the new row's name field allow the owner to add and name a task in two steps (click button, type name). Pass.

**H8 — Aesthetic and minimalist design**  
Log section: timestamp + action description. No icons, no dividers between entries. Resolved row: type + name + datetime (event) + badge. No redundant elements. The error state for log fetch is a single line. Pass.

**H9 — Help users recognize, diagnose, and recover from errors**  
Log fetch failure (Issue 1 error state): "Execution log unavailable." — human-readable, non-technical. Does not block action. The actions panel remains fully functional. Approve failure: the current implementation logs to console only; this is out of scope for this spec (it is a pre-existing issue not raised at G6). Pass for the four issues in scope.

**H10 — Help and documentation**  
Not applicable at this interaction level. The interface is self-explanatory for a single-user tool operated by the owner daily. Pass.

**Result:** No heuristic failures in this spec. H3 has a deliberate tension that is documented with rationale. This spec is ready for Devon.

---

## What Devon does not need to ask about

- Log timestamp format: `DD Mon YYYY HH:MM` — 28 Jun 2026 14:03 — no seconds, no timezone suffix, 24-hour
- Log entry language: English throughout (matches G2 pitch changelog entry from 2026-06-27 14:00)
- Log ordering: newest first, always — no configuration, no toggle
- Cancel button on manually added rows: does not exist — this is intentional, not a missing feature
- Escape key on manually added rows: does not remove the row — browser default behavior on the text input is acceptable
- Empty name in resolved state: show "(untitled)" — not blank, not an error state
- Empty datetime in resolved event resolved state: show "(no date)" — not blank
- Resolved state input type: static text, not a disabled input element
- Log section visibility: not rendered when zero entries — no empty placeholder

---

*Quinn — 2026-06-28*
