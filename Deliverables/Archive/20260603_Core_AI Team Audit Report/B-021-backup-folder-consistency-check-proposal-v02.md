# B-021 Backup Folder Consistency Check Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Supersedes:** B-021 v0.1 (2026-06-03)

---

## Change Log (v0.1 → v0.2)

| # | Correction applied |
|---|---|
| 1 | Recommendations split into three execution-safe phases: B-021A (SOP-001 docs), B-021B (logging), B-021C (credential recovery) |
| 2 | C-001 and C-004 merged into one SOP-001 update covering all backup documentation in a single pass |
| 3 | n8n recommendation made conservative: document both mechanisms, no decommissioning of pre-existing script |
| 4 | `.env` recommendation tightened: treat as sensitive credential, manual recovery only, no regular backup, no secret values in deliverable |
| 5 | Logging recommendations tightened: `mypka-backup.log` classified as needing focused investigation; `mypka-sync.log` requires separate implementation proposal before execution |
| 6 | Google Drive remote validation disclaimer added: remote was not validated in this pass |
| 7 | Final recommendation adjusted: local structure appears consistent but not fully validated; DR documentation and credential recovery need follow-up |

---

## 1. Purpose

This proposal checks whether the backup folder structure on the myPKA Raspberry Pi is consistent, complete and aligned with the backup scripts introduced in B-001 (Stabilization Package v1). The goal is to identify gaps, redundancies, unclear conventions or unmaintained locations before they become a recovery risk.

v0.2 revises the original proposal to split recommendations into execution-safe phases, merge overlapping SOP-001 changes, apply a conservative stance on the pre-existing n8n backup, tighten the `.env` handling recommendation, clarify logging investigation scope, and explicitly state that Google Drive remote validation was not performed.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| Backup and disaster recovery procedures must be documented | SOP-001 Disaster Recovery |
| All backup-related scripts are placed under `Team Knowledge/Core/Integrations/<name>/` or `Team Knowledge/Core/Scripts/` | Larry AGENT.md conventions, GL-004 Canonical Paths |
| Database schema changes and critical infrastructure changes require Owner approval | GL-014 v1.2 §1 |
| Owner = Walter Kamer | GL-014 v1.2 Owner definition |
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |

---

## 3. Scope

**Inspected:**
- `/home/admin/backups/` — all subdirectories and contents
- Crontab — all scheduled backup entries
- Backup scripts in `Team Knowledge/Core/Scripts/` and `Team Knowledge/Core/Integrations/`
- `local-backup.sh` at `/home/admin/.config/rclone/`
- SOP-001 Disaster Recovery — for expected backup references
- rclone filter at `/home/admin/.config/rclone/myPKA-filter.txt`

**Excluded:**
- Google Drive backup contents (remote, not locally inspectable in this pass) — **see §6 for disclaimer**
- Content validation of backup files (restore testing — separate task)
- Integration log files (conflict logs, dropbox logs — out of scope)
- Language rule compliance of backup scripts (separate concern)

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `ls -lh` on all subdirectories under `/home/admin/backups/`
- `crontab -l` filtered for backup-related entries
- `find` to locate all scripts containing "backup" or "sync" in `Team Knowledge/Core/`
- `grep -n` on backup scripts for RETAIN_DAYS values
- `cat` on `local-backup.sh` and `myPKA-filter.txt`
- `grep -n` on SOP-001 for backup-related references

No files were modified, created, moved or deleted.

---

## 5. Expected Backup Structure

Based on B-001 (Stabilization Package v1) execution and the backup scripts found, the expected backup structure is:

