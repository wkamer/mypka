# Review Context Packet and Review Gate Package
## SOP-017 Source Folder Closure Amendment v02

**RCP version:** v02
**Prepared by:** Larry (Team Orchestrator)
**Date:** 2026-06-05
**Review session:** 2026-06-05
**Status:** Pending Owner instruction — Review Gate not yet executed

**Revision note (v01 → v02):** Field 11 corrected. "Approve execution" replaced with "Accept proposal at DP-3" to correctly separate DP-3 proposal acceptance from DP-4 implementation confirmation, per live SOP-018. No other fields changed.

---

## Review Context Packet

---

### Field 1 — Review Purpose

Determine whether the SOP-017 source folder closure amendment (v01) is complete, internally consistent, safe to implement, and ready for Owner approval to proceed to implementation under SOP-015.

---

### Field 2 — Deliverable Path

`Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/sop-017-amendment-source-folder-closure-v01.md`

---

### Field 3 — Deliverable Type

Amendment — governance file change proposal. SOP-015 deliverable. Scenario class S8 (Governance-Relevant Idea). Route D. Impact: Low.

---

### Field 4 — Owner

Walter Kamer

---

### Field 5 — Maintainer

Larry (Team Orchestrator)

---

### Field 6 — Governance Baseline

All active GLs and SOPs at time of review (2026-06-05):

**Active Guidelines:**

| Number | Title |
|---|---|
| GL-001 | File naming conventions |
| GL-002 | Frontmatter conventions |
| GL-003 | Email setup |
| GL-004 | Canonical paths |
| GL-005 | AI Engineering Operating System |
| GL-006 | Notification Format |
| GL-007 | Integration naming convention |
| GL-008 | WhatsApp conversatie borging |
| GL-009 | CRM people link consistency |
| GL-010 | Session logs purpose and discipline |
| GL-011 | Project documentation conventions |
| GL-012 | ChatGPT prompt ICOR module-verwerking |
| GL-013 | Memory Core Architecture |
| GL-014 | AI Team Governance |
| GL-015 | Memory Domain Routing Protocol |
| GL-016 | Review Gate for Governance-Relevant Deliverables |
| GL-017 | Deliverable Lifecycle Knowledge Processing and Archiving |
| GL-018 | Idea Routing and Implementation Governance Principles |

**Active SOPs:**

| Number | Title |
|---|---|
| SOP-001 | Disaster recovery |
| SOP-002 | How to do deep online research |
| SOP-003 | How to hire a new team member |
| SOP-005 | Task management |
| SOP-006 | Project management |
| SOP-007 | Memory Core operaties |
| SOP-008 | Read own journal before task |
| SOP-009 | Write journal entry after task |
| SOP-012 | Daily Planning v3 flow |
| SOP-013 | 365academy bestanden hernoemen |
| SOP-014 | Claude Code session context hygiene |
| SOP-015 | Proposal Iteration Protocol for System File Changes |
| SOP-016 | Review Gate Procedure for Governance-Relevant Deliverables |
| SOP-017 | Deliverable Lifecycle Knowledge Processing and Archiving Procedure |
| SOP-018 | Idea-to-Implementation Routing Procedure |

**Note on GL-018 and SOP-018:** Both were implemented on 2026-06-05 as part of the Idea-to-Implementation Governance Pack v05. They are live at their canonical locations. They are not pending.

**Note on SOP-016 Section 11 (RCP amendment):** The Review Context Packet amendment is live in SOP-016 as Section 11. It was implemented on 2026-06-05 as part of the same governance pack.

---

### Field 7 — Relevant Active GLs and SOPs

The reviewer must apply or verify against the following instruments for this review:

| Document | Why relevant |
|---|---|
| SOP-017 — Deliverable Lifecycle Knowledge Processing and Archiving Procedure | The document being amended. The reviewer must verify all changes against the live file. |
| GL-017 — Deliverable Lifecycle Knowledge Processing and Archiving | Companion principle document to SOP-017. Reviewer must verify the amendment belongs in SOP-017 and not GL-017. |
| SOP-015 — Proposal Iteration Protocol for System File Changes | Governs the proposal iteration process for system-file change proposals. Route D applies. |
| SOP-016 — Review Gate Procedure for Governance-Relevant Deliverables | Defines the 13 review checks applied in this review gate. Contains the RCP specification (Section 11). |
| GL-016 — Review Gate for Governance-Relevant Deliverables | Governing principle behind SOP-016. Defines when a review gate is required. |
| SOP-018 — Idea-to-Implementation Routing Procedure | Governs scenario classification (S8), route selection (Route D), review gate triggers, and Owner decision points (DP-3 and DP-4) for this amendment. |
| GL-018 — Idea Routing and Implementation Governance Principles | Governing principle behind SOP-018. |

