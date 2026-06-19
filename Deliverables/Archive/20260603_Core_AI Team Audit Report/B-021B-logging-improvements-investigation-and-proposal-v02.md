# B-021B Logging Improvements Investigation and Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry (investigation) / Kai (executor when approved)
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Supersedes:** B-021B v0.1 (2026-06-03)

---

## Change Log (v0.1 → v0.2)

| # | Correction applied |
|---|---|
| 1 | Rollback method for P-001 corrected — `local-backup.sh` is NOT in the myPKA rsync backup path; safe rollback strategy provided (timestamped copy before edit + original content in execution report) |
| 2 | P-001 scope explicitly stated — logging-only; rsync flags, backup behavior, cleanup behavior and script exit behavior are unchanged |
| 3 | Exit behavior clarification — `EXIT_CODE=$?` is for log output only; script exit behavior is unchanged; any change to exit behavior is explicitly deferred to a separate proposal |
| 4 | P-002 logrotate unchanged |
| 5 | RATE_LIMIT_EXCEEDED remains out of scope |
| 6 | Execution Plan updated — read-before-edit, rollback preparation step, exact post-checks, confirmations |

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
- `/home/admin/.config/rclone/myPKA-filter.txt` — rclone sync filter (to assess backup scope)
- `crontab -l` — all entries for local-backup.sh and sync.sh
- `/home/admin/backups/myPKA/` — backup folder presence to confirm rsync is running
- logrotate availability and existing configs

**Excluded:**
- `/home/admin/.config/rclone/rclone.conf` — not relevant to logging behavior
- Google Drive remote contents
- Other backup scripts (backup_sqlite_dbs.sh, backup_n8n.sh, backup_memory_db.sh)
- Content of backup folders
- RATE_LIMIT_EXCEEDED error handling — a separate operational finding, out of scope for B-021B

---

## 4. Read-Only Investigation Method

Investigation performed using:
- `ls -lh` on both log files — sizes, permissions, timestamps
- `stat` on `mypka-backup.log` — exact creation, modification and change times
- `wc -l` on both log files — line counts
- `cat` / Read tool on `local-backup.sh`, `sync.sh`, and `myPKA-filter.txt` — full content
- `crontab -l` filtered for backup/sync entries — cron schedules and any cron-level redirection
- `head` and `tail` on `mypka-sync.log` — content structure and entry format
- `grep -c` on `mypka-sync.log` — line composition analysis
- `ls -la` on backup folder — confirmed rsync is running
- `stat` on most recent backup folder — confirmed last run timestamp
- `logrotate --version` and `ls /etc/logrotate.d/` — logrotate availability
- `df -h` — available disk space
- `realpath` on `local-backup.sh` — confirmed its actual location relative to backup scope
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

The `find` cleanup command (which removes folders older than 30 days) also produces no output unless it actually deletes something.

### 6.5 Risk level

**Low for backup integrity** — the daily backups ARE running and producing correct results. The risk is observability-only: there is no way to confirm from the log whether a specific day's backup succeeded or encountered a non-fatal error.

**Would become Medium** if rsync begins failing silently — there would be no log evidence to detect the failure without manually inspecting the backup folder timestamps each day.

### 6.6 Fix proposal allowed under GL-005 Diagnostic Discipline

**Yes.** The cause is confirmed read-only. GL-005 permits proposing a fix when the cause is known. See §8 for the exact proposed change.

### 6.7 Recommended next action

Add timestamped status lines to `local-backup.sh` around the rsync command. This gives operational visibility (confirmation of each daily run) without flooding the log with file-level details. See P-001 in §8.

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

**Note on RATE_LIMIT_EXCEEDED errors:** The log contains repeated rate limit errors from the Google Drive API. Addressing this is a separate operational finding outside B-021B scope. It is noted here because these multi-line JSON payloads contribute to the above-average growth rate.

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
- Rate limit error bursts generate verbose JSON payloads that can spike growth
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
| **Type** | Logging-only change |
| **Risk** | Low |
| **Owner approval required** | Yes — script modification |

#### Scope of P-001 — logging only

P-001 changes exactly the following:
- Adds a timestamped `echo` line before the rsync command (records start time and destination)
- Adds a timestamped `echo` line after the rsync command (records completion and rsync exit code, for log visibility only)
- Translates the Dutch comments in the script to English (language compliance)

P-001 does **not** change:
- rsync flags or options — `rsync -a` is preserved exactly
- Backup source or destination paths
- Backup behavior or what is backed up
- Cleanup behavior (find command is unchanged)
- Script exit behavior — the script exits naturally after the find command, as before. The `EXIT_CODE` variable is used only for the log echo; it does not affect whether the script continues, retries, or exits early.
- Any alerting or notification mechanism
- Cron schedule

