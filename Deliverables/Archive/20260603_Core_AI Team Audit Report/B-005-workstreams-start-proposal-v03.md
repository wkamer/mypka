# B-005 Workstreams Start Proposal v0.3

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Supersedes:** B-005 v0.2 (2026-06-03)

---

## Change Log (v0.2 → v0.3)

| # | Correction applied |
|---|---|
| 1 | Dutch placeholder fixed in WS-001 exact content: `YYYYMMDD_beschrijving.ext` → `YYYYMMDD_description.ext` (two occurrences, Step 2) |
| 2 | Full language compliance check performed on all B-005A exact content — results documented in §9 Language Compliance Check |
| 3 | Final recommendation updated: B-005A is now ready for Owner approval |

## Change Log (v0.1 → v0.2)

| # | Correction applied |
|---|---|
| 1 | Risk for B-005A reclassified from zero to low–medium; rationale: WS-001 is an authoritative contract that takes precedence over Penn AGENT.md |
| 2 | Exact file content provided for all B-005A changes: WS-001, workstream-index.md, GL-004 insertion and changelog |
| 3 | C-004 GL-004 routing rule made definitive — included in B-005A with exact text, no longer optional |
| 4 | Owner terminology corrected throughout — `**Owner:**` in step-level fields replaced with `**Step lead:**` everywhere |
| 5 | WS-001 content tightened and based directly on Penn AGENT.md, Larry AGENT.md and SOP references — scaffold used only as historical reference |
| 6 | B-005B (template) kept strictly separate — WS-001 uses embedded structure, reusable template follows in B-005B |
| 7 | B-005C (KE translation) kept strictly separate — requires dedicated proposal with exact replacement text |
| 8 | Final recommendation adjusted: recommend B-005A only, now that exact content is provided |

---

## 1. Purpose

The Workstreams layer is the third static knowledge layer in the myPKA team, alongside SOPs and Guidelines. Workstreams define how recurring multi-agent orchestrations run: who triggers what, in which order, with which inputs and outputs, and to whom the result goes.

Without active Workstreams, agents operate from AGENT.md alone. This means:
- Recurring orchestrations are not documented independently of any one agent
- No shared contract exists between agents for recurring collaboration
- Agents that reference a Workstream file fall back silently when it is missing, using AGENT.md as their contract instead — which may diverge from what other agents expect

The purpose of this proposal is to assess the current state of the Workstreams layer, identify what is missing or misaligned, and propose a controlled activation plan with exact content for Owner Walter Kamer's review and approval.

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
- `Team Knowledge/Core/SOPs/SOP-005, SOP-006, SOP-008, SOP-009` — for hierarchy and specialist journal references
- `Team Knowledge/Templates/` — for existing templates
- `CLAUDE.md` — for taxonomy and operational conventions

**Excluded:**
- Content quality review of `WS-001_Kamer E-commerce operationeel procesframework.md`
- Goal, Project and Task state in Todoist or databases
- Domain-level research quality
- Any files outside `Team Knowledge/` and `Team/`

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `find` on `Team Knowledge/Core/`, `Team Knowledge/Kamer E-commerce/Workstreams/`, `Team Knowledge/Geldstroom Regie/Workstreams/`, and `Team Inbox/Archive/mypka-scaffold-v1.0.0/`
- `grep -rn` on all `AGENT.md` files for "workstream" and "WS-" references
- `grep -rn` on all Core Guidelines for "workstream" mentions
- `Read` on GL-001, GL-004, GL-010, GL-014, SOP-005, SOP-006, SOP-008, SOP-009, CLAUDE.md, Penn AGENT.md, Lena AGENT.md, KE WS-001, KE workstream-index.md, Templates INDEX.md

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

`Team Inbox/Archive/mypka-scaffold-v1.0.0/Team Knowledge/Workstreams/WS-001-daily-journaling.md` — exists in archive only. Uses kebab-case naming inconsistent with current GL-001. References old file paths that no longer match the live structure. It is archived and has never been the live file. It was used as historical reference only when drafting WS-001 content in §9 of this proposal.

### Summary

| Location | Folder exists | Files | State |
|---|---|---|---|
| `Team Knowledge/Core/Workstreams/` | No | None | Missing |
| `Team Knowledge/Kamer E-commerce/Workstreams/` | Yes | 1 WS + index | Partial — Dutch language violation |
| `Team Knowledge/Geldstroom Regie/Workstreams/` | Yes | None | Empty |
| Scaffold (archived) | Yes (archive) | 1 WS (old format) | Archived, not active |

