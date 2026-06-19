# B-005 Workstreams Start Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Purpose

The Workstreams layer is the third static knowledge layer in the myPKA team, alongside SOPs and Guidelines. Workstreams define how recurring multi-agent orchestrations run: who triggers what, in which order, with which inputs and outputs, and to whom the result goes.

Without active Workstreams, agents operate from AGENT.md alone. This means:
- Recurring orchestrations are not documented independently of any one agent
- No shared contract exists between agents for recurring collaboration
- Agents that reference a Workstream file fall back silently when it is missing, using AGENT.md as their contract instead — which may diverge from what other agents expect

The purpose of this proposal is to assess the current state of the Workstreams layer, identify what is missing or misaligned, and propose a controlled activation plan for Owner Walter Kamer's review.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| Workstreams require Owner approval before creation or modification | GL-014 v1.2 §1 |
| Workstreams are critical files — may never be modified without Owner approval | GL-014 v1.2 §8 |
| Workstream executor: Marcus/Larry. Reviewer: Larry. Final approval: Owner | GL-014 v1.2 §9 |
| Workstreams are 7th in SSOT hierarchy — below SOPs, above Memory | GL-014 v1.2 §7 |
| Canonical path for Core Workstreams: `Team Knowledge/Core/Workstreams/` | GL-004 Canonical Paths |
| Workstream naming: `WS-001_Title.md` | GL-001 File Naming Conventions |
| All Workstream files must be written in English | GL-014 v1.2 §10 System File Language Rule |
| All system files (incl. Workstreams) require changelog entry on every change | GL-014 v1.2 §5 |
| "Workstreams — recurring multi-agent orchestrations. Filename: WS-001_<omschrijving met spaties>.md. Reference SOPs and Guidelines, never duplicate them." | CLAUDE.md Team Knowledge Taxonomy |
| After writing any file to `Team Knowledge/Core/Workstreams/`: read it back, confirm, update index | CLAUDE.md Operational Conventions |
| Task priority follows from: Goals → Projects → Workstreams → Tasks | CLAUDE.md, SOP-005 |

---

## 3. Scope

**Inspected:**
- `Team Knowledge/Core/Workstreams/` — canonical Core path (per GL-004)
- `Team Knowledge/Kamer E-commerce/Workstreams/` — domain Workstreams
- `Team Knowledge/Geldstroom Regie/Workstreams/` — domain Workstreams
- `Team Inbox/Archive/mypka-scaffold-v1.0.0/Team Knowledge/Workstreams/` — scaffold reference
- All `AGENT.md` files under `Team/` — for Workstream references
- `Team Knowledge/Core/Guidelines/GL-001, GL-004, GL-010, GL-014` — for Workstream conventions
- `Team Knowledge/Core/SOPs/SOP-005, SOP-006` — for hierarchy references
- `Team Knowledge/Templates/` — for existing templates
- `CLAUDE.md` — for taxonomy and operational conventions

**Excluded:**
- Content quality review of `WS-001_Kamer E-commerce operationeel procesframework.md` (operational domain content)
- Goal, Project and Task state in Todoist or databases
- Domain-level research quality
- Any files outside `Team Knowledge/` and `Team/`

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `find` on `Team Knowledge/Core/`, `Team Knowledge/Kamer E-commerce/Workstreams/`, `Team Knowledge/Geldstroom Regie/Workstreams/`, and `Team Inbox/Archive/mypka-scaffold-v1.0.0/` to identify existing Workstream files
- `find` on `Team/` for all `AGENT.md` files followed by `grep -rn` for "workstream" and "WS-" references
- `grep -rn` on all Core Guidelines for "workstream" mentions
- `Read` on GL-001, GL-004, GL-010, GL-014, SOP-005, SOP-006, CLAUDE.md, Marcus AGENT.md, Penn AGENT.md, Lena AGENT.md, KE WS-001, KE workstream-index.md, Templates INDEX.md

No files were modified, created, moved or deleted.

---

## 5. Current Workstreams State

### Core Workstreams

**Folder:** `Team Knowledge/Core/Workstreams/` — **does not exist on disk**

The canonical path is defined in GL-004 and referenced by GL-014 as a critical path. The folder has never been created.

**Files:** None. No Core Workstream files exist.

### Kamer E-commerce Domain Workstreams

