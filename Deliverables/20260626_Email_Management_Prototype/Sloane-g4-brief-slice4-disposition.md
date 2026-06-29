# G4 Brief — Email Management Slice 4: Disposition

**Author:** Sloane
**Date:** 2026-06-29
**Status:** Ready for Devon / Codex
**References:** pitch-v1.md (Slice 4), Quinn-interaction-spec-slice4-disposition.md

---

## 1. Vertical Slice Plan

**Slice 4 — Disposition and Processed section**

One slice. End-to-end and owner-verifiable in under 15 minutes.

**What it delivers:**
The owner can complete a full triage pass. After reviewing and resolving all action rows in an accordion, Archive and Delete buttons activate. Clicking either immediately moves the email to the top of the Processed section with a "✓ Processed" badge, decrements Pending count, increments Processed count, and appends a disposition log entry. The processed accordion shows Email Summary and the execution log with the disposition entry as the final visible line. On API failure the email returns to Pending with an error band.

**Files changed:**

| File | Change type |
|---|---|
| `EmailTriage.jsx` | Replace `emails` state with `pendingEmails` + `processedEmails` + `disposeErrors`; split initial load; add `handleDispose`; render two labelled sections; pass `onDispose` and `disposeError` to `InboxRow` |
| `ActionsPanel.jsx` | Add `onDispose` prop; add `allResolved` computation; add `handleArchive` and `handleDelete`; add Archive/Delete button row at bottom of JSX |
| `InboxRow.jsx` | Add `onDispose` and `disposeError` props; render error band; pass `onDispose` to `ActionsPanel` |
| `formatters.js` | Add `buildDispositionLogEntry(disposition, ts)` export |
| `ProcessedRow.jsx` | New component: muted row header with "✓ Processed" badge; accordion renders Email Summary + ProcessedPanel |
| `ProcessedPanel.jsx` | New component: read-only reversed execution log |
| `emailTriage.js` (API client) | Add `disposeEmail(emailId, disposition)` method |

**Preconditions:**
- Slice 3 is live: ActionsPanel, ActionRowV3, buildLogEntry, emailSessions state all exist.
- Backend endpoint exists. Confirm the exact path with Kai before building: Quinn's spec says `/api/email-management/emails/${emailId}/dispose` — the task brief says `/api/email-management/emails/{id}/disposition`. These differ. Devon must not guess.

---

## 2. Gherkin Feature File