**Overall state: Core infrastructure missing. Penn's workflow contract is broken. One domain Workstream exists with a language violation.**

---

## 6. Related System Components

### Goals, Projects, Tasks

The myPKA hierarchy per SOP-005 and CLAUDE.md is:

```
Goals → Projects → Workstreams → Tasks
```

In this model, a Workstream is a non-time-bound recurring element between Projects and Tasks. A Project has an end; a Workstream does not. A Task executes within a Workstream. Without active Workstreams, this chain is broken between Projects and Tasks for recurring work.

Marcus's AGENT.md makes this explicit: "Workstream — recurring operation with no fixed end → attach to existing Project or create standalone."

### SOPs

SOPs define how to do a single repeatable task. Workstreams orchestrate multiple agents across multiple SOPs in a recurring sequence. Workstreams reference SOPs; they never duplicate them.

### AGENT.md files

Two AGENT.md files hold live Workstream references that currently resolve to missing files:

- **Penn** (`Team/Penn - The Journal Writer/AGENT.md`, line 18 and line 307): References `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` as the workflow contract. Penn is instructed to read it before every journaling task, and explicitly states: "If the contract and this file disagree, the contract wins." This makes WS-001 an **authoritative contract** — not supplementary documentation.

- **Lena** (`Team/Lena - The Health Coach/AGENT.md`, line 18): References `Team Knowledge/Core/Workstreams/WS-002_Health habit coaching.md`. Lena explicitly acknowledges the gap and designates AGENT.md as the temporary fallback.

### Team Governance

Per GL-014 §9, the executor for Workstream changes is Marcus or Larry. The reviewer is Larry. Owner Walter Kamer gives final approval. This applies to every Workstream creation or modification.

Per GL-014 §8, `Team Knowledge/Core/Workstreams/` is listed as a critical path. All files in it are critical files.

**Owner terminology note:** Throughout this proposal and in all proposed Workstream file content, `Owner` refers exclusively to Owner Walter Kamer. Agent responsibility within Workstream steps is expressed as `**Step lead:**`, never as `**Owner:**`.

### Templates

`Team Knowledge/Templates/` contains templates for projects, goals, persons, organizations, topics, key elements, habits, and session logs. No Workstream template exists. The Templates INDEX.md has no WS entry. The reusable Workstream template is proposed in Phase B-005B (separate from B-005A).

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
| **Recommended action** | Create folder as first step of B-005A |

---

### Finding F-002: WS-001 Daily Journaling does not exist

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` |
| **Finding type** | Missing file — broken authoritative agent contract |
| **Expected state** | File exists and serves as Penn's workflow contract, taking precedence over AGENT.md |
| **Actual state** | File does not exist. Penn's AGENT.md instructs Penn to read it before every journaling task and states it takes precedence over AGENT.md if they disagree. Penn silently falls back to AGENT.md alone. |
| **Risk** | High — Penn's stated authoritative contract is unresolvable. If Penn AGENT.md and WS-001 ever diverge, there is no contract to arbitrate. The risk is not just documentation — any WS-001 content that adds steps or differs from AGENT.md will immediately change Penn's behavior. |
| **Recommended action** | Create WS-001 as highest-priority item in B-005A. Content must be derived from Penn AGENT.md current state to avoid unintended behavioral changes. Exact content is provided in §9. |

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
| **Risk** | Medium — governance non-compliance consistent with pre-B-028 state. Content is operationally correct; this is a language compliance issue. |
| **Recommended action** | Translate to English in dedicated B-005C pass. B-005C requires a separate exact translation proposal before execution. |

---

### Finding F-005: No Core Workstream index file

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/workstream-index.md` (expected) |
| **Finding type** | Missing index |
| **Expected state** | Index file analogous to `SOP-index.md` listing all Core Workstreams |
| **Actual state** | File does not exist (folder also missing) |
| **Risk** | Low — only one Core WS will exist initially |
| **Recommended action** | Create alongside folder and WS-001 in B-005A. Exact content provided in §9. |

---

### Finding F-006: No Workstream template

| | |
|---|---|
| **Path** | `Team Knowledge/Templates/workstream.md` (expected) |
| **Finding type** | Missing template |
| **Expected state** | Template exists for creating new Workstream files consistently |
| **Actual state** | No Workstream template in `Team Knowledge/Templates/`. Templates INDEX.md has no WS entry. |
| **Risk** | Low — blocks consistency for future Workstreams, not an immediate blocker |
| **Recommended action** | Create as B-005B (separate phase). WS-001 uses its own embedded structure until the reusable template exists. |

