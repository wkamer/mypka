# G4 Brief — Email Management Part 2

**Author:** Sloane  
**Date:** 2026-06-29  
**Gate:** G4  
**Input spec:** Quinn-interaction-spec-full-review.md  
**Status:** Ready for Devon / Codex  

---

## Slice Plan

Two slices. Independent. Sequential delivery is preferred — Slice 4 touches logic, Slice 5 touches markup. No cross-dependency.

| Slice | Name | Scope | Files touched |
|-------|------|-------|---------------|
| Slice 4 | State Reconstruction | Fix merge priority in ActionsPanel; remove GET /log call; rebuild log from GET /actions response | `ActionsPanel.jsx` |
| Slice 5 | Accessibility and Design Fixes | 10 issues from Quinn spec: 4 contrast failures, keyboard operability, focus rings, semantic fixes, section label | `InboxRow.jsx`, `ActionRowV3.jsx`, `ActionsPanel.jsx`, `EmailTriage.jsx` |

---

## Slice 4 — State Reconstruction

### Acceptance Criteria

1. On page load after a previous session, opening an email accordion shows each action in its last persisted state (approved or declined) without re-approving.
2. If the API returns `status: "approved"` for an action and the current session has no record for that action, the action renders as approved.
3. If the API returns `status: "approved"` for an action and the current session has that action as pending, the API status wins — the action renders as approved.
4. If the API returns `status: "pending"` and the current session resolved that action in the current session, the session state wins — the action renders as the session resolved it.
5. On accordion open, the execution log is populated from approved actions in the GET /actions response, sorted newest first by `approved_at`.
6. No GET `/api/email-management/emails/{emailId}/log` request is made at any point.
7. If an approved action has `approved_at: null`, it is excluded from log reconstruction without error.
8. If GET /actions fails, the error message renders and no log section renders independently.

### Gherkin Feature File

```gherkin
Feature: Email action state reconstruction on accordion open

  Background:
    Given the email management page has loaded
    And email "email-001" has two actions persisted in the database:
      | id          | type  | name                          | status   | approved_at              |
      | action-001  | Task  | Send follow-up to Remko       | approved | 2026-06-28T14:03:00Z     |
      | action-002  | Event | Broederweekend planning call  | pending  | null                     |

  Scenario: Approved actions render in approved state on first open after page refresh
    Given the browser has been refreshed and session state is cleared
    When the user opens the accordion for email "email-001"
    Then action "action-001" renders as approved without a confirm button
    And action "action-002" renders with approve and decline buttons
    And the execution log shows one entry for "action-001" with the correct timestamp

  Scenario: API approved status overrides stale session pending state
    Given the session state records action "action-001" as pending
    When the user opens the accordion for email "email-001"
    Then action "action-001" renders as approved
    And the execution log contains an entry for action "action-001"

  Scenario: Session resolved state is preserved when API still returns pending
    Given the user approved action "action-002" earlier in the current session
    And the API still returns status "pending" for action "action-002"
    When the user closes and reopens the accordion for email "email-001" within the same session
    Then action "action-002" renders as approved

  Scenario: Approved action with null approved_at is excluded from log
    Given email "email-003" has one action with status "approved" and approved_at null
    When the user opens the accordion for email "email-003"
    Then the execution log is empty
    And no error is shown

  Scenario: Actions fetch failure shows error and no log section
    Given GET /actions for email "email-001" returns a 500 error
    When the user opens the accordion for email "email-001"
    Then the error message "Failed to load actions" is shown
    And no execution log section is rendered

  Scenario: No GET /log request is issued on accordion open
    When the user opens the accordion for email "email-001"
    Then no HTTP request is made to "/api/email-management/emails/email-001/log"
```

### Test Spec

| Scenario | Automate | Regression |
|----------|----------|------------|
| Approved state renders on first open after refresh | Yes — unit test on merge function | Yes |
| API approved overrides stale session pending | Yes — unit test on merge function | Yes |
| Session resolved state preserved within session | Yes — unit test on merge function | Yes |
| Null approved_at excluded from log | Yes — unit test on log reconstruction | Yes |
| Actions fetch failure — error, no log | Yes — component test with mocked fetch | Yes |
| No GET /log request issued | Yes — component test, assert fetch not called | Yes |

All six scenarios form the Slice 4 regression suite. The merge function and log reconstruction function should have isolated unit tests. The no-/log-call check can be verified by asserting on `fetch` mock calls in the component test.

---

## Slice 5 — Accessibility and Design Fixes

### Acceptance Criteria

