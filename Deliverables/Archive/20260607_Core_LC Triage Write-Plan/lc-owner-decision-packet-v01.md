# LC Owner Decision Packet v01

**Date:** 2026-06-07
**Author:** Larry
**Status:** Awaiting Owner decision
**Scope:** Decision preparation only — no writes executed

Learning Candidates in scope: id=5, id=6, id=7
All three: `status=triaged`, `triage_routing=standard`, `processed_outcome=NULL`

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

Post-check scripts in governance write-plans have been written with two recurring fragility patterns:
- Queries use broad status filters (`WHERE status = 'triaged'`) instead of targeting the specific rows the write-plan intended. Any other row in that status contaminates the result set, making the check non-deterministic.
- Print statements reference wrong column indices (e.g. `r[7]` printed twice instead of `r[6]` and `r[7]`), which silently misreports scope without causing a script error.

Both errors were present in `lc-triage-write-plan.md` (v01) and were only caught during the v02 correction round. Neither error produced a visible failure — they produced subtly wrong or misleadingly broad output while reporting PASS.

**Recommended Owner decision: escalate LC-5**

**Reasoning:** This is not a one-off script bug. It is a recurring pattern risk that affects every governance post-check script written by any agent. A team_learning log entry is insufficient because agents writing new post-check scripts will not consult agent_learnings at authoring time. The standard needs to live in a GL document that is referenced when post-check scripts are written. The governed destination is either GL-005 (AI Engineering Operating System, which covers script quality) or a new GL dedicated to post-check script standards. Either way, SOP-019 governs the amendment.

**Expected governed destination:** GL-005 or new GL (post-check script standards)

**Expected next artifact if escalated:** SOP-019 governance track initiated; Pax research brief on post-check script best practices; Nolan drafts GL amendment; Owner approves GL write

**Follow-up action authorized by escalation:**
```
triage_routing = 'graduation_candidate' (UPDATE only — status stays 'triaged')
SOP-019 track opened for GL-005 amendment or new GL
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

Batch-stop rules are documented inside the write-list document (e.g. "stop if Candidate A already exists"). When Larry briefs an executor, the brief does not automatically include these rules — it summarizes the task. If the executor does not read the full write-list independently, batch-stop rules are absent from their execution context. During LC Batch 2, this was a live risk: the write-list contained stop conditions that existed only in the write-list document, not in the brief presented to the executing agent.

**Recommended Owner decision: apply LC-6 (agent_learning)**

**Reasoning:** This is a bounded, specific rule that applies to Larry only: "when briefing an executor against a write-plan, explicitly include all batch-stop rules in the brief — do not rely on the executor deriving them from the write-list." The fix is a single behavioral rule added to CLAUDE.md under the Hard Rules section (Delegatie section or new Execution Briefing subsection). Full SOP-019 governance is disproportionate for one agent behavioral rule. The apply path logs the learning and produces the CLAUDE.md update in the same action.

**Expected governed destination:** CLAUDE.md (Larry — Hard Rules / Delegatie section)

**Expected next artifact if applied:** `agent_learnings` row inserted, CLAUDE.md updated with explicit briefing rule

**Follow-up action authorized by apply:**
```
status = 'processed', processed_outcome = 'agent_learning'
CLAUDE.md updated: batch-stop rules must be explicitly listed in every execution brief
```

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

The post-check script for `resolve_lc` used `re.search(r"elif decision == 'reject':(.*?)elif decision == 'escalate'")` to verify the reject branch. This pattern assumes that the reject branch precedes the escalate branch in the function body. If the branch order differs in the actual written file, the regex silently returns no match and the reject branch check reports a false negative — the post-check reports PASS even though the reject path is malformed or absent.

The root cause: post-check scripts that verify code structure by regex are fragile unless they explicitly extract the target function text before applying pattern checks, rather than relying on surrounding structural context.

**Recommended Owner decision: escalate LC-7 (process together with LC-5)**

**Reasoning:** This is the same class of problem as LC-5: a post-check script quality pattern that will recur unless it is encoded in a GL standard. The governed destination is the same (GL-005 or new GL for post-check script standards). Escalating both LC-5 and LC-7 together means one SOP-019 track addresses both patterns in a single GL amendment rather than two separate governance runs. Processing them separately would produce two partial GL additions that should have been one coherent section.

**Expected governed destination:** GL-005 or new GL — same destination as LC-5, same SOP-019 track

**Expected next artifact if escalated:** Combined with LC-5 in one SOP-019 governance track; GL amendment addresses both fragility patterns in one section

**Follow-up action authorized by escalation:**
```
triage_routing = 'graduation_candidate' (UPDATE only — status stays 'triaged')
SOP-019 track for LC-5 and LC-7 merged into one GL amendment run
```

---

## Recommended decision table

| id | title (short) | Recommended decision | Destination |
|---|---|---|---|
| 5 | Verification script fragility | escalate | GL-005 or new GL (post-check standards) |
| 6 | Batch-stop rules not in brief | apply (agent_learning) | CLAUDE.md (Larry) |
| 7 | Post-check regex assumes branch order | escalate | same GL as LC-5, same track |

**Recommended Owner decision: escalate LC-5, apply LC-6, escalate LC-7**

LC-5 and LC-7 share the same root domain (post-check script quality) and should be processed in a single SOP-019 track to avoid fragmented GL amendments. LC-6 is a bounded Larry behavioral rule and does not require SOP-019.

---

## Confirmation question

Bevestig je onderstaande beslissing, of geef per LC een afwijkend antwoord:

> **escalate LC-5, apply LC-6, escalate LC-7**

Antwoord met bevestiging of met afwijking per nummer (bijv. "bevestigd" of "LC-5: apply, LC-6: apply, LC-7: reject").

---

Delivered on: 2026-06-07
Delivered at: `Deliverables/20260607_Core_LC Triage Write-Plan/lc-owner-decision-packet-v01.md`
