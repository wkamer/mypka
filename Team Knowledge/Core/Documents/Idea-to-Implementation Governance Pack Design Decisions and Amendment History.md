# Idea-to-Implementation Governance Pack — Design Decisions and Amendment History

**Created:** 2026-06-05
**Maintained by:** Larry (Team Orchestrator)
**Type:** Non-authoritative Core governance knowledge document

> **This is not a GL, SOP, or Workstream.** It is a knowledge reference document. It is not an authoritative source for governance rules. The authoritative sources are:
> - `Team Knowledge/Core/Guidelines/GL-018_Idea Routing and Implementation Governance Principles.md`
> - `Team Knowledge/Core/SOPs/SOP-018_Idea-to-Implementation Routing Procedure.md`
> - `Team Knowledge/Core/SOPs/SOP-016_Review Gate Procedure for Governance-Relevant Deliverables.md` (amended)
>
> This document is not added to gl-index.md or SOP-index.md.

---

## 1. GL-018 Design Decisions

**Source:** `idea-routing-gl-proposal-v05.md` — revision summaries v01 through v05

### v01 to v02 — Key decisions

- **P11 added** — Idea routing does not authorize persistent writes. Transient session capture is permitted; any persistent database write requires either a pre-approved routine or explicit Owner approval. Motivation: prevent idea classification from being used to justify database writes without proper authorization.
- **Maintainer responsibilities corrected** — "Tracks using team_tasks" removed; replaced with "Tracks using transient session context." Motivation: align with P11; team_tasks write requires authorization, not just triage.
- **Section 9 added** — Required Companion Sources. A reviewer without these documents cannot independently verify compliance. Making companion sources explicit prevents reviews from assuming prior chat context.
- **Section 10 added** — Pack-level Implementation Order (later removed from GL content in v03).
- **Relationship table updated** — GL-014, GL-001, and GL-004 marked as required companion sources.
- **Numbering re-confirmation note added** — GL numbers must be re-confirmed against live gl-index.md immediately before implementation, not at proposal time.

### v02 to v03 — Key decisions

- **Section 10 removed from GL-018 content** — The pack-level implementation order is an ephemeral deployment note, not a permanent governance principle. It was moved to the proposal wrapper as context only. The final GL-018 file contains Sections 1 through 9 and Changelog only. This decision prevents the GL from embedding deployment-specific content that would become outdated.

### v03 to v04 — Key decisions

- **P8 lifecycle timing made explicit** — The implementation-route lifecycle decision occurs at DP-6 after DP-5 acceptance. Other accepted deliverables produced during idea routing (proposals, research briefs, review reports, closure reports) may separately receive SOP-017 lifecycle processing when accepted as standalone deliverables. Motivation: P8 previously left ambiguity about whether the lifecycle decision covered the implementation route only or also other deliverables produced during routing.
- **SOP-015 row in Section 7 corrected** — "system-file change" replaced with the more precise category terms "governance file" and "operational system file" (per SOP-018 Section 2.4 distinction). Cross-reference to SOP-018 Section 2.4 added. Motivation: prevent conflation of governance file changes (S8/Route D/SOP-015) with operational system file changes (Route C or higher).

### v04 to v05 — Key decisions

- No GL-018 content changes. Companion file references in the proposal wrapper updated from v04 to v05 versions.

---

## 2. SOP-018 Design Decisions

**Source:** `idea-routing-sop-proposal-v05.md` — revision summaries v01 through v05

### v01 to v02 — Key decisions

- **Role-based agent table added (Section 2.2)** — Named agents replaced with role-based references. Motivation: the SOP must remain valid when agents are replaced or restructured. Role is the governance dependency; current assignment is informational only.
- **Review Gate mode definitions added (Section 2.3)** — Brief definitions embedded in SOP-018 for routing decisions; full procedure in SOP-016. Motivation: Maintainer needs mode guidance at the classification step, before consulting SOP-016.
- **Section 3a Companion Sources added** — All documents a reviewer must have to independently review any SOP-018-governed deliverable. Motivation: self-containment is a design requirement (GL-018 P9).
- **Section 4 persistent write prohibition** — Intake does not authorize persistent writes. This is the procedural implementation of GL-018 P11.
- **Route B escalation rule added (Section 9)** — Six explicit conditions; automatic escalation to Route C, D, or F. Motivation: Route B was being used loosely; explicit escalation conditions prevent Review Gate bypass.
- **Section 12 restructured** — Review Gate must execute before Owner makes DP-3 decision. v01 had DP-3 before Review Gate, which would make the Review Gate advisory rather than gate-keeping. Corrected sequencing: Review Gate → findings → Owner DP-3 decision.
- **Section 14 added** — Persistent Write Rules as a standalone section.
- **EX-9 added** — No persistent write may be executed as a result of idea routing itself.
- **HR-6, HR-7 added** — SOP number re-confirmation required before implementation; Route B may not claim Review Gate-free status without Maintainer explicitly confirming all escalation conditions false.
- **Section 21 added** — Pack-level Implementation Order.