1. The received date in InboxRow passes WCAG 1.4.3 AA contrast (at minimum 4.5:1 on the dark background).
2. The Decline button in ActionRowV3 passes WCAG 1.4.3 AA contrast at base state.
3. The action type label in ActionRowV3 passes WCAG 1.4.3 AA contrast.
4. The "Execution log" heading in ActionsPanel passes WCAG 1.4.3 AA contrast.
5. InboxRow is reachable by keyboard Tab and can be opened or closed with Enter and Space.
6. InboxRow communicates open/closed state to screen readers via `aria-expanded`.
7. The accordion panel id matches the `aria-controls` value on the toggle row.
8. The Approve and Decline buttons show a visible focus ring when focused by keyboard.
9. The name and datetime inputs show a visible focus ring when focused by keyboard.
10. The chevron SVG in InboxRow is hidden from assistive technology.
11. The Back button in EmailTriage is an anchor element navigating to `/dashboard`, not a button that calls `window.location.href`.
12. A visible "Actions" section label appears before the action rows in ActionsPanel.

### Gherkin Feature File

```gherkin
Feature: Email management accessibility and design compliance

  Background:
    Given the email management page has loaded
    And at least one email is present in the inbox list

  Scenario: Keyboard user can open an email accordion
    Given the user has not used the mouse
    When the user presses Tab until an email row receives focus
    Then the email row is visually indicated as focused
    When the user presses Enter
    Then the accordion panel opens
    When the user presses Space
    Then the accordion panel closes

  Scenario: Screen reader receives accurate expanded state
    Given email "email-001" accordion is closed
    When the email row for "email-001" has focus
    Then the row exposes aria-expanded="false" to assistive technology
    When the user opens the accordion
    Then the row exposes aria-expanded="true" to assistive technology

  Scenario: Keyboard user can reach and activate Approve and Decline buttons
    Given the accordion for "email-001" is open
    And "email-001" has one pending action
    When the user presses Tab until the Approve button receives focus
    Then a focus ring is visible on the Approve button
    When the user presses Tab once more
    Then a focus ring is visible on the Decline button

  Scenario: Keyboard user can reach the name input and see focus indicator
    Given the accordion for "email-001" is open
    And "email-001" has one pending Task action
    When the user tabs to the name input
    Then a visible ring appears around the name input

  Scenario: Back button navigates without JavaScript redirect
    When the user activates the Back control
    Then the browser navigates to "/dashboard" as a standard link

  Scenario: Actions section label is visible before action rows
    Given the accordion for "email-001" is open
    Then the text "ACTIONS" is visible above the first action row

  Scenario: Decorative chevron is not announced by screen reader
    When a screen reader traverses the email row for "email-001"
    Then the chevron icon is not announced
```

### Test Spec

| Scenario | Automate | Regression |
|----------|----------|------------|
| Keyboard opens accordion via Enter | Yes — jsdom keyboard event test | Yes |
| Keyboard opens accordion via Space | Yes — jsdom keyboard event test | Yes |
| aria-expanded reflects open state | Yes — attribute assertion in component test | Yes |
| Approve button shows focus ring class | Yes — class assertion in component test | Yes |
| Decline button shows focus ring class | Yes — class assertion in component test | Yes |
| Name input shows focus ring class | Yes — class assertion in component test | Yes |
| Back button renders as anchor | Yes — element type assertion | Yes |
| Actions section label present | Yes — text content assertion | Yes |
| Chevron has aria-hidden="true" | Yes — attribute assertion | Yes |
| Contrast ratios (Issues 1-4) | Manual — computed contrast requires browser rendering | Manual check, not automated |

Contrast ratio checks (Issues 1, 2, 3, 4) are not automatable in jsdom. These are verified manually in the running app or via a browser accessibility tool (e.g. Chrome DevTools contrast checker) after the build. All other scenarios are automated and form the Slice 5 regression suite.

---

## File Locations

| File | Path |
|------|------|
| EmailTriage | `/opt/myPKA/apps/dashboard/frontend/src/pages/EmailTriage.jsx` |
| InboxRow | `/opt/myPKA/apps/dashboard/frontend/src/components/EmailTriage/InboxRow.jsx` |
| ActionsPanel | `/opt/myPKA/apps/dashboard/frontend/src/components/EmailTriage/ActionsPanel.jsx` |
| ActionRowV3 | `/opt/myPKA/apps/dashboard/frontend/src/components/EmailTriage/ActionRowV3.jsx` |
| Existing test file | `/opt/myPKA/apps/dashboard/frontend/src/pages/EmailTriage.test.jsx` |

---

## Handoff Notes for Devon

- Slice 4 and Slice 5 can be built in a single session. Slice 4 first — it changes logic. Slice 5 second — it changes markup.
- Slice 4 has no markup changes. All changes are in the `useEffect` that fetches actions in `ActionsPanel.jsx`.
- Slice 5 has no logic changes. All changes are Tailwind token swaps, ARIA attribute additions, and one element type change (`<button>` to `<a>`).
- The existing `buildLogEntry` function is correct and must not be changed.
- The existing `EmailTriage.test.jsx` should be extended, not replaced.
- React Router usage: check whether `App.jsx` uses React Router before choosing between `<a href>` and `<Link to>` for the Back button fix (Issue 9).

---

*Sloane — 2026-06-29*
