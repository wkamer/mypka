# Email Triage — G4 Delivery Brief

**Feature:** Email Management System (Inbox Zero)
**Product brief:** v0.2 — 2026-06-25
**Author:** Sloane
**Date:** 2026-06-25
**Implementer:** Devon
**Status:** Ready — Devon fixes the existing code from this document without asking Sloane for clarification

---

## Architectural decision (SSOT — owner confirmed 2026-06-25)

Gmail is the single source of truth for email content. The DB stores triage state only.

| Stored where | What |
|---|---|
| Gmail (live) | sender, subject, body, received_at, thread_id — all email content |
| SQLite DB | email_id (Gmail message ID as FK), classification, ai_summary, triage_status, actions |

The dashboard fetches emails live from Gmail on every page load. The DB is joined in-memory to add triage state. Email content is never written to the DB.

**Devon's existing implementation violated this rule.** The `emails` table stores subject, sender, body_text, snippet, received_at, thread_id. This must be corrected. Fix the existing code — do not rebuild from scratch.

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

Three slices. S1 corrects the backend. S2 builds the email list. S3 builds the accordion with triage display.

| Slice | Delivers | ACs covered |
|---|---|---|
| S1 | Backend SSOT fix — DB schema corrected, live Gmail endpoint, run endpoint stores triage state only | Backend only |
| S2 | Two-line inbox list on the dashboard page | AC-1, AC-2, AC-3, AC-4, AC-5 |
| S3 | Accordion with triage classification and action approve/decline | AC-6, AC-7, AC-8, AC-9, AC-11, AC-12, AC-13 |

Build in order. S2 depends on the S1 endpoint. S3 adds interactivity on top of S2. Stop after each slice.

**Note on AC-10:** Product brief v0.2 AC-10 states the accordion panel is empty in MVP. This is superseded by the owner's architectural decision (2026-06-25): the accordion shows triage classification and action approve/decline buttons. AC-10 is replaced by AC-12 and AC-13 in this brief.

---

## Slice 1 — Backend SSOT fix

### Owner verification (target: under 10 minutes)

Navigate to `https://raspberrypi.local/api/email-triage/emails` while logged in. The browser returns a JSON array of live Gmail inbox emails. Each object contains: `id`, `sender` (display name or raw address), `subject`, `received_at` (ISO 8601), `classification` (null if not yet triaged), `triage_status` (null if not yet triaged), `ai_summary` (null if not yet triaged). List is ordered newest first. No stale DB content. That confirms S1 is done.

### What Devon fixes

**`backend/email_triage.py` — modify existing.**

#### Fix 1 — DB schema migration

The `emails` table currently stores email content. Strip it to triage state only.

New `emails` schema (replace the existing CREATE TABLE):

```sql
CREATE TABLE IF NOT EXISTS emails (
    id             TEXT PRIMARY KEY,
    classification TEXT,
    ai_summary     TEXT,
    triage_status  TEXT NOT NULL DEFAULT 'pending',
    created_at     TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at     TEXT NOT NULL DEFAULT (datetime('now'))
)
```

The `actions` table schema is correct — keep it unchanged.

Add a `_migrate_db()` function that runs before `_init_db()`:

```python
def _migrate_db() -> None:
    """Drop old bloated emails table if it contains content columns (SSOT violation)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    cols = [row[1] for row in c.execute("PRAGMA table_info(emails)").fetchall()]
    if "body_text" in cols or "subject" in cols:
        # Old schema violates SSOT — drop and recreate. Data loss is intentional.
        c.execute("DROP TABLE IF EXISTS emails")
        conn.commit()
    conn.close()
```

Call order at module level:
```python
_migrate_db()
_init_db()
```

#### Fix 2 — `GET /api/email-triage/emails` returns live Gmail + triage state

Replace the existing `get_emails` function body entirely. Remove the DB SELECT. Replace with:

