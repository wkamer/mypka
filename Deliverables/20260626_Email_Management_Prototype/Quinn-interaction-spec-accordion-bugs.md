# Interaction Spec — Email Management Accordion Bugs (Post-G6)

**Author:** Quinn — Senior UX-UI Designer
**Date:** 2026-06-28
**Scope:** Two persistent bugs reported after Devon's G6 fix implementation (72 tests green).
**Input sources:** `email-management-v1.html` (full code review), `Quinn-interaction-spec-slice3-fixes.md` (prior spec), `pitch-v1.md` (G2 source of truth).

---

## Context

Devon's G6 implementation uses vanilla DOM manipulation in a single HTML file. There is no framework, no virtual DOM, no component lifecycle. State lives entirely in the DOM. The accordion open/close is purely CSS-based — `toggleAccordion` (L155–162) adds and removes the `hidden` class on `.email-panel`. No DOM nodes are destroyed or recreated on accordion toggle. This is the key structural fact that determines where the bugs actually come from.

---

## Bug 1 — Log entries lost on accordion collapse

### Root cause (grounded in v1.html)

The log entries do NOT disappear from a pure accordion collapse/reopen cycle. `toggleAccordion` only manipulates a CSS class — the DOM, including all `<li>` log entries appended by `approveAction` (L254), is fully preserved through CSS hide/show.

The actual trigger is `renderPending()` (L438–444):

```
pendingList.innerHTML = "";
pendingSeed.map(cloneEmail).forEach((email) => {
  pendingList.appendChild(createEmailItem(email, false));
});
```

This destroys every DOM node in the pending list and rebuilds from the static `pendingSeed` array. Every new email item is created with an empty `.execution-log-list`. This function runs in two places: page load (L467) and inside the "Run Triage" click handler (L458).

When the owner clicks "Run Triage" after having approved actions, the list rebuilds from scratch. All log entries are gone. Reopening the accordion then shows an empty log section. From the owner's perspective this looks like "accordion collapsed → reopened → log gone" because Run Triage rebuilds the entire list and the accordion is no longer in its open state.

All session state — log entries, approved action states, user-typed names — is stored only in the DOM. `renderPending()` destroys that state without warning.

### Correct behavior

**Session state must survive `renderPending()`.**

A session state store lives in JavaScript memory, outside the DOM. It is a plain object keyed by email ID:

```
sessionState = {
  "jan-de-vries": {
    logEntries: [
      { text: "Task \"Factuur betalen voor 15 juli\" aangemaakt", timestamp: "28 jun 14:03" },
      ...
    ]
  },
  ...
}
```

**When `approveAction` fires:**
1. Append the new log entry `<li>` to `.execution-log-list` in the DOM (as now).
2. Also push the entry data to `sessionState[emailId].logEntries`. The entry data is an object containing the full text string and the timestamp label.
3. Remove `hidden` from `.execution-log` (as now).

**When `declineAction` fires:**
No log entry is added (per spec). No change to `sessionState[emailId].logEntries`.

**When `renderPending()` rebuilds the pending list:**
After each new email item is created and inserted into the DOM, check `sessionState[emailId]`:
- If `sessionState[emailId]` does not exist or `logEntries.length === 0`: leave `.execution-log` hidden (empty state rule — log section is not shown before any approval). This is unchanged behavior.
- If `sessionState[emailId].logEntries.length > 0`: restore each entry as an `<li>` element into `.execution-log-list`, in the order they appear in the array (newest at top per spec Issue 2 from prior spec). Remove `hidden` from `.execution-log`.

**Log section states:**

| State | Trigger | Display |
|---|---|---|
| Empty | No approvals yet, or `sessionState[emailId].logEntries` is empty | Section not rendered. No placeholder. |
| Populated | `logEntries.length > 0` | Section visible, entries in reverse chronological order (newest at top). |

No new states are introduced. No loading indicator is needed for this in-memory restore — it is synchronous.

**Run Triage behavior after this fix:**
The owner can click "Run Triage" at any time. The pending email list rebuilds (simulating a fresh triage pass). Log entries from the current session are restored immediately when each email item is recreated. The owner sees no state loss.

**Log entry format (unchanged from prior spec Issue 2):**
- Timestamp first: `DD Mon YYYY HH:MM`
- Task approved: `Task "[name]" aangemaakt`
- Event approved: `Event "[name]" — [formatted datetime] toegevoegd aan agenda`

### Accessibility

