# G4 Brief — Email Management: Slice 3 (Actions panel and execution log)

**Feature:** Email Management
**Slice:** 3 — Actions panel and execution log
**Prepared by:** Sloane
**Date:** 2026-06-28
**For:** Devon

---

## 1. Slice definition

Slice 3 connects the accordion panel to live action data and enables the owner to review, edit,
approve, and decline AI-suggested task and event actions, and to add new ones manually. When an
accordion opens, the actions associated with that email are loaded from the backend. Each
AI-suggested action shows its type, an editable name pre-populated with the AI suggestion, and
for event actions an editable datetime pre-populated with the AI-extracted value. The datetime
field is always visible on event rows: this makes the AI extraction transparent to the owner.
The owner may edit either field before approving. On approval the action is executed in the
owner's external system, the controls collapse to a resolved state, and a timestamped entry is
appended to an in-panel execution log. Declining moves the row to a resolved declined state with
no log entry. Two manual-add controls are always present at the bottom of the actions block for
every email classification; each adds an empty row of the corresponding type. The execution log
is cumulative within the panel. Only one email row may be expanded at a time.

---

## 2. Gherkin feature file

```gherkin
Feature: Email Management — Actions panel and execution log

  Background:
    Given the owner is authenticated
    And at least one pending email is displayed in the email list


  # -------------------------------------------------------------------------
  # SCENARIO AREA 1 — Task approve
  # -------------------------------------------------------------------------

  Scenario: Approving a pending task action executes the task and appends a log entry
    Given the accordion for a pending email is open
    And the email has one task action in pending state
    When the owner approves the task action
    Then the action row transitions to a resolved approved state
    And the execution log shows a new entry that records the task name and a date-time timestamp

  Scenario: Approving a task action after editing the name logs the edited name
    Given the accordion for a pending email is open
    And the email has one task action in pending state
    When the owner modifies the name of the task action
    And the owner approves the task action
    Then the execution log entry records the name as entered rather than the original AI suggestion


  # -------------------------------------------------------------------------
  # SCENARIO AREA 2 — Event approve
  # -------------------------------------------------------------------------

  Scenario: Approving a pending event action creates the calendar event and appends a log entry
    Given the accordion for a pending email is open
    And the email has one event action with an AI-suggested name and an AI-extracted datetime
    When the owner approves the event action
    Then the action row transitions to a resolved approved state
    And the execution log shows a new entry that records the event name, the datetime, and a date-time timestamp

  Scenario: Approving an event action after editing name and datetime logs the edited values
    Given the accordion for a pending email is open
    And the email has one event action in pending state
    When the owner modifies the event name
    And the owner modifies the event datetime
    And the owner approves the event action
    Then the execution log entry records the name and datetime as entered at the time of approval


  # -------------------------------------------------------------------------
  # SCENARIO AREA 3 — Decline
  # -------------------------------------------------------------------------

  Scenario: Declining a pending action moves the row to a declined state without a log entry
    Given the accordion for a pending email is open
    And the email has one task action in pending state
    When the owner declines the action
    Then the action row transitions to a resolved declined state
    And no new entry is added to the execution log

  Scenario: Declining one action when another is already approved does not add a log entry for the declined action
    Given the accordion for a pending email is open
    And the email has one approved action with one log entry already present
    And the email has one additional action in pending state
    When the owner declines the pending action
    Then the execution log still contains exactly one entry
    And the declined action row is in a resolved declined state


  # -------------------------------------------------------------------------
  # SCENARIO AREA 4 — Manual add-task
  # -------------------------------------------------------------------------

  Scenario: Activating the manual add-task control appends an empty task row to the actions block
    Given the accordion for a pending email is open
    When the owner activates the add-task control
    Then a new pending task row appears below the existing action rows
    And the new row has an empty name field
    And the new row shows approve and decline controls

  Scenario: Approving a manually added task row logs the name entered by the owner
    Given the accordion for a pending email is open
    And the owner has activated add-task and entered a name in the new task row
    When the owner approves the manually added task action
    Then the execution log shows a new entry that records the entered name and a date-time timestamp


  # -------------------------------------------------------------------------
  # SCENARIO AREA 5 — Manual add-event
  # -------------------------------------------------------------------------

  Scenario: Activating the manual add-event control appends an empty event row with a datetime field
    Given the accordion for a pending email is open
    When the owner activates the add-event control
    Then a new pending event row appears below the existing action rows
    And the new row has an empty name field
    And the new row has an empty datetime field
    And the new row shows approve and decline controls

  Scenario: Approving a manually added event row logs the entered name and datetime
    Given the accordion for a pending email is open
    And the owner has activated add-event and entered a name and datetime in the new event row
    When the owner approves the manually added event action
    Then the execution log shows a new entry that records the event name, the entered datetime, and a date-time timestamp


  # -------------------------------------------------------------------------
  # SCENARIO AREA 6 — Editable fields
  # -------------------------------------------------------------------------

  Scenario: A task action name field is pre-populated with the AI suggestion and accepts input
    Given the accordion for a pending email is open
    And the email has one task action with an AI-suggested name
    Then the task action name field is pre-populated with the AI-suggested name
    And the owner can change the name before taking any action

  Scenario: An event action shows both name and datetime pre-populated from AI output and both fields accept input
    Given the accordion for a pending email is open
    And the email has one event action with an AI-suggested name and an AI-extracted datetime
    Then the event action name field is pre-populated with the AI suggestion
    And the event action datetime field is pre-populated with the AI-extracted value
    And both fields are visible and accept input before the owner approves or declines


  # -------------------------------------------------------------------------
  # SCENARIO AREA 7 — Execution log
  # -------------------------------------------------------------------------

  Scenario: The execution log accumulates entries as actions are approved
    Given the accordion for a pending email is open
    And the email has two pending actions
    When the owner approves the first action
    And the owner approves the second action
    Then the execution log contains two entries in the order the approvals occurred

  Scenario: The execution log is not shown before any action has been approved
    Given the accordion for a pending email is open
    And the email has only pending actions with no prior approvals
    Then no execution log section is visible in the panel


  # -------------------------------------------------------------------------
  # SCENARIO AREA 8 — Exclusive accordion toggle
  # -------------------------------------------------------------------------

  Scenario: Opening a second email row collapses the previously open row
    Given the accordion for a pending email is open
    When the owner opens the accordion for a different pending email
    Then the previously open accordion is collapsed
    And only the newly selected accordion is open

  Scenario: Clicking the header of the currently open row collapses that accordion
    Given the accordion for a pending email is open
    When the owner selects the header of the same email row a second time
    Then the accordion collapses
    And no other row becomes open as a result
```

