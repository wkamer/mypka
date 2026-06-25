# Working Agreement — {{PROJECT}}

The operating framework for the team. Amendable; record amendments at the end.

## 1. Roles & routing
Larry orchestrates and never executes. All work is briefed via `team_inbox/`,
delivered back, and surfaced to the owner from `owner_inbox/`. Each owner-facing
doc is followed by an inline CLI summary — the owner decides to act on the
summary or read the full doc.

## 2. Delivery
- **Iterative vertical delivery**: build the thinnest end-to-end slice; each
  slice works in a real environment before the next begins.
- **Test-first**: scenarios before fixtures, fixtures before code. Never seed
  test data by hand as a substitute for coverage.
- **Tests must cross boundaries**: state survives a turn / a DB round-trip, not
  just an in-memory happy path.

## 3. Architecture
- Arch signs off before code. No inherited/third-party code is adopted without
  an Arch review (licence, security, fit). ADR logged for every decision; RFC
  for contested or cross-cutting ones.

## 4. Quality & safety
- The quality gate (`QUALITY_GATE.md`) and Definition of Done
  (`DEFINITION_OF_DONE.md`) are non-negotiable for merge.
- Live / real-environment acceptance is the real gate; CI is the backstop.
- Dev/prod isolation and the secrets split are respected at all times.

## 5. Team discipline (AI agents)
- **Brief scope cap**: max two deliverables per brief; split into parallel
  agents at brief time rather than overloading one.
- **WIP-1 per gate**; one working tree per agent — commit scope must match the
  task (no sweeping up another agent's files).
- **Retro accuracy**: check `git log` before filing a retro.

## 6. Proactive standard (founding, non-negotiable)
Every agent proactively challenges the approach and raises gaps. The owner
should never have to ask.

## 7. Operator ergonomics
- Multi-line commands go in scripts, run via `make` targets — never multi-line
  inline `-c`.
- Prefix terminal commands with an environment label when more than one exists
  (e.g. `[local]` / `[prod]`).

## Amendments
- _(record dated amendments here as the team learns)_
