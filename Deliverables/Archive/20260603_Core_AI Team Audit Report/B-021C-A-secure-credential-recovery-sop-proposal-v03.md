# B-021C-A Secure Credential Recovery SOP-001 Proposal v0.3

**Status:** Proposal only — no implementation  
**Version:** v0.3 (supersedes v0.2)  
**Date:** 2026-06-03  
**Author:** Larry (orchestrator)  
**Backlog item:** B-021C-A  
**Requires approval by:** Owner Walter Kamer — see §12 Approval Gate

---

## 1. Purpose

v0.2 proposed inserting a new `Step 12c-ext` after the existing Step 12c. Owner Walter Kamer rejected that approach: adding an extension step leaves the existing Step 12c in place — a brief, partly Dutch two-liner — creating a fragmented, mixed-language recovery procedure. For a system file that a Maintainer must follow under pressure during disaster recovery, the procedure must be complete, English, and directly usable from a single step.

v0.3 replaces the existing Step 12c in full with a complete English credential recovery procedure. No extension step is added. Step 12d is unchanged.

---

## 2. Governance Basis

| Item | Reference |
|---|---|
| Credential file backup rule | GL-014 §3 — Sensitive credential files must not be added to regular myPKA, rclone or Google Drive backups |
| Recovery is manual-only | GL-014 §3 — Source credentials from a secure external store and re-enter them |
| Recovery procedures must be secret-free | GL-014 §3 — Documented in SOP-001 without including secret values |
| Automated backup requires separate proposal | GL-014 §3 — A separate secure-credential backup proposal is required before any automated credential backup is approved |
| SOP changes require Owner approval | GL-014 §1 — Only after explicit Owner approval |
| System files must be in English | GL-014 §10 — All system files are English |
| No secrets in output or documents | GL-014 §3 — Secrets may never be shown in output or copied to SOPs, Guidelines, or session logs |

---

## 3. Scope

### Included

- Read-only inspection of existing Step 12c, Step 12d, the Backup Infrastructure placeholder, and the SOP-001 changelog section
- Exact replacement text for Step 12c (Change A)
- Exact replacement text for the Backup Infrastructure placeholder (Change B)
- Exact changelog entry (Change C)
- Risk assessment and controlled execution plan

### Excluded

- Execution of any change
- Modification of SOP-001, GL-014, GL-005, CLAUDE.md, AGENT.md files, scripts, or databases
- Any read or exposure of `/opt/mypka-memory/.env` contents
- Service restart, credential rotation, backup or copy of `.env`

---

## 4. Read-Only Investigation Method

SOP-001 (`Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`) was read in full via context-mode batch execution in a prior investigation step (B-021C v0.1 and v0.2 sessions, 2026-06-03). Exact line numbers were confirmed via targeted `grep -n` on non-secret content. No files were modified. No secret values were accessed.

Relevant confirmed locations:

| Location | Line(s) |
|---|---|
| Step 12c — `.env aanmaken` | 315–319 |
| Step 12d — Container starten | 321–327 |
| `### /opt/mypka-memory/.env — Sensitive Credential File` | 472–476 |
| `## Changelog` (last entry) | last line: `2026-06-03 — B-021A: backup infrastructure documentation added.` |

No re-read was required for this proposal. All source text is confirmed from prior indexed content.

---

## 5. Current SOP-001 Issue

### 5.1 Existing Step 12c

Current text (lines 315–319):

```
**12c — .env aanmaken:**
```bash
cp /opt/mypka-memory/.env.template /opt/mypka-memory/.env
nano /opt/mypka-memory/.env   # wachtwoord ophalen uit Bitwarden: "memory-db / PostgreSQL"
```
```

Problems:
1. Header and inline comment are Dutch — violates GL-014 §10 System File Language Rule
2. No permission-setting step after editor save
3. No metadata-only verification step
4. No gate: nothing prevents the Maintainer from proceeding to Step 12d with insecure permissions
5. No explicit prohibition on printing secrets

### 5.2 Why v0.2 Step 12c-ext Was Rejected

v0.2 left the existing Step 12c in place and added Step 12c-ext after it. This creates:
- Two steps where one complete step suffices
- Ambiguity about which step is authoritative
- Continued presence of Dutch text in a system file
- A Maintainer who stops reading after Step 12c would miss the permission gate

### 5.3 Correct Approach

