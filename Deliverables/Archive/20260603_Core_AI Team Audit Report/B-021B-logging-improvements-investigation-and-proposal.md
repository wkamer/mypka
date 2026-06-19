# B-021B Logging Improvements Investigation and Proposal

**Date:** 2026-06-03
**Prepared by:** Larry (investigation) / Kai (executor when approved)
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Purpose

This investigation addresses two logging findings from the B-021 backup folder consistency check:

- **Finding F-002:** `/home/admin/backups/mypka-backup.log` is 0 bytes. The daily myPKA rsync snapshot runs successfully but leaves no log output, making it impossible to confirm daily backup success or failure from the log.
- **Finding F-003:** `/home/admin/backups/mypka-sync.log` grows without rotation. The rclone Google Drive sync runs every 5 minutes and appends to an unbounded log file.

This proposal follows the GL-005 Diagnostic Discipline rule: a read-only investigation was performed to confirm the cause of Finding F-002 before any fix is proposed. Finding B (mypka-sync.log) is a known pattern and an implementation proposal is provided directly.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| No fix proposed until cause is confirmed | GL-005 Diagnostic Discipline |
| No script or system file may be modified based on a hypothesis alone | GL-005 Diagnostic Discipline |
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |
| Scripts must not have hardcoded values | Larry AGENT.md Script Creation conventions |
| Critical infrastructure changes require Owner approval and audit trail | GL-014 v1.2 §6 |
| No secret values may appear in any deliverable | GL-014 v1.2 §3 |

---

## 3. Scope

**Inspected:**
- `/home/admin/backups/mypka-backup.log` — size, timestamps, content
- `/home/admin/backups/mypka-sync.log` — size, line count, content structure, growth rate
- `/home/admin/.config/rclone/local-backup.sh` — full script content
- `/home/admin/.config/rclone/sync.sh` — full script content
- `crontab -l` — all entries for local-backup.sh and sync.sh
- `/home/admin/backups/myPKA/` — backup folder presence to confirm rsync is running
- logrotate availability and existing configs

**Excluded:**
- `/home/admin/.config/rclone/rclone.conf` — not relevant to logging behavior
- Google Drive remote contents
- Other backup scripts (backup_sqlite_dbs.sh, backup_n8n.sh, backup_memory_db.sh)
- Content of backup folders

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `ls -lh` on both log files — sizes, permissions, timestamps
- `stat` on `mypka-backup.log` — exact creation, modification and change times
- `wc -l` on both log files — line counts
- `cat` / Read tool on `local-backup.sh` and `sync.sh` — full script content
- `crontab -l` filtered for backup/sync entries — cron schedules and any cron-level redirection
- `head` and `tail` on `mypka-sync.log` — content structure and entry format
- `grep -c` on `mypka-sync.log` — line composition analysis
- `ls -la` on backup folder — confirmed rsync is running
- `stat` on most recent backup folder — confirmed last run timestamp
- `logrotate --version` and `ls /etc/logrotate.d/` — logrotate availability
- `df -h` — available disk space
- Python calculation for growth rate projections

No files were modified, created, truncated, moved or deleted.

---

## 5. Current Logging State

### `mypka-backup.log`

| Property | Value |
|---|---|
| Path | `/home/admin/backups/mypka-backup.log` |
| Size | 0 bytes |
| Lines | 0 |
| Created | 2026-05-18 02:00:02 |
| Last modified | 2026-05-18 02:00:02 — never written to after creation |
| Permissions | `-rw-rw-r--` (admin:admin) |

### `mypka-sync.log`

| Property | Value |
|---|---|
| Path | `/home/admin/backups/mypka-sync.log` |
| Size | 2.0M |
| Lines | 15,621 |
| First entry | 2026-05-17 23:45:01 |
| Last entry | 2026-06-03 10:47:02 |
| Age | ~17 days |
| Growth rate | ~120 KB/day (~919 lines/day) |
| No rotation | Unbounded — no logrotate config exists |

### Crontab entries (relevant)

```
*/5 * * * * /home/admin/.config/rclone/sync.sh
0 2 * * * /home/admin/.config/rclone/local-backup.sh
```

Neither entry has cron-level output redirection. Both scripts handle their own logging.

### Script logging behavior

**`local-backup.sh`** (lines 1–11):
```bash
LOGFILE=/home/admin/backups/mypka-backup.log
rsync -a /opt/myPKA/ "$DEST/" >> "$LOGFILE" 2>&1
find ... >> "$LOGFILE" 2>&1
```
Redirect syntax is correct. LOGFILE path matches the actual log path. Both commands redirect stdout and stderr.

