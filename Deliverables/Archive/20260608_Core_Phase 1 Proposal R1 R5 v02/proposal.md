# Phase 1 Proposal — R1 and R5 (v02)

**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Revision:** v02
**Supersedes:** `Deliverables/20260608_Core_Phase 1 Proposal R1 R5 v01/proposal.md`
**Authorized for proposal preparation:** Owner decision 2026-06-08 (Phase 1 only)
**Source:** `Deliverables/20260608_Core_R1-R5 Prioritization Assessment/assessment.md`
**Scope:** R1 (Minimal-Retention-First Gate) and R5 (Language Rule at Draft Time). Read-only proposal. No implementation until Owner confirmation.

---

## Revision Notes (v01 → v02)

**Removed:** W-3 (GL-013 full file write). W-3 was based on a false premise: GL-013 was incorrectly assessed as empty. Reconciliation analysis `Deliverables/20260608_Core_GL-013 Reconciliation Analysis/reconciliation.md` confirmed GL-013 contains 4,977 bytes including P2 and P5 content written and verified in the previous session. W-3 as proposed would have overwritten valid existing content. Owner rejected W-3 and confirmed no further GL-013 action is required.

**Unchanged:** W-1 and W-2. Both remain valid. No content changes from v01.

**Owner decision on v01:** W-1 acceptable in principle. W-2 acceptable in principle. W-3 rejected.

---

## Documents Affected

| Write ref | Document | Change type | Rule |
|---|---|---|---|
| W-1 | `CLAUDE.md` | Insert new Hard Rule section | R1 |
| W-2 | `CLAUDE.md` | Insert behavioral rule in `### Communicatie & Toon` | R5 |

Total: 1 file, 2 write actions. No deletions. No database changes. No GL-013 modifications.

---

## W-1 — CLAUDE.md: New Hard Rule (R1)

### Location

`CLAUDE.md`, `## Hard Rules` section.

Insert position: after the closing `---` of `### Granularity Gate — Deliverable Folder Creation (mandatory)` and before `### Deliverable Registration — Mandatory`.

### Insertion anchor (current surrounding text)

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

The archive eligibility chain (2026-06-08) applied full governance classification to a retention decision that required only appending two sections to an existing document. No mechanism existed to stop that escalation. This rule creates a mandatory two-question gate that routes retention-only actions directly to write proposals and reserves governance triage for actions that genuinely require new system components. Without this gate, every uncaptured item in an archive eligibility check defaults to the full governance path, generating unnecessary deliverable folders and Owner review interactions.

### Risks

**Over-inclusion (low):** A retention action might be incorrectly classified as append-only when it actually requires a governance path. Mitigation: the gate explicitly routes any new system component through governance triage. Any new GL, new SOP, new cron job, or new code triggers Question 2.

**Ambiguity at the boundary (low):** The distinction between "append to existing document" and "structural change" may occasionally be unclear. Mitigation: the default resolves to retention-only. When genuinely uncertain, the Owner is consulted before governance triage is opened.

### Expected benefits

- Archive eligibility chains involving retention-only captures collapse from four steps to two (eligibility analysis and write proposal).
- Owner review interactions per chain reduce by approximately two.
- GL-022, GL-018, and SOP-019 are not triggered for documentation-only actions.
- Deliverable folder count per archive eligibility chain reduces by approximately two.

---

## W-2 — CLAUDE.md: Pre-Draft Language Constraint (R5)

### Location

`CLAUDE.md`, `## Behavioral Rules` section, `### Communicatie & Toon` subsection.

Insert position: after the "Store in EN, display in NL" bullet and before the "Never use dashes" bullet.

### Insertion anchor (current surrounding text)

```
- **Store in EN, display in NL (gradual transition):** All internal records written to databases (team_tasks, session_logs, agent_learnings, delegation_outcomes) use English. All content shown to the owner uses Dutch. Todoist tasks stay Dutch — they are owner-facing. Journal content stays Dutch — it is personal. File slugs, scripts, variables, and function names are already English. New records follow this rule; no retroactive migration of existing Dutch content required.
- Never use dashes (em dash —, en dash –, gedachtestreepjes, koppeltekens) in any response or in messages drafted for the owner. No exceptions.
```

### Exact text to insert

```markdown
- **System document draft language — pre-draft constraint:** Any document written to `Team Knowledge/` (GL, SOP, WS, AGENT.md, proposal, write plan, write proposal) must begin in English. This check runs before the first word is written, not after the draft is complete. Before drafting any system document, Larry confirms the target language is English. If any draft text for a system document is produced in Dutch, stop, discard the draft, and restart in English. The v01-to-v02 revision cycle for language correction is not an acceptable pattern — the language rule applies at character one.
```

### Why this change is required

The archive eligibility chain produced a write proposal in Dutch (v01) that was immediately revised to English (v02), requiring one additional Owner review interaction. The existing language rule defines the storage and display distinction but does not specify when the check is applied. Without a pre-draft trigger, the check defaults to post-draft review and generates avoidable iteration cycles. This rule moves the enforcement point to before the first word is written.

### Risks

**False stops (very low):** Larry might incorrectly identify an Owner-facing document as a system document. Mitigation: the rule specifies exactly what qualifies — any file written to `Team Knowledge/`. Owner-facing outputs (chat messages, Todoist tasks, journal entries) are not in scope.

**Overcorrection (none):** The rule does not change the language policy. It moves the enforcement point earlier in the process.

### Expected benefits

- Language revision cycles (v01 Dutch to v02 English) are eliminated.
- One Owner review interaction saved per affected draft.
- The rule reinforces an existing policy at the point where it is most actionable.

---

## Post-Check Approach

After Owner confirms and both write actions execute:

**W-1 verification:** Read `CLAUDE.md` at the insertion point. Confirm `### Archive Eligibility — Minimal Retention Gate (mandatory)` is present between `### Granularity Gate — Deliverable Folder Creation (mandatory)` and `### Deliverable Registration — Mandatory`. Confirm exact text matches this proposal word for word.

**W-2 verification:** Read `CLAUDE.md` in `### Communicatie & Toon`. Confirm the pre-draft constraint bullet is present between the "Store in EN, display in NL" bullet and the "Never use dashes" bullet. Confirm exact text matches this proposal word for word.

**Functional check:** After both verifications pass, Larry reads back the W-1 gate rule verbatim and confirms: "If an archive eligibility analysis identifies a knowledge gap resolvable by appending to an existing document, the next step is a write proposal, not a governance triage." This confirms behavioral internalization beyond textual presence.

---

## Summary

| Write ref | Document | Location | Words added | Deletions |
|---|---|---|---|---|
| W-1 | `CLAUDE.md` | After Granularity Gate, before Deliverable Registration | ~120 | 0 |
| W-2 | `CLAUDE.md` | After "Store in EN" bullet, before "Never use dashes" bullet | ~75 | 0 |

Total: one file, two insertions, additions only. No existing content modified. No existing content removed. No GL-013 changes.

Owner confirms with: ja / nee / correctie.

---

Delivered on: 2026-06-08
Delivered at: session
