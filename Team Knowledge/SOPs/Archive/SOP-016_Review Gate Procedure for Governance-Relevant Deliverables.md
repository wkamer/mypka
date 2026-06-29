# SOP-016 — Review Gate Procedure for Governance-Relevant Deliverables

**Owner:** Walter Kamer
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
   the orchestrator may act as reviewer with a documented rationale stating why a separate
   reviewer was not available or necessary.
3. Larry may orchestrate governance review but must not self-approve his own governance
   deliverables. If Larry produces a governance-relevant deliverable, use Mode 1 (external
   review) or assign a separate internal reviewer under Mode 2 wherever possible.
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
2. **Approved scope** — the exact scope that was authorized before work began; what was and
   was not permitted
3. **Decision needed** — a precise statement of what the reviewer is asked to assess
4. **Known risks or uncertainties** — anything the producer could not verify, any edge cases
   identified, any assumptions made
5. **Evidence used** — list of sources consulted, with their precedence level per GL-016 Rule 3
6. **Confirmation of no further work executed** — explicit statement that no execution,
   database write, system-file change, or backlog update was performed beyond producing this
   deliverable
7. **Requested review outcome** — what the producer expects back (pass/fail, annotated
   findings, amended version, or Owner decision packet)
8. **Copy-ready next instruction** — a single paragraph or bullet list the Owner or
   orchestrator can use verbatim to initiate the next step

For deliverables that require an RCP per Section 11.2, the orchestrator must prepare the RCP using the template in Section 11.4 before assembling the review package. The completed RCP must be included in the review package. The review package is not complete without the RCP when one is required. Pending proposals used for context must be listed in Field 6 of the RCP with their pending status stated.

### Step 2 — Reviewer applies the 13 checks

The reviewer applies all 13 checks from Section 6 of this SOP. Each check is marked pass,
fail, or uncertain with a one-line reason.

### Step 3 — Reviewer returns findings

The reviewer returns the completed 13-check findings to the orchestrator. The reviewer must
not execute any action. The reviewer returns findings only.

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

Step 0 — RCP preparation. Before distributing the review package to internal reviewers, the orchestrator prepares the RCP per Section 11. The RCP is distributed to all reviewers alongside the deliverable. Reviewers must read the RCP before reading the deliverable. The review does not begin until all reviewers confirm the RCP is complete.

1. Producer creates the deliverable and confirms no further work was executed.
2. Orchestrator routes the deliverable to the assigned reviewer with the review package from
   Mode 1 Step 1.
3. Reviewer applies the 13 checks and returns findings to the orchestrator.
4. Orchestrator synthesizes findings. If all checks pass: present Owner decision packet. If
   any check fails: return to producer for amendment before re-review.
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
Owner approval." If the deliverable requires an RCP per Section 11.2, the system prepares and states the RCP in full before applying any review checks. A Mode 3 review without a required RCP is not valid and may not be presented to the Owner as a completed review.

### Step 2 — Apply all 13 checks

The system applies all 13 checks from Section 6 to its own output. Each check is answered
pass, fail, or uncertain with a one-line reason.

### Step 3 — Uncertainty reporting

For every check answered uncertain: the system states exactly what it could not verify and
why. Example: "Post-check completeness — uncertain: the execution report lists three
post-checks but I cannot confirm check 2 passed because the expected output was not included
in the deliverable."

Uncertainty must be surfaced. It must not be resolved by the system unilaterally.

### Step 4 — Hard stop conditions

If any of the following five checks fails or is answered uncertain, the system must stop and
surface to Owner without proceeding further:

1. Scope check — any unauthorized work included
2. Out-of-scope modification check — any unauthorized file, record, or system modified
3. Secret exposure check — any credential, token, key, or secret value present in the
   deliverable
4. Database or file modification check — any unauthorized database or system-file change
5. Rollback requirement check — migration or remediation deliverable lacks an actionable
   rollback plan

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
- Deliverable path: `Deliverables/[folder]/gl-proposal-v0N.md`
- Approved scope: "Prepare a GL proposal for [topic] — no file creation, no index updates"
- Decision needed: "Confirm scope compliance, source accuracy, and exact text integrity"
- Evidence used: current gl-index.md (read date), triage report (source)
- Confirmation: "No GL file created, no index updated, no database writes"
- Requested outcome: 13-check findings
- Copy-ready next instruction: "Owner Walter Kamer: to approve GL implementation, respond
  with the applicable option from the Owner decision options in the proposal. No execution
  proceeds without this confirmation."

**Expected findings:** all 13 checks pass if the proposal is within scope and the exact
content is correctly specified.

**Owner decision options applicable:** Approve execution / Request amendments / Defer / Reject.

---

### Example 2 — Execution Report Review