**`sync.sh`** (lines 1–22):
```bash
LOGFILE=/home/admin/backups/mypka-sync.log
...
echo "$(date): sync already running, skipping" >> "$LOGFILE"
...
rclone sync /opt/myPKA gdrive:myPKA ... >> "$LOGFILE" 2>&1
```
Appends to LOGFILE on every run. No size limit, no rotation.

---

## 6. Finding A — Empty `mypka-backup.log`

### 6.1 Expected behavior

The log file is populated with rsync output after each daily run. A complete log allows confirming that the daily snapshot succeeded and what was transferred.

### 6.2 Actual behavior

The file exists, has size 0, and has never been written to since creation on 2026-05-18 02:00:02. Every daily run since then has left no log output.

### 6.3 Evidence

| Evidence | Observation |
|---|---|
| Log created: 2026-05-18 02:00:02 | Matches cron schedule `0 2 * * *` — the `>>` redirect created the file on the first run |
| Log last modified: 2026-05-18 02:00:02 | Identical to creation time — the file has never been written to after creation |
| Backup folder 20260603 exists with access time 2026-06-03 02:00:01 | rsync ran today at 02:00 |
| Backup folders exist from 20260530 through 20260603 | rsync is running successfully every day |
| Script redirect syntax: `>> "$LOGFILE" 2>&1` | Correct — both stdout and stderr are captured |
| LOGFILE path: `/home/admin/backups/mypka-backup.log` | Matches the actual log file path exactly |
| rsync command flags: `rsync -a` | Archive mode only — no verbosity flags |
| No cron-level output redirection | Cron does not suppress the script's output; the script handles all logging itself |

### 6.4 Confirmed cause

**Cause confirmed read-only.**

`rsync -a` (archive mode) without any verbosity flag (`-v`, `--verbose`, `--itemize-changes`, `--stats`, `--progress`, or `--log-file`) produces **zero stdout output** on successful completion. rsync in quiet mode only emits output to stderr when an error occurs.

Because the daily backups are completing successfully (backup folders exist and are current), rsync exits without printing anything. The `>>` operator creates the log file on the first run, but since rsync emits nothing, nothing is ever appended.

This is expected rsync behavior — it is not a bug in the redirect syntax, the LOGFILE path, or the cron schedule. The redirect IS correct. The script was designed to capture rsync output, but rsync was called without flags that produce output.

The `find` cleanup command (which removes folders older than 30 days) also produces no output unless it actually deletes something, which has not happened yet given the backup folder age.

### 6.5 Risk level

**Low for backup integrity** — the daily backups ARE running and producing correct results. The risk is observability-only: there is no way to confirm from the log whether a specific day's backup succeeded or encountered a non-fatal error.

**Would become Medium** if rsync begins failing silently — there would be no log evidence to detect the failure without manually inspecting the backup folder timestamps each day.

### 6.6 Fix proposal allowed under GL-005 Diagnostic Discipline

**Yes.** The cause is confirmed read-only. GL-005 permits proposing a fix when the cause is known. See §8 for the exact proposed change.

### 6.7 Recommended next action

Add timestamped status lines to `local-backup.sh` around the rsync command. This gives operational visibility (confirmation of each daily run) without flooding the log with file-level details. Optionally add `--stats` to rsync to include a transfer summary.

---

## 7. Finding B — Growing `mypka-sync.log`

### 7.1 Expected behavior

The rclone sync log captures sync activity and errors in a bounded, manageable file. Old log content is rotated out so the file remains useful and does not consume unbounded disk space.

### 7.2 Actual behavior

The log has grown to 2.0M (15,621 lines) over 17 days with no rotation in place. The file will continue growing indefinitely as long as sync.sh appends to it.

### 7.3 Evidence

| Metric | Value |
|---|---|
| Size | 2.0 MB |
| Lines | 15,621 |
| Timestamped entries | 9,537 |
| "sync already running" skips | 53 |
| First entry | 2026-05-17 23:45:01 |
| Last entry | 2026-06-03 10:47:02 |
| Age | 17 days |

**Content composition:** The log contains rclone sync messages, rate limit exceeded errors (with verbose JSON API response payloads), and lock-skip notifications. The initial section of the log contains a large rclone bisync help output from 2026-05-17, which appears to be a setup artifact from before sync.sh was finalized. This historical block contributes to the current file size but will rotate away naturally once logrotate is implemented.

### 7.4 Growth risk

