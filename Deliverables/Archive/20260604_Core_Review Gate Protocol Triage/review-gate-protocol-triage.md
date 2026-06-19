# System-Agnostic Review Gate Protocol — Triage Report

**File:** `Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-triage.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Status:** Proposal-only triage — awaiting Owner decision

**Folder rationale:** The Core AI Team Audit is formally closed as of 2026-06-04. This triage
initiates a new governance topic with its own scope, lifecycle, and proposal chain. It is placed
in a new deliverables folder rather than the audit folder to preserve audit closure integrity and
to give this initiative a clean starting point.

**Governance:** This document is read-only. No implementation, SOP creation, GL creation, system-file
change, database write, backlog update, or further governance work may be executed without Owner
Walter Kamer's explicit approval.

---

## 1. Background and Context

During the Core AI Team Audit (2026-06-01 to 2026-06-04), deliverables such as proposals, execution
reports, status reports, and closure reports passed through a controlled review gate before
follow-up action was authorized. That review gate was applied ad hoc — governed by convention and
session discipline rather than a written protocol. It worked. The following failure modes were
detected and corrected because the gate existed:

- Scope drift (items outside approved scope included in execution)
- Stale status sources (backlog registrations overriding execution reports)
- Incorrect open/closed item status
- Markdown fence issues in deliverables containing code blocks
- Exact-text ambiguity in approved changes
- Missing post-checks in execution reports
- Out-of-scope modifications included without notice
- Secret exposure risk surfaced before execution
- Premature execution before Owner approval
- Unclear or absent next steps after a deliverable

Owner Walter Kamer wants this review process formalized inside the myPKA AI-team operating model
so it is system-agnostic and functions regardless of which AI system, agent, tool, script,
automation, orchestration layer, or human-assisted workflow produces a deliverable.

This triage report assesses the right governance instrument and documents the proposed protocol
content for Owner review.

---

## 2. Instrument Assessment

Before recommending a canonical destination, three alternatives are assessed: update SOP-015,
update GL-014, or create new instruments.

### 2.1 Update SOP-015 — Proposal Iteration Protocol for System File Changes

SOP-015 governs the iterative proposal process for system-file changes: versioned proposal rounds,
Revision Notes per round, version-specific approval, and exact-text execution. Its scope is
deliberately narrow — it was designed to prevent drift in proposals that touch sensitive system
files.

**Not suitable as the destination for the Review Gate Protocol.**

Reasons:
- SOP-015 scope is system-file change proposals only. The Review Gate Protocol applies to all
  governance-relevant deliverables including execution reports, status reports, closure reports,
  migration plans, and automation changes — none of which are system-file proposals.
- Embedding a broader protocol into SOP-015 would make SOP-015 unwieldy and dilute its precision.
- The Review Gate Protocol is a prerequisite standard that SOP-015 should reference, not absorb.

**Relationship:** The Review Gate Protocol will cite SOP-015 as the applicable procedure when the
deliverable is a system-file change proposal. SOP-015 will cite the Review Gate Protocol as the
overarching review gate standard.

### 2.2 Update GL-014 — AI Team Governance

GL-014 defines the AI team's governance principles: agent roles, language standards, system-file
rules, and operating conventions. It is the current top-level governance reference.

**Partial fit but not the right primary destination.**

Reasons:
- GL-014 is already broad. Adding a full review gate protocol with operating modes, checklists,
  and decision option sets would expand GL-014 beyond its current purpose as a principles document.
- The Review Gate Protocol has enough procedural content to warrant its own SOP. Embedding
  procedures inside a GL collapses the principle/procedure separation that the team's taxonomy
  is built on.
- GL-014 should reference the new GL (principle) once it exists.

### 2.3 New GL only

A standalone GL that defines the review gate principle: what it is, why it exists, when it
applies, and the four exact rules. Short, stable, referenceable.

**Partial fit — covers the why, not the how.**

Suitable as the principle layer. Not sufficient alone because operating modes, checklists, and
decision option sets are procedural content that belongs in a SOP, not a GL.

### 2.4 New SOP only

A standalone SOP that defines the review gate procedure: the three operating modes, the 13 review
checks, the decision options, the package format, and the stop conditions.

**Partial fit — covers the how, not the why.**

Suitable as the procedure layer. Not sufficient alone because the core principle (governance-relevant
deliverables require a review gate regardless of which system produced them) is a team-wide
operating standard that deserves GL-level permanence so it can be cited from agent instructions,
other SOPs, and onboarding materials without repeating the full procedure.

### 2.5 Assessment Conclusion

**Best destination: both a new GL and a new SOP.**

- The GL defines the principle: what a review gate is, when it applies, the tool-agnostic mandate,
  and the four exact rules. Stable. Short. Citable everywhere.
- The SOP defines the procedure: the three operating modes, the review package format, the 13 checks,
  the decision options, and the stop conditions. Actionable. Updatable independently of the principle.

This matches the team's existing taxonomy where GL = reference, SOP = procedure, and one does not
duplicate the other.

---

## 3. Proposed Protocol Content

This section documents what the protocol should contain. It is not the final SOP or GL text —
that will be produced only after Owner approval of this triage.

### 3.1 Scope — Which Deliverables Require a Review Gate

A review gate is required for any of the following deliverable types, regardless of which system,
agent, tool, script, or workflow produced it:

| Deliverable type | Review gate required |
|---|---|
| Proposals (new) | Yes |
| Revised proposals | Yes |
| Execution reports | Yes |
| Status reports | Yes |
| Closure reports | Yes |
| Graduation candidates | Yes |
| Remediation plans | Yes |
| Migration plans | Yes |
| Rollback plans | Yes |
| System-file changes | Yes — SOP-015 applies in addition |
| Database changes | Yes |
| Automation changes | Yes |

Deliverables not in scope: conversational clarifications, single-turn lookups, read-only status
queries with no downstream action, and session log drafts awaiting routine Owner approval.

### 3.2 Three Operating Modes

#### Mode 1 — External Review

A deliverable is produced by one system or agent and reviewed by a different external reviewer
(another AI system, a human reviewer, or a specialist outside the original producer's domain).

**How to package the deliverable for external review:**

The producer must assemble a review package containing exactly these elements:

1. **Deliverable path** — exact file path and location of the deliverable to be reviewed
2. **Approved scope** — the exact scope that was authorized before work began; what was and was
   not permitted
3. **Decision needed** — a clear statement of what the reviewer is being asked to assess (e.g.,
   "confirm scope compliance", "verify evidence sources", "check for secret exposure risk")
4. **Known risks or uncertainties** — anything the producer could not verify, any edge cases
   identified, any assumptions made
5. **Evidence used** — list of sources consulted, with their precedence level per the status
   precedence rule
6. **Confirmation of no further work executed** — explicit statement that no execution, database
   write, system-file change, or backlog update was performed beyond producing this deliverable
7. **Requested review outcome** — what the producer expects the reviewer to return (pass/fail,
   annotated findings, amended version, or Owner decision packet)
8. **Copy-ready next instruction** — a single paragraph or bullet list the Owner or orchestrator
   can use verbatim to initiate the next step once review is complete

The external reviewer returns findings using the 13-check format from section 3.3. If the reviewer
is another AI system (e.g., ChatGPT reviewing a Claude deliverable), the review package is passed
as structured context; the reviewer must not execute any action and must return findings only.

#### Mode 2 — Internal Multi-Agent Review

A deliverable is produced inside the AI team and reviewed by a different specialist role before
the Owner decision is presented.

**Role separation:**

| Role | Responsibility | May not |
|---|---|---|
| Producer | Creates the deliverable according to approved scope | Self-approve; execute beyond the deliverable itself |
| Reviewer | Applies the 13-check checklist; returns pass/fail findings and amendments | Execute on findings; escalate directly to Owner without orchestrator |
| Orchestrator (Larry) | Routes the deliverable to the right reviewer; synthesizes findings; packages the Owner decision | Override reviewer findings without documenting the override reason |
| Owner | Approves, rejects, defers, or requests amendments | Delegate the approval decision to any agent or system |

**When to involve which specialist type:**

| Deliverable type | Reviewer role |
|---|---|
| SOP or GL proposals | Larry (governance) + domain specialist if domain-specific |
| Migration or remediation plans | Kai (technical) |
| Agent learning or AGENT.md changes | Nolan |
| Domain knowledge proposals | Pax + relevant domain specialist |
| Status or closure reports | Larry (orchestrator reviews for SSOT compliance) |
| Database change proposals | Kai |
| Credential or security-adjacent changes | Larry confirms no secret exposure; Kai confirms technical correctness |

The producer and reviewer must never be the same role for governance-critical deliverables
(system-file changes, database changes, migration plans, closure reports). For lower-stakes
deliverables (routine status reports, single-check execution confirmations), the orchestrator
may serve as reviewer with a documented rationale.

#### Mode 3 — Single-System Fallback Review

Only one system or agent is available. Self-approval is still prohibited. The system applies an
explicit self-review checklist, surfaces all uncertainties, and packages a decision for the Owner
without executing anything.

**Safe fallback pattern:**

1. **Explicit self-review checklist** — the producing system runs all 13 checks from section 3.3
   against its own output. Each check is answered pass, fail, or uncertain with a one-line reason.
2. **Uncertainty reporting** — for every check answered uncertain: the system states exactly what
   it could not verify and why. Example: "Post-check completeness — uncertain: the execution report
   lists three post-checks but I cannot confirm check 2 passed because the expected output was not
   included in the deliverable."
3. **No automatic execution** — the system must not proceed to execution based on a passing
   self-review. The self-review produces a findings package only.
4. **Owner decision packet** — the system assembles: deliverable path, self-review findings per
   check, list of uncertainties, and recommended decision options from section 3.4.
5. **Copy-ready next instruction** — a single paragraph the Owner can paste into the next session
   to initiate execution, amendment, or deferral.
6. **Stronger stop conditions** — if any of the following checks fails or is uncertain, the system
   must stop and surface to Owner without proceeding further: scope check, out-of-scope modification
   check, secret exposure check, database or file modification check, rollback requirement check.
   These five are hard stops in single-system fallback mode.

### 3.3 Required Review Checks

All 13 checks apply to every in-scope deliverable. Reviewers mark each as **pass**, **fail**, or
**uncertain** with a one-line reason.

| # | Check | What to verify |
|---|---|---|
| 1 | Scope check | Does the deliverable stay within the approved scope? Does it include work that was not authorized? |
| 2 | Evidence check | Are all factual claims backed by sources? Are sources named? |
| 3 | Source precedence check | If status sources conflict, has the status precedence rule been applied correctly? (Owner acceptance > execution report > team_tasks > current backlog proposal > older backlog proposals) |
| 4 | Exact text check | Where approved text was specified verbatim, does the deliverable contain exactly that text with no substitutions? |
| 5 | Exact file path check | Are all file paths exact? No approximate paths, no assumed extensions, no inferred subdirectories? |
| 6 | Markdown fence integrity check | Where code blocks are present: are all fences opened and closed? Are language identifiers correct? No runaway fences that consume surrounding text? |
| 7 | Post-check completeness | Does the deliverable include the required post-checks? Are all post-check results stated? |
| 8 | Out-of-scope modification check | Were any files, records, or systems modified that were not in the approved scope? |
| 9 | Secret exposure check | Does the deliverable contain or reveal any credential, token, API key, password, or secret value? |
| 10 | Database or file modification check | Were any databases, system files, AGENT.md files, CLAUDE.md, SOPs, GLs, or Workstreams modified? If yes, were these modifications explicitly authorized? |
| 11 | Rollback requirement check | For migration, remediation, or database change deliverables: is a rollback plan stated? Is it actionable? |
| 12 | Final status check | Is the final status of all items in the deliverable clearly stated? Are open items named as open? Are closed items named as closed? Is there no ambiguity about what remains? |
| 13 | Next-step safety check | Is the recommended next step stated? Is it safe to execute without further approval? Does it require a new proposal before execution? |

### 3.4 Owner Decision Options

Every review outcome presented to the Owner must include exactly the applicable decision options
from this set. Not all options apply to every deliverable — the review package states which are
applicable.

| Option | Meaning |
|---|---|
| Approve execution | Deliverable is accepted; execution may proceed as specified |
| Request amendments | Deliverable requires specific changes before re-review |
| Defer | Deliverable is valid but action is postponed; reason and condition stated |
| Reject | Deliverable is not accepted; reason stated; no execution |
| Accept as Done | Item is closed; no further action required |
| Accept as Done with administrative follow-up | Item is closed; one or more administrative records require updating |
| Accept as parked | Deliverable is acknowledged but not actioned; may be revisited in a future session |
| Approve triage only | Triage findings are accepted; a formal proposal must still be prepared before execution |
| Approve proposal preparation only | Preparation of a formal proposal is authorized; no execution until that proposal is separately reviewed and approved |

### 3.5 Four Exact Rules

**Rule 1 — No self-execution**
Systems, tools, scripts, agents, or automations may recommend, but must not execute the
recommendation without explicit Owner Walter Kamer approval. A passing self-review does not
constitute Owner approval.

**Rule 2 — Copy-ready next instruction**
Every review outcome that requires a next action must include a copy-ready next instruction or
prompt. The Owner must not need to construct the next step from memory or inference.

**Rule 3 — Status precedence**
If status sources conflict, apply the status precedence rule in this order:
1. Owner acceptance / final acknowledgement
2. Execution report with final status
3. team_tasks status
4. Current backlog proposal
5. Older backlog proposals or session summaries (lowest — only used when nothing above exists)

**Rule 4 — Tool-agnostic**
The review gate protocol must not depend on Claude, ChatGPT, Codex, n8n, MCP, or any specific
implementation tool. The protocol is defined in terms of roles, checks, and decision options that
can be executed by any system, agent, or human reviewer with access to the deliverable.

### 3.6 Phase Definitions

The protocol must distinguish between these phases. Each phase has a defined endpoint and must not
automatically trigger the next.

| Phase | Definition | Endpoint |
|---|---|---|
| Triage | Assess a question or gap; determine the right instrument or next step | Owner approves recommended path |
| Proposal preparation | Draft a formal proposal describing scope, method, risks, and decision options | Owner receives proposal for review |
| Review | Apply the 13-check checklist against a deliverable; return findings | Owner receives findings and decision options |
| Execution | Implement the approved proposal exactly as specified | Execution report produced |
| Administrative closure | Update administrative records (team_tasks, session logs) to reflect completed status | Record updated; no content changes |
| Final closure | Issue a formal closure declaration; produce closure deliverable | Closure report signed off by Owner |

A phase may not skip to a later phase without Owner approval of the intermediate steps.

### 3.7 Relationship to SOP-015

SOP-015 (Proposal Iteration Protocol for System File Changes) governs the iterative proposal
process for a specific deliverable type: proposals that modify system files (AGENT.md, CLAUDE.md,
SOPs, GLs, Workstreams). It defines versioning, Revision Notes, and exact-text execution.

The Review Gate Protocol is the overarching standard. SOP-015 is a specific procedure that applies
within the Review Gate Protocol's scope when the deliverable is a system-file change proposal.

Relationship after the Review Gate Protocol is created:
- The Review Gate Protocol GL cites SOP-015 as the applicable SOP for system-file change proposals.
- SOP-015 cites the Review Gate Protocol GL as the overarching review gate standard.
- No content in SOP-015 is modified by this proposal — that would require its own SOP-015 iteration.

---

## 4. Canonical Destination

**Recommended: both a new GL and a new SOP.**

| Instrument | Content | GL or SOP |
|---|---|---|
| New GL | Principle: what a review gate is, why it exists, when it applies, the tool-agnostic mandate, the four exact rules, the phase definitions, and the relationship to SOP-015. Short, stable, citable. | GL |
| New SOP | Procedure: the three operating modes, the review package format, the 13-check checklist, the decision option set, and the stop conditions per mode. Actionable, updatable. | SOP |

The GL is the "why and what." The SOP is the "how." Neither duplicates the other. Both are citable
independently from agent instructions, CLAUDE.md, and other SOPs.

Suggested numbering: next available GL and SOP numbers at the time of creation. GL-016 and SOP-016
are candidates, but the exact numbers must be verified against the current indexes at proposal time.

---

## 5. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Protocol overhead is too high for routine deliverables | Apply a tiered scope: the full 13-check list applies to migration plans, database changes, and system-file changes; a lightweight 5-check subset (scope, evidence, exact text, out-of-scope modification, secret exposure) applies to routine proposals and status reports. Define the tiers in the SOP. |
| Tool-agnostic language becomes too abstract to apply | Include one worked example per operating mode in the SOP: a concrete deliverable type, a concrete reviewer, and a concrete package. |
| Single-system fallback creates false confidence | Enforce the five hard-stop checks in fallback mode. State explicitly: a passing self-review does not equal Owner approval. Uncertainty must be surfaced, not resolved by the system. |
| Future agents ignore the protocol | Embed a reference to the GL in GL-014 and in each agent's AGENT.md Never Does or operating rules section, at the time the SOP and GL are created and approved. |
| Protocol becomes stale | Add a Knowledge Currency section to the GL with a refresh trigger: "Review when a new AI system is added to the team, when a new deliverable type is introduced, or annually." |
| Scope creep during proposal preparation | This triage is the gate. The formal proposal must stay within the scope of what this triage defines. The SOP-015 iteration model applies if the formal proposal requires multiple rounds. |

---

## 6. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve preparing a formal SOP proposal for the Review Gate Protocol procedure |
| **B** | Approve preparing a formal GL proposal for the Review Gate Protocol principle |
| **C** | Approve preparing both — a GL principle proposal and a SOP procedure proposal — as a paired set **(recommended)** |
| **D** | Request amendments to this triage before any proposal preparation |
| **E** | Defer — park this triage for a future session |
| **F** | Reject — do not formalize the review gate as a protocol at this time |

---

## 7. Recommended Option

**Option C — approve preparing both a GL principle proposal and a SOP procedure proposal.**

Rationale:

The GL and SOP serve distinct, non-overlapping functions. The GL is permanent and citable; it
gives the review gate principle a stable home that any agent, system, or human can reference
without reading the full procedure. The SOP is operational; it gives any producer, reviewer, or
orchestrator a step-by-step procedure that can be updated without touching the principle.

Creating only the SOP (Option A) leaves the principle unanchored — agents can follow the procedure
without understanding when or why it applies. Creating only the GL (Option B) leaves the procedure
undefined — reviewers know the standard exists but not how to execute it.

The paired approach also creates a natural proposal sequence: GL first (short, principle-only,
fast to review), SOP second (longer, procedural, references the approved GL). Each passes through
its own SOP-015 review cycle. Risk is low because no system files are changed at this stage.

Option D is appropriate if Owner Walter Kamer wants to adjust the protocol content before a formal
proposal is prepared. All protocol content in Section 3 is draft at this stage and can be amended.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Review Gate Protocol Triage/review-gate-protocol-triage.md*
