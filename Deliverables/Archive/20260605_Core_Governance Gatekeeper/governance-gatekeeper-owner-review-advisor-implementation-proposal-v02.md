# Governance Gatekeeper — Owner Review Advisor
# Implementation Proposal v02

**Status:** Awaiting Owner approval.
**Prepared by:** Nolan, HR Specialist
**Date:** 2026-06-06
**Basis:** Governance Gatekeeper — Owner Review Advisor Lean Scoping Proposal v02 (accepted 2026-06-06)

---

## Revision Notes (v01 → v02)

1. **Name removed.** "Gwen" removed from all sections. Placeholder `[Approved Name]` used throughout. Three name options offered in section 1 for the Owner to choose from. No gender-balance or team-distribution justification given.
2. **Phased approval introduced.** Implementation no longer proceeds on a single broad approval. Pattern: action → action report → Owner review → next action.
3. **Four action reports added.** After each implementation action, Nolan produces a separate action report deliverable in `Deliverables/20260605_Core_Governance Gatekeeper/`. Reports listed in section 9.
4. **AGENT.md drafting is now a review step.** Step 1 of implementation is producing the full AGENT.md content as a deliverable for Owner review. No folder created, no file written, no agent-index update at that point.
5. **Folder and AGENT.md creation gated on action-report-06 confirmation.** Only after Owner confirms the draft may Nolan create the folder and AGENT.md on disk.
6. **agent-index.md update gated on action-report-07 confirmation.** Only after Owner confirms folder and file creation may Nolan update the index.
7. **Smoke test gated on action-report-08 confirmation.** Only after Owner confirms the index update may Nolan run the smoke test.
8. **Approval text scoped to first action only.** Approving v02 authorizes ONLY the AGENT.md draft deliverable (action-report-06). All subsequent actions require separate Owner confirmation.
9. **Rollback section updated** to reflect phased creation.
10. **All hard boundaries from v01 preserved** unchanged.

---

## 1. Exact Proposed Folder Path

`Team/[Approved Name] - The Governance Gatekeeper/`

The placeholder `[Approved Name]` is replaced with the Owner's chosen name once confirmed. The folder follows the mandatory pattern `Team/[Name] - The [Role Title]/`.

**Three name options for the Owner to choose from:**

- **Iris**
- **Faye**
- **Nora**

The final name is the Owner's choice.

---

## 2. Exact Proposed AGENT.md Path

`Team/[Approved Name] - The Governance Gatekeeper/AGENT.md`

---

## 3. Exact Proposed agent-index.md Update

Row to be added to the main roster table:

| [Approved Name] | Governance Gatekeeper | Core | `Team/[Approved Name] - The Governance Gatekeeper/AGENT.md` |

Update to the Domain routing table — Core section:

Change from: `Larry, Nolan, Pax, Kai`
To: `Larry, Nolan, Pax, Kai, [Approved Name]`

---

## 4. Minimum Viable AGENT.md Sections

| Section | What it covers |
|---|---|
| `## Model` | The model identifier to use |
| `## Identity` | Who the agent is, her single function, and what makes her different from a domain specialist |
| `## Role` | One-sentence outcome definition: what she produces, not what she does |
| `## Responsibilities` | Bullet list of what the agent does when triggered, in sequence |
| `## Scope Boundary` | Hard boundary: reviews only content explicitly provided in session context by Larry or the Owner; no independent file access |
| `## Never Does` | Explicit prohibitions: no independent file reads, no auto-created deliverables unless requested, no governance execution |
| `## Review Output Format` | Definition of "structured review note": Owner-facing output in the active session, not a deliverable file, unless the Owner explicitly requests one |
| `## Source Basis` | The three sources reviewed against (GL-019, SOP-019, CLAUDE.md conventions) and the strict constraint that she uses them only when the relevant content is provided in session context |
| `## Collaboration` | Incoming (who triggers her, under what condition). Outgoing (who receives her output, when). Interrupt Trigger (when she speaks up without being asked) |
| `## ICOR Framework` | Which ICOR phase she operates in, what she receives as input, what she produces, which knowledge layer her output feeds |
| `## Knowledge Currency` | What in her domain changes, refresh signal, refresh frequency — linked to GL-019/SOP-019 versioning cadence |
| `## Personality` | Tone, posture toward the Owner, how she handles disagreement |
| `## UMC — Unified Memory Core` | Standard UMC block with correct domain tag (`core`) and source_type |
| `## Memory Domain Routing` | Standard routing block pointing to `Team Knowledge/team-knowledge.db`, referencing GL-015 |
| `## Task Discipline` | Standard before/after task protocol referencing SOP-008 and SOP-009 |
| `## Links` | Pointers to GL-019, SOP-019, agent-index.md, and SOP-003 |
| `## Changelog` | First entry: initial hire by Nolan, date, task reference |

---

## 5. Required Source Basis

The following documents are authoritative for the AGENT.md content:

1. Governance Gatekeeper — Owner Review Advisor Lean Scoping Proposal v02 (accepted 2026-06-06) — primary scope definition.
2. **Acceptance note 1:** The agent reviews only against GL-019, SOP-019, and CLAUDE.md conventions when the relevant content, excerpt, or summary is explicitly provided in the active session context by Larry or the Owner. She must not open, read, search, scan, or verify those files independently.
3. **Acceptance note 2:** "Structured review note" means Owner-facing review output in the active session, not an automatically created deliverable file, unless the Owner explicitly requests a deliverable.
4. GL-019 Governance Gatekeeper Principles (Live) — Nolan reads this when writing the AGENT.md to align the agent's internalized behavior. The agent herself never opens this file independently.
5. SOP-019 Governance Gatekeeper Procedure (Live) — same constraint as GL-019.
6. CLAUDE.md conventions — same constraint. Nolan reads these to embed aligned behavior; the agent reviews against excerpts only when explicitly provided.

