# Review Gate Protocol — SOP Proposal v01

**File:** `Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-sop-proposal-v01.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Status:** Formal proposal v01 — awaiting Owner decision
**Paired with:** `review-gate-protocol-gl-proposal-v01.md`

**Governance:** This document is read-only. No SOP file creation, no index update, no system-file
change, no database write, no backlog update, and no further governance work may be executed
without Owner Walter Kamer's explicit approval.

---

## 1. Proposed SOP Identity

| Field | Value |
|---|---|
| Proposed SOP number | SOP-016 |
| Basis for number | SOP-015 is the current highest entry in `Team Knowledge/Core/SOPs/SOP-index.md` as of 2026-06-04. SOP-016 is the next available number. |
| Proposed filename | `SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` |
| Proposed canonical path | `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` |
| Paired GL | GL-016 — Review Gate for Governance-Relevant Deliverables (see `review-gate-protocol-gl-proposal-v01.md`) |
| Execution order | GL-016 must exist on disk before SOP-016 implementation begins. This SOP references GL-016 by name and number. |

---

## 2. Implementation Scope

If Owner Walter Kamer approves this SOP proposal for implementation, the following actions are
performed — no more, no less:

1. Create the file `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` with the exact content from Section 4.
2. Add one row to `Team Knowledge/Core/SOPs/SOP-index.md` as specified in Section 5.

**Nothing else is created, modified, or deleted by this implementation.**

---

## 3. Explicit Exclusions

The following are explicitly not part of this SOP implementation:

- No GL-016 file is created by this implementation (separate proposal and execution)
- No update to any existing SOP, including SOP-015
- No update to GL-014 or any other GL
- No AGENT.md files modified
- No CLAUDE.md modified
- No database writes
- No UMC or memory-db entries
- No team_tasks or team_log entries
- No Workstream files created or modified
- No scripts modified

---

## 4. Exact Full SOP Content

The following is the verbatim text that will be written to
`Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md`
if this proposal is approved. No word, heading, or line may be changed at execution time.
Any amendment requires a new proposal version per SOP-015.

---

```
# SOP-016 — Review Gate Procedure for Governance-Relevant Deliverables

**Maintainer:** Larry, Team Orchestrator
**Created:** 2026-06-04
**Principle reference:** GL-016 (Review Gate for Governance-Relevant Deliverables)

---

## 1. Purpose

This SOP defines the step-by-step procedure for applying the review gate required by GL-016.
It covers three operating modes for different availability contexts, the review package format,
the 13 review checks, the Owner decision options, and the hard stop conditions.

This SOP is tool-agnostic. It applies to any system, agent, tool, script, automation,
orchestration layer, or human-assisted workflow that produces or reviews a governance-relevant
deliverable within the myPKA AI team.

---

## 2. Role Definitions

| Role | Definition |
|---|---|
| Producer | The system, agent, or workflow that created the deliverable |
| Reviewer | The system, agent, role, or person that evaluates the deliverable against the 13 checks |
| Orchestrator | Larry (or equivalent orchestration layer) — routes the deliverable, manages the review package, synthesizes findings for the Owner decision |
| Owner | Walter Kamer — provides the final decision; may not delegate the approval decision to any agent or system |

**Role separation rules:**

1. Producer and reviewer must not be the same role for governance-critical deliverables
   (system-file changes, database changes, migration plans, remediation plans, closure reports).
2. For lower-stakes deliverables (routine status reports, single-check execution confirmations),
   the orchestrator may act as reviewer with a documented rationale stating why a separate reviewer
   was not available or necessary.
3. Larry may orchestrate governance review but must not self-approve his own governance
   deliverables. If Larry produces a governance-relevant deliverable, use Mode 1 (external review)
   or assign a separate internal reviewer under Mode 2 wherever possible.
4. A passing internal review or self-review does not equal Owner approval. The Owner decision
   step is always required.

---

