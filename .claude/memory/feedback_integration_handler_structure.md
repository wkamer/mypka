---
name: feedback_integration_handler_structure
description: "Integration folders are self-contained — handlers at root level, logs inside integration folder, own credentials — pattern from meta + dropbox"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5a2983e5-c77b-4ec7-bc06-7bcb44595997
---

Integration folders are fully self-contained. Everything belonging to an integration lives inside the integration folder.

**Standard structure:**
```
<name>/
  config.md             — auth, config, usage, rate limits, crontab documentation
  connection.py         — reusable auth/connection module (for Python APIs)
  *_handler.py / *.sh   — domain-specific handlers, at root level
  rclone.conf           — integration-specific rclone config (for rclone integrations, via --config flag)
  .env.example          — environment variables template
  .env                  — credentials (not in git)
  logs/                 — all log output for this integration
```

**Why:** Self-containment — nothing outside the integration folder that gets scattered across the system. References: meta integration (handlers at root), dropbox integration (logs/ + own rclone.conf).

**How to apply:**
- No Scripts/ subfolder — handlers at root level
- Logs always to `<integration>/logs/` — never to `/home/admin/logs/` or `/var/log/`
- Credentials and config inside integration folder — no shared system configs (e.g. for rclone: own rclone.conf + `--config` flag)
- Lock files may go in `/tmp/` (ephemeral by design)
- Crontab stays at system level — document the entry in config.md