**Folder:** `Team Knowledge/Kamer E-commerce/Workstreams/` — exists

**Files:**
- `WS-001_Kamer E-commerce operationeel procesframework.md` — exists, active
- `workstream-index.md` — exists, lists WS-001

**State:** Partially functional. One Workstream exists and is indexed. It is written entirely in Dutch, which violates the System File Language Rule (GL-014 §10).

### Geldstroom Regie Domain Workstreams

**Folder:** `Team Knowledge/Geldstroom Regie/Workstreams/` — exists, but is empty

**Files:** None.

**State:** Folder present, no content.

### Scaffold Reference

`Team Inbox/Archive/mypka-scaffold-v1.0.0/Team Knowledge/Workstreams/WS-001-daily-journaling.md` — exists in archive only. This is the original scaffold WS file from before the `Core/` layer was introduced. It uses kebab-case naming (`WS-001-daily-journaling.md`) inconsistent with current GL-001 convention (`WS-001_Daily journaling.md`). It references old file paths (`Team/Penn - Journal Writer/AGENTS`) that no longer match the live structure. It is archived and has never been the live file.

### Summary

| Location | Folder exists | Files | State |
|---|---|---|---|
| `Team Knowledge/Core/Workstreams/` | No | None | Missing |
| `Team Knowledge/Kamer E-commerce/Workstreams/` | Yes | 1 WS + index | Partial — Dutch language violation |
| `Team Knowledge/Geldstroom Regie/Workstreams/` | Yes | None | Empty |
| Scaffold (archived) | Yes (archive) | 1 WS (old format) | Archived, not active |

**Overall state: Missing core infrastructure. Agent references are broken. One domain Workstream exists with a language violation.**

---

## 6. Related System Components

### Goals, Projects, Tasks

The myPKA hierarchy per SOP-005 and CLAUDE.md is:

```
Goals → Projects → Workstreams → Tasks
```

In this model, a Workstream is a non-time-bound recurring element that sits between Projects and Tasks. A Project has an end; a Workstream does not. A Task executes within a Workstream. Without active Workstreams, this chain is broken between Projects and Tasks for recurring work.

Marcus's AGENT.md makes this explicit: "Workstream — recurring operation with no fixed end → attach to existing Project or create standalone."

### SOPs

SOPs define how to do a single repeatable task. Workstreams orchestrate multiple agents across multiple SOPs in a recurring sequence. Workstreams reference SOPs; they never duplicate them. Example: a Daily Journaling Workstream references SOP-008 (Read journal) and SOP-009 (Write journal) rather than repeating those steps inline.

### AGENT.md files

Two AGENT.md files hold live Workstream references that currently resolve to missing files:

- **Penn** (`Team/Penn - The Journal Writer/AGENT.md`, line 18): `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` is your workflow contract. Read it before processing any input. If the contract and this file disagree, the contract wins.
- **Penn** (line 307): `- Workflow contract: Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md`
- **Lena** (`Team/Lena - The Health Coach/AGENT.md`, line 18): No dedicated workstream exists yet. When one is created, it will live at `Team Knowledge/Core/Workstreams/WS-002_Health habit coaching.md`. Until then, this file is the operating contract.

Penn is instructed to read WS-001 before every journaling task, with the contract taking precedence over AGENT.md. The file does not exist. Penn therefore operates without a contract and relies solely on AGENT.md. This is a structural gap.

Lena explicitly acknowledges the missing WS-002 and uses AGENT.md as fallback. This is documented and acceptable as a temporary state, but it is an open item.

### Team Governance

Per GL-014 §9, the executor for Workstream changes is Marcus or Larry. The reviewer is Larry. Owner Walter Kamer gives final approval. This applies to every Workstream creation or modification — including WS-001 and the folder itself.

Per GL-014 §8, `Team Knowledge/Core/Workstreams/` is listed as a critical path. All files in it are critical files.

### Templates

The `Team Knowledge/Templates/` directory contains templates for: projects, goals, persons, organizations, topics, key elements, habits, and session logs. No Workstream template exists. The Templates INDEX.md has no WS entry.

---

## 7. Findings