### v02 to v03 — Key decisions

- **Section 2.4 added** — File Category Definitions. Distinguishes governance files (GLs, SOPs, Workstreams, AGENT.md, CLAUDE.md, governance indexes) from operational system files (scripts, handlers, integration files, skill files, configuration files). Motivation: "system file" was being used ambiguously; the distinction determines which route (C vs. D) applies.
- **Route B condition 1 split into 1a and 1b** — Governance file change → escalate to Route D. Operational system file change → escalate to Route C. Motivation: the original single condition did not distinguish between the two categories, which have different governance requirements.
- **EX-2 updated** — Explicitly distinguishes governance files from operational system files.
- **Acceptance Criteria corrected** — Item 12 changed from "7" to "9" explicit exclusions (v02 error).
- **HR-7 updated** — Hard count of Route B escalation conditions removed; replaced with "all Route B escalation conditions" to avoid needing a version update if conditions change.

### v03 to v04 — Key decisions

- **Route B DP-4 made explicit** — Route B steps column corrected to read: "Short proposal → Owner direct review → Owner DP-3 decision → Implementation confirmation (DP-4) → Execution." v03 read "Owner decision → Execution" which could be read as DP-3 acceptance authorizing execution. DP-4 is always a separate step.
- **Route B scope note added** — Route B applies to Low-impact ideas only. Not available for Medium, High, or Critical. Motivation: the route matrix already reflected this, but the scope note makes it explicit to prevent misapplication.
- **S1-High corrected** — Changed from Route B* to Route C. High impact requires full proposal, Review Gate, implementation report, and lifecycle decision. Route B cannot satisfy these requirements.
- **Section 13 Route B trigger clarified** — "Without any of conditions 1a, 1b, 2–6" replaced with "without any Route B escalation condition from Section 9." Maintainer must explicitly confirm all conditions false. Motivation: removes ambiguity in the cross-reference.
- **Section 17 lifecycle timing made explicit** — Implementation-route lifecycle decision at DP-6 after DP-5. Other accepted deliverables may receive SOP-017 lifecycle processing independently. Consistent with GL-018 P8 (v04 correction).

### v04 to v05 — Key decisions

- **EX-5 corrected** — v04 text "Low-impact ideas may proceed to Route A with Owner confirmation at DP-4 only" could be read as excluding Route B from Low-impact applicability. Corrected: "Low-impact direct-execution ideas may proceed to Route A with Owner confirmation at DP-4 only. Low-impact ideas requiring a lightweight proposal follow Route B, subject to the Route B escalation conditions in Section 9." Motivation: Route A and Route B are both available at Low impact; they serve different use cases (direct execution vs. lightweight proposal); neither excludes the other.

---

## 3. SOP-016 RCP Amendment Design Decisions

**Source:** `review-context-packet-sop-016-amendment-proposal-v05.md` — revision summaries v01 through v05

### v01 to v02 — Key decisions

- **Implementation dependency made explicit** — This amendment depends on SOP-018 for S9/S10 definitions. Must be implemented after GL-018 and SOP-018. Section 11.6 added defining pre-SOP-018 reduced behavior.
- **Section 11.7 added** — Companion Files for Governance Pack Reviews. All four pack documents must appear in RCP Field 15 when reviewing any governance-pack deliverable.
- **Field 18 strengthened** — Reviewer must not rely on any prior chat history, session memory, or accumulated tool context. Verbatim requirement added (may not be paraphrased). Motivation: weaker language in v01 left room for reviewers to supplement with context from their session memory, defeating portability.
- **Worked Example 4 updated** — DP references aligned with SOP-018 v02 sequence (DP-1 through DP-6).

### v02 to v03 — Key decisions

- **Worked Example 4 corrected** — v02 example incorrectly framed S2-Medium as Route B first, then escalated to Route C. The route matrix maps S2-Medium directly to Route C without a Route B check. The integration handler is correctly identified as an operational system file. Motivation: Example 4 is used for training and must accurately represent the route matrix.

### v03 to v04 — Key decisions

