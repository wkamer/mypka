# Discovery and Scope Proposal: Auto-Processing / Deliverable Lifecycle

**Status:** Proposal — awaiting Owner authorization to proceed
**Date:** 2026-06-07
**Author:** Larry (Team Orchestrator)
**Related:** LC Phase 1 (GL-022, learning_candidates, Iris LC Flag, /close-session LC sweep)

---

## 1. Problem Statement

LC Phase 1 gave the team a working auto-learning foundation: learning candidates are flagged, Iris reviews them, and the /close-session sweep surfaces unresolved items. What that phase does not solve is what happens to the team's output artifacts once they are produced.

The current situation:

- Deliverables land in `Deliverables/` with no lifecycle state. There is no protocol that decides whether a deliverable remains authoritative, must be extracted into knowledge, or can be archived.
- Session logs are written but the insights they contain are not systematically converted into SOPs, GL updates, or project notes.
- Execution reports, audit reports, and closure records are produced but their decisions and lessons learned exist only in the deliverable file. They are not promoted to PKM or BKM.
- The same fact can appear in a session log, a closure record, and a project file without cross-links. Duplicate truth accumulates silently.
- No mechanism exists to flag a deliverable as superseded when a newer version replaces it.

The practical consequence: the team has amnesia about its own outputs. A specialist who needs to know what was decided in a prior governance cycle cannot find it systematically. Knowledge that was produced with effort does not compound.

---

## 2. Goal of Auto-Processing

The goal is not automation for its own sake. The goal is:

1. Every team deliverable reaches a defined final state. No deliverable stays permanently "loose."
2. Valuable insights are promoted to PKM or BKM so future specialists can find them without reading raw deliverable files.
3. Duplicate truth is prevented by establishing a single authoritative home for each fact and linking from all other locations.
4. Superseded deliverables are marked as such so the team does not act on outdated information.
5. The Owner spends no effort tracking which deliverables have been processed and which have not. The system surfaces this automatically at close-session.

---

## 3. Artifact Types In Scope

| Artifact Type | Examples |
|---|---|
| Proposal | Discovery proposals, scope proposals, feature proposals, amendment proposals |
| Execution report | Implementation records, build records, migration records |
| Status report | Phase readiness gate records, smoke test results |
| Closure report | Project closure records, workstream closure records, session closure records |
| Audit report | AI team audit, system audit, knowledge base audit |
| Decision record | Formal governance decisions, overrides, scope changes |
| Research brief | Pax domain research outputs, delta reports |
| Domain knowledge update | AGENT.md amendments, GL/SOP/WS updates when stored as deliverables |
| Triage document | Architecture triage, review gate triage |

All of these are artifacts that were produced by the team with deliberate effort and that contain decisions, insights, or authoritative facts.

---

## 4. Artifact Types Out of Scope

| Artifact Type | Reason |
|---|---|
| Journal entries | Handled by Penn with its own lifecycle |
| Personal routine outputs | Explicitly out of scope per Owner instruction |
| WhatsApp conversation logs | Handled by UMC tool log and GL-008 |
| Raw tool outputs | Handled by UMC PostToolUse hook |
| Session logs | Already handled by /close-session skill |
| Todoist tasks | Owner-facing system, separate from team knowledge |
| Draft files in Team Inbox | Not yet a deliverable; lifecycle starts at Ready state |
| Images and photos | Not knowledge artifacts; stored separately in PKM/Images |

Personal routine processing is out of scope until explicitly authorized by the Owner.

---

## 5. Proposed Lifecycle States

```
Draft → Ready → [Processing] → Processed
                     ↓
              Active / Authoritative
                     ↓
              Superseded → Archived
                     ↓
              Archived (direct)
```

| State | Meaning |
|---|---|
| **Draft** | Being prepared. Not yet a team deliverable. |
| **Ready** | Complete. Awaiting processing decision. |
| **Active / Authoritative** | The current source of truth. No extraction needed; the file itself is the reference. |
| **Processing** | Insights are being extracted into PKM or BKM. |
| **Processed** | Extraction complete. Deliverable archived as reference. |
| **Superseded** | Replaced by a newer deliverable. Marked with a link to the replacement. |
| **Archived** | Filed for reference only. No further processing. |

Transitions are always explicit. No deliverable moves state without a logged decision.

---

## 6. Proposed Processing Destinations