The log section is a `<ul>` with `<li>` entries. Restoring entries from session state produces the same DOM structure as when entries were first appended — no accessibility difference. No ARIA attribute changes are needed. Screen readers will announce the list and item count normally.

---

## Bug 2 — Task title gone after accordion collapse

### Root cause (grounded in v1.html)

**Primary cause (same as Bug 1):** `renderPending()` destroys all action row state. Approved rows, declined rows, and user-typed name edits are all wiped when the pending list rebuilds from `pendingSeed`. The rebuilt action rows use the original seed names and show Approve/Decline buttons — as if no action had been taken.

**Secondary cause (spec non-compliance — Issue 4 from prior spec not fully implemented):** `approveAction` (L229–258) does not replace the action row with a static name display. It takes the following approach instead:

1. Replaces `.action-controls` innerHTML with the Approved badge.
2. Disables the `<input type="text">` in-place and adds `text-slate-400`.

The disabled input in `text-slate-400` (a medium gray) on a dark background (`bg-slate-800/70` row) can visually appear missing or unreadably faint. The owner may perceive the name as "gone" even without `renderPending()` having run. This is an independent visual problem distinct from Bug 1.

The prior spec (Issue 4 — "Resolved state displays the submitted name") required that the approved state replace the editable input with static text. Devon's implementation does not do this.

### Correct behavior

Both causes require their own fix.

**Fix A — Session state persistence for action row states**

Extend `sessionState[emailId]` to also track action states:

```
sessionState = {
  "jan-de-vries": {
    logEntries: [...],
    actionStates: [
      { index: 0, type: "Task", name: "Factuur betalen voor 15 juli", status: "approved" },
      { index: 1, type: "Task", name: "Bevestiging sturen aan Jan de Vries", status: "declined" }
    ]
  }
}
```

The `index` is the position of the action row in the `.action-list`, matching the order in `email.actions` from the seed data.

**When `approveAction` fires:**
Push to `sessionState[emailId].actionStates`:
```
{ index: rowIndex, type: row.dataset.type, name: capturedName, datetime: capturedDatetime, status: "approved" }
```

`capturedName` is the value of `input.value.trim()` at the moment Approve was clicked (same value used for the log entry). `capturedDatetime` is the datetime field value (empty string for Task rows).

**When `declineAction` fires:**
Push to `sessionState[emailId].actionStates`:
```
{ index: rowIndex, type: row.dataset.type, status: "declined" }
```

**When `renderPending()` rebuilds and `createEmailItem` creates action rows:**
After seeding the initial AI-suggested rows, apply any persisted states from `sessionState[emailId].actionStates`:
- For each entry where `status === "approved"`: apply the approved display to that row (see Fix B below).
- For each entry where `status === "declined"`: apply the declined display to that row (disable input, replace controls with Declined label — as `declineAction` currently does).

**Manually added rows (added via +Task / +Event) and session state:**
Manually added rows have no corresponding index in the seed data. They must also be persisted. Extend `sessionState[emailId]` with a `manualRows` array:

```
manualRows: [
  { type: "Task", name: "Handmatige taak naam", status: "approved", datetime: "" },
  ...
]
```

When `renderPending()` rebuilds, re-add manual rows in order and apply their persisted states. Manual rows that are still in pending state (Approve/Decline not yet clicked) are restored with the name the owner typed at the time they last edited the field. This requires that manual row name input changes are written to `sessionState` on each `input` event (keyup / input event listener on the name field).

---

**Fix B — Resolved row displays name as static text (per prior spec Issue 4)**

The approved state must show the submitted name as readable, static text — not a disabled input. The disabled input pattern is replaced.

**Approved Task row layout:**

```
[Task label]  [name as static text]  [✓ Approved badge]
```

The name text element:
- Element: `<span>`
- Content: the submitted name (captured at Approve time)
- Style: same text size as the input it replaces (`text-sm`), color `text-slate-300`
- The `text-slate-300` value ensures the name is clearly readable against the row background (`bg-slate-800/70`). It is lighter than the current `text-slate-400` used on the disabled input, which is the minimum readable contrast in this dark context.

**Approved Event row layout:**

```
Event
[name as static text — text-sm text-slate-300]
[datetime as static text — text-sm text-slate-400]
[✓ Approved badge]
```

The datetime text element:
- Element: `<span>`
- Content: the submitted datetime formatted as `DD Mon YYYY HH:MM` (use `formatDatetime()`, already present in v1.html)
- Style: `text-sm text-slate-400`
- If no datetime was submitted: show `(geen datum)` in `text-slate-500`