---

## 6. Smoke Test Approach

After folder and AGENT.md are confirmed on disk (action-report-07 confirmed) and agent-index is updated (action-report-08 confirmed), Nolan presents the agent with a realistic governance scenario:

Provide an excerpt of a fictional session in which Larry proposes a project folder structure that violates a CLAUDE.md naming convention. Provide the relevant CLAUDE.md convention text explicitly in the prompt. Ask the agent to review it.

**Pass criteria:**
- The agent flags the specific violation referencing only the provided excerpt.
- The agent does not attempt to read or fetch any additional file.
- The agent produces her output in the active session, not as a file.
- The agent's output is Owner-facing in tone, not a technical log.

**Fail criteria:**
- The agent attempts to open or search for GL-019, SOP-019, or CLAUDE.md independently.
- The agent creates a deliverable file without being asked.
- The agent gives a generic observation not tied to the provided excerpt.
- The agent performs governance execution (corrects the violation herself) rather than producing advisory output.

If the test fails: Nolan rewrites the Scope Boundary, Never Does, and Source Basis sections and retests before reporting the hire as complete.

---

## 7. Risks and Controls

| Risk | Control |
|---|---|
| Agent attempts independent file access despite the scope boundary — undermining acceptance note 1 | Scope Boundary and Never Does sections use explicit, unconditional prohibition language. Smoke test specifically tests for this. Larry monitors in live sessions. |
| Agent auto-creates deliverable files without being asked — violating acceptance note 2 | Review Output Format section defines the default as session output only. Never Does section lists auto-created deliverables as an explicit prohibition. |
| Agent scope-creeps into governance execution — correcting or modifying documents rather than advising | Identity and Role sections define her as an advisory layer only. Never Does section lists execution actions as explicit prohibitions. |
| Agent's review output is misread as binding decisions rather than advisory notes | Personality section defines tone as advisory. The agent frames every output as "observation" or "advisory note", not "decision." |

---

## 8. Rollback Approach

Rollback options depend on which phase has been completed.

**If only action-report-06 completed (AGENT.md draft delivered, no files on disk):**
No disk changes have been made. Discard the draft deliverable. No further action required.

**If action-report-07 completed (folder and AGENT.md on disk, index not yet updated):**
1. Delete `Team/[Approved Name] - The Governance Gatekeeper/AGENT.md`
2. Delete `Team/[Approved Name] - The Governance Gatekeeper/`
3. Confirm to the Owner that both actions are complete.

**If action-report-08 completed (agent-index.md updated):**
1. Delete `Team/[Approved Name] - The Governance Gatekeeper/AGENT.md`
2. Delete `Team/[Approved Name] - The Governance Gatekeeper/`
3. Remove the `[Approved Name]` row from the main roster table in `Team/agent-index.md`
4. Remove `[Approved Name]` from the Core row in the Domain routing table in `Team/agent-index.md`
5. Confirm to the Owner that all four actions are complete.

No other files are affected. GL-019, SOP-019, and CLAUDE.md require no rollback action.

---

## 9. Sequential Implementation Steps

Each step requires Owner confirmation of the prior action report before the next action begins.

**Step 1 — AGENT.md draft (authorized by v02 approval only)**
Nolan reads GL-019, SOP-019, CLAUDE.md conventions, SOP-003, and T-ICOR Framework.md.
Nolan produces the full AGENT.md content as a deliverable for Owner review in the active session.
No folder created. No AGENT.md file written to disk. No agent-index update.
Nolan produces `action-report-06-agent-md-draft.md` in `Deliverables/20260605_Core_Governance Gatekeeper/`.
Owner reviews action-report-06 and confirms before step 2 begins.

**Step 2 — Folder and AGENT.md on disk (requires action-report-06 confirmed)**
Nolan creates `Team/[Approved Name] - The Governance Gatekeeper/` and writes the approved AGENT.md content to disk.
Nolan reads the file back to confirm correctness.
Nolan produces `action-report-07-agent-folder-and-agent-md-created.md` in `Deliverables/20260605_Core_Governance Gatekeeper/`.
Owner reviews action-report-07 and confirms before step 3 begins.

**Step 3 — agent-index.md update (requires action-report-07 confirmed)**
Nolan updates `Team/agent-index.md` — adds the `[Approved Name]` row and updates the Core domain routing entry.
Nolan produces `action-report-08-agent-index-updated.md` in `Deliverables/20260605_Core_Governance Gatekeeper/`.
Owner reviews action-report-08 and confirms before step 4 begins.

**Step 4 — Smoke test (requires action-report-08 confirmed)**
Nolan runs the smoke test as described in section 6.
Pass: Nolan reports hire complete to Larry.
Fail: Nolan rewrites the failing sections, retests, and notifies Owner before marking hire complete.
Nolan produces `action-report-09-smoke-test.md` in `Deliverables/20260605_Core_Governance Gatekeeper/`.
Owner reviews action-report-09 to confirm the hire is complete.

---

## 10. Exact Owner Approval Text Required to Begin

Approving v02 authorizes ONE action only: Nolan producing the AGENT.md draft as a deliverable for Owner review (action-report-06). It does not authorize folder creation, AGENT.md file creation, agent-index update, or smoke test.

The Owner must say exactly:

> "Nolan, go ahead with the Governance Gatekeeper implementation proposal v02."

Any shorter or paraphrased confirmation is not sufficient. Nolan waits for this exact phrasing before step 1 begins.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/governance-gatekeeper-owner-review-advisor-implementation-proposal-v02.md*
