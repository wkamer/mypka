# LC Naming Alignment Impact Assessment

**Date:** 2026-06-07
**Author:** Larry
**Status:** Read-only assessment — no files modified, no databases updated
**Scope:** Learning Candidate Lifecycle simplification and naming alignment
**Goal model:** `Captured → Triaged → Processed → Closed`

---

## 1. Purpose and Scope

This assessment identifies every location in the active system where existing terminology, status values, variable names, SQL strings, document sections, or behavioral instructions conflict with the Owner's simplified Learning Candidate (LC) lifecycle model:

**Captured → Triaged → Processed → Closed**

Additional Owner decisions in scope:
- LC = Learning Candidate (confirmed abbreviation)
- GL = Guideline (confirmed abbreviation — KE prefix reserved for Key Element files)
- Graduation Candidate = classification or routing qualification during Triage or Process, not a separate lifecycle
- Team Learning = possible `processed_outcome` value, not a lifecycle state
- Process / Processed = formal wording
- Landing = not the formal lifecycle term (preemptive correction)

This is a read-only document. No changes have been made. All findings are inputs for one or more future implementation proposals.

---

## 2. System State at Time of Assessment

### 2.1 Database state

The `learning_candidates` table does **not exist** in `team-knowledge.db`. The entire Phase 1 write batch (W-1 through W-5) has not been executed. This is the single most important finding: there are no rows to migrate, no data at risk. All proposed changes are pre-implementation corrections.

`team-knowledge.db`, `personal.db`, `kamer-ecommerce.db`, and `geldstroom-regie.db` all exist as files. Their table schemas were empty or not populated for the LC-related tables at assessment time.

### 2.2 Live files using current LC terminology

The following files are active and use current (pre-simplification) LC terminology:

| File | Role | Status at assessment |
|---|---|---|
| `Team Knowledge/Core/Guidelines/GL-022_Learning Candidate Lifecycle.md` | Authoritative lifecycle definition | Active, live |
| `.claude/commands/close-session.md` | Session closure skill | Active, live |
| `Deliverables/20260606_Core_LC Lifecycle Phase 1 Write-List v05/lc-lifecycle-phase1-write-list-v05.md` | Phase 1 implementation batch | Deliverable, not yet executed |
| `Team/Iris - The Governance Gatekeeper/AGENT.md` | Iris behavior | Active, live |
| `Team/Larry - The Orchestrator/AGENT.md` | Larry behavior | Active, live |
| `Team Knowledge/Core/Guidelines/GL-021_Owner Interaction Rule and Write Authorization Boundary.md` | Write authorization rules | Active, live |
| `Team Knowledge/Core/Guidelines/GL-020_Intent Classification Taxonomy.md` | Intent classification | Active, live |
| `Team Knowledge/Core/Guidelines/gl-index.md` | Guidelines index | Active, live |
| `Team Knowledge/Core/SOPs/SOP-009_Write journal entry after task.md` | Journal SOP | Active, live |
| `Team Knowledge/Core/SOPs/SOP-019_Governance Gatekeeper Procedure.md` | Governance gate SOP | Active, live |
| `CLAUDE.md` | Larry primary instructions | Active, live |

---

## 3. Model Comparison: Current vs Owner Goal

### 3.1 Current status model (GL-022 Section 3)

```
pending → surfaced → approved
                   → rejected
                   → promoted
```

Five values: `pending`, `surfaced`, `approved`, `rejected`, `promoted`

The current model embeds outcome (what happened to the LC) directly in the status field. `approved`, `rejected`, and `promoted` are three terminal statuses with distinct semantics.

### 3.2 Owner goal model

```
Captured → Triaged → Processed → Closed
```

Four values. Outcomes are captured separately (a `processed_outcome` field), not embedded in the status.

### 3.3 Conceptual mapping