- **Section 11.2 clarified — system-file change terminology** — The SOP-015 bullet now carries a parenthetical noting that SOP-015 uses "system-file change" to refer to governance file changes, with a cross-reference to SOP-018 Section 2.4. Motivation: prevent apparent conflict between SOP-015's established "system-file change" terminology and SOP-018's more precise "governance file / operational system file" distinction.

### v04 to v05 — Key decisions

- **Section 11.2 Route B without escalation exemption added** — v04 text "A proposal authorizing implementation (from any route per the active idea routing procedure)" could be read as requiring an RCP for Route B without escalation. Corrected: "An implementation-authorizing proposal from any route that requires Review Gate under the active idea routing procedure. Route B without escalation does not require an RCP unless the Owner explicitly requests one." Motivation: Route B without escalation is intentionally lightweight (no Review Gate, no Review Gate package). Requiring an RCP for Route B would add overhead inconsistent with its design. The exemption is bounded: when any Route B escalation condition is true, the route escalates and the escalated route's RCP rules apply in full.

---

## 4. Lessons Learned

**Source:** `step-2-implementation-report-sop-018-addendum.md`

### LL-001 — Heading count versus section count in implementation reports

**Context:** Step 2 post-check 9 stated "12 sections confirmed" for GL-018. This was imprecise.

**Root cause:** The verification command `grep -c "^##"` counts all headings beginning with `##`, which includes `###`-level subsection headings. GL-018 Section 6 contains two `###` subsection headings (`### Owner (Walter Kamer)` and `### Maintainer (currently: Larry)`), which were counted alongside the nine numbered sections and the Changelog, producing a count of 12.

**Correct statement:** GL-018 contains 9 numbered sections (Sections 1 through 9), 1 Changelog, and 2 subsection headings within Section 6. The heading grep returned 12 matches. There are not 12 sections.

**Rule for future implementation reports:** When confirming section count, use `grep -c "^## "` (with trailing space) to count only top-level `##` headings, or list sections by name rather than by count. Never report a grep count as a section count without distinguishing subsection headings. Prefer: "Sections 1 through 9 and Changelog confirmed" over "12 sections confirmed."

---

## 5. Governance Pack Implementation Pattern

**Source:** Pack-level Implementation Order (SOP-018 Section 21, smoke test plan)

This is the reusable pattern for implementing a GL/SOP pair plus a SOP amendment. Follow this pattern for any future governance pack of similar structure.

### Step 1 — Implement the new GL

1. Re-confirm the proposed GL number against the live `gl-index.md` immediately before implementation.
2. Create the GL file in `Team Knowledge/Core/Guidelines/` with the exact approved content only:
   - Numbered sections as approved
   - Changelog
   - No proposal wrapper
   - No Pack-level Implementation Order
   - No Owner Decision Options
   - No Acceptance Criteria
   - No numbering re-confirmation note
3. Add the GL entry to `gl-index.md`.
4. Read back the GL file and `gl-index.md`. Confirm content matches approved proposal. Confirm no other files were modified.
5. Owner confirms Step 1 complete before Step 2 begins. No advancement without explicit Owner confirmation.

### Step 2 — Implement the new SOP

1. Re-confirm the proposed SOP number against the live `SOP-index.md` immediately before implementation.
2. Create the SOP file in `Team Knowledge/Core/SOPs/` with the exact approved content only (same exclusions as Step 1).
3. Add the SOP entry to `SOP-index.md`.
4. Read back the SOP file and `SOP-index.md`. Confirm GL from Step 1 is unchanged.
5. Owner confirms Step 2 complete before Step 3 begins.

### Step 3 — Implement the SOP amendment

1. Apply only the exact amendment text. No additional changes.
2. Read back the amended SOP in full. Confirm: new sections present, existing sections unchanged, no wrapper content introduced.
3. Confirm the GL (Step 1) and the new SOP (Step 2) remain unchanged.
4. Owner confirms Step 3 complete before Step 4 is considered.

### Step 4 — Execute smoke test (only with separate Owner authorization)

1. Smoke test requires explicit Owner authorization in a dedicated session. Approval of the smoke test plan is not authorization to execute.
2. Execute all test cases as logical governance walkthroughs. No real execution.
3. Produce a smoke test execution report.
4. Owner accepts the execution report.

### Hard constraints across all steps

- Each step requires individual Owner confirmation before the next step begins.
- No step may be skipped or reordered.
- No real execution occurs during the smoke test.
- No files outside the authorized scope are created, modified, moved, or deleted at any step.
- No database writes occur unless authorized by a pre-approved routine.

---

Delivered on: 2026-06-05
Delivered at: Team Knowledge/Core/Documents/
