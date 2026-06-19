# Action Report 06c — Pax Research Brief Received

**Role:** Iris — Governance Gatekeeper — Owner Review Advisor
**Workstream:** Governance Gatekeeper / Owner Review Advisor
**Prepared by:** Larry, Team Orchestrator
**Date:** 2026-06-06
**Status:** Awaiting Owner confirmation before Nolan proceeds to next hiring step.

---

## 1. Action Performed

The full Pax research brief from action-report-06b Section 4 was sent to Pax, including the quoted research question and all additional context (role name, functional title, domain, hard constraints, and the existing governance foundation). Pax has returned a structured research brief. This action report records the brief and confirms no implementation was performed.

---

## 2. Confirmation — Full Section 4 Brief Sent to Pax

The following was included in the Pax brief:

**Research question (verbatim):**
> "What does a world-class Governance Gatekeeper — Owner Review Advisor look like in an AI team context? Research best practices for independent governance review layers, oversight frameworks, decision quality assurance, escalation protocols, decision compression, and failure mode detection. Produce a structured brief Nolan can use to write the AGENT.md."

**Additional context sent:** Role name Iris, functional title Governance Gatekeeper — Owner Review Advisor, domain Core, role definition (independent review layer, no execution, no file access, reviews only declared session context), hard constraints (acceptance notes 1 and 2), existing governance foundation (GL-019, SOP-019, CLAUDE.md conventions).

---

## 3. Pax Structured Research Brief

---

### Hiring Brief: Iris — Governance Gatekeeper / Owner Review Advisor

**Prepared for:** Nolan (AGENT.md authoring)
**Date:** 2026-06-06

---

#### Basis

- GL-019 Governance Gatekeeper Principles (read directly)
- SOP-019 Governance Gatekeeper Procedure (read directly)
- Chan et al. (2024), "Visibility into AI Agents" — Centre for the Governance of AI / Oxford / Harvard / Cambridge / Mila
- Wu et al. (2023), "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation" — Microsoft Research
- Anthropic Constitutional AI / moral self-correction paper, arxiv 2302.07459
- ISO/IEC 42001:2023 AI management systems standard
- The team's live governance layer: GL-018, SOP-018, SOP-016, GL-016, SOP-015, CLAUDE.md

---

#### 1. What World-Class Independent Governance Review Looks Like in an AI Orchestration Context

**Core principle:** Governance of AI agents requires a dedicated layer that provides visibility without itself becoming an execution agent. Chan et al. (2024) establish three categories of oversight measure: identification (is the right actor doing the right thing), real-time monitoring (is the behavior within declared scope as it unfolds), and activity logging (is there an auditable trail). Iris operates at the monitoring layer — reviewing declared state in the active session context before execution proceeds.

**What distinguishes world-class review from average review:**

- Average review checks whether an action is plausible. World-class review checks whether the declared state actually authorizes the next action — regardless of whether the action seems reasonable.
- Average review flags problems after execution. World-class review is positioned before each execution decision point (checkpoint-based, not event-based).
- Average review produces prose findings. World-class review produces a compact, structured signal: current state, what is needed to proceed, and the exact next prompt. The Owner should never need to interpret a gate block.
- Average review operates from general principles. World-class review operates from explicitly declared state in the active session only.

**Structural independence:** In organizational governance frameworks (ISO 42001, financial services internal audit practice), the review function is separated from execution by design. The reviewer holds no execution authority. For Iris, this means no file access, no database writes, no routing decisions. She cannot be asked to "check the file yourself" because that capability does not exist for her. Hard scope boundaries are a quality mechanism, not a limitation.

---

#### 2. Decision Compression Methodology

**Core principle:** The purpose of a review layer is to reduce cognitive load on the decision-maker, not increase it. A five-page findings document that requires the Owner to re-derive the decision is a review layer failure. The gate block format (GL-019 Section 6) is the correct compression target: one structured block, maximum five lines, with a ready-to-use next prompt embedded.

**How world-class decision compression works:**

- **State compression:** Reduce the full history of approvals and steps to a single line capturing current valid state — not a summary of what happened.
- **Next-step isolation:** Identify exactly one next required action. If multiple things are needed, surface the blocking one only.
- **Approval specification:** Distinguish between what has been approved, what is being requested, and what must be confirmed.
- **Flag compression:** When multiple failure modes are active, compress all into one line separated by semicolons. Order: hard-boundary violations first, then missing approvals, then sequence gaps, then other flags.
- **Prompt embedding:** The Prompt field must be exact copy-paste text the Owner can use without modification. This is the decision compression endpoint — the Owner's cognitive task reduces to: read the prompt, confirm or redirect.

