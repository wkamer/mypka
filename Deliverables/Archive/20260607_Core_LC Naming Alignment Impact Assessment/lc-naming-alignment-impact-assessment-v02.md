# LC Naming Alignment Impact Assessment — v02

**Date:** 2026-06-07
**Author:** Larry
**Supersedes:** lc-naming-alignment-impact-assessment.md (v01)
**Status:** Read-only assessment — no files modified, no databases updated
**Scope:** Learning Candidate Lifecycle simplification, naming alignment, table consolidation
**Goal model:** `Captured → Triaged → Processed → Closed`

---

## 1. Executive Verdict

V01 was returned for revision on five grounds: a stated "two-batch" path that defined three batches; two conceptual questions that were not open; incorrect output label recommendation; missing `team_learnings` table investigation; and missing schema direction for `learning_scope`, `processed_outcome` enumeration, and `closure_reason` assessment.

This v02 corrects all five areas and adds the table consolidation assessment. The Owner's model is confirmed and fully specified below. Remaining open questions are technical-behavioral only — no conceptual model questions remain open.

---

## 2. Owner-Confirmed Model

### 2.1 Lifecycle states

```
captured → triaged → processed → closed
```

Formal status values for the `status` field:

| Value | Definition |
|---|---|
| `captured` | LC registered. Not yet reviewed. Larry owns. |
| `triaged` | LC reviewed. Category confirmed, level confirmed, routing determined. Awaiting processing action. |
| `processed` | Action taken. Outcome recorded in `processed_outcome`. |
| `closed` | LC concluded. No further action. |

Valid transitions: `captured → triaged → processed → closed`.
No silent expiry. No implicit approval. No transition without deliberate action.

### 2.2 Terminology decisions (all confirmed)

| Term | Definition |
|---|---|
| LC | Learning Candidate |
| GL | Guideline (KE prefix reserved for Key Element files) |
| Graduation Candidate | Classification or routing qualification applied during Triage or Process — not a separate lifecycle, not a separate system |
| Team Learning | A possible value of `processed_outcome` — not a lifecycle state |
| Landing | Not the formal lifecycle term — not to be used |
| Process / Processed | Formal wording |

### 2.3 SSOT for learnings

`learning_candidates` is the canonical learning lifecycle store and audit trail.
`team_log` remains in use as a chronological operational/team/session log — not a canonical learning lifecycle store.
`team_learnings` is not canonical unless explicitly justified and approved.
`agent_learnings` is assessed as legacy or absorbable into `learning_candidates`. See Section 6.

---

## 3. Database / Table Findings

### 3.1 Confirmed state of all domain databases

All four domain databases exist as files. None contain any tables.

| Database | File exists | Tables | Notes |
|---|---|---|---|
| `team-knowledge.db` | Yes | None | No tables implemented |
| `personal.db` | Yes | None | No tables implemented |
| `kamer-ecommerce.db` | Yes | None | No tables implemented |
| `geldstroom-regie.db` | Yes | None | No tables implemented |

The only `CREATE TABLE` statements found in the entire active codebase are in `Team Knowledge/Core/Integrations/memory-db/init.sql`, which creates `tool_logs` and `memory_summaries` for the UMC memory database. These are not part of the domain database system.

**Consequence:** No data migration is required for any proposed change. All changes to table schemas and status values are pre-implementation corrections applied to design documents only.

### 3.2 `learning_candidates`

| Attribute | Finding |
|---|---|
| Exists in database | No — not implemented |
| Schema defined | Yes — in Write-List v05 W-1 DDL (deliverable, not yet executed) |
| Current status values in DDL | `pending`, `surfaced`, `approved`, `rejected`, `promoted` |
| Conflict with new model | Yes — all five values must change |
| Role | Canonical learning lifecycle store (Owner confirmed) |

### 3.3 `team_log`

| Attribute | Finding |
|---|---|
| Exists in database | No — not implemented |
| Schema defined | No — no DDL found anywhere in the codebase |
| Referenced in | CLAUDE.md (line 68), Larry AGENT.md (line 106), all 14 specialist AGENT.md files |
| Stated purpose in Larry AGENT.md | "Team decisions and learnings" |
| Stated purpose in CLAUDE.md | Written at session close when "a new pattern or insight emerged that affects team level" — INSERT one `team_log` row |
| Written by | Any specialist, as part of session close routine |
| Overlap with LC `processed_outcome = 'team_learning'` | Yes — see Section 6.3 |
| Should remain separate | Yes, as a chronological operational log — not as canonical learning lifecycle store |
| Canonical status | Non-canonical for learnings. Operational log only. |