---

### Field 8 — Review Scope

The reviewer must evaluate exactly the following:

1. Whether the amendment proposal document at Field 2 is complete and internally consistent.
2. Whether Amendments A, B, C, and D are additive only and do not modify any existing SOP-017 section, rule (EX-1 through EX-7), decision rule (R1 through R10), or report field (field 1 through 13).
3. Whether EX-8 (Amendment C) is consistent in structure and language with existing EX-1 through EX-7.
4. Whether EX-8 correctly scopes the source folder closure rule: applies when at least one archive action was executed; does not apply when no archive action was executed.
5. Whether the source folder closure procedure in Amendment A (Section 10 subsection) is clear, actionable, and safe.
6. Whether non-empty source folders are explicitly protected from deletion by the amendment text.
7. Whether hidden files are handled explicitly enough in the amendment text itself (Amendment A steps and EX-8 body) — see Additional Check 14 below.
8. Whether the five new Section 16 fields (Amendment D, fields 14 through 18) cover all required states: archive executed or not executed; folder empty or not empty; folder deleted or retained; remaining files listed.
9. Whether Amendment B (Safeguards Checklist) is minimal and correctly links to EX-8 and Section 16 fields 14 through 18 without duplicating rule text.
10. Whether the amendment preserves the archive proposal requirement in EX-6: a formal archive proposal is still required before any file is moved; source folder closure is a post-archive step, not a replacement of EX-6.
11. Whether the 13 SOP-016 standard review checks pass, fail, or are uncertain.
12. Whether the proposal correctly classifies as S8 and Route D under SOP-018.

---

### Field 9 — Non-Goals

The reviewer must not evaluate:

- The business value or desirability of the amendment.
- Sections of SOP-017 not named in the amendment (Sections 1 through 9, 11, 12, 15, 17).
- Any other governance files (GL-017, GL-016, SOP-016, SOP-015, SOP-018, GL-018).
- Whether the underlying operational incident (empty folder left after lifecycle execution) required a governance response.
- Whether the amendment should be split into multiple proposals.
- Whether the amendment resolves or does not resolve any other known gap in SOP-017.

---

### Field 10 — Hard Exclusions

The following actions must not occur during or as a result of this review:

- No modification to SOP-017 or any section of it.
- No modification to GL-017.
- No modification to SOP-016.
- No modification to GL-016.
- No modification to SOP-015.
- No modification to SOP-018.
- No modification to GL-018.
- No update to any index file.
- No database writes of any kind.
- No creation of backlog items.
- No archiving, moving, or deletion of any file.
- No execution of any implementation action.
- No claim that the amendment is approved.
- No claim that implementation is authorized.

---

### Field 11 — Allowed Owner Decisions

After the reviewer returns findings, the Owner may choose from the following options (per SOP-016 Section 7 and SOP-018 Section 12):

| Option | Meaning |
|---|---|
| Accept proposal at DP-3 | Amendment proposal accepted as stated after Review Gate findings. This does not authorize implementation. Separate DP-4 implementation confirmation is required before SOP-017 may be modified. |
| Request amendments | Specific changes required before re-review; a v02 amendment proposal is prepared. |
| Defer | Amendment valid but action postponed; reason and condition stated. |
| Reject | Amendment not accepted; reason stated; no execution. |

---

### Field 12 — Required Reviewer Checks

Apply all 13 standard checks (SOP-016 Section 6) plus the one additional check specific to this deliverable.

**Standard checks (13):**

