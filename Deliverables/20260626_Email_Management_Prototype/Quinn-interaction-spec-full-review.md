# Interaction Spec — Email Management Full Review

**Author:** Quinn
**Date:** 2026-06-28
**Status:** Ready for Devon / Codex
**References:** EmailTriage.jsx, Quinn-interaction-spec-slice3-fixes.md, pitch-v1.md

---

## Purpose

This spec covers two deliverables:

1. Frontend state reconstruction — how the UI must render persisted action states on accordion open, and how the execution log must be rebuilt from the GET /actions response.
2. Full UI/UX design review — every design quality issue that materially affects usability, with heuristic and WCAG reference for each.

Both parts are implementation-ready. No ambiguity should remain after reading this doc.

---

## Part 1 — Frontend State Reconstruction

### User outcome

The owner can close the browser, reopen the page, and open any email accordion. Every action renders in its persisted state. The execution log is present and accurate. No state is lost between sessions.

### What is broken today

The `ActionsPanel` component mounts on accordion open and unmounts on accordion close. The `emailSessions` state lives in the parent `EmailTriage` component and survives accordion close within a session — but it is cleared on page refresh. After refresh:

- `emailSession` is `undefined`
- `emailSession?.logEntries` is `undefined`
- The log section is rebuilt only from the `/api/email-management/emails/${emailId}/log` response

The deeper problem: the current code makes two separate fetches on accordion open (GET /actions and GET /log). GET /actions already returns `status`, `name`, `event_datetime`, and `approved_at` for every action. There is no need for a separate log endpoint. The log can and must be reconstructed entirely from the GET /actions response. This eliminates a parallel fetch, a race condition, and the dependency on a separate endpoint for data that already exists in the actions response.

### Correct behavior — accordion opens

**Step 1: Actions fetch**

The frontend calls `GET /api/email-management/emails/${emailId}/actions`.

The response contains an array of action objects. Each object includes:

```
{
  id: string,
  type: "Task" | "Event",
  name: string | null,
  event_datetime: string | null,   // ISO datetime string or null
  status: "pending" | "approved" | "declined",
  approved_at: string | null       // ISO datetime string; null for pending and declined rows
}
```

**Step 2: Render actions in their persisted state**

For each action in the response, the `ActionRowV3` component receives the `action` object with its `status` field. The component already checks `action.status !== "pending"` to determine `isResolved`. This logic is correct. The issue is that the merge logic can override the API status with stale session state.

Correct merge behavior when session state exists:

```js
const mergedActions = d.actions.map((a) => {
  const saved = savedById.get(a.id);
  if (!saved) return a;
  // API status is authoritative for resolved states. Session status only wins
  // when the action was resolved in the current session (status !== "pending" in session).
  const resolvedInSession = saved.status && saved.status !== "pending";
  return resolvedInSession ? { ...a, ...saved } : { ...saved, ...a };
});
```

Explanation: if the API returns `status: "approved"`, that is the ground truth. The session state should never downgrade a resolved status back to pending. The merge must preserve the API status for all resolved actions.

**Step 3: Reconstruct the execution log from approved actions**

After the actions fetch resolves, the frontend filters and sorts approved actions to build the log:

```js
const approvedActions = mergedActions
  .filter((a) => a.status === "approved" && a.approved_at)
  .sort((a, b) => new Date(b.approved_at) - new Date(a.approved_at)); // newest first

const backendLogEntries = approvedActions.map((a) =>
  buildLogEntry(a.type, a.name, a.event_datetime, a.approved_at)
);
```

Then merge with any in-session log entries that are not yet covered:

```js
const ssLog = emailSession?.logEntries || [];
const merged = [...ssLog];
backendLogEntries.forEach((e) => {
  if (!merged.includes(e)) merged.push(e);
});
setLogEntries(merged);
setLogStatus("loaded");
```

The `/api/email-management/emails/${emailId}/log` endpoint call is removed. It is replaced entirely by this reconstruction from GET /actions.

