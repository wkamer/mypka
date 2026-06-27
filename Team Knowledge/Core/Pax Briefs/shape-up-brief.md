# Shape Up — Research Brief for myPKA Delivery Framework

**Author:** Pax  
**Date:** 2026-06-27  
**Requested by:** Larry, on behalf of Phoebe and Sloane  
**Primary sources:** basecamp.com/shapeup (Chapters 1 through 10, read directly)  
**Status:** Delivered

---

## TL;DR

Shape Up is a product development methodology by Basecamp (Ryan Singer, 2019). Its core insight: the problem with slow product delivery is not execution — it is under-specified work entering the build phase. Shape Up fixes this at the source by requiring that a trained "shaper" resolves scope, solution, and risk before any team picks up the work. The key artifacts are the breadboard (interaction topology, text-based), the fat marker sketch (spatial layout, deliberately rough), and the pitch (the complete shaped package). The build cycle is fixed at six weeks, scope is variable, and there is no extension — the circuit breaker kills unfinished work and returns it to shaping.

For the myPKA pipeline: Shape Up's shaping phase maps cleanly onto G2 (Phoebe) and extends it with two concrete artifacts that replace or supplement the current markdown spec. The methodology does not require a wholesale adoption. The three conventions that matter for this system are appetite, breadboard, and the pitch format. These can be inserted into the existing GL-024 gates without restructuring the pipeline.

---

## 1. Core Shape Up Concepts

### 1.1 The Abstraction Problem

Shape Up begins with a diagnosis: product managers err in one of two directions.

**Too concrete** — wireframes and high-fidelity mockups. These over-specify detail before the solution is validated. They leave the implementer no room to trade scope for time. They generate estimation errors because making the interface "just so" requires solving hidden implementation details not visible in the mockup.

**Too abstract** — prose requirements like "build a calendar view." No implementer can make trade-offs from this. No boundary exists to define what is out of scope. The work grows unbounded.

Shape Up targets the zone between these extremes: rough enough that the implementer resolves details, specific enough that they know what they are building and what they are not.

The three properties of shaped work (from Chapter 2, primary source):

- **Rough.** The concept is sketched, not designed. Details are deliberately left open so the implementer can adapt during build. Roughness also signals that the work has not been pixel-polished — it is a brief, not a spec.
- **Solved.** The shaped work represents a point of view on the solution. It is not a list of requirements or a problem statement. Whoever shaped it has thought through the major elements and made a real design decision about the approach.
- **Bounded.** The shaped work defines what is out of scope — explicitly. The appetite (see below) is the primary boundary. "Bounded" means the implementer knows when to stop.

---

### 1.2 Appetite

**Definition (primary source, Chapter 3):**

> "You can think of the appetite as a time budget for a standard team size."

An appetite is the maximum time you are willing to invest in a solution before deciding it is not worth more. It is set before shaping, not after. This is the inverse of estimation.

- Estimation: start with a design, derive a time number.
- Appetite: start with a time number, constrain the design to fit.

Basecamp uses two standard sizes:

| Type | Team | Duration |
|---|---|---|
| Small Batch | 1 designer + 1-2 programmers | 1-2 weeks |
| Big Batch | 1 designer + 1-2 programmers | 6 weeks (full cycle) |

The appetite acts as a creative constraint. When you know you have two weeks, you design a different solution than when you assume unlimited time. The appetite determines which problems you cut and which you keep.

**Fixed time, variable scope (Chapter 3):**

> "An appetite is completely different from an estimate. Estimates start with a design and end with a number. Appetites start with a number and end with a design."

Scope is the variable. Time is fixed. When scope threatens to exceed the appetite, you cut features — you do not extend the cycle.

---

### 1.3 Breadboard

**Definition (primary source, Chapter 4):**

> "A breadboard is an electrical engineering prototype that has all the components and wiring of a real device but no industrial design."

A breadboard answers the topology question: what connects to what? It does not answer the visual design question: where does each element go, what color, what size?

A breadboard uses three elements, all written as text on paper or a whiteboard:

1. **Places** — screens, dialogs, or menus the user can navigate to. Written as a name with an underline.
2. **Affordances** — things the user can act on: buttons, fields, copy. Written below the place they appear at.
3. **Connection lines** — arrows showing which affordance takes the user to which place.

No visual design is implied. A modal and a separate screen are indistinguishable in a breadboard — both are just "a place." This is intentional. The breadboard forces the shaper to think about interaction flow and the presence of elements, not their appearance.

**What a breadboard is not:**