| Current status | New status | Notes |
|---|---|---|
| `pending` | `captured` | Semantically equivalent: LC registered, awaiting review |
| `surfaced` | `triaged` | Partial shift: current "surfaced" means presented to Owner and awaiting decision; new "triaged" means categorized and routing determined. The Owner-review moment is now implicit within the Triaged state, not a separate status gate |
| `approved` | → `processed` + `processed_outcome = 'behavior_applied'` | Outcome separated from state |
| `rejected` | → `closed` + `closure_reason = 'rejected'` | Or: `processed` + `processed_outcome = 'rejected'`, then → `closed` |
| `promoted` | → `processed` + `processed_outcome = 'graduation_candidate'` | Graduation Candidate becomes a routing classification within Process, not a status |

### 3.4 New fields implied by the Owner model

The new model requires one or two additional fields that do not currently exist in the proposed DDL:
- `processed_outcome TEXT` — captures what was decided at the Process stage (e.g., `team_learning`, `graduation_candidate`)
- Optionally: `closure_reason TEXT` — captures why an LC was closed (e.g., `rejected`, `superseded`, `completed`)

These are not in the current Write-List v05 DDL. The DDL must be updated before implementation.

---

## 4. Impact Table

For each affected location:
- **Conflict** = yes/no
- **Type** = Naming / Behavioral / Both
- **Risk** = Low / Medium / High
- **Batch** = which implementation batch this correction belongs to

### 4.1 GL-022 — Learning Candidate Lifecycle

This is the authoritative document. All other files derive from it.

| # | Location within GL-022 | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 1 | Section 3 — title | "Lifecycle: Status States and Transitions" | Yes | Rename to "Lifecycle States and Transitions" — remove "Status" since states now have semantic meaning beyond DB status values | Low | Naming | 1 |
| 2 | Section 3 — status table | 5 values: `pending`, `surfaced`, `approved`, `rejected`, `promoted` | Yes | Replace with 4 values: `captured`, `triaged`, `processed`, `closed`. Add note on `processed_outcome` field | High | Both | 1 |
| 3 | Section 3 — transitions | "pending → surfaced → approved / rejected / promoted" | Yes | Replace with "captured → triaged → processed → closed" | High | Both | 1 |
| 4 | Section 3 — no-silent-expiry rule | "An LC cannot leave pending without being surfaced. An LC cannot leave surfaced without Owner decision." | Yes | Update to match new states: "An LC cannot leave captured without being triaged. An LC cannot leave triaged without being processed or closed." | Medium | Behavioral | 1 |
| 5 | Section 6 — decay prevention, item 2 | "Larry queries all `pending` rows. Rows where `days_pending >= max_days_pending`" | Yes | Replace `pending` with `captured` | Medium | Naming | 1 |
| 6 | Section 6 — decay prevention, item 4 | "exactly three valid endings — `approved`, `rejected`, `promoted`" | Yes | Replace with: "exactly two terminal states — `processed` and `closed`. Outcome recorded in `processed_outcome`." | Medium | Both | 1 |
| 7 | Section 7 — operational writes table | "UPDATE status → 'surfaced'" and "UPDATE status → approved / rejected / promoted" | Yes | Replace with new status values: `triaged`, `processed`, `closed` | High | Both | 1 |

### 4.2 Write-List v05 — W-1 DDL

This deliverable defines the `CREATE TABLE` statement that will be executed. The table does not yet exist.

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 8 | W-1 DDL — `status` CHECK constraint | `CHECK(status IN ('pending','surfaced','approved','rejected','promoted'))` | Yes | Replace values with `('captured','triaged','processed','closed')` | High | Naming | 1 |
| 9 | W-1 DDL — `status` DEFAULT | `DEFAULT 'pending'` | Yes | Change to `DEFAULT 'captured'` | Medium | Naming | 1 |
| 10 | W-1 DDL — `surfaced_at` column name | `surfaced_at TEXT` | Yes — partial | Rename to `triaged_at TEXT` for alignment. `surfaced_session` → `triaged_session`. | Low | Naming | 1 |
| 11 | W-1 DDL — missing fields | No `processed_outcome` field in DDL | Yes | Add `processed_outcome TEXT` column and optionally `closure_reason TEXT` | High | Behavioral | 1 |
| 12 | W-1 DDL — pre-check output string | `print('ABORTED: learning_candidates already exists ...')` | No | No conflict — output string, not a status value | — | — | — |