```gherkin
Feature: Email Disposition — Archive and Delete

  Background:
    Given the Email Triage page is loaded
    And there is at least one email in the Pending section

  # --- Disabled gate ---

  Scenario: Archive and Delete are disabled while any action row is unresolved
    Given an email accordion is open
    And the email has at least one action row in pending state
    Then the Archive button is disabled
    And the Delete button is disabled

  Scenario: Archive and Delete activate when all action rows are resolved
    Given an email accordion is open
    And all action rows have been either approved or declined
    Then the Archive button is enabled
    And the Delete button is enabled

  Scenario: Archive and Delete are immediately active when the email has no action rows
    Given an email accordion is open
    And the email has no action rows
    Then the Archive button is enabled
    And the Delete button is enabled

  # --- Archive happy path ---

  Scenario: Archive moves the email to the top of the Processed section immediately
    Given an email accordion is open
    And all action rows are resolved
    When the owner clicks Archive
    Then the email is no longer in the Pending section
    And the Pending count decrements by one
    And the email appears at the top of the Processed section
    And the email shows a "✓ Processed" badge
    And the Processed count increments by one

  Scenario: Archive appends a disposition log entry to the execution log
    Given an email accordion is open
    And all action rows are resolved
    When the owner clicks Archive
    And the owner opens the processed row accordion
    Then the execution log shows "Email archived" as the final line

  # --- Delete happy path ---

  Scenario: Delete moves the email to the top of the Processed section immediately
    Given an email accordion is open
    And all action rows are resolved
    When the owner clicks Delete
    Then the email is no longer in the Pending section
    And the Pending count decrements by one
    And the email appears at the top of the Processed section
    And the email shows a "✓ Processed" badge
    And the Processed count increments by one

  Scenario: Delete appends a disposition log entry to the execution log
    Given an email accordion is open
    And all action rows are resolved
    When the owner clicks Delete
    And the owner opens the processed row accordion
    Then the execution log shows "Email deleted" as the final line

  # --- Processed section rendering ---

  Scenario: Processed accordion shows Email Summary and full execution log in read-only state
    Given an email has been processed
    When the owner opens the processed row accordion
    Then the Email Summary is visible
    And the execution log is visible
    And the action entries appear before the disposition entry
    And no action buttons are visible
    And no disposition buttons are visible

  Scenario: Execution log in processed accordion shows disposition as the final visible line
    Given an email was processed after one action was approved
    When the owner opens the processed row accordion
    Then the approved action entry appears first
    And the disposition entry is the last line in the log

  Scenario: Execution log is only visible in the processed accordion when no actions were approved before disposition
    Given an email with no action rows has been archived
    When the owner opens the processed row accordion
    Then the execution log shows exactly one entry
    And that entry is "Email archived"

  Scenario: Most recently processed email appears at the top of the Processed section
    Given two emails have been processed in sequence
    When the owner views the Processed section
    Then the most recently processed email is at the top

  # --- Error state ---

  Scenario: Disposition failure returns the email to Pending and shows an error band
    Given an email accordion is open
    And all action rows are resolved
    And the disposition API will return an error
    When the owner clicks Archive
    Then the email returns to the Pending section
    And an error message is visible on the email row
    And the Processed section does not contain the email
    And the disposition log entry is not present in the email session

  Scenario: Error band clears on successful retry
    Given an email row shows a disposition error
    And the disposition API is now available
    When the owner clicks Archive again
    Then the error message is no longer visible on the row
    And the email moves to the Processed section
```

---

## 3. Test Spec

### Automated

| Scenario | Type | Notes |
|---|---|---|
| `allResolved` with `actions === null` returns false | Unit | Prevents buttons activating during load |
| `allResolved` with empty array returns true | Unit | Vacuous case — no rows means immediately active |
| `allResolved` with all rows approved or declined returns true | Unit | Happy gate |
| `allResolved` with one row in pending state returns false | Unit | Gate holds |
| `buildDispositionLogEntry("archive", date)` returns correct string | Unit | Format: "DD Mon YYYY HH:MM  Email archived" |
| `buildDispositionLogEntry("delete", date)` returns correct string | Unit | Format: "DD Mon YYYY HH:MM  Email deleted" |
| Archive button has HTML `disabled` attribute when `allResolved` is false | Component | Not CSS-only; use `getByRole("button", { name: "Archive email" })` |
| Delete button has HTML `disabled` attribute when `allResolved` is false | Component | Same pattern |
| `handleDispose` moves email from `pendingEmails` to front of `processedEmails` | Integration | State-level assertion |
| `handleDispose` rollback: email returns to `pendingEmails` on API rejection | Integration | Includes log entry cleanup |
| `disposeErrors[emailId]` is set on failure and cleared on next click | Integration | Error band state |
| Processed section renders "✓ Processed" badge on processed email | Component | Renders `ProcessedRow` with badge text |
| `ProcessedPanel` renders log entries in reverse order | Unit | Oldest first, disposition entry last |
| `ProcessedPanel` renders "No actions recorded." when log is empty | Unit | Empty state |

### Manual

| Scenario | Reason automated is insufficient |
|---|---|
| Full triage pass: open accordion, resolve actions, Archive activates, click Archive, email processes | Requires visual confirmation of immediate move and count update |
| Delete button visual distinction — red tokens visible in browser | Color rendering not covered by unit tests |
| Processed row muted styling (sender name visually lighter) | Visual regression |
| Error band renders at row level, not as a page-level banner | Layout position requires visual check |
| Error recovery: error band disappears on successful retry | Sequence of interactions |
| Processed accordion log reversed correctly: disposition appears as final line | Log order requires visual confirmation |
| Screen reader announcement on Processed count update (`aria-live`) | Requires assistive technology or browser audit |
| Disposition log entry timestamp format matches existing log entries | Format consistency is visual |

