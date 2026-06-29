# Interaction Spec — Email Management Slice 4: Disposition

**Author:** Quinn
**Date:** 2026-06-29
**Status:** Ready for Devon / Codex
**References:** pitch-v1.md (Slice 4), Quinn-interaction-spec-full-review.md, ActionsPanel.jsx, InboxRow.jsx, EmailTriage.jsx

---

## Scope

This spec covers the Archive and Delete buttons, the all-resolved disabled gate, the optimistic move to the Processed section, the processed row and accordion, and all error and accessibility behavior for Slice 4.

All Slice 3 component structure (ActionsPanel, ActionRowV3, buildLogEntry, emailSessions state) is assumed to be in place. This spec does not restate Slice 3 behavior.

---

## Issue 1 — Archive and Delete button placement

**Where:** `ActionsPanel.jsx`, bottom of the returned JSX.

**Render order within the accordion panel:**
1. "Actions" section header
2. Action rows (`ActionRowV3`)
3. `+ Task` / `+ Event` button row
4. Execution log (conditional — only when `logEntries.length > 0`)
5. Archive / Delete button row (always rendered; disabled state controlled by gate — see Issue 2)

The Archive and Delete buttons appear below the execution log. If no log entries exist yet (owner has not approved any actions), they appear directly below the `+ Task` / `+ Event` row.

The button row is separated from the section above by a top border divider, matching the existing execution log section divider pattern (`border-t border-slate-700`).

**JSX position in ActionsPanel return:**

```jsx
{/* Disposition — bottom of ActionsPanel, after execution log */}
<div className="flex justify-end gap-2 mt-3 pt-3 border-t border-slate-700">
  <button
    disabled={!allResolved}
    aria-label="Archive email"
    aria-disabled={!allResolved}
    onClick={handleArchive}
    className="..."
  >
    Archive
  </button>
  <button
    disabled={!allResolved}
    aria-label="Delete email"
    aria-disabled={!allResolved}
    onClick={handleDelete}
    className="..."
  >
    Delete
  </button>
</div>
```

Archive is to the left of Delete. This matches the fat marker sketch in pitch-v1.md: `[Archive]  [Delete]`.

---

## Issue 2 — All-resolved gate: computation and HTML disabled attribute

**Computation (add to ActionsPanel body):**

```js
const allResolved =
  actions !== null &&
  actions.every(
    (a) => a.status === "approved" || a.status === "declined"
  );
```

Behavior notes:
- `actions === null` means the GET /actions fetch is in flight. Both buttons are disabled during loading.
- Empty array (`actions.length === 0`): `every` returns `true` vacuously. Buttons activate immediately when no action rows exist. This is correct — the owner can dispose without adding any actions.
- Any single row with `status: "pending"` keeps `allResolved` false.

**HTML attribute vs CSS-only approach:**

Use the HTML `disabled` attribute on both `<button>` elements. Do not use a CSS-only approach.

Rationale:
- `disabled` prevents native click events without a JavaScript guard.
- Browsers and screen readers natively announce a disabled button as unavailable. `aria-disabled="true"` without `disabled` keeps the button focusable and requires additional JavaScript click prevention.
- This is consistent with the existing `Run Triage` button which uses `disabled={runLoading}`.

```jsx
<button disabled={!allResolved} ...>Archive</button>
<button disabled={!allResolved} ...>Delete</button>
```

---

## Issue 3 — Button classes: disabled state

Applied via Tailwind `disabled:` variant on the same element. No separate conditional class string needed.

**Archive button (disabled visual state):**
`disabled:opacity-40 disabled:cursor-not-allowed`

**Delete button (disabled visual state):**
`disabled:opacity-40 disabled:cursor-not-allowed`

Identical for both. `opacity-40` communicates unavailability. `cursor-not-allowed` reinforces the blocked interaction. `pointer-events-none` is not needed — the `disabled` HTML attribute blocks click events natively on `<button>` elements.

---

## Issue 4 — Button classes: active state, hover, and focus

**Archive button — full class string:**
```
px-3 py-1.5 text-xs rounded bg-slate-700 hover:bg-slate-600 text-slate-100 font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400 disabled:opacity-40 disabled:cursor-not-allowed
```

**Delete button — full class string:**
```
px-3 py-1.5 text-xs rounded bg-red-900 hover:bg-red-800 text-red-200 font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-red-400 disabled:opacity-40 disabled:cursor-not-allowed
```