| # | Check | What to verify |
|---|---|---|
| 1 | Scope check | Does the amendment stay within the approved scope? Does it include work that was not authorized? |
| 2 | Evidence check | Are all factual claims backed by named sources? Are sources listed? |
| 3 | Source precedence check | If status sources conflict, has GL-016 Rule 3 been applied? |
| 4 | Exact text check | Where approved text was specified verbatim, does the deliverable contain exactly that text with no substitutions? |
| 5 | Exact file path check | Are all file paths exact? No approximate paths, no assumed extensions, no inferred subdirectories? |
| 6 | Markdown fence integrity check | Where code blocks are present: are all fences opened and closed? Are language identifiers correct? No runaway fences? |
| 7 | Post-check completeness | Does the deliverable include the required post-checks? Are all post-check results stated? |
| 8 | Out-of-scope modification check | Were any files, records, or systems modified that were not in the approved scope? (Note: this is a proposal document — no modifications should have occurred at all.) |
| 9 | Secret exposure check | Does the deliverable contain or reveal any credential, token, API key, password, or secret value? |
| 10 | Database or file modification check | Were any databases, system files, AGENT.md files, CLAUDE.md, SOPs, GLs, or Workstreams modified? If yes, were these modifications explicitly authorized? |
| 11 | Rollback requirement check | Not applicable — this is an amendment proposal, not a migration or database change. State: "Not applicable — amendment proposal." |
| 12 | Final status check | Is the final status of all items in the deliverable clearly stated? Are open items named as open? |
| 13 | Next-step safety check | Is the recommended next step stated? Is it safe to execute without further approval? Does it require a new proposal before execution? |

**Additional check (1):**

| # | Check | What to verify |
|---|---|---|
| 14 | Hidden-file-aware check coverage | Verify whether the amendment text itself — specifically Amendment A (Section 10 subsection steps) and EX-8 body (Amendment C) — includes explicit hidden-file-aware source folder checking, such as `ls -A` or a platform-equivalent instruction. The risk mitigation table in the proposal document mentions hidden files and `ls -A`. Determine whether this mention is sufficient, or whether the executable amendment text (Amendment A steps and/or EX-8) should also include an explicit instruction to use a hidden-file-aware check. Return: (a) whether `ls -A` or equivalent appears in the Amendment A steps; (b) whether `ls -A` or equivalent appears in the EX-8 body; (c) whether the reviewer judges the current coverage sufficient or insufficient; (d) if insufficient, state exactly which amendment text location should contain the explicit instruction. |

---

### Field 13 — Required Output Format

The reviewer must return findings in the following format:

1. **Per-check results** — for each of the 14 checks: Pass / Fail / Uncertain, with a one-line reason.
2. **Uncertainty list** — list all checks marked Uncertain, with the specific information gap that prevents a Pass or Fail determination.
3. **Hard stop list** — list any checks where the finding must block Owner presentation (Fail on checks 1, 4, 5, 8, 10, or 14 if critical). State: "Hard stop — [reason]."
4. **Additional check 14 findings** — structured per the four sub-items stated in Field 12 Additional Check 14.
5. **Owner decision packet** — a brief neutral summary of findings, followed by the applicable Owner decision options from Field 11.

The reviewer must not include implementation instructions, amendment drafts, or executable text in the findings.

---

### Field 14 — Known Dependencies

| Dependency | Type | Notes |
|---|---|---|
| `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` | File — target of amendment | Reviewer must read the live file before applying checks. |
| `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md` | File — companion principle | Reviewer must read to verify amendment placement (SOP-017 not GL-017). |
| `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` | File — governs this review | Reviewer must read Section 6 (checks), Section 7 (decision options), Section 11 (RCP). |
| `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` | File — companion principle | Reviewer must read to verify review gate trigger and scope. |
| `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md` | File — governs iteration | Reviewer must read to verify proposal format compliance. |
| `Team Knowledge/Core/SOPs/SOP-018_Idea-to-Implementation Routing Procedure.md` | File — governs classification | Reviewer must verify S8 classification, Route D selection, and DP-3/DP-4 decision point structure. |
| `Team Knowledge/Core/Guidelines/GL-018_Idea Routing and Implementation Governance Principles.md` | File — companion principle | Reviewer must read for S8 and Route D principle definitions. |
| DP-1 (Owner confirmation of S8 and Route D) | Prior decision | Owner confirmed classification and Route D via task instruction on 2026-06-05. No file record; session-bound only. |
| Owner content-direction acceptance | Prior decision | Owner accepted content direction of the amendment on 2026-06-05 but stated it was not yet approval-ready due to missing RCP. This review is the required next step before re-presenting to Owner. |