---

## 4. Acceptance Criteria

**Slice 4 is done when all of the following are true:**

1. Archive and Delete buttons render at the bottom of `ActionsPanel`, below the execution log when it exists and below `+ Task` / `+ Event` when no log entries exist yet.
2. Both buttons have the HTML `disabled` attribute while any action row for that email is in pending state. CSS-only approaches are not accepted.
3. With no action rows present, both buttons are active immediately on accordion open.
4. Clicking Archive or Delete moves the email to the top of the Processed section in the same render cycle. No loading state is shown on the buttons.
5. The Pending count decrements and the Processed count increments on disposition.
6. The Processed count update is wrapped in an `aria-live="polite"` region.
7. A disposition log entry is prepended to the email session log. Format: `"DD Mon YYYY HH:MM  Email archived"` or `"DD Mon YYYY HH:MM  Email deleted"`.
8. The processed row shows a "✓ Processed" badge and muted sender name styling. The row toggles an accordion that shows Email Summary (when present) and the execution log read-only.
9. The processed accordion renders log entries reversed so the disposition entry is the final visible line.
10. If the owner dispositioned without approving any actions, the execution log contains only the disposition entry — visible exclusively in the processed accordion.
11. On API failure: the email is removed from Processed and re-appended to Pending, the disposition log entry is removed from the session, and an error band appears at the row level using existing red tokens. The accordion is not automatically re-opened.
12. The error band clears when the owner clicks Archive or Delete again and the call succeeds.
13. The `emailTriage.js` API client has a `disposeEmail(emailId, disposition)` method posting to the confirmed endpoint path. Devon must confirm this path with Kai before building.

---

## 5. Handoff Notes for Devon

**State refactor is the largest change.** `EmailTriage.jsx` currently holds a single `emails` array. This must become three separate state values: `pendingEmails`, `processedEmails`, `disposeErrors`. Quinn's spec Issue 8 contains the exact useState declarations, initial load split, and `handleDispose` function including rollback logic. Use it as the implementation reference.

**Confirm the API endpoint path before writing a single line of client code.** The task brief says `/api/email-management/emails/{id}/disposition`. Quinn's spec says `/api/email-management/emails/${emailId}/dispose`. These differ. Ask Kai which is live before adding `disposeEmail` to the client.

**New components go in `src/components/EmailTriage/`.** Two new files: `ProcessedRow.jsx` and `ProcessedPanel.jsx`. Quinn's spec Issues 9 and 10 contain the full JSX for both. Do not put them elsewhere.

**`buildDispositionLogEntry` goes in `formatters.js`** alongside the existing `buildLogEntry` export. Quinn's spec Issue 6 has the exact function signature and implementation.

**Prop threading.** `onDispose` and `disposeError` are new props on `InboxRow`. `InboxRow` passes `onDispose` down to `ActionsPanel`. The error band renders in `InboxRow` below the row header div, not inside `ActionsPanel`. Quinn's spec Issue 8 has the exact JSX for both.

**Rollback behavior is intentionally simplified.** On error, the email re-appends to the end of `pendingEmails`, not its original position. This is accepted per spec. Do not attempt to preserve original index.

**Empty pending state.** When all emails are processed and `pendingEmails.length === 0`, whether to show "PENDING · 0" or hide the header is Devon's call. Either is acceptable.

**No loading state on Archive/Delete buttons.** The optimistic update completes in one synchronous React render cycle. The buttons are unmounted before any async gap. Do not add a loading spinner to them.

**`email.summary` in InboxRow pending accordion.** Quinn's spec Issue 10 notes that if Email Summary is not currently shown in the InboxRow accordion panel (above ActionsPanel), Devon should add it in the same pass using the pattern `email.summary && ...`. Check `InboxRow.jsx` — it currently renders only `ActionsPanel` inside the accordion panel. Add the summary block above `ActionsPanel` if it is absent.

---

*Sloane — 2026-06-29*
