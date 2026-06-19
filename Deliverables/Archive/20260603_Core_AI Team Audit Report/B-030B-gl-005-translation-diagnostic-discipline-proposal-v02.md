# B-030B GL-005 English Translation + Diagnostic Discipline Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Supersedes:** B-030B v0.1 (2026-06-03)
**Based on:** B-030 Graduation Candidate Triage, B-030A Rule Promotion Proposal (Option B selected)

---

## Change Log (v0.1 → v0.2)

| # | Correction applied |
|---|---|
| 1 | Removed casual "single Write operation" language from §12; execution method now stated as controlled read-before-write, exact approved content, full read-back, and post-checks |
| 2 | Footer metadata explicitly identified and addressed in §5 and §6; removal justified |
| 3 | Translation integrity check table added to §6; explicit confirmation that no rule is removed, no rule meaning is changed, Diagnostic Discipline is the only new behavioral rule, Changelog is the only new governance section, `P-Naam/` is the only preserved Dutch convention |
| 4 | Diagnostic Discipline content unchanged |
| 5 | Candidate 1 (GL-014) explicitly excluded — B-030A is complete |
| 6 | B-021B and B-021C explicitly excluded |

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
- Maintainer terminology correction (`**Bewaker:**` → `**Maintainer:**`)
- Diagnostic Discipline section added between Development rules and Production safety, using rule text from B-030A §5.7
- Missing `## Changelog` section added (required by GL-014 §5)
- Footer metadata lines removed — see §5 for explicit justification
- Double `---` separator artifact removed (lines 164–166 in current file — formatting cleanup, no content impact)

**Excluded:**
- Content changes to existing rules — meaning is preserved exactly
- Any modification to GL-014 — B-030A Candidate 1 is already complete
- Any modification to GL-005, GL-001, or other GL files (in this pass)
- B-021B execution
- B-021C execution
- Any change to AGENT.md files, SOPs, CLAUDE.md, or databases
- Registration of new backlog items

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `Read` on `Team Knowledge/Core/Guidelines/GL-005_AI Engineering Operating System.md` — full content (183 lines)
- Cross-reference against GL-014 §5 (Changelog requirement) and §10 (Language rule)
- Cross-reference against B-030A §5.7 (exact Diagnostic Discipline rule text)

No files were modified. No database writes were performed.

---

## 5. Current GL-005 State

### Language

GL-005 is entirely in Dutch, except for:
- Section heading `## Mandatory engineering flow` — already English
- Step headings `### Step 1.` through `### Step 6.` — already English
- Code block fields (`Feature:`, `Purpose:`, `Inputs:`, etc.) — already English
- Tool names (`pytest, mypy, ruff, eslint`) — language-neutral
- Methodology terms (`KISS, SOLID, CI/CD, observability`) — language-neutral

### Structure (current file)

| Section | Lines | Language |
|---|---|---|
| Header metadata | 1–6 | Dutch (`Volledig AI team`, `Bewaker`, `Actief`) |
| Core principle | 9–22 | Dutch body |
| Mandatory engineering flow (Steps 1–6) | 26–109 | English headings, Dutch body |
| Team role system | 112–121 | Dutch table body |
| Development rules | 125–129 | Dutch |
| Production safety | 133–139 | Dutch |
| Definition of Done | 143–154 | Dutch |
| Long-term goal | 158–162 | Dutch |
| Double `---` separator | 164–166 | Formatting artifact |
| SSOT — Content routing | 168–177 | Dutch |
| Footer metadata | 181–182 | Dutch (see below) |

### Footer metadata — explicit identification

The current file ends with two footer lines:

```
*Opgesteld door owner — 2026-05-17*
*Bewaakt door Larry*
```

- `*Opgesteld door owner — 2026-05-17*` means "Created by owner — 2026-05-17." This records the original authorship date.
- `*Bewaakt door Larry*` means "Maintained by Larry." This duplicates the `**Bewaker:** Larry` header field.

**Proposed handling:** Remove both footer lines. Justification:
1. The Maintainer field in the header (`**Maintainer:** Larry`) already captures the guardian information. The footer line is redundant.
2. The creation date (2026-05-17) is a one-time fact about original authorship. It is not a governance requirement. Its loss is acceptable because: (a) it is not referenced by any agent, (b) the Changelog section being added will record all future changes, (c) the creation date can be inferred from session logs if needed.
3. Other GL files (GL-014) do not use this footer pattern — they use only a Changelog section. Removing the footer aligns GL-005 with the established pattern.

**No functional impact.** No agent reads or depends on these footer lines.

### Missing governance elements

- No `## Changelog` section — required by GL-014 §5.

### Formatting artifact

Lines 164–166 contain two consecutive `---` separators. The proposed replacement removes the duplicate.

---

## 6. Proposed GL-005 Replacement

### 6.1 Translation integrity checks

Before reviewing the proposed content, the following confirms what this replacement does and does not change:

