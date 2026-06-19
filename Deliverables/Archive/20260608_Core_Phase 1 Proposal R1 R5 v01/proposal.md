# Phase 1 Proposal — R1 and R5 (v01)

**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Revision:** v01
**Authorized for proposal preparation:** Owner decision 2026-06-08 (Phase 1 only)
**Source:** `Deliverables/20260608_Core_R1-R5 Prioritization Assessment/assessment.md`
**Scope:** R1 (Minimal-Retention-First Gate) and R5 (Language Rule at Draft Time). Read-only proposal. No implementation until Owner confirmation.

---

## Pre-Proposal Note: GL-013 State

`Team Knowledge/Core/Guidelines/GL-013_Memory Core Architecture.md` currently exists as an empty file. The previous chain (UMC archive eligibility, 2026-06-08) was described as having retained P2 and P5 knowledge in GL-013, but the file has no content. This discrepancy is flagged here for Owner awareness.

This proposal treats GL-013 as an empty file and proposes its first written content as part of W-3 (R1 formal definition). This makes W-3 a full file write, not an append. The Owner should confirm that GL-013 content from the previous chain is not stored elsewhere before authorizing W-3.

---

## Documents Affected

| Write ref | Document | Change type | Rule |
|---|---|---|---|
| W-1 | `CLAUDE.md` | Insert new Hard Rule section | R1 |
| W-2 | `CLAUDE.md` | Insert behavioral rule in `### Communicatie & Toon` | R5 |
| W-3 | `Team Knowledge/Core/Guidelines/GL-013_Memory Core Architecture.md` | Write full file content (currently empty) | R1 |

Total: 2 files, 3 write actions. No deletions. No database changes.

---

## W-1 — CLAUDE.md: New Hard Rule (R1)

### Location

`CLAUDE.md`, `## Hard Rules` section.

Insert position: after the closing `---` of `### Granularity Gate — Deliverable Folder Creation (mandatory)` and before `### Deliverable Registration — Mandatory`.

Current surrounding text (insertion anchor):

```
**Violation trigger:** If Larry creates a deliverable folder without applying this check —
stop, note the potential misclassification, apply the test retroactively, and report
to Owner if the folder should have been a file.

---

### Deliverable Registration — Mandatory
```

### Exact text to insert

```markdown
### Archive Eligibility — Minimal Retention Gate (mandatory)

Before any archive eligibility check proceeds past the initial analysis: apply the two-question retention gate.

**Question 1:** Is the retention action an append to an existing document only — no new system components, no new behavior, no new infrastructure?
- Yes: go directly to a write proposal. No governance triage. GL-022, GL-018, and SOP-019 do not apply.

**Question 2:** Does the retention action require a new system component — cron job, new GL, new SOP, new code, new infrastructure?
- Yes: proceed with governance triage through the standard path.

**Default:** Treat any knowledge gap as retention-only until a specific new system component is identified. Retention-only means appending knowledge to an existing, named document. Uncertainty resolves to retention-only, not governance triage.

**Violation trigger:** If Larry enters governance triage (GL-022, GL-018, SOP-019) for an archive eligibility chain where the only action required is appending to an existing document — stop immediately, redirect to a write proposal, and report the correction to the Owner.

---

```

### Why this change is required

The archive eligibility chain (2026-06-08) applied full governance classification (GL-022, GL-018, SOP-019) to a retention decision that required only appending two sections to GL-013. No mechanism existed to stop that escalation at the eligibility analysis stage. This rule creates that mechanism: a mandatory two-question gate that routes retention-only actions directly to write proposals and reserves governance triage for actions that genuinely require new system components.

### Risks

- **Over-inclusion risk (low):** A case might arise where a retention action is incorrectly classified as "append-only" when it actually needs a governance path. Mitigation: the gate explicitly preserves the governance path for any action requiring new system components. Any new GL, new SOP, new cron job, or new code triggers Question 2 and enters governance triage.
- **Under-specification risk (low):** The boundary between "append to existing document" and "structural change" might be ambiguous for edge cases. Mitigation: the default resolves to retention-only. When genuinely unclear, the Owner is consulted before governance triage is opened.

### Expected benefits

