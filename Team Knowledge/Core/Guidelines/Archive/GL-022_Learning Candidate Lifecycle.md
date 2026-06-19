# GL-022 — Learning Candidate Lifecycle

**Last reviewed:** 2026-06-07
**Status:** Active

---

## Section 1 — Purpose and Scope

This guideline governs the full lifecycle of Learning Candidates (LCs): behavioral observations
flagged by team members as potentially useful beyond the current session. It implements the
mitigation defined in GL-020 Section 8 Risk 5 (Level 2 Candidate Decay).

Cross-references: [[GL-020_Intent Classification Taxonomy]] Section 5 and Section 8 Risk 5,
[[GL-021_Owner Interaction Rule and Write Authorization Boundary]] Section 7

---

## Section 2 — What Is a Learning Candidate?

A Learning Candidate exists when a team member encounters an observation during execution that:
1. Does not meet the Level 1 boundary criterion: a third party reading the team member's
   AGENT.md without session context could not have predicted this behavioral change, AND
2. Is not yet a confirmed structural change requiring SOP-019.

Level 1 learnings are autonomous — never registered as LCs.
Level 2 learnings are registered in `learning_candidates` and tracked per this guideline.
The `level` field is always 2. Level 3 learnings trigger SOP-019 immediately and are never
entered as new records in `learning_candidates`.

A Level 2 record may be escalated by Owner decision. At Triage, `triage_routing` is set to
`graduation_candidate`. When processed, `processed_outcome` records the specific structural
change produced (e.g., `sop_update`, `guideline_update`). Status transitions to `processed`,
then `closed`. The `level` field remains 2 as origin documentation.

---

## Section 3 — Lifecycle States and Transitions

| Status | Definition |
|---|---|
| `captured` | Registered. Not yet reviewed. Larry owns. |
| `triaged` | Reviewed. Category confirmed, level confirmed, routing determined. |
| `processed` | Action taken. Outcome recorded in `processed_outcome`. |
| `closed` | Concluded. No further action. |

Valid transitions: `captured → triaged → processed → closed`.
No silent expiry. No implicit approval. An LC cannot leave `captured` without being triaged.
An LC cannot leave `triaged` without an explicit processing or closure action.

**Outcome fields (set at Processing):**
- `triage_routing` — routing classification set at Triage: `graduation_candidate`, `standard`, or `urgent`
- `processed_outcome` — result set at Processing: see Section 7 for the full enum

---

## Section 4 — Who Flags, Who Owns

Any team member may flag a Level 2 candidate. The flagging threshold is intentionally low.

**Standard flagging fields:**
1. `title` — one sentence
2. `description` — what was observed and why it qualifies as a candidate
3. `category` — GL-020 CAT that produced the observation (CAT-1 through CAT-6)

**Exception — Iris:** Iris flags with title and category only. The review output in which
the LC Flag appears serves as the implicit description. Larry records the description during
registration, drawing from the review context. Iris does not provide a separate description
field.

Ownership transfers immediately to Larry upon flagging.
Larry is the sole owner of all LCs after flagging.

---

## Section 5 — Triage Rules

| Situation | When to triage |
|---|---|
| CAT-3 Governance Input → Level 2 | Same session as flagging — no delay |
| Level 3 learning | SOP-019 triggered same session — never enters this register |
| All other categories, within max_days_captured | At next /close-session |
| Any captured LC older than max_days_captured (default 3) | Mandatory at next /close-session |

`max_days_captured` default is 3. Stored per row and adjustable at flagging time.

**Phase 1 sweep point:** /close-session only.
Personal routines (Morning Routine, Afternoon Routine, End-of-Day Routine) are outside the
scope of LC tracking. A dedicated system-maintenance flow may extend sweep points in a
future phase — see Section 9.

---

## Section 6 — Decay Prevention

Five layers, scoped to Phase 1:

1. **Durable registration:** every LC written to `learning_candidates` at flagging with
   `flagged_at` timestamp and `status = 'captured'` — no "flagged and forgotten" possible.
2. **Staleness trigger at /close-session:** at every /close-session, Larry queries all
   `captured` rows. Rows where `days_captured >= max_days_captured` are included in the
   /close-session write plan and triaged after Owner confirmation.
3. **Ownership transfer:** passes from flagging team member to Larry at flagging moment.
4. **Explicit closure paths:** exactly two terminal states — `processed` and `closed`.
   Outcome recorded in `processed_outcome`. No passive expiry, no implicit approval.
5. **Write plan inclusion:** overdue LC triage updates are included in the /close-session
   write plan per GL-021 Section 7 and execute after Owner confirmation.

