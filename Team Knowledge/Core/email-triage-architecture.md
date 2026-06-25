# Email Triage — Architecture Decisions

**Project:** Email Management System (Inbox Zero)
**Date:** 2026-06-25
**Author:** Kai
**Status:** Accepted — Devon builds from this document
**Revision:** 2 — decisions 2, 3, 4, and 5 updated after scope change

---

## Scope

Email triage feature added to the existing dashboard at `/opt/myPKA/apps/dashboard/`. Not a standalone app. AI classifies each email as Information or Action. Walter approves per email and per extracted action. Approved actions execute: Todoist task, Google Calendar event, or Gmail archive. Manual trigger only for v1.

Devon must be able to build the full v1 from this document without making any additional architecture decisions.

---

## Decision 1 — Gmail OAuth Re-auth

**Current state:**
`token.json` exists at `/opt/myPKA/Team Knowledge/Core/Integrations/google/token.json`. The file has a valid refresh token and was updated 2026-06-24. The access token (short-lived) is expired, but `get_credentials()` in `google_helper.py` auto-refreshes it on the next API call using the refresh token. No manual re-auth is required right now.

**Required scope check:**
The `gmail.modify` scope is already granted. This scope covers: read messages, apply/remove labels, archive (remove INBOX label), and move to trash. Sufficient for v1.

**If re-auth is ever needed (symptoms: `google.auth.exceptions.RefreshError` on any Gmail call):**

The re-auth script is at `/opt/myPKA/Team Knowledge/Core/Integrations/google/Scripts/google_auth.py`. The script uses a manual copy-paste URL flow that works over SSH without a browser on the Pi.

Steps:
1. SSH into the Pi: `ssh admin@raspberrypi.local`
2. Activate the dashboard backend venv: `source /opt/myPKA/apps/dashboard/backend/venv/bin/activate`
3. Run: `cd "/opt/myPKA/Team Knowledge/Core/Integrations/google/Scripts" && python3 google_auth.py`
4. The script prints an authorization URL. Open that URL in any browser on any device.
5. Grant permission to the Google account (`wkamer@gmail.com`).
6. After granting, the browser redirects to `localhost` — the page will not load. That is expected.
7. Copy the full URL from the browser address bar (starts with `http://localhost/?code=...`).
8. Paste that URL into the SSH terminal when prompted.
9. The script saves a fresh `token.json`. Done.

**Email triage integration with google_helper.py:**
The email triage module calls `google_helper.py`'s `get_credentials()` for all Gmail and Calendar API calls. The helper is shared infrastructure — do not copy or duplicate it. Import it via `sys.path.insert` pointing to the google integration folder:

```python
import sys
sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")
from google_helper import get_credentials
```

The shared `token.json` path is the single source of truth for the OAuth token.

**Delete scope note:**
Permanent Gmail delete requires the `https://mail.google.com/` scope (not currently granted). v1 does not support permanent delete — only archive (remove INBOX label). Scope expansion would require a new OAuth consent and is a v2 decision.

---

## Decision 2 — Integration into the Existing Dashboard

**This is not a new app. No new ports. No new deployment.**

The feature slots into the existing dashboard at `/opt/myPKA/apps/dashboard/` as a new backend module and a new frontend page. The existing FastAPI process (port 8000) and Vite process (port 5173) handle it.

**Backend: new module `email_triage.py`**

Create `/opt/myPKA/apps/dashboard/backend/email_triage.py` as a FastAPI `APIRouter`. Mount it in `main.py` with:

```python
from email_triage import router as email_triage_router
app.include_router(email_triage_router)
```

All email triage routes use the prefix `/api/email-triage/`. Auth pattern is identical to existing routes — import and call `_require_auth(pka_token)` and `decode_token` from `auth.py`.

Example route signature:
```python
@router.post("/api/email-triage/run")
def run_triage(pka_token: str = Cookie(default=None)):
    _require_auth(pka_token)
    ...
```

**Frontend: new page `EmailTriage.jsx`**

