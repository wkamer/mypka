# GL-024 — Delivery Pipeline

**Owner:** Larry
**Applies to:** Phoebe, Kai, Sloane, Devon (and domain implementers: Sasha, Finn)
**Trigger:** Any myPKA product feature build
**Last updated:** 2026-06-25

---

## Gate Sequence

```
G1  Larry      Routing + brief quality
G2  Phoebe     Scope + user value validated
G3  Kai        Architecture decided
G4  Sloane     Scenarios written, slice end-to-end and testable
G5  Implementer Build + tests green + verified in running system
G6  Owner      Acceptance
```

No gate may be skipped. No gate advances without the required output from the previous gate.

---

## Gate Definitions

### G1 — Larry (Routing)

**Input required:** Owner request
**Output:** Complete brief to Phoebe (or Pax / Vera if no build follows)
**Passes when:** Brief contains — problem statement, context, done looks like, minimum viable

### G2 — Phoebe (Scope + User Value)

**Input required:** Larry brief
**Output:** Signed Feature Brief (see SOP-016)
**Passes when:** Feature Brief contains problem statement, user value (observable), scope boundary, non-goals, and feature-level acceptance criteria — and Sloane can write testable scenarios from it without asking Phoebe

### G3 — Kai (Architecture)

**Input required:** G2 Feature Brief
**Output:** Architecture decision + technical constraints
**Passes when:** Stack, data boundaries, and integration points are decided and documented — Devon or domain implementer can build without making architecture decisions

### G4 — Sloane (Test-First)

**Input required:** G2 Feature Brief + G3 architecture decisions
**Output:** Vertical slice plan + Gherkin feature file + test spec (see SOP-017)
**Passes when:** Each slice is end-to-end, independently deliverable, and has at least one happy path and one edge case scenario — implementer can start without asking Sloane for clarification

### G5 — Domain Implementer (Build)

**Input required:** G4 brief (slice plan + Gherkin feature file + test spec)
**Implementer routing:** Devon (full-stack), Sasha (Shopify), Finn (WordPress) — Larry specifies in G1 brief
**Output:** Working feature + test report (see SOP-018)
**Passes when:** All feature tests from Sloane's test spec are green, regression suite is green, feature verified end-to-end in the running system, test report produced

### G6 — Owner (Acceptance)

**Input required:** G5 test report + working feature
**Output:** Accept or reject with reason
**Passes when:** Owner confirms the feature solves the stated problem from G2

---

## Hard Rules

- A gate may not be bypassed by any specialist, including Larry
- If a gate cannot be passed due to missing input, the specialist routes back to the previous gate owner — not to the Owner
- G4 never begins without G2 and G3 complete
- G5 never begins without G4 complete
- The domain implementer at G5 is determined by Larry at G1 — Sloane does not choose

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — delivery pipeline gate reference for myPKA product builds | Larry |
