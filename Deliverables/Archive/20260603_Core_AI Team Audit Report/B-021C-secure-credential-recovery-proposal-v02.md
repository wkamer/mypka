# B-021C Secure Credential Recovery Procedure Proposal — v0.2

**Status:** Proposal only — no implementation  
**Version:** v0.2 (revised from v0.1)  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Backlog item:** B-021C  
**Requires approval by:** Owner Walter Kamer — see §12 Approval Gate

---

## 1. Purpose

GL-014 §3 (Credential file backup rule, added in B-030A) mandates that recovery procedures for specific credential files be documented in SOP-001 Disaster Recovery without including secret values. SOP-001 currently contains a placeholder in two related locations:

1. Under `## Backup Infrastructure (B-001)` → `### /opt/mypka-memory/.env — Sensitive Credential File` (line 476): *"Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval)."*
2. Step 12c is brief and contains no permission-setting or validation steps.

This proposal closes both gaps. It is split into two independently approvable execution scopes: B-021C-A (SOP-001 documentation) and B-021C-B (live file permission fix).

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Credential file backup rule | GL-014 §3 — Sensitive credential files must not be added to regular myPKA, rclone or Google Drive backups |
| Recovery is manual-only | GL-014 §3 — Source credentials from a secure external store and re-enter them |
| Recovery procedures must be secret-free | GL-014 §3 — Documented in SOP-001 without including secret values |
| Automated backup requires separate proposal | GL-014 §3 — A separate secure-credential backup proposal is required before any automated credential backup is approved |
| SOP changes require Owner approval | GL-014 §1 — Only after explicit Owner approval |
| Secrets/credentials changes | GL-014 §9 — Executor: Kai; Reviewer: Larry; Final approval: Owner |
| SOP changes | GL-014 §9 — Executor: domain specialist; Reviewer: Larry; Final approval: Owner |
| No secrets in any output or document | GL-014 §3 — Secrets, tokens, API keys, encryption keys and passwords may never be shown in output or copied to SOPs, Guidelines, Workstreams, or session logs |

---

## 3. Execution Scope Split

This proposal contains two independent execution scopes. Owner Walter Kamer may approve each independently:

| Scope | Description | What changes |
|---|---|---|
| **B-021C-A** | SOP-001 documentation update | Two text changes in `SOP-001_Disaster recovery.md` — no live system change |
| **B-021C-B** | Live `.env` permission fix | `chmod 600 /opt/mypka-memory/.env` — no content change, no secret exposure |

**Approval options:**
- Approve B-021C-A only
- Approve B-021C-B only
- Approve both
- Defer both or either

Neither scope executes unless Owner gives explicit approval for that specific scope (see §12).

---

## 4. Scope

### Included

- Read-only investigation of GL-014 §3 and SOP-001 current content
- Metadata-only inspection of `/opt/mypka-memory/.env` (existence, permissions, size, timestamps — no secret values)
- Exact proposed text for B-021C-A: two SOP-001 changes
- Exact proposed command for B-021C-B: `chmod 600` with metadata-only verification
- Risk assessment and execution plan per approval scope

### Excluded

- Execution of any file change
- Reading, printing, or exposing any secret value
- Modification of GL-014, GL-005, AGENT.md files, CLAUDE.md, scripts, or databases
- Credential rotation
- Service restart
- Backup of `.env` to any path
- Automated secret backup of any kind

---

## 5. Read-Only Investigation Method

All investigation was performed without accessing secret values:

1. **GL-014** read in full via context-mode. §3 extracted and confirmed.
2. **SOP-001** located via `find` (filename: `SOP-001_Disaster recovery.md`, lowercase `r`). Read in full via context-mode.
3. **Line numbers confirmed** via targeted `grep -n` on non-secret content: Step 12c at lines 315–319, Step 12d at lines 321–327, placeholder at line 476.
4. **`/opt/mypka-memory/.env`** inspected using `stat` only — file existence, path, size, permissions, owner, group, timestamps. No content read.
5. **`/opt/mypka-memory/` directory** listed using `ls -la` — filenames and metadata only.
6. No `cat`, `less`, `head`, `tail`, `grep`, `awk`, `sed`, or content-reading command was run against `.env`.

---

## 6. Current State

### 6.1 SOP-001 Current Coverage

SOP-001 (`Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`) contains two relevant locations:

**Location 1 — Step 12c (line 315–319):**