**Scenario:** Kai executes a database migration and produces an execution report. The report
is reviewed before it is presented to Owner as final.

**Mode:** Mode 2 — Larry as reviewer (orchestrator role separate from technical producer).

**Key checks for this deliverable type:**
- Check 8 (out-of-scope modification): were any tables, columns, or records touched outside
  the approved migration scope?
- Check 10 (database or file modification): does the report accurately list every database
  change made?
- Check 11 (rollback requirement): is the rollback procedure stated and actionable?
- Check 7 (post-check completeness): are all post-migration checks documented with results?

**If check 11 fails (rollback plan absent):** hard stop. Return to Kai for amendment before
the execution report is presented to Owner.

**Owner decision options applicable:** Accept as Done / Accept as Done with administrative
follow-up / Request amendments.

---

### Example 3 — Closure Report Review

**Scenario:** Larry produces the final closure report for an audit. Single-system fallback
mode applies because no separate reviewer is assigned.

**Mode:** Mode 3 — fallback self-review.

**Step 1:** Larry declares: "Single-system fallback mode active. Self-review does not equal
Owner approval."

**Key checks for this deliverable type:**
- Check 3 (source precedence): does the closure report apply the precedence rule correctly
  for all items listed as closed?
- Check 12 (final status): are all items in the closure record clearly marked with their
  final status?
- Check 13 (next-step safety): does the report state that future action requires a new
  proposal and Owner approval?

**Hard stop triggers:** any uncertainty on checks 2, 3, or 12 surfaces to Owner before the
closure report is accepted. No item may be listed as closed based on a lower-precedence source
that is contradicted by a higher-precedence source.

**Owner decision options applicable:** Accept as Done / Accept as Done with administrative
follow-up / Request amendments.

---

### Example 4 — Proposal Review with Review Context Packet (v05)

**Scenario:** A proposal for a script extension (S2, Medium impact) has been prepared. The Maintainer consults the route selection matrix: S2-Medium maps directly to Route C. No Route B check is required; the route matrix assigns Route C for S2-Medium independently of any escalation condition. The proposal modifies an existing Todoist integration handler, which is an operational system file (per SOP-018 Section 2.4). The operational system file modification triggers the Review Gate per SOP-018 Section 13. An RCP is required.

**Step-by-step:**

1. Maintainer classifies the idea: S2-Medium.
2. Maintainer consults route matrix (SOP-018 Section 10): S2-Medium → Route C (direct).
3. Maintainer prepares a full proposal (Route C).
4. Maintainer prepares the RCP per Section 11.4.
5. Maintainer assembles the review package: RCP + proposal.
6. Review Gate executed (Mode 1 or Mode 2 per availability and impact).
7. Reviewer reads RCP first; then reads proposal; applies 13 checks; returns findings.
8. Maintainer packages Owner decision packet: proposal + findings + Owner decision options.
9. Owner makes DP-3 decision (post-Review Gate): Accept.
10. Owner makes DP-4 decision (separate step): Confirm implementation may begin.

**Abbreviated RCP for this example:**

- Field 1: Determine whether the script extension proposal is complete, in-scope, and safe to proceed to implementation.
- Field 2: `[exact path of proposal file]`
- Field 3: Proposal (Route C, S2-Medium)
- Field 6: GL-016, SOP-016, GL-018 (PENDING), SOP-018 (PENDING)
- Field 8: Review the proposal at Field 2 for scope accuracy, operational system file change completeness, and review check compliance.
- Field 9: Do not review the implementation. Do not test the script. Do not assess business value.
- Field 10: No files may be created or modified. No execution may begin. No database writes.
- Field 11: Accept / Request amendments / Defer / Reject (per SOP-016 Section 7)
- Field 16: No — execution is not allowed; this review produces findings only.
- Field 17: No — lifecycle processing is not in scope.
- Field 18: Prior memory disclaimer (full verbatim text per Section 11.4).

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

**Refresh frequency:** Review when a new operating mode becomes necessary, when a new
deliverable type is introduced, when GL-016 is updated, or at annual team review.

**Refresh signals:**
- A new AI system or agent type joins the team and requires a mode not covered here
- A review failure occurs that this SOP's checks would not have detected
- A new deliverable type is introduced that the scope table in GL-016 does not cover
- Hard stop conditions require revision based on operational experience

---

## 11. Review Context Packet (RCP)

### 11.1 Purpose

A Review Context Packet (RCP) is a structured document that makes a governance-relevant review self-contained and portable. A reviewer presented with the RCP and the deliverable under review must be able to complete the full review without accessing any prior chat history, session memory, or accumulated tool context.

This requirement applies regardless of which system performs the review: a new AI session, a different AI tool, a human reviewer, or the same system in a different context. The RCP is the complete context. Nothing outside the RCP and the deliverable is authoritative for the review.

