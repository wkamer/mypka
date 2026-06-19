# Process Review — UMC Archive Eligibility Chain (2026-06-08)

**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Scope:** Read-only assessment. No file modifications, no database changes, no task creation.
**Trigger:** Owner observed unnecessary deliverable growth and absence of visible Iris participation in the chain.

---

## 1. Chain Reconstruction

**Source deliverable:** `20260530_Core_UMC diagnose en aanbevelingen`
Author: Kai. A diagnosis report of UMC behavioral gaps containing five recommendations (P1 through P5).

**Goal of the chain:** Determine whether the source deliverable was safe to archive — i.e., whether each recommendation had been captured in the active knowledge architecture.

**Deliverable folders produced by the chain (2026-06-08):**

| # | Folder | Time | Purpose stated |
|---|---|---|---|
| 1 | `20260608_Core_UMC Archive Eligibility Analysis 20260530` | 11:29 | P1-P5 eligibility per recommendation |
| 2 | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen` | 11:35 | Full governance classification of P2 and P5 |
| 3 | `20260608_Core_Retention Assessment P2 P5 UMC` | 11:37 | Minimum retention action for P2 and P5 |
| 4 | `20260608_Core_Write Proposal GL-013 Additions P2 P5` | 11:42 | Write proposal v01 and v02 for GL-013 |

**Outcome:** P2 and P5 appended to GL-013. Source deliverable archived. P1, P3, P4 confirmed captured elsewhere.

**Minimal outcome required:** Append two sections to GL-013, archive the source deliverable.

**Deliverable folders that were necessary:** 1 (eligibility analysis) and 4 (write proposal). Folders 2 and 3 were not required to reach the outcome.

---

## 2. Finding 1 — GL-017 Granularity Gate Was Not Applied to Chain Artifacts

**What GL-017 requires:** Before creating any deliverable folder, apply the G1 test. The default is G2 (file inside an existing folder). A new folder requires an affirmative G1 answer.

**What G1 catches explicitly:** "execution reports, write-lists, session verification reports, initiation proposals for governance track steps, phase discovery/design documents, incident reports, correction notes, and decision packages for specific actions within a larger flow. These do not become standalone folders."

**Assessment of folders 2 and 3:**

Folder 2 (Governance Triage) is a decision package for a specific action within the archive eligibility flow. Its content — LC/GC classification, GL-018 impact scoring, SOP-019 gatekeeper analysis — is analytical workpaper in service of the eligibility conclusion. It is not independently actionable without the eligibility analysis context.

Folder 3 (Retention Assessment) is a confirmation document that states the conclusion already visible in Folder 2 and implicitly in Folder 1. It adds no new information; it formalizes an intermediate decision within the chain.

Both fail the G1 test. Both should have been `.md` files inside the eligibility analysis folder (Folder 1). The chain should have produced two folders, not four.

**Why this happened:** The GL-017 check was applied to each folder at creation time in isolation, without asking "is this artifact part of an ongoing chain that already has a home folder?" The gate does not currently have a chain-awareness clause.

---

## 3. Finding 2 — Governance Classification Was Applied to a Retention Decision

**What triggered governance classification:** The eligibility analysis identified P2 as a structural gap and P5 as an unimplemented requirement. Larry then applied:

- GL-022 (Learning Candidate / Graduation Candidate classification)
- GL-018 (idea classification — P2 as S7-class, Medium impact)
- SOP-019 (gatekeeper logic — Medium-impact requires proposal and Review Gate)

**What these frameworks are designed for:** Implementation decisions — new system components, new behavioral rules, structural changes to active infrastructure.

**What the chain actually needed:** A retention decision — whether to capture two items of knowledge into an existing document (GL-013) before archiving a completed deliverable.

**The conflation:** Larry treated "this recommendation describes a structural change" as equivalent to "implementing this recommendation now requires full governance triage." These are different questions. The archive eligibility question asks whether the knowledge is safe to lose. The governance question asks whether the implementation is safe to proceed. The chain answered the governance question when it only needed to answer the retention question.

**Consequence:** Two extra folders, three extra Owner review interactions, and a 13-minute chain (11:29 to 11:42) for a two-line GL append.

**What the correct path looks like:** Eligibility analysis identifies P2 and P5 as not yet captured. It proposes the minimum retention action: append knowledge description to GL-013. Write proposal created directly. Owner confirms. GL-013 updated. Source archived. Done in two folders.

---

## 4. Finding 3 — Iris Was Not Visible in the Chain

**What GL-021 Section 5 requires:** For any CAT-3 governance action, the correct sequence is:
1. Larry prepares a complete proposal
2. Iris reviews the proposal
3. Larry presents the reviewed proposal to the Owner

**What was observed:** None of the four deliverable folders contain Iris review metadata. The chain proceeded: create deliverable → present to Owner → Owner approves → next deliverable. Iris was not invoked at any step.

**Why this matters:** Iris is designed to intercept over-expanded proposals before they reach the Owner. In this chain, Iris review of Folder 2 (Governance Triage) would have been the natural point to flag: "this is a retention question, not an implementation question — the governance classification is out of scope."

**Contributing factor:** The Iris AGENT.md was not found at expected location. GL-021 Section 9 notes that the Iris AGENT.md update ("Iris review does not authorize writes; Owner authorization is always a separate subsequent gate") is marked as Pending. If Iris does not have a clear scope definition for when she reviews archive-related deliverables, she cannot be expected to intercept them.

**Secondary factor:** GL-021 specifies Iris review for CAT-3 governance actions. Archive eligibility chains may not be classified as CAT-3 by default, creating a gap: chains that expand into governance territory are not automatically routed to Iris even when they should be.

---

## 5. Finding 4 — No Minimal-Retention-First Rule Exists

**Current state of GL-013:** The file exists in the knowledge base but was empty at the expected path during this review (content may be at a renamed or relocated path). Its retention framework does not contain a "minimal-retention-first" gate.

**The missing rule:** When a deliverable archive eligibility check identifies items not yet captured, the first question must be: "Is the minimum retention action an append to an existing document?" If yes, go directly to write proposal. No governance triage, no LC/GC classification, no GL-018 scoring.

The minimum retention action for this chain was always "append to GL-013." That conclusion was reachable from Folder 1 alone. The chain had no mechanism to stop itself at that conclusion and go directly to a write proposal.

**Effect:** Without a minimal-retention-first gate, every archive eligibility chain that encounters an uncaptured item defaults to the full governance path. This is the wrong default for retention.

---

## 6. Finding 5 — Write Proposal Had an Avoidable v01-to-v02 Cycle

**What happened:** The write proposal (Folder 4) was produced in Dutch (v01), then immediately revised to English (v02) — generating a second iteration within the same folder creation cycle.

**Root cause:** The language rule (GL-014: system files in English) was not applied at drafting time. The correction required a revision round and an additional Owner review interaction.

**Scale:** This is a minor finding compared to Findings 1-4, but it represents a consistent pattern: rules that are known at the start of a task are applied retrospectively after drafting, creating avoidable iteration cycles.

---

## 7. Summary of Findings

| # | Finding | Affected Rule | Severity |
|---|---|---|---|
| 1 | Folders 2 and 3 failed the G1 test and should have been files inside Folder 1 | GL-017 | High |
| 2 | Governance classification (GL-022, GL-018, SOP-019) was applied to a retention decision | No rule distinguishes retention from implementation | High |
| 3 | Iris was not present as a filter at any step of the chain | GL-021 Section 5 | Medium |
| 4 | No minimal-retention-first gate exists in the archive eligibility process | GL-013 (gap) | High |
| 5 | Write proposal was drafted in Dutch, then revised to English, causing one avoidable iteration | GL-014 | Low |

---

## 8. Recommendations

These recommendations are read-only observations. None are implemented here. Each requires Owner authorization before implementation.

### R1 — Add a Minimal-Retention-First Gate to GL-013

Before any archive eligibility chain proceeds past the initial analysis, apply a two-question gate:

- "Is the retention action an append to an existing document?" → If yes: write proposal directly. No governance triage. No GL-018/GL-022 classification.
- "Is the retention action a new system component (cron job, new GL, new SOP, new code)?" → If yes: proceed with governance triage through the standard path.

This gate routes the chain at its first decision point, before multiple deliverable folders are created.

### R2 — Add Chain-Awareness to GL-017

GL-017 currently checks each folder at creation in isolation. Add one clause: "If this artifact is a decision package, triage document, or assessment that exists in service of an ongoing chain that already has a home folder, it is G2 regardless of its content complexity."

This closes the loophole that allows intermediate chain artifacts to pass the G1 test by the apparent complexity of their content, when they are structurally G2 by their role in the chain.

### R3 — Define Iris Trigger for Archive Eligibility Chains

Add to Iris scope definition: "Any chain that produces more than one deliverable folder in service of a single archive eligibility question triggers Iris review before the write proposal reaches the Owner."

This is independent of CAT level. The trigger is chain depth, not governance classification. A chain that needs only one folder (eligibility analysis + write proposal = one folder each) bypasses Iris. A chain that produces three or more folders is automatically flagged for Iris review.

### R4 — Separate Retention from Implementation in Governance Triggers

GL-018, GL-022, and SOP-019 should include an explicit exemption clause: "Retention-only actions — captures of existing knowledge into existing documents, with no new system components, no new behavior, and no new infrastructure — are not subject to the governance triage path. A retention action requires a write proposal and Owner authorization only."

This prevents governance frameworks designed for implementation from being applied to documentation.

### R5 — Apply Language Rule at Draft Time

Reinforce for Larry: system-facing documents (proposals, GLs, SOPs) must be drafted in English from the first word. The language check is not a post-draft review — it is a pre-draft constraint. If Larry detects he is about to draft a system document in Dutch, he stops and redirects before producing any text.

---

## 9. Chain Folder Count: What Would Have Been Correct

| Step | What was created | What should have been created |
|---|---|---|
| Eligibility analysis | `20260608_Core_UMC Archive Eligibility Analysis 20260530/` (folder) | Same — correct |
| Governance triage | `20260608_Core_Governance Triage P2 en P5 UMC aanbevelingen/` (folder) | `governance-triage.md` inside eligibility analysis folder |
| Retention assessment | `20260608_Core_Retention Assessment P2 P5 UMC/` (folder) | Internal section of eligibility analysis document, or `retention-notes.md` inside same folder |
| Write proposal | `20260608_Core_Write Proposal GL-013 Additions P2 P5/` (folder) | Same — correct as standalone |

Correct chain: 2 folders. Actual chain: 4 folders. Overhead: 2 unnecessary folders, 3 avoidable Owner review interactions.

---

Delivered on: 2026-06-08
Delivered at: session
