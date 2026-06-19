# LC Owner Decision Packet v02

**Date:** 2026-06-07
**Author:** Larry
**Version:** v02
**Supersedes:** `lc-owner-decision-packet-v01.md`
**Status:** Awaiting Owner decision
**Scope:** Decision preparation only — no writes executed

Learning Candidates in scope: id=5, id=6, id=7
All three: `status=triaged`, `triage_routing=standard`, `processed_outcome=NULL`

**Changes vs v01:**
- LC-6 recommendation corrected: changed from `apply (agent_learning)` to `escalate (graduation_candidate → CLAUDE.md)`. Reason: the v01 recommendation implied CLAUDE.md update as an automatic side effect of apply, which is audit-unsafe for a system behavior change. CLAUDE.md updates require a separate persisted write-plan and explicit Owner authorization.
- "No immediate system-file writes" statement added.
- Decision table and confirmation question updated.

---

## No immediate system-file writes

This decision packet authorizes nothing. It is decision preparation only.

Confirming the recommended decision does not:
- modify CLAUDE.md
- modify any GL, SOP, or AGENT.md
- modify `/close-session` or any skill file
- insert, update, or delete any database row

Every authorized action following Owner confirmation requires a separate write-plan, explicit Owner authorization, and a post-check before execution.

---

## LC id=5 — Verification script fragility in governance post-checks

| Field | Value |
|---|---|
| id | 5 |
| status | triaged |
| triage_routing | standard |
| learning_scope | governance |
| source_domain | core |

**Problem summary**

Post-check scripts in governance write-plans carry two recurring fragility patterns:

1. **Broad status queries.** Scripts use `WHERE status = 'triaged'` instead of targeting the specific rows the write-plan intended. Any other triaged row contaminates the result set, making the check non-deterministic.
2. **Wrong column index in print statements.** Scripts reference `r[7]` twice instead of `r[6]` and `r[7]`, silently misreporting one field while still returning PASS.

Both errors were present in `lc-triage-write-plan.md` (v01) and went undetected until the v02 correction round. Neither produced a visible script error — they produced subtly wrong output while reporting PASS.

**Recommended Owner decision: escalate LC-5**

**Reasoning:** This is a recurring pattern risk, not a one-off script bug. It affects every governance post-check script written by any agent. A team_learning entry in `agent_learnings` is insufficient because agents authoring new post-check scripts do not consult that table at writing time. The standard must live in a GL document that is referenced at authoring time. The governed destination is GL-005 (AI Engineering Operating System, which covers script standards) or a new GL for post-check script quality, to be determined during the SOP-019 track.

LC-5 and LC-7 share the same root domain (post-check script quality). They should be processed in a single SOP-019 track to produce one coherent GL section rather than two fragmented amendments.

**Expected governed destination:** GL-005 or new GL — post-check script standards

**What escalation authorizes (and only this):**
```
UPDATE learning_candidates
SET triage_routing = 'graduation_candidate'
WHERE id = 5
-- status stays 'triaged'
-- SOP-019 governance track opened for GL amendment
```

---

## LC id=6 — Batch-stop rules declared in write-lists are not automatically inherited by the executing agent brief

| Field | Value |
|---|---|
| id | 6 |
| status | triaged |
| triage_routing | standard |
| learning_scope | governance |
| source_domain | core |

**Problem summary**

Batch-stop rules are documented inside write-list documents (e.g. "stop if Candidate A already exists"). When Larry briefs an executor, the brief summarizes the task — it does not automatically include these rules. If the executor does not independently read the full write-list, batch-stop rules are absent from their execution context and will not be enforced.

During LC Batch 2, this was a live risk: stop conditions existed only in the write-list, not in the brief presented to the executing agent.

The fix requires a behavioral rule in Larry's operational document: "when briefing an executor against a write-plan, explicitly list all batch-stop rules in the brief."

**Recommended Owner decision: escalate LC-6 (Option A)**