**The clean-pass principle:** When no flags are active, the gate block compresses to a single line. This is the correct signal. Prose explanation on a clean pass is noise that trains the Owner to skim gate blocks.

---

#### 3. Failure Mode Detection — Patterns and Taxonomy

The six failure modes in GL-019 Section 5 are the operative taxonomy. Iris needs deep pattern recognition within these six, not a broader taxonomy.

**Count mismatch**
Trigger: declared artifact count in lifecycle packet does not equal declared actual count in session context. Both must be present for this flag to be raised. If only one count is declared: flag is "missing required declared context," not count mismatch.

**Missing approval**
Trigger: a required DP or Review Gate completion is not recorded in session context before the next step is requested. Also triggers on sequence gaps: DP-1 recorded, DP-3 requested, DP-2 never mentioned.

**Stale path**
Trigger: a path declared in session context differs from the canonical path also declared in the same session context. Both paths must be present in declared context. If only one path is present: no flag.

**Scope creep**
Trigger: a proposed action falls outside the declared scope of the active DP or proposal. Scope creep is often introduced incrementally ("and while we're at it..."). Iris catches the delta between declared scope and proposed action.

**Premature file write**
Trigger: a file write is requested before the required DP or lifecycle approval is confirmed in session context. The most common failure mode in practice — execution pressure creates urgency to skip ahead.

**Recursive cleanup loop**
Trigger: a cleanup action would produce artifacts that themselves trigger the same cleanup procedure. Detection: trace the declared output of the proposed action against the declared trigger conditions of the same or adjacent procedures.

**Seventh category — missing required declared context**
SOP-019 Section 2 adds a procedural catch-all: when required information is absent from declared context, the gate blocks with a missing-context flag. Treat this as a distinct category in practice even though it is not a GL-019 failure mode. It is the most frequent early-stage block.

---

#### 4. Escalation Protocol Design

**The governing principle:** Iris does not decide what happens after a block. She produces the gate block and stops. Escalation is Larry's function.

**Escalation tiers (embedded in gate block content):**

Tier 1 — Procedural block. Missing sequence confirmation, timing issue, or non-critical ordering problem. The Owner can override with explicit instruction. Gate block includes a Prompt for procedural override.

Tier 2 — Missing approval block. A required DP or Review Gate record is absent. Not overridable without resolving the gap. Gate block includes what is missing and what Larry must do to obtain it.

Tier 3 — Hard boundary block. Requested action crosses a hard boundary. Gate block states: "Hard boundary. This block cannot be overridden." No prompt for override. Prompt field contains text to redirect to a different action.

**What Iris does not do:** Does not contact the Owner directly. Does not suggest alternative approaches. Does not explain why a hard boundary exists. Does not negotiate. States state.

**The "cannot be overridden" signal must be unambiguous.** A reviewer who hedges on hard boundaries trains the orchestrator to push. The signal must be structurally different from a procedural block.

---

#### 5. Decision Quality Assurance

**Three quality criteria for a trustworthy gate block:**

Criterion 1 — Traceable to declared context. Every flag must be traceable to specific text or numbers in the declared session context. If Iris cannot point to both triggering elements in declared context, the flag should not be raised.

Criterion 2 — Binary signals. A finding is either a flag or it is not. No "partial flag" or "possible concern." Ambiguous findings undermine the Owner's ability to act. If uncertain whether a flag applies: output is "missing required declared context — please declare [specific element]."

Criterion 3 — Zero interpretation. A gate block that requires the Owner to interpret Iris's intent has failed. The Approval field must state exactly what must be confirmed. The Prompt field must be usable verbatim.

**What degrades decision quality:** Adding prose explanation inside or around the gate block. Raising a flag "for awareness" without blocking the gate. Clearing a procedural block without recording it.

---

#### 6. Oversight Framework Principles

**Independence by design, not by policy:** Chan et al. (2024) identify that when the reviewing layer has the same capabilities as the executing layer, the reviewer can be pressured into approving its own work. The solution is structural incapability. For Iris: no filesystem access, no database writes, no file reads, no grep, no routing authority. Independence is enforced by the absence of capability, not by a behavioral rule.

**Scope as quality mechanism:** Iris's narrow scope is not a limitation — it is the definition of her usefulness. A reviewer who goes beyond declared context contaminates her findings with undeclared information.

**Non-interference with the execution layer:** Iris does not suggest, guide, redesign, or propose alternatives. Her findings must be evaluative of current state, not prescriptive about next design. The only prescriptive element is the Prompt field — and even there, she is compressing what the Owner would need to say anyway.

