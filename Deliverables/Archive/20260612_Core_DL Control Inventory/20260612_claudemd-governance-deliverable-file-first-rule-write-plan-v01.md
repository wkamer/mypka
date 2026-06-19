# CLAUDE.md Amendment Write Plan: Governance Deliverable File-First Rule

**Version:** v01
**Date:** 2026-06-12
**Author:** Governance Assistant
**Status:** Write plan, awaiting Owner authorization before execution
**Source proposal:** Deliverables/20260612_Core_DL Control Inventory/20260612_claudemd-governance-deliverable-file-first-rule-proposal-v01.md
**Required execution report:** Deliverables/20260612_Core_DL Control Inventory/20260612_claudemd-governance-deliverable-file-first-rule-execution-report-v01.md

---

## 1. Target File

`/opt/myPKA/CLAUDE.md`

One file. One edit. No other files are touched.

---

## 2. Insertion Point

The new rule section is inserted immediately after the Execution Persistence Rule section
and immediately before the Google, Sheets and Email section.

The exact anchor text that must be present at the insertion point is:

```
5. If execution completes without a persisted execution report, the next action before
   any further work is to repair the audit trail.

### Google, Sheets & Email
```

If this anchor text is not found verbatim, execution stops. No edit is made. Stop
condition SC-1 applies.

---

## 3. Exact Text to Insert

The following block is inserted between the Execution Persistence Rule and the Google,
Sheets and Email section. The block starts with a blank line after the anchor, adds the
new section, and leaves a blank line before `### Google, Sheets & Email`.

```
### Governance Deliverable File-First Rule

For every governance deliverable produced during a session: the content must be written
to a file before or at the same time as it is presented to the Owner for review or
approval.

A governance deliverable is any output that:
- presents a proposal, operating model, assessment, or decision record for Owner review,
- will be referenced in a subsequent execution step (write plan, archive action, database
  update, CLAUDE.md edit, SOP or GL change), or
- classifies artifacts, defines categories, or establishes rules that govern future
  team behavior.

**File location:** apply GL-017 Granularity Gate first.
- If G1: create a new D-folder, register in deliverable_lifecycle, write the file inside.
- If G2: write the file inside the most relevant existing D-folder. No new folder needed.

**Write authorization — GL-021 not overridden:** this rule does not override GL-021.
Writing a governance deliverable to a file is a write action and requires Owner
authorization before the file is written.

Standard sequence when producing a governance deliverable:
1. Claude determines the output is a governance deliverable and identifies the target
   file path (via the GL-017 gate above).
2. Claude presents a minimal file-write proposal: proposed file path and one-line
   description of the content. Claude does not output the full governance deliverable
   content in chat at this step.
3. Claude asks for Owner authorization of the exact file write path.
4. After Owner authorizes: Claude writes the governance deliverable to that file and
   responds in chat with a short confirmation and the exact file path only.

Exception: if the Owner's prompt already explicitly authorized the exact target file
path (for example, "write it to X" or by specifying the path in the task brief), Claude
may write directly without a separate authorization step. A general instruction to
produce a deliverable is not explicit authorization of a specific file path.

**Chat output:** a short confirmation (title, file path, one-line description) is
sufficient chat output after the file is written. The full governance content must be
in the file, not in chat.

**Waiver:** Owner may explicitly instruct chat-only delivery for a specific deliverable.
State the waiver in chat before producing the output. No standing waiver applies.

**Violation trigger:** if Claude produces governance deliverable content in chat without a
corresponding persisted file, the next action before any further work is to write the
file and confirm the path to the Owner. Governance decisions made on chat-only content
are not considered authorized until the file exists.
```

---

## 4. Preflight Checks

All preflight checks must pass before the edit is made. If any check fails, execution
stops and the failure is reported to Owner.

| ID | Check | Pass condition |
|---|---|---|
| PF-1 | CLAUDE.md exists at `/opt/myPKA/CLAUDE.md` | File is readable |
| PF-2 | Anchor text present | Exact anchor string from Section 2 found verbatim |
| PF-3 | No existing Governance Deliverable File-First Rule section | Grep for "Governance Deliverable File-First Rule" returns no match |
| PF-4 | Execution Persistence Rule section present | Grep for "### Execution Persistence Rule" returns exactly one match |
| PF-5 | Google section present after anchor | Grep for "### Google, Sheets" returns a match after the anchor |
| PF-6 | Proposal file exists | Source proposal file readable at the path in the header |

---

## 5. Edit Action

One Edit operation. Tool: Edit (not Write, not Bash sed).

**old_string (exact, verbatim):**
```
5. If execution completes without a persisted execution report, the next action before
   any further work is to repair the audit trail.

### Google, Sheets & Email
```