1. Fetch Gmail inbox: `service.users().messages().list(userId="me", labelIds=["INBOX"], maxResults=30).execute()`
2. For each message ref: call `.get(userId="me", id=msg_id, format="metadata", metadataHeaders=["From","Subject","Date"])` to get headers only (faster than full format for the list view)
3. Extract sender: parse `From` header. If format is `Name <address>`, use `Name`. If bare address, use the address.
4. Extract subject from `Subject` header. Extract received_at from `internalDate` (milliseconds to UTC ISO 8601).
5. Load triage state from DB in one query: `SELECT id, classification, ai_summary, triage_status FROM emails WHERE id IN (?, ?, ...)` using the message IDs. Build a dict keyed by id.
6. Merge: for each Gmail message, attach triage state from the dict (or null fields if not yet triaged).
7. Sort by received_at descending.
8. Return list of objects: `{id, sender, subject, received_at, classification, ai_summary, triage_status}`.

Return shape:
```json
{
  "emails": [
    {
      "id": "gmail_message_id",
      "sender": "Alice Example",
      "subject": "Invoice #123",
      "received_at": "2026-06-25T10:30:00+00:00",
      "classification": "Action",
      "ai_summary": "Invoice from supplier...",
      "triage_status": "pending"
    }
  ]
}
```

#### Fix 3 — `POST /api/email-triage/run` stores only triage state

The run endpoint currently inserts subject, sender, body_text, snippet, received_at, thread_id into the DB. Remove those inserts.

Fix the INSERT in the run loop:

```python
conn.execute(
    """INSERT INTO emails
       (id, classification, ai_summary, triage_status, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?)
       ON CONFLICT(id) DO UPDATE SET
           classification = excluded.classification,
           ai_summary = excluded.ai_summary,
           triage_status = excluded.triage_status,
           updated_at = excluded.updated_at""",
    (msg_id, classification, ai_summary, triage_status, now, now),
)
```

Body text still flows in-memory from Gmail to the AI call — it is never written to DB. Remove the `body_text` column from the run INSERT entirely.

The `skip` logic (`SELECT id FROM emails WHERE id = ?`) still works — a previously triaged email will be found in the DB by id and skipped.

#### Fix 4 — `PATCH /api/email-triage/emails/{email_id}` return value

The existing PATCH returns subject/sender/snippet from the DB query. Those columns no longer exist. Fix the return SELECT:

```python
updated = conn.execute(
    "SELECT id, classification, ai_summary, triage_status, updated_at FROM emails WHERE id = ?",
    (email_id,),
).fetchone()
return dict(updated)
```

No other changes needed in patch_email.

#### No changes needed

- `get_actions` — actions table is correct, no changes
- `patch_action` — action execution helpers are correct, no changes
- `execute_todoist_action`, `execute_calendar_action`, `execute_archive_action` — correct, no changes
- `_call_ai` — correct, no changes
- `_extract_body` — still needed for the run endpoint AI call, no changes

### Stop point — S1

After S1: run tests, verify endpoint in browser returns live Gmail data, report to owner. Do not start S2 until owner confirms.

---

## Slice 2 — Two-line inbox list

### Owner verification (target: under 15 minutes)

Open the dashboard. Navigate to Email Triage. Check:
- Each email is two lines: line 1 = sender name (or address), line 2 = subject with date/time on the right
- List is sorted newest first
- No horizontal scrollbar on a standard desktop browser window
- When a display name is available it appears on line 1, not the raw address

### What Devon builds

**`frontend/src/pages/EmailTriage.jsx` — create new.**

- On page load: call `GET /api/email-triage/emails`. Show loading spinner during fetch.
- Render results as a scrollable list. One row per email.
- Row structure (exactly two visible lines):
  - Line 1: sender (from `sender` field)
  - Line 2: subject (left-aligned) + received date/time formatted as `DD-MM HH:mm` (right-aligned)
- No click handler yet — that is S3.
- Empty state (API returns empty array): display "No emails in inbox."
- Error state (fetch fails): display "Could not load emails."
- Layout must not produce horizontal scroll on a standard desktop viewport (1280px+ width).