```
**12c — .env aanmaken:**
```bash
cp /opt/mypka-memory/.env.template /opt/mypka-memory/.env
nano /opt/mypka-memory/.env   # wachtwoord ophalen uit Bitwarden: "memory-db / PostgreSQL"
```
```

Step 12c is brief. It instructs the Maintainer to copy the template and fill in credentials from Bitwarden. It does not include a permissions-setting step or pre-start validation. No `chmod` is instructed. No health check without secrets is documented here.

**Location 2 — Backup Infrastructure placeholder (line 476):**

```
In a DR scenario, credentials must be recovered manually from a secure source. Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval).
```

This is the placeholder B-021C was created to close. It provides no actionable guidance.

### 6.2 `/opt/mypka-memory/.env` Metadata

| Property | Value |
|---|---|
| Path | `/opt/mypka-memory/.env` |
| Status | Exists |
| Size | 339 bytes |
| Permissions | 0664 (-rw-rw-r--) |
| Owner | admin (uid 1000) |
| Group | admin (gid 1000) |
| Modified | 2026-05-20 23:15 |

**Permission finding:** 0664 means the file is readable and writable by any member of the `admin` group, and readable by all other users on the system. For a credential file, this is overly permissive. Recommended: 0600 (owner read/write only). This is the subject of B-021C-B.

### 6.3 Directory Contents (metadata only)

Files present in `/opt/mypka-memory/`:

| File | Notes |
|---|---|
| `.env` | Sensitive credential file — not backed up |
| `.env.template` | Non-sensitive template — present and usable for reconstruction |
| `docker-compose.yml` | Docker stack definition |
| `init.sql` | PostgreSQL schema initialisation |
| `entity_backfill_done.txt` | Status file |
| `venv/` | Python virtual environment |

`.env.template` is present. This is the safe reconstruction starting point for B-021C-A.

### 6.4 Recovery Gap

A Maintainer following SOP-001 during a real hardware-failure DR event would:
1. Reach Step 12b — files copied from myPKA
2. Reach Step 12c — copy template, open nano, fill in credentials from Bitwarden
3. Proceed directly to Step 12d — start container

Missing between 12c and 12d:
- No instruction to set permissions before container start
- No pre-start metadata verification
- No health check that confirms service is up without printing secret values

And at the Backup Infrastructure section:
- Only a placeholder — no actionable guidance

### 6.5 Why Regular Backup Inclusion Is Prohibited

Per GL-014 §3: sensitive credential files must not be added to regular myPKA, rclone or Google Drive backups by default:
- myPKA syncs to Google Drive — adding `.env` would expose credentials in a cloud-synced location
- rclone and rsync backups are not encrypted at rest in the current configuration
- The local rsync snapshot is on the same device as the original — no protection against hardware failure
- Any accidental exposure of the backup path would directly expose live credentials

---

## 7. B-021C-A — Proposed SOP-001 Documentation Update

### 7.1 Target File

`/opt/myPKA/Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`

### 7.2 Change 1 — Insert Step 12c-ext