Replace Step 12c in full. The replacement is a single, self-contained English step that a Maintainer can follow start to finish without referencing any other step.

---

## 6. Proposed SOP-001 Changes

### Change A — Replace Step 12c

**Target file:** `/opt/myPKA/Team Knowledge/Core/SOPs/SOP-001_Disaster recovery.md`

**Exact current text to replace (lines 315–319):**

```
**12c — .env aanmaken:**
```bash
cp /opt/mypka-memory/.env.template /opt/mypka-memory/.env
nano /opt/mypka-memory/.env   # wachtwoord ophalen uit Bitwarden: "memory-db / PostgreSQL"
```
```

**Exact replacement text:**

```
**12c — Recreate `.env` and lock permissions (B-021C-A):**

Copy the template to create a fresh `.env`:
```bash
cp /opt/mypka-memory/.env.template /opt/mypka-memory/.env
```

Open `.env` in a local text editor:
```bash
nano /opt/mypka-memory/.env
```

Retrieve the credential values from Bitwarden entry **"memory-db / PostgreSQL"** controlled by Owner Walter Kamer. Fill in all required fields and save the file. Do not print, paste, echo, `cat`, `grep`, or log secret values at any point.

Set owner-only permissions immediately after saving:
```bash
chmod 600 /opt/mypka-memory/.env
```

Verify permissions (metadata only — no file content is read or printed):
```bash
stat /opt/mypka-memory/.env
```

Expected: `Access: (0600/-rw-------)  Uid: ( 1000/ admin)  Gid: ( 1000/ admin)`

Do not proceed to Step 12d until `stat` confirms mode `0600` and owner `admin`. If the mode is incorrect, re-run `chmod 600` and verify again.
```

**Reason:** Replaces a brief Dutch two-liner with a complete, English, self-contained recovery procedure. Eliminates the language violation, adds the permission gate, and removes the need for Step 12c-ext.

---

### Change B — Replace Backup Infrastructure Placeholder

**Target file:** same — `SOP-001_Disaster recovery.md`

**Exact current text to replace (line 476):**

```
In a DR scenario, credentials must be recovered manually from a secure source. Detailed recovery procedure: pending B-021C (not yet executed — requires separate Owner approval).
```

**Exact replacement text:**

```
In a DR scenario, credentials must be recovered manually from a secure source controlled by Owner Walter Kamer (Bitwarden entry: "memory-db / PostgreSQL"). The full recovery procedure, including permission lock and pre-start verification, is documented in **Step 12c** of this SOP.
```

**Reason:** Closes the placeholder. Cross-references Step 12c directly. No secret values included. Confirms Bitwarden as the authoritative source by entry name only.

---

### Change C — Add Changelog Entry

**Location:** Append to `## Changelog` at the bottom of `SOP-001_Disaster recovery.md`.

**Exact entry:**

```
- 2026-06-03 (Larry, B-021C-A): Step 12c fully replaced — complete English credential recovery procedure with permission lock and pre-start verification. Backup Infrastructure placeholder replaced with cross-reference to Step 12c. Approved by Owner Walter Kamer.
```

**Reason:** Per GL-014 §5 changelog protocol: date, agent, backlog ID, description, approval.

---

## 7. Secret-Free Confirmation

The proposed text in Changes A, B, and C:

- Contains no passwords, tokens, API keys, DSNs, connection strings, or secret values
- References Bitwarden entry by name only ("memory-db / PostgreSQL") — not its contents
- Instructs the Maintainer to use `nano` (local editor, no terminal output of secrets)
- Instructs `stat` for verification — reads file metadata only, never file contents
- Prohibits `cat`, `echo`, `grep`, `env | grep`, and any command that prints `.env` contents
- The `chmod 600` command modifies permission bits only — no content access

The health check in Step 12d (`docker exec memory-db psql -U mypka -d mypka_memory -c "\dt"`) lists table names only and prints no credentials. Step 12d is not modified by this proposal.

---

## 8. No Backup Inclusion Confirmation

None of the three proposed changes instruct adding `.env` to myPKA, Google Drive, rclone, rsync, or any other backup path. Change A explicitly prohibits logging secrets. The Backup Infrastructure section continues to state that `.env` is not covered by any regular backup path — Change B does not alter that statement, it only replaces the placeholder at the end of that section.

---

## 9. Risk Assessment

