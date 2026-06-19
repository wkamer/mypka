# How to Hire a New Team Member

## Purpose

Hire a world-class specialist for the team in a repeatable way. Every specialist must perform at the highest level in their domain — not just fill a structural role.

## Trigger

Larry identifies a gap in the roster (`Team/agent-index.md`) and delegates the hiring task to Nolan.

## Steps

1. **Pax researches the role (mandatory).** Before Nolan writes anything, Larry briefs Pax with the following research question:

   > "What does a world-class [role] look like? Research the best practitioners, frameworks, decision-making standards, knowledge base, and working methods that define excellence in this domain. Produce a structured brief Nolan can use to write the AGENT.md."

   Pax delivers a research report. Nolan does not write the AGENT.md until this brief is received. The quality of the specialist depends on the depth of this brief.

2. **Clarify the role.** Nolan asks the owner at least two clarifying questions based on the Pax brief:
   - What specific output does this specialist produce for the team?
   - Where does this role sit in the ICOR cycle?

3. **Check for overlap.** Read `Team/agent-index.md`. If a similar role already exists, flag the overlap to the owner and ask whether to split, merge, or rename. Do not proceed until the owner decides.

4. **Create the folder.** Path: `Team/<First Name> - The <Role Title>/`. Title Case, exact convention.

5. **Write AGENT.md.** Place it inside the new folder. Required sections:
   - `## Model` — always `claude-sonnet-4-6` unless Larry specifies otherwise
   - `## Identity` — who this specialist is and what makes them world-class
   - `## Role` — scope and boundaries
   - `## Responsibilities` — specific deliverables
   - `## Domain Knowledge` — key frameworks, standards, and methods from the Pax brief embedded directly
   - `## ICOR Framework` — which phase, what input, what output, which knowledge bucket
   - `## Personality` — max three sentences
   - `## Standing Instruction` — always include: "Good is good enough. Do exactly what is asked — no more."
   - `## Links` — relevant files, databases, indexes

   Use instruction language. No marketing copy, no adjective stacking.

6. **Update the roster.** Add a new row to `Team/agent-index.md`.

7. **Smoke test.** Ask the new specialist a domain-specific question that tests their embedded knowledge. A world-class specialist answers with depth, not just structure. If the answer is generic, rewrite the Domain Knowledge section and retest.

8. **Define knowledge refresh.** Before closing the hire, Nolan documents in the AGENT.md:
   - A `## Knowledge Currency` section: what changes in this domain, at what frequency, and which signals trigger an update
   - The refresh cadence: high-frequency (monthly), medium (quarterly), low (annually)

   A specialist without a defined refresh cadence will become outdated. This section is mandatory.

9. **Report back to Larry.** Who was hired, what domain knowledge was embedded, what the refresh cadence is, whether they passed the smoke test.

## Quality Bar

A world-class hire has deep domain knowledge embedded in the AGENT.md — not just a role description. The Pax brief is the source of that depth.

A bad hire has a bloated AGENT.md full of structure but no substance. If the smoke test produces a generic answer, the Domain Knowledge section is the problem — rewrite it with specifics from the Pax brief.
