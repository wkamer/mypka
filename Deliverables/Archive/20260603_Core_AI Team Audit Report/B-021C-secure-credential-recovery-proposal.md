# B-021C Secure Credential Recovery Procedure Proposal

**Status:** Proposal only — no implementation  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Backlog item:** B-021C  
**Requires approval by:** Owner Walter Kamer before any execution

---

## 1. Purpose

GL-014 §3 (Credential file backup rule, added in B-030A) mandates that recovery procedures for specific credential files be documented in SOP-001 Disaster Recovery without including secret values. SOP-001 currently contains a placeholder for this procedure: "Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval)."

This proposal delivers the content to replace that placeholder: a safe, secret-free manual recovery procedure for `/opt/mypka-memory/.env`, together with an exact SOP-001 update text and a secondary finding on file permissions.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Credential file backup rule | GL-014 §3 — Sensitive credential files must not be added to regular myPKA, rclone or Google Drive backups |
| Recovery is manual-only | GL-014 §3 — Source credentials from a secure external store and re-enter them |
| Recovery procedures must be secret-free | GL-014 §3 — Documented in SOP-001 without including secret values |
| Automated backup requires separate approval | GL-014 §3 — A separate secure-credential backup proposal is required before any automated credential backup is approved |
| SOP changes require Owner approval | GL-014 §1 — Only after explicit Owner approval |
| Reviewers for SOP changes | GL-014 §9 — Executor: domain specialist; Reviewer: Larry; Final approval: Owner |
| No secrets in output | GL-014 §3 — Secrets, tokens, API keys, encryption keys and passwords may never be shown in output |
| No secrets in SOPs, GLs, or Workstreams | GL-014 §3 — Secrets may not be copied to session logs, team_log, agent journals, SOPs, Guidelines or Workstreams |

---

## 3. Scope

### Included

- Read-only investigation of GL-014 §3 and SOP-001 current content
- Metadata-only inspection of `/opt/mypka-memory/.env` (existence, path, permissions, size, timestamps — no secret values)
- Proposed exact replacement text for the SOP-001 placeholder under `### /opt/mypka-memory/.env — Sensitive Credential File`
- Secondary finding: current file permissions on `.env` are world-readable (0664); proposed correction to 0600
- Assessment of whether an additional automated secret backup proposal is needed
- Risk assessment

### Excluded

- Execution of any file change
- Reading, printing, or exposing any secret value
- Modification of GL-014, GL-005, AGENT.md files, CLAUDE.md, scripts, or databases
- Credential rotation
- Service restart
- Backup of `.env` to any path

---

## 4. Read-Only Investigation Method

All investigation was performed without accessing secret values:

1. **GL-014** was read in full via context-mode batch execution. §3 was extracted and searched.
2. **SOP-001** path was first located via `find` (case-sensitive mismatch: `_Disaster recovery.md` not `_Disaster Recovery.md`). File was then read in full via context-mode batch execution.
3. **`/opt/mypka-memory/.env`** was inspected using `stat` only — file existence, path, size, permissions, owner, group, and timestamps. No content was read, printed, or summarized.
4. **`/opt/mypka-memory/` directory** was listed using `ls -la` — filenames and metadata only. No file contents were accessed.
5. **Systemd services** were listed using `find /etc/systemd/system` — service names only, no content.
6. No `cat`, `less`, `head`, `tail`, `grep`, `awk`, `sed`, or any content-reading command was run against `.env`.

---

## 5. Current State

### 5.1 SOP-001 Current Coverage

SOP-001 (`Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`) contains:

- **Step 12 — Unified Memory Core (Pi / Linux only):** Full setup procedure for the memory-db stack, including step 12c which instructs the Maintainer to copy `.env.template` to `.env` and fill in the PostgreSQL password retrieved from Bitwarden ("memory-db / PostgreSQL"). This step exists and is correct.
- **Section `### /opt/mypka-memory/.env — Sensitive Credential File`** under `## Backup Infrastructure (B-001)`: Correctly states that the file is not covered by regular backups. Ends with: "Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval)." This placeholder is the recovery gap B-021C closes.
- **`## Key Credentials Reference` table:** Lists `memory-db PostgreSQL` with source as Bitwarden: "memory-db / PostgreSQL".
- **Changelog:** Last entry is `2026-06-03 — B-021A: backup infrastructure documentation added.`

