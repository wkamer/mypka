# Email Triage — G4 Delivery Brief

**Feature:** Email Management System (Inbox Zero)
**Product brief:** v0.2 — 2026-06-25
**Author:** Sloane
**Date:** 2026-06-25
**Implementer:** Devon
**Status:** Ready — Devon starts from this document without asking Sloane for clarification

---

## Feedback loop rule

Devon delivers one slice at a time. After completing a slice:

1. Run all tests for that slice — all must be green
2. Verify end-to-end in the running system
3. Report to owner with test results and verification confirmation
4. Stop — wait for owner feedback before starting the next slice

Do not start the next slice without explicit owner acknowledgment. Each slice is designed to be owner-verifiable in under 15 minutes.

---

## Slice Plan

Three vertical slices. Each is independently buildable and owner-verifiable.

| Slice | Delivers | ACs covered |
|---|---|---|
| S1 | Gmail inbox endpoint — owner can see raw email data from their inbox | Backend only |
| S2 | Two-line email list on the dashboard page | AC-1, AC-2, AC-3, AC-4, AC-5 |
| S3 | Accordion expand/collapse on email rows | AC-6, AC-7, AC-8, AC-9, AC-10, AC-11 |

Build in order. S2 depends on the S1 endpoint. S3 adds interactivity on top of S2. Stop after each slice.

---

## Slice 1 — Gmail inbox endpoint

### Owner verification (target: under 10 minutes)

Navigate to `https://raspberrypi.local/api/email-triage/emails` while logged in. The browser returns a JSON array of email objects. Each object contains: `id`, `sender`, `subject`, `received_at`. List is ordered newest first. That confirms S1 is done.

### What Devon builds

**Backend (`backend/email_triage.py` — create new):**

- `GET /api/email-triage/emails` — fetch the 30 most recent INBOX messages from Gmail using `get_credentials()` via `google_helper.py`. Return them as a JSON array ordered by `received_at` descending. Each item: `id` (Gmail message ID), `sender` (display name from From header if available, raw address as fallback), `subject`, `received_at` (ISO 8601 string).
- Use `_require_auth(pka_token)` from `auth.py` for auth. Cookie name: `pka_token`.
- Import `google_helper.py` via `sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")`.

**Mount in `backend/main.py`:**
```python
from email_triage import router as email_triage_router
app.include_router(email_triage_router)
```
Add after existing route definitions. Do not modify any existing route.

**No DB. No AI calls. No new env vars. No Docker or Traefik changes.**

### Stop point — S1

After S1: run tests, verify endpoint in browser, report to owner. Do not start S2 until owner confirms.

---

## Slice 2 — Two-line email list

### Owner verification (target: under 15 minutes)

Open the dashboard. Navigate to Email Triage. See the inbox email list. Check:
- Each email is two lines: line 1 = sender name, line 2 = subject with date on the right
- List is sorted newest first
- No horizontal scrollbar appears on a standard desktop browser window
- When sender name is not available, the raw email address appears on line 1

### What Devon builds

**Frontend (`frontend/src/pages/EmailTriage.jsx` — create new):**

- On page load: call `GET /api/email-triage/emails`. Show loading state during fetch.
- Render results as a scrollable list. One row per email.
- Row structure (exactly two visible lines):
  - Line 1: sender name (from `sender` field)
  - Line 2: subject (left-aligned) + received date/time (right-aligned or appended)
- No actions on the row (no buttons, no click handler yet — that is S3).
- Empty state (API returns empty array): display "No emails in inbox."
- Error state (fetch fails): display "Could not load emails."
- Layout must not produce horizontal scroll on a standard desktop viewport (1280px+ width).

**Register route in `frontend/src/App.jsx`:**
```jsx
import EmailTriage from "./pages/EmailTriage";
// inside AuthGate <Routes>:
<Route path="/email-triage" element={user ? <EmailTriage /> : <Navigate to="/login" replace />} />
```

**`frontend/src/api/client.js`:**
If `get` method does not already exist with the right signature, add it following the existing `request()` pattern. Do not remove or modify existing methods.

Page layout and styling: follow the pattern of existing pages (see `KeyElements.jsx`). Match existing font, spacing, and color conventions exactly.

### Stop point — S2

After S2: run tests, verify list renders correctly in the browser, report to owner. Do not start S3 until owner confirms.

---

## Slice 3 — Accordion expand/collapse

### Owner verification (target: under 15 minutes)

On the email list page:
1. Click an email row — an accordion panel opens below it (AC-6)
2. Click the same row again — the panel closes (AC-7)
3. Click a second email row while one is open — the first closes and the second opens (AC-8)
4. The open panel looks visually distinct from the list rows — indented or bordered (AC-9)
5. The panel content area is empty — no fields, no text (AC-10)
6. All of the above happen without any page reload (AC-11)

