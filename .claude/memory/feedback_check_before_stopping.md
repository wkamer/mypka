---
name: feedback_check_before_stopping
description: Always check what depends on a service before stopping it — never stop without inspecting running state first
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 80ec999c-7242-4e1f-98c8-251d281f9b74
---

Never stop a service without first checking what is running on it.

**Why:** Proposing `systemctl stop docker` without checking `docker ps` first — Docker was running n8n, Postgres, and Ollama. Stopping it would have killed production services.

**How to apply:** Before stopping any service (Docker, nginx, postgres, systemd unit), run the appropriate status/list command first (`docker ps`, `systemctl status`, `ss -tlnp`, etc.) and surface what is running. Only propose the stop after confirming nothing critical depends on it.
