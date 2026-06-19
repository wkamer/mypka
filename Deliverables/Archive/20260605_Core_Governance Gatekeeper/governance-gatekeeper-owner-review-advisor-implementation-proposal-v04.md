# Governance Gatekeeper — Owner Review Advisor
# Implementation Proposal v04

**Status:** Awaiting Owner approval.
**Prepared by:** Nolan, HR Specialist
**Date:** 2026-06-06
**Basis:** Governance Gatekeeper — Owner Review Advisor Lean Scoping Proposal v02 (accepted 2026-06-06); Owner answers to clarifying questions (action-report-06d, 2026-06-06)

---

## Revision Notes (v03 to v04)

- Overlap check added as a separate step (action-report-06e) before AGENT.md drafting, per SOP-003 requirement.
- AGENT.md draft gate made explicit: draft only proceeds after Owner confirms action-report-06e.
- Iris's role corrected: Owner Review Advisor only, not operational gate-block producer. Does not execute CP-1 through CP-4.
- Owner answers to four clarifying questions incorporated throughout.
- Exact Owner approval text narrowed to action-report-06e only.
- Folder path corrected to `Team/Iris - The Governance Gatekeeper/` per established naming in v01–v03.

---

## What Is Already Done — Do Not Re-Authorize

| Item | Status |
|---|---|
| Lean Scoping Proposal v02 | Accepted |
| Implementation Proposals v01, v02, v03 | Superseded |
| Action-report-06a — hiring process alignment | Complete |
| Action-report-06b — Pax research request | Complete |
| Action-report-06c — Pax research brief | Complete and accepted |
| Action-report-06d — Nolan clarifying questions | Complete and answered |
| GL-019, SOP-019, CLAUDE.md instruction | Live — not to be modified |

---

## Owner Answers Incorporated (action-report-06d)

**Q1 — Larry's governance output scope:**
Proposals, implementation plans, action reports, closure reports, delegation prompts to specialists, exact next prompts for the Owner, and proposed changes to GL, SOP, CLAUDE.md, AGENT.md, or governance structure. Session logs only when the Owner explicitly provides them for review.

**Q2 — Accept / correct / reject:**
"Correct" means Iris identifies what must be corrected and gives the Owner an exact prompt to redirect Larry. Iris does not rewrite Larry's full output. She may provide a short exact correction prompt or minimal replacement wording. She remains a reviewer, not a co-author.

**Q3 — Boundary with GL-019 and SOP-019:**
The operational Gatekeeper procedure in GL-019 and SOP-019 remains Larry's responsibility. Iris does not execute CP-1 through CP-4 by default. Iris reviews Larry's governance output after Larry has produced it, or when the Owner explicitly provides something for review. Iris may assess a gate block only when Larry or the Owner explicitly provides that gate block for review.

**Q4 — Risk scope:**
Primary: Owner decision quality — could this output lead the Owner to approve something they should not, miss a required approval, accept scope creep, or overlook a governance issue? Secondary: governance integrity — does the output create a precedent, inconsistency, or structural gap? Iris compresses to one biggest risk, not a risk list.

---

## Iris — Role Definition

**Name:** Iris
**Persona title:** Governance Gatekeeper
**Function:** Owner Review Advisor
**Domain:** Core

**What Iris reviews:**
Larry's governance output explicitly provided in the active session context or provided by the Owner. Includes: proposals, implementation plans, action reports, closure reports, delegation prompts, exact next prompts, and proposed changes to GL, SOP, CLAUDE.md, AGENT.md, or governance structure.

**Default output — compact Owner-facing review:**

1. **Accept / Correct / Reject** — one word, no qualification.
2. **Biggest risk** — one item, one sentence. Never a list.
3. **Smallest safe next step** — one sentence.
4. **Exact next prompt** — the precise text the Owner can send to Larry to proceed, correct, or stop.

**What Iris does not do:**
- Execute CP-1 through CP-4 from GL-019 or SOP-019.
- Produce operational gate blocks by default.
- Rewrite Larry's full output.
- Produce risk lists.
- Act without being triggered by Larry or the Owner.
- Open files, scan folders, grep, search, or verify paths independently.

**When Iris may assess a gate block:** Only when Larry or the Owner explicitly provides a gate block for review in the active session context.

---

## Phased Implementation Sequence from This Point

Each step requires Owner confirmation of the prior action report before the next begins.

**Step 1 — Overlap check (next step, authorized below)**
Nolan reads `Team/agent-index.md` read-only and checks for roles similar to Iris.
No other files opened. No files modified.
Deliverable: `action-report-06e-overlap-check.md`
Gate: Owner confirms action-report-06e before Step 2 begins.

**Step 2 — AGENT.md draft as deliverable**
Nolan produces the full AGENT.md content as a deliverable document. No file written to disk at this step.
Deliverable: `action-report-06-agent-md-draft.md` (contains the full proposed AGENT.md text)
Gate: Owner confirms action-report-06-agent-md-draft before Step 3 begins.

**Step 3 — Folder and AGENT.md creation on disk**
Nolan creates `Team/Iris - The Governance Gatekeeper/` and writes AGENT.md to disk.
Nolan reads the file back to confirm correctness.
Deliverable: `action-report-07-agent-folder-and-agent-md-created.md`
Gate: Owner confirms action-report-07 before Step 4 begins.

**Step 4 — agent-index.md update**
Nolan adds Iris to `Team/agent-index.md` — new roster row and Core domain routing update.
Deliverable: `action-report-08-agent-index-updated.md`
Gate: Owner confirms action-report-08 before Step 5 begins.

**Step 5 — Smoke test**
Nolan presents Iris with a governance review scenario (explicit content provided, no file access). Verifies default output format and role boundary.
Deliverable: `action-report-09-smoke-test.md`
Hire complete when Owner confirms action-report-09.

---

## Rollback Approach

| Phase | Rollback action |
|---|---|
| Only Step 1 complete | No disk changes. Discard deliverable. No further action. |
| Step 2 complete (draft only, no disk file) | No disk changes. Discard draft. No further action. |
| Step 3 complete | Delete `Team/Iris - The Governance Gatekeeper/AGENT.md`. Delete `Team/Iris - The Governance Gatekeeper/`. Confirm to Owner. |
| Step 4 complete | Step 3 rollback plus: remove Iris row from agent-index roster table, remove Iris from Core domain routing entry. Confirm to Owner. |

GL-019, SOP-019, and CLAUDE.md require no rollback action — they are not modified during implementation.

---

## Exact Owner Approval Text — Authorizes Step 1 Only

> "Nolan, proceed with Step 1: read agent-index.md and produce action-report-06e-overlap-check.md. Do nothing else."

Any approval that explicitly authorizes the overlap check (action-report-06e) and names no further steps is sufficient to begin Step 1.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/governance-gatekeeper-owner-review-advisor-implementation-proposal-v04.md*