---

### Finding F-007: Geldstroom Regie Workstreams folder is empty

| | |
|---|---|
| **Path** | `Team Knowledge/Geldstroom Regie/Workstreams/` |
| **Finding type** | Documentation gap |
| **Expected state** | At least one Workstream for recurring GR operations |
| **Actual state** | Folder exists but contains no files. No agent currently references a missing GR Workstream. |
| **Risk** | Low — GR is at an earlier stage |
| **Recommended action** | Owner decision: define first GR Workstream now or defer. See §10. |

---

### Finding F-008: No documented Core vs Domain Workstream distinction

| | |
|---|---|
| **Path** | GL-004, GL-014, CLAUDE.md |
| **Finding type** | Governance gap |
| **Expected state** | Clear rule stating which orchestrations belong in Core vs domain Workstreams folder |
| **Actual state** | Both paths are defined in GL-004 but no routing rule exists |
| **Risk** | Low now, grows as more Workstreams are created |
| **Recommended action** | Add exact routing rule to GL-004 as part of B-005A. Exact insertion text provided in §9. |

---

### Finding F-009: GL-004 does not have a Changelog section

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` |
| **Finding type** | Governance gap |
| **Expected state** | GL-014 §5 requires every GL file to have a `## Changelog` section |
| **Actual state** | GL-004 has no Changelog section |
| **Risk** | Low — compliance gap; not an operational blocker |
| **Recommended action** | Add Changelog section to GL-004 in the same pass as the routing rule addition (B-005A). |

---

### Finding F-010: Scaffold WS-001 in archive uses old naming and paths

| | |
|---|---|
| **Path** | `Team Inbox/Archive/mypka-scaffold-v1.0.0/Team Knowledge/Workstreams/WS-001-daily-journaling.md` |
| **Finding type** | Informational — historical record |
| **Actual state** | Uses kebab-case name inconsistent with GL-001. References old file paths. Archived, not referenced by any active agent. |
| **Risk** | None |
| **Recommended action** | No action. Used only as historical reference when drafting WS-001 content. |

---

## 8. Proposed Workstreams Model

### 8.1 Definition

A Workstream is a recurring multi-agent orchestration with no fixed end date. It defines:
- What triggers the orchestration
- Which agents participate and in which role
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

Routing rule (to be added to GL-004): Core Workstreams hold cross-domain agent orchestrations managed by Larry or Marcus. Domain Workstreams hold domain-specific operational flows managed by domain specialists.

### 8.3 Naming Convention

Per GL-001 (already defined):

```
WS-NNN_Title with spaces.md
```

- NNN: three-digit sequential number, per-domain (Core and each domain maintain their own counter)
- Title: descriptive, Title Case, spaces allowed
- Extension: `.md`

### 8.4 Required Sections (Structure used in B-005A)

The structure below is used in WS-001 as embedded content. The reusable template is proposed in B-005B. Until B-005B is approved, use this structure when creating new Workstream files.

```
# WS-NNN — Title

**Domain:** Core | Kamer E-commerce | Geldstroom Regie | Personal
**Trigger:** [what starts this orchestration]
**Maintainer:** [agent responsible for keeping this WS up to date]
**Status:** Active | Draft | Deprecated

## Purpose
## Agents
## Inputs
## Steps (with Step lead, not Owner)
## Outputs
## What this Workstream does not do
## References
## Changelog
```

**Important:** Step-level responsibility is always expressed as `**Step lead:**`, never as `**Owner:**`. Owner refers exclusively to Owner Walter Kamer throughout all myPKA documentation.

### 8.5 Maintainer Logic

Per GL-014 §9:
- **Executor:** Marcus or Larry
- **Reviewer:** Larry
- **Final approval:** Owner Walter Kamer

Each Workstream file has a `**Maintainer:**` field naming the agent responsible for proposing updates when the underlying process changes. Maintainer is not the same as Executor — Maintainer notices when the WS is stale; Executor implements the change after approval.

### 8.6 Relationship to Tasks and Projects

A Workstream is non-actionable. It provides the orchestration context within which tasks live. Per the hierarchy: Goals → Projects → Workstreams → Tasks.

### 8.7 Relationship to AI-Team Agents

