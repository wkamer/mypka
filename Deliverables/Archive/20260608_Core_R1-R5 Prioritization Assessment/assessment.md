# Prioritization Assessment — R1 through R5

**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-08
**Source:** `Deliverables/20260608_Core_UMC Archive Eligibility Chain Process Review/process-review.md`
**Scope:** Read-only assessment. No proposals, no implementation plans, no file modifications, no database changes.

---

## 1. Executive Summary

Five recommendations were identified from the UMC archive eligibility chain process review. The chain produced four deliverable folders where two were sufficient, and included a v01-to-v02 iteration cycle that was avoidable.

The root cause was a single conflation: Larry treated a retention decision (append knowledge to an existing document before archiving) as an implementation decision (structural change requiring full governance triage). All unnecessary overhead in the chain flows from that conflation.

**The highest-value fix is R1.** A minimal-retention-first gate in GL-013 would have prevented folders 2 and 3 from being created and would have eliminated three Owner review interactions. R1 is independent, targets a single document, and resolves approximately 75% of the identified overhead.

**R5 is the fastest additional win.** It closes an avoidable iteration cycle with a one-line behavioral rule. Implementation cost is near zero.

**R2 and R4 add systemic robustness** but are not urgent after R1 is in place. They address the same problem class from different angles and can be deferred.

**R3 depends on an external precondition** (Iris AGENT.md being operational) and becomes a secondary safety net once R1 is implemented. It should not block or delay R1.

**Recommended stopping point for minimum effective implementation:** R1 + R5.

---

## 2. Prioritized Recommendation Table

| Rank | Rec | Title | Impact | Cost | Dependencies | Priority |
|---|---|---|---|---|---|---|
| 1 | R1 | Minimal-Retention-First Gate | Highest | Low | None | Implement first |
| 2 | R5 | Language Rule at Draft Time | Low | Minimal | None | Implement alongside R1 |
| 3 | R2 | Chain-Awareness in GL-017 | Medium | Low | None | Implement after R1 |
| 4 | R4 | Separate Retention from Implementation | Medium | Medium | None (but partial overlap with R1) | Implement after R1, assess residual gap |
| 5 | R3 | Iris Trigger for Archive Eligibility Chains | Medium | External dependency | Iris AGENT.md operational | Implement last; do not block on this |

---

## 3. Individual Recommendation Analysis

### R1 — Minimal-Retention-First Gate

**What it does:** Adds a two-question gate to the archive eligibility process. Before any eligibility chain proceeds past the initial analysis, it must answer: is the retention action an append to an existing document? If yes, go directly to write proposal — no governance triage, no LC/GC classification, no GL-018/SOP-019 scoring. Only if the retention action requires a new system component does the governance path activate.

**Impact on deliverable folder growth:** High. In the current chain, this gate would have intercepted the flow after Folder 1, routed P2 and P5 directly to a write proposal (Folder 4), and prevented Folders 2 and 3 from being created. Net reduction: 2 folders per archive eligibility chain involving retention-only captures.

**Impact on Owner review load:** High. Three Owner review interactions were required for Folders 2, 3, and 4 sequentially. With R1, only one Owner review interaction is required (the write proposal). Net reduction: 2 interactions per chain.

**Impact on governance loops:** High. The entire GL-022 / GL-018 / SOP-019 classification exercise was triggered by the absence of this gate. R1 prevents the trigger condition from arising.

**Implementation location:** GL-013 (one new section defining the gate) and CLAUDE.md (one behavioral rule for Larry).

**Implementation cost:** Low. Two documents, one rule each. No new infrastructure, no specialist involvement required.

**Standalone value:** Yes. R1 is complete and effective without any other recommendation being implemented.

---

### R5 — Apply Language Rule at Draft Time

**What it does:** Reinforces that system-facing documents (proposals, GLs, SOPs) must be drafted in English from the first word. The language check is not a post-draft review. If Larry is about to draft a system document in Dutch, he stops before producing any text.

**Impact on deliverable folder growth:** None. This does not prevent folders from being created.

**Impact on Owner review load:** Low. Eliminates one avoidable v01-to-v02 iteration cycle per affected document. In the current chain, this would have removed one Owner review interaction.

**Impact on governance loops:** None.

**Implementation location:** CLAUDE.md (one behavioral rule). GL-014 already states the rule; this is a draft-time trigger, not a new rule.