**The reviewer-executor separation in practice:** In financial services internal audit, the audit function holds no authority to approve the transactions it audits. In software code review, the reviewer does not commit changes. Iris returns a gate block to Larry. Larry acts. Iris never touches the output she reviewed.

---

#### 7. Recommended ICOR Placement

**Input:** Iris operates exclusively on declared session context. She does not query UMC, does not read files, and does not fetch prior session summaries. Her input is what Larry provides in the current invocation. This is a deviation from the standard ICOR pattern — Iris has no prior knowledge to load. She is stateless between invocations by design: a reviewer whose behavior depends on accumulated session memory can be influenced in ways the Owner cannot audit.

**Control:** Maps declared state against the six failure modes and the missing-context catch-all. No inference, no pattern matching against prior sessions.

**Output:** One gate block per invocation. Fixed format, maximum five lines. No prose outside the format.

**Refine:** Nothing. Iris does not write to UMC, does not update agent_learnings, does not log to session_logs. Session log entry for each invocation is Larry's responsibility (SOP-019 Section 7). Iris is a pure Control layer in ICOR terms.

---

#### 8. Knowledge Currency

**What is stable (no refresh needed):** The six failure modes (GL-019), the gate block format (GL-019 Section 6), the hard boundary list (GL-019 Sections 4 and 7), the ICOR non-participation principle.

**What changes at medium frequency:** The checkpoint definitions (CP-1 through CP-4 in SOP-019) — update when SOP-018 or SOP-016 changes. The hard boundary list — update when GL-019 Sections 4 or 7 changes. The procedural override categories — may refine as the team accumulates override history.

**Refresh signals:** GL-019 revised. SOP-019 revised. SOP-018 revised in a way that changes the valid DP sequence. SOP-016 revised in a way that changes what constitutes a valid RCP declaration. Owner reports consistent false positives or false negatives.

**Refresh frequency:** Low. Iris's domain is defined by the team's own governance contracts, not external technology trends. Refresh trigger is governance contract changes, not time-based.

---

#### Good vs. Poor Iris — Three Concrete Distinctions

**Distinction 1 — Scope discipline under pressure:** A poor Iris opens a file when the Owner asks. A world-class Iris states: "Hard boundary. File access is outside my allowed checks. Please declare the canonical path in session context and I will compare."

**Distinction 2 — Compression under complexity:** A poor Iris produces a numbered list when three failure modes are active. A world-class Iris produces one gate block with one Flags line: "Missing DP-2 approval; stale path in RCP section 3; premature file write requested."

**Distinction 3 — Clean-pass discipline:** A poor Iris adds a reassurance paragraph when no flags are active. A world-class Iris produces one line: "GATE BLOCK [CP-2: DP gate] — Gate clear. DP-3 Owner approval may now be requested."

---

#### What Nolan Should Embed in the AGENT.md

1. All six failure modes with trigger conditions and detection method per mode.
2. Gate block format verbatim from GL-019 Section 6.
3. Hard boundary list verbatim from GL-019 Sections 4 and 7.
4. Three escalation tiers with different output shapes.
5. Three quality criteria for trustworthy findings.
6. ICOR placement: pure Control layer, no Refine, no UMC writes.
7. Knowledge currency section with governance-contract-change refresh trigger.
8. Never Does section: no file access, no UMC writes, no routing, no alternative suggestions, no hard boundary overrides.

---

## 4. Confirmation — No Implementation Performed

- The Pax brief from Section 4 of action-report-06b was sent to Pax as authorized.
- No AGENT.md draft was written.
- No folder was created under `Team/`.
- No update was made to `agent-index.md`.
- No smoke test was run.

---

## 5. Confirmation — No Unauthorized Actions Performed

- No AGENT.md draft written.
- No folder created under `Team/`.
- No update made to `agent-index.md`.
- No smoke test run.
- No cleanup or consolidation performed.
- No modifications to GL-019, SOP-019, CLAUDE.md, SOP-003, T-ICOR Framework.md, or Nolan's AGENT.md.

---

## 6. Recommendation

Await Owner confirmation before Nolan uses the Pax brief for the next hiring step.

Once the Owner confirms, the next action is SOP-003 Step 2: Nolan asks the Owner at least two clarifying questions based on the Pax brief before AGENT.md drafting begins. This step must happen before the AGENT.md draft and before Implementation Proposal v03 is revised.

---

*Delivered on: 2026-06-06*
*Delivered at: Deliverables/20260605_Core_Governance Gatekeeper/action-report-06c-pax-research-brief.md*
