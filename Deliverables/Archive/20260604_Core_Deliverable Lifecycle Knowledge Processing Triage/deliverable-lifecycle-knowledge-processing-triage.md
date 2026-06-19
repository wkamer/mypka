# Deliverable Lifecycle, Knowledge Processing, and Archiving Protocol — Triage Report

**File:** `Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-knowledge-processing-triage.md`
**Date:** 2026-06-04
**Prepared by:** Larry, Team Orchestrator
**Status:** Proposal-only triage — awaiting Owner decision

**Folder rationale:** This triage initiates a new governance topic — the lifecycle and processing
of team deliverables after review and acceptance. It is placed in a new deliverables folder to
keep it cleanly separated from the Review Gate Protocol artifacts (which govern the pre-acceptance
review) and from the Core AI Team Audit (which is formally closed).

**Governance:** This document is read-only. No implementation, SOP or GL creation, file move,
archive operation, PKM or BKM extraction, database write, backlog update, or further governance
work may be executed without Owner Walter Kamer's explicit approval.

---

## 1. Background and Context

The myPKA AI team currently produces deliverables — proposals, execution reports, status reports,
closure reports, triage reports, decision packets — that accumulate in Deliverables folders. The
Review Gate Protocol (GL-016 / SOP-016) governs what happens *before* a deliverable is accepted.
No protocol currently governs what happens *after* a deliverable is accepted as Done.

Without a lifecycle protocol:

- Deliverables accumulate without a defined processing decision
- Knowledge contained in accepted deliverables is not systematically extracted to PKM or BKM
- Authoritative sources cannot be distinguished from superseded or archived material
- Lessons learned remain locked in delivery artifacts instead of reaching agent memories
- Cross-domain content has no routing rule, risking duplication or loss

Owner Walter Kamer wants this lifecycle — including both personal and business processing — defined
in the operating model so it applies consistently regardless of which system, agent, or workflow
produced the deliverable.

---

## 2. Instrument Assessment

### 2.1 Update SOP-016 — Review Gate Procedure

SOP-016 governs the review gate: the pre-acceptance review of a deliverable. Its scope ends at
the Owner decision step. Adding lifecycle and processing rules to SOP-016 would conflate two
distinct concerns: reviewing (does this deliverable meet the standard?) and processing (what
happens to this deliverable now that it does?).

**Not suitable as primary destination.** SOP-016 may reference the Lifecycle Protocol as the
downstream procedure, but should not absorb it.

### 2.2 Update GL-016 — Review Gate Principle

GL-016 defines the principle that governance-relevant deliverables must pass through a review
gate before execution or closure. Its scope is the review gate itself. The lifecycle is a
downstream phase — it begins where GL-016 ends.

**Not suitable as primary destination.** GL-016 may be updated to reference the Lifecycle
Protocol as the downstream instrument, but that is a future optional update, not this protocol.

### 2.3 Update GL-015 — Memory Domain Routing Protocol

GL-015 governs where agent write operations go: which database, which domain tag, which
source_type. The Lifecycle Protocol needs to align with GL-015 for the knowledge extraction
step (where extracted content is written). But GL-015 governs the write routing; the Lifecycle
Protocol governs what triggers the write decision and who approves it. These are different layers.

**Partial alignment required, not an update to GL-015.** The Lifecycle Protocol references
GL-015 for routing rules. GL-015 does not need to change.

### 2.4 Backlog item for later

The absence of this protocol creates ongoing accumulation without a defined processing path.
This is not a future refinement — it is a gap that affects every accepted deliverable now.

**Not suitable as a pure deferral.** The triage is the right action; execution timing is the
Owner's decision.

### 2.5 New SOP only

A SOP-only approach would define the procedure (trigger moments, decision tree, processing
destinations) but leave the governing principle undefined. Future agents or systems would know
how to execute but not why the protocol exists, what states a deliverable can be in, or what
protections apply to authoritative sources.

**Partial fit.** Covers the how but not the why.

### 2.6 New GL only

A GL-only approach would define the lifecycle states and protections but leave the procedure
undefined. Agents would know the principle but not the trigger moments or decision logic.

