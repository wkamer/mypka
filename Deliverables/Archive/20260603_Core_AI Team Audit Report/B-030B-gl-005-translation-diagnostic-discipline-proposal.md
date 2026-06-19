# B-030B GL-005 English Translation + Diagnostic Discipline Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Based on:** B-030 Graduation Candidate Triage, B-030A Rule Promotion Proposal (Option B selected)

---

## 1. Purpose

GL-005 — AI Engineering Operating System is the team's engineering operating guideline. It covers the full AI team scope and defines mandatory engineering flow, development rules, production safety, and content routing.

GL-005 is currently written entirely in Dutch, which violates GL-014 v1.2 §10 (System File Language Rule). In B-030A, Owner Walter Kamer selected Option B: translate GL-005 fully to English first, then add the Diagnostic Discipline section from B-030 Candidate 2.

This proposal provides the complete exact English replacement for GL-005, including the Diagnostic Discipline section, for Owner review and approval before any execution.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| All system files must be written in English | GL-014 v1.2 §10 |
| Guidelines are critical files — may never be modified without Owner approval | GL-014 v1.2 §8 |
| Guideline executor: Larry/Nolan. Reviewer: Larry. Final approval: Owner | GL-014 v1.2 §9 |
| Every GL change includes a changelog entry | GL-014 v1.2 §5 |
| Audit trail: changelog in file, team_log entry, session log | GL-014 v1.2 §6 |
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |
| Owner = Walter Kamer | GL-014 v1.2 Owner definition |
| Graduation candidate Candidate 2 selected destination: GL-005, Option B | B-030A §5.5 |

---

## 3. Scope

**Included:**
- Full English translation of all Dutch content in GL-005
- Maintainer terminology correction (`Bewaker` → `Maintainer`)
- Diagnostic Discipline section added using the rule text from B-030A §5.7
- Missing `## Changelog` section added (required by GL-014 §5)
- Double `---` separator artifact removed (formatting cleanup, no content impact)

**Excluded:**
- Content changes to existing rules — meaning is preserved exactly
- Changes to any other GL or system file
- B-021B execution
- B-021C execution
- Any modification to AGENT.md files, SOPs, CLAUDE.md, or databases

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `Read` on `Team Knowledge/Core/Guidelines/GL-005_AI Engineering Operating System.md` — full content (183 lines)
- Cross-reference against GL-014 §5 (Changelog requirement) and §10 (Language rule)
- Cross-reference against B-030A §5.7 (exact Diagnostic Discipline rule text)

No files were modified. No database writes were performed.

---

## 5. Current GL-005 State

**Language:** Entirely Dutch, except for:
- Section heading `## Mandatory engineering flow` — already English
- Step headings `### Step 1.` through `### Step 6.` — already English
- Code block fields (`Feature:`, `Purpose:`, `Inputs:`, etc.) — already English
- Tool names (`pytest, mypy, ruff, eslint`) — language-neutral
- Methodology terms (`KISS, SOLID, CI/CD, observability`) — language-neutral

**Structure:**
1. Header metadata (Dutch field labels)
2. Core principle (Dutch body)
3. Mandatory engineering flow — Steps 1–6 (English headings, Dutch body)
4. Team role system (Dutch table)
5. Development rules (Dutch Always/Never)
6. Production safety (Dutch)
7. Definition of Done (Dutch)
8. Long-term goal (Dutch)
9. SSOT — Content routing (Dutch)
10. Footer metadata (Dutch)

**Missing:** No `## Changelog` section (required by GL-014 §5).

**Formatting artifact:** Lines 164–166 contain two consecutive `---` separators. The proposed replacement removes the duplicate.

**Maintainer terminology:** Current file uses `**Bewaker:** Larry`. Correct term is `**Maintainer:** Larry` per audit conventions.

---

## 6. Proposed GL-005 Replacement

The section below contains the complete exact proposed content for GL-005. Every existing Dutch sentence is translated to English. No rule meaning is changed. The Diagnostic Discipline section is added between Development rules and Production safety. A Changelog section is added at the end.

---

**Complete proposed file content:**

