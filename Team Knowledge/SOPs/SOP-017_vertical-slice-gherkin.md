# SOP-017 — Vertical Slice and Gherkin Scenarios

**Owner:** Sloane
**Applies to:** Sloane
**Trigger:** G4 gate — every feature before the domain implementer starts
**Last updated:** 2026-06-25

---

## Purpose

The G4 brief is the contract between Sloane and the domain implementer. It contains the vertical slice plan, Gherkin feature file, and test spec. The implementer builds against it without asking Sloane for clarification.

---

## Vertical Slice Standards

A vertical slice is the thinnest possible unit of work that:
1. Touches every architectural layer end-to-end (UI through to persistence and back)
2. Delivers observable value to the user when complete
3. Can be built, deployed, and validated independently of other slices

**Rejected (horizontal):** "Build all database models for the feature."
No user value when complete. Cannot be validated end-to-end.

**Accepted (vertical):** "User can create a single task with a title. Task persists across page refresh."
Touches every layer. Observable value. Can be validated end-to-end.

### Slicing heuristics

- Start with the simplest possible user action that produces a visible result
- Each subsequent slice adds one dimension of complexity (more fields, edge cases, secondary flows)
- Never slice by technical layer — always slice by user capability
- If a slice cannot be completed in one focused work session, split it further
- If a slice cannot be demonstrated to a user at the end of a work session, recut it as a vertical slice

---

## Gherkin Scenario Standards

### Structure

```gherkin
Feature: [Feature name from Feature Brief]

  Scenario: [Behaviour being described]
    Given [initial context — what is true before the user acts]
    When  [user action or system event]
    Then  [observable outcome]
```

For scenarios with multiple conditions:

```gherkin
  Scenario Outline: [Behaviour with varying inputs]
    Given [context]
    When  [action] with <input>
    Then  [outcome] shows <result>

    Examples:
      | input | result |
      | ...   | ...    |
```

### Behaviour level — mandatory

Every scenario describes behaviour, not implementation. Test: if the scenario would need to change because a button was renamed or a field was moved, it is written at the wrong level.

- Valid: "When the user submits the form"
- Invalid: "When the user clicks the blue Submit button in the top-right corner"
- Valid: "Then the task appears in the user's task list"
- Invalid: "Then the database record has status='active'"

### Minimum coverage per slice

- One happy path scenario — the standard case where everything works
- At least one edge case — missing input, invalid state, or unexpected system state

### Scenario independence

Each scenario must be runnable in isolation. No scenario depends on state created by a previous scenario in the same feature file.

---

## Test Spec

The test spec accompanies the Gherkin feature file in every G4 brief.

It specifies:
- Which scenarios must be implemented as automated feature tests
- Which existing tests form the regression suite that must remain green after the build

The implementer writes failing tests first from this spec, then writes implementation code to make them pass. The test spec is the contract — the implementer does not define their own test scope.

---

## G4 Brief Contents

Every G4 brief delivered to the domain implementer contains:

1. Slice definition (which slice from the vertical slice plan)
2. Gherkin feature file
3. Test spec (automated test scope + regression scope)
4. Acceptance criteria (from G2 Feature Brief, expressed at slice level)

The brief is self-contained. The implementer starts without asking Sloane for clarification.

---

## Rejection

Sloane issues a rejection notice when:
- A Feature Brief from Phoebe is too vague to write testable scenarios — flag before attempting, never after
- Architecture from Kai is missing or contradictory — route to Larry before writing

A rejection notice states: what is missing and what must change before re-submission. Two sentences maximum.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — extracted from Sloane AGENT.md | Larry |
