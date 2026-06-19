# SOP-019 Initiation Proposal — Learning Candidate 6

**Type:** Governance Initiation Proposal
**Version:** v01
**Status:** Draft — Awaiting Iris Review
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-07
**Learning Candidate id:** 6
**Learning Candidate title:** Batch-stop rules declared in write-lists are not automatically inherited by the executing agent brief
**Learning Candidate category:** CAT-3
**Learning Candidate status:** triaged / graduation_candidate

---

## 1. SOP-019 Track Identification

**Track:** 2 of 2 (this session)
**Track reference:** `team_tasks` id=83 — "Initiate SOP-019 Track 2: CLAUDE.md amendment for Larry execution briefing rule (LC-6)"
**Track 1 reference:** `team_tasks` id=82 — LC-5 + LC-7, GL amendment for post-check script standards (not started, not in scope here)

This proposal covers Track 2 only. Track 1 is separate and has not been initiated.

**SOP-019 phase invoked:** Initiation and proposal preparation (read-only step, no write actions).

---

## 2. LC-6 Source and Current State

**Source:** Iris flagged during LC Batch 2 write-list review.

**Database record (team-knowledge.db, table: learning_candidates, id=6):**

| Field | Value |
|---|---|
| id | 6 |
| title | Batch-stop rules declared in write-lists are not automatically inherited by the executing agent brief |
| description | During LC Batch 2 write-list reviews, Iris flagged that batch-stop rules are documented in the write-list but are not automatically included in the execution brief presented to the executor. If the executor does not read the full write-list, batch-stop rules are silently absent from the execution context. Larry must explicitly include batch-stop rules in every execution brief rather than relying on the executor to derive them from the write-list. |
| level | 2 |
| category | CAT-3 |
| flagged_by | iris |
| status | triaged |
| triage_routing | graduation_candidate |
| processed_outcome | NULL |
| learning_scope | governance |
| source_domain | core |

**Current state:** triaged, graduation_candidate, not yet processed. No write actions have been taken on this LC.

---

## 3. Problem Statement

### What the gap is

Write-lists produced in governed execution sessions contain batch-stop rules: conditions under which execution halts if a preceding action fails, produces an unexpected result, or triggers a defined flag. These rules are critical safety gates for multi-step execution.

When Larry prepares an execution brief for a specialist (e.g., to carry out approved write actions), the brief is created from Larry's orchestration understanding of the task — not by copying the write-list verbatim. Batch-stop rules live in the write-list. They do not automatically transfer to the execution brief unless Larry explicitly puts them there.

If the executing specialist does not read the full write-list independently, those rules are silently absent from the execution context. The specialist proceeds as if no halting conditions exist.

### Why this is a governance risk

Batch-stop rules are the last line of defence against cascading write failures within a single batch. A specialist acting without them may continue writing after a preceding action has already failed or produced an unexpected state. This can corrupt system files, create inconsistent database rows, or require manual recovery.

The pattern is invisible at brief-creation time. The brief looks complete. The gap only surfaces when execution encounters a condition that the batch-stop rule was designed to catch.

### When this pattern was observed

During LC Batch 2 execution in the previous session (2026-06-07). The session log records this as Learning Candidate 6.

---

## 4. Proposed Destination

**File:** `CLAUDE.md`
**Section:** `## Hard Rules`
**Placement:** New subsection, inserted after the existing "Domain Check Before Execution — verplicht" subsection.

**Rationale for placement:** Domain Check is the highest-priority orchestration constraint in Hard Rules. The execution briefing rule is a sibling constraint: it governs a specific Larry briefing action, not a domain-routing decision. Placing it immediately after Domain Check groups the two orchestration-lane constraints together at the top of Hard Rules.

---

## 5. Proposed Rule Text

The following text is proposed for insertion into `CLAUDE.md`, under `## Hard Rules`, as a new subsection titled `### Execution Briefing — Batch-Stop Rules (verplicht)`:

---

### Execution Briefing — Batch-Stop Rules (verplicht)

When Larry prepares an execution brief for any specialist: all batch-stop rules from the associated write-list must be explicitly included in the brief. Batch-stop rules declared in a write-list are not automatically inherited by the execution brief. The executor does not read the full write-list before acting unless explicitly required — silent absence of batch-stop rules in the brief creates an undetected execution risk.

**What a batch-stop rule is:** any condition that halts execution of subsequent write actions within the same batch if a preceding action fails, produces an unexpected outcome, or triggers a defined flag.

**Trigger bij schending:** zodra Larry een execution brief opstelt terwijl de bijbehorende write-list batch-stop regels bevat die niet in de brief zijn opgenomen — stop, herstel de brief voor uitvoering, benoem de correctie naar de owner.

---

This text is proposed, not approved. It is included here for Iris review and Owner authorization before any write action.

---

## 6. Why This Belongs in CLAUDE.md and Not GL or SOP