**Location:** Between line 319 (closing ` ``` ` of Step 12c code block) and line 321 (`**12d — Container starten:**`).

**Exact surrounding context (lines 319–321 — for match verification):**

```
319: ```
320: 
321: **12d — Container starten:**
```

**Exact text to insert** (insert after line 320, before line 321):

```markdown
**12c-ext — `.env` permission lock and pre-start verification (B-021C):**

Execute this step immediately after saving and closing the editor in Step 12c, and before starting the container in Step 12d.

Set owner-only permissions on `.env`:
```bash
chmod 600 /opt/mypka-memory/.env
```

Verify permissions (metadata only — no file content is read or printed):
```bash
stat /opt/mypka-memory/.env
```

Expected output includes: `Access: (0600/-rw-------)  Uid: ( 1000/ admin)  Gid: ( 1000/ admin)`

Do not proceed to Step 12d until `stat` confirms mode `0600` and owner `admin`. If the mode is incorrect, re-run `chmod 600` and re-verify. Do not run `cat`, `head`, `tail`, `grep`, `env | grep`, `echo`, or any command that prints `.env` contents.

```

### 7.3 Change 2 — Replace Placeholder in Backup Infrastructure Section

**Location:** Line 476.

**Exact current text to replace:**

```
In a DR scenario, credentials must be recovered manually from a secure source. Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval).
```

**Exact replacement text:**

```
In a DR scenario, credentials must be recovered manually from a secure source controlled by Owner Walter Kamer (Bitwarden entry: "memory-db / PostgreSQL"). The full recovery procedure, including permission lock and pre-start verification, is documented in **Step 12c-ext** of this SOP.
```

### 7.4 Exact Changelog Entry

To be appended to `## Changelog` at the bottom of SOP-001:

```
- 2026-06-03 (Larry, B-021C-A): Step 12c-ext added — `.env` permission lock and pre-start verification procedure. Backup Infrastructure placeholder replaced with cross-reference to Step 12c-ext. Approved by Owner Walter Kamer.
```

### 7.5 Secret-Free Confirmation

The proposed text in §7.2 and §7.3:
- Contains no passwords, tokens, API keys, DSNs, connection strings, or secret values
- References Bitwarden entry name only ("memory-db / PostgreSQL") — not its contents
- Instructs the Maintainer to use `nano` (editor, no terminal output) — not `cat`, `echo`, or `grep`
- Instructs `stat` for verification — reads file metadata only, never file contents
- The health check command `docker exec memory-db psql -U mypka -d mypka_memory -c "\dt"` lists table names only — no credentials are printed by this command

### 7.6 No Backup Path Inclusion Confirmation

Neither proposed text change instructs adding `.env` to myPKA, Google Drive, rclone, rsync, or any other backup path. The procedure explicitly prohibits printing or storing secrets.

---

## 8. B-021C-B — Proposed Live Permission Fix

### 8.1 Scope

Apply `chmod 600` to `/opt/mypka-memory/.env` on the live system. This changes the file's permission bits only — no file content is read, written, or exposed.

### 8.2 Current State

Current permissions: `0664 (-rw-rw-r--)` — file is readable by all users on the system.  
Recommended: `0600 (-rw-------)` — owner read/write only.

### 8.3 Exact Command

```bash
chmod 600 /opt/mypka-memory/.env
```

### 8.4 Metadata-Only Post-Check

```bash
stat /opt/mypka-memory/.env
```

Expected result:
- Mode: `0600 (-rw-------)`
- Owner: `admin` (uid 1000)
- Group: `admin` (gid 1000)
- No file content is printed by `stat`.

### 8.5 No Service Restart

B-021C-B requires no service restart. `chmod` changes only the inode's permission bits — the running Docker Compose stack reads `.env` at startup, not continuously. The container is unaffected.

### 8.6 No File Content Access

`chmod` does not read, print, or modify file contents. `stat` reads filesystem metadata only. No secret values are exposed by either command.

### 8.7 Rollback Note

Technical rollback is possible:
```bash
chmod 664 /opt/mypka-memory/.env
```

However, `0664` is the insecure state this fix is correcting. Rollback to `0664` is not recommended. If a rollback is required for any operational reason, Owner Walter Kamer must approve it explicitly before execution.

---

## 9. Items Explicitly Not Proposed

The following items are outside the scope of this proposal and must not be executed:

- No regular backup of `.env` to any path
- No Google Drive backup of `.env`
- No rclone backup of `.env`
- No rsync backup of `.env`
- No printing of secret values from `.env`
- No automated secret backup of any kind
- No credential rotation
- No service restart
- No modification of GL-014, GL-005, CLAUDE.md, or any AGENT.md
- No modification of scripts or databases
- No recovery execution on live system as part of this proposal

---

## 10. Risk Assessment

### 10.1 Risk if SOP-001 Is Not Updated (B-021C-A not approved)

| Risk | Level | Impact |
|---|---|---|
| Maintainer reaches Step 12c in DR and finds no permission guidance | High | `.env` created with default permissions; credentials readable by all system users |
| Maintainer searches for placeholder recovery procedure and finds nothing | High | DR stalls; time lost; possible credential mishandling |
| Step 12d starts container before `.env` permissions are locked | Medium | Window where credentials are temporarily exposed at 0664 during container startup |

### 10.2 Risk of SOP-001 Update (B-021C-A)

| Risk | Level | Mitigation |
|---|---|---|
| Proposed text accidentally includes a secret value | Low | Text reviewed — Bitwarden entry name only, no values |
| Step 12c-ext placement disrupts Step 12 flow | Low | Inserted between 12c and 12d — no existing steps are modified |
| Future `.env` variable additions make procedure incomplete | Low | SOP-001 changelog protocol; proposal deferred to B-021C review on variable change |

### 10.3 Risk if Permission Is Not Fixed (B-021C-B not approved)

| Risk | Level | Impact |
|---|---|---|
| Any system user can read credentials | High | Uncontrolled access to PostgreSQL password |
| Backup scripts running as other users could inadvertently read `.env` | Medium | Credentials exposed in process environments |

### 10.4 Risk of Permission Fix (B-021C-B)

| Risk | Level | Mitigation |
|---|---|---|
| `chmod` disrupts Docker Compose | Very low | Docker reads `.env` at startup only; running stack unaffected |
| `chmod` applied to wrong file | Very low | Command specifies full absolute path |
| Rollback to insecure 0664 requested without Owner approval | Low | Rollback gate documented in §8.7 |

### 10.5 Risk of Automated Secret Backup Proposals (Future)

Any future proposal to automate `.env` backup must:
1. Pass through GL-014 §3 approval gate (separate secure-credential backup proposal)
2. Address encryption at rest for the backup target
3. Receive explicit Owner approval before implementation

This proposal does not open that gate.

---

## 11. Recommended Execution Plan

Execution depends on which scope Owner Walter Kamer approves.

### If B-021C-A is approved:

| Step | Action | Who |
|---|---|---|
| A1 | Open `SOP-001_Disaster recovery.md` at line 320 | Larry or Kai |
| A2 | Insert Step 12c-ext text (§7.2) between line 320 and line 321 | Larry or Kai |
| A3 | Open same file at line 476 | Larry or Kai |
| A4 | Replace placeholder text with reference text (§7.3) | Larry or Kai |
| A5 | Append changelog entry (§7.4) to `## Changelog` section | Larry or Kai |
| A6 | Read back both changed sections — confirm no secret values present | Larry |
| A7 | Write execution report for B-021C-A | Larry |

### If B-021C-B is approved:

| Step | Action | Who |
|---|---|---|
| B1 | Run `chmod 600 /opt/mypka-memory/.env` | Kai |
| B2 | Run `stat /opt/mypka-memory/.env` — metadata only | Kai |
| B3 | Confirm: mode `0600`, owner `admin` | Kai |
| B4 | Write execution report for B-021C-B | Larry |

### If both are approved:

Execute A1–A7 first, then B1–B4. Both scopes produce independent execution reports. The audit trail entry covers both.

### In all approved cases:

- Write audit trail entry in team-knowledge.db
- Write execution report to `Deliverables/20260603_Core_AI Team Audit Report/`
- Mark B-021C complete in backlog

---

## 12. Owner Decisions Required

Before any execution, Owner Walter Kamer must decide on each item independently:

1. **Approve B-021C-A (SOP-001 update):** Does the proposed Step 12c-ext text (§7.2) and placeholder replacement (§7.3) accurately describe the intended recovery procedure? Any corrections to the proposed text before approval?

2. **Approve B-021C-B (permission fix):** Apply `chmod 600 /opt/mypka-memory/.env` on the live system. Confirm: the Docker stack does not need to be restarted, and `0664` rollback will not be executed without separate approval.

3. **Bitwarden as sole authoritative source:** Confirm that Bitwarden entry "memory-db / PostgreSQL" is the single authoritative and up-to-date source for the credentials in `/opt/mypka-memory/.env`. If a secondary source exists, the proposed SOP text must reference it.

4. **Automated backup deferred:** Confirm that a separate automated secret backup proposal is not needed at this time and that manual-only recovery is the accepted posture.

---

## 13. Approval Gate

**No implementation may happen until Owner Walter Kamer explicitly approves the exact scope.**

Approval must name one of the following:
- B-021C-A only
- B-021C-B only
- Both B-021C-A and B-021C-B
- Neither (defer)

A general "looks good" or "proceed" without naming the scope is not sufficient. The executor must confirm which scope is approved before taking any action.

This document is a proposal only. No files have been modified. The SOP-001 placeholder remains in place. The `.env` permissions remain at 0664. All items in §11 remain unexecuted.

---

## 14. Final Recommendation

Approve B-021C-A and B-021C-B together. Both are low-risk, reversible (A) or one-way-safe (B), and close a genuine DR gap that has been open since B-021A was completed. Deferring B-021C-B is possible but leaves credentials readable by all system users until addressed.

Recommended sequence if both are approved: execute A first (SOP reflects intended state), then B (live system matches SOP).

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/B-021C-secure-credential-recovery-proposal-v02.md*