### Finding F-001: Core Workstreams folder does not exist

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/` |
| **Finding type** | Missing infrastructure |
| **Expected state** | Folder exists as defined in GL-004 and GL-014 §8 |
| **Actual state** | Folder has never been created |
| **Risk** | High — all Core WS file references are broken; GL-014 critical path points to a non-existent location |
| **Recommended action** | Create folder as Phase 1 of B-005A |

---

### Finding F-002: WS-001 Daily Journaling does not exist

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` |
| **Finding type** | Missing file — broken agent reference |
| **Expected state** | File exists and serves as Penn's workflow contract |
| **Actual state** | File does not exist. Penn's AGENT.md instructs Penn to read it before every journaling task, and states it takes precedence over AGENT.md. Penn silently falls back to AGENT.md alone. |
| **Risk** | High — Penn's stated contract is unresolvable. If Penn and AGENT.md diverge over time, there is no contract to arbitrate. The workflow is undocumented at the Workstream layer. |
| **Recommended action** | Create WS-001 as highest-priority item in B-005A |

---

### Finding F-003: WS-002 Health Habit Coaching does not exist

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/WS-002_Health habit coaching.md` |
| **Finding type** | Missing file — agent references placeholder |
| **Expected state** | File exists as Lena's workflow contract |
| **Actual state** | File does not exist. Lena's AGENT.md explicitly acknowledges this and designates AGENT.md as the temporary fallback. |
| **Risk** | Medium — Lena is explicit about the gap; risk is contained. Becomes higher as Lena's role matures. |
| **Recommended action** | Owner decision: create now or defer. See §10. |

---

### Finding F-004: WS-001 Kamer E-commerce written in Dutch

| | |
|---|---|
| **Path** | `Team Knowledge/Kamer E-commerce/Workstreams/WS-001_Kamer E-commerce operationeel procesframework.md` |
| **Finding type** | System File Language Rule violation |
| **Expected state** | Fully English per GL-014 v1.2 §10 |
| **Actual state** | Entire file written in Dutch — titles, section headers, body text, field labels |
| **Risk** | Medium — governance non-compliance. All agents reading this file encounter Dutch system content, which creates drift from the System File Language Rule already enforced in AGENT.md files (B-028, B-029). |
| **Recommended action** | Translate to English in a dedicated B-005C pass. Content is operationally correct; this is a language compliance update only. |

---

### Finding F-005: No Core Workstream index file

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/workstream-index.md` (expected) |
| **Finding type** | Missing index |
| **Expected state** | Index file analogous to `SOP-index.md` listing all Core Workstreams |
| **Actual state** | File does not exist (folder also missing) |
| **Risk** | Low — only one Core WS will exist initially; grows as more are added |
| **Recommended action** | Create alongside folder and WS-001 in B-005A |

---

### Finding F-006: No Workstream template

| | |
|---|---|
| **Path** | `Team Knowledge/Templates/workstream.md` (expected) |
| **Finding type** | Missing template |
| **Expected state** | Template exists for creating new Workstream files consistently |
| **Actual state** | No Workstream template in `Team Knowledge/Templates/`. Templates INDEX.md has no WS entry. |
| **Risk** | Low — blocks consistency when creating future Workstreams, not an immediate blocker |
| **Recommended action** | Create as part of B-005B |

---

### Finding F-007: Geldstroom Regie Workstreams folder is empty

| | |
|---|---|
| **Path** | `Team Knowledge/Geldstroom Regie/Workstreams/` |
| **Finding type** | Documentation gap |
| **Expected state** | At least one Workstream for recurring GR operations (e.g. Geldstroom Scan delivery) |
| **Actual state** | Folder exists but contains no files |
| **Risk** | Low — GR is earlier stage; no agent currently references a missing GR Workstream |
| **Recommended action** | Owner decision: define first GR Workstream now or defer. See §10. |

---

### Finding F-008: No documented Core vs Domain Workstream distinction

| | |
|---|---|
| **Path** | GL-004, GL-014, CLAUDE.md |
| **Finding type** | Governance gap |
| **Expected state** | Clear rule stating which orchestrations belong in `Team Knowledge/Core/Workstreams/` vs domain-level `Team Knowledge/<Domain>/Workstreams/` |
| **Actual state** | Both paths are defined but no rule specifies what belongs where. In practice, Core appears to hold cross-domain agent orchestrations (journaling, health coaching) while domain folders hold domain-specific operational flows (KE product-to-live process). This is implied but not documented. |
| **Risk** | Low now, grows as more Workstreams are created |
| **Recommended action** | Add a one-line distinction rule to GL-004 when the folder is created |