**Not a GL (Guideline):** Guidelines are static reference documents — classification schemes, canonical paths, naming conventions. The execution briefing rule is an active behavioral constraint on Larry's orchestration actions. It must fire every time Larry creates an execution brief. A GL would be the wrong read surface — Larry reads CLAUDE.md Hard Rules on every action, not a GL file.

**Not a SOP:** SOPs define multi-step atomic procedures for recurring workflows. This rule is a single-sentence behavioral requirement embedded in briefing, not a standalone procedure. There is no sequence of steps to follow — there is one obligation: include batch-stop rules in the brief. A dedicated SOP would add structural weight to a rule that belongs as a standing operational constraint.

**Yes to CLAUDE.md Hard Rules:** Hard Rules are always-active Larry behavioral constraints. They govern Larry's lane directly and are enforced at every action. The existing Hard Rules include Domain Check Before Execution (routing constraint) and the SSOT Golden Rule (content constraint). The execution briefing rule is structurally identical in type: a single mandatory check Larry performs at a specific point in a recurring action. CLAUDE.md Hard Rules is the correct and complete home for this rule.

**Inheritance consideration:** Once this rule is in CLAUDE.md Hard Rules, it is immediately active for Larry in every session. No downstream updates to GL, SOP, or AGENT.md files are required for the rule to take effect. It is self-contained.

---

## 7. Risk Assessment

| Risk | Description | Control |
|---|---|---|
| Overbroad scope | Rule could be read as requiring Larry to copy all write-list content into every brief, not just batch-stop rules | Rule text defines batch-stop rules explicitly: conditions that halt execution if a preceding action fails, produces an unexpected outcome, or triggers a flag. Scope is bounded. |
| No write-list present | Some execution briefs may not have an associated write-list | Rule triggers only "when Larry prepares an execution brief for any specialist" — implied that a write-list is associated. If no write-list exists, no batch-stop rules can be absent. Rule does not fire without a write-list. |
| Overlap with specialist responsibility | Specialists may feel the rule exempts them from checking the write-list themselves | Rule governs Larry's briefing obligation. It does not exempt specialists. If the executing specialist also reads the write-list, that is additional protection, not duplication. No conflict. |
| Scope creep in rule text | Rule could expand during review to include other write-list elements | Scope is fixed: batch-stop rules only. Any extension requires a new LC and separate Owner authorization. |
| Friction in fast-moving sessions | Rule adds a briefing step to every execution brief, potentially slowing sessions | The check is minimal: identify batch-stop rules in the write-list, include them in the brief. When no batch-stop rules exist in the write-list, the rule adds zero friction. |
| Ambiguity on what counts as a batch-stop rule | Executors and Larry may disagree on what is a batch-stop rule vs. a general instruction | Rule text provides a definition. The definition is precise enough for Larry to apply. If ambiguity arises in a specific case, the default is to include the rule in the brief rather than exclude it. |

---

## 8. Exact Files Expected to Be Changed Later (Not Now)

### Write actions in scope

| File | Required change | Notes |
|---|---|---|
| `CLAUDE.md` | Insert new subsection `### Execution Briefing — Batch-Stop Rules (verplicht)` under `## Hard Rules`, after "Domain Check Before Execution — verplicht" | Exact text defined in Section 5 of this proposal |

### Database rows in scope

| Database | Table | Action | Notes |
|---|---|---|---|
| `Team Knowledge/team-knowledge.db` | `team_tasks` | SET status='completed', completed_at=datetime('now') WHERE id=83 | After CLAUDE.md write is confirmed |
| `Team Knowledge/team-knowledge.db` | `learning_candidates` | SET status='processed', processed_outcome='graduated — CLAUDE.md Hard Rules amended', processed_at=datetime('now') WHERE id=6 | After CLAUDE.md write is confirmed |

### Files not in scope for this proposal

The following files are explicitly not changed by this proposal. Any future changes to these files require separate Owner authorization:

| File | Reason not in scope |
|---|---|
| `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md` | This proposal amends CLAUDE.md, not SOP-019 |
| Any `AGENT.md` file | Specialists derive batch-stop briefing behavior from Larry's CLAUDE.md rule, not their own AGENT.md |
| `Team Knowledge/Core/Guidelines/GL-019_Governance Gatekeeper Principles.md` | No GL change needed; the rule is behavioral, not a principle addition |
| Any index file | No new SOP, GL, or WS file is created by this proposal |
| `Team Knowledge/Core/SOPs/SOP-index.md` | No SOP is created or amended |

---

## 9. Proposed Future Write-Plan Structure

When the Owner authorizes execution, the write sequence is:

**Step 1 — Verify current state (read-only)**
Read `CLAUDE.md` Hard Rules section. Confirm "Domain Check Before Execution — verplicht" is present and identify the exact insertion point. Confirm no existing execution briefing rule is present (no duplication).

**Step 2 — Write to CLAUDE.md**
Insert the approved rule text as a new subsection under `## Hard Rules`, immediately after "Domain Check Before Execution — verplicht".

**Step 3 — Post-check CLAUDE.md**
Read back the modified Hard Rules section. Confirm: new subsection present, correct placement, text matches approved version exactly, no surrounding content displaced.