---

## 3. Acceptance criteria

Derived directly from the Slice 3 definition in the G2 pitch. All criteria apply at slice level.

**AC-1 — Actions panel visibility**
The actions block is present inside the accordion for every pending email, regardless of whether
the email is classified as Action or Information.

**AC-2 — Task action row**
A task action row shows the action type ("Task") and an editable name field pre-populated with
the AI-suggested title.

**AC-3 — Event action row**
An event action row shows the action type ("Event"), an editable name field pre-populated with
the AI suggestion, and an editable datetime field pre-populated with the AI-extracted value. The
datetime field is always visible: it is not hidden behind a toggle or collapsed state.

**AC-4 — Approve: task**
Approving a task action:
- sends the approval to the backend via PATCH
- transitions the action row to a resolved approved state (controls no longer interactive)
- appends a log entry in the form `Task [name] created` followed by a date and time timestamp
- the `[name]` in the log entry is the value present in the name field at the moment of approval

**AC-5 — Approve: event**
Approving an event action:
- sends the approval to the backend via PATCH
- transitions the action row to a resolved approved state
- appends a log entry in the form `Event [name] — [datetime] added to calendar` followed by a date and time timestamp
- both `[name]` and `[datetime]` in the log entry reflect the values present in the fields at the moment of approval

**AC-6 — Decline**
Declining an action:
- sends the decline to the backend via PATCH
- transitions the action row to a resolved declined state (muted appearance, controls no longer interactive)
- appends no entry to the execution log

**AC-7 — Manual add-task**
An add-task control is always visible at the bottom of the actions block for all email
classifications. Activating it creates a new pending task action via POST and inserts an empty
task row with an empty name field and approve/decline controls.

**AC-8 — Manual add-event**
An add-event control is always visible at the bottom of the actions block for all email
classifications. Activating it creates a new pending event action via POST and inserts an empty
event row with an empty name field, an empty datetime field, and approve/decline controls.

**AC-9 — Execution log format and behaviour**
- Log entries are appended immediately on approval. Decline never appends a log entry.
- Each entry carries a timestamp at date-and-time precision.
- The log is cumulative: entries are never removed within a session.
- The log section is not rendered before any action on that email has been approved.

**AC-10 — Exclusive accordion toggle**
Only one email row may be expanded at a time. Opening any row collapses the previously open row.

---

## 4. Build note — editable field values on approval

The current PATCH endpoint (`PATCH /api/email-management/actions/{id}`) accepts only
`{status: "approved"|"declined"}`. It does not accept an updated name or datetime.

When the backend executes the task or calendar action, it reads `suggested_title` and
`calendar_start` from the stored DB record, not from the PATCH request. This means: if the
owner edits the name before approving, the frontend log will show the edited name but the
external system (Todoist / Google Calendar) will receive the original AI-suggested value.

Devon must resolve this gap before implementing. Two options:

1. Extend the PATCH request body to also accept `name` (and `event_datetime` for event actions)
   and update the stored record before execution. This ensures the log and the external system
   agree. Requires a backend change within Devon's scope.