```markdown
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

A script that runs is not automatically correct. Everything must demonstrably work in a
reproducible way.

### Step 5. Review

Critically assess every delivery on: simplicity, maintainability, modularity, security,
scalability, error handling, logging, performance, technical debt.

Always ask: Can this be simpler? Can this be safer? Can this be smaller? Can this be clearer?

### Step 6. Refactor

After successful validation: improve structure, reduce duplication, improve naming, split
responsibilities.

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

**Always:** Work iteratively and modularly, document decisions, log important actions, use
clear interfaces, keep responsibilities small.

**Never:** Generate large systems directly, combine features without reason, hide business
logic, modify production without validation, present assumptions as facts, add smart magic
without necessity.

---

## Diagnostic discipline

When a system component behaves unexpectedly — a log file is empty, a script produces no
output, a backup is missing, a service does not respond — the mandatory first step is always
a read-only investigation to confirm the cause.

Rules:
- No fix may be proposed until the cause is confirmed.
- No script, configuration or system file may be modified based on a hypothesis alone.
- Investigation output: a short finding report stating the confirmed cause.
- If the cause cannot be confirmed in a read-only pass: classify as "requires deeper
  investigation" and defer. Do not proceed to a fix.
- This rule applies to every technical agent on every unexpected infrastructure finding.

---

## Production safety

Never work directly on production without: validation, tests, rollback capability, logging,
error handling.

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

Build reliable systems. Create scalable architecture. Achieve knowledge retention. Minimize
technical debt. Deliver consistent engineering quality. Build a mature AI-first engineering
organization.

Every decision contributes to: stability, overview, reliability, maintainability,
scalability.

---

## SSOT — Content routing

Every agent checks when processing content: does this belong to a project?

- **Project content** → `PKM/My Life/Projects/P-Naam/` (personal) or
  `Team Knowledge/<domain>/` (business)
- **Personal profile / self-knowledge** →
  `PKM/Documents/Key Elements/KE-Self/what-about-me.md`
- **Team workflows and formats** → `Team Knowledge/Core/Guidelines/GL-NNN_*.md`
- **Inbox** is a pass-through location, not SSOT — never a final destination

On project close: sweep all loose content into the project folder before archiving.
Information must remain findable even after a project is complete.

---

## Changelog

- 2026-06-03 (Larry, B-030B): Fully translated from Dutch to English. No functional changes.
  Diagnostic Discipline section added (B-030 graduation candidate, Option B). Maintainer
  field updated from Bewaker. Changelog section added. Approved by Owner Walter Kamer.
```

---

## 7. Diagnostic Discipline Placement

The Diagnostic Discipline section is placed between `## Development rules` and `## Production safety`.

**Rationale:**

- Development rules (broad engineering principles — always/never) → sets the general operating mindset
- **Diagnostic Discipline** (specific investigative protocol for unexpected behavior) → extends Development rules with a precise diagnostic constraint
- Production safety (deployment and production-environment rules) → governs how to act safely in production

This placement is natural because Diagnostic Discipline is a tightening of the Development rules principle "Never modify production without validation" — it specifies what to do when something behaves unexpectedly, before any modification is considered. It is not a production-deployment rule, so it belongs before Production safety, not after.

The section is self-contained: it does not duplicate any existing rule and does not modify any surrounding content.

---

## 8. Risk Assessment

### Translation drift

**Risk:** A translation that shifts the meaning of an existing rule.

**Mitigation applied:** Each sentence was translated conservatively, preserving the original intent. Where Dutch terms had direct English equivalents (e.g. `Bewaker` → `Maintainer`, `rust` → `stability`), the most semantically precise translation was chosen. No rules were added, removed, or reordered among the existing content.

**Specific translation decision notes:**

| Dutch | English used | Reason |
|---|---|---|
| `Volledig AI team` | `Full AI team` | Direct |
| `Bewaker` | `Maintainer` | Audit terminology (per B-022 conventions) |
| `Actief` | `Active` | Direct |
| `Begrijpen` | `Understand` | Direct |
| `Opleveren` | `Deliver` | Standard engineering term |
| `Grenzen bewaken` | `boundary enforcement` | Preserves the active/protective intent |
| `Foutafhandeling` | `error handling` | Standard engineering term |
| `Gedragsvalidatie` | `behavior validation` | Direct |
| `Technische schuld` | `technical debt` | Standard engineering term |
| `Rust` | `stability` | `rust` (calm/tranquility) in an engineering context maps to stability |
| `Overzicht` | `overview` | Direct — retaining as-is fits the original intent |
| `Kennis borging realiseren` | `Achieve knowledge retention` | `borging` = securing/anchoring; `kennis borging` = preserving accumulated knowledge |
| `Doorvoerlocatie` | `pass-through location` | Direct — inbox is a transient stop, not storage |

**Risk level:** Low. Each translation was verified against the original Dutch meaning.

---

### Behavior change

**Risk:** An agent changes its behavior based on a reworded rule.

