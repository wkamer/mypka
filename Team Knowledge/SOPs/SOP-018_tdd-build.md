# SOP-018 — TDD Build

**Owner:** Devon
**Applies to:** Devon (and domain implementers Sasha, Finn where applicable)
**Trigger:** G5 gate — every feature build after G4 brief is received
**Last updated:** 2026-06-25

---

## Purpose

No feature is delivered without feature tests and regression tests passing. This SOP defines the build order and G5 completion criteria. Deviation is not permitted.

---

## Pre-condition

Devon does not start without a complete G4 brief from Sloane containing:
- Vertical slice definition
- Gherkin feature file
- Test spec (which scenarios become automated tests + regression scope)
- Acceptance criteria

If the G4 brief is missing or incomplete, route back to Larry before starting.

---

## Build Order

Execute in this sequence for every feature slice:

**1. Read the G4 brief**
Understand the slice definition, the scenarios, and the test spec before touching any code.

**2. Inspect the existing codebase**
Read existing patterns, folder structure, naming conventions, tests, state layer, API layer, and persistence patterns. Match them.

**3. Write failing feature tests**
Implement the feature tests from Sloane's test spec. Tests must fail before any implementation code is written. No exceptions.

**4. Write implementation code**
Write the minimum code to make the failing tests pass. Do not write more than the tests require.

**5. Run the regression suite**
The full project test suite must be green before G5 is closed. Any regression is a blocker — fix before proceeding.

**6. Verify end-to-end in the running system**
Run the feature in the actual running environment. Confirm the happy path works end-to-end. This is not optional.

**7. Produce the test report**
Document: which feature tests were written and passed, regression suite status (green / count), and confirmation of end-to-end verification. This report is the G5 handoff deliverable.

**8. Stop and report to owner**
After completing one slice, stop. Report the test report to the owner and wait for explicit feedback before starting the next slice. Do not start the next slice without owner acknowledgment. This is not optional.

---

## Slice Delivery Discipline

Devon delivers one slice at a time. The feedback loop is:

1. Build slice (steps 1-7 above)
2. Report to owner with the test report
3. Wait for owner feedback
4. Only then start the next slice

Delivering multiple slices before owner feedback is a process violation. Each slice must be owner-verifiable in under 15 minutes. If a slice cannot be verified in 15 minutes, it is too large — route back to Sloane to re-slice.

---

## G5 Completion Criteria

G5 is not complete until all of the following are true:

- All feature tests from Sloane's G4 test spec are implemented and green
- Full regression suite is green
- Feature verified end-to-end in the running system
- Test report produced and included in handoff
- Owner has verified and acknowledged each slice before the next began

If any item is missing, G5 is still in progress.

---

## Expected Test Coverage

Per feature build:

- Unit tests for pure logic
- Service tests for backend behavior
- API tests for request and response behavior
- Frontend component tests where the project already uses them
- Integration tests when the feature crosses frontend/backend boundaries and the project supports them
- Regression tests for fixed bugs

Coverage follows the test spec from Sloane. Devon does not define coverage scope independently.

---

## Test Report Format

Minimum required content:

```
Feature: [feature name]
Slice: [slice name]

Feature tests: [count] written, [count] passing
Regression suite: green / [count] tests
End-to-end verification: confirmed / [what was verified]

Blockers resolved: [any issues encountered and how resolved, or "none"]
```

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — extracted from Devon AGENT.md, formalizes TDD enforcement | Larry |
| 2026-06-25 | Added step 8 (stop and report), Slice Delivery Discipline section, and 15-min verifiability rule | Sloane |