**`frontend/src/App.jsx` — add route only:**
```jsx
import EmailTriage from "./pages/EmailTriage";
// Inside AuthGate <Routes>:
<Route path="/email-triage" element={user ? <EmailTriage /> : <Navigate to="/login" replace />} />
```

**`frontend/src/api/client.js` — add `get` method if missing.** Follow the existing `request()` pattern. Do not remove or modify existing methods.

Page layout and styling: follow the pattern of existing pages (see `KeyElements.jsx`). Match existing font, spacing, and color conventions exactly.

### Stop point — S2

After S2: run tests, verify list renders correctly in the browser, report to owner. Do not start S3 until owner confirms.

---

## Slice 3 — Accordion with triage info and action buttons

### Owner verification (target: under 15 minutes)

On the email list page:
1. Click an email row — an accordion panel opens below it
2. Click the same row again — the panel closes
3. Click a second email row while one is open — the first closes and the second opens
4. The open panel is visually distinct from the list rows (indented or bordered)
5. If the email has been triaged: classification and ai_summary are visible in the panel
6. If the email has actions: each action card shows description, suggested title, and Approve / Decline buttons
7. All of the above happen without any page reload

### What Devon builds

**`EmailTriage.jsx` — modify existing:**

- Add click handler to each email row.
- Track expanded row in component state: store the `id` of the open row or `null`.
- Clicking a collapsed row: set it as open (closes any previously open row — state holds one ID).
- Clicking the open row: set state to `null` (collapse).
- Render accordion panel directly below the clicked row, inside the list — not at the bottom.
- Panel visual treatment: border or indentation that distinguishes it from list rows. Match existing design system.

Panel content when email has `classification` set (triaged):
- Show classification as a badge or label ("Information" or "Action")
- Show ai_summary as a short text block
- For each action (fetched from `GET /api/email-triage/emails/{email_id}/actions`): render an action card with:
  - `description` (main label)
  - `suggested_title` (sub-label)
  - `due_date` if present
  - Approve button and Decline button
  - On Approve: call `PATCH /api/email-triage/actions/{action_id}` with `{"status": "approved"}`
  - On Decline: call `PATCH /api/email-triage/actions/{action_id}` with `{"status": "declined"}`
  - After response: update local state to reflect new action status (executed / declined / failed)
  - Disable buttons after action is taken

Panel content when email has `classification = null` (not yet triaged):
- Show "Not yet triaged" label. No buttons.

Panel content when `triage_status = "triage_error"`:
- Show "Triage failed" label. No buttons.

Fetch actions lazily: call `GET /api/email-triage/emails/{email_id}/actions` when the row is first expanded (not on initial page load). Cache the result in component state to avoid re-fetching on re-expand.

No backend changes in S3.

### Stop point — S3

After S3: run tests, verify all accordion and action behaviors in the browser, report to owner. S3 completes the build. Route back to Sloane if any AC is not met.

---

## Gherkin Feature File

