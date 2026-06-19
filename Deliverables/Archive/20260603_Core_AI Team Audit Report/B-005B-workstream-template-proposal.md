# B-005B Workstream Template Proposal

**Date:** 2026-06-03
**Prepared by:** Larry (orchestrator)
**Status:** Proposal — awaiting Owner Walter Kamer's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Basis:** B-005A complete (Core Workstreams folder, WS-001, workstream-index.md, GL-004 routing rule all active)

---

## 1. Purpose

B-005A established the Core Workstreams infrastructure and created WS-001 as the first live Workstream. WS-001 now serves as the de facto reference pattern. B-005B formalises that pattern into a reusable template so that every new Workstream — whether Core or Domain — starts from a consistent structure rather than being rebuilt from scratch or derived informally from WS-001.

Without a canonical template:
- New Workstreams risk missing required sections (scope exclusions, changelog, references).
- Agents writing a new WS must decide the structure themselves, leading to drift.
- The workstream-index.md grows inconsistently.

With a canonical template:
- Any agent or maintainer can start a new Workstream from a known baseline.
- Required sections are present by default.
- Review is faster because the Owner and Larry already know the structure.

---

## 2. Proposed Canonical Location

`Team Knowledge/Core/Templates/workstream-template.md`

The `Team Knowledge/Core/Templates/` folder already exists. Templates for other document types belong here. The Workstream template follows the same convention.

---

## 3. Proposed Template Filename

```
workstream-template.md
```

Single file, lowercase, no version suffix. Versioning is handled via the Changelog section inside the template and via the B-005B audit trail. If the template is ever structurally revised, a Changelog entry is added to the file itself and a new backlog item documents the change.

---

## 4. Required Sections and Rationale

| Section | Required | Rationale |
|---|---|---|
| Header block | Yes | Provides routing metadata at a glance: domain, trigger, maintainer, status. Agents and the Owner need this without reading the full file. |
| Purpose | Yes | States the problem this Workstream solves. Without it, agents cannot judge whether to invoke it or how to adapt it. |
| Agents | Yes | Names every participating agent and their role. Prevents ambiguity about who does what and who leads. |
| Inputs | Yes | Defines what triggers the Workstream and what material it accepts. Required for correct routing. |
| Steps | Yes | The operational core. Each step has a lead, input, action, output, and handoff. This is the ICOR Control layer for the Workstream. |
| Outputs | Yes | Lists concrete artifacts produced. Required for audit trail and downstream consumption. |
| What this Workstream does not do | Yes | Explicit scope exclusions. Prevents scope creep and misrouting. WS-001 established this as a required section — it is not optional. |
| References | Yes | Links to SOPs, Guidelines, and AGENT.md files that this Workstream depends on. Required for traceability and maintenance. |
| Changelog | Yes | Dated record of structural changes. Required by GL-014 for any document that can be modified post-approval. |

---

## 5. Naming Convention

### Workstream files

```
WS-XXX_Description in lowercase.md
```

- `WS-` prefix — mandatory, uppercase
- Three-digit sequential number — assigned from workstream-index.md at creation time
- Underscore separator between number and description
- Description in lowercase, words separated by spaces
- Proper nouns and abbreviations follow their standard capitalisation (e.g., `WS-003_Kai onboarding.md`, `WS-004_CRM update.md`)
- `.md` extension

### Core vs Domain

| Type | Location | Managed by |
|---|---|---|
| Core Workstream | `Team Knowledge/Core/Workstreams/` | Larry or Marcus |
| Domain Workstream | `Team Knowledge/<Domain>/Workstreams/` | Domain specialist |

This distinction is already live in GL-004 (Workstream routing rule, added by B-005A).

---

## 6. Ownership Model

| Role | Responsibility |
|---|---|
| Owner (Walter Kamer) | Approves creation, structural change, and deprecation of any Workstream |
| Maintainer (Larry for Core; domain specialist for Domain) | Responsible for keeping the Workstream accurate, adding Changelog entries, and updating workstream-index.md |
| Agent author | May draft a new Workstream using the template; must submit as a proposal for Owner approval before the file is placed in the canonical location |

A Workstream is not active until Owner has approved it. Draft Workstreams are deliverables, not system files.

---

## 7. Connection to ICOR, Workstreams, and GL-004

### ICOR mapping

Each Workstream is an ICOR execution contract:

| ICOR layer | Where it lives in the template |
|---|---|
| Input | `## Inputs` section — what triggers the WS and what material it accepts |
| Control | `## Steps` section — numbered steps with lead, action, and handoff |
| Output | `## Outputs` section — concrete artifacts produced |
| Refine | `## Changelog` section — learnings captured as structural revisions over time |

### GL-004 routing

GL-004 already defines the canonical Workstream paths and the Core vs Domain routing rule (added by B-005A). The template reinforces this by requiring a `Domain:` field in the header block. An agent filling in the template must explicitly choose Core or a named Domain, which triggers the correct path from GL-004.

### workstream-index.md

Every active Workstream must have a row in the relevant `workstream-index.md`. The template includes a reminder note at the top:

