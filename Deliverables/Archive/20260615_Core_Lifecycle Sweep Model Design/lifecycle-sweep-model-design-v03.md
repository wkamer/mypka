# Lifecycle Sweep Model Design v03

**Document type:** Proposal — design artifact
**Status:** Active
**Session:** 2026-06-15
**Author:** Larry (Team Orchestrator)
**Supersedes:** v02 (`lifecycle-sweep-model-design-v02.md`)
**Predecessor:** v02 + OD-2 Owner decision 2026-06-15

---

## 1. Purpose and Scope

This document defines the target-quality sweep models for two interdependent lifecycles:

- **Learning Candidate Lifecycle** — signal, triage, and routing lifecycle
- **Deliverable Lifecycle** — artifact and execution lifecycle

Both lifecycles have a sweep step at /close-session. This document specifies what each sweep surfaces, how output is categorized, how items are prioritized, and how ambiguous states are handled.

**Scope:** sweep model design only. This document governs output categories, field mappings, ambiguity rules, and minimum acceptance criteria. It does not govern implementation details of sweep query code, and does not replace GL-022 (Learning Candidate Lifecycle) or any existing Deliverable Lifecycle governance rule.

**Context:** Two Owner decisions were made during the design session that inform this model:

- **Decision A (naming):** `learning_candidates` remains the canonical SSOT table name. `learning_candidate_lifecycle` is the target name for future model alignment. No rename, migration, schema change, or compatibility layer is authorized.
- **Decision B (object semantics):** `deliverable_lifecycle` canonically registers deliverable artifacts, not folders. `artifact_name` identifies the artifact or document. The folder is storage location and context. Existing folder-like rows are baseline/legacy and must not be corrected.

---

## 2. Learning Candidate Lifecycle Sweep Model

The Learning Candidate Lifecycle is the signal, triage, and routing lifecycle. A Learning Candidate (LC) exists when a team member encounters an observation during execution that meets the Level 2 criterion per GL-022 Section 2. Every LC is registered in `learning_candidates` in `team-knowledge.db`.

### 2.1 Output Categories

Five categories, ordered by priority:

| Priority | Category | Short definition |
|---|---|---|
| 1 | **Urgent** | Marked urgent, not yet closed |
| 2 | **Graduation Candidate** | Routed to graduation, not yet closed |
| 3 | **Overdue for Triage** | Captured, days >= max_days_captured |
| 4 | **Stalled at Triaged** | Triaged but not processed within threshold |
| 5 | **Pending** | Captured, days < max_days_captured (informational) |

### 2.2 Field Mapping

| Category | `status` | `triage_routing` | `processed_at` | `flagged_at` / `max_days_captured` | `resolved_at` |
|---|---|---|---|---|---|
| Urgent | not `processed`/`closed` | `urgent` | irrelevant | irrelevant | NULL |
| Graduation Candidate | not `processed`/`closed` | `graduation_candidate` | irrelevant | irrelevant | NULL |
| Overdue for Triage | `captured` | irrelevant | irrelevant | days >= max_days_captured | irrelevant |
| Stalled at Triaged | `triaged` | irrelevant | NULL | triaged_at >= 7 calendar days AND processed_at IS NULL | NULL |
| Pending | `captured` | irrelevant | irrelevant | days < max_days_captured | irrelevant |

### 2.3 Known Values

| Field | Confirmed values |
|---|---|
| `status` | `captured`, `triaged`, `processed`, `closed` |
| `triage_routing` | `graduation_candidate`, `standard`, `urgent` |
| `processed_outcome` | `team_learning`, `agent_learning`, `guideline_update`, `sop_update`, `agent_instruction_update`, `claude_instruction_update`, `backlog_item`, `deliverable_lifecycle_item`, `rejected`, `deferred`, `no_action` |
| `level` | always `2` |
| `max_days_captured` | default `3`, adjustable per row |

### 2.4 Requires Verification