Each agent's AGENT.md may reference one or more Workstreams as workflow contracts. When Penn's AGENT.md states "if the contract and this file disagree, the contract wins" — that makes WS-001 an authoritative override, not supplementary guidance. Any step added to or removed from WS-001 that is not in Penn AGENT.md will change Penn's behavior. This requires careful content alignment and Owner approval before execution.

---

## 9. Proposed Changes

### Phase B-005A — Core Workstreams infrastructure

All changes in B-005A are documentation-only. No scripts, databases, backup folders, or integrations are touched.

**Risk classification: Low to medium.**
- Creating the folder and index is zero risk.
- Creating WS-001 is low to medium risk because Penn's AGENT.md designates it as the authoritative contract. WS-001 content provided below is derived directly from Penn's current AGENT.md to avoid introducing behavioral changes. If the content matches current Penn behavior, risk is low. If Owner approves content that differs from Penn AGENT.md, Penn's behavior will change accordingly — which may be intentional.
- The GL-004 routing rule addition is low risk — a small addition to a non-executable reference document.

**Mitigation:** exact content is provided below for Owner review before approval. After execution, the executor reads back all files and confirms no contradictions with Penn AGENT.md.

---

#### Change C-001: Create `Team Knowledge/Core/Workstreams/` folder

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/` |
| **Action** | Create the folder |
| **Reason** | Canonical path in GL-004 and GL-014 §8 does not exist |
| **Risk** | None |
| **Owner approval required** | Yes |

---

#### Change C-002: Create `WS-001_Daily journaling.md`

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/WS-001_Daily journaling.md` |
| **Action** | Create new file with the exact content below |
| **Reason** | Penn's AGENT.md designates this file as the authoritative workflow contract. It does not exist. |
| **Risk** | Low to medium — content must not contradict Penn AGENT.md |
| **Owner approval required** | Yes |

**Exact proposed content:**

```markdown
# WS-001 — Daily Journaling

**Domain:** Core (Personal)
**Trigger:** Owner delivers raw personal input directly, or Larry or Sienna routes a personal
narrative, reflection, life update, or observation to Penn.
**Maintainer:** Larry
**Status:** Active

---

## Purpose

Turn raw personal input from Owner Walter Kamer into structured PKM entries. The journal is
the Owner's personal memory backbone — every narrative, observation, reflection, or life
update lands here and becomes cross-linked into the rest of the PKM wiki.

This Workstream ensures that input capture, filing, cross-linking and memory extraction happen
in a consistent, auditable sequence regardless of which agent receives the input first.

---

## Agents

| Agent | Role in this Workstream |
|---|---|
| Larry | Receives Owner input; identifies journalable content; routes to Penn; performs Librarian pass at session close |
| Sienna | Identifies journalable content in personal domain sessions; routes to Penn |
| Penn | Processes all input; writes journal entries; cross-links; files entities; extracts UMC entities; writes session log |

---

## Inputs

- Raw text: personal narrative, reflection, day update, observation, or experience
- Image: screenshot, photo, business card
- Audio: voice note
- Document: PDF, scan

---

## Steps

### Step 1 — Route input to Penn

**Step lead:** Larry or Sienna (whichever receives the input first)
**Trigger:** Owner shares a personal narrative, day reflection, life update, observation, or
experience — even mid-conversation on another topic.
**Action:** Route immediately to Penn. Do not process the input before routing. Do not ask
permission to route.
**Passes to:** Step 2

---

### Step 2 — Write journal entry

**Step lead:** Penn
**Input:** Raw Owner input

For text input:
1. Write journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_subject 1, subject 2.md`
   — this is the only canonical location (see [[GL-004_Canonical paths]])
2. Write in the Owner's language (Dutch if Dutch, English if English)
3. Preserve the Owner's words and expressions; paraphrase only for structure
4. Remove repetitions; complete sentences; group related thoughts
5. Do not add opinions, interpretations or conclusions the Owner did not express
6. Create `YYYY/MM/` parent folders if they do not exist

For image input:
1. Save file to `PKM/Images/YYYY/MM/YYYYMMDD_description.ext`
2. Embed in journal entry: `![[Images/YYYY/MM/YYYYMMDD_description.ext]]`
3. If image shows a person: create or update `PKM/CRM/People/Achternaam, Voornaam.md`
4. If image shows an organization: create or update `PKM/CRM/Organizations/Naam.md`

For audio input:
1. Transcribe; if unable, write `[transcript pending]`
2. Process transcript as text input from step 2a above

For document input:
1. File to `PKM/Documents/` using `YYYYMMDD_Type_Persoon_Detail.ext`
2. Create stub in `PKM/Documents/` and link from journal entry