---

### Finding F-009: Scaffold WS-001 in archive uses old naming and paths

| | |
|---|---|
| **Path** | `Team Inbox/Archive/mypka-scaffold-v1.0.0/Team Knowledge/Workstreams/WS-001-daily-journaling.md` |
| **Finding type** | Informational — historical record |
| **Expected state** | Archived scaffold uses legacy format |
| **Actual state** | Uses kebab-case name (`WS-001-daily-journaling.md`) inconsistent with GL-001. References `Team/Penn - Journal Writer/AGENTS` (wrong path, no `Core/` layer). Not the live file. |
| **Risk** | None — archived, not referenced by any active agent |
| **Recommended action** | No action. Historical record. May serve as source material when writing WS-001. |

---

## 8. Proposed Workstreams Model

### 8.1 Definition

A Workstream is a recurring multi-agent orchestration with no fixed end date. It defines:
- What triggers the orchestration
- Which agents participate
- In what order steps happen
- What inputs and outputs each step produces
- Which SOPs or Guidelines each step references

Workstreams do not duplicate SOP content. They reference SOPs and GLs.

**Workstream vs SOP vs Project:**

| Type | Nature | End date | Scope |
|---|---|---|---|
| SOP | Single repeatable task or procedure | n/a | One agent, one job |
| Workstream | Recurring multi-agent orchestration | None | Multiple agents, recurring |
| Project | Time-bound effort toward a Goal | Yes | One or more agents, finite |

### 8.2 Two-Track Model

| Track | Path | Scope |
|---|---|---|
| Core | `Team Knowledge/Core/Workstreams/` | Cross-domain orchestrations involving multiple agents or the core team (journaling, health coaching, session management) |
| Domain | `Team Knowledge/<Domain>/Workstreams/` | Domain-specific operational flows (KE product lifecycle, GR delivery flow) |

**Routing rule (proposed):** If the orchestration involves agents from more than one domain, or is managed by Larry/Marcus at team level → Core. If it operates entirely within one domain and is managed by domain specialists → Domain.

### 8.3 Naming Convention

Per GL-001 (already defined):

```
WS-NNN_Title with spaces.md
```

- NNN: three-digit sequential number, per-domain (Core and each domain maintain their own counter)
- Title: descriptive, Title Case, spaces allowed
- Extension: `.md`

Examples:
- `WS-001_Daily journaling.md` (Core)
- `WS-002_Health habit coaching.md` (Core)
- `WS-001_Kamer E-commerce operational process framework.md` (KE domain)

### 8.4 Required Sections (Template Structure)

Every Workstream file must contain:

```markdown
# WS-NNN — Title

**Domain:** Core | Kamer E-commerce | Geldstroom Regie | Personal
**Trigger:** [what starts this orchestration]
**Maintainer:** [agent responsible for keeping this WS up to date]
**Status:** Active | Draft | Deprecated

---

## Purpose

[Why this orchestration exists. What it produces.]

---

## Agents

| Agent | Role in this workstream |
|---|---|
| [name] | [what they do] |

---

## Inputs

[What the orchestration starts with]

---

## Steps

### Step 1 — [Name]

**Owner:** [agent]
**SOP reference:** [[SOP-NNN_Title]] (if applicable)
**Input:** [what this step receives]
**Action:** [what happens]
**Output:** [what this step produces]
**Passes to:** [next step or agent]

[Repeat per step]

---

## Outputs

[Final deliverable of the orchestration]

---

## What this Workstream does not do

[Explicit exclusions — prevents scope creep]

---

## References

- [[SOP-NNN_Title]] — [why referenced]
- [[GL-NNN_Title]] — [why referenced]

---

## Changelog

- YYYY-MM-DD (Agent, Backlog-ID): [description]. Approved by Owner.
```

### 8.5 Maintainer Logic

Per GL-014 §9:
- **Executor:** Marcus or Larry
- **Reviewer:** Larry
- **Final approval:** Owner Walter Kamer

Each Workstream file has a `**Maintainer:**` field naming the agent responsible for proposing updates when the underlying process changes.

### 8.6 Relationship to Tasks and Projects