**new_string (exact, verbatim):**
```
5. If execution completes without a persisted execution report, the next action before
   any further work is to repair the audit trail.

### Governance Deliverable File-First Rule

For every governance deliverable produced during a session: the content must be written
to a file before or at the same time as it is presented to the Owner for review or
approval.

A governance deliverable is any output that:
- presents a proposal, operating model, assessment, or decision record for Owner review,
- will be referenced in a subsequent execution step (write plan, archive action, database
  update, CLAUDE.md edit, SOP or GL change), or
- classifies artifacts, defines categories, or establishes rules that govern future
  team behavior.

**File location:** apply GL-017 Granularity Gate first.
- If G1: create a new D-folder, register in deliverable_lifecycle, write the file inside.
- If G2: write the file inside the most relevant existing D-folder. No new folder needed.

**Write authorization — GL-021 not overridden:** this rule does not override GL-021.
Writing a governance deliverable to a file is a write action and requires Owner
authorization before the file is written.

Standard sequence when producing a governance deliverable:
1. Claude determines the output is a governance deliverable and identifies the target
   file path (via the GL-017 gate above).
2. Claude presents a minimal file-write proposal: proposed file path and one-line
   description of the content. Claude does not output the full governance deliverable
   content in chat at this step.
3. Claude asks for Owner authorization of the exact file write path.
4. After Owner authorizes: Claude writes the governance deliverable to that file and
   responds in chat with a short confirmation and the exact file path only.

Exception: if the Owner's prompt already explicitly authorized the exact target file
path (for example, "write it to X" or by specifying the path in the task brief), Claude
may write directly without a separate authorization step. A general instruction to
produce a deliverable is not explicit authorization of a specific file path.

**Chat output:** a short confirmation (title, file path, one-line description) is
sufficient chat output after the file is written. The full governance content must be
in the file, not in chat.

**Waiver:** Owner may explicitly instruct chat-only delivery for a specific deliverable.
State the waiver in chat before producing the output. No standing waiver applies.

**Violation trigger:** if Claude produces governance deliverable content in chat without a
corresponding persisted file, the next action before any further work is to write the
file and confirm the path to the Owner. Governance decisions made on chat-only content
are not considered authorized until the file exists.

### Google, Sheets & Email
```

---

## 6. Verification Steps After Edit

All verification steps run after the edit. Failures are reported in the execution report.

| ID | Check | Method | Pass condition |
|---|---|---|---|
| V-1 | New section present | Grep CLAUDE.md for "Governance Deliverable File-First Rule" | Exactly one match |
| V-2 | Insertion point correct | Grep for context: "repair the audit trail" followed within 5 lines by "Governance Deliverable File-First Rule" | Match found |
| V-3 | Google section still present | Grep for "### Google, Sheets & Email" | Match still present |
| V-4 | Execution Persistence Rule intact | Grep for "### Execution Persistence Rule" | Exactly one match |
| V-5 | No duplicate sections | Grep for "File-First Rule" | Exactly one match |
| V-6 | CLAUDE.md line count increased | Line count after edit exceeds line count before edit | True |

---

## 7. Required Execution Report

Immediately after the edit completes and verification passes, write the execution report to:

`Deliverables/20260612_Core_DL Control Inventory/20260612_claudemd-governance-deliverable-file-first-rule-execution-report-v01.md`

The execution report must include: preflight results per check, edit action taken,
verification results per check, final CLAUDE.md line count before and after, timestamp,
and any deviations from this write plan.

If the execution report cannot be written, report the failure to Owner before closing
the session.

---

## 8. Stop Conditions

| ID | Condition | Action |
|---|---|---|
| SC-1 | Anchor text not found verbatim in CLAUDE.md | Stop. Report to Owner. Do not edit. |
| SC-2 | "Governance Deliverable File-First Rule" already present in CLAUDE.md | Stop. Report to Owner. Possible prior partial edit. |
| SC-3 | Any preflight check fails | Stop. Report which check failed. Do not edit. |
| SC-4 | Edit tool returns an error | Stop. Do not retry. Report to Owner. |
| SC-5 | Any verification check fails after edit | Report failure. Do not attempt rollback without Owner instruction. |

---

## 9. Explicit Non-Actions

The following actions do not happen during execution of this write plan, even if they
appear related:

- No changes to any file other than CLAUDE.md.
- No changes to any section of CLAUDE.md other than the single insertion described here.
- No database updates.
- No deliverable_lifecycle rows inserted or updated.
- No D-folder creation.
- No archive actions.
- No Batch 2 work.
- No dashboard work.
- No GL-013 resolution.
- No routing.
- No Learning Candidate triage.
- No Deliverable Lifecycle sweep.
- No team_tasks updates during execution (the execution report is a file, not a DB row).

---

**Delivered on:** 2026-06-12
**Delivered at:** Deliverables/20260612_Core_DL Control Inventory/20260612_claudemd-governance-deliverable-file-first-rule-write-plan-v01.md