**Implementation cost:** Minimal. One behavioral rule added to CLAUDE.md. No documents, no specialist involvement.

**Standalone value:** Yes. Effective immediately upon implementation.

**Note:** R5 does not become unnecessary if any other recommendation is implemented. It addresses a different failure mode (language compliance at draft time) that is orthogonal to deliverable growth.

---

### R2 — Chain-Awareness in GL-017

**What it does:** Adds one clause to GL-017: if an artifact is a decision package, triage document, or assessment that exists in service of an ongoing chain that already has a home folder, it is G2 (file inside existing folder) regardless of content complexity. This closes the loophole that allows intermediate chain artifacts to pass the G1 test by their apparent analytical depth when they are structurally G2 by their role in the chain.

**Impact on deliverable folder growth:** Medium. R1 prevents the specific scenario in this chain (governance triage for a retention decision). R2 catches the broader pattern: any intermediate chain artifact that would otherwise become a standalone folder. Value increases in chains where governance triage is legitimately required but produces multi-step intermediate documents.

**Impact on Owner review load:** Low to medium. Folder reduction does not directly reduce Owner review interactions (those happen at the write proposal level), but it reduces the surface area the Owner must navigate in Deliverables/.

**Impact on governance loops:** Low. R2 does not prevent governance loops; it limits their artifact footprint.

**Implementation location:** GL-017 (one new clause).

**Implementation cost:** Low. One document, one clause.

**Dependency on R1:** R2 is complementary, not dependent. R1 addresses the archive eligibility scenario; R2 addresses any chain type. After R1, R2 adds robustness for scenarios R1 does not cover.

**Does R1 make R2 unnecessary?** No. R1 prevents the specific trigger that produced Folders 2 and 3. R2 prevents the same class of artifact from occurring in any other chain context where the governance path is legitimately active. Both are needed for full coverage.

---

### R4 — Separate Retention from Implementation in Governance Triggers

**What it does:** Adds an explicit exemption clause to GL-018, GL-022, and SOP-019: retention-only actions (captures of existing knowledge into existing documents, no new system components, no new behavior, no new infrastructure) are not subject to the governance triage path. A retention action requires a write proposal and Owner authorization only.

**Impact on deliverable folder growth:** Medium. Prevents governance frameworks from being applied to retention decisions in any context where they might be triggered, not just archive eligibility chains.

**Impact on Owner review load:** Medium. Same reach as R1 but from the governance framework side rather than the archive eligibility entry point.

**Impact on governance loops:** High. Directly blocks the conflation at the framework level, making it impossible for GL-018/GL-022/SOP-019 to be applied to a retention action in any context.

**Implementation location:** GL-018 (one clause), GL-022 (one clause), SOP-019 (one clause). Three documents.

**Implementation cost:** Medium. Three documents, each requiring Owner-authorized edits.

**Overlap with R1:** R1 fixes the behavior at the archive eligibility entry point. R4 fixes the same behavior at the governance framework level. After R1, the archive eligibility scenario cannot reach GL-022/GL-018/SOP-019 inappropriately. The remaining value of R4 is: other contexts (non-archive, non-eligibility) where a retention decision might accidentally enter the governance triage path.

**Does R1 make R4 unnecessary?** Partially. R1 eliminates the archive eligibility scenario. R4 is needed for full systemic coverage — any context where retention and implementation might be conflated. However, the probability of that pattern recurring in non-archive contexts is unknown from this review. R4 can safely be deferred after R1 to assess residual need.

---

### R3 — Iris Trigger for Archive Eligibility Chains

**What it does:** Defines a trigger in Iris scope: any chain that produces more than one deliverable folder in service of a single archive eligibility question triggers Iris review before the write proposal reaches the Owner.

**Impact on deliverable folder growth:** Low. Iris review does not prevent folder creation; it reviews proposals before Owner presentation. R3 would have caught the over-expansion before the Owner saw Folders 2 and 3, but would not have prevented them from being created.

**Impact on Owner review load:** Medium. Iris filters over-expanded proposals and may redirect before Owner interaction, reducing Owner exposure to unnecessary review rounds.

**Impact on governance loops:** Medium. Iris can identify and flag when a chain has entered governance territory inappropriately, creating a human checkpoint before the Owner sees the output.