### 3.4 `team_learnings`

| Attribute | Finding |
|---|---|
| Exists in database | No |
| Schema defined | No — no DDL found anywhere |
| Referenced in active files | No — not referenced in any AGENT.md, CLAUDE.md, script, or GL/SOP |
| Only occurrence | The v01 assessment document (written by Larry in this session) |
| Origin of Owner's concern | Possibly confused with `agent_learnings` or a future planned table |
| Conclusion | `team_learnings` does not exist as a concept or table in the current active system. It is not canonical, not legacy, and not implemented. No action needed unless the Owner explicitly introduces it as a new table. |

### 3.5 `agent_learnings`

| Attribute | Finding |
|---|---|
| Exists in database | No — not implemented |
| Schema defined | No — no DDL found anywhere in the codebase |
| Referenced in active files | Yes — extensively: CLAUDE.md (lines 67, 322, 526), Larry AGENT.md, all 14 specialist AGENT.md files |
| Stated purpose | "Specialist self-improvement notes" (Larry AGENT.md line 107) |
| Written by CLAUDE.md | Two triggers: (1) one row per delegation alongside `delegation_outcomes`; (2) per Teamgroei protocol when a specialist receives feedback or learns a pattern |
| `graduation_candidate` tag | Used in `agent_learnings.tags` for the Kennisgraduatie mechanism in Larry AGENT.md — marks rows eligible for promotion to SOP/GL |
| Dual-purpose problem | `agent_learnings` is currently used for both delegation notes (behavior tracking per task) and behavioral learning records (what changed in how an agent behaves). These are different concerns. |
| Overlap with `learning_candidates` | High — the behavioral-learning purpose of `agent_learnings` is exactly what `learning_candidates` is designed to capture |
| Overlap with `delegation_outcomes` | Partial — delegation notes may duplicate what `delegation_outcomes` already records |
| Canonical status | Non-canonical under Owner direction. Legacy or absorbable. |

---

## 4. Conceptual Corrections from v01

### 4.1 Team Learning — no longer an open conceptual question

V01 treated Team Learning as an unresolved conceptual ambiguity requiring Owner direction. This was incorrect.

Owner confirmation: Team Learning is a possible `processed_outcome` of a Learning Candidate. This is a confirmed decision.

The remaining question is technical-behavioral only:

> When an LC is processed with `processed_outcome = 'team_learning'`, should the system also create a `team_log` row as a chronological reference — or is the `learning_candidates` record sufficient as the sole store?

This is a design question about dual-write behavior, not a conceptual model question. It belongs to Batch 3 scoping, after the core lifecycle model is implemented.

### 4.2 Graduation Candidate — no longer an open conceptual question

V01 treated the dual-context use of "Graduation Candidate" as an unresolved conceptual ambiguity. This was incorrect.

Owner confirmation: Graduation Candidate is a classification or routing qualification applied during Triage or Process. It is not a separate lifecycle, not a separate system.

The remaining question is technical-behavioral only:

> The `graduation_candidate` tag in `agent_learnings.tags` (Larry AGENT.md Kennisgraduatie mechanism) predates `learning_candidates`. If `agent_learnings` behavioral-learning rows are absorbed into `learning_candidates`, then the Kennisgraduatie mechanism must be re-expressed using `processed_outcome = 'graduation_candidate'` or a `triage_routing` field on the LC record. This is an absorption design question — not a conceptual model question.

### 4.3 Step 5 / Graduation candidates in /close-session

V01 suggested the /close-session Step 5 section title "Graduation candidates" might be renamed to "Structural promotions." With the Owner's clarification, the rename is not required: "Graduation candidate" remains valid as a classification label within Step 5's scanning logic. The step's purpose is unchanged — scanning for insights that qualify for structural promotion. What changes is only the output: qualifying insights should be flagged as LCs with appropriate routing classification rather than handled through a separate ad-hoc process.

---

## 5. Naming Corrections from v01

### 5.1 Implementation path wording

V01 stated "the safest path is two batches" but defined three batches. This was an inconsistency.

Corrected statement: The safest path is three batches, with Batch 3 deferred pending resolution of two technical-behavioral design questions.

### 5.2 Print label — overdue LC scan

V01 recommended leaving the print label `LC pending: {total}, LC overdue: {overdue}` unchanged, on grounds that it is prose and not a DB status value. The Owner explicitly requires naming consistency across operational and bash output. This was incorrect.