```
/home/admin/backups/
├── myPKA/
│   └── YYYYMMDD/          ← daily rsync snapshot of /opt/myPKA/ (30-day retention)
├── sqlite/
│   └── YYYYMMDD/          ← daily SQLite backup of 4 databases (7-day retention)
│       ├── personal.db
│       ├── team-knowledge.db
│       ├── kamer-ecommerce.db
│       └── geldstroom-regie.db
├── n8n/
│   └── YYYYMMDD_n8n-postgres.sql  ← daily pg_dump of n8n-postgres (7-day retention)
├── memory-db/
│   └── YYYYMMDD_memory-db.dump    ← daily pg_dump of memory-db/pgvector (7-day retention)
├── mypka-backup.log               ← log from local-backup.sh (myPKA rsync)
└── mypka-sync.log                 ← log from rclone sync.sh (Google Drive sync)
```

**Backup schedule:**
| Time | Script | Target |
|---|---|---|
| `0 2 * * *` | `local-backup.sh` | `/home/admin/backups/myPKA/YYYYMMDD/` |
| `30 2 * * *` | `backup_sqlite_dbs.sh` | `/home/admin/backups/sqlite/YYYYMMDD/` |
| `45 2 * * *` | `backup_n8n.sh` | `/home/admin/backups/n8n/` |
| `0 3 * * *` | `backup_memory_db.sh` | `/home/admin/backups/memory-db/` |
| `*/5 * * * *` | `sync.sh` | `gdrive:myPKA` (Google Drive, one-way) |

---

## 6. Actual Backup Structure

```
/home/admin/backups/
├── memory-db/
│   └── 20260603_memory-db.dump    (4.9M, Jun 3 08:43) — 1 file
├── myPKA/
│   ├── 20260518/ … 20260603/      — 17 date folders (May 18 – Jun 3)
│   └── (30-day retention active)
├── mypka-backup.log               (0 bytes — empty)
├── mypka-sync.log                 (2.0M — rclone sync log, unbounded)
├── n8n/
│   └── 20260603_n8n-postgres.sql  (34M, Jun 3 08:44) — 1 file
└── sqlite/
    └── 20260603/                  — 1 date folder
        ├── personal.db            (188K)
        ├── team-knowledge.db      (196K)
        ├── kamer-ecommerce.db     (60K)
        └── geldstroom-regie.db    (48K)
```

**Crontab (confirmed active):**
- `0 2 * * *` → `local-backup.sh` ✓
- `30 2 * * *` → `backup_sqlite_dbs.sh` ✓
- `45 2 * * *` → `backup_n8n.sh` ✓
- `0 3 * * *` → `backup_memory_db.sh` ✓
- `*/5 * * * *` → `sync.sh` (Google Drive) ✓

**Pre-existing n8n backup (not from B-001):**
- Script: `/opt/n8n/backup-n8n.sh`
- Target: `/opt/n8n/backups/`
- Schedule: `0 3 * * *` (crontab)
- This is a separate backup mechanism pre-dating B-001. Both mechanisms are currently active.

**Google Drive remote validation disclaimer:**
Google Drive backup contents were excluded from this investigation. Remote validation — verifying that files are actually present and intact in `gdrive:myPKA` — was **not performed**. The rclone sync job is confirmed active in crontab and a 2.0M sync log exists, but no check was made confirming files arrived correctly on the remote. A separate read-only remote validation check is recommended before claiming end-to-end backup coverage.

---

## 7. Consistency Findings

### Finding F-001: Dual n8n backup mechanism

| | |
|---|---|
| **Path** | `/opt/n8n/backups/` and `/home/admin/backups/n8n/` |
| **Finding type** | Redundancy |
| **Expected state** | One documented canonical n8n backup target |
| **Actual state** | Two separate n8n backup scripts targeting different directories. Pre-existing `/opt/n8n/backup-n8n.sh` runs at `0 3 * * *` to `/opt/n8n/backups/`. B-001 `backup_n8n.sh` runs at `0 2:45 * * *` to `/home/admin/backups/n8n/`. |
| **Risk** | Low — both work independently. Redundancy is not harmful but creates ambiguity about which backup is authoritative for DR purposes. |
| **Recommended action** | Document `/home/admin/backups/n8n/` as the canonical B-001 managed backup in SOP-001. Document the pre-existing `/opt/n8n/backup-n8n.sh` as a separate active mechanism. Any decommissioning of the pre-existing script requires a dedicated proposal and Owner approval — not in scope for B-021. |