### 4.3 /close-session — Step 1 LC scan

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 13 | Step 1 — SQL scan for overdue LCs | `WHERE status = 'pending'` | Yes | Replace with `WHERE status = 'captured'` | High | Naming | 2 |
| 14 | Step 1 — print output | `f"LC pending: {total}, LC overdue: {overdue}"` | No — output label only | No change required. "pending" in print string is English prose, not a DB status value. | — | — | — |

### 4.4 /close-session — Step 1b write plan table

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 15 | Step 1b — write plan row | `Team learning: [yes / no]` | Potential confusion | This row refers to Step 4 (`team_log` row), not to an LC `processed_outcome`. The term "team learning" in this row is about a different mechanism. See Section 5.1 for full analysis. Low priority. | Low | Naming | 3 |

### 4.5 /close-session — Step 3b LC sweep

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 16 | Step 3b — UPDATE SQL | `SET status = 'surfaced', surfaced_at = datetime('now')` | Yes | Replace with `SET status = 'triaged', triaged_at = datetime('now')` | High | Naming | 2 |
| 17 | Step 3b — WHERE clause | `WHERE status = 'pending'` | Yes | Replace with `WHERE status = 'captured'` | High | Naming | 2 |
| 18 | Step 3b — SELECT query | `WHERE status = 'surfaced' AND date(surfaced_at) = date('now')` | Yes | Replace with `WHERE status = 'triaged' AND date(triaged_at) = date('now')` | High | Naming | 2 |
| 19 | Step 3b — print output | `print(f"LC surfaced: {updated}")` | Yes — misleading label | Replace with `print(f"LC triaged: {updated}")` | Low | Naming | 2 |
| 20 | Step 3b — Owner decision instruction | "wait for the Owner's decision: approve / reject / promote" | Yes | Replace with "wait for the Owner's decision: apply / reject / promote-to-sop" and align with new state model | Medium | Behavioral | 2 |
| 21 | Step 3b — authorization rule text | `"approve LC-{id}", "reject LC-{id}", "promote LC-{id}"` | Yes | Update decision verbs to align with new model | Medium | Behavioral | 2 |
| 22 | Step 3b — `resolve_lc` function keys | `'approve'`, `'reject'`, `'promote'` | Yes | Rename keys. `'approve'` → `'apply'`, `'reject'` → `'reject'` (unchanged), `'promote'` → `'escalate'` | Medium | Naming | 2 |
| 23 | Step 3b — `resolve_lc` resolution strings | `'approved'`, `'rejected'`, `'promoted'` as status values | Yes | Replace with `processed` / `closed` as status; move outcome to `processed_outcome` field | High | Both | 2 |
| 24 | Step 3b — `resolve_lc` UPDATE SQL | `SET status=?, resolved_at=datetime('now'), resolution=?` | Partial | `resolved_at` remains valid. `resolution` field can remain. Status values change. `processed_outcome` field must be SET in the same UPDATE for apply/escalate cases. | Medium | Both | 2 |

### 4.6 /close-session — Step 4

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 25 | Step 4 — section title | "Team learning (optional)" | Potential confusion | See Section 5.1. This step is about `team_log`, not about LC `processed_outcome`. The label overlap is a clarity risk. Recommend renaming to "Team pattern log (optional)" or "Team-log entry (optional)" to eliminate the ambiguity. | Low | Naming | 3 |

### 4.7 /close-session — Step 5

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 26 | Step 5 — section title | "Graduation candidates" | Partial | "Graduation candidates" in Step 5 refers to the manual discovery of insights worth promoting to SOP/GL/WS — this is NOT an LC lifecycle operation. It is a separate scanning step. In the new model, this concept should be described as: insights that have reached the threshold for structural change. The step title can remain "Graduation candidates" but should clarify it is distinct from LC `processed_outcome = 'graduation_candidate'`. Or: rename to "Structural promotions" to eliminate overlap. | Low | Naming | 3 |