- Not a wireframe (wireframes imply spatial layout and relative sizing)
- Not a user story (no "as a user I want")
- Not a component spec (no pixel values, no color, no hierarchy weights)

**Practical notation (text-based):**

```
Invoice
  [Turn on Autopay] --> Setup Autopay
                          [Credit card fields]
                          [Save] --> Invoice (with Autopay active)
                          [Cancel] --> Invoice
```

The shaper can produce this in five minutes. It communicates the interaction path without committing to any visual decision. The implementer — designer or developer — fills in the visual design during the build cycle.

---

### 1.4 Fat Marker Sketch

**Definition (primary source, Chapter 4):**

> "A fat marker sketch is a sketch made with such broad strokes that adding detail is difficult or impossible."

The fat marker sketch is used when the fundamental problem is spatial — when the 2D arrangement of elements is the core design question. A breadboard would miss the point because the position of elements relative to each other is what needs to be communicated.

The fat marker sketch uses:

- Thick marker strokes (physical Sharpie or iPad pen set to large diameter)
- Rough shapes suggesting zones, columns, panels
- Labels written directly on shapes to identify what each area is
- No pixel precision, no alignment guides, no spacing numbers

The deliberate roughness serves a function: it prevents premature convergence on a specific visual solution. A scanned Sharpie sketch signals to the implementer that they are looking at a concept, not a spec. It prevents the implementer from treating sketched proportions as real proportions.

**When to use breadboard vs. fat marker sketch:**

| Situation | Artifact |
|---|---|
| Interaction flow is the question (what connects to what) | Breadboard |
| Spatial layout is the question (where things go relative to each other) | Fat marker sketch |
| Both questions are open | Both — breadboard first, then fat marker sketch for complex panels |

---

### 1.5 Bet and Pitch

**Bet (primary source, Chapters 7-8):**

A bet is a committed decision to invest a fixed time cycle in a shaped project. The term is deliberate: a bet implies a stake (the cycle), a risk (the circuit breaker, see Section 4), and a point of no return (the team starts and works uninterrupted). A bet is not a prioritized backlog item. It is a commitment.

Before betting, the shaped work is packaged into a **pitch**. The pitch is the formal document presented at the betting table. From Chapter 5 and the Structure of a Pitch:

**Five sections of a pitch:**

1. **Problem** — the raw idea, a use case, or something observed that motivates the work. One to three sentences. No solution here.
2. **Appetite** — how much time this is worth. Small batch (1-2 weeks) or big batch (6 weeks). This signals the scope ceiling to everyone reading.
3. **Solution** — the shaped concept. This is where breadboards and fat marker sketches appear. Enough to understand the approach, not enough to eliminate all decisions from the implementer.
4. **Rabbit holes** — known risks, tricky implementation paths, or assumptions that could break the project. Named and explicitly called out so the team knows to avoid them.
5. **No-gos** — explicit things that are out of scope for this cycle. "We are not building X" is a first-class statement, not an omission.

The betting table is a short meeting (rarely more than two hours) with the decision-makers. There is no backlog to review. The pitches on the table are the only options. If a pitch is not chosen, it is dropped. If someone wants to revive it, they lobby for it at the next betting table — they track it themselves. This eliminates the backlog maintenance cost entirely.

---

## 2. Shaping Maps to G1/G2 in GL-024

### Current GL-024 Structure (relevant gates)

| Gate | Owner | Current output |
|---|---|---|
| G1 | Larry | Routing + brief |
| G2 | Phoebe | Feature brief (markdown prose) OR flat HTML prototype |
| G2.5 | Cleo (conditional) | Flat HTML prototype for novel layouts |
| G3 | Kai | Architecture decisions |
| G4 | Sloane | Vertical slice plan + Gherkin scenarios |
| G5 | Devon / implementer | Build |
| G6 | Owner | Acceptance |

### Where Shape Up Fits

Shape Up's shaping phase spans what in GL-024 is the pre-G2 and G2 space. Concretely:

**Shaping = pre-G2 work Phoebe already does, now named and structured.**

| Shape Up step | GL-024 equivalent | Who |
|---|---|---|
| Set boundaries (appetite) | Part of G2 brief — now explicit | Phoebe at G2 |
| Rough out elements (breadboard + fat marker) | G2 artifact — replaces or supplements markdown spec | Phoebe at G2 |
| Address rabbit holes | New addition to G2 output | Phoebe at G2 |
| Write pitch | The G2 Feature Brief, now structured as a pitch | Phoebe at G2 |

**What changes at G2:**