Corrected label (for both print statements in /close-session Steps 1 and 3b):

```python
print(f"Learning Candidates captured: {total}, Learning Candidates overdue_for_triage: {overdue}")
print(f"Learning Candidates triaged: {updated}")
```

### 5.3 Decision verb "promote-to-sop"

V01 used `'promote-to-sop'` as a decision verb in the `resolve_lc` function. This is too narrow — structural routing may target SOP, GL, AGENT.md, CLAUDE.md, Backlog, Deliverable Lifecycle, or another governed target.

Corrected verb: `'escalate'` as the broader action term. The specific routing target is recorded in `processed_outcome` (e.g., `'sop_update'`, `'guideline_update'`, `'agent_instruction_update'`).

---

## 6. Table Consolidation Assessment

### 6.1 `learning_candidates` — canonical SSOT

**Role after consolidation:** Single Source of Truth for all learnings that enter the governed lifecycle.

This includes:
- Observations flagged during execution (current GL-022 scope)
- Behavioral learning patterns that would previously have been written to `agent_learnings`
- Team-level patterns that would previously have been written to `team_log` as learnings

`learning_candidates` is not a chronological log. It is a governed lifecycle store. Every record has a defined path from `captured` to `closed`.

**Verdict:** Keep. Canonical. SSOT for learning lifecycle.

### 6.2 `team_log` — operational log, non-canonical for learnings

**Role after consolidation:** Chronological operational record of team events, patterns, and session-level observations. Not a learning lifecycle store.

`team_log` serves as a log of what happened at team level — similar to a git commit history or a ship's log. It is referenced in all specialist AGENT.md files as one of the standard session-close writes.

After consolidation, the `team_log` entry written in /close-session Step 4 should:
- Remain in use for operational context and chronological record-keeping
- NOT be treated as the canonical record for behavioral learnings
- When a learning also warrants a `team_log` entry, the `learning_candidates` record is the SSOT; the `team_log` entry is supplementary context

The open technical question (Section 4.1) is whether the Step 4 write still creates a `team_log` row independently, or whether it is now triggered only when an LC with `processed_outcome = 'team_learning'` is processed.

**Verdict:** Keep as operational log. Non-canonical for learnings. Scope of Step 4 write behavior is a Batch 3 technical question.

### 6.3 `team_learnings` — does not exist

As confirmed in Section 3.4, `team_learnings` does not exist anywhere in the active system. It was not referenced in any active file before the v01 assessment introduced it.

**Verdict:** No action needed. If the Owner later decides to introduce a `team_learnings` concept, it must go through the standard CAT-3 governance gate.

### 6.4 `agent_learnings` — legacy / absorbable

**Current behavioral coverage:**
1. Delegation notes: one row per delegation, written alongside `delegation_outcomes`
2. Behavioral learning: per Teamgroei protocol when a specialist receives feedback or learns a pattern
3. Kennisgraduatie hook: rows with `tags = 'graduation_candidate'` surfaced at session-close for potential promotion to SOP/GL

**Assessment of each use:**

| Use | Absorbable into `learning_candidates`? | Notes |
|---|---|---|
| Delegation notes (per task) | No — different purpose | Delegation notes document what a specialist did and returned, not a behavioral observation for the team. These belong in `delegation_outcomes` or a dedicated delegation-note field there. |
| Behavioral learning (Teamgroei) | Yes | This is exactly what `learning_candidates` captures: observations that may change how an agent behaves. Should be registered as LCs with appropriate `learning_scope` and `flagged_by` values. |
| Kennisgraduatie (`graduation_candidate` tag) | Yes | In the new model, these become LCs with `triage_routing = 'graduation_candidate'` or `processed_outcome = 'graduation_candidate'` after escalation. The tag mechanism in `agent_learnings` is superseded. |

**Absorption path:**
The behavioral-learning and graduation-candidate uses of `agent_learnings` can be fully absorbed into `learning_candidates`. The delegation-note use should remain in `delegation_outcomes` (the table already exists conceptually for this purpose).

If absorption proceeds:
- CLAUDE.md Teamgroei section (line 526) must be updated: "Log naar `agent_learnings`" → "Register as Learning Candidate in `learning_candidates`"
- CLAUDE.md session log rule (line 67) must be updated: "write one row to `agent_learnings`" → removed or redirected to `delegation_outcomes` for delegation notes only
- Larry AGENT.md Kennisgraduatie block must be replaced with LC-based escalation logic
- All 14+ specialist AGENT.md files contain the boilerplate "writes all operational records (session_logs, agent_learnings, team_log, ...)" — if `agent_learnings` is absorbed, this boilerplate changes across every specialist file