**Output:** Draft journal entry file
**Passes to:** Step 3

---

### Step 3 — People detection and bucket detection

**Step lead:** Penn

**People detection — for every name found:**
- New name: create stub at `PKM/CRM/People/Achternaam, Voornaam.md`; insert row in
  `personal.db` table `people` with `needs_review=true`
- Existing name: update `last_contact` in `personal.db` table `people`
- Every mention: insert row in `personal.db` table `contact_interactions` with
  `interaction_type='journal'`, `summary=one-line description`, `journal_id=inserted journal row id`
- Every mention: add wikilink to journal entry under `## Related to → Journal` in that
  person's CRM file. See [[GL-009_CRM people link consistency]].
- Gift idea or purchase wish → append to CRM stub as `Gift ideas: <item>`

**Bucket detection — map each signal to the right PKM location:**

| Signal | Destination |
|---|---|
| Interest / recurring subject | `PKM/My Life/Topics/T-Naam.md` |
| Time-bound effort | `PKM/My Life/Projects/P-Naam/` |
| Recurring rhythm or routine | `PKM/My Life/Habits/H-Naam.md` |
| Outcome or aspiration | `PKM/My Life/Goals/` |
| Stable life dimension | `PKM/My Life/Key Elements/KE-Naam.md` |
| Someday travel idea | `PKM/My Life/Ideas/I-Travel.md` |
| Someday experience idea | `PKM/My Life/Ideas/I-Experiences.md` |
| Someday purchase idea | `PKM/My Life/Ideas/I-Purchases.md` |
| Real-world document | `PKM/Documents/` |
| Image | `PKM/Images/YYYY/MM/` |

For Topics: add one-line entry under **What I am exploring right now** and append a dated line
to **Mentions log** linking to the journal entry. If no matching topic exists, create
`T-Naam.md` using the standard topic template.

Stub creation rule: if the entity has a name the Owner will refer to again, create the stub.
When in doubt, create it.

**Output:** Journal entry with resolved wikilinks; PKM stubs created or updated
**Passes to:** Step 4

---

### Step 4 — Database insert

**Step lead:** Penn
**Action:**
1. Run schema check: verify actual column names in `journal` table — the date column is
   `entry_date`, not `date`. Never assume column names.
2. Insert one row into `PKM/personal.db` table `journal`
   (`entry_date`, `title`, `entry_type`, `summary`)

**Output:** DB row inserted
**Passes to:** Step 5

---

### Step 5 — UMC entity extraction

**Step lead:** Penn

**Interpreter:** `/opt/mypka-memory/venv/bin/python`

```python
import sys, os
sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
from memory_config import get_dsn
os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
from memory_manager import get_manager
mm = get_manager()

# Extract entities from journal entry (Layer 2 — Entity)
entities = mm.extract_and_store_entities(journal_entry_text)

# Store insight as conversation memory (Layer 6 — Conversation)
mm.icor_refine(
    layer='conversation',
    content='Insight: [pattern or observation from the entry].',
    agent='penn',
    topic='journal-insight',
    date_ref='YYYY-MM-DD'
)
```

If UMC is unreachable: skip and report "⚠️ UMC niet bereikbaar" to the Owner. Report entity
count only if >0.

**Output:** Entities stored in UMC; conversation layer updated
**Passes to:** Step 6

---

### Step 6 — Close journal entry: learning reflections and KE-check

**Step lead:** Penn
**Action:**
1. Close the journal entry with 1–3 learning reflections: patterns observed, open questions,
   connections to goals/topics/people. These are Penn's observations, not the Owner's words.
2. Mandatory KE-check: verify whether the entry connects to an active Key Element in
   `PKM/My Life/Key Elements/` and add the connection if applicable.

**Output:** Journal entry complete with reflections and KE connection
**Passes to:** Step 7

---

### Step 7 — Session log

**Step lead:** Penn
**Action:** Write one row to `Team Knowledge/team-knowledge.db` table `session_logs` with
`agent_slug="penn"`.

**Output:** Session log row written
**Passes to:** Step 8 (Larry — at session close)

---

### Step 8 — Librarian pass

**Step lead:** Larry
**Trigger:** Session close
**Action:**
1. Verify all `[[wikilinks]]` in the new journal entry resolve
2. Confirm images sit in `PKM/Images/YYYY/MM/`, not duplicated elsewhere
3. Confirm each new stub is listed in its section's index file where applicable
4. Flag any SSOT violations to Owner Walter Kamer