- Archive eligibility chains involving retention-only captures collapse from 4 steps to 2 (eligibility analysis + write proposal).
- Owner review interactions per chain reduce from approximately 4 to 2.
- GL-022, GL-018, and SOP-019 are not triggered for documentation actions.
- Deliverable folder count per archive eligibility chain reduces by approximately 2.

---

## W-2 — CLAUDE.md: Pre-Draft Language Constraint (R5)

### Location

`CLAUDE.md`, `## Behavioral Rules` section, `### Communicatie & Toon` subsection.

Insert position: after the "Store in EN, display in NL" bullet (line 404) and before the "Never use dashes" bullet (line 405).

Current surrounding text (insertion anchor):

```
- **Store in EN, display in NL (gradual transition):** All internal records written to databases (team_tasks, session_logs, agent_learnings, delegation_outcomes) use English. All content shown to the owner uses Dutch. Todoist tasks stay Dutch — they are owner-facing. Journal content stays Dutch — it is personal. File slugs, scripts, variables, and function names are already English. New records follow this rule; no retroactive migration of existing Dutch content required.
- Never use dashes (em dash —, en dash –, gedachtestreepjes, koppeltekens) in any response or in messages drafted for the owner. No exceptions.
```

### Exact text to insert

```markdown
- **System document draft language — pre-draft constraint:** Any document written to `Team Knowledge/` (GL, SOP, WS, AGENT.md, proposal, write plan, write proposal) must begin in English. This check runs before the first word is written, not after the draft is complete. Before drafting any system document, Larry confirms the target language is English. If any draft text for a system document is produced in Dutch, stop, discard the draft, and restart in English. The v01-to-v02 revision cycle for language correction is not an acceptable pattern — the language rule applies at character one.
```

### Why this change is required

The archive eligibility chain produced a write proposal in Dutch (v01) that was immediately revised to English (v02), requiring one additional Owner review interaction. The existing language rule at line 403-404 defines the storage/display distinction but does not specify when the language check is applied. Without a pre-draft trigger, the check defaults to post-draft review, which generates avoidable iteration cycles. This rule moves the check to before the first word is written.

### Risks

- **False stops (very low):** Larry might incorrectly identify a document type as system-facing when it is Owner-facing (Dutch). Mitigation: the rule specifies exactly what qualifies — any file written to `Team Knowledge/`. Owner-facing outputs (chat messages, Todoist tasks, journal entries) are not in scope.
- **Overcorrection risk (none):** The rule does not change the language policy; it only moves the enforcement point earlier in the drafting process.

### Expected benefits

- v01-to-v02 language revision cycles are eliminated.
- One Owner review interaction saved per affected draft.
- The rule reinforces an existing policy at the point where it is most actionable.

---

## W-3 — GL-013: Formal Gate Definition (R1)

### Location

`Team Knowledge/Core/Guidelines/GL-013_Memory Core Architecture.md`

Current state: file exists, content is empty.

### Pre-condition note

Before executing W-3, confirm that GL-013 does not contain content stored elsewhere (renamed file, different path). If P2 and P5 knowledge from the previous chain was written to a different file, that content must be reconciled before W-3 writes. This is the Owner's confirmation point.

### Exact full file content to write

```markdown
# GL-013 — Memory Core Architecture

**Owner:** Larry, Team Orchestrator
**Last updated:** 2026-06-08
**Status:** Active

---

## 1. Purpose

This guideline defines the Unified Memory Core (UMC) architecture for the myPKA team. It specifies how the 8 memory layers are used, how specialists write to the UMC, and how archive eligibility checks are performed.

---

## 2. Archive Eligibility — Minimal Retention Gate

When a deliverable archive eligibility check identifies items not yet captured in the active knowledge architecture, apply this gate before proceeding.

**Question 1:** Is the minimum retention action an append to an existing document only?
- Yes: create a write proposal targeting that document. Do not open a governance triage.

**Question 2:** Does the minimum retention action require a new system component?
- Yes: route through governance triage (GL-018, GL-022, SOP-019 as applicable).

**Default:** Retention-only until a specific new system component is identified.

This gate exists to prevent governance classification frameworks from being applied to documentation-only retention actions. Appending to an existing GL or SOP is a write action, not a structural change. It requires a write proposal and Owner authorization — not a Graduation Candidate assessment or GL-018 impact scoring.

---

## 3. Specialist UMC Write Protocol (P2)

Specialists do not write directly to the UMC summary layer at session close. The delegation model is:

1. Each specialist writes handoff notes to session context at task completion.
2. The close-session skill reads all handoff notes and writes one composite summary per domain using `mm.write_summary()`.
3. The `domain=` and `source_type=` parameters are set per the routing table in CLAUDE.md.

**Canonical reference for domain routing:** CLAUDE.md, `#### Domain routing` table.