### 9.1 Risk if SOP-001 Is Not Updated

| Risk | Level | Impact |
|---|---|---|
| Maintainer follows Step 12c in DR and creates `.env` with default permissions | High | Credentials readable by all system users until manually corrected |
| Maintainer misses permission gate and starts container at 0664 | High | Window of credential exposure during container startup and operation |
| Dutch text in system file creates ambiguity under GL-014 §10 | Medium | Language inconsistency; future agents may not follow Dutch instructions correctly |
| Placeholder in Backup Infrastructure section provides no DR guidance | Medium | Maintainer has no actionable reference at the point where it matters |

### 9.2 Risk of the Proposed SOP Update

| Risk | Level | Mitigation |
|---|---|---|
| Step 12c replacement disrupts Step 12 flow | Low | Replacement fits the same position; Step 12d unchanged |
| Proposed text accidentally introduces a secret value | None | Text reviewed — Bitwarden entry name only, no values |
| Replacement makes Step 12c longer and harder to follow | Low | Steps are numbered and sequential; no ambiguity introduced |

### 9.3 Risk of Secret Exposure

The proposed text contains no mechanism for secret exposure. All credential handling happens in a local terminal editor session (`nano`) that produces no output to shell history unless the Maintainer explicitly types content at a prompt. The explicit prohibition list (`cat`, `echo`, `grep`, `env | grep`) further reduces accidental exposure risk.

### 9.4 Risk of Future Drift

If the variables inside `/opt/mypka-memory/.env` change, Step 12c as proposed remains valid: it instructs the Maintainer to copy the template and fill values from Bitwarden. The template (`.env.template`) is the authoritative variable list — as long as it is kept current, Step 12c does not need updating when individual values change. Only a structural change to the template or to the Bitwarden entry name would require a SOP-001 update.

---

## 10. Recommended Execution Plan

**After Owner Walter Kamer gives explicit approval for B-021C-A v0.3:**

| Step | Action | Who |
|---|---|---|
| 1 | Open `SOP-001_Disaster recovery.md` at lines 315–319 | Larry or Kai |
| 2 | Replace existing Step 12c text with Change A replacement text (§6, Change A) | Larry or Kai |
| 3 | Open same file at line 476 | Larry or Kai |
| 4 | Replace placeholder with Change B replacement text (§6, Change B) | Larry or Kai |
| 5 | Append Change C changelog entry to `## Changelog` section (§6, Change C) | Larry or Kai |
| 6 | Read back both changed sections — confirm no secret values, no Dutch text remaining | Larry |
| 7 | Write execution report for B-021C-A | Larry |
| 8 | Mark B-021C complete in team_tasks (both A and B scopes done) | Larry |

---

## 11. Owner Decisions Required

Before any execution, Owner Walter Kamer must decide:

1. **Approve Change A (Step 12c replacement):** Does the proposed replacement text accurately and completely describe the intended recovery procedure? Any corrections before approval?

2. **Approve Change B (placeholder replacement):** Does the short cross-reference to Step 12c correctly close the Backup Infrastructure placeholder?

3. **Approve Change C (changelog entry):** Is the changelog wording acceptable?

4. **Confirm Bitwarden as sole authoritative source:** Confirm that Bitwarden entry "memory-db / PostgreSQL" is the single authoritative and up-to-date source for the credentials in `/opt/mypka-memory/.env`.

---

## 12. Approval Gate

**No implementation may happen until Owner Walter Kamer explicitly approves B-021C-A v0.3.**

Approval must name B-021C-A v0.3 explicitly. A general approval of B-021C-A v0.2 does not cover v0.3 — the proposed text has changed.

This document is a proposal only. No files have been modified. SOP-001 is unchanged. All items in §10 remain unexecuted.

---

## 13. Final Recommendation

Approve Changes A, B, and C together. All three are required to fully close B-021C-A: a partial approval (e.g., only Change A without Change B) would leave the Backup Infrastructure placeholder pointing to a non-existent "Step 12c-ext" from v0.2, which was never added.

Recommended sequence if approved: execute A → B → C in a single edit session, then read back both sections, then write the execution report and mark B-021C complete.

---

*Delivered on: 2026-06-03*  
*Delivered at: Deliverables/20260603_Core_AI Team Audit Report/B-021C-A-secure-credential-recovery-sop-proposal-v03.md*