### What Devon builds

**Frontend (`EmailTriage.jsx` — modify existing):**

- Add click handler to each email row.
- Track which row is expanded in component state (store the email `id` of the open row, or `null` if none).
- Clicking a collapsed row: set it as the open row (closes any previously open row automatically — state holds only one ID at a time).
- Clicking the already-open row: set state to `null` (collapse).
- Render the accordion panel directly below the clicked row, inside the list — not at the bottom of the page.
- Panel content: empty `<div>` with a placeholder comment. No triage fields, no text.
- Panel visual treatment: add a border or indentation that distinguishes it from the list rows. Match existing design system spacing and color.
- Expand/collapse must not trigger a page reload or a new API call.

No backend changes in S3.

### Stop point — S3

After S3: run tests, verify all accordion behaviors in the browser, report to owner. S3 completes the MVP. Route back to Sloane if any AC is not met.

---

## Gherkin Feature File

```gherkin
Feature: Email Triage inbox list and accordion

  # ── SLICE 1: Gmail inbox endpoint ──

  Scenario: Authenticated user fetches inbox emails
    Given the user is authenticated
    When the user requests GET /api/email-triage/emails
    Then the response is 200
    And the response body is a JSON array
    And each item contains id, sender, subject, and received_at
    And items are ordered newest first by received_at

  Scenario: Sender with display name returns name not address
    Given the Gmail inbox contains an email with From "Alice Example <alice@example.com>"
    When the user requests GET /api/email-triage/emails
    Then the sender field for that email is "Alice Example"

  Scenario: Sender without display name returns raw address
    Given the Gmail inbox contains an email with From "bob@example.com"
    When the user requests GET /api/email-triage/emails
    Then the sender field for that email is "bob@example.com"

  Scenario: Unauthenticated request is rejected
    Given the user has no valid session cookie
    When the user requests GET /api/email-triage/emails
    Then the response status is 401

  # ── SLICE 2: Two-line email list ──

  Scenario: Email list renders with correct two-line structure (AC-1)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains at least one email
    Then each email row has exactly two lines
    And line 1 shows the sender name or address
    And line 2 shows the subject

  Scenario: Date is visible on line 2 alongside subject (AC-2)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains at least one email
    Then the received date or time is visible on line 2 of each row

  Scenario: List is sorted newest first (AC-3)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains emails received at different times
    Then the email with the most recent received_at appears first in the list

  Scenario: List renders without horizontal scroll on desktop (AC-4)
    Given the user is authenticated and on the Email Triage page
    And the browser viewport is at standard desktop width
    Then no horizontal scrollbar is visible

  Scenario: Sender name is preferred over raw address (AC-5)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains an email with a display name in the From field
    Then line 1 shows the display name, not the raw email address

  Scenario: Empty inbox shows empty state message
    Given the user is authenticated and on the Email Triage page
    And the Gmail inbox has no messages
    Then the page shows "No emails in inbox."

  # ── SLICE 3: Accordion expand/collapse ──

  Scenario: Clicking a collapsed row expands the accordion panel (AC-6)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains at least one email
    And all accordion panels are collapsed
    When the user clicks an email row
    Then an accordion panel appears directly below that row

  Scenario: Clicking an expanded row collapses the panel (AC-7)
    Given the user is authenticated and on the Email Triage page
    And one accordion panel is open
    When the user clicks the expanded row
    Then the accordion panel collapses

  Scenario: Opening a second accordion closes the first (AC-8)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains at least two emails
    And the first email row is expanded
    When the user clicks the second email row
    Then the second email accordion opens
    And the first email accordion closes

  Scenario: The expanded panel is visually distinct from the list rows (AC-9)
    Given the user is authenticated and on the Email Triage page
    And one accordion panel is open
    Then the panel has a visible border or indentation that distinguishes it from the list rows

  Scenario: The accordion panel content area is empty (AC-10)
    Given the user is authenticated and on the Email Triage page
    And one accordion panel is open
    Then the panel contains no text, fields, or buttons

  Scenario: Accordion works without page reload (AC-11)
    Given the user is authenticated and on the Email Triage page
    When the user expands and collapses accordion panels
    Then no page reload occurs
    And the URL does not change
```

---

## Test Spec

Devon writes failing tests first. Implementation follows to make them pass. This scope is the contract — Devon does not define their own test scope.

### Slice 1 — Automated tests

**Backend (pytest, `backend/test_email_triage.py` — create new):**