**Output:** Structural integrity confirmed or violations flagged to Owner

---

## Outputs

- Journal entry at `PKM/Journal/YYYY/MM/YYYYMMDD_subject 1, subject 2.md`
- Updated PKM stubs (CRM, Topics, Goals, Projects, Habits, Key Elements, Documents as applicable)
- `personal.db` rows: journal insert, people updates, contact_interactions
- UMC: entity and conversation layer updates
- `team-knowledge.db` session log row

---

## What this Workstream does not do

- Does not produce business workflows — business process inputs are routed to the relevant
  domain agent; Penn writes a short journal note linking to it
- Does not produce research reports — route to Pax
- Does not edit past journal entries — entries are append-only
- Does not replace Sienna's behavioral accountability role
- Does not add interpretations, opinions or conclusions the Owner did not express
- Does not skip any step — bucket detection and wikilink cross-linking run on every input
  without exception

---

## References

- [[GL-001_File naming conventions]] — filenames for journal entries, images, documents
- [[GL-004_Canonical paths]] — all canonical PKM folder paths
- [[GL-009_CRM people link consistency]] — CRM update rule on every person mention
- [[SOP-008_Read own journal before task]] — Penn reads prior task journal before processing
- [[SOP-009_Write journal entry after task]] — Penn's specialist journal for task-level learnings

---

## Changelog

- 2026-06-03 (Larry, B-005A): Created. Derived from Penn AGENT.md and Larry AGENT.md current
  state. Approved by Owner Walter Kamer.
```

---

#### Change C-003: Create `workstream-index.md` for Core

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Workstreams/workstream-index.md` |
| **Action** | Create file with the exact content below |
| **Reason** | Analogous to `SOP-index.md`; required to make the Workstream layer discoverable |
| **Risk** | None |
| **Owner approval required** | Yes (same pass as C-001 and C-002) |

**Exact proposed content:**

```markdown
# Workstream Index — Core

All Core Workstreams are listed here. Every new Core Workstream must be added when created.
If a process is not in this index, it does not officially exist.

| Nr | Title | File | Status |
|---|---|---|---|
| WS-001 | Daily journaling | WS-001_Daily journaling.md | Active |
```

---

#### Change C-004: Add Workstream routing rule and Changelog to GL-004

| | |
|---|---|
| **Path** | `Team Knowledge/Core/Guidelines/GL-004_Canonical paths.md` |
| **Action** | Add a routing rule note after the Team structure table, and add a Changelog section at the end of the file |
| **Reason** | F-008: Core vs Domain distinction is undocumented. F-009: GL-004 has no Changelog section (required by GL-014 §5). |
| **Risk** | Low — addition to a non-executable reference document |
| **Owner approval required** | Yes — GL modification |

**Exact insertion 1 — routing rule:**

Insert after the `**Regel:**` note about Team Inbox (`Team Inbox/ heeft geen domeinsubmappen...`), before the `**Scaffold-afwijking:**` note. Note: these are existing Dutch section labels in GL-004, which has not yet been fully translated; the insertion text itself is in English.

```
**Workstream routing:** Core Workstreams (`Team Knowledge/Core/Workstreams/`) hold
cross-domain agent orchestrations managed by Larry or Marcus. Domain Workstreams
(`Team Knowledge/<Domain>/Workstreams/`) hold domain-specific operational flows managed by
domain specialists.
```

**Exact insertion 2 — Changelog section:**

Append at end of file, after the path-change protocol section:

```markdown
---

## Changelog

- 2026-06-03 (Larry, B-005A): Added Workstream routing rule (Core vs Domain distinction).
  Added this Changelog section. Approved by Owner Walter Kamer.
```

---

#### B-005A Language Compliance Check

Language check performed on all exact B-005A proposed content: `WS-001_Daily journaling.md`, `workstream-index.md`, GL-004 insertion text, and all changelog entries.

