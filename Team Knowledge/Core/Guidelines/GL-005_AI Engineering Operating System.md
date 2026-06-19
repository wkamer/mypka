# GL-005 — AI Engineering Operating System

**Scope:** Full AI team
**Maintainer:** Larry
**Status:** Active

---

## Core principle

Never start directly with code.

Always follow this sequence:

1. Understand
2. Specify
3. Define tests
4. Implement minimally
5. Validate automatically
6. Review
7. Refactor
8. Deliver

---

## Mandatory engineering flow

### Step 1. Requirement analysis

Before writing code, the following must be clear:

- What the system must do
- Why it exists
- What input is expected
- What output is expected
- What rules apply
- What edge cases exist
- What success means
- What errors must be handled

Always use this structure:

```
Feature:
Purpose:
Inputs:
Outputs:
Business Rules:
Edge Cases:
Dependencies:
Risks:
Definition of Done:
```

If requirements are unclear:
- Do not guess
- Do not present assumptions as facts
- Mark assumptions explicitly
- Clarify first where needed

### Step 2. Test-first thinking

Before implementation starts:
- Design tests first
- Define behavior first
- Determine validation first
- Describe failure scenarios first

Always answer:
- How do we prove this works correctly?
- How do we detect regressions?
- Which scenarios can break?

### Step 3. Minimal implementation

After defining tests:
- Build only the minimal implementation
- No overengineering
- No premature abstractions
- No unnecessary frameworks
- No speculative future features

Prefer: Simple, readable, modular, explicit, predictable.

Apply: KISS, SOLID, Separation of concerns, Bounded contexts.

Avoid: Magic behavior, hidden dependencies, large monolithic scripts, duplicated logic.

### Step 4. Validation

Minimum checks: tests, linting, typing, formatting, runtime validation, API contract validation.

**Python standard:** pytest, mypy, ruff
**Node standard:** tests, eslint, typescript validation

A script that runs is not automatically correct. Everything must demonstrably work in a reproducible way.

### Step 5. Review

Critically assess every delivery on: simplicity, maintainability, modularity, security, scalability, error handling, logging, performance, technical debt.

Always ask: Can this be simpler? Can this be safer? Can this be smaller? Can this be clearer?

### Step 6. Refactor

After successful validation: improve structure, reduce duplication, improve naming, split responsibilities.

Refactors must not change behavior. Tests must detect regressions.

---

## Team role system

| Role | Responsibility |
|---|---|
| Architect | System structure, interfaces, boundary enforcement |
| Engineer | Implementation, clean code, error handling |
| QA | Tests, edge cases, regressions, behavior validation |
| Reviewer | Code quality, SOLID, KISS, maintainability |
| Security | Secrets, permissions, API safety, risk analysis |
| DevOps | Pipelines, deployment, CI/CD, observability |

---

## Development rules

**Always:** Work iteratively and modularly, document decisions, log important actions, use clear interfaces, keep responsibilities small.

**Never:** Generate large systems directly, combine features without reason, hide business logic, modify production without validation, present assumptions as facts, add smart magic without necessity.

**Context hygiene:** See SOP-014 Claude Code session context hygiene. Compact proactively. Never reach 1M tokens. Deliverables to file; chat returns path, status, summary, deviations, blockers, next step only.

---

## Diagnostic discipline

When a system component behaves unexpectedly — a log file is empty, a script produces no output, a backup is missing, a service does not respond — the mandatory first step is always a read-only investigation to confirm the cause.

Rules:
- No fix may be proposed until the cause is confirmed.
- No script, configuration or system file may be modified based on a hypothesis alone.
- Investigation output: a short finding report stating the confirmed cause.
- If the cause cannot be confirmed in a read-only pass: classify as "requires deeper investigation" and defer. Do not proceed to a fix.
- This rule applies to every technical agent on every unexpected infrastructure finding.

---

## Post-Check Script Standards

Post-check scripts verify that a write action produced the expected outcome. These rules apply to every post-check script written or reviewed by any agent.

### Scope targeting

A post-check must target the specific section or lines relevant to the change — not the full file.

- Full-file string matching is not permitted as a post-check method.
- Each check must be scoped to the smallest relevant unit: a section, a named block, a defined line range.
- Rationale: full-file matching produces false FAIL results when unrelated content elsewhere in the file contains overlapping strings. (Source: LC-5a)

### Format matching

A post-check must match the exact notation used in the target document.

- Before writing regex or string checks: confirm whether the target document uses single quotes, backtick notation, bold markers, or plain text for the expected value.
- A check that searches for `'triaged'` will produce silent False negatives if the document renders `` `triaged` ``.
- Rationale: notation mismatch produces silent false negatives — the check passes, the error is undetected. (Source: LC-5b)

### Code structure independence

A post-check must not assume the order of branches, conditions, or blocks in a function body.

- Do not write regex that depends on one branch appearing before another (e.g. reject before escalate).
- Instead: extract the target function or block text first, then apply checks within that extracted scope.
- Use explicit named-group matching where branch identity matters.
- Rationale: branch order may differ between a write plan and the written file; an order-dependent regex produces silent False negatives without any FAIL signal. (Source: LC-7a)

---

## Production safety

Never work directly on production without: validation, tests, rollback capability, logging, error handling.

Use first: sandbox, staging, mocks, test accounts.

Exercise extra caution with: Shopify, Meta, Gmail, Discord, Telegram, financial systems.

---

## Definition of Done

Work is only done when:

- Requirements are clear
- Tests exist and pass
- Linting and typing pass
- Logging is present
- Edge cases are handled
- Documentation is updated
- Code review has been performed
- Implementation works reproducibly

---

## Long-term goal

Build reliable systems. Create scalable architecture. Achieve knowledge retention. Minimize technical debt. Deliver consistent engineering quality. Build a mature AI-first engineering organization.

Every decision contributes to: stability, overview, reliability, maintainability, scalability.

---

## SSOT — Content routing

Every agent checks when processing content: does this belong to a project?

- **Project content** → `PKM/My Life/Projects/P-Naam/` (personal) or `Team Knowledge/<domain>/` (business)
- **Personal profile / self-knowledge** → `PKM/Documents/Key Elements/KE-Self/what-about-me.md`
- **Team workflows and formats** → `Team Knowledge/Core/Guidelines/GL-NNN_*.md`
- **Inbox** is a pass-through location, not SSOT — never a final destination

On project close: sweep all loose content into the project folder before archiving. Information must remain findable even after a project is complete.

---

## Changelog

- 2026-06-03 (Larry, B-030B): Fully translated from Dutch to English. No functional changes to existing rules. Diagnostic Discipline section added (B-030 Candidate 2, Option B approved). Maintainer field updated (Bewaker → Maintainer). Changelog section added. Footer metadata removed (non-functional; Maintainer already in header). Approved by Owner Walter Kamer.
- 2026-06-03 (Larry, B-031B): Context hygiene pointer added to Development rules. References SOP-014. Approved by Owner Walter Kamer.
- 2026-06-07 (Larry, SOP-019 Track 1): Post-Check Script Standards section added. Covers scope targeting, format matching, and code structure independence. Sources: LC-5 (post-check scope and notation fragility) and LC-7 (branch-order-dependent regex). Approved by Owner.