## 3. Mode 1 — External Review

Use Mode 1 when the deliverable is produced by one system or agent and a different external
reviewer is available (another AI system, a human reviewer, or a specialist outside the
producer's domain).

### Step 1 — Assemble the review package

The producer assembles a review package containing exactly these eight elements:

1. **Deliverable path** — exact file path of the deliverable
2. **Approved scope** — the exact scope that was authorized before work began; what was and was
   not permitted
3. **Decision needed** — a precise statement of what the reviewer is asked to assess
4. **Known risks or uncertainties** — anything the producer could not verify, any edge cases
   identified, any assumptions made
5. **Evidence used** — list of sources consulted, with their precedence level per GL-016 Rule 3
6. **Confirmation of no further work executed** — explicit statement that no execution,
   database write, system-file change, or backlog update was performed beyond producing this
   deliverable
7. **Requested review outcome** — what the producer expects back (pass/fail, annotated findings,
   amended version, or Owner decision packet)
8. **Copy-ready next instruction** — a single paragraph or bullet list the Owner or orchestrator
   can use verbatim to initiate the next step

### Step 2 — Reviewer applies the 13 checks

The reviewer applies all 13 checks from Section 6 of this SOP. Each check is marked pass, fail,
or uncertain with a one-line reason.

### Step 3 — Reviewer returns findings

The reviewer returns the completed 13-check findings to the orchestrator. The reviewer must not
execute any action. The reviewer returns findings only.

### Step 4 — Orchestrator packages Owner decision

The orchestrator assembles: deliverable path, 13-check results, list of any failures or
uncertainties, and the applicable Owner decision options from Section 7.

### Step 5 — Owner decides

Owner Walter Kamer selects a decision option. No further action proceeds without this decision.

---

## 4. Mode 2 — Internal Multi-Agent Review

Use Mode 2 when the deliverable is produced inside the AI team and a different specialist role
can review it before the Owner decision is presented.

### Reviewer assignment by deliverable type

| Deliverable type | Reviewer role |
|---|---|
| SOP or GL proposals | Larry (governance) — if Larry is the producer, assign a second specialist |
| Migration or remediation plans | Kai (technical correctness, rollback plan completeness) |
| Agent learning or AGENT.md changes | Nolan |
| Domain knowledge proposals | Pax and relevant domain specialist |
| Status or closure reports | Larry (SSOT compliance, source precedence) — if Larry is the producer, use Mode 1 or Mode 3 |
| Database change proposals | Kai |
| Credential or security-adjacent changes | Larry (no secret exposure); Kai (technical correctness) |

### Procedure

1. Producer creates the deliverable and confirms no further work was executed.
2. Orchestrator routes the deliverable to the assigned reviewer with the review package from
   Mode 1 Step 1.
3. Reviewer applies the 13 checks and returns findings to the orchestrator.
4. Orchestrator synthesizes findings. If all checks pass: present Owner decision packet. If any
   check fails: return to producer for amendment before re-review.
5. Owner decides from the options in Section 7.

### Hard limit on role overlap

For the following deliverable types, the producer and reviewer must never be the same role:
system-file changes, database changes, migration plans, remediation plans, and closure reports.
If no separate reviewer is available, use Mode 3 with all five hard stops active.

---

## 5. Mode 3 — Single-System Fallback

Use Mode 3 when only one system or agent is available. Self-approval is still prohibited. The
system applies an explicit self-review checklist, surfaces all uncertainties, and packages a
decision for the Owner without executing anything.

### Step 1 — Declare fallback mode

The system explicitly states: "Single-system fallback mode active. Self-review does not equal
Owner approval."

### Step 2 — Apply all 13 checks

The system applies all 13 checks from Section 6 to its own output. Each check is answered pass,
fail, or uncertain with a one-line reason.

### Step 3 — Uncertainty reporting

For every check answered uncertain: the system states exactly what it could not verify and why.
Example: "Post-check completeness — uncertain: the execution report lists three post-checks but I
cannot confirm check 2 passed because the expected output was not included in the deliverable."

Uncertainty must be surfaced. It must not be resolved by the system unilaterally.

### Step 4 — Hard stop conditions

If any of the following five checks fails or is answered uncertain, the system must stop and
surface to Owner without proceeding further:

1. Scope check — any unauthorized work included
2. Out-of-scope modification check — any unauthorized file, record, or system modified
3. Secret exposure check — any credential, token, key, or secret value present in the deliverable
4. Database or file modification check — any unauthorized database or system-file change
5. Rollback requirement check — migration or remediation deliverable lacks an actionable rollback plan

These are hard stops. No exception. No proceeding past a failed or uncertain hard stop check.

### Step 5 — Owner decision packet

The system assembles: deliverable path, self-review findings per check, list of uncertainties,
list of any hard stop triggers, and the applicable Owner decision options from Section 7.

### Step 6 — Copy-ready next instruction

The system provides a single paragraph the Owner can paste into the next session to initiate
execution, amendment, or deferral.

---

## 6. Review Checks

Apply all 13 checks to every in-scope deliverable. Mark each pass, fail, or uncertain with a
one-line reason.

| # | Check | What to verify |
|---|---|---|
| 1 | Scope check | Does the deliverable stay within the approved scope? Does it include work that was not authorized? |
| 2 | Evidence check | Are all factual claims backed by named sources? Are sources listed? |
| 3 | Source precedence check | If status sources conflict, has GL-016 Rule 3 been applied? (Owner acceptance > execution report > team_tasks > current backlog proposal > older backlog proposals) |
| 4 | Exact text check | Where approved text was specified verbatim, does the deliverable contain exactly that text with no substitutions? |
| 5 | Exact file path check | Are all file paths exact? No approximate paths, no assumed extensions, no inferred subdirectories? |
| 6 | Markdown fence integrity check | Where code blocks are present: are all fences opened and closed? Are language identifiers correct? No runaway fences that consume surrounding text? |
| 7 | Post-check completeness | Does the deliverable include the required post-checks? Are all post-check results stated? |
| 8 | Out-of-scope modification check | Were any files, records, or systems modified that were not in the approved scope? |
| 9 | Secret exposure check | Does the deliverable contain or reveal any credential, token, API key, password, or secret value? |
| 10 | Database or file modification check | Were any databases, system files, AGENT.md files, CLAUDE.md, SOPs, GLs, or Workstreams modified? If yes, were these modifications explicitly authorized? |
| 11 | Rollback requirement check | For migration, remediation, or database change deliverables: is a rollback plan stated? Is it actionable without further preparation? |
| 12 | Final status check | Is the final status of all items in the deliverable clearly stated? Are open items named as open? Are closed items named as closed? No ambiguity about what remains? |
| 13 | Next-step safety check | Is the recommended next step stated? Is it safe to execute without further approval? Does it require a new proposal before execution? |

---

## 7. Owner Decision Options

Every review outcome presented to the Owner must include the applicable options from this set.
Not all options apply to every deliverable; the review package states which are applicable.

| Option | Meaning |
|---|---|
| Approve execution | Deliverable accepted; execution may proceed as specified |
| Request amendments | Deliverable requires specific changes before re-review |
| Defer | Deliverable valid but action postponed; reason and condition stated |
| Reject | Deliverable not accepted; reason stated; no execution |
| Accept as Done | Item closed; no further action required |
| Accept as Done with administrative follow-up | Item closed; one or more administrative records require updating |
| Accept as parked | Deliverable acknowledged but not actioned; may be revisited in a future session |
| Approve triage only | Triage findings accepted; a formal proposal must still be prepared before execution |
| Approve proposal preparation only | Preparation of a formal proposal authorized; no execution until that proposal is separately reviewed and approved |

---

## 8. Worked Examples

### Example 1 — Proposal Review

**Scenario:** Larry produces a GL proposal. This is a governance-critical deliverable where
Larry is the producer. Mode 2 role separation applies: Larry may not self-review a governance
deliverable he produced.

**Mode:** Mode 1 (external review) or Mode 2 with a separate reviewer assigned.

**Review package includes:**
- Deliverable path: `Deliverables/[folder]/gl-proposal-v01.md`
- Approved scope: "Prepare a GL proposal for [topic] — no file creation, no index updates"
- Decision needed: "Confirm scope compliance, source accuracy, and exact text integrity"
- Evidence used: current gl-index.md (read 2026-06-04), triage report
- Confirmation: "No GL file created, no index updated, no database writes"
- Requested outcome: 13-check findings
- Copy-ready next instruction: "Owner Walter Kamer: to approve GL implementation, reply 'Approve GL implementation.' No execution proceeds without this confirmation."

**Expected findings:** all 13 checks pass if the proposal is within scope and the exact content
is correctly specified.

**Owner decision packet:** findings summary + "Approve execution / Request amendments / Defer / Reject."

---

### Example 2 — Execution Report Review

**Scenario:** Kai executes a database migration and produces an execution report. The report is
reviewed before it is presented to Owner as final.

**Mode:** Mode 2 — Larry as reviewer (orchestrator role separate from technical producer).

**Key checks for this deliverable type:**
- Check 8 (out-of-scope modification): were any tables, columns, or records touched outside the
  approved migration scope?
- Check 10 (database or file modification): does the report accurately list every database change
  made?
- Check 11 (rollback requirement): is the rollback procedure stated and actionable?
- Check 7 (post-check completeness): are all post-migration checks documented with results?

**If check 11 fails (rollback plan absent):** hard stop. Return to Kai for amendment before
the execution report is presented to Owner.

**Owner decision options applicable:** Accept as Done / Accept as Done with administrative
follow-up / Request amendments.

---

### Example 3 — Closure Report Review

**Scenario:** Larry produces the final closure report for an audit. Single-system fallback mode
applies because no separate reviewer is assigned.

**Mode:** Mode 3 — fallback self-review.

**Step 1:** Larry declares: "Single-system fallback mode active. Self-review does not equal
Owner approval."

**Key checks for this deliverable type:**
- Check 3 (source precedence): does the closure report apply the precedence rule correctly for
  all items listed as closed?
- Check 12 (final status): are all items in the closure record clearly marked with their final
  status?
- Check 13 (next-step safety): does the report state that future action requires a new proposal
  and Owner approval?

**Hard stop triggers:** any uncertainty on checks 2, 3, or 12 surfaces to Owner before the
closure report is accepted. No item may be listed as closed based on a lower-precedence source
that is contradicted by a higher-precedence source.

**Owner decision options applicable:** Accept as Done / Accept as Done with administrative
follow-up / Request amendments.

---

## 9. Relationship to SOP-015

SOP-015 (Proposal Iteration Protocol for System File Changes) governs the iterative proposal
process for system-file change proposals: versioned proposal rounds, Revision Notes per round,
Owner approval gating, and execution against the approved version only.

SOP-015 applies within the scope of this SOP when the deliverable being reviewed is a
system-file change proposal. When both SOPs apply:
- SOP-015 governs the proposal iteration (versioning, Revision Notes, approved-text execution)
- This SOP governs the review gate applied to each proposal version

Neither SOP modifies the other. They are parallel procedures that apply to the same deliverable
type from different angles.

---

## 10. Knowledge Currency

**Refresh frequency:** Review when a new operating mode becomes necessary, when a new deliverable
type is introduced, when GL-016 is updated, or at annual team review.

**Refresh signals:**
- A new AI system or agent type joins the team and requires a mode not covered here
- A review failure occurs that this SOP's checks would not have detected
- A new deliverable type is introduced that the scope table in GL-016 does not cover
- Hard stop conditions require revision based on operational experience
```

---

## 5. Exact sop-index.md Update Text

The following row is appended to the table in
`Team Knowledge/Core/SOPs/SOP-index.md` exactly as written. No changes at execution time.

```
| Review Gate Procedure for Governance-Relevant Deliverables | `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` | Step-by-step review gate procedure — three operating modes, 13 review checks, Owner decision options, hard stop conditions, worked examples |
```

---

## 6. Post-Check Plan

After implementation, the executing agent confirms all of the following before reporting complete:

| # | Check | Pass condition |
|---|---|---|
| 1 | GL-016 exists on disk | `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` confirmed present before SOP-016 implementation begins |
| 2 | File exists | `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` exists on disk |
| 3 | File content integrity | File content matches Section 4 of this proposal verbatim |
| 4 | SOP number | File contains `SOP-016` in the heading — not SOP-015, SOP-017, or any other number |
| 5 | sop-index.md updated | The SOP-016 row from Section 5 is present in `SOP-index.md` |
| 6 | No other files modified | No other file in the vault was touched during implementation |
| 7 | No database writes | No team_tasks, team_log, UMC, or memory-db entries were written |

---

## 7. Execution Order Requirement

SOP-016 must not be implemented before GL-016 exists on disk and all GL-016 post-checks have
passed. If GL-016 implementation fails or is deferred, SOP-016 implementation is blocked until
GL-016 is resolved. This is not a recommendation — it is a hard prerequisite because SOP-016
references GL-016 by name and number. A SOP that references a non-existent GL is a broken record.

---

## 8. Relationship to the Paired GL Proposal

This SOP proposal and `review-gate-protocol-gl-proposal-v01.md` form a paired set.

- GL-016 establishes the principle this SOP implements.
- If Owner approves both (Option C), implement GL-016 first, verify post-checks, then implement
  SOP-016.
- If Owner approves the GL only (Option A in the GL proposal), this SOP remains a pending proposal.
- If Owner approves this SOP only without GL-016 existing: the SOP references a non-existent GL.
  This is not recommended. Option B in the GL proposal is explicitly marked not recommended for
  this reason.

---

## 9. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| SOP number collision — another SOP is created as SOP-016 before this proposal is implemented | Verify SOP-index.md immediately before implementation; if SOP-016 is taken, reissue this proposal with the correct next available number |
| SOP content is amended at execution time without a new proposal version | SOP-015 governs: any change to approved exact text requires a new proposal version and separate Owner approval before execution |
| GL-016 is not yet on disk when SOP-016 implementation is attempted | Post-check 1 explicitly requires GL-016 to be confirmed present before SOP-016 begins. The executing agent must halt and surface this to Owner if GL-016 is absent |
| Mode 3 fallback is misused as the default mode | Mode 3 is a fallback only. The SOP specifies Mode 1 or Mode 2 as the preferred modes. Mode 3 applies only when no separate reviewer is available and must be explicitly declared |
| Worked examples become stale as the operating model evolves | Examples are illustrative, not exhaustive. The 13 checks and hard stop conditions are the authoritative reference. Examples do not need to be updated when new deliverable types are introduced — only the scope table in GL-016 Section 2 requires updating |

---

## 10. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve GL-016 implementation only — SOP-016 remains pending; implement SOP-016 in a separate session after GL-016 post-checks pass |
| **B** | Approve SOP-016 implementation only — not recommended; GL-016 does not yet exist; SOP-016 would reference a non-existent GL |
| **C** | Approve GL-016 and SOP-016 implementation as a paired set — GL-016 first, post-checks pass, then SOP-016 **(recommended)** |
| **D** | Request amendments to this SOP proposal — specify which sections require changes; a v02 will be prepared |
| **E** | Defer — park both proposals for a future session |
| **F** | Reject — do not create SOP-016 |

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-sop-proposal-v01.md*
