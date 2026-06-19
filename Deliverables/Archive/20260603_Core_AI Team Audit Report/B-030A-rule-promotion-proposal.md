# B-030A Rule Promotion Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**
**Based on:** B-030 Graduation Candidate Triage Proposal (2026-06-03)

---

## 1. Purpose

Two graduation candidates from the B-021 audit were triaged in B-030 and accepted as structural team rules. This proposal defines the exact implementation path for each:

- **Candidate 1** (Sensitive credential file handling rule) — destination confirmed: GL-014 §3 extension. Exact insertion text and changelog entry are provided here for Owner review and approval.
- **Candidate 2** (Investigation-before-fix rule) — destination proposed: GL-005 Diagnostic Discipline. However, GL-005 is currently written in Dutch, which requires a destination decision before implementation. Three options are presented with a clear recommendation.

This proposal is documentation-only and proposal-only. No files are modified. No GL changes are executed.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| No implementation without Owner's explicit approval | GL-014 v1.2 §1 |
| Guidelines are critical files — may never be modified without Owner approval | GL-014 v1.2 §8 |
| Guideline executor: Larry/Nolan. Reviewer: Larry. Final approval: Owner | GL-014 v1.2 §9 |
| All system files must be written in English | GL-014 v1.2 §10 |
| Every GL change includes a changelog entry | GL-014 v1.2 §5 |
| Audit trail: changelog in file, team_log entry, session log | GL-014 v1.2 §6 |
| No secret values may be written in any deliverable, SOP, GL or Workstream | GL-014 v1.2 §3 |

---

## 3. Scope

**Included:**
- Exact insertion text for GL-014 §3 (Candidate 1)
- Exact proposed rule text for GL-005 (Candidate 2)
- Three implementation options for Candidate 2, with risk assessment
- Sequencing recommendation

**Excluded:**
- Execution of any GL modification
- Translation of GL-005
- Any change to AGENT.md files, SOPs, CLAUDE.md, or databases
- Registration of new backlog items
- B-021B or B-021C execution

---

## 4. Candidate 1 — GL-014 §3 Extension Proposal

### 4.1 Target file

`Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md`

### 4.2 Exact insertion location

Insert after the last existing bullet in §3 (`When in doubt: stop and escalate to Owner directly.`) and before the `---` separator that follows §3.

**Current §3 content (lines 81–92):**

```markdown
## 3. Secret handling

Rules:

- Secrets, tokens, API keys, encryption keys and passwords may never be shown in output.
- Secrets may not be copied to session logs, team_log, agent journals, SOPs, Guidelines or Workstreams.
- Agents may only report whether a secret exists and where it is securely stored.
- `.env`, `rclone.conf`, credentials and private keys are always critical files.
- Changes to secrets require Owner's explicit approval and technical review by Kai.
- When in doubt: stop and escalate to Owner directly.

---
```

**After insertion, §3 would read:**

```markdown
## 3. Secret handling

Rules:

- Secrets, tokens, API keys, encryption keys and passwords may never be shown in output.
- Secrets may not be copied to session logs, team_log, agent journals, SOPs, Guidelines or Workstreams.
- Agents may only report whether a secret exists and where it is securely stored.
- `.env`, `rclone.conf`, credentials and private keys are always critical files.
- Changes to secrets require Owner's explicit approval and technical review by Kai.
- When in doubt: stop and escalate to Owner directly.

**Credential file backup rule:**
Sensitive credential files (`.env`, `rclone.conf`, private keys, OAuth tokens) must not be
added to regular myPKA, rclone or Google Drive backups by default. If a credential file is
lost on hardware failure, recovery is manual-only: source the credentials from a secure
external store and re-enter them.

Recovery procedures for specific credential files must be documented in SOP-001 Disaster
Recovery without including secret values. A separate secure-credential backup proposal is
required before any automated credential backup is approved.

---
```

### 4.3 Exact rule text

```
**Credential file backup rule:**
Sensitive credential files (`.env`, `rclone.conf`, private keys, OAuth tokens) must not be
added to regular myPKA, rclone or Google Drive backups by default. If a credential file is
lost on hardware failure, recovery is manual-only: source the credentials from a secure
external store and re-enter them.

Recovery procedures for specific credential files must be documented in SOP-001 Disaster
Recovery without including secret values. A separate secure-credential backup proposal is
required before any automated credential backup is approved.
```

### 4.4 Exact changelog entry

To be appended to the existing GL-014 `## Changelog` section at the bottom of the file:

```
- 2026-06-03 (Larry, B-030A): Credential file backup rule added to §3 Secret handling.
  Graduated from B-021 audit finding. Approved by Owner Walter Kamer.
```

### 4.5 Risk assessment

| Aspect | Assessment |
|---|---|
| Change type | Additive — no existing rules removed or modified |
| Scope | §3 only — no other section affected |
| Agent behavior impact | None — this is a governance rule, not an agent behavioral instruction. Agents already comply with it in practice (B-021A execution confirmed). |
| Content risk | Low — the rule describes the status quo confirmed in B-021A. It formalizes what was already done. |
| Secret risk | None — the rule explicitly prohibits secret values; no secrets are written in this proposal or in the GL addition. |
| Overall risk | Low |