**Verdict:** Legacy. Preferred direction is absorption into `learning_candidates` (behavioral rows) and `delegation_outcomes` (delegation notes). This is a Batch 3 or later change due to the breadth of AGENT.md updates required (14+ files). Requires CAT-3 governance gate.

---

## 7. Recommended `learning_candidates` Schema Direction

This section proposes the direction for the DDL update. This is not the final DDL — that belongs in a revised Write-List. This is the schema model the implementation should follow.

### 7.1 Status field

```sql
status TEXT NOT NULL DEFAULT 'captured'
    CHECK(status IN ('captured', 'triaged', 'processed', 'closed'))
```

Remove `pending`, `surfaced`, `approved`, `rejected`, `promoted`.

### 7.2 Timestamp fields

Rename `surfaced_at` → `triaged_at` and `surfaced_session` → `triaged_session` for alignment.

Add `processed_at TEXT` for the transition from `triaged` to `processed`.

### 7.3 `processed_outcome` field — new, required

Captures what action was taken when the LC moved to `processed` or `closed`.

```sql
processed_outcome TEXT CHECK(processed_outcome IN (
    'team_learning',
    'agent_learning',
    'guideline_update',
    'sop_update',
    'agent_instruction_update',
    'claude_instruction_update',
    'backlog_item',
    'deliverable_lifecycle_item',
    'rejected',
    'deferred',
    'no_action'
))
```

Notes on individual values:
- `team_learning` — observation applied as team-level behavioral change; Owner approved
- `agent_learning` — observation applied to specific agent's behavior; Owner approved
- `guideline_update` — escalated; resulted in GL update via SOP-019
- `sop_update` — escalated; resulted in SOP update via SOP-019
- `agent_instruction_update` — escalated; resulted in AGENT.md update
- `claude_instruction_update` — escalated; resulted in CLAUDE.md update
- `backlog_item` — escalated; deferred as backlog item for future governance cycle
- `deliverable_lifecycle_item` — escalated; routed to Deliverable Lifecycle system
- `rejected` — Owner rejected; discarded
- `deferred` — Owner deferred; re-surface at a defined future date
- `no_action` — Owner reviewed; no action warranted; closed

The `resolution TEXT` field (already in the current DDL) remains as a free-text explanation field. `processed_outcome` is the structured enum; `resolution` is the human-readable detail.

### 7.4 `closure_reason` assessment — not needed

V01 proposed a `closure_reason` field. With `processed_outcome` now covering all terminal outcomes including `rejected`, `deferred`, and `no_action`, a separate `closure_reason` field is redundant.

**Recommendation:** Do not add `closure_reason`. The `processed_outcome` enum plus the existing `resolution` free-text field is sufficient. The cleanest schema has one structured outcome field, not two.

### 7.5 `learning_scope` field — new, recommended

Captures the scope or type of the learning, independent of its routing outcome.

```sql
learning_scope TEXT CHECK(learning_scope IN (
    'team',
    'agent',
    'governance',
    'process',
    'session',
    'tooling',
    'owner_interaction'
))
```

Notes:
- `team` — observation affects team-wide behavior or cross-agent workflows
- `agent` — observation affects a specific agent's behavior (use with `target_agent`)
- `governance` — observation relates to governance procedures or gates
- `process` — observation relates to a specific workflow or SOP
- `session` — observation is session-specific and unlikely to repeat; flagging threshold is lower
- `tooling` — observation relates to a tool, integration, or technical system
- `owner_interaction` — observation relates to Owner communication patterns or preferences

This field enables filtering: show all agent-scoped LCs, all governance LCs, etc. It is orthogonal to `processed_outcome` — a learning can have `learning_scope = 'agent'` and `processed_outcome = 'sop_update'` if the agent-specific pattern warranted a structural rule.

### 7.6 `target_agent` field — new, optional

For agent-scoped learnings, the specific agent the learning applies to.

```sql
target_agent TEXT
```

Nullable. Only populated when `learning_scope = 'agent'`. Value is the agent slug (e.g., `iris`, `larry`, `nolan`).

This enables per-agent LC filtering: "show all open LCs targeting Iris."

### 7.7 `triage_routing` field — new, optional