### 4.8 Larry AGENT.md — Kennisgraduatie section

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 27 | AGENT.md — Kennisgraduatie block | `graduation_candidate` tag in `agent_learnings.tags` | Yes — terminology overlap | This mechanism predates GL-022. It operates through `agent_learnings` tags, not through the LC lifecycle. In the new model, an `agent_learnings` row with this tag either (a) should be registered as an LC with `processed_outcome = 'graduation_candidate'` at Triage, or (b) remains a separate mechanism. Assessment: the Kennisgraduatie block and GL-022 serve overlapping purposes. This overlap should be resolved — either the Kennisgraduatie mechanism is absorbed into the LC lifecycle, or they are explicitly documented as separate tracks. Resolution requires Owner direction. | Medium | Both | 3 |

### 4.9 Iris AGENT.md

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 28 | AGENT.md — LC Flag section | `LC Flag: [one-sentence title] — [GL-020 category]` | No | LC abbreviation and format remain correct. No lifecycle status values referenced in Iris output. | — | — | — |
| 29 | AGENT.md — LC Flag description | "observation useful beyond the current session, not derivable from the responsible agent's current AGENT.md without session context" | No | Conceptual definition correct — no lifecycle terms. | — | — | — |
| 30 | AGENT.md — changelog entries | "LC-Iris-001", "LC-Iris-002", "LC-Iris-003" | No | Historical identifiers — not lifecycle states. No change needed. | — | — | — |
| 31 | AGENT.md — Never Does | "No Auto-Learning." | No | "Auto-Learning" is a boundary term (Iris never autonomously applies behavioral changes). Distinct from the LC lifecycle. No conflict. | — | — | — |

### 4.10 GL-021 — Write Authorization Boundary

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 32 | GL-021 — implementation tracker (line ~156) | `LC-Iris-001`, `LC-CloseSession-001` completion markers | No | Historical implementation tracking entries. Not lifecycle states. No change needed. | — | — | — |
| 33 | GL-021 Section 7 — pre-authorized writes | References "INSERT new LC row at flagging" and "UPDATE status → 'surfaced'" | Yes — indirect | The descriptive text "UPDATE status → 'surfaced'" will be incorrect after the rename. GL-021 should be updated to say "UPDATE status → 'triaged'" to remain accurate. Low-risk correction. | Low | Naming | 2 |

### 4.11 GL-020 — Intent Classification Taxonomy

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 34 | GL-020 Section 5 | "Level 2 — Learning candidate" | No | Conceptual level label, not a lifecycle status. "Learning candidate" here means the type of observation, not a status value. No conflict. | — | — | — |
| 35 | GL-020 Section 8 Risk 5 | "Level 2 Candidate Decay" | No | Risk name — no lifecycle status values referenced. No change needed. | — | — | — |
| 36 | GL-020 CAT-3 rules | No lifecycle status values referenced | No | No change needed. | — | — | — |

### 4.12 GL-022 gl-index.md entry

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 37 | gl-index.md line for GL-022 | "LC lifecycle: status states, ownership rule, surfacing via /close-session (Phase 1), decay prevention, pre-authorization scope for operational LC writes" | Partial | "status states" → "lifecycle states"; "surfacing" → "triage" or "surfacing/triage". Minor description update. | Low | Naming | 1 |

### 4.13 SOP-009 — Write Journal Entry After Task

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 38 | SOP-009 Step 5 | "flag it as a graduation candidate at /close-session" | No conflict in current form — no lifecycle state | This is informal language for "consider escalating this insight." It predates GL-022 and refers to the same concept as Larry AGENT.md Kennisgraduatie. Low risk. No immediate action. See item 27 resolution. | Low | — | 3 |

### 4.14 SOP-019 — Governance Gatekeeper Procedure

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 39 | SOP-019 footer | "Learning Candidate 4" in last modified note | No | This is a historical note: LC 4 is the 4th Learning Candidate that was flagged, and the amendment is its processed outcome. Not a lifecycle state value. No change. | — | — | — |

### 4.15 CLAUDE.md

| # | Location | Current wording | Conflict | Recommended correction | Risk | Type | Batch |
|---|---|---|---|---|---|---|---|
| 40 | CLAUDE.md pointer table | "Team Knowledge/ — Session logs, SOPs, team learnings, domain knowledge" | No | "team learnings" here is informal English for "things the team has learned." Not a lifecycle term. No conflict. | — | — | — |
| 41 | CLAUDE.md Session-Log Author | "Cross-links earlier logs, captures decisions and team learnings" | No | Same as above — informal. No change needed. | — | — | — |