**Implementation location:** Iris AGENT.md (scope definition).

**External dependency:** GL-021 Section 9 notes that the Iris AGENT.md update (LC-Iris-001) is currently marked Pending. If Iris AGENT.md does not exist or lacks operational scope definition, R3 cannot be implemented until that prerequisite is resolved. This may require Nolan involvement.

**After R1 is implemented:** The trigger condition for R3 (chain produces more than one folder for archive eligibility) becomes significantly rarer. R3 shifts from a primary control to a secondary safety net. It retains value for other chain types.

**Implement R3 last.** Do not allow R3's external dependency to block R1 or R5.

---

## 4. Dependency Map

```
R1 ─────────────────── independent, implement first
R5 ─────────────────── independent, implement alongside R1
R2 ─────── after R1 ── complements R1, no overlap, low cost
R4 ─────── after R1 ── partial overlap with R1; assess residual gap before implementing
R3 ─────── after all ── depends on Iris AGENT.md operational; secondary safety net after R1
```

No recommendation blocks another. R1 reduces the urgency of R4 and R3 but does not eliminate their value.

---

## 5. Redundancy Analysis

| Pair | Redundant? | Assessment |
|---|---|---|
| R1 makes R4 unnecessary | Partially | R1 fixes archive eligibility entry point; R4 fixes governance framework level. After R1, R4's value is residual coverage for non-archive contexts. Not unnecessary, but deferrable. |
| R1 makes R3 unnecessary | No | R1 prevents the trigger condition; R3 intercepts when it fires anyway. After R1, R3 is a safety net, not a primary control. Still worth implementing once Iris AGENT.md is operational. |
| R1 makes R2 unnecessary | No | R2 covers broader pattern (any chain type); R1 covers archive eligibility only. Complementary. |
| R2 makes R4 unnecessary | No | Different targets: R2 addresses artifact granularity; R4 addresses governance framework scope. |
| R5 overlaps with any | No | R5 addresses a different failure mode (draft language) orthogonal to all others. |

---

## 6. Expected Impact Per Recommendation

| Rec | Folders prevented per chain | Owner interactions prevented | Governance loops blocked |
|---|---|---|---|
| R1 | 2 (for retention-only chains) | 2 | Full GL-022/GL-018/SOP-019 activation |
| R5 | 0 | 1 (per Dutch-first draft) | None |
| R2 | Variable (chain-type dependent) | 0 direct | None |
| R4 | 0 direct | 0 direct | Full across all governance contexts |
| R3 | 0 (Iris review after creation) | 1-2 (Owner redirect before review) | Partial (Iris-intercepted loops) |

---

## 7. Recommended Implementation Roadmap

**Phase 1 — Minimum effective (implement now):**

- R1: Add minimal-retention-first gate to GL-013 and one behavioral rule to CLAUDE.md.
- R5: Add draft-time language trigger to CLAUDE.md.

Expected outcome after Phase 1: Archive eligibility chains collapse from 4 folders to 2. Owner review interactions reduce from 4 to 2 per chain. Avoidable iteration cycles eliminated.

**Phase 2 — Systemic robustness (implement after Phase 1 is confirmed stable):**

- R2: Add chain-awareness clause to GL-017.
- R4: Add retention exemption to GL-018, GL-022, and SOP-019. Assess residual need after observing one post-R1 chain.

Expected outcome after Phase 2: Pattern cannot recur in any chain type, not just archive eligibility. Governance frameworks explicitly exempt retention actions system-wide.

**Phase 3 — Secondary safety net (implement when Iris AGENT.md is operational):**

- R3: Define Iris trigger for multi-folder chains. Do not delay Phase 1 or Phase 2 on this.

Expected outcome after Phase 3: Iris provides an automatic filter for any chain that escapes R1 or R2. Full defense-in-depth.

---

## 8. Recommended Stopping Point

If only the highest-value improvements are implemented, stop after Phase 1 (R1 + R5).

R1 eliminates the structural cause of the chain's overhead. R5 eliminates the avoidable iteration cycle. Together they reduce the identified overhead by approximately 75% with minimal implementation cost and no specialist involvement.

Phase 2 and Phase 3 add robustness and broader coverage but do not materially change the outcome for the archive eligibility scenario that triggered this review.

---

Delivered on: 2026-06-08
Delivered at: session