### 5.2 `/opt/mypka-memory/.env` Metadata

| Property | Value |
|---|---|
| Path | `/opt/mypka-memory/.env` |
| Status | Exists |
| Size | 339 bytes |
| Permissions | 0664 (-rw-rw-r--) |
| Owner | admin (uid 1000) |
| Group | admin (gid 1000) |
| Modified | 2026-05-20 23:15 |

**Secondary finding — permissions:** 0664 means the file is readable and writable by the `admin` group, and readable by all other users on the system. For a credential file this is overly permissive. The recommended permission for a credential file is 0600 (owner read/write only). This is a separate finding; the permission fix is listed under Owner Decisions Required (§11).

### 5.3 Directory Contents

Files present in `/opt/mypka-memory/`:

| File | Notes |
|---|---|
| `.env` | Sensitive credential file — not backed up |
| `.env.template` | Non-sensitive template — used for reconstruction |
| `docker-compose.yml` | Docker stack definition |
| `init.sql` | PostgreSQL schema initialisation |
| `entity_backfill_done.txt` | Status file |
| `venv/` | Python virtual environment |

The `.env.template` file is the safe reconstruction starting point. It is present in the same directory.

### 5.4 Current Recovery Gap

If the Raspberry Pi hardware fails:
- `myPKA` is recovered from Google Drive via rclone (Step 1 of SOP-001)
- Step 12 of SOP-001 covers full memory-db rebuild
- However, the `.env` recovery within Step 12 (step 12c) only says: fill in the password from Bitwarden — without specifying the exact variables to set, the permissions to apply, or the validation steps to confirm service health without printing secrets
- The placeholder in the Backup Infrastructure section provides no guidance at all
- Result: a Maintainer performing DR would need to infer the recovery procedure from scattered context

### 5.5 Why Regular Backup Inclusion is Prohibited

Per GL-014 §3: sensitive credential files must not be added to regular myPKA, rclone or Google Drive backups by default. Reasons:
1. myPKA is synced to Google Drive — adding `.env` would expose credentials in a cloud-synced location accessible from multiple devices
2. rclone backup outputs are not encrypted at rest in the current configuration
3. The local rsync snapshot is on the same device as the original — no protection against hardware failure
4. Any accidental exposure of the backup path would directly expose live credentials

---

## 6. Proposed SOP-001 Update

### 6.1 Target File

`/opt/myPKA/Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`

### 6.2 Exact Insertion Location

Inside section `### /opt/mypka-memory/.env — Sensitive Credential File` under `## Backup Infrastructure (B-001)`.

**Current text to replace** (the last line of that section):

```
In a DR scenario, credentials must be recovered manually from a secure source. Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval).
```

**Replace with** the text in §6.3 below.

### 6.3 Exact Proposed Text