---

## 5. Special Topics

### 5.1 "Team Learning" ambiguity — two separate mechanisms

The term "Team Learning" currently appears in two distinct contexts:

**Context A — /close-session Step 4**
An optional `team_log` INSERT in `team-knowledge.db` when a new pattern or insight affects the whole team. This is a manual step, separate from the LC system.

**Context B — Owner's new LC model**
"Team Learning" as a `processed_outcome` value on an LC row. This captures what happened when an LC was Processed.

These are two different mechanisms that share the term. They are not in direct conflict today (Step 4 does not write to `learning_candidates`), but they create cognitive ambiguity as the LC system grows. Specifically:
- If an LC is processed with `processed_outcome = 'team_learning'`, should a `team_log` row also be written? Or does the LC record replace the need for a `team_log` row?
- If yes: the behavior of Step 4 becomes partially redundant with an LC at `processed_outcome = 'team_learning'`.
- If no: the two mechanisms remain parallel but the naming is confusing.

**Assessment:** This is a behavioral design question, not just a naming question. It requires Owner decision before either Step 4 or the LC `processed_outcome` field can be fully aligned. No change recommended until the Owner has clarified the relationship.

**Risk if left unresolved:** Low in the short term (the LC table doesn't exist yet). Medium in the medium term (once operational, both mechanisms can produce overlapping records).

### 5.2 "Graduation Candidate" in two separate contexts

**Context A — GL-022 current `promoted` status**
An LC escalated to Level 3 triggers SOP-019. In the new model, this would be `processed_outcome = 'graduation_candidate'` at the Process stage.

**Context B — Larry AGENT.md Kennisgraduatie**
The `graduation_candidate` tag in `agent_learnings.tags` triggers a surface-at-session-close behavior in Step 5 of /close-session. This predates GL-022.

These overlap semantically but operate through different mechanisms. In the new LC model, the Kennisgraduatie mechanism (Context B) and the LC `graduation_candidate` outcome (Context A) are both pointing at the same concept: "this insight should become a structural rule."

**Assessment:** The Kennisgraduatie block in Larry AGENT.md should either be:
- Absorbed into the LC lifecycle (agent_learnings rows with `graduation_candidate` tag → automatically registered as LCs at triage with routing = graduation_candidate)
- Or explicitly preserved as a parallel track with a distinct label to avoid confusion

This is a behavioral design question. Owner decision required. Batch 3 candidate.

### 5.3 "Landing" term

Not found in any live system file. Found only in archived deliverables (historical planning documents). No action needed.

### 5.4 "Auto-Learning" term

Found only in Iris AGENT.md "Never Does" list and archived deliverables. The meaning is a hard behavioral boundary for Iris: she does not autonomously apply behavioral changes to the system. This is a constraint on Iris, not a lifecycle concept. No conflict with the simplified LC model. No change needed.

---

## 6. Files Not Requiring Changes

| File | Reason |
|---|---|
| Iris AGENT.md — LC Flag format | Uses LC abbreviation correctly; no lifecycle status values |
| GL-020 — intent classification taxonomy | "Level 2 — Learning candidate" is a conceptual label, not a status value |
| SOP-019 — governance gatekeeper | "Learning Candidate 4" in footer is a historical annotation |
| CLAUDE.md — team learnings references | Informal English, not lifecycle terminology |
| Larry AGENT.md — team learnings pointer | Informal label in team pointers table |
| All AGENT.md changelog LC-* entries | Historical change log identifiers, not lifecycle states |
| Archived deliverables | Outside the active system; no updates needed or warranted |

---

## 7. Proposed Implementation Path

The safest path is two batches, sequenced by dependency.

### Batch 1 — Model definition (governance level)

**Files:**
- GL-022 (complete Section 3, 6, 7 rewrite)
- Write-List W-1 DDL (status CHECK, DEFAULT, column renames, new `processed_outcome` field)
- gl-index.md (description update for GL-022 entry)

**Why first:** GL-022 is the source of truth. All technical files (close-session, DDL) should derive from an updated definition. Aligning GL-022 first removes ambiguity from the Batch 2 write plan.

**Nature:** Primarily naming (status values), with one behavioral addition (`processed_outcome` field).
**Governance gate:** Required — CAT-3 changes to active GL and DDL.

### Batch 2 — Technical alignment

**Files:**
- /close-session Step 1 scan SQL (status = 'captured')
- /close-session Step 3b SQL (triaged_at, status = 'triaged', resolve function)
- /close-session Step 3b Python (decision verbs, processed_outcome SET)
- GL-021 Section 7 descriptive text (status update reference)

**Why second:** These are technical implementations of the model defined in Batch 1. They should align to the new GL-022 definition precisely.

**Nature:** Primarily naming with one behavioral change (processed_outcome writing in resolve_lc).
**Governance gate:** Required — changes to active /close-session skill and GL-021.

### Batch 3 — Terminology clarification (lower priority)

**Files:**
- /close-session Step 4 title (Team learning → clarified label, pending Owner decision on ambiguity)
- /close-session Step 5 title (Graduation candidates → possibly Structural promotions)
- Larry AGENT.md Kennisgraduatie block (pending Owner decision on absorption vs. parallel track)
- SOP-009 Step 5 informal language

**Why third / why deferred:** These require Owner decisions on behavioral design questions, not just naming alignment. Cannot be fully specified until Section 5.1 and 5.2 above are resolved.

**Nature:** Both naming and behavioral.
**Governance gate:** Required per item — scope TBD after Owner decisions.

---

## 8. Effect on Deliverable Lifecycle Refinement

The LC simplification establishes a reusable design pattern for this system. Before the Deliverable Lifecycle is refined, these observations apply:

**Pattern established by the new LC model:**
1. Four-state linear lifecycle: Captured → Triaged → Processed → Closed
2. Outcome captured in a separate field, not embedded in status
3. Status encodes WHERE the item is in its lifecycle; outcome encodes WHAT happened

**If the Deliverable Lifecycle follows the same pattern:**
- The Deliverable Lifecycle `state` field should follow the same structural convention
- Outcome (what was decided: archived, superseded, published, carried forward) would go in a separate `processed_outcome` or `closure_reason` field
- The `deliverable_lifecycle` table currently uses `state = 'ready'` and `owner_decision` as a field — this suggests a similar pattern is already partially present

**Key risk to avoid:**
Do not design the Deliverable Lifecycle in isolation. If the LC model establishes `Captured → Triaged → Processed → Closed` as a team convention, the Deliverable Lifecycle should adopt compatible state names or explicitly diverge with documented rationale. Parallel systems with different state naming conventions increase cognitive load.

**Recommended sequence:**
Complete Batch 1 of this LC alignment first. Once the Owner's LC state model is locked in GL-022, use it as the naming template for Deliverable Lifecycle state design — or decide explicitly at that point whether the two lifecycles should share a naming convention.

---

## 9. Summary of Change Counts

| Batch | Files affected | Changes | Nature | Governance required |
|---|---|---|---|---|
| Batch 1 | GL-022, Write-List W-1 DDL, gl-index.md | 10 | Naming + Behavioral (new field) | Yes — CAT-3 |
| Batch 2 | /close-session (Steps 1, 3b), GL-021 | 9 | Naming + Behavioral | Yes — CAT-3 |
| Batch 3 | /close-session (Steps 4, 5), Larry AGENT.md, SOP-009 | 4+ TBD | Naming + Behavioral | Yes — pending Owner design decisions |
| No change needed | 10+ files | — | — | — |

**Total active conflicts identified:** 39 items across 8 active files.
**Archived-only references:** Not counted — no action required.
**Owner decisions required before Batch 3 can be specified:** 2 (Team Learning ambiguity; Graduation Candidate dual-context resolution).

---

Delivered on: 2026-06-07
Delivered at: /opt/myPKA/Deliverables/20260607_Core_LC Naming Alignment Impact Assessment/lc-naming-alignment-impact-assessment.md
