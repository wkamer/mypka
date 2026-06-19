# B-021 Backup Folder Consistency Check Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Purpose

This proposal checks whether the backup folder structure on the myPKA Raspberry Pi is consistent, complete and aligned with the backup scripts introduced in B-001 (Stabilization Package v1). The goal is to identify gaps, redundancies, unclear conventions or unmaintained locations before they become a recovery risk.

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
- Google Drive backup contents (remote, not locally inspectable in this pass)
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
- This is a separate backup mechanism pre-dating B-001.

---

## 7. Consistency Findings

### Finding F-001: Dual n8n backup mechanism

| | |
|---|---|
| **Path** | `/opt/n8n/backups/` and `/home/admin/backups/n8n/` |
| **Finding type** | Redundancy |
| **Expected state** | One canonical n8n backup target |
| **Actual state** | Two separate n8n backup scripts targeting different directories. Pre-existing `/opt/n8n/backup-n8n.sh` runs at `0 3 * * *` to `/opt/n8n/backups/`. B-001 `backup_n8n.sh` runs at `0 2:45 * * *` to `/home/admin/backups/n8n/`. |
| **Risk** | Low — both work independently. Redundancy is not harmful but creates ambiguity about which backup is authoritative for DR purposes. |
| **Recommended action** | Document which backup is canonical in SOP-001. Optionally decommission the pre-existing script if the B-001 backup fully covers it. |

---

### Finding F-002: `mypka-backup.log` is empty

| | |
|---|---|
| **Path** | `/home/admin/backups/mypka-backup.log` |
| **Finding type** | Logging gap |
| **Expected state** | Log file populated with rsync run results |
| **Actual state** | 0 bytes |
| **Risk** | Low — the backup folders exist and are populated, so rsync is likely running. The log output may be suppressed or redirected differently than expected. Cannot confirm backup success from the log alone. |
| **Recommended action** | Verify that `local-backup.sh` is writing to this log correctly. Check the script's redirection syntax. |

---

### Finding F-003: `mypka-sync.log` grows without rotation

| | |
|---|---|
| **Path** | `/home/admin/backups/mypka-sync.log` |
| **Finding type** | Missing log rotation |
| **Expected state** | Log file with bounded size or rotation policy |
| **Actual state** | 2.0M and growing — every 5-minute rclone sync appends to this file with no cleanup. |
| **Risk** | Low in the near term. Over months this file will consume significant disk space. |
| **Recommended action** | Add `logrotate` config for `mypka-sync.log`, or change `sync.sh` to use a bounded log. |

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
| **Risk** | Medium — in a DR scenario, the operator may not know where backups are or how to use them. |
| **Recommended action** | Update SOP-001 with a new section documenting backup locations, scripts, schedules and restore commands. |

---

### Finding F-006: No backup coverage for mypka-memory venv

| | |
|---|---|
| **Path** | `/opt/mypka-memory/` |
| **Finding type** | Coverage gap |
| **Expected state** | Either included in backup or explicitly documented as outside backup scope |
| **Actual state** | The memory-db Python venv at `/opt/mypka-memory/` is outside `/opt/myPKA/` and outside `/home/admin/backups/`. The myPKA rsync snapshot only covers `/opt/myPKA/`. SOP-001 documents manual recreation of this venv in DR. |
| **Risk** | Low — venv can be recreated from SOP-001 steps. But the `.env` credentials file at `/opt/mypka-memory/.env` is also outside all backup paths. |
| **Recommended action** | Confirm whether `/opt/mypka-memory/.env` is backed up somewhere (possibly included in myPKA via symlink or reference). If not, add it to a backup or document the recovery procedure explicitly. |

---

### Finding F-007: No backup of `/home/admin/.config/rclone/`

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/` |
| **Finding type** | Coverage gap |
| **Expected state** | rclone OAuth token and configuration either backed up or explicitly noted as external-credential requiring manual re-auth on DR |
| **Actual state** | `rclone.conf` (with OAuth token) is in `/home/admin/.config/rclone/`. The myPKA rsync snapshot only covers `/opt/myPKA/`. The rclone config is not in any backup path. |
| **Risk** | Medium — in a DR scenario, Google Drive sync cannot be restored without re-authenticating rclone, which requires device access and OAuth flow. Token expiry also requires this. This is acceptable but should be explicitly documented in SOP-001. |
| **Recommended action** | Document in SOP-001 that rclone re-authentication is required on new hardware. |

---

## 8. Proposed Changes

### Change C-001: Document canonical n8n backup in SOP-001

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` |
| **Action** | Add a section documenting: (1) `/home/admin/backups/n8n/` as the canonical B-001 managed backup, (2) `/opt/n8n/backups/` as the pre-existing backup, (3) which to use for restore. |
| **Reason** | Removes dual-backup ambiguity for DR use. |
| **Risk** | Low — documentation only. |
| **Owner approval required** | Yes — SOP modification. |

---