Create `/opt/myPKA/apps/dashboard/frontend/src/pages/EmailTriage.jsx`.

Register the route in `App.jsx` following the existing pattern:
```jsx
import EmailTriage from "./pages/EmailTriage";
// inside AuthGate <Routes>:
<Route path="/email-triage" element={user ? <EmailTriage /> : <Navigate to="/login" replace />} />
```

API calls use the existing `api.get()` from `client.js` for GET requests. Add `post` and `patch` methods to `client.js` following the same `request()` pattern already in place. The `BASE = ""` ensures all calls hit the same origin — no CORS changes needed.

**No changes to:**
- Docker Compose / deployment configuration
- Traefik / Cloudflare Tunnel routing
- Existing `main.py` routes (add only, do not modify)
- `App.jsx` existing routes (add only, do not modify)

---

## Decision 3 — Tech Stack

**Backend:** Python + FastAPI + Uvicorn (existing dashboard backend)

No new Python environment. Add new dependencies to the existing `/opt/myPKA/apps/dashboard/backend/requirements.txt`.

**New dependencies to add to requirements.txt:**
- `httpx` — for OpenRouter API calls (no new SDK needed)
- `google-auth` — Gmail and Calendar credential handling
- `google-auth-oauthlib` — OAuth flow for re-auth script
- `google-api-python-client` — Gmail and Calendar API clients

Install into the existing venv:
```bash
source /opt/myPKA/apps/dashboard/backend/venv/bin/activate
pip install httpx google-auth google-auth-oauthlib google-api-python-client
pip freeze > requirements.txt
```

**Frontend:** React + Vite (existing dashboard frontend)

No new npm packages needed. All required packages (`react`, `react-dom`, `react-router-dom`) are already installed.

**Database:** SQLite (Decision 5 below)

---

## Decision 4 — AI Triage

**Decision: use the Claude Code CLI subprocess approach.**

Walter's instruction (exact words): "Eerst maar claude en accepteer mogelijk traagheid" — use the Claude Code CLI first and accept possible slowness.

This is the same mechanism as the Discord integration: `subprocess.run(["claude", "-p", prompt, "--dangerously-skip-permissions"], ...)`. No API key is needed. The CLI session handles authentication.

**Call pattern:**

```python
import subprocess, json

def call_ai(subject: str, sender: str, body: str) -> dict:
    prompt = f"""{SYSTEM_PROMPT}

Subject: {subject}
From: {sender}

{body[:2000]}"""
    result = subprocess.run(
        ["claude", "-p", prompt, "--dangerously-skip-permissions"],
        capture_output=True,
        text=True,
        timeout=120
    )
    result.check_returncode()
    return json.loads(result.stdout.strip())
```

**Known trade-off:**
The CLI subprocess approach is slower than a direct API call. This is accepted. Walter explicitly chose this approach for v1. Speed can be optimized in v2 if needed.

**No API key needed:**
No `OPENROUTER_API_KEY`, no `ANTHROPIC_API_KEY`. The CLI session handles authentication. No `.env` changes are required for the AI call.

**AI call contract:**

Single call per email. System prompt defines the classification task. User message contains the email subject, sender, and body (truncated to 2000 characters). Response must be JSON.

Required output schema:
```json
{
  "classification": "Information | Action",
  "summary": "one sentence plain-text summary of the email",
  "actions": [
    {
      "type": "todoist | calendar | archive",
      "description": "human-readable description of the action",
      "suggested_title": "string (for Todoist task or Calendar event title)",
      "due_date": "YYYY-MM-DD or null",
      "calendar_start": "ISO 8601 or null",
      "calendar_end": "ISO 8601 or null"
    }
  ]
}
```

For `classification: "Information"`, return `actions: []`.

---

## Decision 5 — Data Persistence

**Decision: SQLite database.**