Currently, the G2 Feature Brief is a markdown prose document. When the feature has UI, GL-024 requires a flat HTML prototype (the "designing in the browser" path). The Shape Up insertion changes the G2 artifact as follows:

For any feature with a UI component, before Phoebe writes the flat HTML prototype or the markdown spec, she first produces:

1. A **breadboard** — interaction topology, text notation, one page maximum
2. A **fat marker sketch** — spatial layout of any panel with novel arrangement
3. An explicit **appetite** — stated in the G2 brief header: "This feature is worth a [Small Batch: X days / Big Batch: X weeks] cycle"
4. A named **rabbit holes** section — at least one, even if it is "none identified"
5. A **no-gos** section — explicit scope exclusions

The flat HTML prototype (current G2 requirement) remains unchanged. The breadboard and fat marker sketch are pre-prototype artifacts — they are produced first, approved by the owner, and then Phoebe uses them to build the prototype. The owner approves the shaped artifacts before the prototype is built.

**What does not change:**

- G3 (Kai: architecture) is unchanged. Kai receives the G2 pitch.
- G4 (Sloane: test-first) is unchanged. The pitch feeds directly into BDD scenario writing.
- G5 and G6 are unchanged.

**G2.5 (Cleo) interaction:**

G2.5 was introduced in GL-024 as a conditional gate for novel layouts where the markdown spec leaves visual decisions open for Devon to interpret. With Shape Up artifacts at G2:

- The fat marker sketch at G2 addresses the layout question that previously triggered G2.5.
- G2.5 becomes less frequently triggered because the fat marker sketch communicates spatial intent without requiring a full HTML prototype from Cleo.
- G2.5 may be reduced to: "triggered only when the owner rejects the fat marker sketch and wants a full interactive prototype before G3."

---

## 3. Breadboard in Practice — Email Management Inbox + Accordion

This section provides enough detail for Phoebe to produce a breadboard for the email management feature described in the session context.

### Step 1: Identify the places

The email management feature has two primary places:

```
Inbox (email list)
Email Detail (accordion panel)
```

Are there secondary places? Based on the feature description (inbox-style two-line email list + accordion detail panel):

```
Inbox (email list)
Email Detail — collapsed row
Email Detail — expanded accordion
Compose / Reply
```

### Step 2: Identify the affordances at each place

```
Inbox
  [Search / filter bar]
  [email row: sender, subject, snippet] --> Email Detail — expanded accordion
  [checkbox per row] --> (bulk selection state)
  [bulk action bar — Archive / Delete / Mark read] --> Inbox (updated)

Email Detail — expanded accordion
  [Collapse toggle] --> Email Detail — collapsed row
  [Reply] --> Compose / Reply
  [Archive] --> Inbox (email removed)
  [Delete] --> Inbox (email removed)
  [Mark unread] --> Inbox (row marked unread)
  [email body — full text]

Compose / Reply
  [To field]
  [Subject field (pre-filled)]
  [Body field]
  [Send] --> Inbox
  [Discard] --> Email Detail — expanded accordion
```

### Step 3: Check the topology

Reading the breadboard, a shaper asks:

- Can the user get back from every place? Yes — every terminal affordance navigates somewhere.
- Are there states not represented? The unread/read visual state is not a "place" but an attribute of the row. It does not need its own place in the breadboard unless there is a dedicated filter for it.
- Is there a place for bulk selection? The checkbox row changes the state of the inbox toolbar. This is a state, not a place. No separate node needed.

### Step 4: Fat marker sketch (spatial)

The fat marker sketch for the email management inbox:

```
+---------------------------+
|  [search bar             ]|
+---------------------------+
|  [  ] From    Subject     |  <-- collapsed row (unread: bold)
|       snippet             |
+---------------------------+
|  [  ] From    Subject     |  <-- EXPANDED ROW (accordion open)
|  +-----------------------+|
|  | Full email body here  ||
|  |                       ||
|  | [Reply] [Archive] [X] ||
|  +-----------------------+|
+---------------------------+
|  [  ] From    Subject     |
|       snippet             |
+---------------------------+
```

Notes on the fat marker sketch:
- Two-line rows with sender + subject on line 1, snippet on line 2
- Expanded row shows inline accordion — not a modal, not a separate screen
- Action buttons (Reply, Archive, Delete) live inside the expanded panel
- Only one row expands at a time (implied by the topology — clicking a new row collapses the current one)

**What the shaper does NOT decide in this sketch:**
- Column widths
- Font sizes
- Color treatment for unread rows (bold is a note, not a spec)
- Whether the accordion transition is animated
- Exact padding values