| Item | Location | Status | Notes |
|---|---|---|---|
| `YYYYMMDD_beschrijving.ext` | WS-001 Step 2, image input (2 occurrences) | **Fixed in v0.3** | Replaced with `YYYYMMDD_description.ext` |
| `Achternaam, Voornaam.md` | WS-001 Step 2 and Step 3 | Preserved — convention reference | Dutch PKM naming convention from GL-001 (CRM People path pattern). Changing in WS-001 without changing GL-001 and Penn AGENT.md would create inconsistency. Pending GL-001 full translation. |
| `PKM/CRM/Organizations/Naam.md` | WS-001 Step 2, image input | Preserved — convention reference | Matches Penn AGENT.md current state. Pending GL-001/Penn cleanup. |
| `T-Naam.md`, `P-Naam/`, `H-Naam.md`, `KE-Naam.md` | WS-001 Step 3, bucket detection table | Preserved — convention references | Dutch PKM naming prefix conventions from GL-001. Consistent with Penn AGENT.md. Pending GL-001 full translation. |
| `YYYYMMDD_Type_Persoon_Detail.ext` | WS-001 Step 2, document input | Flagged — pre-existing | Dutch `Persoon` in document naming pattern. Present in Penn AGENT.md (not translated in B-029 scope). Reproduced verbatim for consistency. Requires separate Penn AGENT.md cleanup; out of scope for B-005A. |
| `"⚠️ UMC niet bereikbaar"` | WS-001 Step 5, UMC section | Preserved — user-facing Dutch output | Intentionally Dutch per GL-014 §10 exception. Confirmed in B-029 execution. |
| `Pad-wijziging`, `Scaffold-afwijking` | C-004 positioning instructions | Noted — reference only | These are existing Dutch section names in GL-004, referenced to tell the executor where to insert. The insertion text itself is English. GL-004 full translation is a separate item. |
| All section headings | WS-001, workstream-index.md, GL-004 insertions | English ✓ | |
| All field labels | WS-001 (`**Step lead:**`, `**Maintainer:**`, etc.) | English ✓ | |
| All changelog entries | WS-001, GL-004 | English ✓ | |
| All other instructions and body text | WS-001, workstream-index.md, GL-004 insertions | English ✓ | |

**Result:** One Dutch placeholder fixed. All remaining Dutch items are either convention references from GL-001/Penn AGENT.md (intentionally preserved for consistency), a pre-existing naming pattern from Penn AGENT.md (flagged, out of scope), or user-facing Dutch output (intentionally preserved). No further language compliance changes are required in the B-005A exact content.

---

### Phase B-005B — Workstream template (separate phase)

#### Change C-005: Create `workstream.md` template and update Templates INDEX.md

| | |
|---|---|
| **Paths** | `Team Knowledge/Templates/workstream.md` and `Team Knowledge/Templates/INDEX.md` |
| **Action** | Create template file; add entry to INDEX.md |
| **Note** | Exact template content is not provided in this proposal. B-005B requires its own proposal with exact content before execution. The structure in §8.4 of this proposal may serve as the starting point. |
| **Risk** | None |
| **Owner approval required** | Yes — separate from B-005A |

---

### Phase B-005C — KE language compliance (separate phase)

#### Change C-006: Translate KE WS-001 to English

| | |
|---|---|
| **Path** | `Team Knowledge/Kamer E-commerce/Workstreams/WS-001_Kamer E-commerce operationeel procesframework.md` |
| **Note** | B-005C requires a dedicated proposal with the exact English replacement text for every section before execution. No translation may be executed without that proposal and Owner approval. Operational content must be preserved exactly; this is a language compliance update only. |
| **Risk** | Low — language compliance update. However, the file is long and contains domain-operational detail; exact replacement text must be reviewed before applying. |
| **Owner approval required** | Yes — requires dedicated proposal first |

---

### Deferred — Owner decision required (see §10)

#### Change C-007: Create `WS-002_Health habit coaching.md`

Lena's coaching orchestration. Lena explicitly acknowledges the gap and designates AGENT.md as the temporary fallback. Risk is contained. Requires Owner decision on whether to define it now. If approved: requires a separate proposal with exact content.

#### Change C-008: First Workstream for Geldstroom Regie

GR Workstreams folder is empty. Finn is the GR domain specialist. Requires Owner decision on whether a GR Workstream should be defined now, and if so, which process to document first. If approved: requires a separate proposal with exact content.

---

## 10. Items Requiring Owner Decision

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve Phase B-005A? (folder + WS-001 + index + GL-004 change) | a) Approve b) Defer | Fixes Penn broken contract; activates Core Workstreams layer |
| 2 | Review exact WS-001 content: does it match current Penn behavior? | a) Approve as written b) Request content changes | Content changes will change Penn's behavior — Owner's call |
| 3 | Approve Phase B-005B? (workstream template — separate proposal needed) | a) Commission B-005B proposal b) Defer | Consistency for future WS creation |
| 4 | Approve commissioning B-005C? (exact KE WS-001 translation proposal) | a) Commission b) Defer | Language compliance for one existing WS |
| 5 | Create WS-002 Health Habit Coaching now or defer? | a) Commission separate proposal b) Defer | Lena currently functional without it |
| 6 | First GR Workstream: define now or defer? | a) Commission separate proposal (which process?) b) Defer | GR domain growing but not blocked |
| 7 | Who executes B-005A? | a) Larry b) Marcus | Both are listed executors in GL-014 §9 |