2. Accept the discrepancy: the log reflects what the owner saw, execution uses the stored value.
   This is lower effort but misleads the owner.

Option 1 is the correct product behaviour given AC-4 and AC-5. If Devon chooses option 2, flag
this to Larry before marking G5 complete.

---

## 5. Test spec

### 5a. Automated feature tests — write failing tests first, then implementation

**Backend — extend `test_email_management.py`:**

| Scenario | Route | Expected outcome |
|----------|-------|-----------------|
| List actions for a known email | GET /emails/{id}/actions | 200, `actions` array with correct shape per item |
| List actions for an unknown email | GET /emails/{id}/actions | 404 |
| Create a task action | POST /emails/{id}/actions | 201/200, action row with type task, name, no event_datetime |
| Create an event action with datetime | POST /emails/{id}/actions | 201/200, action row with type event, name, and event_datetime |
| Create action for an unknown email | POST /emails/{id}/actions | 404 |
| Approve a pending task action | PATCH /actions/{id} | 200, status approved, external_id set, executed_at set |
| Approve a pending event action | PATCH /actions/{id} | 200, status approved, external_id set, executed_at set |
| Decline a pending action | PATCH /actions/{id} | 200, status declined, external_id null |
| Patch unknown action | PATCH /actions/{id} | 404 |
| Patch with invalid status | PATCH /actions/{id} | 422 |
| Patch without auth | PATCH /actions/{id} | 401 or 403 |

**Frontend — Vitest (or the project's existing test framework):**

| Scenario | Description |
|----------|-------------|
| Actions load on accordion open | Opening the accordion calls GET /actions and renders the returned rows |
| Task row pre-populated name | A task action from the API renders a pre-populated name field that accepts input |
| Event row name and datetime visible | An event action renders both a pre-populated name field and a pre-populated datetime field |
| Approve task — row state | Approving a task calls PATCH with approved status; row transitions to resolved state |
| Approve task — log entry | After approval the log contains one entry referencing the task name and a timestamp |
| Approve event — log entry | After approval the log entry references the event name, the datetime, and a timestamp |
| Decline — no log entry | Declining transitions the row to declined state; no entry added to the log |
| Manual add-task | Activating add-task calls POST /actions; new empty task row appears in pending state |
| Manual add-event | Activating add-event calls POST /actions; new empty event row with datetime field appears |
| Approve manual task — log entry | Approving a manually added task appends a log entry with the entered name and timestamp |
| Approve manual event — log entry | Approving a manually added event appends a log entry with entered name, datetime, and timestamp |
| Cumulative log | Two consecutive approvals produce two log entries in the order they occurred |
| Log absent before first approval | Accordion with only pending actions shows no log section |
| Exclusive accordion toggle | Opening a second accordion row collapses the first |

### 5b. Regression suite — these tests must stay green after the build

All existing tests in the email management test file covering:
- Run triage: `POST /api/email-management/run`
- List emails: `GET /api/email-management/emails`
- Email patch (triage status): `PATCH /api/email-management/emails/{id}`
- All Slice 1 and Slice 2 frontend smoke paths

Devon must run the full test suite and confirm zero regressions before marking G5 complete.

---

## 6. Smoke test definition

Devon runs these checks manually against the running application after implementation is complete.

1. Open the Email Management page. Confirm at least one pending email is shown in the list.
2. Open the accordion for an email that has AI-suggested actions. Confirm the actions panel
   renders with one or more action rows.
3. For a task action: confirm the name field is pre-populated with the AI suggestion and accepts
   input. Edit the name. Approve. Confirm the row enters resolved state. Confirm the log shows
   one entry containing the edited name and a timestamp in the format `Task [name] created`.
4. For an event action: confirm both the name and datetime fields are pre-populated and accept
   input. Edit both. Approve. Confirm the log entry contains the edited name, the edited
   datetime, and a timestamp in the format `Event [name] — [datetime] added to calendar`.
5. Decline one pending action. Confirm the row enters resolved declined state. Confirm no log
   entry was added.
6. Activate the add-task control. Confirm an empty task row appears with an empty name field and
   approve/decline controls. Enter a name. Approve. Confirm the log entry records the entered name.
7. Activate the add-event control. Confirm an empty event row appears with an empty name field,
   an empty datetime field, and approve/decline controls. Enter both fields. Approve. Confirm the
   log entry records both the name and the datetime.
8. Open the accordion for a second pending email. Confirm the first accordion collapses. Select
   the header of the open row again. Confirm it collapses and no other row opens.
9. Reload the page. Open the accordion for an email that had actions approved before the reload.
   Confirm approved action rows remain in resolved state (backend persistence confirmed).
10. Run the full test suite. Confirm all Slice 1, Slice 2, and Slice 3 backend tests are green
    and no previously passing tests have regressed.

---

*G4 brief — Sloane — 2026-06-28*