---

### Field 15 — Canonical Source Files

The reviewer must use the following authoritative source files. All paths are exact. Read each file before applying checks.

**Deliverable under review:**

| Document | Path |
|---|---|
| Amendment proposal (v01) | `Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/sop-017-amendment-source-folder-closure-v01.md` |

**Governance pack companion files (all live as of 2026-06-05):**

| Document | Path | Status |
|---|---|---|
| GL-018 — Idea Routing and Implementation Governance Principles | `Team Knowledge/Core/Guidelines/GL-018_Idea Routing and Implementation Governance Principles.md` | LIVE — implemented 2026-06-05 |
| SOP-018 — Idea-to-Implementation Routing Procedure | `Team Knowledge/Core/SOPs/SOP-018_Idea-to-Implementation Routing Procedure.md` | LIVE — implemented 2026-06-05 |
| SOP-016 with Section 11 RCP amendment | `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` | LIVE — Section 11 implemented 2026-06-05 |

**Source documents for amendment verification:**

| Document | Path |
|---|---|
| Live SOP-017 (document being amended) | `Team Knowledge/Core/SOPs/SOP-017_Deliverable Lifecycle Knowledge Processing and Archiving Procedure.md` |
| Live GL-017 (companion principle) | `Team Knowledge/Core/Guidelines/GL-017_Deliverable Lifecycle Knowledge Processing and Archiving.md` |
| Live GL-016 (review gate principle) | `Team Knowledge/Core/Guidelines/GL-016_Review Gate for Governance-Relevant Deliverables.md` |
| Live SOP-015 (proposal iteration protocol) | `Team Knowledge/Core/SOPs/SOP-015_Proposal Iteration Protocol for System File Changes.md` |

**File naming conventions (for filename evaluation):**

| Document | Path |
|---|---|
| GL-001 — File naming conventions | `Team Knowledge/Core/Guidelines/GL-001_File naming conventions.md` |

---

### Field 16 — Execution Allowed

**No.**

No implementation may occur as a result of this review. This review produces findings and an Owner decision packet only. Implementation requires a separate Owner approval at DP-3 (proposal acceptance) followed by a further explicit Owner confirmation at DP-4 (implementation authorization) before SOP-017 may be modified. No file may be created, modified, moved, or deleted. No database writes may occur.

---

### Field 17 — Lifecycle Processing in Scope

**No.**

Lifecycle processing under SOP-017 is not in scope for this review session. This review evaluates a proposal document. The proposal is pre-acceptance. GL-017 and SOP-017 lifecycle rules apply only after Owner acceptance. Lifecycle decisions for the proposal document itself are deferred to a separate session after Owner acceptance.

---

### Field 18 — Prior Memory Disclaimer

The reviewer must not rely on any prior chat history, session memory, or accumulated tool context. All context required for this review is contained in this RCP and the deliverable under review. If the reviewer requires information not present in this RCP and the deliverable, the reviewer must stop and request it from the Maintainer before proceeding. Inferring missing context from prior conversations or tool state is not permitted and will invalidate the review findings.

---

---

## Review Gate Instruction Section

**Status:** Package prepared. Review Gate execution is pending Owner instruction.

The Review Gate must not be executed unless the Owner explicitly instructs it in a subsequent session. This package is ready for that execution.

---

### Reviewer Instructions

Read this entire RCP before reading the deliverable. Verify that all 18 fields are present and complete. Apply the 14 checks listed in Field 12. Return findings in the format specified in Field 13.

---

### Review Gate Evaluation Points

The reviewer must evaluate all of the following. These are in addition to the 13 standard SOP-016 checks.

**1. Amendment placement: SOP-017 or GL-017?**

Verify whether the source folder closure rule is correctly placed in SOP-017 and not GL-017.

Check: GL-017 defines lifecycle states, markers, and governing principles. SOP-017 defines the procedure — the step-by-step execution of those principles. Source folder closure is a procedural step (what to do after archive moves are complete), not a principle change. The reviewer must confirm whether SOP-017 is the correct and sufficient home for this amendment, or whether GL-017 also requires a corresponding update.

