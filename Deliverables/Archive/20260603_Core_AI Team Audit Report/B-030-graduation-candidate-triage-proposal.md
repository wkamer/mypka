# B-030 Graduation Candidate Triage Proposal

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Proposal — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.2
**No changes executed**

---

## 1. Purpose

Two graduation candidates were approved and recorded in team_log during the B-021 audit session (2026-06-03). Per CLAUDE.md and SOP-009, graduation candidates must be triaged: assessed for structural permanence and, if they qualify, promoted to the appropriate system document through a controlled proposal and approval flow.

This proposal performs that triage. It does not modify any system file. It produces a recommendation for each candidate — including proposed destination, exact rule text, and dependencies — for Owner Walter Kamer's review.

---

## 2. Governance Basis

| Rule | Source |
|---|---|
| Graduation candidates require a separate proposal and Owner approval before any GL/SOP modification | GL-014 v1.2 §1 |
| Guidelines are critical files — may never be modified without Owner approval | GL-014 v1.2 §8 |
| Guideline executor: Larry/Nolan. Reviewer: Larry. Final approval: Owner | GL-014 v1.2 §9 |
| All system files must be written in English | GL-014 v1.2 §10 |
| Every change to a GL includes a changelog entry | GL-014 v1.2 §5 |
| Graduation candidates are set-in-stone insights that have earned permanent team rule status | CLAUDE.md, SOP-009 |
| Agents may never modify their own AGENT.md — proposals go through Nolan → Larry → Owner | GL-014 v1.2 §4 |

---

## 3. Scope

**Candidates reviewed:**
- team_log id 67: Sensitive credential file handling rule (source: B-021 audit, 2026-06-03)
- team_log id 68: Investigation-before-fix rule for broken log/script issues (source: B-021 audit, 2026-06-03)

**System documents consulted (read-only):**
- `Team Knowledge/Core/Guidelines/GL-005_AI Engineering Operating System.md` — current content and structure
- `Team Knowledge/Core/Guidelines/GL-014_AI Team Governance.md` §3 Secret handling — existing coverage
- `CLAUDE.md` — existing rules for context

**Excluded:**
- Execution of any GL or SOP modification
- Backlog item registration
- Any change to GL-005, GL-014, SOP-001, CLAUDE.md or AGENT.md files

---

## 4. Read-Only Method

Investigation performed using:
- `SELECT id, log_date, content FROM team_log WHERE entry_type='graduation_candidate'` — exact candidate text
- `Read` on GL-005 — full content inspection to assess fit for Candidate 2
- `Read` on GL-014 §3 — existing secret handling rules to assess overlap with Candidate 1
- Cross-reference against CLAUDE.md §Hard Rules and §Scripts & Engineering for existing coverage

No files were modified. No database writes were performed.

---

## 5. Candidate Triage

### Candidate 1 — Sensitive Credential File Handling Rule

**Source:** team_log id 67, B-021 audit, 2026-06-03

**Original text:**
> Files such as `.env` with service credentials must not be added to regular myPKA, rclone or Google Drive backups. Default action is always manual recovery documentation only. No secret values in any deliverable. Approved as candidate by Owner — implementation requires separate proposal, review and explicit approval before any GL-005 or standalone GL modification.

---

**Structural or session-specific:**
Structural. The rule emerged from a specific audit finding (B-021 — `.env` not in any backup path) but expresses a permanent security principle applicable to every future infrastructure task, backup proposal, and integration that involves credential files. It does not describe a one-time decision; it describes standing behavior.

---

**Assessment of existing coverage:**

GL-014 §3 currently states:
- Secrets, tokens, API keys, encryption keys and passwords may never be shown in output
- Secrets may not be copied to session logs, agent journals, SOPs, Guidelines or Workstreams
- `.env`, `rclone.conf`, credentials and private keys are always critical files
- Changes to secrets require Owner's explicit approval and technical review by Kai