**Partial fit.** Covers the why but not the how.

### 2.7 Assessment Conclusion

**Best destination: both a new GL and a new SOP.**

This is the same architectural pattern as GL-016 / SOP-016:
- The GL defines the principle: what a deliverable lifecycle is, what states exist, what
  protections apply to authoritative sources, and how this protocol relates to GL-015 and GL-016.
- The SOP defines the procedure: trigger moments, processing destinations, decision rules, domain
  routing, Owner approval gates, and safeguards.

The GL is stable and citable everywhere. The SOP is operational and updatable as processing
workflows mature. Neither duplicates the other.

---

## 3. Proposed Protocol Content

This section documents what the protocol should contain. It is not the final SOP or GL text.
Formal proposal documents will be prepared only after Owner approval of this triage.

### 3.1 Trigger Moments

A processing decision is triggered at each of the following moments. The trigger does not
automatically initiate processing — it surfaces the decision to the orchestrator and Owner.

| Trigger | What happens |
|---|---|
| Proposal ready | Enters review gate (GL-016 / SOP-016); no processing yet |
| Revised proposal ready | Previous version becomes a candidate for "superseded" status |
| Execution report ready | Enters review gate; accepted execution report triggers knowledge extraction review |
| Status report ready | Enters review gate; accepted status report becomes authoritative or is superseded by later version |
| Closure report ready | Enters review gate; accepted closure report triggers knowledge extraction + archive candidate |
| Triage report ready | Enters review gate; accepted triage report remains authoritative source for the initiative it covers |
| Decision packet ready | Enters review gate; accepted decision packet becomes a decision record |
| Deliverable accepted as Done | Primary lifecycle trigger: processing decision must be made for every accepted deliverable |
| Deliverable superseded by newer version | Previous version enters "superseded" state; reference preserved; original file not deleted |

**Rule:** The review gate (GL-016 / SOP-016) must complete before any processing, archiving,
or knowledge extraction decision is made. "Accepted as Done" is the post-review-gate state
that gates the lifecycle protocol.

### 3.2 Lifecycle States

A deliverable passes through these states. Each state has a defined entry condition and a
protected exit path.

| State | Definition | Entry condition | Exit path |
|---|---|---|---|
| Draft | Being prepared; not yet in review | Agent begins producing the deliverable | Submitted for review |
| Under review | Review gate active (GL-016 / SOP-016) | Deliverable submitted for Owner review | Owner decision |
| Approved | Proposal approved for execution; not yet executed | Owner approves execution | Execution begins |
| Executed | Implementation complete; execution report produced | Execution report produced | Execution report enters review |
| Accepted as Done | Owner has accepted the deliverable outcome | Owner decision: Accept as Done | Processing decision required |
| Authoritative | Designated as the canonical reference for a topic | Owner or orchestrator designates; cannot be auto-assigned | Explicit supersession or archiving via proposal |
| Processed | Knowledge has been extracted to PKM, BKM, or agent_learnings | Processing executed with Owner approval | Content lives in target system; source remains |
| Superseded | Replaced by a newer version; preserved but no longer current | Newer version accepted as Done | Archived or retained as historical record |
| Archived | Moved to Archive folder; no longer in active use | Processing decision: archive; references preserved first | Retained in archive indefinitely |
| Parked | Acknowledged but not actioned | Owner selects "accept as parked" | Owner re-opens or explicitly closes |
| Deferred | Valid but postponed; not in active lifecycle | Owner selects "defer" | Owner activates in a future session |

### 3.3 Processing Destinations

Each accepted deliverable is assessed against these destinations. A deliverable may have
multiple applicable destinations (e.g., a closure report may be both authoritative and a
source for lessons learned). Each destination requires a separate Owner-approved action.

