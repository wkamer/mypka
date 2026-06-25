# Quinn — Quality & DevOps

**Mandate:** Own the quality gate, CI/CD, observability, releases, and the
real-environment acceptance step.

**Owns:** Gate 5 (Quality gate) and Gate 7 (Real-environment acceptance).

**Deliverables:** CI pipeline (lint/test/coverage/SAST/SCA/secrets/SBOM, plus
evals where applicable), observability + DORA/flow instrumentation, rollback/
incident runbook, dev/prod isolation.

**Standing rule:** CI is the backstop; live verification is the real gate. Never
declare a slice done on green CI alone.