Token sources:
- `bg-slate-700 hover:bg-slate-600 text-slate-100`: used by `Run Triage` button in EmailTriage.jsx.
- `bg-red-900 text-red-200`: used by the error banner in EmailTriage.jsx (`bg-red-900 border border-red-700 text-red-200`). `hover:bg-red-800` is one step lighter in the same token family.
- `focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900`: identical to the focus ring pattern on Approve/Decline buttons per Quinn-interaction-spec-full-review.md Issue 6. The accordion panel background is `bg-slate-900` (InboxRow.jsx: `className="... bg-slate-900 ..."`), so `ring-offset-slate-900` is correct.
- `focus-visible:ring-slate-400`: used on Approve button (full-review spec Issue 6) and Back link.
- `focus-visible:ring-red-400`: not yet on an element but consistent with the red token family (`bg-red-900`, `text-red-200`). The ring color matches the button's visual identity.

---

## Issue 5 — Click behavior: optimistic update sequence

**Approach:** Optimistic update. The UI responds immediately on click. Backend call fires after the state change. The pitch is explicit: "Clicking either button immediately adds a 'Processed' label to the email row."

**Sequence on Archive click (Delete follows the same sequence with `"delete"` substituted):**

Step 1 — `ActionsPanel.handleArchive`:
  a. Build the disposition log entry: `buildDispositionLogEntry("archive", new Date())` (see Issue 6).
  b. Persist the entry in session state before unmount: `updateEmailSession(emailId, (prev) => ({ ...prev, logEntries: [dispositionEntry, ...(prev.logEntries || [])] }))`.
  c. Call `onDispose("archive")`.

Step 2 — `EmailTriage.handleDispose(emailId, "archive")` (synchronous state updates, then async API):
  a. Move the email object from `pendingEmails` to front of `processedEmails`.
  b. Clear any existing `disposeErrors[emailId]`.
  c. Fire `emailTriageApi.disposeEmail(emailId, "archive")` asynchronously.

Step 3 — React re-render:
  - Email disappears from Pending section.
  - Email appears at top of Processed section with "✓ Processed" badge.
  - Accordion closes because the email is no longer in the pending list.
  - `ActionsPanel` unmounts.

Step 4 — Backend response:
  - Success: no further state change.
  - Failure: see Issue 11.

**No loading state on the Archive/Delete buttons.** Steps 1 through 3 are synchronous React state updates that resolve in a single render cycle. The buttons are not visible after step 3. A loading state would introduce an async gap before the optimistic move, which contradicts "immediately."

---

## Issue 6 — Disposition log entry format

**New helper:** `buildDispositionLogEntry(disposition, ts)` in the same `formatters.js` file that exports `buildLogEntry`.

```js
/**
 * Builds a disposition log entry string.
 * @param {"archive"|"delete"} disposition
 * @param {Date|string} ts
 * @returns {string} e.g. "29 Jun 2026 14:09  Email archived"
 */
export function buildDispositionLogEntry(disposition, ts) {
  const d = ts instanceof Date ? ts : new Date(ts);
  const dateStr = d.toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
  const timeStr = d.toLocaleTimeString("en-GB", {
    hour: "2-digit",
    minute: "2-digit",
  });
  const label = disposition === "archive" ? "Email archived" : "Email deleted";
  return `${dateStr} ${timeStr}  ${label}`;
}
```

Output examples:
- `"29 Jun 2026 14:09  Email archived"`
- `"29 Jun 2026 14:09  Email deleted"`

The two-space separator between timestamp and label is identical to the existing `buildLogEntry` format. The timestamp locale and field order match existing log entries.

The disposition entry is prepended to `logEntries` (index 0), consistent with the newest-first storage order already used for approve entries. The `ProcessedPanel` reverses the array for display so the disposition entry appears as the final visible line (see Issue 10).

---

## Issue 7 — Success state: row and section changes

**Pending section:**
- The dispositioned email disappears from the list.
- Section count decrements: `PENDING · {n-1}`.
- If `pendingEmails.length` reaches 0, the Pending section header can remain visible with `PENDING · 0` or be hidden. Devon's call — either is acceptable.

**Processed section:**
- The email appears at the top (prepended) with a "✓ Processed" badge.
- Section count increments: `PROCESSED · {n+1}`.

**"Processed" badge JSX:**