**Declined row layout (Task and Event):**

The declined state is unchanged from current implementation. The disabled/muted input style is acceptable for declined rows because the owner explicitly chose not to act on them — the muted appearance is appropriate.

**Empty name fallback (approved rows):**
If `capturedName` is empty string after trim: display `(naamloze taak)` or `(naamloos event)` in `text-slate-500` italic. This matches the existing fallback logic in `approveAction` but surfaces it visually rather than hiding it in a disabled input.

| Row type | Name state | Displayed text | Color |
|---|---|---|---|
| Task approved | name provided | submitted name | `text-slate-300` |
| Task approved | name empty | `(naamloze taak)` | `text-slate-500`, italic |
| Event approved | name provided | submitted name | `text-slate-300` |
| Event approved | name empty | `(naamloos event)` | `text-slate-500`, italic |
| Event approved | datetime provided | formatted datetime | `text-slate-400` |
| Event approved | datetime empty | `(geen datum)` | `text-slate-500`, italic |

### Accessibility

The prior spec (Issue 4 accessibility note) applies here: replacing the disabled input with a static `<span>` is the correct accessible pattern. Disabled form controls are announced by screen readers as "unavailable" or "dimmed" — creating noise when the owner navigates resolved rows. Static text elements are announced as plain content with no interactive annotation.

No ARIA role changes are needed. The row remains a non-interactive container after approval.

When `renderPending()` restores approved rows from `sessionState`, the resulting DOM is identical to what `approveAction` would have produced — the screen reader experience is consistent.

---

## What Devon does not need to ask about

- Whether `sessionState` should use a `Map` or a plain object: either is correct. The key is that it is a module-level variable outside any render function.
- Whether to debounce the name-field input listener: a simple `input` event listener on each keyup is sufficient. No debounce needed for a prototype.
- Whether the Processed section needs the same session state treatment: No. Once an email moves to Processed, it is created via `createEmailItem(email, true, allEntries)` with the log entries passed directly. The processed section does not rebuild from seed.
- Whether `renderProcessedInitial()` is affected: No. It runs once at page load and is not triggered by Run Triage.
- Color tokens: `text-slate-300` for approved name, `text-slate-400` for approved datetime, `text-slate-500` for empty fallbacks. All are already in use in v1.html — no new tokens required.
- Whether manual rows that are still pending (not yet approved or declined) need to be persisted across Run Triage: Yes, they must be. The name the owner typed must survive. See the `manualRows` array in Fix A above.

---

## Nielsen's 10 Heuristics — Self-Review

| # | Heuristic | Assessment |
|---|---|---|
| 1 | Visibility of system status | Pass. Log entries persist after Run Triage — the owner always sees what they approved. The approved name is now clearly readable (slate-300 not slate-400). |
| 2 | Match between system and real world | Pass. Language unchanged. The resolved row shows the actual name the owner typed, matching their mental model of "I created task X." |
| 3 | User control and freedom | Pass. No new restrictions. Run Triage is now safe to use freely without losing work. |
| 4 | Consistency and standards | Pass. Static text in resolved rows is the standard for read-only display in form UIs. Disabled inputs in resolved states are non-standard and removed by this fix. |
| 5 | Error prevention | Pass. Session state store prevents accidental loss of work when the owner clicks Run Triage. No warning dialog needed — state is silently preserved. |
| 6 | Recognition rather than recall | Pass. The owner does not need to remember what they approved — the log and the resolved row display the submitted names. This is the core UX principle at stake in both bugs. |
| 7 | Flexibility and efficiency | Pass. The owner can click Run Triage freely. No workflow workaround is required. |
| 8 | Aesthetic and minimalist design | Pass. The resolved row with static text is cleaner than a disabled input. One fewer interactive affordance in a non-interactive state. |
| 9 | Help users recognize, diagnose, and recover from errors | Pass. No errors are introduced. The previous state loss gave users no way to recover — this fix prevents the loss entirely. |
| 10 | Help and documentation | Pass. No new help text needed. The UI behavior is self-evident. |

All 10 heuristics pass. No open items.

---

## Scope boundary

This spec covers exactly the two reported bugs:
1. Log entries lost on accordion collapse (trigger: `renderPending()`).
2. Task title gone after accordion collapse (trigger: `renderPending()` + disabled input non-compliance from prior Issue 4).

No other issues are in scope. The fix for both bugs shares the same session state store mechanism — Devon should implement them together, not as separate passes.