| Test | What to verify |
|---|---|
| `test_get_emails_requires_auth` | `GET /api/email-triage/emails` without cookie returns 401 |
| `test_get_emails_returns_list` | With mocked Gmail returning 3 messages, response is 200 and body is a list of 3 items |
| `test_get_emails_fields_present` | Each item in the list contains `id`, `sender`, `subject`, `received_at` |
| `test_get_emails_ordered_newest_first` | Items are ordered by `received_at` descending |
| `test_get_emails_sender_name_from_display_name` | Gmail message with `From: Alice <alice@example.com>` produces `sender = "Alice"` |
| `test_get_emails_sender_fallback_to_address` | Gmail message with `From: bob@example.com` produces `sender = "bob@example.com"` |
| `test_get_emails_empty_inbox` | With mocked Gmail returning 0 messages, response is 200 and body is `[]` |

**Frontend (manual verification for S1):**
Visit `https://raspberrypi.local/api/email-triage/emails` while logged in — browser shows JSON array with correct fields.

### Slice 2 — Automated tests

**Frontend (pytest-playwright or equivalent, append to test file):**

| Test | What to verify |
|---|---|
| `test_email_list_renders_two_lines_per_row` | Each list row contains exactly two visible text lines (AC-1) |
| `test_email_list_line2_contains_date` | Line 2 of each row includes a date or time string (AC-2) |
| `test_email_list_sorted_newest_first` | With mocked API returning emails at t1 < t2, t2 appears before t1 in the DOM (AC-3) |
| `test_email_list_no_horizontal_overflow` | At 1280px viewport, no element has `scrollWidth > clientWidth` at document level (AC-4) |
| `test_email_list_sender_name_preferred` | When sender has display name, line 1 shows the name not the address (AC-5) |
| `test_email_list_empty_state` | With mocked API returning `[]`, page shows "No emails in inbox." |

**Manual verification for S2:** Open dashboard, navigate to Email Triage, confirm list renders as two-line rows with date visible and newest email first.

### Slice 3 — Automated tests

**Frontend (pytest-playwright or equivalent, append to test file):**

| Test | What to verify |
|---|---|
| `test_accordion_click_opens_panel` | Clicking a collapsed row makes an accordion panel appear below it (AC-6) |
| `test_accordion_click_again_closes_panel` | Clicking the expanded row removes the panel from the DOM (AC-7) |
| `test_accordion_second_click_closes_first` | With row A open, clicking row B closes row A and opens row B (AC-8) |
| `test_accordion_panel_has_distinct_style` | Expanded panel has a CSS class, border, or indentation attribute (AC-9) |
| `test_accordion_panel_content_is_empty` | Expanded panel contains no text content and no form elements (AC-10) |
| `test_accordion_no_page_reload` | Accordion interactions do not trigger navigation events (AC-11) |

**Manual verification for S3:** Click through all accordion behaviors listed in the owner verification section above.

### Regression suite (all slices)

After mounting the email_triage router, verify these existing endpoints remain unaffected:

| Endpoint | Expected |
|---|---|
| `POST /api/login` | Returns 200 with valid credentials |
| `GET /api/me` | Returns username with valid cookie |
| `POST /api/logout` | Clears cookie |
| `GET /api/projects` | Returns personal and business project lists |
| `GET /api/key-elements` | Returns key element list |
| `GET /api/key-elements/{slug}` | Returns key element content |
| `GET /api/topics` | Returns topic list |
| `GET /api/topics/{slug}` | Returns topic content |

---

## File Reference

| File | Action |
|---|---|
| `/opt/myPKA/apps/dashboard/backend/email_triage.py` | Create (new) |
| `/opt/myPKA/apps/dashboard/backend/test_email_triage.py` | Create (new) |
| `/opt/myPKA/apps/dashboard/backend/main.py` | Add `include_router` line (add only) |
| `/opt/myPKA/apps/dashboard/frontend/src/pages/EmailTriage.jsx` | Create (new) |
| `/opt/myPKA/apps/dashboard/frontend/src/App.jsx` | Add `/email-triage` route (add only) |
| `/opt/myPKA/apps/dashboard/frontend/src/api/client.js` | Add `get` method if missing (add only) |

**No DB. No AI subprocess calls. No new dependencies beyond what is already installed.**

---

## Architecture constraints (Devon must not deviate from these)

- Gmail API calls: use `get_credentials()` from `google_helper.py`. No new auth flows.
- `google_helper.py` import: always via `sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")`.
- Auth: `_require_auth(pka_token)` from `auth.py`. Cookie name: `pka_token`.
- No AI calls in this MVP.
- No DB in this MVP.
- No new ports, no Docker changes, no Traefik changes.
- No new env vars.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Initial brief — AI triage with approve/decline/execute (v0.1 scope) | Sloane |
| 2026-06-25 | Full rewrite — aligned to product brief v0.2 (inbox list + accordion, no AI, no DB); 3 smaller slices; feedback loop stop points added | Sloane |