**Reasoning:** A CLAUDE.md update is a system behavior change. Recommending `apply (agent_learning)` while implying CLAUDE.md update as a side effect — as v01 did — is audit-unsafe. The CLAUDE.md update requires its own write-plan, reviewable artifact, and explicit Owner authorization. Escalating LC-6 as a graduation_candidate keeps the full LC lifecycle in one governed track and ensures the CLAUDE.md rule addition goes through SOP-019 before execution. This is the appropriate governance path for any change to Larry's Hard Rules.

The destination is bounded and specific: one rule addition in CLAUDE.md under the Hard Rules / Delegatie section (execution briefing standard). No GL or SOP involvement.

**Expected governed destination:** CLAUDE.md — Larry execution briefing rule under Hard Rules

**What escalation authorizes (and only this):**
```
UPDATE learning_candidates
SET triage_routing = 'graduation_candidate'
WHERE id = 6
-- status stays 'triaged'
-- SOP-019 governance track opened for CLAUDE.md amendment
```

CLAUDE.md is not modified as part of this decision. It is modified only after the SOP-019 track produces an approved write-plan and the Owner confirms that write explicitly.

---

## LC id=7 — Post-check regex assumes branch order in `resolve_lc`, causing potential silent false negatives

| Field | Value |
|---|---|
| id | 7 |
| status | triaged |
| triage_routing | standard |
| learning_scope | tooling |
| source_domain | core |

**Problem summary**

The post-check script for `resolve_lc` used a regex that assumed the reject branch precedes the escalate branch in the function body:

```python
re.search(r"elif decision == 'reject':(.*?)elif decision == 'escalate'")
```

If the branch order differs in the written file, the reject branch check silently returns no match and reports a false negative — the post-check returns PASS even though the reject path is malformed or absent.

Root cause: post-check scripts that verify code structure by regex are fragile when they rely on surrounding structural context rather than extracting the target function text first and then applying pattern checks against it.

**Recommended Owner decision: escalate LC-7 (same track as LC-5)**

**Reasoning:** Same class of problem as LC-5: a post-check script quality pattern that recurs unless encoded in a GL standard. The governed destination is the same (GL-005 or new GL for post-check script standards). Processing LC-5 and LC-7 together in one SOP-019 track produces one coherent GL section covering both fragility patterns — broad query scope and branch-order assumptions. Two separate SOP-019 tracks for the same domain would be wasteful and would produce a fragmented standard.

**Expected governed destination:** GL-005 or new GL — same destination as LC-5, same SOP-019 track

**What escalation authorizes (and only this):**
```
UPDATE learning_candidates
SET triage_routing = 'graduation_candidate'
WHERE id = 7
-- status stays 'triaged'
-- SOP-019 governance track for LC-5 and LC-7 merged into one GL amendment run
```

---

## Recommended decision table

| id | title (short) | Recommended decision | Governed destination |
|---|---|---|---|
| 5 | Verification script fragility | escalate (graduation_candidate) | GL-005 or new GL — post-check standards |
| 6 | Batch-stop rules not in brief | escalate (graduation_candidate) | CLAUDE.md — Larry execution briefing rule |
| 7 | Post-check regex assumes branch order | escalate (graduation_candidate) | same GL as LC-5, same SOP-019 track |

**Recommended Owner decision: escalate LC-5, escalate LC-6, escalate LC-7**

LC-5 and LC-7 share one SOP-019 track (GL amendment). LC-6 is a separate SOP-019 track (CLAUDE.md amendment). No immediate system-file writes in either case.

---

## Confirmation question

Bevestig je onderstaande beslissing, of geef per LC een afwijkend antwoord:

> **escalate LC-5, escalate LC-6, escalate LC-7**

Antwoord met bevestiging of met afwijking per nummer (bijv. "bevestigd" of "LC-6: apply, rest bevestigd").

---

## Report file preservation

| File | Status |
|---|---|
| `lc-owner-decision-packet-v01.md` | Present — not overwritten |
| `lc-owner-decision-packet-v02.md` | Present — active version |

---

Delivered on: 2026-06-07
Delivered at: `Deliverables/20260607_Core_LC Triage Write-Plan/lc-owner-decision-packet-v02.md`