```markdown
In a DR scenario, credentials must be recovered manually from a secure source controlled by Owner Walter Kamer. See the full recovery procedure in **Step 12c-ext** below.

**Step 12c-ext — `.env` Manual Recovery (B-021C)**

This step replaces the placeholder in Step 12c. Execute during Step 12 of a full DR restore, after completing step 12b (files copied from myPKA) and before step 12d (container start).

**Prerequisites:**
- Access to the secure external store (Bitwarden, vault entry: "memory-db / PostgreSQL")
- `.env.template` already copied to `/opt/mypka-memory/` (completed in step 12b)
- No container running yet

**Recovery steps:**

1. Open Bitwarden and locate the entry "memory-db / PostgreSQL". Keep it open in a separate window — do not paste secret values into any chat, log, or document.

2. Copy `.env.template` to `.env` if not already present:
   ```bash
   cp /opt/mypka-memory/.env.template /opt/mypka-memory/.env
   ```

3. Open `.env` in a terminal text editor and fill in the values using the credentials from Bitwarden:
   ```bash
   nano /opt/mypka-memory/.env
   ```
   Do not print `.env` contents to terminal at any point.

4. Set safe permissions immediately after saving:
   ```bash
   chmod 600 /opt/mypka-memory/.env
   ```
   Verify permissions:
   ```bash
   stat /opt/mypka-memory/.env
   ```
   Expected: `0600 (-rw-------)`, owner `admin`.

5. Proceed to step 12d — start the Docker Compose stack:
   ```bash
   cd /opt/mypka-memory
   docker compose --env-file .env up -d
   ```

6. Validate service health without printing secrets:
   ```bash
   docker exec memory-db psql -U mypka -d mypka_memory -c "\dt"
   ```
   Expected: 5 tables listed (`tool_logs`, `memory_summaries`, `conversational_memory`, `memory_entities`, `memory_knowledge`). No password is printed by this command.

7. Verify the Python venv can connect:
   ```bash
   /opt/mypka-memory/venv/bin/python3 -c "
   import sys, os
   sys.path.insert(0, '/opt/myPKA/Team Knowledge/Core/Integrations/memory-db')
   from memory_config import get_dsn
   os.environ['MEMORY_DB_DSN'] = get_dsn()
   from memory_manager import get_manager
   mm = get_manager()
   print('Memory service: OK')
   "
   ```
   Expected output: `Memory service: OK`. If connection fails, verify `.env` values against Bitwarden before debugging further.

**What `.env` must not contain after recovery:**
- Printed in terminal history (`cat .env`, `echo`, `env | grep`)
- Copied into any myPKA file, session log, or chat output
- Added to any backup path

Continue with steps 12e and beyond as documented.
```

### 6.4 Exact Changelog Entry

```markdown
- 2026-06-03 (Larry, B-021C): Step 12c-ext added — manual recovery procedure for `/opt/mypka-memory/.env`. Approved by Owner Walter Kamer.
```

### 6.5 Confirmation: No Secret Values

The proposed text contains no secret values, no API keys, no passwords, and no tokens. All credential references point to Bitwarden by entry name only. The command in step 7 reads DSN via `memory_config.get_dsn()` which reads from `.env` at runtime — it does not print the DSN.

### 6.6 Confirmation: `.env` Not Added to Any Regular Backup

The proposed text contains no instruction to copy `.env` to myPKA, Google Drive, rclone, or any rsync path. The procedure explicitly prohibits it.

---

## 7. Manual Recovery Procedure (Summary)

This is the high-level procedure referenced by the SOP-001 update. Full detail is in §6.3.

1. **Identify required credential sources:** The `.env` file contains the PostgreSQL credentials for the `mypka` database user and the connection DSN for the memory-db service. The authoritative source is Bitwarden, vault entry "memory-db / PostgreSQL", controlled by Owner Walter Kamer.

2. **Retrieve credentials from the secure external store:** Open Bitwarden on a trusted device. Do not share or log the values.

3. **Recreate `/opt/mypka-memory/.env` manually:** Copy `.env.template` to `.env`. Fill in credential fields using values from Bitwarden in a local text editor. Do not print `.env` to terminal.

4. **Set safe permissions and ownership:**
   ```bash
   chmod 600 /opt/mypka-memory/.env
   ```
   Expected after: `0600 (-rw-------)`, owner `admin`.

5. **Restart the memory service only after credentials are restored:** Run `docker compose --env-file .env up -d` from `/opt/mypka-memory/`. Do not start the container before `.env` is complete.

6. **Confirm service health without printing secrets:** Run `docker exec memory-db psql -U mypka -d mypka_memory -c "\dt"` — expected: 5 tables. Run the Python venv connectivity check from §6.3 step 7 — expected: `Memory service: OK`.

---

## 8. Items Explicitly Not Proposed

The following items are outside the scope of this proposal and must not be executed:

- No regular backup of `.env` to any path
- No Google Drive backup of `.env`
- No rclone backup of `.env`
- No rsync backup of `.env`
- No printing of secret values from `.env`
- No automated secret backup of any kind
- No credential rotation
- No service restart as part of this proposal
- No modification of GL-014, GL-005, CLAUDE.md, or any AGENT.md
- No modification of scripts or databases
- No recovery execution

---

## 9. Risk Assessment

### 9.1 Risk if SOP-001 is Not Updated