Any change to script exit behavior (e.g. `exit $EXIT_CODE` to propagate the rsync exit code to cron, or conditional abort on failure) is explicitly deferred to a separate future proposal and is not part of B-021B.

#### Rollback method — corrected

**Important:** `/home/admin/.config/rclone/local-backup.sh` is located at `/home/admin/.config/rclone/`, which is **not** under `/opt/myPKA/`. The myPKA rsync snapshot (`rsync -a /opt/myPKA/ ...`) and the rclone Google Drive sync (`rclone sync /opt/myPKA gdrive:myPKA`) both cover `/opt/myPKA/` only. Neither backup covers `/home/admin/.config/rclone/`. This script is not recoverable from any existing backup path.

**Approved rollback strategy (two-layer):**

Layer 1 — Before editing, the executor creates a timestamped backup copy in the same directory:
```bash
cp /home/admin/.config/rclone/local-backup.sh \
   /home/admin/.config/rclone/local-backup.sh.pre-B021B-$(date +%Y%m%d)
```
This stays on the same device. If the edited file has issues, restoring is:
```bash
cp /home/admin/.config/rclone/local-backup.sh.pre-B021B-YYYYMMDD \
   /home/admin/.config/rclone/local-backup.sh
```

Layer 2 — The execution report must include the exact original file content verbatim. This ensures the script can be reconstructed from the deliverable even if both the current file and the timestamped copy are unavailable.

**Neither rollback action is executed now.** This is a proposal. The timestamped copy is created by the executor as the first step of the execution session, before any edit.

#### Exact proposed content for `local-backup.sh`

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

#### Changes from current version, line by line

| Change | Detail |
|---|---|
| Comment on line 2 | `# myPKA dagelijkse lokale snapshot...` → `# myPKA daily local snapshot...` (language compliance only) |
| New line before rsync | `echo "...backup started → $DEST"` — records start timestamp and destination |
| New `EXIT_CODE` capture | `EXIT_CODE=$?` — captures rsync exit code immediately after rsync completes |
| New line after rsync | `echo "...backup completed, exit code $EXIT_CODE"` — records completion timestamp and rsync exit code in the log |
| Cleanup comment | `# Opruimen: ...` → `# Remove snapshots older than 30 days` (language compliance only) |
| All other lines | Unchanged |

---

### Change P-002: Create logrotate config for `mypka-sync.log`

| Field | Value |
|---|---|
| **Path** | `/etc/logrotate.d/mypka-sync` (new file) |
| **Executor** | Kai |
| **Action** | Create a logrotate configuration file for `mypka-sync.log` |
| **Risk** | Low — logrotate is additive; sync.sh unchanged; `copytruncate` is safe for append-based scripts |
| **Owner approval required** | Yes — system file creation (requires sudo/root access) |

#### Exact proposed content for `/etc/logrotate.d/mypka-sync`

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
- `copytruncate` — copy the log to the rotated file then truncate the original to zero in-place. Safe for sync.sh because the script uses `>>` append and does not hold the file open between runs. No signal or restart is needed.

**Rollback method:** Remove `/etc/logrotate.d/mypka-sync`. The log file continues to grow as before. Any already-rotated files remain but cause no harm.

**Note on current log content:** The existing 2.0M log will be rotated out within 7 daily cycles. No manual truncation is required.

---

## 9. Items Not Proposed

### Script exit behavior change — explicitly deferred

Changing the script's exit behavior (e.g. adding `exit $EXIT_CODE` to propagate the rsync result to cron, or aborting cleanup if rsync fails) is a behavioral change beyond the logging scope of B-021B. It is not proposed here. Any such change requires a separate proposal with exact content and risk assessment.

### mypka-backup.log — no manual truncation proposed

The log is already empty. No truncation or clearing is needed or proposed.

### rclone `--log-level` to reduce sync.sh verbosity — deferred

Adding `--log-level ERROR` to sync.sh would reduce log size by suppressing informational messages. This is a valid follow-up improvement but requires modifying sync.sh and is independent of the logrotate config. It can be proposed separately after P-002 is executed.

### RATE_LIMIT_EXCEEDED error handling — out of scope