| Destination | Description | Who acts |
|---|---|---|
| Authoritative deliverable source | Stays in Deliverables folder; indexed; not moved or modified | Orchestrator designates; Owner confirms |
| PKM — Personal Knowledge Management | Personal decisions, personal insights, personal lessons | Penn or Sienna; Owner approval required |
| BKM — Kamer E-commerce Knowledge | Business knowledge for Kamer E-commerce domain | Nova, Vera, Sasha, or Zara; Owner approval required |
| BKM — Geldstroom Regie Knowledge | Business knowledge for Geldstroom Regie domain | Finn; Owner approval required |
| Team-knowledge governance reference | Governance decisions, team-level patterns, cross-team learnings | Larry; Owner approval for new GL or SOP |
| Personal decision record | A specific decision by Owner Walter Kamer; logged for future reference | Sienna or Marcus; domain: personal |
| Business decision record | A domain-specific business decision | Domain specialist; domain: kamer-ecommerce or geldstroom-regie |
| Lesson learned | Durable insight for one or more specialist agents | Nolan logs to agent_learnings; agent AGENT.md updated | 
| Project note | Relevant to an active project; added to project.md or project KB | Marcus |
| Workstream note | Relevant to a workstream; added via separate proposal | Kai or domain specialist; SOP-015 applies |
| Reference note | Indexed as a future lookup reference; no file move required | Larry indexes |
| Backlog candidate | May warrant a future proposal; registered only after Owner approval | Larry; Owner must approve registration |
| Archive | Moved to Archive folder after references are preserved | Larry via proposal; references confirmed first |
| Superseded | Marked superseded; preserved; not deleted | Larry; original file retained |

### 3.4 Domain Routing — Alignment with GL-015

All knowledge extraction must follow GL-015 (Memory Domain Routing Protocol) for any write
to a database or memory system. The Lifecycle Protocol adds the decision layer on top of GL-015.

| Content type | Domain | Database | GL-015 source_type |
|---|---|---|---|
| Personal insights, personal decisions | personal | personal.db | knowledge or journal |
| Kamer E-commerce business knowledge | kamer-ecommerce | kamer e-commerce.db | knowledge |
| Geldstroom Regie business knowledge | geldstroom-regie | geldstroom-regie.db | knowledge |
| Governance decisions, team patterns | core | team-knowledge.db | knowledge |
| Lessons learned for a specialist | matches agent domain per GL-015 | domain-appropriate DB | knowledge |
| Cross-domain content | — | surface to Owner before any write | Owner decides routing |

**Cross-domain rule:** If extracted content is relevant to more than one domain, it must be
surfaced to Owner before any second write or duplicated processing. The SSOT Golden Rule from
CLAUDE.md applies: every fact lives in exactly one place. Cross-domain access uses references,
not duplication.

### 3.5 Review Gate Relationship

The Lifecycle Protocol is downstream of GL-016 and SOP-016. The relationship is:

1. Deliverable produced → Review gate (GL-016 / SOP-016) applied
2. Review gate passes → Owner makes acceptance decision
3. Owner accepts as Done → Lifecycle Protocol activates
4. Lifecycle Protocol → Owner approves processing destination(s)
5. Processing executed → Deliverable state updated

No lifecycle processing may begin before step 3. A deliverable that has not passed the review
gate is not eligible for processing, archiving, or knowledge extraction.

When the processing decision itself produces a new deliverable (e.g., a lesson-learned entry
or a project note), that new deliverable re-enters the review gate before being written.

### 3.6 Processing Decision Rules

The following rules determine what happens to an accepted deliverable. Rules are applied in
order. A deliverable may satisfy multiple rules.

| Rule | Condition | Action |
|---|---|---|
| R1 — Authoritative source protection | Deliverable is the canonical reference for an active governance item (GL, SOP, canonical path, active project) | Mark authoritative; index; do not move, archive, or delete without a new proposal |
| R2 — Supersession | A newer version of the same deliverable has been accepted | Mark previous version superseded; preserve file; update any references to point to new version |
| R3 — Lessons learned candidate | Deliverable contains a pattern, error, correction, or insight relevant to one or more specialist agents | Surface to Nolan for agent_learnings extraction; Owner approval required before write |
| R4 — Governance reference | Deliverable contains a decision or pattern relevant to the team's operating model | Larry indexes; Owner approval before any GL or SOP update |
| R5 — Personal knowledge candidate | Deliverable contains personal insights or decisions by Owner Walter Kamer | Surface to Sienna or Penn; Owner approval before PKM write |
| R6 — Business knowledge candidate | Deliverable contains domain-specific operational knowledge | Surface to domain specialist; Owner approval before BKM write |
| R7 — Project note candidate | Deliverable contains information relevant to an active project | Surface to Marcus; Owner approval before project.md write |
| R8 — Archive eligible | Deliverable is not authoritative, not a current reference, and all references have been preserved | Archive via proposal; references confirmed before move |
| R9 — Retain in place | Deliverable is authoritative, is referenced by other documents, or has not been assessed yet | No action; retain in Deliverables folder |
| R10 — No action required | Deliverable is a working artifact (intermediate draft, proposal round superseded by later version) that produced no standalone value | Mark superseded; no further action |

