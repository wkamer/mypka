# GL-024 — Delivery Pipeline

**Owner:** Larry
**Applies to:** Phoebe, Kai, Sloane, Devon (and domain implementers: Sasha, Finn)
**Trigger:** Any myPKA product feature build
**Last updated:** 2026-06-25

---

## Gate Sequence

```
G1   Larry       Routing + brief quality
G2   Phoebe      Scope + user value validated
G2.5 Cleo        Visual prototype (conditional — see below)
G3   Kai         Architecture decided
G4   Sloane      Scenarios written, slice end-to-end and testable
G5   Implementer Build + tests green + verified in running system
G6   Owner       Acceptance
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

#### G2 variant: UI features — Designing in the browser

For any feature with a visible UI component, Phoebe produces a **flat HTML prototype** in addition to (or instead of) a prose brief. This is the primary G2 deliverable for UI features.

**What it is:** A single `.html` file using Tailwind CDN (`<script src="https://cdn.tailwindcss.com">`). No build step, no React, no Node. Opens directly in a browser. Uses identical Tailwind classes to what Devon will build.

**Who owns it:** Phoebe. She iterates on it until the owner approves. The approved flat file is the frozen design.

**Where it lives:** `Deliverables/YYYYMMDD_Domain_feature/prototype/feature-name-v1.html`

**Rules:**
- Time-box: max 4 hours per prototype iteration
- Owner approves visually before G3 begins
- Devon does not touch the dashboard until the owner has approved the prototype
- Devon ports the approved HTML to React — he does not redesign. No design decisions at G5.
- The prototype is throwaway. Devon re-implements; copy-paste is not expected.

**MVP gate:** A feature may not ship to the running dashboard until the owner has accepted the prototype at G2 and signed off at G6. "Designing in the browser" means no partial builds land in production while the design is still open.

### G2.5 — Cleo (Visual Prototype) — Conditional

**Trigger:** G2.5 is required when the G2 output is a prose brief for a feature with novel layout, new visual patterns, or multiple branching states where the spec leaves open any question Devon would have to answer independently about layout or state behavior.

**G2.5 is skipped when:** The G2 output is a markdown design spec, the pattern is one Devon has built before, and the spec is unambiguous — no layout or state decision is left open for Devon to interpret.

| Feature type | G2 output | G2.5 |
|---|---|---|
| Novel layout, new pattern, multiple branching states | Prose brief | Required. Cleo builds HTML prototype. |
| Simple pattern Devon has built before, clear markdown spec | Markdown spec | Skipped. Goes directly to G3. |

**When required:**
**Input required:** G2 Feature Brief or prose brief
**Output:** Approved flat HTML prototype (`Deliverables/YYYYMMDD_Domain_feature/prototype/feature-name-v1.html`)
**Passes when:** Owner approves the prototype visually. Approved file is the frozen design. Devon ports it — no redesign at G5.
**Rules:** Time-box max 4 hours per iteration. Devon does not touch the feature until G2.5 passes.

**When skipped:**
The G2 markdown spec is the frozen design. It passes directly to Kai at G3. Devon builds from the markdown — no interpretation permitted; if a gap exists, Devon routes back to Phoebe before building.

---

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
- G2.5 is conditional — Phoebe determines at G2 whether G2.5 is required or skipped based on the trigger criteria above
- G3 never begins without G2 complete and G2.5 resolved (either passed or explicitly skipped)
- G4 never begins without G2 and G3 complete
- G5 never begins without G4 complete
- The domain implementer at G5 is determined by Larry at G1 — Sloane does not choose
- G5 delivers one slice at a time. Owner verifies each slice before Devon continues.

---

## Changelog

| Date | Change | By |
|---|---|---|
| 2026-06-25 | Created — delivery pipeline gate reference for myPKA product builds | Larry |
| 2026-06-25 | G5: added slice-at-a-time delivery rule, 15-min verifiability size guideline, and Hard Rule | Sloane |
| 2026-06-26 | G2: added "designing in the browser" variant for UI features — flat HTML prototype as primary G2 deliverable, MVP gate rule | Larry |
| 2026-06-27 | G2.5 added as conditional gate — Cleo's HTML prototype required for novel/complex UI, skipped for simple patterns with unambiguous markdown spec; hard rules updated accordingly | Larry / Phoebe |