**Step 4 — Update team_tasks id=83**
SET status='completed', completed_at=datetime('now').

**Step 5 — Update learning_candidates id=6**
SET status='processed', processed_outcome='graduated — CLAUDE.md Hard Rules execution briefing rule added', processed_at=datetime('now').

**Step 6 — Session log**
Record: LC-6 processed, CLAUDE.md Hard Rules amended, batch-stop execution briefing rule added.

**Execution boundary:** Steps 2 through 6 are write actions. None execute until Owner authorization is confirmed after Iris review. Step 1 is read-only and may be performed at any time.

---

## 10. Required Iris Review Step Before Any Write

Iris review is mandatory before Owner authorization for this amendment because:

- It modifies CLAUDE.md, a live system file governing Larry's active behavior
- The rule introduces a new standing obligation in Larry's Hard Rules lane
- The proposed text must be assessed for: unintended scope expansion, conflict with existing Hard Rules (particularly Domain Check), ambiguity in the definition of batch-stop rules, and alignment with GL-020 intent classification
- Category CAT-3 mandates advisory review before Owner authorization (per GL-021)

**Iris does not authorize. Iris reviews and advises. Owner authorizes.**

If Iris is not available when this proposal is presented, Larry states this explicitly and presents the proposal to the Owner without Iris review. Owner authorization is still required.

**Iris review prompt (exact text for Larry to use):**

> Iris, please review the CLAUDE.md amendment proposal at `Deliverables/20260607_Core_SOP-019 LC-6 Execution Briefing Rule/lc-6-sop-019-initiation-proposal-v01.md`. The proposal adds a new Hard Rule subsection titled "Execution Briefing — Batch-Stop Rules (verplicht)" to CLAUDE.md, inserted after the existing "Domain Check Before Execution" subsection. Review for: (1) alignment with GL-020 intent classification, (2) conflict with existing Hard Rules, especially Domain Check Before Execution, (3) ambiguity in the batch-stop rule definition, (4) unintended scope expansion, (5) execution risk. This is advisory review only. Do not authorize. Return your findings for Larry to present to the Owner.

---

## 11. Required Owner Authorization Step Before Any Write

After Iris review, Larry presents the reviewed proposal to the Owner.

Per GL-021 Section 3, no persistent write action executes without explicit Owner authorization. This applies to all write actions in the write-plan (Section 9, Steps 2 through 6).

**Owner presentation format:** Larry summarizes the proposal and Iris findings in a single block. The Owner responds with one of:

- **Ja** — proceed with execution as proposed
- **Nee** — do not proceed; proposal is closed
- **Correctie** — specify what to change; Larry creates v02 and Iris reviews again before re-presenting

A prior "yes" in a different context does not authorize this write. Explicit confirmation is required.

---

## 12. Post-Check Requirements for the Eventual Write

After CLAUDE.md is modified, Larry performs the following checks before marking the task complete:

| Check | Pass condition |
|---|---|
| Rule present in Hard Rules | The new subsection `### Execution Briefing — Batch-Stop Rules (verplicht)` appears under `## Hard Rules` in CLAUDE.md |
| Correct placement | New subsection is immediately after "Domain Check Before Execution — verplicht" |
| Text matches approval | Rule text matches the approved version from this proposal (or v02+ if a correction was applied) exactly |
| No displacement | Surrounding Hard Rules subsections (SSOT Golden Rule etc.) are intact and unmodified |
| No duplication | The rule text does not appear elsewhere in CLAUDE.md |
| team_tasks id=83 closed | status='completed' confirmed |
| LC-6 processed | status='processed', processed_outcome set, confirmed |

If any check fails: stop, do not proceed to database updates, report the failure to the Owner.

---

## 13. No System Files Were Modified in This Step

This proposal is a read-only initiation document.

**No system files were created, modified, or deleted in this step.**
**No database rows were inserted, updated, or deleted in this step.**
**No CLAUDE.md changes were made.**
**No SOP, GL, or AGENT.md files were touched.**
**team_tasks id=83 remains open (status='open').**
**learning_candidates id=6 remains at status='triaged'.**

The only output of this step is the deliverable file at:
`Deliverables/20260607_Core_SOP-019 LC-6 Execution Briefing Rule/lc-6-sop-019-initiation-proposal-v01.md`

---

## 14. Next Step Recommendation

**Recommended next step: Iris review of this proposal.**

This proposal is complete. The next action is to invoke Iris review using the exact prompt in Section 10. After Iris returns findings, Larry presents the reviewed proposal to the Owner for authorization.

**Iris review does not require Owner action.** Larry invokes Iris directly using the prompt in Section 10.

**The Owner is next asked to act only after Iris findings are in hand** — at the authorization step (Section 11).

Do not proceed to the write-plan (Section 9 Step 2 onward) without completing both the Iris review step and the explicit Owner authorization step.

---

*Prepared: 2026-06-07*
*Delivered on: 2026-06-07*
*Delivered at: Larry, read-only initiation step*