### 11.2 When an RCP Is Required

An RCP is required for every review in which the deliverable is any of the following:

- An implementation-authorizing proposal from any route that requires Review Gate under the active idea routing procedure. Route B without escalation does not require an RCP unless the Owner explicitly requests one.
- A governance file change proposal (SOP-015 deliverable — SOP-015 uses the term "system-file change" for this category; for the governance file / operational system file distinction, see SOP-018 Section 2.4 when SOP-018 is active)
- An execution report for a High or Critical impact action
- A closure report
- Any amendment to a GL, SOP, Workstream, AGENT.md, or CLAUDE.md
- Any cross-domain deliverable (S10 scenario class per SOP-018, when SOP-018 is active; when SOP-018 is not yet active, apply the GL-016 scope criteria for cross-domain deliverables)
- Any security-sensitive deliverable (S9 scenario class per SOP-018, when SOP-018 is active; when SOP-018 is not yet active, apply the GL-016 scope criteria for security-sensitive deliverables)

An RCP is not required for routine status reports, Low-impact execution confirmations, or single-check action records. The Maintainer determines whether an RCP is required and records the determination in the session context.

### 11.3 Mandatory RCP Fields

An RCP must contain all of the following fields. Fields may not be omitted. If a field is not applicable, state "Not applicable" with a one-line reason.

| # | Field | Required content |
|---|---|---|
| 1 | Review purpose | One sentence: what decision does this review enable? |
| 2 | Deliverable path | Exact file path(s) of the deliverable(s) under review |
| 3 | Deliverable type | Proposal / Execution report / Closure report / Amendment / Other (specify) |
| 4 | Owner | Walter Kamer |
| 5 | Maintainer | Current Maintainer role holder (currently: Larry) |
| 6 | Governance baseline | List of all active GLs and SOPs by number and title at the time of review; include any pending proposals used for this review and state their pending status |
| 7 | Relevant active GLs and SOPs | The specific GLs and SOPs the reviewer must apply or verify against for this review |
| 8 | Review scope | Exact list of what the reviewer must evaluate — not broader than the deliverable |
| 9 | Non-goals | Explicit list of what the reviewer must not evaluate, modify, or recommend |
| 10 | Hard exclusions | Actions that must not occur during or as a result of this review — stated as prohibitions |
| 11 | Allowed Owner decisions | List the applicable options from SOP-016 Section 7 |
| 12 | Required reviewer checks | The 13 standard checks from Section 6 plus any additional checks specific to this deliverable |
| 13 | Required output format | The format the reviewer must use to return findings: pass/fail per check, uncertainty list, hard stop list, Owner decision packet |
| 14 | Known dependencies | Files, databases, prior decisions, or external systems the deliverable depends on |
| 15 | Canonical source files | The authoritative source documents the reviewer must use — exact paths; not summaries. When reviewing a deliverable in the Idea-to-Implementation Governance Pack, include all companion pack documents per Section 11.7. |
| 16 | Execution allowed | Yes / No — state explicitly whether any execution may occur as a result of this review |
| 17 | Lifecycle processing in scope | Yes / No — state explicitly whether lifecycle decisions (SOP-017) are in scope for this review session |
| 18 | Prior memory disclaimer | The full text specified in Section 11.4 Field 18 — this field must appear verbatim and may not be paraphrased |

### 11.4 RCP Template

The following template must be used when preparing an RCP. All 18 fields are mandatory.

```markdown
## Review Context Packet

**RCP version:** [version number, e.g. v01]
**Prepared by:** [Maintainer name]
**Date:** [YYYY-MM-DD]
**Review session:** [session identifier or date]

---

### Field 1 — Review Purpose
[One sentence: what decision does this review enable?]

### Field 2 — Deliverable Path
[Exact file path(s)]

### Field 3 — Deliverable Type
[Proposal / Execution report / Closure report / Amendment / Other]

### Field 4 — Owner
Walter Kamer

### Field 5 — Maintainer
[Current Maintainer role holder]

### Field 6 — Governance Baseline
[List all active GLs and SOPs by number and title. For any pending proposal used in this review, state: "PENDING — [filename]".]

### Field 7 — Relevant Active GLs and SOPs
[The specific GLs and SOPs that apply to this review]

### Field 8 — Review Scope
[Exact list of what the reviewer must evaluate]

### Field 9 — Non-Goals
[Explicit list of what the reviewer must not evaluate, modify, or recommend]

### Field 10 — Hard Exclusions
[Actions that must not occur during or as a result of this review]

### Field 11 — Allowed Owner Decisions
[List applicable options from SOP-016 Section 7]

### Field 12 — Required Reviewer Checks
[The 13 standard checks (Section 6) plus any additional checks. List each check by number and name.]

### Field 13 — Required Output Format
[The format the reviewer must use to return findings: pass/fail per check, uncertainty list, hard stop list, Owner decision packet]

### Field 14 — Known Dependencies
[Files, databases, prior decisions, or external systems]

### Field 15 — Canonical Source Files
[Exact paths of the authoritative source documents the reviewer must use.
If this is a governance pack review, include all four companion documents per Section 11.7.]

### Field 16 — Execution Allowed
[Yes / No — state explicitly]

### Field 17 — Lifecycle Processing in Scope
[Yes / No — state explicitly]

### Field 18 — Prior Memory Disclaimer
The reviewer must not rely on any prior chat history, session memory, or accumulated tool context. All context required for this review is contained in this RCP and the deliverable under review. If the reviewer requires information not present in this RCP and the deliverable, the reviewer must stop and request it from the Maintainer before proceeding. Inferring missing context from prior conversations or tool state is not permitted and will invalidate the review findings.
```