```gherkin
Feature: Email Triage inbox list and accordion

  # ── SLICE 1: Backend SSOT fix ──

  Scenario: Authenticated user fetches inbox emails live from Gmail
    Given the user is authenticated
    When the user requests GET /api/email-triage/emails
    Then the response is 200
    And the response body contains an "emails" array
    And each item contains id, sender, subject, received_at
    And items are ordered newest first by received_at

  Scenario: Triage state is merged into live Gmail response
    Given the user is authenticated
    And email "abc123" has been triaged with classification "Action"
    When the user requests GET /api/email-triage/emails
    Then the item with id "abc123" includes classification "Action"

  Scenario: Untriaged email has null classification in response
    Given the user is authenticated
    And email "xyz789" has not been triaged
    When the user requests GET /api/email-triage/emails
    Then the item with id "xyz789" has classification null

  Scenario: Sender with display name returns name not address
    Given the Gmail inbox contains an email with From "Alice Example <alice@example.com>"
    When the user requests GET /api/email-triage/emails
    Then the sender field for that email is "Alice Example"

  Scenario: Sender without display name returns raw address
    Given the Gmail inbox contains an email with From "bob@example.com"
    When the user requests GET /api/email-triage/emails
    Then the sender field for that email is "bob@example.com"

  Scenario: Run triage stores only triage state in DB
    Given the user is authenticated
    When the user calls POST /api/email-triage/run
    Then the emails table contains only id, classification, ai_summary, triage_status
    And the emails table does not contain subject, sender, body_text, or received_at

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
    And the browser viewport is at standard desktop width (1280px or wider)
    Then no horizontal scrollbar is visible

  Scenario: Sender name is preferred over raw address (AC-5)
    Given the user is authenticated and on the Email Triage page
    And the inbox contains an email with a display name in the From field
    Then line 1 shows the display name, not the raw email address

  Scenario: Empty inbox shows empty state message
    Given the user is authenticated and on the Email Triage page
    And the Gmail inbox has no messages
    Then the page shows "No emails in inbox."

  # ── SLICE 3: Accordion with triage info and action buttons ──

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

  Scenario: Accordion works without page reload (AC-11)
    Given the user is authenticated and on the Email Triage page
    When the user expands and collapses accordion panels
    Then no page reload occurs
    And the URL does not change

  Scenario: Triaged email shows classification and summary in accordion (AC-12)
    Given the user is authenticated and on the Email Triage page
    And an email has been triaged with classification "Action" and a summary
    When the user clicks that email row
    Then the accordion panel shows the classification label
    And the accordion panel shows the ai_summary text

  Scenario: Action card renders with approve and decline buttons (AC-13)
    Given the user is authenticated and on the Email Triage page
    And a triaged email has one or more actions
    When the user expands the accordion for that email
    Then each action is shown as a card with Approve and Decline buttons
    And clicking Approve calls PATCH /api/email-triage/actions/{action_id} with status "approved"
    And clicking Decline calls PATCH /api/email-triage/actions/{action_id} with status "declined"
    And the buttons are disabled after the action is taken
```

---

## Test Spec

Devon writes failing tests first. Implementation follows to make them pass. This scope is the contract — Devon does not define their own test scope.

### Slice 1 — Automated tests

**Backend (pytest, `backend/test_email_triage.py` — create new if not exists):**

| Test | What to verify |
|---|---|
| `test_get_emails_requires_auth` | GET /api/email-triage/emails without cookie returns 401 |
| `test_get_emails_returns_live_list` | With mocked Gmail returning 3 messages, response is 200 and "emails" array has 3 items |
| `test_get_emails_fields_present` | Each item contains id, sender, subject, received_at |
| `test_get_emails_ordered_newest_first` | Items are ordered by received_at descending |
| `test_get_emails_merges_triage_state` | DB has triage row for msg_id "abc": response item for "abc" includes classification |
| `test_get_emails_null_triage_for_untriaged` | DB has no row for msg_id "xyz": response item for "xyz" has classification null |
| `test_get_emails_sender_display_name` | From "Alice <alice@example.com>" produces sender "Alice" |
| `test_get_emails_sender_fallback` | From "bob@example.com" produces sender "bob@example.com" |
| `test_run_does_not_store_content` | After POST /run with mocked Gmail and AI: emails table row for processed msg_id has no subject column |
| `test_db_migration_drops_old_schema` | DB with old body_text column: after _migrate_db() and _init_db(), table has no body_text column |

### Slice 2 — Automated tests

**Frontend (pytest-playwright or equivalent):**

| Test | What to verify |
|---|---|
| `test_email_list_renders_two_lines_per_row` | Each list row contains exactly two visible text lines (AC-1) |
| `test_email_list_line2_contains_date` | Line 2 of each row includes a date or time string (AC-2) |
| `test_email_list_sorted_newest_first` | With mocked API returning emails at t1 < t2, t2 appears before t1 in the DOM (AC-3) |
| `test_email_list_no_horizontal_overflow` | At 1280px viewport, no element has scrollWidth > clientWidth at document level (AC-4) |
| `test_email_list_sender_name_preferred` | When sender has display name, line 1 shows the name not the address (AC-5) |
| `test_email_list_empty_state` | With mocked API returning empty array, page shows "No emails in inbox." |

