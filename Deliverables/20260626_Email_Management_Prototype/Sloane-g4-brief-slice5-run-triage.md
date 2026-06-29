# G4 Brief — Email Management Slice 5: Run Triage (live)

**Author:** Sloane
**Date:** 2026-06-29
**Trigger:** G4 gate — behaviour-first, test-first delivery contract
**Input:** Quinn-interaction-spec-slice5-run-triage.md, pitch-v1.md (Slice 5), routes.py
**Status:** Ready for Devon / Codex

---

## 1. Vertical Slice Plan

**Scope:** One slice. Frontend only. No backend changes required.

**What gets built:**

The Run Triage button already exists in `EmailTriage.jsx`. This slice completes the interaction contract end-to-end:

1. Wire the button click to `POST /api/email-management/run`.
2. During the call: disable the button, show a spinner + "Running..." label, render "Running triage..." in the `aria-live` status region.
3. On success: re-enable the button, call `GET /api/email-management/emails` to refresh the pending list, show "X emails processed" or "No new emails found" in the status region.
4. On error: re-enable the button, show the persistent inline error banner, clear the status region.
5. Fix two missing button attributes that Quinn flagged: `disabled:cursor-not-allowed` and the focus ring.

**What does not change:**

- Backend: `POST /api/email-management/run` is used as-is. It returns `{processed, skipped, errors}`. No streaming. No per-email progress.
- The pending list rendering from Slices 1-4 is untouched.
- The `triage_error` row state (emails where AI failed individually) is out of scope for this slice.

**End state the owner can verify:**

Click Run Triage on an account with unread Gmail. Watch the spinner. When it stops, new email rows appear in the Pending section with AI-generated summaries and action suggestions already populated.

---

## 2. Gherkin Feature File

```gherkin
Feature: Run Triage — live email fetch and AI triage

  Background:
    Given the owner is authenticated on the Email Management page

  # --- Happy path ---

  Scenario: Run Triage fetches new emails and refreshes the pending list
    Given there are no emails in the pending list
    When the owner clicks "Run Triage"
    Then the button label changes to "Running..."
    And the button is disabled
    And the status region shows "Running triage..."
    When the triage call completes with 3 emails processed
    Then the button label returns to "Run Triage"
    And the button is enabled
    And the status region shows "3 emails processed"
    And the pending list shows 3 new email rows
    And the "Pending" section counter shows "PENDING · 3"

  Scenario: Pending count increments by the number of new emails found
    Given the pending list already contains 2 emails
    When the owner clicks "Run Triage"
    And the triage call completes with 2 emails processed
    Then the "Pending" section counter shows "PENDING · 4"
    And the 2 new email rows appear above the existing 2 rows

  # --- Loading / disabled state ---

  Scenario: Button cannot be triggered a second time while triage is running
    Given the owner has clicked "Run Triage" and the call is in progress
    When the owner clicks the button again
    Then the button does not submit a second request
    And the button remains disabled until the first call completes

  Scenario: Pending list remains visible and interactive during triage
    Given the pending list contains 1 email with an open accordion
    When the owner clicks "Run Triage"
    Then the accordion remains open and interactive during the call

  # --- Empty result ---

  Scenario: No new emails found after triage
    Given there are no unread Gmail messages matching the triage criteria
    When the owner clicks "Run Triage"
    And the triage call completes with 0 emails processed
    Then the status region shows "No new emails found"
    And the pending list is unchanged
    And the button is re-enabled

  Scenario: Empty state copy remains visible after a zero-result run
    Given the pending list is empty and shows "No emails yet. Click Run Triage to start."
    When the owner runs triage and 0 emails are processed
    Then the empty state copy remains visible
    And the status region shows "No new emails found"

  # --- Error state ---

  Scenario: Network failure during triage shows an error banner
    Given the triage API is unreachable
    When the owner clicks "Run Triage"
    And the call fails with a network error
    Then a persistent error banner appears above the pending section
    And the banner contains a human-readable message
    And the status region shows nothing
    And the button is re-enabled

  Scenario: API error during triage shows an error banner
    Given the triage API returns a 500 error
    When the owner clicks "Run Triage"
    Then a persistent error banner appears above the pending section
    And the button is re-enabled
    And the pending list is unchanged

  Scenario: Error banner from a previous run clears on the next successful run
    Given an error banner is visible from a previous failed triage run
    When the owner clicks "Run Triage"
    And the call completes successfully with 1 email processed
    Then the error banner is no longer visible
    And the status region shows "1 email processed"

  # --- New emails appear after success ---

  Scenario: New email rows are ordered by received date descending
    Given the pending list contains an email from 10 June
    When triage completes and returns 1 new email from 15 June
    Then the 15 June email appears above the 10 June email in the pending list

  Scenario: New email rows have AI summary and actions populated
    When triage completes and adds a new email
    Then the new email row shows the sender, subject, classification badge, and Gmail link
    And opening the accordion shows the AI-generated email summary
    And the Actions section contains the AI-suggested action rows
```

---

## 3. Test Spec

### Automated (component tests)