| Control | Status |
|---|---|
| No existing engineering rule removed | ✓ Verified — all 6 steps, Development rules, Production safety, Definition of Done, Long-term goal, and SSOT routing are present in the replacement |
| No existing engineering rule meaning changed | ✓ Verified — see translation decision notes in §8 |
| Diagnostic Discipline is the only new behavioral rule | ✓ Only new section between Development rules and Production safety |
| `## Changelog` is the only new governance metadata section | ✓ No other new sections added |
| Maintainer terminology corrected (`Bewaker` → `Maintainer`) | ✓ Applied in header |
| Footer metadata removed with justification | ✓ Justified in §5 |
| `P-Naam/` is the only preserved Dutch-looking naming convention | ✓ All other Dutch content is translated; `P-Naam/` preserved as GL-001 convention reference (see §8) |
| No new Dutch content introduced | ✓ |
| GL-014 not modified | ✓ B-030A Candidate 1 is already complete |
| B-021B and B-021C not in scope | ✓ |

### 6.2 Complete proposed file content

The block below is the exact proposed content for GL-005 after execution. It is the full replacement — every line is shown.

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

Minimum checks: tests, linting, typing, formatting, runtime validation, API contract
validation.

**Python standard:** pytest, mypy, ruff
**Node standard:** tests, eslint, typescript validation

A script that runs is not automatically correct. Everything must demonstrably work in a
reproducible way.

### Step 5. Review

Critically assess every delivery on: simplicity, maintainability, modularity, security,
scalability, error handling, logging, performance, technical debt.

Always ask: Can this be simpler? Can this be safer? Can this be smaller? Can this be
clearer?

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

- 2026-06-03 (Larry, B-030B): Fully translated from Dutch to English. No functional changes
  to existing rules. Diagnostic Discipline section added (B-030 Candidate 2, Option B
  approved). Maintainer field updated (Bewaker → Maintainer). Changelog section added.
  Footer metadata removed (non-functional; Maintainer already in header). Approved by Owner
  Walter Kamer.
```

---

## 7. Diagnostic Discipline Placement

The Diagnostic Discipline section is placed between `## Development rules` and `## Production safety`.

**Rationale:** Development rules establish the broad engineering mindset (always/never). Diagnostic Discipline tightens that mindset with a specific protocol for unexpected behavior — it is a precision extension of "Never modify production without validation." It belongs before Production safety because it governs the investigative step that must precede any decision about whether to modify anything, in production or otherwise. The section is self-contained and does not duplicate or weaken any surrounding content.

---

## 8. Risk Assessment

### Translation drift

**Risk:** A translation that shifts the meaning of an existing rule.

**Translation decision notes:**

| Dutch | English used | Reason |
|---|---|---|
| `Volledig AI team` | `Full AI team` | Direct |
| `Bewaker` | `Maintainer` | Audit terminology (B-022 conventions); header field, not behavioral |
| `Actief` | `Active` | Direct |
| `Begrijpen` | `Understand` | Direct |
| `Opleveren` | `Deliver` | Standard engineering term |
| `Grenzen bewaken` | `boundary enforcement` | Preserves the active/protective intent |
| `Foutafhandeling` | `error handling` | Standard engineering term |
| `Gedragsvalidatie` | `behavior validation` | Direct |
| `Technische schuld` | `technical debt` | Standard engineering term |
| `Rust` | `stability` | `rust` (calm/tranquility) in an engineering context maps closest to stability; flagged for explicit Owner confirmation |
| `Overzicht` | `overview` | Direct; retained as-is |
| `Kennis borging realiseren` | `Achieve knowledge retention` | `borging` = securing/anchoring accumulated knowledge |
| `Doorvoerlocatie` | `pass-through location` | Direct — inbox as transient stop, not storage |
| `P-Naam/` | Preserved | GL-001 Dutch naming convention; only preserved Dutch item; consistent with B-005A approval |

**Risk level:** Low. Each translation was verified against the original Dutch meaning. No substantive change to any rule.

---

### No-removal and no-meaning-change verification

The following table confirms that every existing GL-005 section is present in the replacement with meaning preserved:

| Existing section | Present in replacement | Meaning changed |
|---|---|---|
| Core principle (8-step sequence) | ✓ | No |
| Step 1 Requirement analysis | ✓ | No |
| Step 2 Test-first thinking | ✓ | No |
| Step 3 Minimal implementation | ✓ | No |
| Step 4 Validation | ✓ | No |
| Step 5 Review | ✓ | No |
| Step 6 Refactor | ✓ | No |
| Team role system | ✓ | No |
| Development rules (Always/Never) | ✓ | No |
| Production safety | ✓ | No |
| Definition of Done | ✓ | No |
| Long-term goal | ✓ | No |
| SSOT — Content routing | ✓ | No |
| Footer metadata lines | Removed | Non-functional; justified in §5 |
| Double `---` separator | Removed | Formatting artifact; no content |