**Step 4: Edit state initialization**

The edits state is initialized from the API response when no session data exists. For resolved actions, the edit values are read-only display values, not inputs. The initialization must use the API `name` and `event_datetime`:

```js
initial[a.id] = {
  name: sessionEdit !== undefined ? sessionEdit.name : (a.name ?? ""),
  event_datetime: sessionEdit !== undefined
    ? sessionEdit.event_datetime
    : (a.event_datetime ?? ""),
};
```

No change from the current logic here — the current logic is correct for initialization. The bug is in the status merge, not the edit initialization.

### Log entry format

Matches the format specified in Quinn-interaction-spec-slice3-fixes.md Issue 2.

The `buildLogEntry` function already exists and produces the correct format. Pass the `approved_at` value from the API as the `ts` argument:

```js
buildLogEntry(a.type, a.name, a.event_datetime, a.approved_at)
// Task:  "28 Jun 2026 14:03  Task \"Stuur datum door aan Remko\" created"
// Event: "28 Jun 2026 14:07  Event \"Broederweekend inplannen\" — 12 Jul 2026 10:00 added to calendar"
```

### Log ordering

Newest first. The sort by `approved_at` descending handles backend entries. In-session entries are prepended as per existing behavior (correct). No re-sort is needed when merging.

### Loading state

While the GET /actions fetch is in flight, actions is `null`, and the existing loading indicator `"Loading actions..."` renders. There is no separate log loading state. The log section renders as part of the resolved actions render — it appears when the fetch completes, not on a separate timer.

### Error state

If GET /actions fails, the existing error path renders `"Failed to load actions: {message}"`. The log section does not render independently. No change needed.

### What Devon does not need to ask about

- The `/log` endpoint: remove it from the accordion open flow entirely.
- The `approved_at` field: assume the API returns it for all approved actions. If it is null on an approved action, skip that action from log reconstruction (do not render a log entry with `undefined` date).
- Merge priority: API status is authoritative. Session state wins only when the action was resolved within the current session.
- Log ordering: approved_at descending, no exceptions.
- Log format: use the existing `buildLogEntry` function unchanged.

---

## Part 2 — Full UI/UX Design Review

The Nielsen heuristic self-review is embedded at the end of this section. Every issue below is supported by a WCAG rule or heuristic reference. Issues without that support are not in this spec.

### Issue 1 — Received date text fails WCAG 1.4.3

**Where:** `InboxRow`, line containing `text-slate-600 text-xs shrink-0 whitespace-nowrap`