---

## 11. Risk Assessment

| Change | Risk if applied | Risk if not applied |
|---|---|---|
| C-001: Create Core folder | None | Penn reference permanently unresolvable |
| C-002: Create WS-001 | Low–medium: content matches AGENT.md = low; content differs = Penn behavior changes. Mitigated by exact content review + Owner approval. | Penn has no workflow contract; AGENT.md may drift without correction over time |
| C-003: Create Core index | None | No discoverable registry of Core Workstreams |
| C-004: GL-004 routing rule + Changelog | Low — small addition + missing section added | Core vs Domain ambiguity; GL-004 non-compliant with GL-014 §5 |
| C-005: Workstream template (B-005B) | None | Inconsistent WS files as team grows |
| C-006: KE WS-001 English (B-005C) | Low — language only; mitigated by exact replacement proposal | Language rule drift |
| C-007: Lena WS-002 | Low–medium: same authoritativeness risk as WS-001 | Lena operating without contract; acceptable short-term |
| C-008: GR first WS | Low | GR has no documented recurring orchestrations |

**Overall risk of B-005A: Low to medium, fully mitigated by:**
1. Exact WS-001 content derived from Penn's current AGENT.md — no new steps introduced
2. Language compliance check completed — one placeholder fixed, all remaining items documented
3. Owner reviews exact content before approval
4. Read-back verification after execution confirms no AGENT.md contradictions

---

## 12. Recommended Execution Plan

After Owner's explicit approval per phase:

**Phase B-005A — Core Workstreams infrastructure:**
- Executor: Larry (or Marcus)
- Reviewer: Larry
- Sequence:
  1. Create `Team Knowledge/Core/Workstreams/` folder
  2. Create `WS-001_Daily journaling.md` using exact content from §9
  3. Create `workstream-index.md` using exact content from §9
  4. Edit `GL-004_Canonical paths.md` using exact insertion text from §9
- Post-checks:
  - Read back WS-001 in full — confirm no contradictions with Penn AGENT.md
  - Read back workstream-index.md — confirm WS-001 is listed
  - Read back GL-004 — confirm routing rule and Changelog are present
  - Confirm `Team Knowledge/Core/Workstreams/` folder exists on disk
- Audit trail: changelog in WS-001 and GL-004; team_log entry; session log per GL-014 §6

**Phase B-005B — Workstream template:**
- Requires a separate proposal with exact `workstream.md` content and INDEX.md update
- Not part of B-005A approval scope

**Phase B-005C — KE WS-001 language compliance:**
- Requires a separate proposal with the full English translation of every section
- Not part of B-005A approval scope

**Deferred phases:**
- B-005D: Lena WS-002 — requires separate proposal with exact content if Owner approves
- B-005E: GR first Workstream — requires Owner decision on which process, then separate proposal

---

## 13. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. No folder has been created. No database has been touched. The execution plan in §12 is not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of B-005A is an approval of the exact content provided in §9 of this document. Any content change to WS-001 after approval but before execution requires a separate approval.

---

## 14. Final Recommendation

**B-005A is ready for Owner approval.**

The exact content for all four B-005A changes is provided in §9. A full language compliance check has been performed. One Dutch placeholder was fixed (`beschrijving` → `description`). All remaining Dutch items are either GL-001 convention references preserved for consistency with Penn AGENT.md (pending GL-001 full translation), a pre-existing naming pattern from Penn AGENT.md (flagged, out of scope), or user-facing Dutch output intentionally preserved per GL-014 §10. No further changes are required before Owner review.

Owner Walter Kamer reviews the exact WS-001 content in §9, confirms it matches expected Penn behavior, and approves B-005A for execution. Penn's broken workflow contract — the only current high-risk gap — is resolved by executing C-001 and C-002.

B-005B (template) and B-005C (KE translation) are follow-up phases and can be commissioned as separate proposals after B-005A. Lena WS-002 and Geldstroom Regie Workstream remain deferred pending Owner decision.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-005-workstreams-start-proposal-v03.md`*
