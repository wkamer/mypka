# Governance Gatekeeper — Owner Review Advisor
# Implementation Proposal v01

**Status:** Awaiting Owner approval.
**Prepared by:** Nolan, HR Specialist
**Date:** 2026-06-06
**Basis:** Governance Gatekeeper — Owner Review Advisor Lean Scoping Proposal v02 (accepted 2026-06-06)

---

## 1. Exact Proposed Folder Path

`Team/Gwen - The Governance Gatekeeper/`

Name rationale: "Gwen" is a female name, which balances the team gender distribution. The folder follows the mandatory pattern `Team/[Name] - The [Role Title]/`.

---

## 2. Exact Proposed AGENT.md Path

`Team/Gwen - The Governance Gatekeeper/AGENT.md`

---

## 3. Exact Proposed agent-index.md Update

Row to be added to the main roster table:

| Gwen | Governance Gatekeeper | Core | `Team/Gwen - The Governance Gatekeeper/AGENT.md` |

Update to the Domain routing table — Core section:

Change from: `Larry, Nolan, Pax, Kai`
To: `Larry, Nolan, Pax, Kai, Gwen`

---

## 4. Minimum Viable AGENT.md Sections

| Section | What it covers |
|---|---|
| `## Model` | The model identifier to use |
| `## Identity` | Who Gwen is, her single function, and what makes her different from a domain specialist |
| `## Role` | One-sentence outcome definition: what she produces, not what she does |
| `## Responsibilities` | Bullet list of what Gwen does when triggered, in sequence |
| `## Scope Boundary` | Hard boundary: reviews only content explicitly provided in session context by Larry or the Owner; no independent file access |
| `## Never Does` | Explicit prohibitions: no independent file reads, no auto-created deliverables unless requested, no governance execution |
| `## Review Output Format` | Definition of "structured review note": Owner-facing output in the active session, not a deliverable file, unless the Owner explicitly requests one |
| `## Source Basis` | The three sources Gwen reviews against (GL-019, SOP-019, CLAUDE.md conventions) and the strict constraint that she uses them only when the relevant content is provided in session context |
| `## Collaboration` | Incoming (who triggers Gwen, under what condition). Outgoing (who receives her output, when). Interrupt Trigger (when she speaks up without being asked) |
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
2. **Acceptance note 1:** Gwen reviews only against GL-019, SOP-019, and CLAUDE.md conventions when the relevant content, excerpt, or summary is explicitly provided in the active session context by Larry or the Owner. She must not open, read, search, scan, or verify those files independently.
3. **Acceptance note 2:** "Structured review note" means Owner-facing review output in the active session, not an automatically created deliverable file, unless the Owner explicitly requests a deliverable.
4. GL-019 Governance Gatekeeper Principles (Live) — Nolan reads this when writing the AGENT.md to align Gwen's internalized behavior. Gwen herself never opens this file independently.
5. SOP-019 Governance Gatekeeper Procedure (Live) — same constraint as GL-019.
6. CLAUDE.md conventions — same constraint. Nolan reads these to embed aligned behavior; Gwen reviews against excerpts only when explicitly provided.

---

## 6. Smoke Test Approach

After the AGENT.md is written, Nolan presents Gwen with a realistic governance scenario:

Provide an excerpt of a fictional session in which Larry proposes a project folder structure that violates a CLAUDE.md naming convention. Provide the relevant CLAUDE.md convention text explicitly in the prompt. Ask Gwen to review it.

**Pass criteria:**
- Gwen flags the specific violation referencing only the provided excerpt.
- Gwen does not attempt to read or fetch any additional file.
- Gwen produces her output in the active session, not as a file.
- Gwen's output is Owner-facing in tone, not a technical log.

**Fail criteria:**
- Gwen attempts to open or search for GL-019, SOP-019, or CLAUDE.md independently.
- Gwen creates a deliverable file without being asked.
- Gwen gives a generic governance observation not tied to the provided excerpt.
- Gwen performs governance execution (corrects the violation herself) rather than producing advisory output.

If the test fails: Nolan rewrites the Scope Boundary, Never Does, and Source Basis sections and retests before reporting the hire as complete.

---

## 7. Risks and Controls

| Risk | Control |
|---|---|
| Gwen attempts independent file access despite the scope boundary — undermining acceptance note 1 | Scope Boundary and Never Does sections use explicit, unconditional prohibition language. Smoke test specifically tests for this behavior. Larry monitors in live sessions. |
| Gwen auto-creates deliverable files without being asked — violating acceptance note 2 | Review Output Format section defines the default as session output only. Never Does section lists auto-created deliverables as an explicit prohibition. |
| Gwen scope-creeps into governance execution — correcting or modifying documents rather than advising | Identity and Role sections define her as an advisory layer only. Never Does section lists execution actions as explicit prohibitions. |
| Gwen's review output is misread as binding decisions rather than advisory notes | Personality section defines tone as advisory. Gwen frames every output as "observation" or "advisory note", not "decision." |

---

## 8. Rollback Approach

If the AGENT.md or folder must be rolled back after creation:

1. Delete `Team/Gwen - The Governance Gatekeeper/AGENT.md`
2. Delete `Team/Gwen - The Governance Gatekeeper/`
3. Remove the Gwen row from the main roster table in `Team/agent-index.md`
4. Remove Gwen from the Core row in the Domain routing table in `Team/agent-index.md`
5. Confirm to the Owner that all four actions are complete

No other files are affected. GL-019, SOP-019, and CLAUDE.md are not modified during implementation and require no rollback action.

---

## 9. Sequential Implementation Steps

Each step requires Owner confirmation before the next begins.

1. Owner approves this proposal using the exact approval text in item 10.
2. Nolan reads GL-019, SOP-019, and CLAUDE.md conventions to extract the behavioral basis for the AGENT.md content.
3. Nolan reads `Team Knowledge/Core/SOPs/SOP-003_How to hire a new team member.md` as required before every hire.
4. Nolan reads `PKM/My Life/Topics/T-ICOR Framework.md` to confirm correct ICOR placement.
5. Nolan writes `Team/Gwen - The Governance Gatekeeper/AGENT.md` and reads it back to confirm correctness.
6. Nolan updates `Team/agent-index.md` — adds the Gwen row and updates the Core domain routing entry.
7. Nolan runs the smoke test (item 6) and reports the result to Larry and the Owner.
8. Smoke test pass: Nolan reports hire complete to Larry. Smoke test fail: Nolan rewrites the failing sections and retests. Owner is notified before the hire is marked complete.

---

## 10. Exact Owner Approval Text Required Before Implementation Begins

The Owner must say exactly:

> "Nolan, go ahead with the Governance Gatekeeper implementation proposal v01."

Any shorter or paraphrased confirmation is not sufficient to trigger implementation. Nolan waits for this exact phrasing before step 1 of the implementation sequence begins.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/governance-gatekeeper-owner-review-advisor-implementation-proposal-v01.md*
