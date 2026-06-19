# B-021 Backlog Registration

**Date:** 2026-06-03
**Prepared by:** Larry
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2

---

## 1. Purpose

This document records the completion of B-021A and the registration of B-021B and B-021C as open backlog candidates. No files were modified. No scripts, backup folders, credentials or remote contents were touched. All entries are database-only (team_tasks in team-knowledge.db).

---

## 2. B-021A — Recorded as Complete

| Field | Value |
|---|---|
| team_tasks id | 57 |
| Title | B-021A: SOP-001 backup infrastructure documentation |
| Assignee | Kai |
| Status | completed |
| Completed at | 2026-06-03 |
| Execution report | `Deliverables/20260603_Core_AI Team Audit Report/B-021A-execution-report.md` |

---

## 3. B-021B — Registered as Open Backlog Candidate

| Field | Value |
|---|---|
| team_tasks id | 58 |
| Title | B-021B: Logging improvements investigation and proposal |
| Assignee | Kai |
| Status | open |
| Priority | 3 |

**Scope:**
1. Read-only investigation of `mypka-backup.log` empty state — identify exact cause, deliver short finding report.
2. Exact implementation proposal for bounded logging or logrotate for `mypka-sync.log`.

**Constraints:**
- No script changes without a separate dedicated proposal and Owner's explicit approval.
- Investigation only until cause is confirmed.

**Not approved for execution yet.** Requires its own proposal, review and Owner approval.

---

## 4. B-021C — Registered as Open Backlog Candidate

| Field | Value |
|---|---|
| team_tasks id | 59 |
| Title | B-021C: Secure credential recovery procedure for /opt/mypka-memory/.env |
| Assignee | Kai |
| Status | open |
| Priority | 2 |

**Scope:**
- Proposal for documenting manual recovery procedure of `/opt/mypka-memory/.env` in SOP-001.
- States what credentials are needed and where to source them in a DR scenario.

**Constraints:**
- No secret values may be printed or written in any deliverable.
- `/opt/mypka-memory/.env` must not be added to regular myPKA, rclone or Google Drive backups.
- A separate secure-secret backup proposal may follow B-021C if manual recovery is deemed insufficient — that is a further separate step.

**Not approved for execution yet.** Requires its own proposal, review and Owner approval.

---

## 5. Confirmation — No Files Modified

| Item | Status |
|---|---|
| SOP-001 | Not modified in this action (was modified in B-021A execution earlier today) |
| AGENT.md files | Not modified |
| Scripts | Not modified |
| Backup folders | Not modified |
| Credentials | Not modified |
| Crontab | Not modified |
| Google Drive remote | Not accessed |

Only database operations were performed: three INSERT rows into team_tasks in team-knowledge.db.

---

## 6. Open Backlog Summary

| ID | Title | Status | Priority |
|---|---|---|---|
| 57 | B-021A: SOP-001 backup infrastructure documentation | completed | — |
| 58 | B-021B: Logging improvements investigation and proposal | open | 3 |
| 59 | B-021C: Secure credential recovery procedure | open | 2 |

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-021-backlog-registration.md`*