> Before filing this as an active Workstream, add a row to workstream-index.md.

---

## 8. Scope Boundaries

### What B-005B covers

- Creating `workstream-template.md` at `Team Knowledge/Core/Templates/workstream-template.md`.
- Optionally: adding a row to the `Templates/INDEX.md` if one exists (or noting it as a follow-up if none exists).

### What B-005B does not cover

- Creating any new Workstream files (WS-002, WS-003, etc.).
- Modifying WS-001 or workstream-index.md.
- Modifying GL-004, GL-014, or any other Guideline.
- Modifying any AGENT.md file.
- Modifying any SOP.
- Translating existing Domain Workstreams (that is B-005C).

---

## 9. Exact Proposed Template Content

The following is the exact content proposed for `workstream-template.md`. Placeholder text is shown in `[square brackets]`.

---

```markdown
# WS-XXX — [Workstream title]

<!-- Before filing as active: add a row to workstream-index.md -->

**Domain:** [Core | Kamer E-commerce | Geldstroom Regie | Personal]
**Trigger:** [What event or request starts this Workstream]
**Maintainer:** [Agent name responsible for keeping this file accurate]
**Status:** [Draft | Active | Paused | Deprecated]
**Owner approval:** [Date and reference, e.g. "2026-06-03 — B-005B"]

---

## Purpose

[One paragraph. What problem does this Workstream solve? What does it produce?
State the why, not the how. The Steps section handles the how.]

---

## Agents

| Agent | Role in this Workstream |
|---|---|
| [Agent name] | [Role: e.g. Orchestrator, Executor, Reviewer] |

---

## Inputs

| Input | Source | Required |
|---|---|---|
| [Input type, e.g. raw text, task ID, file path] | [Who or what provides this] | [Yes / No] |

---

## Steps

### Step 1 — [Step title]

**Step lead:** [Agent name]
**Input:** [What this step receives]

[Numbered action list:]
1. [Action]
2. [Action]

**Output:** [What this step produces]
**Passes to:** [Step 2 / End]

---

### Step 2 — [Step title]

**Step lead:** [Agent name]
**Input:** [What this step receives]

[Numbered action list:]
1. [Action]
2. [Action]

**Output:** [What this step produces]
**Passes to:** [Step 3 / End]

---

<!-- Add or remove steps as needed. Minimum 1 step. -->

---

## Outputs

| Output | Location | Notes |
|---|---|---|
| [Artifact, e.g. journal entry, session log row, Todoist task] | [Canonical path or system] | [Optional note] |

---

## What this Workstream does not do

- [Explicit exclusion 1]
- [Explicit exclusion 2]
- [Explicit exclusion 3]

<!-- At least two explicit exclusions required. State what an agent might wrongly assume is in scope. -->

---

## References

| Reference | Location |
|---|---|
| [SOP or GL name] | `[path/to/file.md]` |

---

## Changelog

- [YYYY-MM-DD] ([Agent], [backlog item or reason]): [What changed]. Approved by Owner Walter Kamer.
```

---

## 10. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Template not adopted — agents continue to free-form new Workstreams | Low | Medium | Template is placed in the canonical Templates folder and referenced in GL-004 or the workstream-index.md preamble |
| Template becomes stale as WS-001 evolves | Low | Low | Changelog section inside template; B-005B establishes the template as a living document subject to the same revision governance as all other system files |
| Template creates over-engineering pressure — agents pad sections | Low | Low | Template is explicitly lightweight; the "What this Workstream does not do" section prevents scope inflation by example |
| Placeholder text left in a filed Workstream | Low | Low | Reviewer (Larry or maintainer) checks for `[square brackets]` before approval |

---

## 11. Owner Decision Options

| Option | Description | Impact |
|---|---|---|
| A — Approve as proposed | Create `workstream-template.md` at `Team Knowledge/Core/Templates/workstream-template.md` with the exact content in §9 | Template active; new Workstreams have a canonical starting point |
| B — Approve with amendments | Approve the structure but request changes to section content, placeholder text, or scope before execution | Revised proposal required; no execution until Owner approves the revision |
| C — Defer | No template yet; continue creating Workstreams ad hoc from WS-001 as reference | No file created; B-005B remains open; drift risk accumulates as more Workstreams are written |

---

## 12. Recommended Option

**Option A — Approve as proposed.**

The template in §9 is directly derived from WS-001's live structure. It introduces no new structural decisions. It is lightweight: no section exceeds what WS-001 already demonstrates. Option A closes B-005B cleanly and gives every future Workstream author a clear starting point.

---

## 13. Implementation Requires Separate Owner Approval

This document is a proposal only. No files have been created or modified. The template will be written to `Team Knowledge/Core/Templates/workstream-template.md` only after Owner Walter Kamer has explicitly approved this proposal — either as Option A, or as Option B after any requested amendments are incorporated.

No implementation, logging, or backlog update will be executed without that explicit approval.

---

Delivered on: 2026-06-03
Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-005B-workstream-template-proposal.md`
No files were modified as part of this proposal. No secret values were accessed or exposed.