### 4.6 Post-checks

After execution:
1. Read back GL-014 §3 — confirm the credential file backup rule is present and correctly placed
2. Confirm the `---` separator between §3 and §4 is still in place
3. Confirm the changelog entry is appended at the bottom of the file
4. Confirm no secret values appear anywhere in the file

### 4.7 Confirmation — no secret values

The proposed rule text does not contain any secret values, passwords, tokens, API keys or credentials. It references where credentials are stored conceptually (a secure external store) without naming specific values. GL-014 itself does not and will not contain any secrets.

---

## 5. Candidate 2 — GL-005 Destination Decision

### 5.1 Why the rule is structural

The investigation-before-fix rule emerged from a specific finding (mypka-backup.log is 0 bytes — cause unknown, fix deferred). But the principle applies to any instance of unexpected infrastructure behavior: an empty log, an absent output, a script that runs but produces nothing, a service that does not respond. The temptation to immediately propose or apply a fix without confirming the cause is a recurring risk in infrastructure work. The rule is not tied to the specific log file — it is a standing engineering discipline.

### 5.2 Why GL-005 is the likely home

GL-005 is the AI Engineering Operating System. Its scope is "volledig AI team" (full AI team). Its Development rules section already prohibits "productie aanpassen zonder validatie" and "aannames presenteren als feiten" — principles that are adjacent to, but do not cover, the specific case of investigating before fixing.

GL-005 is where the team's engineering operating rules live. The investigation-before-fix rule belongs in that layer: it is a general engineering discipline, not a governance rule (GL-014), not a procedure (SOP), and not agent-specific (AGENT.md). A standalone GL for a single rule is possible but fragments the engineering OS unnecessarily.

### 5.3 Language compliance issue

GL-005 is currently written entirely in Dutch. GL-014 v1.2 §10 requires all system files, including Guidelines, to be written in English.

Adding an English section to a Dutch GL-005 would create a bilingual system file. This is inconsistent with GL-014 §10 and with the approach taken in B-026 through B-029, where Dutch content in system files was systematically translated to English.

This does not block the rule from being correct or valuable. It creates a compliance dependency that must be resolved before or alongside promotion.

### 5.4 Options

#### Option A — Add English Diagnostic Discipline section to current Dutch GL-005

**What it means:** Add the new English section directly to GL-005 as it stands today, without translating the existing Dutch content. GL-005 would contain Dutch sections (existing) and one English section (new).

**Advantage:** Fastest path to making the rule active. The rule is available immediately.

**Risk:**
- Creates a bilingual system file — explicitly inconsistent with GL-014 §10
- Sets a precedent: agents reading GL-005 encounter a mixed-language document
- Future additions would face the same dilemma: Dutch or English?
- The bilingual state accumulates technical debt

**Risk level:** Low for the rule itself; medium for governance compliance.

**Recommended for:** When the rule is urgently needed and GL-005 translation cannot wait.

---

#### Option B — Translate GL-005 fully to English first, then add the rule

**What it means:** Commission a full GL-005 English translation (following the same approach as B-028 for GL-014) as a prerequisite. After translation is complete and approved, add the Diagnostic Discipline section to the fully English GL-005.

**Advantage:**
- GL-005 becomes fully compliant with GL-014 §10
- The new rule integrates cleanly into an all-English document
- No bilingual state is introduced
- Consistent with the audit-phase approach: B-028 translated GL-014, this would do the same for GL-005

**Risk:**
- Adds one preparation step before the rule is active
- GL-005 translation is a bounded task (183 lines, no behavioral logic — only Dutch engineering principles that translate cleanly)
- Both steps require separate Owner approvals

**Risk level:** Low. Translation of GL-005 is similar in scope to B-026/B-028 — a clean Dutch-to-English pass with no functional changes.

**Recommended for:** When the audit-phase approach is to maintain full language compliance at each step.

---

#### Option C — Create a standalone English GL for Diagnostic Discipline

**What it means:** Create a new `GL-015_Diagnostic Discipline.md` (or the next available number) containing the investigation-before-fix rule and any related diagnostic principles. GL-005 is not modified. GL-015 is fully English from creation.

**Advantage:**
- Completely avoids the GL-005 language issue
- New GL is immediately English-compliant
- No dependency on GL-005 translation
- Can be created and approved independently

**Risk:**
- Fragments the engineering OS: a core engineering discipline would live outside GL-005
- Agents doing technical work must now consult both GL-005 and GL-015 for engineering rules
- Long-term: likely to be merged into GL-005 anyway when GL-005 is eventually translated
- Adds a GL file for content that naturally belongs in the existing engineering OS

**Risk level:** Low for compliance; medium for system coherence.

**Recommended for:** When Option B's translation prerequisite is not acceptable and Option A's bilingual state is also not acceptable. A valid fallback.