### 11.5 RCP Usage Instructions

**For the Maintainer:**

1. Determine whether an RCP is required per Section 11.2.
2. If required: prepare the RCP before the review package is assembled or distributed.
3. Include the RCP in the review package alongside the deliverable.
4. Record in session context: RCP prepared (yes/no), RCP version, review date, determination rationale.
5. If not required: record the determination in session context with a one-line reason.

**For the Reviewer:**

1. Read the RCP in full before reading the deliverable.
2. Verify that all 18 fields are present and complete. If any field is absent or states "Not applicable" without a reason: stop and request completion from the Maintainer.
3. Apply only the checks listed in Field 12. Do not apply checks outside this scope.
4. Do not access prior chat history, session memory, or accumulated tool context. All required context is in the RCP and the deliverable.
5. Return findings in the format specified in Field 13.
6. If you require information not in the RCP or the deliverable: stop and request it from the Maintainer. Do not infer or assume.
7. Do not execute any action whose authorization is not explicit in Field 16 (Execution Allowed).

**For the Owner:**

1. The RCP is a support document. The Owner reviews findings and decision options — not the RCP itself.
2. Decision options are listed in Field 11.
3. If the Owner notices that the RCP is missing or incomplete, the Owner may decline to review the deliverable until the RCP is corrected.

### 11.6 Implementation Dependency and Pre-SOP-018 Behavior

This amendment depends on SOP-018 for the definitions of scenario classes S9 (security-sensitive) and S10 (cross-domain) referenced in Section 11.2.

**Implementation order (mandatory):**

1. GL-018 implemented and post-checked
2. SOP-018 implemented and post-checked
3. This SOP-016 RCP amendment implemented and post-checked
4. Smoke test executed — only if separately approved by Owner in a dedicated session

This amendment must not be applied to SOP-016 before steps 1 and 2 are complete.

**Pre-SOP-018 behavior (if this amendment is applied before SOP-018 is active):**

This situation must not arise if the implementation order above is followed. If for any reason this amendment is evaluated before SOP-018 is active, the following reduced behavior applies:

- The Section 11.2 condition "any cross-domain deliverable (S10 scenario class per SOP-018)" does not apply. Instead, use the GL-016 scope criteria to determine whether a cross-domain deliverable requires an RCP.
- The Section 11.2 condition "any security-sensitive deliverable (S9 scenario class per SOP-018)" does not apply. Instead, use the GL-016 scope criteria to determine whether a security-sensitive deliverable requires an RCP.
- All other Section 11.2 conditions apply regardless of SOP-018 status.
- Field 6 (Governance Baseline) must state: "SOP-018 is not yet active" and list the pending proposal path.

### 11.7 Companion Files for Governance Pack Reviews

When reviewing any deliverable that is part of the Idea-to-Implementation Governance Pack (GL-018 proposal, SOP-018 proposal, this amendment, or the smoke test plan), Field 15 (Canonical Source Files) of the RCP must include all four companion documents listed below. The reviewer must read these documents before applying review checks. Their pending status must be stated.

| Companion document | Path | Status at time of this proposal |
|---|---|---|
| GL-018 proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-gl-proposal-v05.md` | PENDING — not yet implemented |
| SOP-018 proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-sop-proposal-v05.md` | PENDING — not yet implemented |
| SOP-016 RCP amendment proposal | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/review-context-packet-sop-016-amendment-proposal-v05.md` | PENDING — not yet implemented |
| Smoke test plan | `Deliverables/20260605_Core_Idea-to-Implementation Governance Pack proposals/idea-routing-smoke-test-plan-v05.md` | PENDING — not yet executed |

After implementation, update the paths in Field 15 to the canonical locations of the implemented documents.