| Question | Risk if assumed |
|---|---|
| Is `triage_routing` set at flagging or only at triage? | If only at triage: a `captured` item never has `triage_routing` — Urgent and Graduation Candidate categories cannot be detected pre-triage |
| Are `resolved_at` and `resolution` in active use? | May cause duplicate or missing items in sweep |
| What do the 7 existing rows contain? | No design assumption about live data confirmed |
| GL-020 CAT-1 through CAT-6 definitions | Unknown whether category type affects sweep priority |

### 2.5 Owner-Facing Output Format

```
Learning Candidate Lifecycle Sweep — [date]
[X] items

URGENT:
| # | LC-ID | Title | Flagged by | Flagged on | Status |

GRADUATION CANDIDATE:
| # | LC-ID | Title | Flagged by | Flagged on | Status |

OVERDUE FOR TRIAGE (action required this session):
| # | LC-ID | Title | Flagged by | Flagged on | Days |

STALLED AT TRIAGED:
| # | LC-ID | Title | Triaged on | Days waiting |

PENDING (informational):
| # | LC-ID | Title | Flagged on | Days |

[CONFLICT — requires verification]: (shown as empty when none)
[NOT CLASSIFIABLE]: (shown as empty when none)

Per Urgent / Graduation Candidate / Overdue item: reply with row number + decision (triage / defer / reject).
```

---

## 3. Deliverable Lifecycle Sweep Model

The Deliverable Lifecycle is the artifact and execution lifecycle. A deliverable artifact that passes GL-017 G1 is registered in `deliverable_lifecycle` in `team-knowledge.db`.

### 3.1 Output Categories

Five top-level categories. Overdue and Within-threshold are urgency attributes displayed inline per item, not top-level categories.

| Priority | Category | Short definition |
|---|---|---|
| 1 | **Open Execution** | Owner confirmed, processing not completed |
| 2 | **Carry-Forward** | Acknowledged, intentionally not actioned — no formal Owner decision |
| 3 | **Deferred** | Owner explicitly said later |
| 4 | **Excluded** | Explicitly scoped out by Owner decision |
| 5 | **Not-blocker** | Informational — does not block any work, no action required |

**Urgency attributes** (applied per item within any category):
- `[OVERDUE]` — item in `ready` state for >= 7 days without resolution
- `[WITHIN THRESHOLD]` — item in `ready` state for < 7 days

### 3.2 Field Mapping

| Category | `state` | `owner_decision` | `processed_at` | Notes |
|---|---|---|---|---|
| Open Execution | `ready` | `confirmed` | NULL | Processing confirmed but outcome not recorded |
| Carry-Forward | `active` or `ready` | IS NULL | NULL | OD-2 resolved: NULL = no formal Owner decision |
| Deferred | `ready` | `deferred` | irrelevant | Owner explicitly deferred |
| Excluded | `ready` or `active` | `rejected` or explicit exclusion marker | irrelevant | Requires verification — see 3.4 |
| Not-blocker | `active` | NULL | irrelevant | Informational; does not require Owner action |

### 3.3 Known Values

| Field | Confirmed values |
|---|---|
| `state` | `active`, `ready`, `archived`, `closed` |
| `owner_decision` | NULL, `confirmed`, `deferred`, `rejected` |
| `artifact_type` | `proposal`, `execution_report`, `status_report`, `closure_report`, `audit_report`, `decision_record`, `triage_document`, `research_brief`, `domain_knowledge_update`, `working_artifact` |
| `processed_at` | NULL or timestamp |

### 3.4 Requires Verification

| Question | Risk if assumed |
|---|---|
| Is `accepted_done` a `state` value or only a `state_gl017` value? | Closed items may appear in sweep if incorrectly filtered |
| Is there a `processing` state between `ready` and `processed`? | Open Execution may miss items already in processing |
| Does `carry_forward` exist as a structured `owner_decision` value? | Carry-Forward cannot be auto-classified without this |
| Does an `excluded` or not-blocker marker exist as a structured value? | Excluded and Not-blocker cannot be auto-classified |
| Can `state` and `state_gl017` be inconsistent on the same row? | Sweep cannot determine correct category without a precedence rule |
| What are all `state_gl017` values in the live DB? | Only inferred from session logs — not confirmed |

