# Session log — Agile delivery pipeline — Phoebe, Sloane, TDD enforcement

**Date:** 2026-06-25
**Agent:** Larry
**Domain:** Team
**DB id:** 254

---

## What happened

Sparred on embedding Scrum practices in the myPKA agent team. Established SRP (Single Responsibility Principle) as the governing rule for agent design — each specialist owns exactly one gate. Onboarded Phoebe (Product Strategist, G2) and Sloane (Delivery Lead, G4) via Pax research then Nolan AGENT.md authoring. Built the full G1-G6 gate sequence. Enforced TDD structurally: Sloane produces mandatory test spec at G4, Devon writes failing tests first and cannot close G5 without all feature tests green + regression green + test report. Smoke tests removed as irrelevant for single-environment myPKA. Procedures extracted from AGENT.md files into GL-024 and SOPs 016-018. Forge template folder archived from Team Inbox.

---

## Decisions

- Narrow roles: Phoebe (scope/value, G2), Sloane (slicing/scenarios, G4), Devon (build, G5) — no overlap
- Owner (not Vera) is G6 for myPKA self-development
- TDD is structural: Sloane's test spec is the contract Devon builds against — not a guideline
- Smoke tests removed — single-environment setup; replaced by "verify end-to-end in running system" in Devon's Definition of Done
- AGENT.md = identity + mandate + boundaries only; procedures live in SOPs
- Phoebe routes dynamically after G2 (Kai + Sloane for builds, Pax for research, Vera for business validation)
- Sloane routes dynamically at G4 (Devon / Sasha / Finn per domain, Larry specifies)

---

## Actions taken

- Pax briefed: researched Phoebe and Sloane roles against agile primary sources + Forge template
- Nolan briefed: wrote AGENT.md for Phoebe and Sloane, updated agent-index.md and CLAUDE.md
- Phoebe AGENT.md + Sloane AGENT.md: dynamic routing added (not hardcoded to Kai/Devon)
- Devon AGENT.md: TDD hard rules added — no start without G4 test spec, G5 not done without tests green + test report
- Sloane AGENT.md: test spec as mandatory G4 output added
- Smoke test definition removed from Sloane G4 output and Devon Definition of Done
- GL-024 created: delivery pipeline gate reference (G1-G6)
- SOP-016 created: Feature Brief procedure (Phoebe)
- SOP-017 created: Vertical slice + Gherkin standards (Sloane)
- SOP-018 created: TDD build order + G5 criteria (Devon)
- Phoebe, Sloane, Devon AGENT.md files trimmed — procedures replaced by SOP references
- Forge folder archived: Deliverables/Archive/20260625_Core_Forge template/

---

## Open items

None from this session.
