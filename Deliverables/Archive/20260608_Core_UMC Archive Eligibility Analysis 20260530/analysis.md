# Archive Eligibility Analysis
## Deliverable: 20260530_Core_UMC diagnose en aanbevelingen

**Prepared by:** Larry, Team Orchestrator  
**Date:** 2026-06-08  
**Scope:** Read-only investigation. No archive actions taken. No files modified. No databases modified.

---

## 1. Subject

**Deliverable under review:** `Deliverables/20260530_Core_UMC diagnose en aanbevelingen/rapport.md`  
**Author:** Kai  
**Date of delivery:** 2026-05-30  
**Nature:** Diagnosis report of Unified Memory Core (UMC) behavioral gaps and structural recommendations.

The deliverable contains five recommendations (P1 through P5). Archive eligibility depends on whether each recommendation has been captured in the active knowledge architecture. A recommendation that exists only in this deliverable creates a knowledge gap upon archive.

---

## 2. Recommendations Extracted

| # | Label | Summary |
|---|---|---|
| P1 | Domain naming | Fix `ke`/`gr` shortforms in `close_routine_verification.py`; map to canonical `kamer-ecommerce` and `geldstroom-regie`; backfill 2 rows in `memory_summaries`. |
| P2 | AGENT.md write_summary | Replace "specialist calls Python at session close" with delegation model: specialists write handoff notes; close-session script handles UMC summary per domain. |
| P3 | SessionStart hook | Add hook that calls `get_summary_pointers(limit=3)` at session start to inject prior UMC context automatically. |
| P4 | source_type attribution | Extend `close_routine_verification.py` with `--agents` argument; write per-specialist `agent_learnings` rows and structured tags on the composite summary. |
| P5 | Periodic validation cron | Weekly cron to count UMC entries per domain per week; alert to Discord or Team Inbox when any domain goes silent for 7+ days. |

---

## 3. Recommendation-by-Recommendation Analysis

### P1 — Fix domain naming inconsistency

**Specification level:**  
GL-015 Section 3 defines the canonical UMC domain tags: `personal`, `team`, `kamer-ecommerce`, `geldstroom-regie`, `core`. These are authoritative and match the long-form names recommended in P1.  
GL-015 Section 5.3 explicitly registers the 2 existing `gr` rows in `memory_summaries` as historical data under the Non-Remediation Principle (Section 5.1). No retroactive fix required; forward writes must use the canonical names.

**Code level:**  
`close_routine_verification.py` does not exist (confirmed: NOT FOUND). Whether the domain normalization was implemented in the script before removal, moved to another file, or is currently absent could not be confirmed from a read-only scan. The close-session skill and close-end-of-day skill contain no visible domain mapping logic.

**Captured?** Specification: yes (GL-015). Code enforcement: unconfirmed.

---

### P2 — Replace write_summary instruction in AGENT.md

**Structural change:**  
Confirmed: neither Kai's AGENT.md nor Sasha's AGENT.md contains a `## UMC` section. This is consistent with the old "specialist calls Python at session close" instruction having been removed from all 14 AGENT.md files.

**Delegation model:**  
The replacement described in P2 (specialists write handoff notes to session context; close-session reads them and writes one composite summary per domain) is **not documented in any GL, SOP, or skill file** found during this investigation. The CLAUDE.md still contains `mm.write_summary()` as a session-close instruction for Larry/close routines, but the specialist-facing delegation model has no formal specification.

**Risk:** The knowledge of WHAT should replace the old instruction exists only in this deliverable. A new specialist onboarded or a new AGENT.md author has no canonical reference for how UMC writes should now work.

**Captured?** Structural change: yes. Replacement model: no — only in this deliverable.

---

### P3 — SessionStart hook for get_summary_pointers

**Fully implemented:**  
`/opt/myPKA/.claude/settings.json` contains a `SessionStart` hook that calls `umc_session_start.sh`. The script executes `mm.get_summary_pointers(limit=3)` and prints the result to session context. This matches the recommendation exactly.