### 3.5 Owner-Facing Output Format

```
Deliverable Lifecycle Sweep — [date]
[X] items

OPEN EXECUTION (confirmed — awaiting processing completion):
| # | ID | Artifact | Type | Confirmed on | [OVERDUE] |

CARRY-FORWARD (on radar — no formal decision):
| # | ID | Artifact | Type | Days open | Note |

DEFERRED (Owner said later):
| # | ID | Artifact | Type | Days open | Deferred on |

EXCLUDED (out of scope by Owner decision):
| # | ID | Artifact | Type | Excluded on |

NOT-BLOCKER (informational):
| # | ID | Artifact | Type | Days open |

[STATE CONFLICT — requires verification]: (shown as empty when none)
[NOT CLASSIFIABLE]: (shown as empty when none)

Per Open Execution / Carry-Forward / Deferred item: reply with row number + decision (confirm / defer / reject / correct).
```

---

## 4. Shared Lifecycle Sweep Principles

These principles apply to both the LC sweep and the DL sweep.

**P-1 — No silent hiding:** Every item in scope for the sweep is shown. An item that does not fit any defined category is placed in a `[NOT CLASSIFIABLE]` section. It is never silently excluded.

**P-2 — Empty categories are shown:** Every category is present in the output, even when empty. An empty category displays `— no items —`.

**P-3 — Conflict sections are always present:** Every sweep output includes a conflict section shown as empty when no conflicts exist.

**P-4 — Write authorization per item:** The sweep output is a proposal. No state changes are made until the Owner responds. Each Owner response is a separate authorization.

**P-5 — Priority ordering within output:** Higher-priority categories appear first. Within a category, items are ordered by days open descending.

**P-6 — Urgency attributes are inline labels:** `[OVERDUE]` and `[WITHIN THRESHOLD]` are displayed inline per item. They do not move items between categories.

---

## 5. Handoff Rule: When a Learning Candidate Creates a Deliverable

**Principle:** The Learning Candidate Lifecycle decides whether a learning requires a deliverable. The Deliverable Lifecycle governs the resulting artifact only if one is created. The two lifecycles are independent. Their handoff must be explicit and auditable.

**When a Deliverable is created:**
A Learning Candidate creates a Deliverable when `processed_outcome` is one of:
`guideline_update`, `sop_update`, `agent_instruction_update`, `claude_instruction_update`, or a `backlog_item` or `deliverable_lifecycle_item` that results in a reviewable artifact.

**When no Deliverable is created:**
LCs with `processed_outcome` of `team_learning`, `agent_learning`, `no_action`, `rejected`, `deferred`, or `backlog_item` where no artifact is produced do not generate a `deliverable_lifecycle` row.

**Traceability:**
The connection between an LC and its resulting Deliverable artifact is traceable through:
- `source_reference` in `deliverable_lifecycle` — contains the LC id or session reference
- `processed_outcome` in `learning_candidates` — identifies the type of artifact produced
- `processing_notes` in `deliverable_lifecycle` (optional) — may contain additional context

**Rule:** No `deliverable_lifecycle` row is inserted for an LC outcome until the artifact exists as a persisted file. File first, registration after verification.

---

## 6. Ambiguity and Conflict Rules

### LC Sweep

| Situation | Rule |
|---|---|
| `status = 'captured'` AND `triage_routing = 'urgent'` | Urgent wins over Overdue for Triage. `triage_routing` overrides age threshold |
| `status = 'captured'` AND `triage_routing = 'graduation_candidate'` | Graduation Candidate wins over Overdue for Triage |
| Both Urgent and Graduation Candidate on same row | Impossible per GL-022 (single value per field). If present: `[CONFLICT]` section |
| `status = 'triaged'` AND `triage_routing IS NULL` | Stalled at Triaged on status alone. `triage_routing` not required for classification |
| `resolved_at` filled but `status` not `closed` | `[CONFLICT — status/resolved_at mismatch]` section |

### DL Sweep

