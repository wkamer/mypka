# SOP-016 — Feature Brief

**Owner:** Phoebe
**Applies to:** Phoebe
**Trigger:** G2 gate — every feature before architecture begins
**Last updated:** 2026-06-25

---

## Purpose

A Feature Brief is the G2 output. It locks scope and user value before Kai starts architecture and Sloane writes scenarios. If Sloane cannot write testable scenarios from a Feature Brief without asking Phoebe for clarification, the brief is not done.

---

## Required Sections

Every Feature Brief contains exactly these five sections:

### 1. Problem statement
What problem does this solve, for whom, and why now.
Not the solution — the problem.

### 2. User value
What the user gains, expressed as an observable behavior or outcome.

**Weak:** "Users will find it easier to manage their tasks."
**Strong:** "Users will complete task assignment without leaving the current screen, reducing the steps from four to one."

The strong version allows Sloane to write a testable scenario. The weak version does not.

### 3. Scope boundary
What is explicitly included.
Every item must pass the "so that" test: "We are building X so that [user] can [outcome]." If the outcome cannot be stated, the item does not belong.

### 4. Non-goals
What is explicitly excluded, with rationale.
Non-goals are not afterthoughts — they are active decisions that prevent scope creep downstream.

### 5. Acceptance criteria
Feature-level conditions that must be true for G2 to sign off.

Criteria must be:
- Observable: can be confirmed by watching a user interact with the system
- Independent of implementation: would still be valid if the UI changed
- Sufficient: Sloane can derive testable Gherkin scenarios without further input

---

## G2 Sign-Off

G2 is signed off when all five sections are complete and Phoebe confirms:
- The scope boundary is the minimum that delivers the stated user value
- Non-goals explicitly exclude anything that was considered and rejected
- Acceptance criteria are testable without knowing how the UI is built

G2 is not signed off on verbal agreement. The Feature Brief must be written.

---

## Scope Discipline

**Scope creep is the default.** Every request arrives slightly larger than necessary. Phoebe finds the minimum viable scope that still delivers the user outcome and holds that boundary.

**The "so that" test:** Every scope item must pass: "We are building X so that [user] can [outcome]." If the outcome cannot be stated, the scope item does not belong.

---

## Prioritization

Features are sequenced on two axes:
- **User value:** how much does this change user behavior for the better
- **Strategic impact:** how much does this move the system forward

Features high on both are sequenced first. Features high on only one require explicit rationale.

No feature enters the backlog without a value rationale. No feature enters the roadmap without a Feature Brief at G2 sign-off level.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — extracted from Phoebe AGENT.md | Larry |
