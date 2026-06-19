---
name: Google API via google_helper.py
description: All Google communication (Sheets, Gmail, Calendar, Drive) goes via google_helper.py scripts — not via MCP integrations
type: reference
originSessionId: 45d9c0f5-f6e3-4280-ad6c-7d2675dbe115
---
All Google API calls go via `Team Knowledge/Core/Scripts/google_helper.py`.

Functions: `sheets()`, `gmail()`, `calendar()`, `drive()` — each returns an authenticated service client.

Auth: OAuth token in `C:\Users\wkame\myPKA\token.json`. Refreshes automatically.

Scripts with special characters (e, e with diaeresis, etc.): always run with `python -X utf8 script.py` or `# -*- coding: utf-8 -*-` at the top of the file.

**Why:** MCP integrations were tested and rejected. The direct Google API via Python scripts is the only approved route. The owner has repeatedly emphasised this — this is a hard rule.

**How to apply:** Always write a persistent script in `Team Knowledge/Core/Scripts/` that imports `google_helper`. Never use MCP Google tools — not even as a fallback. No exceptions.