---

### Finding F-002: `mypka-backup.log` is empty

| | |
|---|---|
| **Path** | `/home/admin/backups/mypka-backup.log` |
| **Finding type** | Logging gap |
| **Expected state** | Log file populated with rsync run results |
| **Actual state** | 0 bytes |
| **Risk** | Low — backup folders exist and are populated, so rsync is running. The exact cause of the empty log (suppressed output, missing redirect, wrong path) has not been identified in this pass. |
| **Recommended action** | Classify as requiring focused read-only technical investigation before any script modification is proposed. No fix may be executed until the cause is confirmed and a separate proposal is approved. |

---

### Finding F-003: `mypka-sync.log` grows without rotation

| | |
|---|---|
| **Path** | `/home/admin/backups/mypka-sync.log` |
| **Finding type** | Missing log rotation |
| **Expected state** | Log file with bounded size or rotation policy |
| **Actual state** | 2.0M and growing — every 5-minute rclone sync appends to this file with no cleanup. |
| **Risk** | Low in the near term. Over months this file will consume significant disk space on the Pi's SD card. |
| **Recommended action** | Prepare a separate exact implementation proposal for either logrotate config or bounded logging in `sync.sh`. No execution until that proposal exists and is separately approved. |

---

### Finding F-004: SQLite backup — only one date set exists

| | |
|---|---|
| **Path** | `/home/admin/backups/sqlite/` |
| **Finding type** | Expected behavior — noted for completeness |
| **Expected state** | Up to 7 date sets (7-day retention) |
| **Actual state** | 1 date set (`20260603/`) — B-001 was implemented on June 3 |
| **Risk** | None — expected. Will accumulate to 7 sets within a week of the first nightly run. |
| **Recommended action** | No action required. Verify again in 7 days. |

---

### Finding F-005: SOP-001 does not reference B-001 backup scripts

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` |
| **Finding type** | Documentation gap |
| **Expected state** | SOP-001 references the backup scripts and expected restore procedure |
| **Actual state** | SOP-001 describes memory-db restore and general setup steps but does not mention `backup_sqlite_dbs.sh`, `backup_n8n.sh`, `backup_memory_db.sh` or `local-backup.sh`. The backup infrastructure from B-001 is not reflected in DR documentation. |
| **Risk** | Medium — in a DR scenario, the operator may not know where backups are or how to restore them. |
| **Recommended action** | Update SOP-001 with a comprehensive backup section. See C-001 in B-021A. |

---

### Finding F-006: `/opt/mypka-memory/.env` not in any backup path

| | |
|---|---|
| **Path** | `/opt/mypka-memory/.env` |
| **Finding type** | Credential coverage gap |
| **Expected state** | Either documented as manually recovered on DR, or covered by a separate secure credential backup |
| **Actual state** | The `.env` file at `/opt/mypka-memory/` is outside `/opt/myPKA/` and outside all current backup paths. If the Pi hardware fails, this file is lost and memory-db cannot start without re-entering the credentials. |
| **Risk** | Medium if undocumented. |
| **Recommended action** | Do not add to regular myPKA, rclone or Google Drive backups. Treat as sensitive credential material. Default: document manual recovery procedure in SOP-001 — what credentials are needed and where to source them. No secret values may be written in SOP-001 or any deliverable. A separate secure-secret backup proposal may follow if manual recovery is deemed insufficient. |

---

### Finding F-007: No backup of `/home/admin/.config/rclone/`

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/` |
| **Finding type** | Coverage gap |
| **Expected state** | rclone OAuth token either backed up or explicitly noted as requiring manual re-authentication on DR |
| **Actual state** | `rclone.conf` (with OAuth token) is in `/home/admin/.config/rclone/`. Not covered by any backup path. |
| **Risk** | Low — acceptable if documented. Re-authentication requires device access and OAuth flow on new hardware. Token expiry also requires this. |
| **Recommended action** | Document in SOP-001 that rclone re-authentication is required on new hardware or after token expiry. This is a documentation item, not a backup item. |