| Destination | What goes there |
|---|---|
| **PKM: KE file** | Personal knowledge that belongs in a Key Element (health, finance, identity) |
| **PKM: project.md** | Decisions and lessons learned for a specific personal project |
| **PKM: goals** | Outcomes that affect a goal's status or direction |
| **BKM: team-knowledge.db** | Team-level patterns, governance decisions, lessons learned |
| **BKM: domain database** | Domain-specific knowledge (Kamer E-commerce, Geldstroom Regie) |
| **BKM: agent_learnings** | Behavioral corrections or improvements for a specific specialist |
| **BKM: GL / SOP update** | Procedural knowledge that warrants a formal document update |
| **BKM: project/workstream notes** | Execution history for a specific project or workstream |
| **Reference only** | Linked from relevant files but not extracted (large reports, raw data) |
| **Archived directly** | No extraction needed; the deliverable has no reusable knowledge content |

Destination is determined per artifact type. A closure report may produce entries in multiple destinations (project notes, decision record, agent_learnings). A status report may go directly to archived.

---

## 7. Key Risks

**Over-processing:** Extracting from every deliverable creates noise. Not every deliverable contains reusable knowledge. A status report that shows "all green" has no knowledge value beyond its date.

**Write authorization bypass:** Automated state transitions or auto-extraction could proceed without Owner confirmation, violating GL-021. Every write action requires explicit authorization.

**Duplicate truth through processing:** If a decision is extracted into both a KE file and a project.md without cross-linking, the processing step creates the problem it was meant to solve.

**Wrong domain routing:** A business deliverable extracted into PKM (personal) or vice versa creates cross-domain contamination that is hard to untangle.

**Loss of provenance:** An insight extracted into a KE file without a backlink to the source deliverable loses its origin. Future specialists cannot verify where it came from.

**Scope creep into personal routines:** The boundary between personal and business processing is load-bearing. Any ambiguity risks violating the explicit out-of-scope instruction.

**Processing paralysis:** A protocol that requires Owner confirmation for every single extraction step will not be used. The design must find the right authorization granularity.

---

## 8. Required Governance Boundaries

These boundaries are non-negotiable and apply to all phases.

1. **Write Authorization Boundary (GL-021):** No state transition and no extraction write to PKM or BKM without Owner confirmation. A prior yes for one artifact does not authorize a subsequent one.

2. **No deletion without approval:** No deliverable is deleted, overwritten, or moved to Archive without explicit Owner confirmation showing the artifact name and proposed action.

3. **Domain routing is explicit:** Every processing action must declare its destination domain (personal, core, kamer-ecommerce, geldstroom-regie) before execution. No implicit routing.

4. **Provenance preservation:** Every extracted knowledge item retains a link to its source deliverable. Extraction does not sever the chain.

5. **Superseded requires replacement link:** A deliverable cannot be marked Superseded unless it carries a direct link to the artifact that replaces it.

6. **Personal routines out of scope:** No processing protocol touches personal routine outputs unless the Owner explicitly authorizes an extension to that scope.

7. **Phase gate before implementation:** No Phase 2 or later work begins without a separate Owner authorization after Phase 1 is validated.

---

## 9. Proposed Phase 1 Scope

Phase 1 is detection and classification only. No extraction, no archiving, no state transitions.

**What Phase 1 builds:**

- A `deliverable_lifecycle` table in `team-knowledge.db` to track artifact name, type, state, processing destination (proposed), and processing date.
- A classification rule set: per artifact type, what is the default proposed destination and state.
- An extension to the /close-session sweep: surface all Ready-state deliverables older than 7 days and show proposed processing action to the Owner.
- A read-only inventory of existing Deliverables/ to classify and register current artifacts.

**What Phase 1 does not do:**

- No extraction of insights into PKM or BKM.
- No file moves or archiving.
- No state transitions beyond the initial registration.
- No automation of any processing step.

**Phase 1 success criterion:** At the end of every /close-session, the Owner sees a list of unprocessed deliverables with a proposed action for each. The Owner can confirm, defer, or reject per item. No deliverable accumulates silently.

---

## 10. What Should Not Be Built Yet

These items are intentionally deferred.

- Auto-extraction pipelines (insights from deliverables into PKM/BKM)
- Auto-archiving on state transition
- Auto-SOP or GL updates triggered by deliverable content
- Integration with UMC for auto-indexing of deliverables
- Processing pipelines for specific artifact types
- Deletion or cleanup automation of any kind
- Personal routine processing
- Cross-deliverable deduplication analysis
- Any Phase 2 or Phase 3 work

The risk of building too much too early outweighs the inconvenience of manual confirmation in Phase 1.

---

## 11. Owner Authorization

The Owner can respond to this proposal with:

- **Yes** to authorize proceeding to Phase 1 design (no implementation yet, design only)
- **No** to stop here
- **Correction** to adjust scope, boundaries, or definitions before proceeding

No implementation, file writes, database updates, or document creation will occur without a separate write authorization after the design phase.

---

*Delivered on: 2026-06-07*
*Delivered at: /opt/myPKA/Deliverables/20260607_Core_Auto-Processing Deliverable Lifecycle Discovery/discovery-scope-proposal.md*