**Default rule:** If no processing rule clearly applies, retain in place (R9). Never archive or
delete by default.

### 3.7 Required Safeguards

| Safeguard | Rule |
|---|---|
| No deletion of authoritative sources | A deliverable marked authoritative may not be deleted or moved without a formal proposal and explicit Owner approval |
| No archiving before references preserved | Before any file is moved to Archive, all wikilinks and cross-references pointing to it must be identified and preserved or updated |
| No PKM/BKM extraction without Owner approval for sensitive or domain-crossing content | Any extraction touching personal data, credentials, domain-sensitive information, or cross-domain content requires explicit Owner approval before the write |
| No database writes without explicit approval | No writes to personal.db, team-knowledge.db, kamer e-commerce.db, or geldstroom-regie.db as part of lifecycle processing without Owner approval |
| No automatic backlog creation | Identifying a backlog candidate does not create a backlog entry. The candidate must be surfaced to Owner, who decides whether to register it |
| No moving files without proposal | File moves (including archiving) require a formal proposal specifying source path, target path, and reference preservation plan |
| No loss of traceability | Every processing action must be recorded in an execution report. The source deliverable path must be preserved in all extracted knowledge records |
| No processing of secrets or credentials into PKM/BKM | Deliverables containing credentials, tokens, API keys, or secrets must never be processed into PKM or BKM in a way that exposes those values |
| No duplicate writes (SSOT) | Extracted knowledge is written to exactly one canonical location. Cross-domain references use links, not copies |
| Review gate prerequisite | No processing action begins before the deliverable has passed the review gate and been accepted as Done |

### 3.8 Formal Proposal Requirements

If Owner approves Option C (both GL and SOP), the formal proposals must include:

**GL proposal must cover:**
- Lifecycle states (with entry conditions and exit paths)
- The principle that "Accepted as Done" gates the lifecycle protocol
- The relationship to GL-015 (domain routing alignment)
- The relationship to GL-016 (review gate prerequisite)
- Authoritative source protection principle
- The SSOT principle applied to knowledge extraction
- No automatic processing rule
- Owner approval gate for all processing decisions

**SOP proposal must cover:**
- Trigger moments (table with condition and action)
- Processing destination catalog (all 13 destinations)
- Decision rules R1–R10 (in order, with conditions)
- Domain routing table (aligned with GL-015)
- Safeguard checklist (to be run before any processing action)
- Owner decision options for each processing decision type
- Integration with GL-016/SOP-016 review gate
- Worked examples (at minimum: closure report processing, proposal supersession, lessons learned extraction)

**Execution order:** GL first (principle), SOP second (procedure). Same pattern as GL-016/SOP-016.

---