**Manual verification for S2:** Open dashboard, navigate to Email Triage, confirm list renders as two-line rows with date visible and newest email first.

### Slice 3 — Automated tests

**Frontend (pytest-playwright or equivalent):**

| Test | What to verify |
|---|---|
| `test_accordion_click_opens_panel` | Clicking a collapsed row makes an accordion panel appear below it (AC-6) |
| `test_accordion_click_again_closes_panel` | Clicking the expanded row removes the panel from the DOM (AC-7) |
| `test_accordion_second_click_closes_first` | With row A open, clicking row B closes row A and opens row B (AC-8) |
| `test_accordion_panel_has_distinct_style` | Expanded panel has a CSS class, border, or indentation attribute (AC-9) |
| `test_accordion_no_page_reload` | Accordion interactions do not trigger navigation events (AC-11) |
| `test_accordion_shows_classification` | Triaged email panel shows classification text (AC-12) |
| `test_accordion_action_buttons_present` | Panel for email with actions shows Approve and Decline buttons (AC-13) |
| `test_accordion_approve_calls_api` | Clicking Approve sends PATCH with status "approved" (AC-13) |
| `test_accordion_buttons_disabled_after_action` | Approve/Decline buttons are disabled after one is clicked (AC-13) |

**Manual verification for S3:** Click through all accordion behaviors. Approve one action, confirm it executes (Todoist task or Calendar event created). Decline one action, confirm status shows declined.

### Regression suite (all slices)

After fixing the router, verify these existing endpoints remain unaffected:

| Endpoint | Expected |
|---|---|
| POST /api/login | Returns 200 with valid credentials |
| GET /api/me | Returns username with valid cookie |
| POST /api/logout | Clears cookie |
| GET /api/projects | Returns personal and business project lists |
| GET /api/key-elements | Returns key element list |
| GET /api/key-elements/{slug} | Returns key element content |
| GET /api/topics | Returns topic list |
| GET /api/topics/{slug} | Returns topic content |

---

## File Reference

| File | Action |
|---|---|
| `/opt/myPKA/apps/dashboard/backend/email_triage.py` | Modify existing — fix DB schema, fix 3 endpoints |
| `/opt/myPKA/apps/dashboard/backend/test_email_triage.py` | Create new |
| `/opt/myPKA/apps/dashboard/frontend/src/pages/EmailTriage.jsx` | Create new |
| `/opt/myPKA/apps/dashboard/frontend/src/App.jsx` | Add /email-triage route (add only) |
| `/opt/myPKA/apps/dashboard/frontend/src/api/client.js` | Add get method if missing (add only) |

**No new dependencies. No Docker or Traefik changes. No new env vars.**

---

## Architecture constraints (Devon must not deviate)

- Gmail is the SSOT for email content. Never write subject, sender, body, snippet, received_at, or thread_id to the DB.
- Gmail API calls: use `get_credentials()` from `google_helper.py`. No new auth flows.
- `google_helper.py` import: always via `sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")`.
- Auth: `_require_auth(pka_token)` from `auth.py`. Cookie name: `pka_token`.
- DB path: `EMAIL_TRIAGE_DB` env var or `/opt/myPKA/apps/dashboard/email-triage.db`.
- No new ports, no Docker changes, no Traefik changes.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Initial brief — AI triage with approve/decline/execute (v0.1 scope) | Sloane |
| 2026-06-25 | Full rewrite — aligned to product brief v0.2 (inbox list + accordion, no AI, no DB); 3 smaller slices; feedback loop stop points added | Sloane |
| 2026-06-25 | Full rewrite — SSOT correction applied; Devon fixes existing code not rebuilds; Gmail is SSOT; DB stores triage state only; S1 is backend fix, S2 is frontend list, S3 is accordion with triage display; AC-10 superseded by AC-12 and AC-13 | Sloane |