GL-014 §3 covers secrecy (do not show, do not copy to docs) and criticality (`.env` is a critical file). It does **not** cover:
- The backup exclusion rule (`.env` must not enter regular myPKA/rclone/Google Drive backups)
- The default recovery strategy (document manual recovery only)
- The prohibition on writing secret values in deliverables when documenting recovery

The candidate fills a specific, unaddressed gap in GL-014 §3.

---

**Recommended destination:** GL-014 §3 extension

**Rationale:** GL-014 §3 is already the SSOT for secret handling. Adding the backup exclusion and recovery documentation rule to §3 is a natural extension of the existing principle (".env is always a critical file"). It avoids creating a standalone GL for a three-sentence rule and keeps all credential security rules in one place. GL-005 is not the right destination — GL-005 governs engineering process, not governance/security rules.

**Responsible agent / Maintainer:** Larry (GL-014 Maintainer per audit work; GL-005 Bewaker per file)

**Risk level:** Low. GL-014 §3 already governs secrets; this extends it with a backup-specific sub-rule. The addition is declarative and does not change any existing behavior — it formalizes what is already the correct practice.

---

**Proposed rule text** (to be appended to GL-014 §3 Secret handling):

```markdown
**Credential file backup rule:**
Sensitive credential files (`.env`, `rclone.conf`, private keys, OAuth tokens) must not be
added to regular myPKA, rclone or Google Drive backups by default. If a credential file is
lost on hardware failure, recovery is manual-only — sourcing credentials from a secure
external store and re-entering them.

Recovery procedures for specific credential files must be documented in SOP-001 Disaster
Recovery without including secret values. A separate secure-credential backup proposal is
required before any automated credential backup is approved.
```

**Whether a separate proposal is required:** Yes. The rule text above is the proposed content. Execution requires a dedicated proposal showing the exact GL-014 §3 insertion (with surrounding context for the Edit operation), changelog entry, and post-check. Owner's explicit approval of that proposal is required before any file is modified.

**Dependencies:** B-021C (Secure Credential Recovery Procedure) — the SOP-001 documentation required by this rule is the direct scope of B-021C. Candidate 1 and B-021C should be sequenced: promote Candidate 1 to GL-014 §3 first (sets the rule), then execute B-021C (fulfills the rule for `/opt/mypka-memory/.env`).

**Recommendation:** Promote to GL-014 §3. Commission a dedicated GL-014 §3 extension proposal.

---

### Candidate 2 — Investigation-Before-Fix Rule

**Source:** team_log id 68, B-021 audit, 2026-06-03

**Original text:**
> When a log file is unexpectedly empty or a script behaves unexpectedly, the correct first step is always a read-only investigation to confirm the cause. No fix proposed or executed until the cause is known. Approved as candidate by Owner — implementation requires separate proposal, review and explicit approval before any GL-005 or standalone GL modification.

---

**Structural or session-specific:**
Structural. The rule emerged from a specific finding (mypka-backup.log is 0 bytes — cause unknown) but describes a permanent engineering discipline: diagnose before prescribing. It applies to any future instance of unexpected infrastructure behavior, not only to the specific log file that triggered it.

---

**Assessment of existing coverage:**

GL-005 Development rules currently states:

**Never:**
> "Direct grote systemen genereren, features combineren zonder reden, business logic verstoppen, productie aanpassen zonder validatie, aannames presenteren als feiten, smart magic toevoegen zonder noodzaak."

GL-005 already prohibits "productie aanpassen zonder validatie" (modifying production without validation) and "aannames presenteren als feiten" (presenting assumptions as facts). These are adjacent but do not specifically address the investigation-before-fix pattern for unexpected behavior in log files, scripts, or other infrastructure components.

GL-005 Production safety section states: "Nooit direct op productie werken zonder: validatie, tests, rollback mogelijkheid, logging, foutafhandeling." This is about production deployment safety, not diagnostic discipline for unexpected system behavior.