A Workstream is non-actionable. It provides the orchestration context within which tasks live. Per the hierarchy (CLAUDE.md, SOP-005): Goals → Projects → Workstreams → Tasks.

A task inside a Workstream points back to the Workstream as its parent context. A Workstream itself is not a task — it is the container that makes recurring task sets coherent.

### 8.7 Relationship to AI-Team Agents

Each agent's AGENT.md may reference one or more Workstreams as workflow contracts. When a Workstream file exists and the AGENT.md says "this WS is your contract — it takes precedence," the WS file is the authoritative instruction for that orchestration. The AGENT.md holds identity and role; the WS holds the step-by-step collaboration contract.

---

## 9. Proposed Changes

### Phase B-005A — Core Workstreams infrastructure (recommended first)

#### Change C-001: Create `Team Knowledge/Core/Workstreams/` folder

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/` |
| **Action** | Create the folder |
| **Reason** | Canonical path in GL-004 and GL-014 does not exist — all future WS files depend on this |
| **Risk** | None |
| **Owner approval required** | Yes — folder structure modification per GL-014 §1 |

---

#### Change C-002: Create `WS-001_Daily journaling.md`

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` |
| **Action** | Create new file using the WS template (C-004), authored by Marcus or Larry |
| **Content** | Orchestration of Penn journaling flow: trigger (owner shares personal narrative), Steps (Larry routes → Penn writes journal → Penn cross-links → Larry Librarian pass at session close). References: SOP-008, SOP-009, Penn AGENT.md, Larry AGENT.md. |
| **Source material** | Scaffold `WS-001-daily-journaling.md` (archived) may inform content but must be adapted to current Penn workflow, GL-014 language rule (fully English), and current file paths. |
| **Reason** | Penn's AGENT.md instructs it to read this file as the authoritative workflow contract before every journaling task. This is the highest-priority gap. |
| **Risk** | Low — documentation only. No agent behavior changes; Penn already falls back to AGENT.md. The WS adds the missing contract layer. |
| **Owner approval required** | Yes |

---

#### Change C-003: Create `workstream-index.md` for Core

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/workstream-index.md` |
| **Action** | Create index file listing all Core Workstreams |
| **Content** | Table: Nr / Title / File / Status — starting with WS-001 |
| **Reason** | Analogous to `SOP-index.md`; required to make the Workstream layer discoverable |
| **Risk** | None |
| **Owner approval required** | Yes (same pass as C-001 and C-002) |

---

#### Change C-004 (optional, same pass): Add Core vs Domain routing rule to GL-004

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` |
| **Action** | Add a one-line routing rule under the Workstreams path entry: "Core: cross-domain agent orchestrations. Domain: domain-specific operational flows." |
| **Reason** | Closes the undocumented distinction found in F-008 |
| **Risk** | Low — documentation only |
| **Owner approval required** | Yes — GL modification |

---

### Phase B-005B — Workstream template

#### Change C-005: Create `workstream.md` template and update Templates INDEX.md

| | |
|---|---|
| **Path** | `Team Knowledge/Templates/workstream.md` and `Team Knowledge/Templates/INDEX.md` |
| **Action** | Create template file using the structure defined in §8.4; add entry to INDEX.md |
| **Reason** | Ensures all future Workstream files follow a consistent structure |
| **Risk** | None |
| **Owner approval required** | Yes |

---

### Phase B-005C — Language compliance for KE WS-001

#### Change C-006: Translate KE WS-001 to English

| | |
|---|---|
| **Path** | `Team Knowledge/Kamer E-commerce/Workstreams/WS-001_Kamer E-commerce operationeel procesframework.md` |
| **Action** | Translate all Dutch content to English. No operational content changes. Add changelog entry. |
| **Reason** | GL-014 §10 System File Language Rule — all Workstream files must be in English |
| **Risk** | Low — language compliance update only. Operational logic unchanged. |
| **Owner approval required** | Yes |

---

### Deferred — Owner decision required (see §10)

#### Change C-007: Create `WS-002_Health habit coaching.md`
Lena's coaching orchestration. Lena explicitly acknowledges the gap. Requires Owner decision on whether to define it now.

#### Change C-008: First Workstream for Geldstroom Regie
GR domain Workstreams folder is empty. Finn is the GR domain specialist. Requires Owner decision on whether a GR Workstream should be defined now, and if so, which process to document first.

---