**Problem:** The received date uses `text-slate-600` (#475569) on `bg-slate-800` (#1e293b). Measured contrast ratio: approximately 1.9:1. Required minimum for normal text (text-xs = 12px, below the 18pt/14pt-bold large text threshold): 4.5:1.

**Standard:** WCAG 1.4.3 Contrast (Minimum), Level AA.

**Correct behavior:** Change to `text-slate-400` (#94a3b8) on `bg-slate-800`. Measured ratio: approximately 5.7:1. Passes AA.

**Token change:** `text-slate-600` → `text-slate-400` on the received date span.

---

### Issue 2 — Decline button text fails WCAG 1.4.3

**Where:** `ActionRowV3`, the Decline button, class `text-xs text-slate-500 hover:text-slate-400 transition-colors`

**Problem:** `text-slate-500` (#64748b) on `bg-slate-900` (#0f172a). Measured ratio: approximately 3.8:1. Required: 4.5:1 for normal text. Fails AA for text-xs (12px).

**Standard:** WCAG 1.4.3.

**Correct behavior:** Base state `text-slate-400` (#94a3b8) on `bg-slate-900`: approximately 7.1:1. Passes AA. Hover: `hover:text-slate-300`.

**Token change:** `text-slate-500 hover:text-slate-400` → `text-slate-400 hover:text-slate-300` on the Decline button.

---

### Issue 3 — Action type label fails WCAG 1.4.3

**Where:** `ActionRowV3`, the type label span, class `text-xs text-slate-500 uppercase mt-2 w-10 shrink-0 font-medium`

**Problem:** `text-slate-500` on `bg-slate-900`: approximately 3.8:1. text-xs uppercase text. Uppercase does not qualify as "large text" under WCAG — large text requires 18pt (24px) or 14pt bold (approximately 18.67px). text-xs at 12px fails both thresholds. Required: 4.5:1.

**Standard:** WCAG 1.4.3.

**Correct behavior:** `text-slate-400` on `bg-slate-900`: approximately 7.1:1.

**Token change:** `text-slate-500` → `text-slate-400` on the type label span in ActionRowV3.

---

### Issue 4 — Execution log section heading fails WCAG 1.4.3

**Where:** `ActionsPanel`, the "Execution log" paragraph, class `text-slate-500 text-xs font-medium mb-2`

**Problem:** `text-slate-500` on `bg-slate-900`: approximately 3.8:1. Fails AA for text-xs normal text. `font-medium` is not bold — bold for WCAG large text exemption requires `font-bold` (700 weight) and even then only at 14pt (approximately 18.67px), not 12px.

**Standard:** WCAG 1.4.3.

**Correct behavior:** `text-slate-400` on `bg-slate-900`: approximately 7.1:1.

**Token change:** `text-slate-500` → `text-slate-400` on the "Execution log" heading.

---

### Issue 5 — InboxRow is not keyboard operable

**Where:** `InboxRow`, the outer `<div>` with `onClick={() => onToggle(email.id)}`

**Problem:** This div acts as an interactive accordion toggle but is not reachable or operable via keyboard. It has no `role`, no `tabIndex`, and no keyboard event handler. A keyboard user cannot open or close email accordions. This is a functional accessibility failure.

This is flagged in the code comments at lines 56-59 as parked. It is not cosmetic — keyboard users cannot use the core feature of this page.

**Standard:** WCAG 2.1.1 Keyboard (Level A). Nielsen H3 — User control and freedom (keyboard users have no control path).

**Correct behavior:**

```jsx
<div
  role="button"
  tabIndex={0}
  aria-expanded={isOpen}
  aria-controls={`email-panel-${email.id}`}
  className="flex items-center gap-3 px-4 py-3 hover:bg-slate-700 transition-colors cursor-pointer select-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-slate-400"
  onClick={() => onToggle(email.id)}
  onKeyDown={(e) => {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      onToggle(email.id);
    }
  }}
>
```

The accordion panel div should receive `id={`email-panel-${email.id}`}` to match `aria-controls`. `aria-expanded` communicates open/closed state to screen readers.

---

### Issue 6 — Approve and Decline buttons have no focus indicator

**Where:** `ActionRowV3`, both the Approve button and Decline button.

**Problem:** Current classes: `text-xs text-green-400 hover:text-green-300 transition-colors` and `text-xs text-slate-500 hover:text-slate-400 transition-colors`. No focus style. The browser's default outline is suppressed in most Tailwind configurations via preflight. Keyboard users see no focus indicator when tabbing to these buttons.

**Standard:** WCAG 2.4.7 Focus Visible (Level AA). Nielsen H3 — keyboard users cannot see which button has focus.

**Correct behavior:** Add `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400` to both buttons.

Approve button final class:
```
text-xs text-green-400 hover:text-green-300 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-green-400 rounded
```

Decline button final class (incorporating the contrast fix from Issue 2):
```
text-xs text-slate-400 hover:text-slate-300 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400 rounded
```

The `rounded` class ensures the ring follows the button's shape.

---

### Issue 7 — Input focus style removes outline and replaces it with insufficient indicator

**Where:** All inputs in `ActionRowV3` — name input and datetime input, class fragment `focus:outline-none focus:border-slate-500`

**Problem:** `focus:outline-none` removes the browser focus ring. The replacement is a border color change from `border-slate-700` (#334155) to `border-slate-500` (#64748b). The change is 1px and low-contrast. On a dark background, this is nearly invisible. A keyboard user cannot reliably determine which input has focus.

**Standard:** WCAG 2.4.7 Focus Visible (Level AA). WCAG 2.4.11 Focus Not Obscured (Level AA, added in 2.2).

**Correct behavior:** Keep `focus:outline-none` to suppress the default outline. Add a visible ring as the explicit focus indicator:

Name input focus classes:
```
focus:outline-none focus:border-slate-500 focus-visible:ring-2 focus-visible:ring-slate-400 focus-visible:ring-offset-0
```

Datetime input focus classes (same pattern):
```
focus:outline-none focus:border-slate-500 focus-visible:ring-2 focus-visible:ring-slate-400 focus-visible:ring-offset-0
```

The ring is `ring-slate-400` on `bg-slate-800` — this is the input container background. Contrast of ring against input background: approximately 5.7:1. Passes the 3:1 minimum for focus indicators (WCAG 2.4.11) and the 4.5:1 threshold for visibility.

---

### Issue 8 — Chevron SVG is not hidden from accessibility tree

**Where:** `InboxRow`, the chevron `<svg>` element at the end of the row.

**Problem:** The chevron is decorative — it indicates open/closed state visually, but this same information is conveyed by `aria-expanded` on the row (after Issue 5 fix) and by the presence of the panel itself. Screen readers will attempt to announce the SVG, which produces noise (often announced as empty or as path data).

**Standard:** WCAG 1.1.1 Non-text Content (Level A) — decorative images must be hidden from assistive technology with `aria-hidden="true"`.

**Correct behavior:** Add `aria-hidden="true"` to the chevron SVG.

Also flagged in the code comment at line 59 as parked.

---

### Issue 9 — Back button uses button semantics for navigation

**Where:** `EmailTriage`, the Back button, `<button onClick={() => { window.location.href = "/dashboard"; }}>`

**Problem:** This is a navigation action — it takes the user to a different URL. Using a `<button>` element for navigation is semantically incorrect. Screen readers announce it as a button (implying a stateful action), not a link (implying navigation). Keyboard users may not expect that Enter on what they hear as "Back, button" will navigate away. This is inconsistent with web standards.

**Standard:** WCAG 4.1.2 Name, Role, Value (Level A) — UI components must have correct roles. Nielsen H4 — Consistency and standards — navigation controls are links on the web.

**Correct behavior:** Replace with an anchor element:

```jsx
<a
  href="/dashboard"
  className="text-sm text-slate-400 hover:text-slate-200 transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-slate-400 rounded"
>
  &larr; Back
</a>
```

If the project uses React Router, use `<Link to="/dashboard">` instead.

---

### Issue 10 — Actions section has no visible section header

**Where:** `ActionsPanel`, before the action rows.

**Problem:** The accordion panel opens directly into action rows with no label identifying what they are. The pitch fat marker sketch shows an "Actions" section label. Without it, the owner must infer the purpose of the rows from context. This is a recognition failure — the section is not self-identifying.

**Standard:** Nielsen H6 — Recognition over recall. The interface should not require the user to remember what these rows are; the section label makes it explicit.

**Correct behavior:** Add a section heading immediately before the action rows in `ActionsPanel`:

```jsx
<div className="space-y-2 mt-2">
  <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
    Actions
  </p>
  {actions.map((action) => (
    <ActionRowV3 ... />
  ))}
  ...
</div>
```

`text-slate-400` on `bg-slate-900`: approximately 7.1:1. Passes AA. No new component needed — this is a paragraph element with existing tokens.

---

## Nielsen's 10 Heuristics Self-Review

Run against both parts of this spec before delivery.

**H1 — Visibility of system status**
Part 1: Actions load in one fetch with a single loading indicator. Log appears when fetch resolves, reconstructed from the data already in hand. No dual loading states. Error state shown when fetch fails. The owner always knows whether data is loading, loaded, or unavailable.
Part 2: Contrast fixes make all status text (type labels, log headings, timestamps) visible. The system cannot communicate status that the user cannot read. Pass.

**H2 — Match between system and real world**
Log entry language unchanged from prior spec (Issue 2 fix). Section header "Actions" matches what the breadboard calls this section. Type labels ("Task", "Event") match real-world categories. Pass.

**H3 — User control and freedom**
Part 1: Resolved states render immediately on accordion open — no loss of control state between sessions.
Part 2: InboxRow keyboard fix (Issue 5) restores keyboard access to the primary navigation gesture. Approve/Decline focus styles (Issue 6) restore keyboard users' ability to operate the primary action controls. Pass after fixes.

**H4 — Consistency and standards**
Back button semantic fix (Issue 9) aligns navigation controls with web conventions. Focus ring pattern is consistent across all interactive elements after Issues 6 and 7. Pass after fixes.

**H5 — Error prevention**
Contrast fixes (Issues 1-4) prevent the owner from missing information due to invisible text. Status reconstruction from GET /actions prevents stale data from causing incorrect rendering decisions. Pass.

**H6 — Recognition over recall**
Actions section header (Issue 10) makes the section self-identifying. Resolved state rendering on accordion open means the owner does not need to remember what they approved in a prior session — it is shown. Pass.

**H7 — Flexibility and efficiency**
No changes to the approval flow. The state reconstruction improvement means experienced users do not need to re-approve already-resolved actions after a page refresh. Net improvement.

**H8 — Aesthetic and minimalist design**
All proposed additions serve a functional purpose: section header aids recognition, focus rings aid accessibility, contrast corrections aid readability. No decorative elements added. The removal of the separate /log endpoint call simplifies the data flow. Pass.

**H9 — Help users recognize, diagnose, and recover from errors**
Error states from Part 1 (actions fetch fail) remain clear and human-readable. Not within scope of Part 2 design review. Pass.

**H10 — Help and documentation**
Not applicable for this single-user operational tool. Pass.

**Result:** No heuristic failures after applying all fixes. Spec is ready for Devon / Codex.

---

## Implementation Summary — What Codex Needs to Change

**Part 1 — State reconstruction:**

1. Fix the merge priority in the `ActionsPanel` effect: API status is authoritative for resolved states. Session status only overrides API status when the action was resolved in the current session.
2. Remove the GET `/api/email-management/emails/${emailId}/log` fetch entirely.
3. After GET /actions resolves, filter approved actions, sort by `approved_at` descending, and build log entries using the existing `buildLogEntry` function.
4. Merge backend-derived log entries with session log entries using the existing pattern.

**Part 2 — Design fixes (Tailwind token changes + structural):**

| Location | Current | Change |
|---|---|---|
| InboxRow — received date | `text-slate-600` | `text-slate-400` |
| ActionRowV3 — Decline button | `text-slate-500 hover:text-slate-400` | `text-slate-400 hover:text-slate-300` + focus ring |
| ActionRowV3 — type label | `text-slate-500` | `text-slate-400` |
| ActionsPanel — log heading | `text-slate-500` | `text-slate-400` |
| InboxRow — outer div | no role/tabIndex/keyboard | role="button", tabIndex={0}, aria-expanded, onKeyDown, focus ring |
| ActionRowV3 — Approve button | no focus style | add focus-visible:ring |
| ActionRowV3 — Decline button | no focus style | add focus-visible:ring |
| ActionRowV3 — name input | focus:outline-none focus:border-slate-500 | add focus-visible:ring-2 focus-visible:ring-slate-400 |
| ActionRowV3 — datetime input | focus:outline-none focus:border-slate-500 | add focus-visible:ring-2 focus-visible:ring-slate-400 |
| InboxRow — chevron SVG | no aria-hidden | aria-hidden="true" |
| EmailTriage — Back button | `<button onClick window.location.href>` | `<a href="/dashboard">` |
| ActionsPanel — before action rows | no section label | add `<p>Actions</p>` with text-slate-400 text-xs uppercase |

---

*Quinn — 2026-06-28*