| Projection | Size |
|---|---|
| Current (17 days) | 2.0 MB |
| 6 months | ~21 MB |
| 1 year | ~43 MB |
| 2 years | ~86 MB |
| Available disk (`/`) | 160 GB |

**Absolute disk risk: Low.** 160 GB is available. At current growth rate, the file would not cause disk issues for years. However:
- Unbounded logs become difficult to search for relevant entries
- Rate limit error bursts (which generate multi-line JSON payloads) can spike growth beyond the average rate
- Establishing logrotate now prevents the file from becoming an unmanaged artifact over time
- It is a hygiene issue, not an emergency

### 7.5 Recommended bounded logging approach

**logrotate** is the recommended approach. It requires no modification to `sync.sh`, is system-standard on Debian/Pi OS, and logrotate 3.22.0 is confirmed available. The `copytruncate` option makes it compatible with sync.sh's `>>` append pattern without requiring the script to be restarted or notified.

The alternative — modifying `sync.sh` to bound the log itself — is possible but adds complexity to the script and requires separate Owner approval for a script change. logrotate is simpler, lower risk, and the right tool for this use case.

---

## 8. Proposed Changes

### Change P-001: Add timestamped status lines to `local-backup.sh`

| Field | Value |
|---|---|
| **Path** | `/home/admin/.config/rclone/local-backup.sh` |
| **Executor** | Kai |
| **Action** | Add `echo` statements before and after the rsync command to record the start time, destination, and exit code |
| **Risk** | Low — additive only; rsync behavior unchanged |
| **Owner approval required** | Yes — script modification |

**Exact proposed change** (full replacement content for `local-backup.sh`):

```bash
#!/bin/bash
# myPKA daily local snapshot (disaster recovery)

DEST="/home/admin/backups/myPKA/$(date +%Y%m%d)"
LOGFILE=/home/admin/backups/mypka-backup.log

echo "$(date '+%Y-%m-%d %H:%M:%S'): backup started → $DEST" >> "$LOGFILE"
rsync -a /opt/myPKA/ "$DEST/" >> "$LOGFILE" 2>&1
EXIT_CODE=$?
echo "$(date '+%Y-%m-%d %H:%M:%S'): backup completed, exit code $EXIT_CODE" >> "$LOGFILE"

# Remove snapshots older than 30 days
find /home/admin/backups/myPKA/ -maxdepth 1 -type d -name '[0-9]*' -mtime +30 -exec rm -rf {} + >> "$LOGFILE" 2>&1
```

**Changes from current version:**
1. Comment translated to English (language compliance)
2. `echo` start line added before rsync
3. Exit code captured in `$EXIT_CODE`
4. `echo` completion line with exit code added after rsync
5. Cleanup comment translated to English

**Why this approach:** Minimal change. rsync flags unchanged — no file lists written to the log, keeping it compact. Start/end timestamps confirm each run. Exit code captures silent failures. Errors from rsync still go to the log via stderr redirect.

**Rollback method:** Restore the original script content. The original is in the myPKA rsync backup folder (`/home/admin/backups/myPKA/YYYYMMDD/`).

---

### Change P-002: Create logrotate config for `mypka-sync.log`

| Field | Value |
|---|---|
| **Path** | `/etc/logrotate.d/mypka-sync` (new file) |
| **Executor** | Kai |
| **Action** | Create a logrotate configuration file for `mypka-sync.log` |
| **Risk** | Low — logrotate is additive; sync.sh unchanged; copytruncate is safe for append-based scripts |
| **Owner approval required** | Yes — system file creation |

**Exact proposed content for `/etc/logrotate.d/mypka-sync`:**

```
/home/admin/backups/mypka-sync.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    copytruncate
}
```

**Configuration notes:**
- `daily` — rotate once per day
- `rotate 7` — keep 7 compressed rotated copies (one week of history)
- `compress` — gzip compress rotated logs
- `missingok` — do not error if the log file is missing
- `notifempty` — do not rotate if the log is empty
- `copytruncate` — copy the log to the rotated file then truncate the original to zero in-place. This is safe for sync.sh because the script uses `>>` append and does not hold the file open between runs. No signal or restart is needed.

**Rollback method:** Remove `/etc/logrotate.d/mypka-sync`. The log file continues to grow as before. Any already-rotated files remain but cause no harm.

**Note on current log content:** The existing 2.0M log (including the historical bisync error block from 2026-05-17) will be rotated out within 7 daily cycles after implementation. No manual truncation is required.

---

## 9. Items Not Proposed