```jsx
<span className="inline-flex items-center gap-1 text-xs rounded px-1.5 py-0.5 bg-slate-700 text-green-400 font-medium shrink-0">
  ✓ Processed
</span>
```

Token sources: `bg-slate-700` (Run Triage button base), `text-green-400` (Approve button in ActionRowV3). No new tokens.

---

## Issue 8 — EmailTriage.jsx state and section layout changes

**Replace `emails` state with two lists:**

```js
const [pendingEmails, setPendingEmails] = useState([]);
const [processedEmails, setProcessedEmails] = useState([]);
const [disposeErrors, setDisposeErrors] = useState({}); // { [emailId]: string | null }
```

**Split on initial load:**

```js
emailTriageApi.getEmails().then((d) => {
  setPendingEmails(d.emails.filter((e) => e.status !== "processed"));
  setProcessedEmails(
    d.emails
      .filter((e) => e.status === "processed")
      .sort((a, b) => new Date(b.processed_at || 0) - new Date(a.processed_at || 0))
  );
});
```

The API is expected to return `status` and optionally `processed_at` on each email object. If `processed_at` is not available, sort order on initial load falls back to API return order.

**handleDispose function:**

```js
const handleDispose = useCallback(
  async (emailId, disposition) => {
    const email = pendingEmails.find((e) => e.id === emailId);
    if (!email) return;

    // Optimistic move
    setPendingEmails((prev) => prev.filter((e) => e.id !== emailId));
    setProcessedEmails((prev) => [{ ...email, status: "processed" }, ...prev]);
    setDisposeErrors((prev) => ({ ...prev, [emailId]: null }));

    try {
      await emailTriageApi.disposeEmail(emailId, disposition);
    } catch (e) {
      // Rollback
      setProcessedEmails((prev) => prev.filter((e) => e.id !== emailId));
      setPendingEmails((prev) => [...prev, email]);
      setDisposeErrors((prev) => ({ ...prev, [emailId]: e.message }));
      // Remove the disposition log entry written before the call
      updateEmailSession(emailId, (prev) => ({
        ...prev,
        logEntries: (prev.logEntries || []).slice(1),
      }));
    }
  },
  [pendingEmails, updateEmailSession]
);
```

Note: rollback re-appends the email to the end of the pending list, not its original position. This is acceptable for this scope.

**New API client method (add to `emailTriageApi`):**

```js
disposeEmail(emailId, disposition) {
  // POST /api/email-management/emails/${emailId}/dispose
  // Body: { disposition: "archive" | "delete" }
  // Returns 200 on success, error with message on failure
}
```

The endpoint is Kai's boundary. Devon adds only the client-side method.

**Section layout in EmailTriage.jsx JSX (replace existing single-list render):**

```jsx
{/* Pending section */}
{!loading && pendingEmails.length > 0 && (
  <div className="mb-6">
    <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
      Pending · {pendingEmails.length}
    </p>
    <div className="bg-slate-800 rounded-lg overflow-hidden divide-y divide-slate-700">
      {pendingEmails.map((email) => (
        <InboxRow
          key={email.id}
          email={email}
          isOpen={openEmailId === email.id}
          onToggle={handleToggle}
          emailSession={emailSessions[email.id]}
          updateEmailSession={updateEmailSession}
          onDispose={(disposition) => handleDispose(email.id, disposition)}
          disposeError={disposeErrors[email.id] || null}
        />
      ))}
    </div>
  </div>
)}

{/* Empty state */}
{!loading && pendingEmails.length === 0 && processedEmails.length === 0 && !error && (
  <div className="text-center py-16">
    <p className="text-slate-500 text-sm">No emails yet. Click Run Triage to start.</p>
  </div>
)}

{/* Processed section */}
{processedEmails.length > 0 && (
  <div>
    <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
      Processed · {processedEmails.length}
    </p>
    <div className="bg-slate-800 rounded-lg overflow-hidden divide-y divide-slate-700">
      {processedEmails.map((email) => (
        <ProcessedRow
          key={email.id}
          email={email}
          isOpen={openEmailId === email.id}
          onToggle={handleToggle}
          emailSession={emailSessions[email.id]}
        />
      ))}
    </div>
  </div>
)}
```

**InboxRow prop additions:**

```jsx
export function InboxRow({ email, isOpen, onToggle, emailSession, updateEmailSession, onDispose, disposeError }) {
```

Pass `onDispose` through to `ActionsPanel`:

