# GL-024 — Delivery Pipeline

**Owner:** Larry
**Applies to:** Phoebe, Kai, Sloane, Devon (and domain implementers: Sasha, Finn)
**Trigger:** Any myPKA product feature build
**Last updated:** 2026-06-25

---

## Gate Sequence

```
G1  Larry       Routing + brief quality
G2  Phoebe      Scope shaped — appetite, breadboard, fat marker sketch approved by owner
G3  Kai         Architecture decided
G4  Sloane      Scenarios written, slice end-to-end and testable
G5  Implementer Build + tests green + verified in running system
G6  Owner       Acceptance
```

No gate may be skipped. No gate advances without the required output from the previous gate.

---

## Gate Definitions

### G1 — Larry (Routing)

**Input required:** Owner request
**Output:** Complete brief to Phoebe (or Pax / Vera if no build follows)
**Passes when:** Brief contains — problem statement, context, done looks like, minimum viable

### G2 — Phoebe (Shaping)

**Input required:** Larry brief
**Output:** Shaped pitch containing — appetite, breadboard, fat marker sketch (for UI features), rabbit holes, no-gos
**Passes when:** Owner has approved the breadboard and fat marker sketch. Sloane can write testable scenarios from the pitch without asking Phoebe.

#### Appetite

Every G2 pitch opens with an appetite: "This feature is worth [N hours/days] of build time." Appetite is set by the owner before shaping begins — not after. Appetite constrains what Phoebe shapes. If the shaped solution cannot fit the appetite, scope is cut. Time is never extended.

#### Breadboard

A text-only artifact. Answers: what connects to what? Three elements: places (screens/panels), affordances (buttons/fields/links), and connection lines (arrows showing where actions go).

No visual design. No layout information. Phoebe produces this in 15 to 30 minutes.

#### Fat marker sketch (UI features)

A rough spatial artifact. Answers: where does each element go relative to the others? ASCII or hand-drawn. Deliberately rough — column widths, font sizes, and padding are Devon's decisions.

Phoebe produces this in 15 to 30 minutes.

#### Rabbit holes and no-gos

Every pitch includes:
- **Rabbit holes:** known implementation traps that could blow the appetite — named explicitly so Devon can avoid them
- **No-gos:** features or behaviors explicitly excluded from this iteration

#### Owner approval at G2

The owner reviews breadboard and fat marker sketch and approves or corrects. Corrections cost minutes. G3 does not begin until the owner has explicitly approved. The approved pitch is the frozen scope — no additions during G5.

#### On-demand visual prototype (Cleo)

For features where a fat marker sketch leaves genuine visual ambiguity the owner cannot resolve from the sketch alone, Cleo may be activated on request to produce a flat HTML prototype. This is not a gate — it is an optional tool. Cleo is activated by Larry, not by Phoebe.

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
**Output:** Working feature + test report per slice (see SOP-018)
**Passes when:** All feature tests from Sloane's test spec are green, regression suite is green, feature verified end-to-end in the running system, test report produced
**Slice delivery rule:** The implementer delivers one slice at a time. After each slice: stop, report to owner, wait for feedback before starting the next slice. Batching slices is not permitted.
**Slice size:** Each slice must be owner-verifiable in under 15 minutes. If a slice cannot be verified in 15 minutes, it is too large — re-slice before building.

### G6 — Owner (Acceptance)

**Input required:** G5 test report + working feature
**Output:** Accept or reject with reason
**Passes when:** Owner confirms the feature solves the stated problem from G2

---

## Hard Rules

- A gate may not be bypassed by any specialist, including Larry
- If a gate cannot be passed due to missing input, the specialist routes back to the previous gate owner — not to the Owner
- G3 never begins without owner-approved G2 pitch (breadboard + fat marker sketch approved)
- G4 never begins without G2 and G3 complete
- G5 never begins without G4 complete
- The domain implementer at G5 is determined by Larry at G1 — Sloane does not choose
- G5 delivers one slice at a time. Owner verifies each slice before Devon continues.
- Circuit breaker: if shaped work cannot fit the appetite during G5, scope is cut — time is never extended. Devon routes back to Phoebe for re-shaping, not to owner for a time extension.
- No scope additions during G5. Any new idea is a new pitch at G1.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — delivery pipeline gate reference for myPKA product builds | Larry |
| 2026-06-25 | G5: added slice-at-a-time delivery rule, 15-min verifiability size guideline, and Hard Rule | Sloane |
| 2026-06-26 | G2: added "designing in the browser" variant for UI features — flat HTML prototype as primary G2 deliverable, MVP gate rule | Larry |
| 2026-06-27 | G2.5 added as conditional gate — Cleo's HTML prototype required for novel/complex UI, skipped for simple patterns with unambiguous markdown spec; hard rules updated accordingly | Larry / Phoebe |
| 2026-06-27 | Shape Up adopted — G2.5 removed; G2 rewritten with appetite, breadboard, fat marker sketch, rabbit holes, no-gos as mandatory pitch output; circuit breaker and no-scope-addition rules added; Cleo moved to on-demand role | Larry / Sloane / Phoebe |