The sync log contains repeated Google Drive API rate limit errors. Addressing these (e.g. adjusting sync frequency or rclone transfer parameters) is a separate operational finding and is not in scope for B-021B.

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
| P-001: Add echo lines to local-backup.sh | Low — additive only. rsync flags unchanged. Backup behavior unchanged. Script exit behavior unchanged. Rollback: restore from timestamped copy created before edit. |
| P-002: Create logrotate config | Low — logrotate is additive. `copytruncate` is the safe option for append-based scripts. Rollback: delete the config file. |

**Both changes together: Low overall risk.**

---

## 11. Recommended Execution Plan

After Owner's explicit approval:

**Step 1 — Rollback preparation for `local-backup.sh` (before any edit)**
- Executor: Kai
- Action: Create a timestamped backup copy of the current script:
  ```bash
  cp /home/admin/.config/rclone/local-backup.sh \
     /home/admin/.config/rclone/local-backup.sh.pre-B021B-$(date +%Y%m%d)
  ```
- Verify: confirm the copy exists and matches the original
- This step must complete before any edit to `local-backup.sh`

**Step 2 — Read current `local-backup.sh`**
- Executor: Kai
- Action: Read the current file and confirm it matches the expected state described in §5 and §8 of this proposal
- Do not proceed if the file content differs from expected — report to Owner

**Step 3 — Execute P-001: Update `local-backup.sh`**
- Executor: Kai
- Action: Replace `local-backup.sh` with the exact content from §8 P-001
- Read-after: read the file back in full and confirm the content is correct
- Post-checks:
  - `echo` lines present before and after rsync
  - rsync command unchanged (`rsync -a /opt/myPKA/ "$DEST/" >> "$LOGFILE" 2>&1`)
  - `EXIT_CODE=$?` present — for logging only; no `exit $EXIT_CODE` present
  - Find command unchanged
  - Comments in English
  - No secrets or credential values introduced
  - No cron schedule changes
  - Script exit behavior unchanged: script ends with find command, no early exit added

**Step 4 — Execute P-002: Create logrotate config**
- Executor: Kai
- Action: Create `/etc/logrotate.d/mypka-sync` with the exact content from §8 P-002
- Requires: sudo or root access (logrotate.d is a system directory)
- Post-checks:
  - `sudo logrotate -d /etc/logrotate.d/mypka-sync` (dry-run, read-only) — confirm config is valid and would rotate the correct file
  - Confirm `copytruncate` directive is present
  - Confirm `rotate 7` and `daily` are present
  - Confirm no manual truncation of `mypka-sync.log` was performed

**Step 5 — Audit trail**
- team_log entry
- Session log
- Execution report including:
  - Exact original `local-backup.sh` content documented verbatim (Layer 2 rollback)
  - Confirmation that no logs were manually truncated
  - Confirmation that no script behavior was changed beyond logging (no rsync flag changes, no exit behavior changes)
  - Confirmation that sync.sh was not modified

P-001 and P-002 may be executed in the same session or separately. Step 1 (rollback preparation) must precede Step 3.

---

## 12. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve P-001 (add echo lines to local-backup.sh)? | a) Approve b) Request content changes c) Defer | Fixes empty log; confirms daily backup success/failure |
| 2 | Confirm P-001 scope: logging-only, no exit behavior change? | a) Confirm b) Request exit behavior change as part of this proposal (requires separate exact content) | Scope boundary for B-021B execution |
| 3 | Approve P-002 (logrotate config for mypka-sync.log)? | a) Approve b) Request config changes c) Defer | Bounds mypka-sync.log to ~7 days of compressed history |
| 4 | Execute P-001 and P-002 in the same session? | a) Same session b) Separate sessions | Scope management |

---

## 13. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only investigation and proposal. No files, scripts, logs, cron entries or databases have been modified. The changes described in §8 are not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of B-021B v0.2 is an approval of the exact content provided in §8. Any content change to either P-001 or P-002 after approval but before execution requires a separate approval.

---

## 14. Final Recommendation

**B-021B v0.2 is ready for Owner approval.**

**Finding A (mypka-backup.log) — cause confirmed.** rsync -a without verbosity flags produces no output on success. Adding timestamped echo lines (P-001) resolves this immediately. P-001 is logging-only and does not change rsync flags, backup behavior, cleanup behavior, or script exit behavior. The rollback strategy is controlled: timestamped copy created before edit, original content documented in execution report.

**Finding B (mypka-sync.log) — logrotate recommended.** logrotate (P-002) requires no script changes, is system-standard, and uses `copytruncate` for safe compatibility with sync.sh's append pattern.

**Recommended next step:** Owner Walter Kamer approves P-001 and P-002 for Kai to execute. Both are low-risk, bounded changes that can be executed in a single session.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-021B-logging-improvements-investigation-and-proposal-v02.md`*
