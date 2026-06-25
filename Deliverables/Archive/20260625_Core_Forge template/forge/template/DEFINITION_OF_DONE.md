# Definition of Done — {{PROJECT}}

A slice/story is **done** only when every applicable box is true. This is the
connective tissue between the gates.

- [ ] BDD scenarios written first and passing.
- [ ] Tests cover persistence round-trip + multi-turn / state-across-boundary.
- [ ] Code reviewed (incl. an adversarial/red-team pass on risky changes).
- [ ] Quality gate green (lint, tests, coverage, SAST, SCA, secrets, SBOM).
- [ ] Evals green _(if the slice touches an LLM/agent component)._
- [ ] Observability added: logs/traces/metrics for the new path.
- [ ] UX + accessibility reviewed _(if the slice has a human-facing surface)._
- [ ] Verified live in a real (non-test) environment.
- [ ] Docs updated: CHANGELOG, BACKLOG, ADR if a decision was made.
- [ ] No new structural duplication (or it was refactored into a shared path).
- [ ] Secrets handled via `.env.secrets`; nothing sensitive committed.