---

## Section 7 — Operational Write Rules

**Batch 1** (CAT-3 — Larry prepares → Iris review → Owner authorization):

| Write | Description |
|---|---|
| W-1 | MIGRATE TABLE learning_candidates in team-knowledge.db — new lifecycle states (`captured`, `triaged`, `processed`, `closed`); new fields: `processed_outcome`, `processed_at`, `learning_scope`, `target_agent`, `triage_routing`, `source_domain`, `affected_domain`, `target_database`, `source_reference`; renamed: `triaged_at`, `triaged_session`, `max_days_captured` |
| W-2 | GL-022 document (this file) — Sections 2, 3, 5, 6, 7, 10 updated |
| W-3 | gl-index.md — GL-022 entry description updated |

**Batch 2** (CAT-3 — separate batch, requires Batch 1 complete):

| Write | Description |
|---|---|
| W-4 | /close-session — Step 1 scan, Step 1b write plan label, Step 3b SQL and Python |
| W-5 | GL-021 — Section 7 description update |

**Post-implementation operational writes** (SOP-bounded, pre-authorized per GL-021 Section 7):

| Write | Authorization |
|---|---|
| INSERT new LC row at flagging (`status = 'captured'`) | Included in session write plan |
| UPDATE status → `triaged` at /close-session sweep | Included in /close-session write plan |
| UPDATE status → `processed` or `closed` with `processed_outcome` | Owner's decision statement is the authorization — no separate 'yes' required |

**`processed_outcome` enum:**
`team_learning` — `agent_learning` — `guideline_update` — `sop_update` — `agent_instruction_update` — `claude_instruction_update` — `backlog_item` — `deliverable_lifecycle_item` — `rejected` — `deferred` — `no_action`

**`triage_routing` enum:**
`graduation_candidate` — `standard` — `urgent`

**`learning_scope` enum:**
`team` — `agent` — `governance` — `process` — `session` — `tooling` — `owner_interaction`

**`source_domain` enum:**
`core` — `personal` — `kamer_ecommerce` — `geldstroom_regie` — `cross_domain`

---

## Section 8 — Roles

| Role | Responsibility |
|---|---|
| **Larry** | Sole owner after flagging. Registers (including description reconstruction for Iris-flagged LCs). Sweeps at /close-session. Surfaces to Owner. Updates status after Owner decision. |
| **Iris** | Flags with title + category only via optional LC Flag line. Review context is implicit description. Ownership transfers to Larry immediately. Does not register. |
| **Responsible team member** | Flags with three fields. No further action after flagging. Applies approved Level 2 behavior autonomously after Owner approval. |
| **Nolan** | Updates AGENT.md files when a promoted Level 3 LC produces structural changes. Receives brief from Larry after Owner approval. |
| **Kai** | Available for database implementation or maintenance when assigned. |

---

## Section 9 — Future Extension

Phase 1 sweep point is /close-session only.

A future governance-maintenance or system-maintenance flow may add additional LC sweep
points — for example, a weekly system-health command that surfaces aged candidates without
requiring a full /close-session. This extension:

- Is explicitly outside the scope of personal routines (Morning, Afternoon, End-of-Day)
- Requires separate Owner authorization before implementation
- Would be designed as a standalone governance command, not embedded in personal workflows
- Will reference this GL and extend Section 5 when authorized

No action is taken on this extension until the Owner explicitly initiates the design flow.

---

## Section 10 — Changelog

| Date | Change | By | Approval |
|---|---|---|---|
| 2026-06-06 | Initial creation. LC lifecycle, status states, ownership rule, surfacing rules (Phase 1: /close-session only), decay prevention, pre-authorization scope, roles, Future Extension note. Iris exception in Section 4: title + category only, review context as implicit description. Implements GL-020 Section 8 Risk 5 mitigation. Iris-reviewed and accepted. | Larry | Owner |
| 2026-06-07 | Batch 1 naming alignment. Lifecycle states renamed: pending→captured, surfaced→triaged; terminal statuses (approved/rejected/promoted) replaced by processed and closed with processed_outcome and triage_routing outcome fields. Sections 2, 3, 5, 6, 7 updated. New fields: processed_outcome, triage_routing, learning_scope, target_agent, source_domain, affected_domain, target_database, source_reference. Field renames: surfaced_at→triaged_at, surfaced_session→triaged_session, max_days_pending→max_days_captured. Basis: LC Naming Alignment Impact Assessment v05. Iris-reviewed and Owner-authorized. | Larry | Owner |