```jsx
<ActionsPanel
  emailId={email.id}
  emailSession={emailSession}
  updateEmailSession={updateEmailSession}
  onDispose={onDispose}
/>
```

Render `disposeError` band below the row header, above the accordion:

```jsx
{disposeError && (
  <div className="mx-4 mt-1 mb-2 p-2 rounded bg-red-900 border border-red-700 text-red-200 text-xs">
    Disposition failed: {disposeError}
  </div>
)}
```

**ActionsPanel prop additions:**

```jsx
export function ActionsPanel({ emailId, emailSession, updateEmailSession, onDispose }) {
```

---

## Issue 9 — Processed row styling

**New component:** `src/components/EmailTriage/ProcessedRow.jsx`

The processed row shares the toggle behavior and visual structure of `InboxRow` but:
- All text uses `text-slate-400` (sender name drops from `text-slate-200` to `text-slate-400`; subject and date stay `text-slate-400`).
- "✓ Processed" badge replaces any classification badge.
- The accordion renders `ProcessedPanel`, not `ActionsPanel`.
- No `disposeError` or `onDispose` — processed rows are read-only.

**ProcessedRow header JSX:**

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
  <div className="flex-1 min-w-0">
    <div className="flex items-center gap-1.5">
      <span className="text-slate-400 text-sm font-medium truncate">
        {senderName}
      </span>
      <span className="inline-flex items-center gap-1 text-xs rounded px-1.5 py-0.5 bg-slate-700 text-green-400 font-medium shrink-0">
        ✓ Processed
      </span>
      {email.gmail_url && (
        <a
          href={email.gmail_url}
          target="_blank"
          rel="noopener noreferrer"
          className="shrink-0 text-slate-500 hover:text-slate-300 transition-colors"
          aria-label="Open in Gmail"
          onClick={(e) => e.stopPropagation()}
        >
          {/* same external link SVG as InboxRow */}
        </a>
      )}
    </div>
    <div className="flex items-baseline justify-between gap-4 mt-0.5">
      <p className="text-slate-400 text-xs truncate">
        {email.subject || "(no subject)"}
      </p>
      <span className="text-slate-400 text-xs shrink-0 whitespace-nowrap">
        {receivedAt}
      </span>
    </div>
  </div>
  <svg
    aria-hidden="true"
    className={`shrink-0 text-slate-500 transition-transform duration-200 ${isOpen ? "rotate-180" : ""}`}
    xmlns="http://www.w3.org/2000/svg"
    width="14"
    height="14"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <polyline points="6 9 12 15 18 9" />
  </svg>