These are implementation details for Devon. The breadboard and fat marker sketch establish: what the places are, what affordances exist, and how they connect. Devon resolves the visual details.

---

## 4. Fixed Build Cycle — Duration, Scope Creep, and Done

### Cycle Length

Basecamp runs 6-week cycles for Big Batch projects and 1-2 week projects batched within a 6-week cycle for Small Batch work. The reasoning for 6 weeks (primary source, Chapter 8):

- Two-week sprints are too short. Planning overhead consumes a disproportionate share of the cycle. Sprint planning ceremonies interrupt momentum.
- Six weeks is long enough to complete meaningful work start-to-end. It is short enough that the deadline is visible from the start — teams feel the constraint and make trade-offs.

After each 6-week cycle: a 2-week cool-down. No scheduled work. Programmers fix bugs, explore ideas, recharge. The betting table for the next cycle meets during cool-down.

**For myPKA context:** The myPKA system does not run 6-week cycles. Features are built in days to weeks. The appetite concept still applies — it is the time budget set before shaping, not a fixed calendar unit. The relevant principle is: define the time budget at the start, design the solution to fit, do not extend.

### Scope Creep — The Circuit Breaker

Shape Up's answer to scope creep is the circuit breaker (primary source, Chapter 8):

> "Teams have to ship the work within the amount of time that we bet. If they don't finish, by default the project doesn't get an extension."

If the build hits the appetite ceiling and the feature is not done:

1. The project is not extended.
2. The unfinished work is returned to shaping.
3. The shaper diagnoses what went wrong — which rabbit hole was missed, which scope was underestimated.
4. A new pitch is written with a revised approach.
5. The revised pitch goes to the next betting table.

The circuit breaker has three functions:
- Eliminates runaway projects — one feature cannot consume unlimited cycles.
- Forces re-shaping — if time ran out, the shaping was wrong. Fix the shaping, not the schedule.
- Gives the team real authority — they own the scope trade-offs within the cycle. No one extends from outside.

**Scope hammering during the cycle:**

When scope threatens to exceed the appetite during the build, the team "hammers" scope down. This means:

- Identifying what is essential (the core use case)
- Identifying what is peripheral (nice-to-have)
- Cutting the peripheral without seeking approval for each cut
- The shaped pitch's no-gos list pre-authorizes most of these cuts

### Done

Done means deployed (primary source, Chapter 10):

> "At the end of the cycle, the team will deploy their work."

Testing and QA happen inside the cycle — not after. The team scopes off the essential aspects early, finishes them, and coordinates QA within the budget.

Done does not mean "all originally imagined features are built." Done means: the core use case works, it is shipped, and the cycle is closed.

---

## 5. Recommendation — Wholesale vs. Selective Adoption

### Assessment

Shape Up is designed for a team of 3-6 people running parallel build tracks with a dedicated shaping track that runs separate from the build track. The myPKA system has a different structure: a single owner with AI specialists executing gates sequentially. There is no parallel shaping track. There is no betting table with multiple stakeholders.

Adopting Shape Up wholesale — including 6-week cycles, cool-down periods, and a formal betting table — would impose structure that does not match the system's scale or operating rhythm.

### What Should Be Extracted

Three Shape Up conventions provide direct, high value for myPKA with minimal adoption cost:

**Convention 1: Appetite at G2 (high value, zero cost)**

Every G2 Feature Brief must open with an explicit appetite: "This feature is worth [N days] of build time." This single sentence changes how Phoebe scopes the solution and how Devon plans the build. It pre-authorizes scope cuts and eliminates the "this is taking longer than expected" ambiguity. Currently, GL-024 has no appetite declaration. Add it.

**Convention 2: Breadboard before prototype at G2 (high value, low cost)**

For any feature with interaction flow across multiple places or states, Phoebe produces a breadboard before building the flat HTML prototype. The breadboard takes 15-30 minutes. It gives the owner a lightweight artifact to approve before the 4-hour prototype investment. It prevents building the wrong interaction structure. The breadboard replaces the current "write a markdown spec, then maybe build a prototype" sequence with "sketch the topology first, then build the prototype based on the approved topology."

**Convention 3: Rabbit holes and no-gos section in the G2 pitch (medium value, low cost)**

The current G2 Feature Brief has no formal section for known risks or explicit scope exclusions. Shape Up makes these first-class sections. Add them to the G2 Feature Brief template. This prevents Devon from discovering scope ambiguity at G5 and routing back to Phoebe for clarification — a common cause of delay in the current pipeline.

### What to Leave Out

