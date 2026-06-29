# Interaction Spec — Email Management Slice 5: Run Triage (live)

**Author:** Quinn
**Date:** 2026-06-29
**Status:** Ready for Devon / Codex
**References:** pitch-v1.md (Slice 5 + AI latency rabbit hole), Quinn-interaction-spec-full-review.md, EmailTriage.jsx, routes.py (`POST /api/email-management/run`)

---

## Backend contract summary

`POST /api/email-management/run` is synchronous. It fetches up to 20 unread Gmail messages, calls the AI service per message, inserts emails and actions into the DB, and returns `{processed, skipped, errors}` when all messages are done. There is no streaming endpoint. The response arrives as a single payload after all processing is complete (5+ seconds under normal conditions).

---

## Issue 1 — Button: placement and normal state

**Where:** Top of `<main>`, inside the existing `<div className="flex items-center gap-4 mb-6">`. This matches the current implementation placement. The fat marker sketch positions the button top-right of the page header — that layout change is not in scope for this slice.

**Normal state label:** "Run Triage"

**Normal state classes** (current classes corrected to add focus ring and cursor):

```
px-4 py-2 text-sm rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-100
disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium
focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2
focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400
```

The current implementation is missing `disabled:cursor-not-allowed` and the focus ring. Both are required.

---

## Issue 2 — Loading state: decision and specification

**Decision: status indicator.** Not optimistic UI. Not skeleton loading.

**Rationale:**
- The backend is synchronous with no streaming. There is no per-email progress signal to render.
- Skeleton loading requires knowing the incoming email count in advance. We do not.
- Optimistic UI is not applicable: the emails arriving are unknown until the response lands.
- A spinner on the button plus a `aria-live` status line is the minimum unambiguous indicator for a 5–10 second wait. It does not overstate certainty, and it does not make the list appear broken.

**Behavior during the call:**

The pending list stays frozen in its current state. If there are existing pending emails, they remain visible and interactable. If the list was empty, the empty state copy remains ("No emails yet. Click Run Triage to start."). Nothing goes blank.

**Button loading state:**

The button label changes from "Run Triage" to a spinner icon + "Running..." inline. The spinner is a 14x14px inline SVG with `animate-spin`. The button is disabled.

```jsx
<button
  onClick={handleRunTriage}
  disabled={runLoading}
  aria-busy={runLoading}
  className="inline-flex items-center gap-2 px-4 py-2 text-sm rounded-lg bg-slate-700 hover:bg-slate-600
             text-slate-100 disabled:opacity-50 disabled:cursor-not-allowed transition-colors font-medium
             focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2
             focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400"
>
  {runLoading && (
    <svg
      aria-hidden="true"
      className="w-3.5 h-3.5 animate-spin text-slate-300"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
      <path className="opacity-75" fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
    </svg>
  )}
  {runLoading ? "Running..." : "Run Triage"}
</button>
```

---

## Issue 3 — Progress feedback during the wait

**No streaming is available from the backend.** Per-email count ("Processing email 3 of 8") requires the backend to emit progress events. The backend does not do this. Specifying that UI now would force a backend change outside this slice's scope.

**What the owner sees:**

1. The button shows spinner + "Running..." (Issue 2).
2. A status line immediately below the button row renders: "Running triage..." in `text-slate-400 text-xs`.
3. This status line is a `aria-live` region (Issue 8). Screen readers announce "Running triage..." when it appears.
4. No time estimate is shown. No percentage. No email count.

```jsx
{/* Status region — always mounted, content changes with state */}
<span
  role="status"
  aria-live="polite"
  aria-atomic="true"
  className="text-slate-400 text-xs"
>
  {runLoading && "Running triage..."}
  {!runLoading && runResult && runResult.processed > 0 &&
    `${runResult.processed} email${runResult.processed === 1 ? "" : "s"} processed`}
  {!runLoading && runResult && runResult.processed === 0 && !error &&
    "No new emails found"}
</span>
```

This region replaces the current inline `runResult` span that uses `|` separators. The processed/skipped/errors breakdown is removed — it is noise for the owner. "X emails processed" or "No new emails found" is sufficient.

---

## Issue 4 — Success state

After `runTriage()` resolves and `loadEmails()` completes:

1. The button returns to "Run Triage" (spinner gone, `aria-busy="false"`).
2. The status region (Issue 3) shows "X emails processed" (or "No new emails found" if processed = 0).
3. The pending list refreshes. New emails appear at the top because `GET /api/email-management/emails` returns `ORDER BY received_at DESC`. The section counter "Pending · N" updates.
4. The section counter change is the visual cue that new emails arrived. No per-row animation is required. The count delta is immediately visible.

If `runResult.errors > 0` alongside `runResult.processed > 0`, the status line reads: "X emails processed, Y errors" in `text-slate-400 text-xs`. Errors here means individual AI failures on specific emails — those emails appear in the list with `triage_status = "triage_error"`. That error state on the row is out of scope for this slice.

---

## Issue 5 — Empty state (no new emails after triage)

**Scenario:** Run Triage completes. `processed === 0`. The pending list was already empty or unchanged.

**What the owner sees:**

- The status region shows: "No new emails found"
- The pending list is unchanged (empty state copy remains if there were no emails before)
- The button is re-enabled

No additional visual treatment is needed. "No new emails found" is unambiguous.

**Scenario:** First-ever run, no unread Gmail messages match the criteria, `processed === 0`.

The existing empty state copy ("No emails yet. Click Run Triage to start.") stays visible. After the run completes with 0 results, the status region shows "No new emails found" — this is sufficient. The empty state copy is not removed; it remains accurate.