The candidate addresses a gap: the specific case where a component behaves unexpectedly and the reflex to immediately propose or apply a fix — without confirming the cause — is a recurring risk in infrastructure work.

---

**Language dependency noted:** GL-005 is currently written entirely in Dutch. GL-014 §10 requires all system files to be in English. Adding an English rule to a Dutch GL-005 would create an inconsistency. Two options exist:

- Option A: Add the rule to GL-005 in English only, accepting that GL-005's existing Dutch content is a pre-existing compliance gap (pending a future GL-005 translation pass).
- Option B: Commission GL-005 translation (similar to B-028 for GL-014) as a prerequisite, then add the rule.

Option A is the more pragmatic path — it does not block the promotion and is consistent with the approach used throughout this audit (translate on touch, don't require a pre-emptive global translation). The GL-005 Dutch content already exists as a pre-existing compliance item; the new English rule does not make that worse.

---

**Recommended destination:** GL-005, under Development rules — new subsection "Diagnostic discipline"

**Rationale:** GL-005 is the AI Engineering Operating System and applies to all agents doing technical work. The investigation-before-fix principle is a general engineering operating rule, not a governance rule (GL-014), not a procedure (SOP), and not agent-specific (AGENT.md). Adding it to GL-005 makes it a standing instruction that every technical agent (primarily Kai) inherits. A standalone GL for a single-rule diagnostic principle is overkill; GL-005 is the right home.

**Responsible agent / Maintainer:** Larry (GL-005 Bewaker per file; GL modifications require Larry as executor per GL-014 §9)

**Risk level:** Low. The rule is additive. It does not change any current behavior — it formalizes a diagnostic discipline that was already implied by GL-005's "never modify production without validation." The addition is declarative.

---

**Proposed rule text** (new subsection to add to GL-005 under Development rules, or as a standalone new section):

```markdown
## Diagnostic discipline

When a system component behaves unexpectedly — a log file is empty, a script produces no
output, a backup is missing, a service does not respond — the mandatory first step is always
a read-only investigation to confirm the cause.

Rules:
- No fix may be proposed until the cause is confirmed.
- No script or configuration may be modified based on a hypothesis.
- Investigation output: a short finding report stating the confirmed cause.
- If the cause cannot be confirmed in a read-only pass: classify as "requires deeper
  investigation" and defer — do not proceed to a fix.
- This rule applies to every technical agent on every unexpected infrastructure finding.
```

**Whether a separate proposal is required:** Yes. The rule text above is the proposed content. Execution requires a dedicated proposal showing the exact GL-005 insertion (new section after Development rules or as a subsection within it), changelog entry, language note (English addition to Dutch GL), and post-check. Owner's explicit approval of that proposal is required before any file is modified.

**Dependencies:** B-021B (Logging Improvements Investigation) — the `mypka-backup.log` investigation in B-021B is the first instance of applying this rule. Candidate 2's promotion to GL-005 does not need to complete before B-021B begins; B-021B was already designed as a read-only investigation. However, promoting Candidate 2 before B-021B execution makes the rule formally active and auditable.

**Recommendation:** Promote to GL-005. Commission a dedicated GL-005 insertion proposal. Note the pre-existing Dutch language state of GL-005 in the proposal.

---

## 6. Cross-Candidate Impact

The two candidates are complementary and both inform active backlog items:

| Candidate | Informs | How |
|---|---|---|
| Candidate 1 (credential rule) | B-021C | The GL-014 §3 extension sets the rule that B-021C must fulfill: SOP-001 must document `.env` manual recovery without secret values. Sequence: promote Candidate 1 → then execute B-021C. |
| Candidate 2 (investigation-before-fix) | B-021B | The GL-005 addition formalizes the approach B-021B already uses: read-only investigation before any logging fix is proposed. Sequence: B-021B can proceed regardless; GL-005 promotion is parallel. |
| Candidate 1 | B-021B | Candidate 1 clarifies that credential files must not enter backups. This is informational context for B-021B — the logging investigation does not touch credential files, so no direct dependency. |
| Both candidates | Future infrastructure work | Together they establish two standing engineering disciplines: credential isolation and diagnostic rigor. Any future infrastructure task that involves credential files or unexpected behavior will reference these rules. |

There is no blocking dependency between the two candidates. They can be promoted in the same proposal pass or separately.

---

## 7. Proposed Next Actions

None of these actions may be executed without Owner's explicit approval:

| # | Action | Executor | Deliverable |
|---|---|---|---|
| 1 | Commission a GL-014 §3 extension proposal for Candidate 1 | Larry | Exact insertion text, changelog entry, post-check for GL-014. Proposal-only until approved. |
| 2 | Commission a GL-005 insertion proposal for Candidate 2 | Larry | Exact new section text, changelog entry, language note, post-check for GL-005. Proposal-only until approved. |
| 3 | After Candidate 1 is promoted: commission B-021C execution | Kai | SOP-001 update for `.env` manual recovery procedure. Fulfills GL-014 §3 extended rule. |
| 4 | After Candidate 2 is promoted (or in parallel): commission B-021B | Kai | Read-only investigation of mypka-backup.log. Produces finding report + implementation proposal for mypka-sync.log rotation. |

Items 1 and 2 may be handled in a single session. Items 3 and 4 are separate sessions.

---

## 8. Owner Decisions Required

| # | Decision | Options | Impact |
|---|---|---|---|
| 1 | Approve Candidate 1 destination: GL-014 §3 extension? | a) Approve — commission GL-014 §3 proposal b) Redirect to standalone GL c) Defer | Determines whether credential backup rule becomes permanent team governance |
| 2 | Approve Candidate 1 proposed rule text? | a) Approve as written b) Request edits | Exact text will be used in GL-014 §3 insertion |
| 3 | Approve Candidate 2 destination: GL-005 new section? | a) Approve — commission GL-005 proposal b) Redirect to standalone GL c) Defer | Determines whether investigation-before-fix rule becomes a standing engineering rule |
| 4 | Approve Candidate 2 proposed rule text? | a) Approve as written b) Request edits | Exact text will be used in GL-005 insertion |
| 5 | Accept Option A for GL-005 language (English addition to existing Dutch content)? | a) Accept — add English rule to existing Dutch GL b) Require GL-005 translation first | If b): GL-005 translation must precede Candidate 2 promotion |
| 6 | Commission items 1 and 2 (GL proposals) in the same session? | a) Same session b) Separate sessions | Scope management |