- 6-week cycles: not applicable. The system uses feature-by-feature delivery.
- Cool-down: not applicable for the same reason.
- Betting table: the owner is the sole decision-maker and approves at G2 and G6. No table needed.
- Shaping track / build track separation: the system does not have parallel tracks. Phoebe shapes at G2. Devon builds at G5. The gates are already sequential.
- Hill charts: progress tracking tool for multi-week cycles. Not applicable at current feature scale.

### Implementation Proposal for GL-024

Insert the following changes into GL-024 at G2:

1. **G2 Artifact requirement (all UI features):**
   - Step 1: Breadboard (text notation, places + affordances + connections) — 15-30 min
   - Step 2: Fat marker sketch (for features with novel spatial layout) — 15-30 min
   - Step 3: Owner approves breadboard and sketch before Phoebe builds the HTML prototype
   - Step 4: Flat HTML prototype (existing requirement, unchanged)
   - Step 5: Owner approves prototype (existing requirement, unchanged)

2. **G2 Feature Brief template additions:**
   - Appetite: [N days or "undefined — needs scoping"]
   - Rabbit holes: [list known risks or "none identified"]
   - No-gos: [explicit exclusions]

3. **Circuit breaker rule (new hard rule in GL-024):**
   - If a G5 build exceeds the stated appetite by more than 50%, Devon routes back to Phoebe rather than continuing. Phoebe re-shapes the remaining scope and produces a new G2 brief for the next cycle.

---

## Sources

All content is sourced from the Shape Up online book by Ryan Singer, published by Basecamp. Read directly.

| Chapter | URL | Status |
|---|---|---|
| Chapter 1: Introduction | https://basecamp.com/shapeup/0.3-chapter-01 | Read directly |
| Chapter 2: Principles of Shaping | https://basecamp.com/shapeup/1.1-chapter-02 | Read directly |
| Chapter 3: Set Boundaries | https://basecamp.com/shapeup/1.2-chapter-03 | Read directly |
| Chapter 4: Find the Elements | https://basecamp.com/shapeup/1.3-chapter-04 | Read directly |
| Chapter 5: Risks and Rabbit Holes | https://basecamp.com/shapeup/1.4-chapter-05 | Read directly |
| Chapter 7: Bets, Not Backlogs | https://basecamp.com/shapeup/2.1-chapter-07 | Read directly |
| Chapter 8: The Betting Table | https://basecamp.com/shapeup/2.2-chapter-08 | Read directly |
| Chapter 10: Hand Over Responsibility | https://basecamp.com/shapeup/3.1-chapter-09 | Read directly |
| Chapter 11: Get One Piece Done | https://basecamp.com/shapeup/3.2-chapter-10 | Read directly |

Chapter 6 (Write the Pitch) returned HTTP 404 at time of research. The five pitch sections described in this brief are sourced from Chapters 2 and 5 where they are referenced explicitly. The pitch structure is directional for the no-gos and rabbit holes sections; the core three sections (problem, appetite, solution) are primary-source confirmed.

---

## Directional Findings

The following claims are based on industry-level usage of Shape Up outside Basecamp, not on primary source content from the book:

- (directional — based on industry adoption reports) Many teams using Shape Up reduce their scope creep incidents by removing the backlog entirely. This is consistent with the book's argument but is not a claim Basecamp makes with data.
- (directional — based on community reports) Teams smaller than 3 people sometimes collapse the shaping and building tracks — one person shapes and builds. The book assumes separation of these tracks.

---

## Open Questions for Phoebe and Sloane

1. Should the breadboard be a formal deliverable stored in the Deliverables folder, or is it a throwaway pre-artifact that informs the prototype? Shape Up treats it as throwaway. GL-024's "frozen design" principle suggests storing it. Decide before implementing.

2. Who de-risks rabbit holes for features that touch backend data? Phoebe shapes the UI and interaction. Kai owns architecture. The current pipeline runs Phoebe before Kai. A rabbit hole that requires a backend constraint check cannot be fully addressed by Phoebe alone. Consider whether the G2 rabbit holes section triggers an async check from Kai before G2 passes.

3. Appetite for small batch features in myPKA: is the right unit "days" or "hours"? The email management feature ran across multiple sessions. If appetite is stated in hours, it creates a more meaningful constraint for AI-assisted builds.

---

**This belongs in:** Team Knowledge / Core (system methodology reference, feeds GL-024 revision)

**Route to:** Phoebe (G2 artifact protocol changes) + Sloane (G4 receives richer pitch, no structural change needed) + Larry (GL-024 revision proposal)