---

## 8. Proposed Changes

v0.2 restructures the proposed changes into three execution-safe phases. **None of these phases are approved or active until Owner Walter Kamer gives explicit approval for each phase separately.**

---

### Phase B-021A — SOP-001 Documentation Update

Documentation only. No scripts touched. Highest-priority phase.

#### Change C-001 (merged from v0.1 C-001 and C-004): SOP-001 comprehensive backup section

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` |
| **Executor** | Kai |
| **Action** | Add a dedicated backup section to SOP-001 documenting: |
| | (1) All four B-001 backup scripts with paths, cron schedules, retention periods and target directories |
| | (2) `/home/admin/backups/n8n/` as the canonical B-001 managed n8n backup |
| | (3) `/opt/n8n/backups/` as the pre-existing separate n8n backup — both mechanisms documented; no decommissioning in this task |
| | (4) Restore references or known restore commands for each backup type where already documented |
| | (5) Rclone re-authentication requirement: re-auth is required on new hardware or after token expiry, requiring device access and OAuth flow |
| | (6) `/opt/mypka-memory/.env` recovery note: credentials must be recovered manually from a secure source; this file is not in regular backups; no secret values written anywhere |
| **Note** | This merges v0.1 C-001 and C-004 into a single SOP-001 update. |
| **Risk** | Low — documentation only. |
| **Owner approval required** | Yes |

---

### Phase B-021B — Logging Improvements Proposal

Each change in this phase requires a separate exact implementation proposal before any execution.

#### Change C-002: Focused investigation of `mypka-backup.log` empty state

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/local-backup.sh` |
| **Executor** | Kai |
| **Action** | Perform a read-only investigation to identify the exact cause of the zero-byte log. Check the log redirection syntax in `local-backup.sh`. |
| **Deliverable** | Short finding report: cause identified or "cause not identified — needs deeper investigation." |
| **Note** | If the cause cannot be confirmed in a read-only pass, classify as "needs focused technical investigation" and defer. No script modification without a confirmed cause and a separately approved fix proposal. |
| **Risk** | None — investigation only. Any subsequent fix requires separate Owner approval. |
| **Owner approval required** | Yes for any script modification. |

---

#### Change C-003: Bounded logging for `mypka-sync.log`

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/sync.sh` or `logrotate.d` |
| **Executor** | Kai |
| **Action** | Prepare an exact implementation proposal for one of: (a) `logrotate` config for `mypka-sync.log`, or (b) bounded log approach in `sync.sh`. |
| **Deliverable** | Proposal showing exact change — before/after, rationale, risk. |
| **Note** | No execution until the implementation proposal is reviewed and approved separately by Owner. |
| **Risk** | Low — affects logging only, not backup integrity. |
| **Owner approval required** | Yes — both for the proposal review and execution. |

---

### Phase B-021C — Secure Credential Recovery Proposal

Concerns sensitive credential material. Requires a separate proposal and Owner approval.

#### Change C-004: Document manual recovery procedure for `/opt/mypka-memory/.env`

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` |
| **Executor** | Kai |
| **Action** | Document the manual recovery procedure in SOP-001: which service the credentials belong to, what to re-enter, where to source the values on DR. Optionally: prepare a separate secure-secret backup proposal if manual recovery is deemed insufficient after review. |
| **Constraints** | No secret values may be written in SOP-001 or any deliverable. This file must not be added to regular myPKA, rclone or Google Drive backups. |
| **Risk** | Low if documented. Medium if silent. |
| **Owner approval required** | Yes for both the documentation and any secure backup proposal. |

---

## 9. Items Requiring Owner Decision