## 10. Items Requiring Owner Decision

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve Phase B-005A? (folder + WS-001 Daily Journaling + index + GL-004 routing rule) | a) Approve b) Defer | Fixes Penn broken reference; activates Core Workstreams layer |
| 2 | Approve Phase B-005B? (workstream template) | a) Approve, same pass as A b) Separate pass c) Defer | Consistency for all future WS creation |
| 3 | Approve Phase B-005C? (KE WS-001 English translation) | a) Approve b) Defer | Language compliance for one existing WS |
| 4 | Create WS-002 Health Habit Coaching now or defer? | a) Create now b) Defer until Lena's scope matures | Lena currently functioning without it |
| 5 | First GR Workstream: define now or defer? | a) Define now (which process?) b) Defer | GR domain is growing but not blocked |
| 6 | Who authors WS-001 Daily Journaling? | a) Marcus (domain — projects/workstreams) b) Larry (orchestrator — knows the journaling flow) | Governance-consistent either way; Marcus is listed executor in GL-014 |
| 7 | Should WS-001 Daily Journaling content be based on scaffold, written fresh, or reviewed by Penn? | a) Marcus/Larry write fresh b) Adapt scaffold c) Larry drafts, Penn reviews against AGENT.md | Quality of the contract |

---

## 11. Risk Assessment

| Change | Risk if applied | Risk if not applied |
|---|---|---|
| C-001: Create Core folder | None | Penn reference permanently broken |
| C-002: Create WS-001 Daily Journaling | Low — documentation only | Penn has no workflow contract; AGENT.md may drift without correction |
| C-003: Create Core workstream-index.md | None | No discoverable registry of Core Workstreams |
| C-004: GL-004 routing rule | Low — one-line addition | Core vs Domain ambiguity grows with each new WS |
| C-005: Workstream template | None | Inconsistent WS files as team grows |
| C-006: KE WS-001 English | Low — language only | Language rule drift; inconsistency with B-028/B-029 language compliance work |
| C-007: Lena WS-002 | Low | Lena operating without contract; acceptable short-term |
| C-008: GR first WS | Low | GR has no documented recurring orchestrations |

**Overall risk of activation: Low.** All proposed changes are documentation-only. No agent behavior changes. No scripts, databases, or infrastructure touched. The highest-urgency item is C-001 + C-002 (Penn broken reference).

---

## 12. Recommended Execution Plan

After Owner's explicit approval per phase:

**Phase B-005A — Core Workstreams infrastructure (recommended first, highest priority):**
- Executor: Marcus (or Larry)
- Reviewer: Larry
- Actions: C-001, C-002, C-003, C-004
- Sequence: create folder → write WS-001 → create index → add GL-004 routing note
- Audit trail: changelog in WS-001 and GL-004, team_log entry, session log per GL-014 §6
- Post-check: folder exists, WS-001 readable, Penn reference resolves, index lists WS-001

**Phase B-005B — Template (can follow immediately or run in parallel):**
- Executor: Marcus or Larry
- Actions: C-005
- Post-check: `Team Knowledge/Templates/workstream.md` exists, INDEX.md updated

**Phase B-005C — KE language compliance:**
- Executor: Nolan (language compliance specialist) or Marcus
- Actions: C-006
- Note: Consistent with B-029 language cleanup approach — content-neutral translation
- Post-check: WS-001 KE fully English, operational content unchanged

**Deferred phases (after Owner decision):**
- B-005D: Lena WS-002 — if approved
- B-005E: GR first Workstream — if approved, which process to document is an Owner decision

---

## 13. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. No folder has been created. No database has been touched. The execution plan in §12 is not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

---

## 14. Final Recommendation

The Workstreams layer is the only static knowledge layer (alongside SOPs and Guidelines) that has not been activated in the Core. The folder does not exist. Two agent contracts are broken. One existing domain Workstream violates the language rule.

The clearest immediate path is to approve Phase B-005A: create the Core Workstreams folder, write WS-001 Daily Journaling, and create the index. This is documentation-only work with zero operational risk and directly resolves Penn's broken workflow contract — which is the most concrete structural gap in the team today.

Phases B-005B and C can follow in the same session or the next. The deferred items (Lena WS-002, GR first Workstream) are lower priority and can wait for a separate Owner decision.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-005-workstreams-start-proposal.md`*