**2. Source folder closure rule: clarity and safety**

Verify whether Amendment A (Section 10 subsection) states the closure rule in terms that are clear, unambiguous, and executable without further interpretation.

Specifically: is it clear exactly when the check is triggered (after all archive moves in the current lifecycle execution, not after each individual move)? Is the scope of "source folder" defined precisely enough to prevent confusion with parent or sibling folders?

**3. Non-empty folder protection**

Verify whether the amendment text explicitly and unambiguously prohibits deleting a non-empty source folder under any circumstance. Check Amendment A steps, EX-8 body, and all related amendment text.

Confirm that no path through the amendment logic could result in authorized deletion of a non-empty folder. A non-empty folder must require Owner decision for each remaining file before any further action.

**4. Hidden file handling: is it explicit enough in the amendment text?**

This is Additional Check 14 from Field 12. The proposal's risk mitigation table identifies the "false empty" risk and states that `ls -A` should be used. Determine whether:

a. The `ls -A` instruction (or a platform-equivalent) appears in the actual Amendment A procedure steps — not only in the risk table.
b. The `ls -A` instruction (or a platform-equivalent) appears in the EX-8 body.
c. If it appears only in the risk table and not in the executable amendment text: whether the reviewer judges this sufficient or whether the executable amendment text must also include the instruction.

The reviewer must return a specific finding: sufficient or insufficient. If insufficient, state exactly which amendment text location should be revised.

**5. Section 16 fields 14 through 18: coverage and mutual consistency**

Verify whether the five new report fields (Amendment D) cover all required states without gap or overlap:

- Archive executed / not executed (field 14 / not-applicable path)
- Folder empty / not empty after archive (field 15)
- Folder deleted / not deleted (field 16)
- Remaining files listed (field 17)
- Reason for retention (field 18)

Check that the not-applicable chain is internally consistent: if field 14 is not applicable, fields 15, 16, and 17 must also cascade to not-applicable without ambiguity. Check that the field labels in Amendment D match the field labels referenced in Amendment A, Amendment B, and Amendment C.

**6. EX-8 consistency with EX-1 through EX-7**

Verify whether EX-8 (Amendment C) is consistent in structure, language, and authority level with existing EX-1 through EX-7.

Check: EX-1 through EX-7 each state a hard constraint and use language like "must," "may not," "requires." EX-8 must use the same level of constraint language. No softening ("should," "recommended") is acceptable for a rule that is stated as mandatory.

Check also whether EX-8 correctly uses "must be checked," "must be deleted," and "may not be reported as Done until" — the three mandatory-language anchors described in the proposal's Acceptance Criteria item 2.

**7. EX-6 preservation: archive proposal requirement**

Verify whether the amendment preserves the archive proposal requirement in EX-6 without modification or weakening.

EX-6 requires a formal archive proposal before any file move. This amendment adds a post-archive step (source folder closure). The reviewer must confirm that nothing in Amendments A, B, C, or D could be read as relaxing, replacing, or circumventing the EX-6 formal proposal requirement.

**8. Additive-only character: no unintended modifications**

Verify that the amendment is purely additive. Check:

- No existing section of SOP-017 (Sections 1 through 17) is reworded, deleted, or restructured.
- No existing rule (EX-1 through EX-7) is changed.
- No existing decision rule (R1 through R10) is changed.
- No existing report field (fields 1 through 13) is changed.
- The new items (Amendment A subsection, Amendment B checklist item, Amendment C EX-8, Amendment D fields 14 through 18) are purely additions to existing sections at the locations stated in the proposal.

---

### Review Gate Execution Status

**This Review Gate has not been executed.**

The Maintainer (Larry) has prepared:
- The Review Context Packet v02 (this document, all 18 fields complete)
- The amendment proposal at Field 2 (v01, content direction accepted by Owner)

The package is ready for reviewer assignment and execution. The Maintainer awaits Owner instruction before proceeding.

When the Owner instructs execution, the next step is: assign a reviewer (Mode 1 external review or Mode 3 single-system fallback per SOP-016), provide the reviewer with this RCP and the amendment proposal, and receive findings in the format specified in Field 13.

---

Delivered on: 2026-06-05
Delivered at: `Deliverables/20260605_Core_SOP-017 Source Folder Closure Amendment/`