**Why this model:** Specialist-level `mm.write_summary()` calls produced fragmented, overlapping, and domain-misrouted entries. The composite model consolidates per domain and ensures correct attribution. See `Deliverables/20260530_Core_UMC diagnose en aanbevelingen/` for the original diagnosis.

---

## 4. Periodic Validation Requirement (P5)

A periodic UMC activity check is required but not yet implemented.

**Requirement:** Weekly count of UMC entries per domain. If any domain goes silent for 7 or more consecutive days without a session having occurred, generate an alert.

**Alert target:** Discord or Team Inbox.

**Status:** Pending implementation. Delegated to Kai. Tagged `umc-monitoring` in team_tasks.

**Why this matters:** A domain going silent typically indicates a specialist is not writing to the UMC, or that the close-session skill is failing silently. Without a periodic check, silent failures accumulate undetected.

---
```

### Why this change is required

GL-013 exists as an empty stub. The previous session intended to write P2 and P5 knowledge to it; that content is not present. W-3 writes the formal gate definition (R1) and restores the P2 and P5 knowledge as the initial content of the file, resolving both the R1 requirement and the empty-file discrepancy.

### Risks

- **Overwrite risk (medium):** If P2 and P5 content was written to a different location and also applies here, W-3 may create a divergence. Mitigation: Owner confirms pre-condition before W-3 executes. W-3 does not execute until the pre-condition is cleared.
- **Scope creep risk (low):** GL-013 as proposed includes more than the R1 gate — it includes P2 and P5 content. If the Owner wants only the gate in GL-013, Sections 3 and 4 can be removed. The gate in Section 2 is the R1 requirement; Sections 3 and 4 are restorative.

### Expected benefits

- GL-013 has its first meaningful content.
- The minimal retention gate has a canonical document-level definition beyond CLAUDE.md.
- P2 (specialist UMC write protocol) and P5 (periodic validation) are documented in their designated location.
- Archive eligibility checks have a referenced document they can point to.

---

## Post-Check Approach

After Owner confirms and all three write actions execute:

1. **W-1 verification:** Read `CLAUDE.md` at the insertion point. Confirm `### Archive Eligibility — Minimal Retention Gate (mandatory)` is present between `### Granularity Gate` and `### Deliverable Registration`. Confirm exact text matches proposal.

2. **W-2 verification:** Read `CLAUDE.md` at line ~405. Confirm the pre-draft constraint bullet is present between the "Store in EN, display in NL" bullet and the "Never use dashes" bullet. Confirm exact text matches proposal.

3. **W-3 verification:** Read `GL-013_Memory Core Architecture.md`. Confirm file is not empty and contains Sections 1 through 4 as proposed. Confirm Section 2 matches the exact gate definition.

4. **Functional check:** After verification, Larry reads back the gate rule from CLAUDE.md verbatim and confirms: "If an archive eligibility analysis identifies a knowledge gap that can be resolved by appending to an existing document, the next step is a write proposal — not a governance triage." This confirms behavioral internalization, not just textual presence.

---

## Summary

| Write ref | Document | Change | Words added | Deletions |
|---|---|---|---|---|
| W-1 | CLAUDE.md | New Hard Rule section | ~120 | 0 |
| W-2 | CLAUDE.md | New bullet in Communicatie & Toon | ~70 | 0 |
| W-3 | GL-013 | Full file content (empty → ~380 words) | ~380 | 0 |

Total: additions only. No existing content modified. No existing content removed.

Owner confirms with: yes / no / correction.

---

Delivered on: 2026-06-08
Delivered at: session