Captures the routing classification determined at Triage. This is where "Graduation Candidate" lives in the new model.

```sql
triage_routing TEXT CHECK(triage_routing IN (
    'graduation_candidate',
    'standard',
    'urgent'
))
```

- `graduation_candidate` — Triage determined this LC qualifies for structural promotion; routes to escalation path
- `standard` — normal processing path
- `urgent` — requires processing in the same session as Triage (replaces GL-022's CAT-3 same-session rule)

### 7.8 Revised full column list direction

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER PK AUTOINCREMENT | Unchanged |
| `title` | TEXT NOT NULL | Unchanged |
| `description` | TEXT | Unchanged |
| `level` | INTEGER NOT NULL CHECK(level = 2) | Unchanged |
| `category` | TEXT | GL-020 CAT reference — unchanged |
| `flagged_by` | TEXT NOT NULL | Unchanged |
| `flagged_at` | TEXT NOT NULL DEFAULT datetime('now') | Unchanged |
| `session_id` | INTEGER REFERENCES session_logs(id) | Unchanged |
| `status` | TEXT NOT NULL DEFAULT 'captured' CHECK(...) | Changed: new values |
| `triaged_at` | TEXT | Renamed from `surfaced_at` |
| `triaged_session` | INTEGER REFERENCES session_logs(id) | Renamed from `surfaced_session` |
| `processed_at` | TEXT | New column |
| `processed_outcome` | TEXT CHECK(...) | New column |
| `learning_scope` | TEXT CHECK(...) | New column |
| `target_agent` | TEXT | New column — nullable |
| `triage_routing` | TEXT CHECK(...) | New column — nullable |
| `resolved_at` | TEXT | Unchanged — populated at `closed` |
| `resolution` | TEXT | Unchanged — free text |
| `owner` | TEXT NOT NULL DEFAULT 'larry' | Unchanged |
| `max_days_pending` | INTEGER NOT NULL DEFAULT 3 | Rename to `max_days_captured` for alignment |
| `created_at` | TEXT NOT NULL DEFAULT datetime('now') | Unchanged |

---

## 8. Updated Impact Table

Items marked **[v01]** were in v01 and are unchanged or confirmed. Items marked **[new]** are new in v02. Items marked **[corrected]** replace a v01 item.

### 8.1 GL-022

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 1 | Section 3 table | 5 status values: `pending`, `surfaced`, `approved`, `rejected`, `promoted` | Yes | Replace with 4: `captured`, `triaged`, `processed`, `closed`. Add `processed_outcome` and `triage_routing` rows to the model explanation. | High | Both | 1 |
| 2 | Section 3 transitions | `pending → surfaced → approved / rejected / promoted` | Yes | `captured → triaged → processed → closed` | High | Both | 1 |
| 3 | Section 3 integrity rules | "An LC cannot leave pending without being surfaced. An LC cannot leave surfaced without Owner decision." | Yes | Update to new state names and add transition guard for `processed → closed` | Medium | Behavioral | 1 |
| 4 | Section 6 decay prevention, item 2 | `pending` rows | Yes | `captured` rows | Low | Naming | 1 |
| 5 | Section 6 decay prevention, item 4 | "three valid endings: `approved`, `rejected`, `promoted`" | Yes | "two terminal states: `processed` and `closed`. Outcome in `processed_outcome`." | Medium | Both | 1 |
| 6 | Section 7 operational writes table | `UPDATE status → 'surfaced'` and `approved / rejected / promoted` | Yes | `UPDATE status → 'triaged'` and terminal via `processed_outcome` | High | Both | 1 |
| 7 | Section 5 surfacing rules | References `pending`, `surfaced`, `max_days_pending` | Yes | Rename to match new states: `captured`, `triaged`, `max_days_captured` | Medium | Naming | 1 |

### 8.2 Write-List v05 — W-1 DDL

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 8 | `status` CHECK constraint | `('pending','surfaced','approved','rejected','promoted')` | Yes | `('captured','triaged','processed','closed')` | High | Naming | 1 |
| 9 | `status` DEFAULT | `DEFAULT 'pending'` | Yes | `DEFAULT 'captured'` | Medium | Naming | 1 |
| 10 | `surfaced_at` column | `surfaced_at TEXT` | Yes | Rename to `triaged_at TEXT` | Low | Naming | 1 |
| 11 | `surfaced_session` column | `surfaced_session INTEGER` | Yes | Rename to `triaged_session INTEGER` | Low | Naming | 1 |
| 12 | `max_days_pending` column | `max_days_pending INTEGER NOT NULL DEFAULT 3` | Yes | Rename to `max_days_captured INTEGER NOT NULL DEFAULT 3` | Low | Naming | 1 |
| 13 | Missing columns | No `processed_outcome`, `processed_at`, `learning_scope`, `target_agent`, `triage_routing` | Yes | Add all five columns per Section 7 above | High | Behavioral | 1 |

### 8.3 /close-session — Step 1

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 14 | Step 1 SQL scan | `WHERE status = 'pending'` | Yes | `WHERE status = 'captured'` | High | Naming | 2 |
| 15 | Step 1 SQL scan | `AND ... >= max_days_pending` | Yes | `AND ... >= max_days_captured` | Medium | Naming | 2 |
| 16 [corrected] | Step 1 print output | `f"LC pending: {total}, LC overdue: {overdue}"` | Yes | `f"Learning Candidates captured: {total}, Learning Candidates overdue_for_triage: {overdue}"` | Low | Naming | 2 |

### 8.4 /close-session — Step 1b write plan

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 17 | Write plan row label | `LC status updates: [X overdue / none]` | Yes | `LC triage updates: [X overdue_for_triage / none]` | Low | Naming | 2 |
| 18 | Write plan row label | `Team learning: [yes / no]` | Low risk — see Section 4.1 | Deferred to Batch 3 pending Step 4 behavior design decision | Low | Naming | 3 |

### 8.5 /close-session — Step 3b LC sweep

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 19 | UPDATE SQL | `SET status = 'surfaced', surfaced_at = datetime('now')` | Yes | `SET status = 'triaged', triaged_at = datetime('now')` | High | Naming | 2 |
| 20 | WHERE clause | `WHERE status = 'pending'` | Yes | `WHERE status = 'captured'` | High | Naming | 2 |
| 21 | SELECT query | `WHERE status = 'surfaced' AND date(surfaced_at) = date('now')` | Yes | `WHERE status = 'triaged' AND date(triaged_at) = date('now')` | High | Naming | 2 |
| 22 [corrected] | Print output | `print(f"LC surfaced: {updated}")` | Yes | `print(f"Learning Candidates triaged: {updated}")` | Low | Naming | 2 |
| 23 | Owner decision instruction | "approve / reject / promote" | Yes | "apply / reject / escalate" | Medium | Behavioral | 2 |
| 24 | Authorization rule text | `"approve LC-{id}", "reject LC-{id}", "promote LC-{id}"` | Yes | `"apply LC-{id}", "reject LC-{id}", "escalate LC-{id}"` | Medium | Behavioral | 2 |
| 25 [corrected] | `resolve_lc` function keys | `'approve'`, `'reject'`, `'promote'` | Yes | `'apply'`, `'reject'`, `'escalate'` | Medium | Naming | 2 |
| 26 | `resolve_lc` status values | `'approved'`, `'rejected'`, `'promoted'` as status | Yes | `'processed'` for apply and escalate; `'closed'` for reject. Add `processed_outcome` SET in the same UPDATE. | High | Both | 2 |
| 27 | `resolve_lc` UPDATE SQL | Sets only `status`, `resolved_at`, `resolution` | Yes | Must also SET `processed_outcome` and `processed_at` for apply and escalate; for reject must SET `status = 'closed'` with `processed_outcome = 'rejected'` | High | Behavioral | 2 |

### 8.6 /close-session — Step 4

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 28 | Step 4 title | "Team learning (optional)" | Low — see Section 4.1 | Deferred to Batch 3. Rename scope depends on the dual-write design decision. | Low | Naming | 3 |

### 8.7 /close-session — Step 5

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 29 | Step 5 behavior | Scanning for "graduation candidates" as ad-hoc insights | Yes — partial | After absorption, this step should register qualifying insights as LCs with `triage_routing = 'graduation_candidate'` rather than handling them outside the LC lifecycle. Exact change deferred to Batch 3 after `agent_learnings` absorption design is confirmed. | Medium | Behavioral | 3 |

### 8.8 GL-021

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 30 | Section 7 descriptive text | "UPDATE status → 'surfaced'" | Yes | "UPDATE status → 'triaged'" | Low | Naming | 2 |
| 31 | Section 7 descriptive text | "UPDATE status → approved / rejected / promoted" | Yes | "UPDATE status → 'processed' or 'closed' with processed_outcome" | Low | Naming | 2 |

### 8.9 gl-index.md

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 32 | GL-022 entry description | "status states ... surfacing via /close-session" | Partial | "lifecycle states ... triage via /close-session" | Low | Naming | 1 |

### 8.10 Larry AGENT.md

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 33 | Kennisgraduatie block | `graduation_candidate` tag in `agent_learnings` | Yes — behavioral overlap | After `agent_learnings` absorption: replace Kennisgraduatie block with LC-based escalation. LCs with `triage_routing = 'graduation_candidate'` surface via Step 3b; Step 5 registers new observations as LCs. Exact rewording deferred to Batch 3. | Medium | Both | 3 |
| 34 | Database table pointer | `agent_learnings — Specialist self-improvement notes` | Yes — after absorption | Remove or redirect after Batch 3 execution | Low | Naming | 3 |
| 35 | AGENT.md boilerplate | "writes all operational records (session_logs, agent_learnings, team_log, ...)" | Yes — after absorption | Remove `agent_learnings` from list after Batch 3 | Low | Naming | 3 |

### 8.11 All specialist AGENT.md files (14+ files)

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 36 | Boilerplate write list | "writes all operational records (session_logs, agent_learnings, team_log, ...)" | Yes — after absorption | Remove `agent_learnings` from all 14+ specialist files after Batch 3. This is the broadest single change in the consolidation. | Medium | Naming | 3 |

### 8.12 CLAUDE.md

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 37 | Session log rule line 67 | "write one row to `agent_learnings` and one row to `delegation_outcomes`" | Yes — after absorption | Remove agent_learnings write; delegation notes stay in `delegation_outcomes` only | Medium | Behavioral | 3 |
| 38 | Language rule line 322 | `agent_learnings` in list of tables using English | Yes — after absorption | Remove from list after Batch 3 | Low | Naming | 3 |
| 39 | Teamgroei protocol line 526 | "Log naar `agent_learnings` in de domein-database" | Yes — after absorption | Replace with "Register as Learning Candidate in `learning_candidates`" | High | Behavioral | 3 |

### 8.13 SOP-009

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 40 | Step 5 | "flag it as a graduation candidate at /close-session" | Partial — see item 29 | After Batch 3: update to "register as LC with triage_routing = graduation_candidate" | Low | Naming | 3 |

### 8.14 No change required (confirmed)

| File | Reason |
|---|---|
| Iris AGENT.md LC Flag format | LC abbreviation correct; no lifecycle status values |
| Iris AGENT.md "No Auto-Learning" | Boundary term, not a lifecycle concept |
| GL-020 "Level 2 — Learning candidate" | Conceptual level label, not a status value |
| GL-020 CAT-3 rules | No lifecycle status values referenced |
| SOP-019 "Learning Candidate 4" footer | Historical annotation, not a status value |
| CLAUDE.md "team learnings" informal references | Informal English, not lifecycle terminology |
| All archived deliverables | Outside active system scope |
| `team_learnings` | Does not exist — no action |

---

## 9. Updated Batch Plan

The safest path is three batches, with Batch 3 deferred pending resolution of two technical-behavioral design questions.

### Batch 1 — Model definition

**Scope:** Define the authoritative model. All implementation files derive from this.

**Files:**
- GL-022 — complete rewrite of Section 3, Section 5, Section 6, Section 7 (items 1–7)
- Write-List W-1 DDL — status values, renamed columns, new columns (items 8–13)
- gl-index.md — description update for GL-022 entry (item 32)

**Nature:** Primarily naming with behavioral additions (new fields).
**Governance gate:** CAT-3 required. Changes to active GL.
**Dependency:** None — this is the foundation for Batch 2.
**Affected file count:** 3

### Batch 2 — Technical alignment

**Scope:** Align the operational implementation to the model defined in Batch 1.

**Files:**
- /close-session Step 1 (items 14–16)
- /close-session Step 1b (item 17)
- /close-session Step 3b (items 19–27)
- GL-021 Section 7 (items 30–31)

**Nature:** Naming and behavioral (processed_outcome SET logic in resolve_lc).
**Governance gate:** CAT-3 required. Changes to active /close-session skill and GL-021.
**Dependency:** Batch 1 must be complete — Batch 2 implements exactly the model defined there.
**Affected file count:** 3

### Batch 3 — Consolidation and behavioral cleanup (deferred)

**Deferred pending resolution of two technical-behavioral design questions:**

**Question A:** When `processed_outcome = 'team_learning'`, should the system also create a `team_log` row as a chronological reference, or is the `learning_candidates` record alone sufficient? This determines the scope of Step 4 changes (items 18, 28).

**Question B:** When `agent_learnings` behavioral rows are absorbed into `learning_candidates`, what happens to the delegation-note rows that are also in `agent_learnings`? Do they move to `delegation_outcomes` only, or does a delegation-note subset remain? This determines the scope of the CLAUDE.md and AGENT.md changes (items 33–40).

**Files in scope once design questions are answered:**
- CLAUDE.md (items 37–39)
- Larry AGENT.md (items 33–35)
- 14+ specialist AGENT.md files (item 36)
- /close-session Steps 4 and 5 (items 18, 28–29)
- SOP-009 (item 40)

**Nature:** Behavioral and naming. Broadest change set — touches every specialist AGENT.md.
**Governance gate:** CAT-3 required per file. The 14+ AGENT.md updates may warrant a dedicated batch proposal (bulk AGENT.md update) as a single governed execution.
**Affected file count:** 20+

---

## 10. Open Design Questions

Only questions that remain genuinely open after Owner clarification.

### Q1 — team_log dual-write (Batch 3 blocker A)

When an LC is processed with `processed_outcome = 'team_learning'`:

**Option A:** The `learning_candidates` record is the sole store. No `team_log` row is created. Step 4 of /close-session is redesigned to only INSERT `team_log` rows for operational events that are not LCs (e.g., team procedural changes, infrastructure events).

**Option B:** The `learning_candidates` record is the SSOT; a `team_log` row is also created as a lightweight chronological reference, linking back to the LC `id`. Step 4 writes both records.

**Option C:** Step 4 is deprecated. All team-level learnings go through the LC lifecycle. `team_log` becomes a read-only derived view or is phased out.

The answer determines how Step 4 is rewritten and whether `team_log` retains its write trigger.

### Q2 — agent_learnings delegation-note rows (Batch 3 blocker B)

`agent_learnings` currently serves two purposes: delegation notes (one per delegation) and behavioral learning notes. The behavioral rows absorb into `learning_candidates`. The question is whether delegation notes:

**Option A:** Move entirely to `delegation_outcomes`, which already exists for delegation history. `agent_learnings` is retired.

**Option B:** Remain in `agent_learnings` as a separate table, now narrowly scoped to delegation notes only. `agent_learnings` is kept but its name is misleading for this purpose. Rename to `delegation_notes`?

**Option C:** Are dropped entirely — `delegation_outcomes` already captures sufficient delegation context and the per-delegation note is redundant.

The answer determines whether `agent_learnings` survives in any form, and therefore the scope of the CLAUDE.md and AGENT.md updates.

---

## 11. Recommendation for Next Step After v02

V02 is the complete read-only assessment. No open conceptual model questions remain. Two technical-behavioral design questions remain (Q1 and Q2) and are the only blockers for Batch 3.

Recommended sequence:

1. **Owner reviews v02 and answers Q1 and Q2.** These are binary choices with no governance gate requirement for the decision itself — only for the implementation that follows.

2. **After Q1 and Q2 are answered:** Prepare the Batch 1 write-list. Batch 1 is fully specifiable now and does not depend on Q1 or Q2.

3. **Run Batch 1 through governance** (Iris review + Owner authorization per SOP-019 CP-1 through CP-4).

4. **After Batch 1 is complete:** Prepare and run Batch 2. Batch 2 is also fully specifiable now.

5. **After Q1 and Q2 are answered and Batches 1–2 are complete:** Prepare Batch 3 write-list. This will be the largest single governed execution (20+ files). Consider whether it should be split further by file type (e.g., AGENT.md updates as a dedicated sub-batch).

---

## 12. Change Count Summary

| Batch | Items | Files | Nature | Governance | Status |
|---|---|---|---|---|---|
| Batch 1 | 7 | 3 | Naming + Behavioral | CAT-3 | Ready to specify |
| Batch 2 | 9 | 3 | Naming + Behavioral | CAT-3 | Ready to specify (after Batch 1) |
| Batch 3 | 23+ | 20+ | Naming + Behavioral | CAT-3 per file | Deferred — Q1 and Q2 |
| No change | 14 | — | — | — | Confirmed |

**Total active conflicts: 39 items across 26 active files.**
**Open design questions: 2 (technical-behavioral only — no conceptual model questions remain).**

---

Delivered on: 2026-06-07
Delivered at: /opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment/lc-naming-alignment-impact-assessment-v02.md