These scenarios can be driven by mocking `fetch` for `POST /api/email-management/run` and `GET /api/email-management/emails`.

| Scenario | Approach |
|---|---|
| Button disabled and label changes to "Running..." on click | Mock call that never resolves; assert button `disabled` and text content |
| Status region shows "Running triage..." during call | Assert `role="status"` element text during pending mock |
| Pending list refreshes after success | Mock `run` returning `{processed: 2}`, mock `emails` returning 2 rows; assert 2 rows rendered |
| Status region shows "X emails processed" on success | Assert `role="status"` text after mocked success |
| Status region shows "No new emails found" on zero result | Mock `processed: 0`; assert status text |
| Error banner appears on fetch failure | Mock rejected promise; assert banner present, button enabled |
| Error banner clears on subsequent success | Set initial error state; run success mock; assert banner gone |
| Button re-enabled after success | Assert button not `disabled` after mock resolves |
| Button re-enabled after error | Assert button not `disabled` after mock rejects |
| Second click during load does not submit second request | Assert `fetch` called exactly once during loading state |

### Manual (owner verification)

These require a live environment with real Gmail and the AI service running.

| Scenario | Why manual |
|---|---|
| Spinner animation visible and smooth during live run | CSS `animate-spin` not verifiable in jsdom |
| Real AI latency — owner can observe 5-10 second wait | No meaningful mock for duration |
| New email rows have real AI summary and real actions | Content correctness requires real AI call |
| Status region announced by screen reader | Requires assistive technology in a real browser |
| Focus ring visible on keyboard navigation to button | Requires real browser focus handling |

---

## 4. Acceptance Criteria

1. Clicking "Run Triage" calls `POST /api/email-management/run` exactly once per click.
2. The button is disabled from click until the call resolves or rejects.
3. While disabled, the button shows a spinner and the label "Running...".
4. A status region with `role="status"` and `aria-live="polite"` exists in the DOM at all times, not only during a run.
5. The status region shows "Running triage..." during the call, "X emails processed" on success, "No new emails found" on zero-result success, and nothing on error.
6. On success, `GET /api/email-management/emails` is called and the pending list re-renders with all current pending emails.
7. The Pending section counter reflects the updated email count.
8. On any error (network, API, AI service down), a persistent inline error banner appears. The banner does not auto-dismiss.
9. On error, the button returns to "Run Triage" and is re-enabled.
10. A successful run after a failed run clears the error banner.
11. The button carries `aria-busy={runLoading}` and `disabled` is set to the same boolean.
12. The button has a visible focus ring matching `focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-slate-900 focus-visible:ring-slate-400`.
13. The button carries `disabled:cursor-not-allowed` so the cursor changes over the disabled button.

---

## 5. Handoff Notes for Devon

**File to modify:** `apps/dashboard/frontend/src/components/EmailTriage.jsx` (or equivalent path — confirm location before edit).

**No backend changes required.** The `POST /api/email-management/run` endpoint is complete and returns `{processed, skipped, errors}`. Only `processed` is surfaced in the UI. `skipped` and `errors` are dropped from display.

**Backend gaps confirmed by Quinn — no action needed this slice:**

- **No streaming.** The endpoint is synchronous. Per-email progress ("Processing 3 of 8") is not possible without a backend streaming endpoint. That is explicitly out of scope. The spinner + "Running triage..." status line is the correct response.
- **`triage_error` row state.** The backend sets `triage_status = "triage_error"` when the AI call fails for a specific email. Those rows arrive in the email list via `GET /api/email-management/emails`. How to display a `triage_error` row in the accordion is out of scope for this slice.

**Two small backend observations (not blockers, log as TODO LOW):**

- The action rows inserted during triage (lines 106-124 in routes.py) are not asserted in the existing test `test_run_triage_inserts_emails` (noted in a TODO LOW comment at line 19). This does not affect Slice 5 delivery but should be closed before the feature ships.
- `GET /api/email-management/emails` returns emails `ORDER BY received_at DESC`. This is correct and matches the pitch spec (most recent first). No change needed.

**What changed relative to the current implementation (from Quinn's implementation summary):**

| # | What | Current | Required |
|---|---|---|---|
| 1 | Button classes | Missing focus ring and `disabled:cursor-not-allowed` | Add both |
| 2 | Button loading | Label changes, no spinner | Add SVG spinner (`aria-hidden`, `animate-spin`, `w-3.5 h-3.5`) |
| 3 | Button ARIA | No `aria-busy` | Add `aria-busy={runLoading}` |
| 4 | Status region | Raw `processed / skipped / errors` inline span | Replace with `<span role="status" aria-live="polite" aria-atomic="true">` |
| 5 | Error message | Raw API error string | Wrap in human-readable copy |

**Delegate all code writing to a `codex:codex-rescue` subagent (Agent tool, subagent_type: `codex:codex-rescue`). Read and plan using Claude-side tools, then spawn Codex with `--write` for the implementation. Do not write code yourself using Edit/Write/Bash.**

---

*Sloane — 2026-06-29*