---

### Behavior change

**Risk:** An agent changes its behavior based on a reworded rule.

**Assessment:** No existing rule is changed in substance. The Diagnostic Discipline section introduces one intentional behavior change: agents are now explicitly required to investigate before fixing. This is the purpose of promoting the graduation candidate.

**Risk level:** Low for existing rules. Intentional for Diagnostic Discipline.

---

### Language compliance

**Risk:** Residual Dutch in the translated file.

**Only preserved Dutch-looking item:** `P-Naam/` in the SSOT routing table — GL-001 Dutch naming convention, preserved for consistency pending GL-001 translation (team_tasks id 63). No other Dutch words or phrases remain.

**Risk level:** Low. One convention reference preserved and documented.

---

### Engineering rule impact

**Risk:** Diagnostic Discipline blocks legitimate quick fixes.

**Assessment:** The rule requires a read-only investigation before proposing a fix — it does not prohibit fixes. For obvious issues, the investigation is trivially fast. The rule introduces meaningful friction only when the cause is genuinely unknown, which is exactly the scenario where a rushed fix creates risk.

**Risk level:** Low.

---

## 9. Post-Checks

After execution, verify:

| Check | What to confirm |
|---|---|
| Header: `**Scope:** Full AI team` | Present |
| Header: `**Maintainer:** Larry` | Present (not `Bewaker`) |
| Header: `**Status:** Active` | Present (not `Actief`) |
| Core principle | 8-step list in English |
| Step 1–6 headings | Unchanged (`### Step 1. Requirement analysis` etc.) |
| Step 1–6 body text | All Dutch replaced with English |
| Team role system | Table headers: `Role` / `Responsibility` |
| Development rules | `**Always:**` and `**Never:**` in English |
| Diagnostic Discipline section | Present between Development rules and Production safety |
| Diagnostic Discipline rule text | Matches B-030A §5.7 exactly — five bullet rules present |
| No existing rule removed | Spot-check: all 6 steps, Development rules, Production safety, Definition of Done, Long-term goal, SSOT routing present |
| No rule text materially altered | Re-read each section; compare against Dutch original if uncertain |
| Production safety | Fully English |
| Definition of Done | 8 bullets in English |
| Long-term goal | Fully English |
| SSOT — Content routing | Fully English; `P-Naam/` preserved |
| Footer metadata removed | Neither `*Opgesteld door owner*` nor `*Bewaakt door Larry*` present |
| Double `---` artifact removed | Only single separators between sections |
| Changelog section | Present at end of file |
| Changelog entry | Contains `B-030B`, date, agent, description |
| No Dutch system instructions remaining | `grep -n` check for Dutch words |
| No secrets or credential values | Confirm; not expected |

---

## 10. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve this proposal for execution? | a) Approve b) Request content edits c) Defer | Determines whether GL-005 translation + Diagnostic Discipline proceeds |
| 2 | Confirm footer metadata removal is acceptable? | a) Confirm removal b) Translate and preserve | If b): specify which lines to keep and how to translate them |
| 3 | Confirm `rust` → `stability` as the correct English translation? | a) Confirm b) Prefer alternative (`calm`, `peace of mind`, other) | Single word; low impact; requires explicit Owner confirmation |
| 4 | Confirm `P-Naam/` is the only Dutch convention to preserve? | a) Confirm b) Identify other items to preserve | Affects language compliance completeness |
| 5 | Confirm the Diagnostic Discipline rule text in §6.2 is approved as written? | a) Confirm b) Request edits | Text in §6.2 will be used verbatim; edits require a revised proposal |

---

## 11. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. No database rows have been written. The proposed GL-005 content in §6.2 is proposed text only — it is not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of B-030B v0.2 is an approval of the exact content in §6.2. Any content change to the proposed file after approval but before execution requires a separate approval.

---

## 12. Final Recommendation

**B-030B v0.2 is ready for Owner approval.**

The proposed replacement in §6.2 is complete, execution-ready, and integrity-verified. All existing rules are present and unchanged. The Diagnostic Discipline section is the only new behavioral rule. The footer metadata removal is explicitly justified.

**Controlled execution method** — after Owner approval:
1. Read the current GL-005 file to confirm its state before any edit
2. Replace the full file content with the exact approved content from §6.2 of this proposal — no deviations
3. Read back the full GL-005 file to confirm the replacement is correct
4. Run all post-checks from §9
5. Write audit trail: team_log entry, session log, UMC summary

GL-005 is a critical file. Execution must use the exact approved content. Any deviation from §6.2 requires stopping, reporting to Owner, and obtaining a revised approval before proceeding.

B-021B (logging investigation) and B-021C (credential recovery proposal) can proceed in parallel — they do not depend on GL-005 being translated.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-030B-gl-005-translation-diagnostic-discipline-proposal-v02.md`*