**Mitigation:** No existing rules were changed in substance. The only new content is the Diagnostic Discipline section (already approved as a graduation candidate). Terminology corrections (`Bewaker` → `Maintainer`, `Actief` → `Active`) are metadata labels, not behavioral instructions.

**Risk level:** Low. The Diagnostic Discipline section changes behavior intentionally — agents are now explicitly required to investigate before fixing. This is the purpose of promoting the graduation candidate.

---

### Language compliance

**Risk:** Residual Dutch in the translated file.

**Items deliberately preserved in original form:**

| Item | Reason |
|---|---|
| `P-Naam/` in SSOT routing table | GL-001 Dutch naming convention — preserved pending GL-001 translation (see team_tasks id 63) |
| Tool names: `pytest, mypy, ruff, eslint` | Language-neutral; not Dutch |
| Methodology terms: `KISS, SOLID, CI/CD, observability` | Language-neutral acronyms/borrowed terms |

No other Dutch words or phrases remain in the proposed replacement.

**Risk level:** Low. One convention reference preserved intentionally and documented.

---

### Engineering rule impact

**Risk:** The Diagnostic Discipline section introduces an obligation that blocks legitimate quick fixes.

**Assessment:** The rule requires a read-only investigation before proposing a fix — it does not prohibit fixes. The investigation step produces a short finding report. For clear and obvious issues (e.g. a typo in a script), the investigation is trivially fast. The rule only introduces meaningful friction when the cause is genuinely unknown, which is exactly the scenario where a rushed fix creates additional risk.

**Risk level:** Low. The rule is a diagnostic discipline, not a work blocker.

---

## 9. Post-Checks

After execution:

| Check | What to verify |
|---|---|
| Header | `**Scope:** Full AI team`, `**Maintainer:** Larry`, `**Status:** Active` present |
| Core principle | 8-step list in English |
| Step 1–6 headings | Unchanged (`### Step 1. Requirement analysis` etc.) |
| Step 1–6 body | All Dutch replaced with English |
| Team role system | Table headers: `Role` / `Responsibility` |
| Development rules | `**Always:**` and `**Never:**` in English |
| Diagnostic Discipline section | Present between Development rules and Production safety |
| Diagnostic Discipline rule text | Matches B-030A §5.7 exactly |
| Production safety | Fully English |
| Definition of Done | 8 bullets in English |
| Long-term goal | Fully English |
| SSOT — Content routing | Fully English; `P-Naam/` preserved as convention reference |
| Changelog section | Present at end of file |
| Changelog entry | Contains `B-030B`, date, agent, description |
| No Dutch system instructions remaining | Verify with grep |
| Double `---` artifact removed | Confirm only one `---` between Long-term goal and SSOT |
| No secrets or credential values | Confirm file contains no secrets |

---

## 10. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve this proposal for execution? | a) Approve b) Request content edits c) Defer | Determines whether GL-005 translation + Diagnostic Discipline proceeds |
| 2 | Confirm the exact Diagnostic Discipline rule text in §6? | a) Approve as written b) Request edits | Text in §6 will be used verbatim; edits require a revised proposal |
| 3 | Confirm translation choices are acceptable? | a) Approve b) Flag specific translations for review | Any translation objection should be noted before execution |
| 4 | Confirm `rust` → `stability` as the correct translation for long-term goal? | a) Confirm b) Alternative (`calm`, `peace of mind`, other) | Single word; low impact; noted for explicit Owner confirmation |
| 5 | Should `P-Naam/` in the SSOT routing table be translated now or preserved as GL-001 convention? | a) Preserve as convention reference (recommended) b) Translate now | If b): would require consistent update to GL-001 and any file referencing this path pattern — out of scope for B-030B |

---

## 11. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. No database rows have been written. The exact GL-005 replacement content in §6 is proposed content only — it is not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of B-030B is an approval of the exact content provided in §6. Any content change after approval requires a separate approval before execution.

---

## 12. Final Recommendation

GL-005 is the AI Engineering Operating System. It is short, fully Dutch, and already non-compliant with GL-014 §10. The translation is exact, conservative, and preserves every existing rule. The Diagnostic Discipline section adds a standing engineering discipline that was already applied in practice during the B-021 audit.

The proposed replacement in §6 is complete and execution-ready. Owner Walter Kamer reviews §6, confirms the translation and Diagnostic Discipline content, and approves for execution. The execution pass is a single Write operation replacing the file, followed by a read-back and audit trail.

B-021B (logging investigation) and B-021C (credential recovery proposal) can proceed in parallel — they do not depend on GL-005 being translated.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-030B-gl-005-translation-diagnostic-discipline-proposal.md`*
