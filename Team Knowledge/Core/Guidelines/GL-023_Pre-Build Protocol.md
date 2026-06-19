# GL-023 — Pre-Build Protocol

**Owner:** Larry  
**Applies to:** All specialists  
**Trigger:** Any build, script, integration, GL, SOP, AGENT.md, or system change  
**Last updated:** 2026-06-15

---

## Principle

Nothing is built until five questions are answered in sequence. The protocol runs in conversation — no file is written until all five steps are complete. This rule applies to every specialist and every output type. There are no exceptions based on scope, urgency, or simplicity.

---

## The Five Steps

### Step 1 — Interview (Discovery)

Before a spec is written, the specialist interviews the owner or reads the brief carefully to surface:

- What is the core problem being solved?
- Who is this for — and who is it explicitly NOT for?
- What does success look like?
- What is out of scope?

If the request comes via Larry's brief, Larry runs the interview before briefing the specialist. The specialist does not start from an incomplete brief.

### Step 2 — Spec

The specialist writes a structured spec covering:

- What it does
- Who it is for / not for
- What success looks like
- What is out of scope
- For each build step: what the step does and what the key decision is at that step

The spec is presented to the owner before any file is written. The owner answers yes, no, or correction.

### Step 3 — Verify Plan

Before building: state how the output will be verified.

The verify plan answers: "How will we know this works — before and after delivery?"

Verification criteria per output type:

| Output type | Verification method |
|-------------|-------------------|
| Script / integration | Dry-run or test with non-destructive input; confirm expected stdout/result before live run |
| GL / SOP / WS | State the behavioral test: which agent action does this change, and how do we confirm the new behavior is active? |
| AGENT.md | Smoke test: give the specialist a representative task and confirm output matches intent |
| Database write | Read-back confirmation: query the written row before proceeding to dependent steps |
| CLAUDE.md change | Name the session in which the new rule will first be exercised and what observable behavior confirms it |

### Step 4 — Tool Check

Based on what is being built: identify which tools help with verification.

Ask: "What internal or external tools can verify this output?"

Examples:
- Scripts: Bash dry-run, Python unit assertions, log output comparison
- Integrations: API response validation, staging endpoint, Postman / curl
- Database: SQLite query read-back, row count check
- GL / SOP: cross-reference against existing rules for conflicts
- AGENT.md: role-overlap check against existing specialist roster

The specialist names at least one verification tool before building starts.

### Step 5 — Murphy Scan

Anything that can go wrong, will go wrong. Before building, the specialist runs a Murphy scan:

- What is the worst realistic failure mode for this output?
- What happens to downstream systems or agents if this fails mid-execution?
- What is the rollback or recovery path?
- Are there hard-to-reverse actions in this build? If yes: name them explicitly and confirm the order of operations minimizes risk.

The Murphy scan result is stated in the conversation before the first file write.

---

## Enforcement

**Larry's role:** Larry runs Steps 1 and 2 before briefing any specialist. The brief Larry sends must include: the spec, the verify plan, and the Murphy scan findings. A brief without these three is incomplete — the specialist must request them before starting.

**Specialist's role:** On receiving a brief, confirm Steps 3–5 are present. If absent: surface the gap to Larry before starting.

**Violation trigger:** If any specialist begins a build without completing Steps 1–5, stop immediately, complete the missing steps, and note the deviation in the session log.

---

## Waiver

The owner may waive this protocol for a specific task by stating so explicitly. A general instruction to "just do it" or time pressure alone does not constitute a waiver. State the waiver in the session log.