| Situation | Rule |
|---|---|
| `owner_decision = 'confirmed'` AND `processed_at IS NULL` | Always Open Execution. Takes priority over age classification |
| `owner_decision = 'deferred'` AND days >= 7 | Always Deferred. `[OVERDUE]` attribute applied as inline label. Not reclassified to a different category |
| `state` and `state_gl017` conflict on same row | `[STATE CONFLICT]` section. No category assignment until resolved |
| Unknown `owner_decision` value not in known enum | `[NOT CLASSIFIABLE]` section. No category assignment |
| Item fits Carry-Forward AND another category | Any structured `owner_decision` value takes precedence over Carry-Forward |

### Shared

| Situation | Rule |
|---|---|
| Item fits no defined category | `[NOT CLASSIFIABLE]` section. Never silently excluded |
| Sweep query produces a database error for one item | Skip that item, add to `[SWEEP ERROR]` section, continue sweep. Do not halt entire sweep for a single item error |

---

## 7. Minimum Acceptance Criteria

### LC Sweep

| Code | Criterion |
|---|---|
| MAC-LC-1 | All five categories present in output, even when empty |
| MAC-LC-2 | Items with `triage_routing = 'urgent'` always appear in Urgent, regardless of age |
| MAC-LC-3 | Overdue for Triage contains no items with `triage_routing = 'urgent'` or `'graduation_candidate'` |
| MAC-LC-4 | Stalled at Triaged contains items with `status = 'triaged'` AND `processed_at IS NULL` AND `triaged_at` >= 7 calendar days ago. Shown as active. Items ordered by triaged_at ascending. |
| MAC-LC-5 | Items with `status = 'processed'` or `'closed'` do not appear in any category |
| MAC-LC-6 | `[CONFLICT]` section present in every sweep output, shown as empty when no conflicts |

### DL Sweep

| Code | Criterion |
|---|---|
| MAC-DL-1 | All five categories present in output, even when empty |
| MAC-DL-2 | Carry-Forward contains items with `owner_decision IS NULL` AND `state IN ('active', 'ready')`. Shown as active. Items ordered by registered_at ascending. |
| MAC-DL-3 | Open Execution contains only items with `owner_decision = 'confirmed'` AND `processed_at IS NULL` |
| MAC-DL-4 | Items with `state` in `('archived', 'closed')` do not appear in any category |
| MAC-DL-5 | `state` / `state_gl017` conflicts appear in `[STATE CONFLICT]` section, not in any category |
| MAC-DL-6 | `[NOT CLASSIFIABLE]` section present in every sweep output |

---

## 8. Open Owner Decisions

| Code | Decision | Blocks |
|---|---|---|
| OD-3 | **State conflict precedence (DL sweep):** Which field governs when `state` and `state_gl017` disagree on the same row? Without a precedence rule, 13 rows (ids 10, 11, 13, 14, 16, 36, 40, 41, 42, 55, 56, 57, 59) cannot be auto-classified. | STATE CONFLICT resolution; auto-classification of `archived_cleanup_no_active_need` and `accepted_done` rows |

**Resolved Owner Decisions:**

| Code | Decision | Resolution |
|---|---|---|
| OD-1 | Stalled-at-Triaged threshold (LC sweep) | 7 calendar days. Owner confirmed 2026-06-15. |
| OD-2 | Carry-Forward structure (DL sweep) | `owner_decision IS NULL` AND `state IN ('active', 'ready')`. No new value, no schema change. Owner confirmed 2026-06-15. |
| Decision A | LC table naming | `learning_candidates` remains canonical SSOT. Target name `learning_candidate_lifecycle` for future alignment. No rename or migration authorized. |
| Decision B | DL object semantics | `deliverable_lifecycle` registers artifacts, not folders. `artifact_name` identifies the artifact or document. Folder = storage location. Existing folder-like rows = baseline/legacy, not corrected. |

---

*Delivered on: 2026-06-15*
*Delivered at: Deliverables/20260615_Core_Lifecycle Sweep Model Design/lifecycle-sweep-model-design-v03.md*