Gmail label state alone is not sufficient. Labels track inbox membership — they do not track:
- Which emails have been fetched and shown to Walter
- The AI classification result per email
- Which actions were extracted
- Whether Walter approved or declined each individual action
- Whether an approved action was executed (Todoist task ID, Calendar event ID)
- Idempotency — preventing re-execution on page refresh or app restart

**Database location:** `/opt/myPKA/apps/dashboard/email-triage.db`

Co-located at the dashboard app root (not inside `backend/`). The path is consistent with how other databases in the ecosystem sit at the app root level.

Initialize the database on first run via `email_triage.py` using Python's built-in `sqlite3` module. The `sqlite3` CLI is not installed on this host — always use `python3 -c "import sqlite3; ..."` or the module in code.

**Schema:**

Table `emails`:
```sql
CREATE TABLE IF NOT EXISTS emails (
  id            TEXT PRIMARY KEY,  -- Gmail message ID
  thread_id     TEXT NOT NULL,
  subject       TEXT,
  sender        TEXT,
  received_at   TEXT NOT NULL,     -- ISO 8601
  snippet       TEXT,              -- Gmail snippet for display
  body_text     TEXT,              -- First 2000 chars of body sent to AI
  classification TEXT,             -- 'Information' | 'Action' | null (pending triage)
  ai_summary    TEXT,
  triage_status TEXT NOT NULL DEFAULT 'pending',
  -- pending | approved | declined | triage_error
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at    TEXT NOT NULL DEFAULT (datetime('now'))
);
```

Table `actions`:
```sql
CREATE TABLE IF NOT EXISTS actions (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  email_id        TEXT NOT NULL REFERENCES emails(id),
  action_type     TEXT NOT NULL,   -- 'todoist' | 'calendar' | 'archive'
  description     TEXT,
  suggested_title TEXT,
  due_date        TEXT,
  calendar_start  TEXT,
  calendar_end    TEXT,
  status          TEXT NOT NULL DEFAULT 'pending',
  -- pending | approved | declined | executed | failed
  external_id     TEXT,            -- Todoist task ID or Calendar event ID after execution
  executed_at     TEXT,
  created_at      TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
);
```

**Gmail label coordination:**
When an archive action executes, remove the `INBOX` label via Gmail API. The source of truth for "was this archived" is the `actions` table (`status = 'executed'`), not the Gmail label state.

**Backup:**
`email-triage.db` is covered by the existing daily SQLite backup cron once the path is added to the backup script. Devon flags this to Kai before go-live — do not assume it is covered automatically at the new path.

---

## Summary Table

| Decision | Answer |
|---|---|
| Gmail OAuth re-auth | Token auto-refreshes. If re-auth needed: activate dashboard venv, run `google_auth.py` via SSH. |
| App location | Inside existing dashboard at `/opt/myPKA/apps/dashboard/` |
| Backend port | 8000 (existing dashboard backend — no new port) |
| Frontend port | 5173 dev (existing dashboard frontend — no new port) |
| Backend module | `backend/email_triage.py` with `APIRouter`, mounted in `main.py` |
| Frontend page | `frontend/src/pages/EmailTriage.jsx`, route `/email-triage` in `App.jsx` |
| Tech stack | FastAPI + Uvicorn (backend), React + Vite (frontend) — same as existing dashboard |
| Python venv | Reuse `/opt/myPKA/apps/dashboard/backend/venv/` — add new deps to `requirements.txt` |
| AI provider | Claude Code CLI subprocess — no API key needed, CLI session handles auth |
| AI model | Determined by CLI session (no explicit model selection required) |
| AI client | `subprocess.run(["claude", "-p", prompt, "--dangerously-skip-permissions"], ...)` |
| Data persistence | SQLite at `/opt/myPKA/apps/dashboard/email-triage.db`, two tables: `emails` + `actions` |
| Gmail scope | `gmail.modify` already granted — sufficient for v1 |
| Delete support | Out of scope for v1 (requires scope expansion + new OAuth consent) |
| Backup | Devon flags `email-triage.db` path to Kai before go-live for backup script update |