| Risk | Level | Impact |
|---|---|---|
| Maintainer performs DR without documented `.env` recovery | High | Memory service cannot start; UMC unavailable until credentials are manually located |
| Maintainer searches for credentials in the wrong location | Medium | Delay; possible failed DR |
| Maintainer attempts to copy `.env` from backup that does not exist | Medium | Unnecessary troubleshooting time |

**Assessment:** The placeholder in SOP-001 is insufficient. A Maintainer following the current SOP during a real DR event would reach step 12c and have no recovery procedure beyond "use Bitwarden" — with no guidance on variables, permissions, or health validation. Updating SOP-001 is low-risk and high-value.

### 9.2 Risk of Manual Recovery Documentation

| Risk | Level | Mitigation |
|---|---|---|
| Documentation becomes outdated if `.env` variables change | Low | SOP-001 changelog protocol; B-021C to be re-reviewed on variable change |
| Documentation is too verbose and causes confusion | Low | Proposal uses numbered steps matching existing SOP style |
| Maintainer skips permission step | Low | Step 4 is explicit; `stat` command confirms before proceeding |

### 9.3 Risk of Accidentally Exposing Secrets

The proposed text uses Bitwarden entry names only. No secret value appears in any file, chat, or log produced by this proposal. Risks mitigated by:
- Explicit prohibition in step instructions ("do not print")
- No `cat .env` or `echo` instructions
- Health check uses schema query, not credential query

### 9.4 Risk of Future Automated Secret Backup Proposals

Any future proposal to automate `.env` backup must:
1. Pass through GL-014 §3 approval gate (separate secure-credential backup proposal)
2. Address encryption at rest for the backup target
3. Receive explicit Owner approval before implementation

This proposal does not open that gate. It explicitly defers automated backup to a separate future proposal.

---

## 10. Recommended Execution Plan

**After Owner Walter Kamer gives explicit approval:**

| Step | Action | Who | Note |
|---|---|---|---|
| 1 | Open SOP-001 at insertion location (§6.2) | Kai or Larry | Read current text to confirm match |
| 2 | Replace placeholder line with proposed text (§6.3) | Kai or Larry | No other changes to SOP-001 |
| 3 | Append changelog entry (§6.4) to SOP-001 `## Changelog` section | Kai or Larry | |
| 4 | Read back modified section to confirm no secret values and no backup instructions slipped in | Larry | |
| 5 | Apply permissions fix to live `.env`: `chmod 600 /opt/mypka-memory/.env` | Kai | Secondary finding from §5.2 — requires separate Owner approval (see §11 item 2) |
| 6 | Confirm B-021C complete in backlog | Larry | |

Steps 1–4 and step 5 are independent; step 5 requires a separate Owner decision (see §11).

---

## 11. Owner Decisions Required

Before any execution, Owner Walter Kamer must decide:

1. **Approve proposed SOP-001 update text (§6.3):** Does the proposed Step 12c-ext text accurately describe the intended recovery procedure? Are there credential sources or variables missing?

2. **Approve permissions fix:** Current `.env` permissions are 0664 (readable by all users on the system). Proposed: `chmod 600` (owner-only). This is a separate change from the SOP text update. Approve or defer?

3. **Bitwarden as sole authoritative source:** Confirm that Bitwarden vault entry "memory-db / PostgreSQL" is the single authoritative and up-to-date source for these credentials. If a secondary source exists, the SOP text should reference it.

4. **Automated backup deferral confirmed:** Confirm that a separate automated secret backup proposal is not needed at this time, and that manual-only recovery is acceptable as the current posture.

---

## 12. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This document is a proposal only. It contains no executed changes. All items in §10 remain unexecuted. The SOP-001 placeholder ("pending B-021C") remains in place until the Owner approves and execution is confirmed.

Approval trigger: Owner says "akkoord" or "go" on this proposal, or approves specific items from §11.

---

## 13. Final Recommendation

**Recommended next step:** Owner Walter Kamer reviews this proposal and provides decisions on the four items in §11. Upon approval, execute steps 1–4 of §10 (SOP-001 update) and separately confirm or defer step 5 (permissions fix).

The SOP-001 update is low-risk, fully reversible, and closes a genuine DR gap. The permissions fix is a separate security improvement that can be executed independently. No automated backup is proposed at this time.

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/B-021C-secure-credential-recovery-proposal.md*
