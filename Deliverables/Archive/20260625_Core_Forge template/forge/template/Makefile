# {{PROJECT}} — all operations behind make targets (never raw shell when a target exists).
.PHONY: help install test lint quality eval run deploy clean

help:
	@echo "{{PROJECT}} targets:"
	@echo "  install   Install dependencies"
	@echo "  test      Run the test suite (BDD + unit + integration)"
	@echo "  lint      Lint + format check"
	@echo "  quality   Full quality gate (lint, test, SAST, SCA, secrets, SBOM)"
	@echo "  eval      Run LLM/agent evals (if applicable)"
	@echo "  run       Run the app locally (dev mode)"
	@echo "  deploy    Deploy (manual; enforces safe mode)"
	@echo "  clean     Remove build artifacts"

install:  ; @echo "TODO: define at the Architecture gate"
test:     ; @echo "TODO: wire test runner"
lint:     ; @echo "TODO: wire linter"
quality: lint test ; @echo "TODO: add SAST/SCA/secrets/SBOM"
eval:     ; @echo "TODO: wire eval suite (if AI components)"
run:      ; @echo "TODO: wire local run"
deploy:   ; @echo "TODO: wire manual deploy (safe mode)"
clean:    ; @echo "TODO: wire clean"