**Captured?** Yes — implemented in active infrastructure (settings.json + script).

---

### P4 — source_type attribution to specialist summaries

**Specification level:**  
GL-015 Section 3 contains a full table mapping every agent to a canonical `domain=` and `source_type=` value. This codifies the attribution model described in P4.

**Code level:**  
The `--agents` argument extension to `close_routine_verification.py` described in P4 cannot be verified: the script does not exist. No close-routine skill file shows per-agent summary writing logic. Whether the code that writes summaries applies the per-agent source_types from GL-015 is unconfirmed.

**Captured?** Specification: yes (GL-015 §3). Code implementation: unconfirmed.

---

### P5 — Periodic validation cron

**Infrastructure:**  
Crontab contains only backup jobs (SQLite, n8n-postgres, memory-db pg_dump). No UMC monitoring or validation job is present.

**Scripts:**  
`check_schemas.py` exists in `Team Knowledge/Core/Scripts/` but addresses schema validation, not UMC activity monitoring. No script matching the P5 requirement (count entries per domain per week, alert on silence) was found.

**GL/SOP documentation:**  
No GL or SOP references UMC activity monitoring, silence thresholds, or periodic validation.

**Captured?** No — not implemented, not documented anywhere in the active knowledge architecture.

---

## 4. Summary Table

| # | Recommendation | Specification captured | Code confirmed | Unique to this deliverable |
|---|---|---|---|---|
| P1 | Domain naming | Yes — GL-015 §3 + §5.3 | No | No |
| P2 | AGENT.md delegation model | No | No (structural removal confirmed) | **Yes** |
| P3 | SessionStart hook | Yes | Yes — settings.json + script | No |
| P4 | source_type attribution | Yes — GL-015 §3 | No | No |
| P5 | Periodic validation cron | **No** | **No** | **Yes** |

---

## 5. Verdict

**Not safe to archive.**

Two recommendations exist only in this deliverable:

- **P2** (delegation model): The AGENT.md UMC sections were removed, but the replacement model is nowhere formally specified. Any future specialist onboarding or AGENT.md revision has no reference for how UMC writes should now work.
- **P5** (periodic validation): The recommendation, its rationale, and the threshold design (7-day silence window, Discord/Team Inbox alert) exist exclusively in this file.

---

## 6. Required Knowledge Captures

### Capture 1 — P2 Delegation Model

**What must be captured:** The replacement for the "specialist calls write_summary at session close" instruction. Specifically: (a) specialists write handoff notes to session context when finishing a substantive task; (b) the close-session routine reads handoff notes and writes one composite UMC summary per active domain, with the correct source_type from GL-015 §3.

**Destination:** GL-013 (Memory Core Architecture), as a new section "Specialist UMC Write Protocol." GL-013 is the authoritative document for UMC architecture decisions and operational model.

**Owner required:** Kai (implementation) + Nolan (GL-013 update). Larry routes.

---

### Capture 2 — P5 Periodic Validation

**What must be captured:** The requirement for a weekly UMC activity check: count entries per domain per week, compare to expected minimum based on session activity, alert if any domain goes silent for 7+ days.

**Destination (two actions):**  
1. Register as an open `team_tasks` row assigned to Kai with source `delegation`, tag `umc-monitoring`.  
2. Add a "Future Enhancement" subsection to GL-013 documenting the requirement, the threshold (7 days), and the alert target (Discord or Team Inbox). This prevents the requirement from being lost if the team_tasks row is closed without implementation.

**Owner required:** Confirmation to delegate to Kai.

---

## 7. Recommended Next Action

Present this analysis to the Owner. Once the Owner confirms:

1. Route Capture 1 to Kai (implementation) and Nolan (GL-013 update).
2. Route Capture 2 to Kai (team_tasks row) and Nolan (GL-013 Future Enhancement entry).
3. After both captures are confirmed written, re-evaluate archive eligibility. At that point the deliverable will be redundant and safe to archive.

---

Delivered on: 2026-06-08  
Delivered at: (session)