### `mypka-backup.log` — no fix proposed until this proposal is approved

Per GL-005 Diagnostic Discipline, a fix is not executed without confirmed cause. The cause is now confirmed. The fix is proposed in P-001 above and awaits Owner approval before execution.

### rclone sync rate limit errors — out of scope

The `mypka-sync.log` contains repeated RATE_LIMIT_EXCEEDED errors from the Google Drive API. These indicate rclone is hitting Google Drive API quotas during sync runs. This is a separate operational finding. Addressing it (e.g. adjusting sync frequency or rclone transfer parameters) is outside the scope of B-021B, which covers logging only.

### mypka-backup.log historical content — not an issue

The log is empty. There is no historical content to rotate or archive.

### Reducing rclone log verbosity — deferred

sync.sh does not currently use `--log-level` to filter rclone output. Adding `--log-level ERROR` would reduce log size by suppressing informational messages. This is a valid improvement but requires modifying sync.sh and is a separate, independent change from the logrotate config. It can be proposed as a follow-up after P-002 is executed.

---

## 10. Risk Assessment

### Risk of leaving current state unchanged

| Finding | Risk if not addressed |
|---|---|
| Empty `mypka-backup.log` | Low to Medium — backups run correctly but failures are invisible. A future rsync error would go undetected without daily manual folder inspection. |
| Growing `mypka-sync.log` | Low — disk is not at risk (160 GB available). The log becomes progressively harder to use for diagnostics as it grows. Risk increases if error rate spikes (JSON API payloads are large). |

### Risk of applying proposed changes

| Change | Risk if applied |
|---|---|
| P-001: Add echo lines to local-backup.sh | Low — additive only. rsync behavior unchanged. Rollback: restore original file from backup. |
| P-002: Create logrotate config | Low — logrotate is additive. `copytruncate` is the safe option for append-based scripts. Rollback: delete the config file. The only behavioral change is that the log file is truncated after rotation — sync.sh continues appending to the truncated file immediately. |

**Both changes together: Low overall risk.**

---

## 11. Recommended Execution Plan

After Owner's explicit approval:

**Step 1 — P-001: Update `local-backup.sh`**
- Executor: Kai
- Action: Replace `local-backup.sh` with the exact content from §8 P-001
- Read-before: confirm current file matches expected state
- Read-after: confirm new content is correct
- Post-check: verify next cron run (02:00) produces log output the following morning
- Audit trail: team_log entry, session log

**Step 2 — P-002: Create logrotate config**
- Executor: Kai
- Action: Create `/etc/logrotate.d/mypka-sync` with exact content from §8 P-002
- Requires: sudo or root access (logrotate.d is a system directory)
- Post-check: `sudo logrotate -d /etc/logrotate.d/mypka-sync` (dry-run, read-only) to confirm config is valid
- The current mypka-sync.log will be rotated the following day during the system's daily logrotate run
- Audit trail: team_log entry, session log

Both steps may be executed in the same session or separately. P-001 and P-002 are independent.

---

## 12. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve P-001 (add echo lines to local-backup.sh)? | a) Approve b) Request content changes c) Defer | Fixes empty log; confirms daily backup success/failure |
| 2 | Approve P-002 (logrotate config for mypka-sync.log)? | a) Approve b) Request config changes c) Defer | Bounds mypka-sync.log to ~7 days of compressed history |
| 3 | Approve both in the same execution session? | a) Same session b) Separate sessions | Scope management |
| 4 | Optional: also add `--log-level ERROR` to sync.sh to reduce rclone verbosity? | a) Include in this proposal b) Defer to separate proposal | Reduces log volume further but requires sync.sh change |

---

## 13. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only investigation and proposal. No files, scripts, logs, cron entries or databases have been modified. The changes described in §8 are not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

---

## 14. Final Recommendation

**Finding A (mypka-backup.log) — cause confirmed.** rsync -a without verbosity flags produces no output on success. The log is permanently empty because the redirect is correct but rsync emits nothing. Adding timestamped echo lines (P-001) resolves this immediately and gives operational visibility into daily backup runs.

**Finding B (mypka-sync.log) — logrotate recommended.** The log grows at ~120KB/day with no current risk to disk, but is already large enough to make diagnostics inconvenient. logrotate (P-002) requires no script changes and is the right system tool for this job.

**Recommended next step:** Owner Walter Kamer approves P-001 and P-002 for Kai to execute. Both are low-risk, bounded changes. Execution can be a single session.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-021B-logging-improvements-investigation-and-proposal.md`*