| Decision | Recommended approach | Impact |
|---|---|---|
| Approve B-021A for execution? | Yes — documentation only, high DR value, lowest risk | DR clarity |
| Dual n8n backup: document both without decommissioning? | Yes — document both; pre-existing script stays active; any future decommission is a separate proposal | Low risk |
| `mypka-backup.log`: investigation before any fix? | Yes — Kai investigates read-only first; no script change until cause confirmed | Low risk |
| `mypka-sync.log`: separate implementation proposal before execution? | Yes — Kai prepares exact proposal; no execution until separately approved | Low risk |
| `.env`: manual recovery documentation as default (B-021C)? | Yes — sensitive credential; document recovery only; no regular backup | Credential safety |
| Google Drive remote validation: separate read-only check? | Recommended — one-time check that files are present in `gdrive:myPKA` | DR completeness |

---

## 10. Risk Assessment

| Finding | Risk if not addressed | Priority |
|---|---|---|
| SOP-001 not updated (F-005) | DR operator cannot find backups | Medium |
| `.env` not covered (F-006) | Credentials lost on hardware failure | Medium |
| Dual n8n backup ambiguity (F-001) | Operator uses wrong backup in DR | Low |
| Empty `mypka-backup.log` (F-002) | Cannot confirm daily snapshot ran from log | Low |
| `mypka-sync.log` unbounded (F-003) | Disk fill over months | Low |
| rclone config not backed up (F-007) | Re-auth required on DR | Low |
| Google Drive not validated | Cannot confirm end-to-end backup coverage | Informational |

Overall risk: **Low to Medium**. The local backup infrastructure is running on schedule. The risks are documentation gaps, two medium-priority items (SOP-001 and `.env` recovery), and Google Drive remote coverage not yet confirmed.

---

## 11. Recommended Execution Plan

After Owner's explicit approval per phase:

**Phase B-021A — SOP-001 documentation update (recommended to approve first):**
- Executor: Kai
- Action: C-001 — add comprehensive backup section to SOP-001
- Audit trail: changelog in SOP-001, team_log entry, session log per GL-014 v1.2 §6
- Post-check: SOP-001 contains backup section referencing all four scripts, both n8n mechanisms, rclone re-auth note, `.env` recovery note (no secrets)

**Phase B-021B — Logging improvements (propose before executing):**
- Executor: Kai
- Step 1: C-002 — read-only investigation of `mypka-backup.log`; deliver finding report
- Step 2: C-003 — prepare exact implementation proposal for `mypka-sync.log` bounded logging
- No execution until investigation result and proposals are reviewed and separately approved

**Phase B-021C — Credential recovery documentation (separate proposal):**
- Executor: Kai
- Action: C-004 — document manual `.env` recovery procedure in SOP-001
- Constraint: no secret values in any deliverable
- Optional follow-up: secure-secret backup proposal if manual recovery is deemed insufficient

---

## 12. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval per phase.**

This is a read-only proposal. No files have been modified. The execution plan in §11 is not active until Owner's explicit approval is received for each phase separately.

---

## 13. Final Recommendation

The local backup infrastructure introduced in B-001 is running on schedule. All four backup types — myPKA snapshot, SQLite, n8n, memory-db — are active with appropriate retention policies. The local folder structure appears consistent with the expected design.

This investigation does **not** constitute full backup validation:
- Google Drive remote contents were not validated. It is not confirmed that files are present and intact in `gdrive:myPKA`.
- Restore procedures have not been tested.
- Backup log visibility is incomplete (`mypka-backup.log` is empty; cause unknown).

The two highest-priority follow-up items are:
1. **SOP-001 update (B-021A)** — the backup infrastructure is undiscoverable in a DR scenario without this documentation. Safe to approve for immediate execution.
2. **`.env` credential recovery documentation (B-021C)** — this credential file is outside all current backup paths and its loss on hardware failure is currently undocumented. Requires a separate proposal before execution.

B-021B (logging) should proceed as investigation first, with exact implementation proposals before any execution.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-021-backup-folder-consistency-check-proposal-v02.md`*
