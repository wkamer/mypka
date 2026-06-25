# Quality Gate — {{PROJECT}}

Nothing merges unless **all** applicable checks pass. Owner: Quinn.

## CI pipeline (every PR)
1. **Lint / format** — style is enforced, not debated.
2. **Tests** — unit + integration + BDD; coverage at or above the project
   threshold (start at 80%; raise only once integration tests are real).
3. **SAST** — static analysis for code vulnerabilities.
4. **SCA / dependencies** — known-vuln scan; dependencies pinned / hash-locked.
5. **Secrets scan** — no credentials in the diff or history.
6. **SBOM** — software bill of materials generated and stored.
7. **Build** — reproducible build succeeds.

## Evals (active when the project has LLM/agent components)
- Golden eval set runs in CI; LLM-as-judge + heuristic checks.
- Judge model and target model **versions pinned**.
- Prompts and agent definitions are versioned with a regression corpus.

## Not enforced from day one (tune per project)
- Strict typing: enable per-module, not globally up front.
- Coverage above ~85%: only once integration tests cover the real seams.

## The real gate
CI is the backstop. **Live / real-environment acceptance (gate 7) is the gate
that actually catches the expensive bugs.** Do not call a slice done on green
CI alone.
