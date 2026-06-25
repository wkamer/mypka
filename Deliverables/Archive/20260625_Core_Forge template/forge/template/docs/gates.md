# Gates

Work advances through gates. Each gate has an owner and an exit condition.
Gates are **tiered**: small, reversible changes take the *fast lane* (gates 2,
3 and 6 collapse into a single Arch+owner ack); architectural, risky, or
irreversible work takes the *deep lane* (every gate, in full). Reversibility
decides the lane (Bezos one-way vs two-way doors).

| # | Gate | Owner | Exit condition |
|---|------|-------|----------------|
| 0 | **Walking skeleton + spikes** | Arch | Thinnest end-to-end path runs in a real environment; key architectural risks spiked before feature work. |
| 1 | **Discovery-first** | Larry | Problem explored conversationally. No files, no stack, no code during ideation. |
| 2 | **Concept sign-off** | Phoebe → owner | Concept brief approved by the owner before architecture. |
| 3 | **Arch-before-code** | Arch | Target architecture + ADR logged; threat-model-lite done; contested calls get an RFC first. No inherited code adopted without sign-off. |
| 4 | **Test-first** | Vera | BDD scenarios → fixtures → code. Tests cover **persistence round-trip + multi-turn / state-survives-a-boundary**, not just happy path. Golden assertions are human-owned; the agent writing tests is not the agent writing the code. |
| 5 | **Quality gate** | Quinn | CI green: lint + tests + coverage threshold + SAST + SCA + secrets scan + SBOM. **Evals green for any LLM/agent component.** See `QUALITY_GATE.md`. |
| 6 | **UX / use-case approval** | UX lead | _Active only if the project has a human-facing surface._ Use case + interaction reviewed; WCAG 2.2 accessibility checked. |
| 7 | **Real-environment acceptance** | Quinn → owner | Slice verified live in a real (non-test) environment before it is "done". CI validates; live testing is the real gate. |

## Always-on principles
- **Proactive challenge** — every agent surfaces gaps and better options unasked.
  Made structural by a red-team/adversarial review step on plans, threat models,
  and evals (agents tend to agree; challenge must be a mechanism, not a vibe).
- **Proactive admin** — CHANGELOG, BACKLOG, and a retro are updated at every
  milestone. Prefer auto-generated docs (CHANGELOG from conventional commits)
  over manual prose.
- **Documentation review and consolidation cycle** — run at milestones to retire
  stale docs (this exact name).

## Runtime truth (the post-merge blind spot, covered by design)
- **Observability**: structured logs + OpenTelemetry traces/metrics + SLOs.
- **Flow metrics**: DORA (lead time, deploy freq, change-fail rate, recovery
  time, rework rate) so the gates can be proven to help.
- **Evals + prompt/agent versioning**: agents and prompts are code — versioned,
  diffed, and regression-tested in CI.

## Safety kit (templated lessons)
- Dev/prod isolation; verify-mode-before-test; deploy enforces the safe mode.
- Secrets split: `.env` (config) vs `.env.secrets` (never committed).
- Build-context hygiene: code in a package dir; watch stale build cache.
- Structural-duplication standing rule: one fix must not require N edits —
  share the pattern before the Nth copy.