---

## Issue 6 — Error state

**Scenario:** `runTriage()` throws (network failure, API error, AI service down entirely).

**Current behavior:** The catch block sets `error` to the error message string. An inline red banner renders above the pending section:

```jsx
<div className="mb-4 p-3 rounded-lg bg-red-900 border border-red-700 text-red-200 text-sm">
  {error}
</div>
```

**Decision: keep inline banner.** No toast. The banner is persistent — it does not auto-dismiss. The owner must be able to read the error message without time pressure.

**Additions to the current implementation:**

1. The status region (Issue 3) clears when an error is set — it shows nothing (not "Running triage...", not "No new emails found"). The error banner is the single source of truth for failure.
2. The error message shown in the banner should be human-readable. If the raw API error message is technical, Devon should map known error strings to readable copy. Minimum: wrap the raw message. Example copy: "Triage failed. Check your connection and try again."
3. The button returns to normal state immediately (re-runnable after failure).

**The status region condition when error exists:**

```jsx
<span role="status" aria-live="polite" aria-atomic="true" className="text-slate-400 text-xs">
  {runLoading && "Running triage..."}
  {!runLoading && !error && runResult && runResult.processed > 0 &&
    `${runResult.processed} email${runResult.processed === 1 ? "" : "s"} processed`}
  {!runLoading && !error && runResult && runResult.processed === 0 &&
    "No new emails found"}
  {/* error state: banner handles messaging — status region is silent */}
</span>
```

---

## Issue 7 — Disabled state

The button is disabled when `runLoading === true`. This prevents double-trigger.

**Disabled Tailwind classes (only the disability-relevant subset):**

```
disabled:opacity-50 disabled:cursor-not-allowed
```

Combined with `aria-busy={runLoading}`, this satisfies both visual and semantic disabled communication. The `disabled:cursor-not-allowed` class is missing from the current implementation and must be added.

No further visual treatment (e.g., different background color) is needed for the disabled state. The spinner inside the button already communicates the reason for the disabled state.

---

## Issue 8 — Accessibility

**Button ARIA:**

```jsx
<button
  aria-busy={runLoading}
  disabled={runLoading}
  ...
>
```

`aria-busy` communicates to assistive technology that the widget is updating. Combined with `disabled`, screen readers announce the button as "Run Triage, dimmed" or "unavailable" in the idle state, and "busy" when triage is running.

**Status region (aria-live):**

The `<span role="status" aria-live="polite" aria-atomic="true">` from Issue 3 is the single live region for all triage state transitions. `aria-live="polite"` waits for the current utterance to finish before announcing the change — appropriate here since no change is urgent. `aria-atomic="true"` ensures the full text content is re-announced on any change, not just the changed portion.

**Spinner SVG:**

```jsx
<svg aria-hidden="true" ...>
```

The spinner is decorative. `aria-hidden="true"` prevents screen readers from announcing the SVG path data.

**Button label change ("Running..."):**

The button label change from "Run Triage" to "Running..." is announced by screen readers because the button is in the accessibility tree and its text content changes. No additional `aria-label` override is needed. This is correct and consistent.

**Focus ring:**

The focus ring specification in Issue 1 (`focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400`) is consistent with the pattern established in Quinn-interaction-spec-full-review.md Issues 5 and 6.

---

## Issue 9 — Token consistency

All tokens used in this spec are already present in existing components. No new color families introduced.

| Token | Used for | Source |
|---|---|---|
| `bg-slate-700` | Button background | InboxRow, existing button |
| `hover:bg-slate-600` | Button hover | existing button |
| `text-slate-100` | Button label | existing button |
| `text-slate-300` | Spinner icon color | Decline button hover (prior spec) |
| `text-slate-400` | Status region text | Section headings, Back link |
| `disabled:opacity-50` | Button disabled | existing button |
| `animate-spin` | Spinner | Tailwind core utility, no new color |
| `bg-red-900 border-red-700 text-red-200` | Error banner | existing error div |
| `focus-visible:ring-slate-400` | Focus ring | All interactive elements (prior spec) |

---

## Implementation Summary

| # | Location | Current state | Required change |
|---|---|---|---|
| 1 | Button — normal state | Missing focus ring, missing `disabled:cursor-not-allowed` | Add `focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400 disabled:cursor-not-allowed`; add `inline-flex items-center gap-2` to accommodate spinner |
| 2 | Button — loading state | Label changes to "Running...", no spinner | Add spinner SVG (`animate-spin`, `aria-hidden="true"`, `w-3.5 h-3.5 text-slate-300`) before label text when `runLoading` is true |
| 3 | Button — ARIA | No `aria-busy` | Add `aria-busy={runLoading}` |
| 4 | Status region | Current: inline `runResult` span with raw `processed / skipped / errors` values | Replace with `<span role="status" aria-live="polite" aria-atomic="true">` that shows: "Running triage..." during load, "X emails processed" on success, "No new emails found" on zero-result success, silent on error |
| 5 | Error handling | Error message is raw API error string | Wrap in human-readable copy: "Triage failed. Check your connection and try again." (or map known error strings); error banner clears status region |
| 6 | Button — disabled state | `disabled:opacity-50` only | Add `disabled:cursor-not-allowed` |
| 7 | Success feedback | List refreshes silently | No change to list rendering needed; count change in "Pending · N" header is the visual cue; status region provides text confirmation |
| 8 | Empty state | Existing copy "No emails yet. Click Run Triage to start." | No change to empty state copy; status region provides "No new emails found" after a zero-result run |

---

*Quinn — 2026-06-29*
