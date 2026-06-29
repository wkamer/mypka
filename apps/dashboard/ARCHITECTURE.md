# Dashboard App — Architecture

## Overview

This app is a personal knowledge assistant dashboard. It runs as a FastAPI backend (Python) and a React/Vite frontend (TypeScript-ready JSX). Both layers are organized by feature domain. A new session should be able to locate any code in under 30 seconds using this document.

---

## Repository layout

```
apps/dashboard/
  backend/                  FastAPI application
  frontend/                 Vite + React application
  ARCHITECTURE.md           This file
```

---

## Backend

### Entry point

`backend/main.py` — FastAPI app, CORS config, auth routes, and router mounts.
Mount pattern: `app.include_router(email_management_router)`.

### Packages and modules

| File / package | Responsibility |
|---|---|
| `main.py` | App factory, login/logout/me endpoints, projects/key-elements/topics read routes |
| `auth.py` | JWT creation, decode, and credential verification |
| `email_management/` | Email Triage feature — see breakdown below |

### email_management package

Introduced 2026-06-29 to replace the single-file `email_management.py`.
Each file has one responsibility.

| File | Responsibility |
|---|---|
| `__init__.py` | Package entry point — calls `_init_db()` and `_migrate_drop_body_text()` on import, exports `router` |
| `db.py` | `DB_PATH` constant, `_get_db()`, `_init_db()`, `_migrate_drop_body_text()` |
| `models.py` | Pydantic request/response models: `ActionStatusUpdate`, `ActionCreate`, `DisposeRequest` |
| `ai.py` | `SYSTEM_PROMPT`, `_call_ai()` (Claude subprocess), `_extract_body()` (Gmail base64 decode) |
| `executors.py` | `execute_todoist_action()`, `execute_calendar_action()`, `execute_archive_action()`, `execute_delete_action()`, `_get_todoist_token()` — all external side-effect calls |
| `serializers.py` | `_email_to_dict()`, `_action_to_dict()` — DB row to API response shape |
| `routes.py` | `router`, `_require_auth()`, and all HTTP route handlers |

### HTTP routes (email_management)

| Method | Path | Handler | File |
|---|---|---|---|
| POST | `/api/email-management/run` | `run_triage` | routes.py |
| GET | `/api/email-management/emails` | `get_emails` | routes.py |
| GET | `/api/email-management/emails/{id}/actions` | `get_actions` | routes.py |
| POST | `/api/email-management/emails/{id}/actions` | `create_action` | routes.py |
| GET | `/api/email-management/emails/{id}/log` | `get_execution_log` | routes.py |
| PATCH | `/api/email-management/actions/{id}` | `patch_action` | routes.py |
| POST | `/api/email-management/emails/{id}/dispose` | `dispose_email` | routes.py |

### Database

SQLite at `email-management.db` (path configurable via `EMAIL_MANAGEMENT_DB` env var).
Two tables: `emails`, `actions`. Schema defined in `email_management/db.py`.

### Auth pattern

Cookie `pka_token` (JWT). Every protected route calls `_require_auth(pka_token)` which decodes via `auth.decode_token()`. Returns 401 on failure.

### Running tests

```bash
cd backend && ./venv/bin/pytest test_email_management.py -v
```

### Starting the server

```bash
cd backend && ./venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Frontend

### Entry point

`frontend/src/main.jsx` — mounts React app. Routes handled in `App.jsx`.

### Pages

| File | Route | Description |
|---|---|---|
| `pages/Login.jsx` | `/` | Login form |
| `pages/Dashboard.jsx` | `/dashboard` | Home tile grid |
| `pages/EmailTriage.jsx` | `/email-triage` | Email Triage feature page (thin shell) |
| `pages/Projects.jsx` | `/projects` | Project list |
| `pages/KeyElements.jsx` | `/key-elements` | Key Elements index |
| `pages/KeyElementDetail.jsx` | `/key-elements/:slug` | Single Key Element |
| `pages/Topics.jsx` | `/topics` | Topics index |
| `pages/TopicDetail.jsx` | `/topics/:slug` | Single Topic |

### EmailTriage component tree

Introduced 2026-06-29. Previously a single 756-line file.

```
pages/EmailTriage.jsx           Thin page: state, run-triage trigger, email list render
  components/EmailTriage/
    InboxRow.jsx                Accordion row per email (sender, subject, chevron)
      ActionsPanel.jsx          Mounts on accordion open: fetches and manages actions
        ActionRowV3.jsx         Single action row (editable name/datetime, approve/decline)
    ClassificationBadge.jsx     Badge: "Action" / "Information" (available, not yet used in UI)
    TriageStatusBadge.jsx       Badge: pending / approved / declined / error (available, not yet used)
    formatters.js               Pure helpers: fmtTimestamp, fmtEventDatetime, buildLogEntry, parseSenderName
    index.js                    Barrel: exports InboxRow
```

### API layer

`frontend/src/api/`

| File | Description |
|---|---|
| `client.js` | Generic `api` object with `get`, `post`, `patch` methods. Uses `fetch` with `credentials: "include"`. |
| `emailTriage.js` | Domain client `emailTriageApi` — wraps `client.js` with named methods: `runTriage`, `getEmails`, `getActions`, `patchAction`, `createAction`. |

Add a new domain client (e.g. `projects.js`) when a new feature needs more than one endpoint.

### Adding a new Email Triage feature

1. New API route? Add to `backend/email_management/routes.py` and update `emailTriageApi` in `frontend/src/api/emailTriage.js`
2. New business logic? Add to the relevant backend file (`ai.py`, `executors.py`, `serializers.py`)
3. New UI component? Add to `frontend/src/components/EmailTriage/` — import in the component that needs it
4. New DB column? Update `_init_db()` in `backend/email_management/db.py` and add a migration function there

### Building the frontend

```bash
cd frontend && npm run build
```

### Running tests

```bash
cd frontend && npm test -- EmailTriage.test.jsx
```

---

## Session notes

- 2026-06-29 Devon: Refactored to this modular structure. No behavior changes. 43 backend tests pass, frontend build clean (38 modules).
- Known pre-existing test failure: `reconstructs approved action log entries from actions on accordion open` — existed before this refactor, not caused by it.
