# Learning Candidate Registration Proposal v01

**Document type:** Read-only registration proposal — pending Iris review and Owner authorization
**Date:** 2026-06-07
**Author:** Larry (Team Orchestrator)
**Status:** Pending Iris review
**Triage reference:** `learning-candidate-flag-triage-proposal-v02.md` — Owner confirmed: yes
**Related task:** team_tasks id 73 (remains open until registration and surfacing are complete)

---

## Context

The Owner confirmed the triage classification (2026-06-07):

- Register this as a Learning Candidate (Level 2).
- Surface it in the same session because it is CAT-3.
- Keep team_tasks id 73 open until registration and surfacing are complete.
- Promotion to SOP-019 is the recommended likely next decision after surfacing — not approved yet.

This proposal defines the exact write action required. It requires Iris review and then separate Owner authorization before execution.

---

## Proposed Write Action

**Target:** `Team Knowledge/team-knowledge.db` — table `learning_candidates`
**Operation:** INSERT one row
**Pre-condition:** Table already exists. Zero existing rows.

### Field values

| Field | Value |
|---|---|
| `title` | Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace |
| `description` | During Deliverable Lifecycle Phase 1 implementation on 2026-06-07, all five governance checkpoints (CP-1 through CP-4 and the Iris pre-implementation check) were not invoked. Individual write steps received interactive Owner authorization throughout. The retroactive Iris review confirmed the implementation was correct, but the formal governance protocol was not followed. Iris issued this flag (CAT-3) in the retroactive Governance Gatekeeper review. The gap: no documented procedure defines CP invocation behavior in Owner-directed interactive flows. This observation cannot be applied autonomously — Owner input on governance intent is required. |
| `level` | 2 |
| `category` | CAT-3 |
| `flagged_by` | iris |
| `flagged_at` | 2026-06-07 |
| `status` | surfaced |
| `surfaced_at` | datetime('now') at execution time |
| `owner` | larry |
| `max_days_pending` | 3 |
| `session_id` | NULL (session log not yet written at time of registration) |

**Rationale for status = surfaced at INSERT:**
CAT-3 rule (GL-022 Section 5): surface in the same session as flagging, no delay. Owner confirmed triage classification in this session. The surfacing act is the triage confirmation and presentation of this registration proposal. Inserting directly as `surfaced` reflects this without requiring a separate pending → surfaced update cycle.

### Exact SQL

```sql
INSERT INTO learning_candidates (
    title,
    description,
    level,
    category,
    flagged_by,
    flagged_at,
    status,
    surfaced_at,
    owner,
    max_days_pending
) VALUES (
    'Governance checkpoints bypassed when Owner drives implementation interactively — CP invocation required even under Owner-directed pace',
    'During Deliverable Lifecycle Phase 1 implementation on 2026-06-07, all five governance checkpoints (CP-1 through CP-4 and the Iris pre-implementation check) were not invoked. Individual write steps received interactive Owner authorization throughout. The retroactive Iris review confirmed the implementation was correct, but the formal governance protocol was not followed. Iris issued this flag (CAT-3) in the retroactive Governance Gatekeeper review. The gap: no documented procedure defines CP invocation behavior in Owner-directed interactive flows. This observation cannot be applied autonomously — Owner input on governance intent is required.',
    2,
    'CAT-3',
    'iris',
    '2026-06-07',
    'surfaced',
    datetime('now'),
    'larry',
    3
);
```

---

## What This Write Does Not Do

- Does not close team_tasks id 73 (closed only after registration and surfacing are confirmed complete).
- Does not create SOP-019.
- Does not modify any AGENT.md files.
- Does not modify CLAUDE.md or any Guidelines.
- Does not approve promotion to SOP-019.

---

## Governance References

- GL-022 Section 3 — status states and transitions
- GL-022 Section 4 — Iris flags with title + category only; Larry reconstructs description from review context
- GL-022 Section 5 — CAT-3 surfacing rule: same session as flagging, no delay
- GL-021 Section 5 Rule 3 — mandatory CAT-3 sequence: Larry prepares, Iris reviews, Owner confirms, execute

---

## Next Steps After Iris Review

1. Larry presents Iris-reviewed proposal to Owner.
2. Owner confirms with yes / no / correction.
3. Larry executes the INSERT.
4. Larry presents the surfaced Learning Candidate to Owner (surfacing step).
5. Owner decides: approve / reject / promote (separate decision, not part of this confirmation).
6. team_tasks id 73 closed after registration and surfacing are confirmed complete.

---

*Delivered on: 2026-06-07*
*Delivered by: Larry — Team Orchestrator*