## 4. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Protocol is too heavyweight for routine deliverables | Define a tiered scope: light processing (mark superseded, retain, index) requires no proposal; heavy processing (PKM/BKM write, archive, lessons learned) requires Owner approval. Define tiers clearly in the SOP. |
| Authoritative sources accidentally archived or deleted | R1 safeguard is a hard stop: authoritative status blocks archive and delete without a new proposal. |
| Cross-domain content duplicated | Cross-domain rule in §3.4 and the SSOT safeguard in §3.7 prevent duplicate writes. Owner must approve routing before any cross-domain write. |
| Credentials or secrets leak into PKM/BKM | Explicit safeguard in §3.7: no processing of deliverables containing secrets. The review gate's secret exposure check (SOP-016 check 9) catches this upstream. |
| Processing decisions accumulate without action | The lifecycle protocol surfaces decisions; it does not require them to be made immediately. Deferred and parked are valid states. Backlog candidates require Owner approval to register. |
| Domain routing conflicts with GL-015 | The Lifecycle Protocol references GL-015 for routing; it does not replace or override it. Any conflict is resolved by GL-015 as the authoritative routing standard. |
| GL/SOP numbers are taken by the time proposals are prepared | Number verification is performed immediately before implementation, following the same pre-check pattern as GL-016/SOP-016. |
| Protocol stales as new deliverable types emerge | Knowledge Currency section in the GL specifies refresh triggers. The SOP's destination catalog is updated via the standard SOP-015 iteration process. |

---

## 5. Relationship to Existing Instruments

| Instrument | Relationship |
|---|---|
| GL-015 (Memory Domain Routing) | Lifecycle Protocol references GL-015 for all database write routing. GL-015 governs where content goes; the Lifecycle Protocol governs what triggers the write decision and who approves it. No change to GL-015 required. |
| GL-016 (Review Gate Principle) | Review gate is a prerequisite of the Lifecycle Protocol. "Accepted as Done" (the post-review-gate state) gates lifecycle processing. GL-016 may optionally reference the Lifecycle Protocol as the downstream instrument in a future update. |
| SOP-016 (Review Gate Procedure) | The review gate procedure must complete before lifecycle processing begins. SOP-016 may optionally reference the Lifecycle Protocol as the downstream procedure in a future update. |
| SOP-015 (Proposal Iteration Protocol) | All formal proposals for SOP or GL creation follow SOP-015 discipline: versioned proposals, Revision Notes, exact-text execution. File moves and workstream updates also follow SOP-015. |
| CLAUDE.md — SSOT Golden Rule | The SSOT principle governs knowledge extraction: one home, no duplication. The Lifecycle Protocol enforces this at the processing decision layer. |
| CLAUDE.md — Deliverables Rule | The Deliverables Rule defines the folder structure (`YYYYMMDD_Domain_beschrijving/`). The Lifecycle Protocol adds the decision layer on top of this structure without changing the naming convention. |

---

## 6. Owner Decision Options

| Option | Action |
|---|---|
| **A** | Approve preparing a formal SOP proposal for the Lifecycle Protocol procedure |
| **B** | Approve preparing a formal GL proposal for the Lifecycle Protocol principle |
| **C** | Approve preparing both — a GL principle proposal and a SOP procedure proposal — as a paired set **(recommended)** |
| **D** | Request amendments to this triage — specify which sections require changes; a v02 will be prepared |
| **E** | Defer |
| **F** | Reject |

---

## 7. Recommended Option

**Option C — approve preparing both a GL principle proposal and a SOP procedure proposal.**

Rationale:

The Lifecycle Protocol has two clearly separable layers. The principle layer (what a deliverable
lifecycle is, what states exist, what protections apply, what prerequisites are required) belongs
in a GL: it is stable, short, and citable from agent instructions, other SOPs, and CLAUDE.md. The
procedure layer (trigger moments, decision rules, destination routing, safeguards) belongs in a
SOP: it is operational and can be updated as processing workflows mature without touching the
principle.

This is the same pattern that proved correct for the Review Gate Protocol (GL-016 / SOP-016).
The two layers serve different audiences: the GL is read by anyone asking "why does this protocol
exist and what does it protect?"; the SOP is read by anyone executing a processing decision.

Option C does not mean both are implemented simultaneously. The GL is shorter, faster to review,
and the prerequisite for the SOP. The recommended execution sequence: GL first, SOP after GL
post-checks pass — identical to the GL-016 / SOP-016 implementation.

Option D is appropriate if Owner Walter Kamer wants to adjust any of the protocol content in
Section 3 before a formal proposal is prepared. All content in Section 3 is draft at this stage.

---

*Delivered on: 2026-06-04*
*Delivered at: Deliverables/20260604_Core_Deliverable Lifecycle Knowledge Processing Triage/deliverable-lifecycle-knowledge-processing-triage.md*