---

## 9. Approval Gate

**No implementation may happen until Owner Walter Kamer gives explicit approval.**

This is a read-only triage proposal. No files have been modified. No database rows have been written. No backlog items have been registered. The proposed next actions in §7 are not active until Owner's explicit approval is received, per GL-014 v1.2 §1.

Owner Walter Kamer's approval of the proposed destinations and rule texts in §5 is required before any GL-014 or GL-005 insertion proposal may be drafted and executed.

---

## 10. Final Recommendation

Both graduation candidates are structural. Neither is session-specific. Both qualify for promotion.

**Candidate 1** belongs in GL-014 §3 — the natural home for credential security rules. The proposed rule text fills a specific gap (backup exclusion and manual recovery documentation requirement) that is not currently covered by the existing §3 content.

**Candidate 2** belongs in GL-005 — the AI Engineering Operating System, as a new "Diagnostic discipline" section. It formalizes a principle already implied by GL-005 but not explicitly stated. The pre-existing Dutch language state of GL-005 is a known compliance gap; adding the rule in English is the pragmatic approach.

**Recommended next step:** Owner Walter Kamer reviews and approves the proposed destinations and rule texts. After approval, a single session can commission both GL proposals (GL-014 §3 extension and GL-005 insertion) as a controlled two-file update. B-021C and B-021B follow in subsequent sessions.

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-030-graduation-candidate-triage-proposal.md`*