---

### 5.5 Recommendation

**Option B — Translate GL-005 to English first, then add the rule.**

Rationale: GL-005 is short (183 lines), fully Dutch, and already non-compliant with GL-014 §10. Translating it is a bounded, audit-consistent task. Once translated, the Diagnostic Discipline section integrates cleanly. This is the same path taken for GL-014 (B-028), which produced v1.2 — a clean, fully English governance document. GL-005 deserves the same treatment.

The investigation-before-fix rule is not urgently needed in a way that justifies bilingual debt (Option A) or permanent fragmentation (Option C). B-021B can proceed regardless of whether Candidate 2 is yet codified in GL-005 — the rule was already observed in B-021B's design (read-only investigation before any fix is proposed).

### 5.6 Risk summary

| Option | Language compliance | System coherence | Speed | Overall |
|---|---|---|---|---|
| A — English addition to Dutch GL-005 | Non-compliant (bilingual) | Acceptable | Fastest | Medium |
| B — Translate GL-005 first, then add | Fully compliant | Best | One extra step | Low |
| C — Standalone GL-015 | Fully compliant | Fragmented | Fast | Low–medium |

### 5.7 Exact proposed rule text

The rule text below applies to all three options; only the destination file and section differ.

```markdown
## Diagnostic discipline

When a system component behaves unexpectedly — a log file is empty, a script produces no
output, a backup is missing, a service does not respond — the mandatory first step is always
a read-only investigation to confirm the cause.

Rules:
- No fix may be proposed until the cause is confirmed.
- No script, configuration or system file may be modified based on a hypothesis alone.
- Investigation output: a short finding report stating the confirmed cause.
- If the cause cannot be confirmed in a read-only pass: classify as "requires deeper
  investigation" and defer. Do not proceed to a fix.
- This rule applies to every technical agent on every unexpected infrastructure finding.
```

This section is not proposed for execution until Owner selects a destination option and approves a separate execution proposal.

---

## 6. Proposed Sequencing

| Step | Action | Dependency | Session |
|---|---|---|---|
| 1 | Execute Candidate 1: GL-014 §3 extension | None — immediately executable after Owner approval | Session A |
| 2 | Commission GL-005 English translation (if Option B selected) | Owner selects Option B | Session B |
| 3 | Execute Candidate 2: add Diagnostic Discipline to translated GL-005 | GL-005 translation complete (Step 2) | Session B or C |

**If Option A is selected:** Steps 2 and 3 collapse into one step — add the rule to GL-005 as-is. Can be done in Session A alongside Candidate 1.

**If Option C is selected:** Create GL-015 in Session A or B. No prerequisite.

**Recommendation:** Execute Candidate 1 in Session A immediately. Commission GL-005 translation (Option B) as a separate task. Candidate 2 follows in Session B after translation is approved and complete. This keeps each step small, auditable and independently reversible.

---

## 7. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve Candidate 1 for execution? (GL-014 §3 insertion) | a) Approve b) Request content changes c) Defer | If approved: execute as exact content in §4. If changes requested: revise before execution. |
| 2 | Approve exact rule text for Candidate 1? | a) Approve §4.3 as written b) Request edits | Text in §4.3 will be inserted verbatim into GL-014 §3 |
| 3 | Select destination option for Candidate 2 | a) Option A — add to Dutch GL-005 now b) Option B — translate GL-005 first (recommended) c) Option C — standalone GL-015 | Determines Candidate 2 implementation path |
| 4 | Approve exact rule text for Candidate 2? | a) Approve §5.7 as written b) Request edits | Text in §5.7 will be used in whichever destination is selected |
| 5 | Candidate 1 and Candidate 2: same session or separate? | a) Same session (only if Option A selected for Candidate 2) b) Separate sessions (Option B or C) | Execution scope |

---

## 8. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only proposal. No files have been modified. No database rows have been written. No GL or SOP has been touched. The execution described in this proposal is not active until Owner's explicit approval is received for each component, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of B-030A is an approval of the exact content provided in §4 and the option selected in §5. Any content change after approval requires a separate approval.

---

## 9. Final Recommendation

**Candidate 1:** Ready for immediate execution. The GL-014 §3 insertion is exact, low risk, additive only, and directly formalizes the practice confirmed in B-021A. No prerequisite required.

**Candidate 2:** Option B recommended — translate GL-005 to English first, then add the Diagnostic Discipline section. This is the audit-consistent path and produces a fully compliant GL-005. The rule is sound; the delivery path simply requires one bounded preparatory step.

**Recommended execution sequence:**
1. Owner approves Candidate 1 exact text → execute GL-014 §3 insertion (Session A)
2. Owner selects Option B → commission GL-005 English translation (Session B, bounded task)
3. Owner approves GL-005 translation + Candidate 2 rule text → execute both in one pass (Session B or C)

B-021B (logging investigation) and B-021C (credential recovery documentation) can proceed in parallel with step 2, without waiting for Candidate 2 promotion.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-030A-rule-promotion-proposal.md`*