</div>
```

Key differences from `InboxRow` header: sender name is `text-slate-400` (not `text-slate-200`), badge is "✓ Processed" instead of classification badge.

---

## Issue 10 — Processed accordion: ProcessedPanel component

**New component:** `src/components/EmailTriage/ProcessedPanel.jsx`

Renders the execution log for a processed email. No actions, no `+ Task`/`+ Event`, no disposition buttons.

**Display order:** Log entries are stored newest-first (disposition entry at index 0, oldest action approval at the end). The processed panel renders them in reverse — oldest first, disposition entry last — so the disposition entry is always the final visible line, matching the pitch: "Execution log in processed accordion always shows the disposition entry as final line."

```jsx
export function ProcessedPanel({ emailSession }) {
  const logEntries = emailSession?.logEntries || [];
  const displayEntries = [...logEntries].reverse(); // oldest first, disposition last

  if (displayEntries.length === 0) {
    return (
      <p className="text-slate-500 text-xs mt-2">No actions recorded.</p>
    );
  }

  return (
    <div className="mt-2" aria-label="Execution log">
      <p className="text-slate-400 text-xs font-medium mb-2">Execution log</p>
      <ul className="space-y-1">
        {displayEntries.map((entry, i) => (
          <li key={i} className="text-slate-400 text-xs font-mono">
            {entry}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

**ProcessedRow accordion panel JSX:**

```jsx
{isOpen && (
  <div
    id={`email-panel-${email.id}`}
    className="mx-4 mb-3 border border-slate-700 rounded bg-slate-900 px-4 py-3"
  >
    {email.summary && (
      <div className="mb-3">
        <p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-1">
          Email Summary
        </p>
        <p className="text-slate-400 text-xs">{email.summary}</p>
      </div>
    )}
    <ProcessedPanel emailSession={emailSession} />
  </div>
)}
```

The accordion container class is identical to `InboxRow`'s accordion panel. `email.summary` is rendered if present. If Email Summary is also absent from the current `InboxRow` pending accordion, Devon should add it there in the same pass (same pattern: `email.summary && ...` above `ActionsPanel`).

---

## Issue 11 — Error state: rollback and display

**When `emailTriageApi.disposeEmail` rejects:**

1. `processedEmails` is updated: the email is removed.
2. `pendingEmails` is updated: the email is re-appended.
3. `disposeErrors[emailId]` is set to `e.message`.
4. The disposition log entry is removed from `emailSession.logEntries` (the first element, prepended in Issue 5 step 1b): `logEntries.slice(1)`.
5. The accordion is not automatically re-opened. The user sees the error band on the row and must re-open to retry.

**Error band (rendered in `InboxRow` below the row header):**

```jsx
{disposeError && (
  <div className="mx-4 mt-1 mb-2 p-2 rounded bg-red-900 border border-red-700 text-red-200 text-xs">
    Disposition failed: {disposeError}
  </div>
)}
```

Tokens: `bg-red-900 border border-red-700 text-red-200` — identical to the error banner in `EmailTriage.jsx`, at smaller scale (`text-xs`, `p-2` instead of `text-sm`, `p-3`).

**Error dismissal:** The error clears when the user clicks Archive or Delete again and the call succeeds (`setDisposeErrors` sets the value to `null` at the start of `handleDispose` before the API call).

---

## Issue 12 — Accessibility

**Archive button:**
```jsx
<button
  disabled={!allResolved}
  aria-label="Archive email"
  aria-disabled={!allResolved}
  onClick={handleArchive}
  className="... rounded"
>
  Archive
</button>
```

**Delete button:**
```jsx
<button
  disabled={!allResolved}
  aria-label="Delete email"
  aria-disabled={!allResolved}
  onClick={handleDelete}
  className="... rounded"
>
  Delete
</button>
```

**`aria-disabled` alongside `disabled`:** When `disabled` is present on a `<button>`, `aria-disabled="true"` is redundant but not harmful. Include it explicitly for consistent announcement across all screen readers. Some older screen readers handle `disabled` inconsistently on buttons not inside a `<form>`.

**`aria-label`:** The visible text "Archive" and "Delete" is sufficient for most contexts. `aria-label` makes the target action explicit ("Archive email", "Delete email") when the button is announced in isolation — for example, when navigating by button via screen reader without surrounding context. This is a low-cost addition.

**Screen reader announcement when disabled:**
- NVDA/JAWS: "Archive email, button, dimmed" or "unavailable"
- VoiceOver: "Archive email, dimmed button"

This is sufficient. No additional hint text (e.g. "resolve all actions first") is required for this scope.

**`rounded` class on both buttons:** Required to ensure the `focus-visible:ring` follows the button's shape correctly.

**Focus order within ActionsPanel:** The Archive and Delete buttons are the last two focusable elements in the panel. Tab order: action row inputs → Approve buttons → Decline buttons → + Task → + Event → Archive → Delete. This matches the visual top-to-bottom layout and requires no additional `tabIndex` manipulation.

**`aria-live` on the Processed section header:** The section count updates when an email is processed. Wrap the count in a live region so screen reader users hear the update:

```jsx
<p className="text-xs font-medium text-slate-400 uppercase tracking-wide mb-2">
  Processed{" "}
  <span aria-live="polite" aria-atomic="true">
    · {processedEmails.length}
  </span>
</p>
```

`aria-atomic="true"` ensures the full count is announced, not just the changed digit.

---

## Issue 13 — Design token consistency

All tokens used in this spec are already present in the existing components or are first-degree extensions of existing token families.

| Token | Source |
|---|---|
| `bg-slate-700 hover:bg-slate-600 text-slate-100` | `Run Triage` button in EmailTriage.jsx |
| `bg-red-900 text-red-200` | Error banner in EmailTriage.jsx |
| `hover:bg-red-800` | One step lighter than `bg-red-900` — same token family, same pattern as `bg-slate-700 hover:bg-slate-600` |
| `text-green-400` | Approve button in ActionRowV3 |
| `bg-slate-700` (badge background) | Run Triage button |
| `border-slate-700 border-t` | Execution log divider already in ActionsPanel |
| `focus-visible:ring-2 focus-visible:ring-offset-1 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400` | Approve/Decline buttons per full-review spec Issue 6 |
| `focus-visible:ring-red-400` | First use, but consistent with the red token family (`bg-red-900`, `text-red-200`) already in the system. The ring color matches the button's visual identity. |
| `text-slate-400 text-xs font-mono` | Execution log entries in ActionsPanel |
| `bg-red-900 border border-red-700 text-red-200 text-xs` | Error banner — scaled down from EmailTriage.jsx error banner |

No new color families. `ring-red-400` is the only first-use token; it is a direct member of the Tailwind red scale already in use.

---

## Nielsen's 10 Heuristics Self-Review

**H1 — Visibility of system status**
Pending count decrements on disposition. Processed count increments. The "✓ Processed" badge makes the outcome unambiguous on the processed row. Pass.

**H2 — Match between system and real world**
"Archive" and "Delete" are standard email actions. Log entries "Email archived" / "Email deleted" use real-world terminology consistent with Gmail. Pass.

**H3 — User control and freedom**
No undo is provided — disposition is an irreversible action by design (pitch no-gos). The Delete button uses red tokens to signal destructive action. The disabled gate prevents premature disposition before all actions are reviewed. The processed accordion is always accessible, so the owner can review what was done. Pass within scope.

**H4 — Consistency and standards**
Button size and padding match the `Run Triage` button at `px-3 py-1.5 text-xs`. Focus ring pattern is identical to all other interactive elements in the component. Section header pattern (`text-xs font-medium text-slate-400 uppercase tracking-wide`) matches "Actions" and "Execution log" headings. The `ProcessedRow` row toggle reuses the exact same `role="button"` pattern from `InboxRow`. Pass.

**H5 — Error prevention**
The all-resolved gate prevents accidental disposition before all action rows are reviewed. The Delete button is visually distinct (red) to signal irreversible action. Pass.

**H6 — Recognition over recall**
Section headers "PENDING · N" and "PROCESSED · N" make the page state immediately scannable without requiring the owner to count rows. The "✓ Processed" badge on processed rows removes ambiguity at a glance. The processed accordion preserves the full log so the owner does not need to remember what was approved. Pass.

**H7 — Flexibility and efficiency**
The owner can open any processed accordion to review the full execution log including the disposition entry. Pass.

**H8 — Aesthetic and minimalist design**
Two buttons, one badge, two section headers, one new divider. No decorative additions. The processed row is a simplified version of the pending row — same structure, lower visual weight, no action controls. Pass.

**H9 — Help users recognize, diagnose, and recover from errors**
Disposition failure shows a red inline error band at the row level with the error message. The email returns to Pending. The error uses the same token pattern as the existing error banner. No new error patterns introduced. Pass.

**H10 — Help and documentation**
Not applicable for this single-user operational tool. Pass.

---

## Implementation Summary

| # | File | Change |
|---|---|---|
| 1 | `ActionsPanel.jsx` | Add `onDispose` prop; add `allResolved` computation; add `handleArchive` and `handleDelete` functions that call `buildDispositionLogEntry`, persist to `updateEmailSession`, then call `onDispose`; add Archive/Delete button row at bottom of returned JSX |
| 2 | `formatters.js` | Add `buildDispositionLogEntry(disposition, ts)` export |
| 3 | `EmailTriage.jsx` | Replace `emails` state with `pendingEmails` + `processedEmails` + `disposeErrors`; split initial load; add `handleDispose(emailId, disposition)` async function with optimistic move and rollback; render two sections with counts and live region on Processed count; pass `onDispose` and `disposeError` to `InboxRow` |
| 4 | `InboxRow.jsx` | Add `onDispose` and `disposeError` props; render `disposeError` error band; pass `onDispose` to `ActionsPanel` |
| 5 | `ProcessedRow.jsx` | New component: processed row header with "✓ Processed" badge, `text-slate-400` sender name, same toggle pattern as `InboxRow`; accordion renders Email Summary (if present) + `ProcessedPanel` |
| 6 | `ProcessedPanel.jsx` | New component: renders `emailSession.logEntries` reversed for display (oldest first, disposition entry last); read-only log, no actions |
| 7 | `emailTriage.js` (API client) | Add `disposeEmail(emailId, disposition)` method posting to `/api/email-management/emails/${emailId}/dispose` |

---

*Quinn — 2026-06-29*