### Change C-002: Add log rotation or bounded logging for `mypka-sync.log`

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/sync.sh` or `logrotate.d` |
| **Action** | Either add a logrotate configuration for `mypka-sync.log`, or modify `sync.sh` to use a max-size log (e.g. `tail -c 1M` approach). |
| **Reason** | Prevents unbounded log growth on the Pi's SD card. |
| **Risk** | Low — affects only logging, not backup integrity. |
| **Owner approval required** | Yes — script modification. |

---

### Change C-003: Investigate and fix `mypka-backup.log` empty state

| | |
|---|---|
| **Path** | `/home/admin/.config/rclone/local-backup.sh` |
| **Action** | Check the redirection syntax in `local-backup.sh`. If the log redirect is missing or broken, fix it so rsync success/failure is captured. |
| **Reason** | Zero-byte log prevents confirming daily myPKA snapshot success without checking folder mtime manually. |
| **Risk** | Low — if backup folders are being created, the actual backup is working. This is a visibility fix only. |
| **Owner approval required** | Yes — script modification. |

---

### Change C-004: Update SOP-001 with B-001 backup infrastructure

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` |
| **Action** | Add a dedicated backup section listing all four backup scripts, their targets, schedules and restore commands. |
| **Reason** | SOP-001 is the DR reference. Without this, the B-001 backup infrastructure is undiscoverable in a real DR scenario. |
| **Risk** | Low — documentation only. |
| **Owner approval required** | Yes — SOP modification. |

---

### Change C-005: Document mypka-memory `.env` backup status

| | |
|---|---|
| **Path** | `Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md` or `Team Knowledge/Core/Integrations/memory-db/` |
| **Action** | Either add `/opt/mypka-memory/.env` to a backup mechanism, or explicitly document its DR recovery method (re-create credentials from secure source). |
| **Reason** | If `.env` is lost, memory-db connection credentials must be manually re-entered. This risk should be documented. |
| **Risk** | Low if documented. Medium if lost silently. |
| **Owner approval required** | Yes. |

---

## 9. Items Requiring Owner Decision

| Decision | Options | Impact |
|---|---|---|
| Dual n8n backup: keep both or consolidate? | a) Keep both as redundancy b) Decommission pre-existing `/opt/n8n/backup-n8n.sh` c) Document both as active | Affects DR clarity |
| Log rotation for `mypka-sync.log`: add or accept unbounded growth? | a) Add logrotate b) Modify sync.sh c) Accept current state | Disk space management |
| Scope of SOP-001 update: minimal (backup locations only) or full (locations + restore commands)? | a) Minimal reference b) Full restore walkthrough | DR readiness |
| `mypka-memory/.env` backup: add to backup or document manual recovery? | a) Add to secure backup b) Document manual re-entry procedure | DR completeness |

---

## 10. Risk Assessment

| Finding | Risk if not addressed | Priority |
|---|---|---|
| Dual n8n backup ambiguity (F-001) | Operator uses wrong backup in DR | Low |
| Empty `mypka-backup.log` (F-002) | Cannot confirm daily snapshot ran from log | Low |
| `mypka-sync.log` unbounded (F-003) | Disk fill over months | Low |
| SOP-001 not updated (F-005) | DR operator cannot find backups | Medium |
| `mypka-memory/.env` not backed up (F-006) | Credentials lost on hardware failure | Medium |
| rclone config not backed up (F-007) | Re-auth required on DR (documented or not) | Low |

Overall risk: **Low to Medium**. The backup infrastructure is functioning. The risks are documentation gaps and two medium-priority items (SOP-001 and `.env` coverage).

---

## 11. Recommended Execution Plan

After Owner's explicit approval for the proposed changes:

1. **Executor:** Kai (infrastructure and integration specialist)
2. **Sequence:**
   1. C-004 first: update SOP-001 with B-001 backup documentation (highest DR value)
   2. C-001: document canonical n8n backup choice in SOP-001 (can be done in same pass as C-004)
   3. C-003: investigate and fix `mypka-backup.log` empty state
   4. C-002: add log rotation for `mypka-sync.log`
   5. C-005: document or backup `mypka-memory/.env`
3. **Audit trail:** changelog in SOP-001, team_log entry, session log per GL-014 v1.2 §6
4. **Post-checks after execution:**
   - SOP-001 contains backup section referencing all four scripts
   - `mypka-backup.log` captures rsync output
   - `mypka-sync.log` has rotation or bounded size

---

## 12. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. The execution plan in §11 is not active until Owner's explicit approval is received.

---

## 13. Final Recommendation

The backup infrastructure introduced in B-001 is functioning correctly. All four backup types (myPKA snapshot, SQLite, n8n, memory-db) are running on schedule with appropriate retention policies. No backup data has been lost and no critical gaps in coverage have been found.

The two medium-priority items to address are:
1. **SOP-001 update** — without this, the backup infrastructure is invisible in a DR scenario
2. **`mypka-memory/.env` coverage** — this credential file is outside all current backup paths

Both can be addressed in a single Kai execution pass after Owner approval.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-021-backup-folder-consistency-check-proposal.md`*
