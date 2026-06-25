"""
email_triage.py — Email Management (Inbox Zero) backend module.

FastAPI APIRouter mounted in main.py. DB initialized on module import.
Auth: _require_auth(pka_token) pattern identical to main.py.

Architecture: Kai (2026-06-25)
Delivery brief: Sloane G4 (2026-06-25)
Implementer: Devon
"""

import os
import sys
import base64
import json
import sqlite3
import subprocess
from datetime import datetime, timezone

import httpx
from fastapi import APIRouter, Cookie, HTTPException
from pydantic import BaseModel

from auth import decode_token

# ── Google helper ──
sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")
from google_helper import get_credentials
from googleapiclient.discovery import build

# ── Config ──
DB_PATH = os.environ.get(
    "EMAIL_TRIAGE_DB",
    "/opt/myPKA/apps/dashboard/email-triage.db",
)

TODOIST_TOKEN_PATH = (
    "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/.env"
)

SYSTEM_PROMPT = """You are an email triage assistant. Read the email and respond ONLY with valid JSON.

Required JSON schema:
{
  "classification": "Information or Action",
  "summary": "one sentence plain-text summary of the email",
  "actions": [
    {
      "type": "todoist or calendar or archive",
      "description": "human-readable description of the action",
      "suggested_title": "string for Todoist task or Calendar event title",
      "due_date": "YYYY-MM-DD or null",
      "calendar_start": "ISO 8601 or null",
      "calendar_end": "ISO 8601 or null"
    }
  ]
}

Rules:
- classification is exactly "Information" or "Action" (capital first letter)
- For "Information" emails: actions must be an empty array []
- For "Action" emails: include one or more relevant actions
- Action type is exactly one of: todoist, calendar, archive
- Respond with JSON only — no prose, no markdown fences
"""

router = APIRouter()


# ── Database ──

def _init_db() -> None:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id            TEXT PRIMARY KEY,
            thread_id     TEXT NOT NULL,
            subject       TEXT,
            sender        TEXT,
            received_at   TEXT NOT NULL,
            snippet       TEXT,
            body_text     TEXT,
            classification TEXT,
            ai_summary    TEXT,
            triage_status TEXT NOT NULL DEFAULT 'pending',
            created_at    TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at    TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS actions (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            email_id        TEXT NOT NULL REFERENCES emails(id),
            action_type     TEXT NOT NULL,
            description     TEXT,
            suggested_title TEXT,
            due_date        TEXT,
            calendar_start  TEXT,
            calendar_end    TEXT,
            status          TEXT NOT NULL DEFAULT 'pending',
            external_id     TEXT,
            executed_at     TEXT,
            created_at      TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at      TEXT NOT NULL DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()


_init_db()


def _get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ── Auth ──

def _require_auth(pka_token: str | None) -> None:
    if pka_token is None or decode_token(pka_token) is None:
        raise HTTPException(status_code=401, detail="Not authenticated")


# ── Pydantic models ──

class EmailStatusUpdate(BaseModel):
    triage_status: str


class ActionStatusUpdate(BaseModel):
    status: str


# ── AI triage ──

def _call_ai(subject: str, sender: str, body: str) -> dict:
    prompt = f"""{SYSTEM_PROMPT}

Subject: {subject}
From: {sender}

{body[:2000]}"""
    result = subprocess.run(
        ["claude", "-p", prompt, "--dangerously-skip-permissions"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    result.check_returncode()
    return json.loads(result.stdout.strip())


# ── Gmail body extraction ──

def _extract_body(msg: dict) -> str:
    payload = msg.get("payload", {})

    def get_part_text(part: dict) -> str:
        mime = part.get("mimeType", "")
        if mime == "text/plain":
            data = part.get("body", {}).get("data", "")
            if data:
                return base64.urlsafe_b64decode(data + "==").decode(
                    "utf-8", errors="replace"
                )
        for sub in part.get("parts", []):
            result = get_part_text(sub)
            if result:
                return result
        return ""

    return get_part_text(payload)[:2000]


# ── Todoist token ──

def _get_todoist_token() -> str:
    # First try environment variable (e.g. from backend/.env)
    token = os.environ.get("TODOIST_API_TOKEN", "")
    if token:
        return token
    # Fall back to Todoist integration .env file
    try:
        with open(TODOIST_TOKEN_PATH) as f:
            for line in f:
                line = line.strip()
                if line.startswith("TODOIST_API_TOKEN="):
                    return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    raise ValueError("TODOIST_API_TOKEN not found in env or Todoist .env file")


# ── Execution helpers ──

def execute_todoist_action(action_row: dict) -> str:
    """Create a Todoist task. Returns task ID as string. Raises on failure."""
    token = _get_todoist_token()
    payload: dict = {"content": action_row["suggested_title"]}
    if action_row.get("due_date"):
        payload["due_date"] = action_row["due_date"]

    resp = httpx.post(
        "https://api.todoist.com/api/v1/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return str(resp.json()["id"])


def execute_calendar_action(action_row: dict) -> str:
    """Create a Google Calendar event. Returns event ID as string. Raises on failure."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)
    event = {
        "summary": action_row["suggested_title"],
        "start": {
            "dateTime": action_row["calendar_start"],
            "timeZone": "Europe/Amsterdam",
        },
        "end": {
            "dateTime": action_row["calendar_end"],
            "timeZone": "Europe/Amsterdam",
        },
    }
    result = service.events().insert(calendarId="primary", body=event).execute()
    return str(result["id"])


def execute_archive_action(action_row: dict) -> str:
    """Remove INBOX label from Gmail message. Returns message ID. Raises on failure."""
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)
    result = (
        service.users()
        .messages()
        .modify(
            userId="me",
            id=action_row["email_id"],
            body={"removeLabelIds": ["INBOX"]},
        )
        .execute()
    )
    return str(result["id"])


# ════════════════════════════════════════════════════════════
# SLICE 1 — Routes: run triage, list emails
# ════════════════════════════════════════════════════════════

@router.post("/api/email-triage/run")
def run_triage(pka_token: str = Cookie(default=None)):
    _require_auth(pka_token)

    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    result = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX", "UNREAD"], maxResults=20)
        .execute()
    )
    messages = result.get("messages", [])

    processed = 0
    skipped = 0
    errors = 0

    conn = _get_db()
    try:
        for msg_ref in messages:
            msg_id = msg_ref["id"]

            existing = conn.execute(
                "SELECT id FROM emails WHERE id = ?", (msg_id,)
            ).fetchone()
            if existing:
                skipped += 1
                continue

            msg = (
                service.users()
                .messages()
                .get(userId="me", id=msg_id, format="full")
                .execute()
            )

            headers = {
                h["name"]: h["value"]
                for h in msg.get("payload", {}).get("headers", [])
            }
            subject = headers.get("Subject", "")
            sender = headers.get("From", "")
            received_ts = int(msg.get("internalDate", "0")) // 1000
            received_at = datetime.fromtimestamp(
                received_ts, tz=timezone.utc
            ).isoformat()
            snippet = msg.get("snippet", "")
            thread_id = msg.get("threadId", "")
            body_text = _extract_body(msg)

            try:
                ai_result = _call_ai(subject, sender, body_text)
                classification = ai_result.get("classification")
                ai_summary = ai_result.get("summary", "")
                actions = ai_result.get("actions", [])
                triage_status = "pending"
            except Exception:
                classification = None
                ai_summary = None
                actions = []
                triage_status = "triage_error"
                errors += 1

            now = datetime.now(timezone.utc).isoformat()
            conn.execute(
                """INSERT INTO emails
                   (id, thread_id, subject, sender, received_at, snippet,
                    body_text, classification, ai_summary, triage_status,
                    created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    msg_id, thread_id, subject, sender, received_at,
                    snippet, body_text, classification, ai_summary,
                    triage_status, now, now,
                ),
            )

            for action in actions:
                conn.execute(
                    """INSERT INTO actions
                       (email_id, action_type, description, suggested_title,
                        due_date, calendar_start, calendar_end, status,
                        created_at, updated_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?)""",
                    (
                        msg_id,
                        action.get("type"),
                        action.get("description"),
                        action.get("suggested_title"),
                        action.get("due_date"),
                        action.get("calendar_start"),
                        action.get("calendar_end"),
                        now,
                        now,
                    ),
                )

            if triage_status != "triage_error":
                processed += 1

        conn.commit()
    finally:
        conn.close()

    return {"processed": processed, "skipped": skipped, "errors": errors}


@router.get("/api/email-triage/emails")
def get_emails(pka_token: str = Cookie(default=None)):
    _require_auth(pka_token)
    conn = _get_db()
    try:
        rows = conn.execute(
            """SELECT id, subject, sender, received_at, snippet, ai_summary,
               classification, triage_status
               FROM emails
               ORDER BY received_at DESC"""
        ).fetchall()
        return {"emails": [dict(r) for r in rows]}
    finally:
        conn.close()


# ════════════════════════════════════════════════════════════
# SLICE 2 — Route: approve / decline email classification
# ════════════════════════════════════════════════════════════

@router.patch("/api/email-triage/emails/{email_id}")
def patch_email(
    email_id: str,
    body: EmailStatusUpdate,
    pka_token: str = Cookie(default=None),
):
    _require_auth(pka_token)

    if body.triage_status not in ("approved", "declined"):
        raise HTTPException(status_code=422, detail="Invalid triage_status value")

    conn = _get_db()
    try:
        row = conn.execute(
            "SELECT id FROM emails WHERE id = ?", (email_id,)
        ).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Email not found")

        now = datetime.now(timezone.utc).isoformat()
        conn.execute(
            "UPDATE emails SET triage_status = ?, updated_at = ? WHERE id = ?",
            (body.triage_status, now, email_id),
        )
        conn.commit()

        updated = conn.execute(
            """SELECT id, subject, sender, received_at, snippet, ai_summary,
               classification, triage_status, updated_at
               FROM emails WHERE id = ?""",
            (email_id,),
        ).fetchone()
        return dict(updated)
    finally:
        conn.close()


# ════════════════════════════════════════════════════════════
# SLICE 3 — Routes: actions per email, approve / decline action
# ════════════════════════════════════════════════════════════

@router.get("/api/email-triage/emails/{email_id}/actions")
def get_actions(
    email_id: str,
    pka_token: str = Cookie(default=None),
):
    _require_auth(pka_token)
    conn = _get_db()
    try:
        email = conn.execute(
            "SELECT id FROM emails WHERE id = ?", (email_id,)
        ).fetchone()
        if not email:
            raise HTTPException(status_code=404, detail="Email not found")

        rows = conn.execute(
            """SELECT id, email_id, action_type, description, suggested_title,
               due_date, calendar_start, calendar_end, status, external_id, executed_at
               FROM actions WHERE email_id = ?""",
            (email_id,),
        ).fetchall()
        return {"actions": [dict(r) for r in rows]}
    finally:
        conn.close()


@router.patch("/api/email-triage/actions/{action_id}")
def patch_action(
    action_id: int,
    body: ActionStatusUpdate,
    pka_token: str = Cookie(default=None),
):
    _require_auth(pka_token)

    if body.status not in ("approved", "declined"):
        raise HTTPException(status_code=422, detail="Invalid status value")

    conn = _get_db()
    try:
        row = conn.execute(
            "SELECT * FROM actions WHERE id = ?", (action_id,)
        ).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Action not found")

        row_dict = dict(row)
        now = datetime.now(timezone.utc).isoformat()

        if body.status == "declined":
            conn.execute(
                "UPDATE actions SET status = 'declined', updated_at = ? WHERE id = ?",
                (now, action_id),
            )
            conn.commit()
        else:
            # approved — attempt execution
            action_type = row_dict["action_type"]
            try:
                if action_type == "todoist":
                    external_id = execute_todoist_action(row_dict)
                elif action_type == "calendar":
                    external_id = execute_calendar_action(row_dict)
                elif action_type == "archive":
                    external_id = execute_archive_action(row_dict)
                else:
                    external_id = None

                conn.execute(
                    """UPDATE actions
                       SET status = 'executed', external_id = ?,
                           executed_at = ?, updated_at = ?
                       WHERE id = ?""",
                    (external_id, now, now, action_id),
                )
                conn.commit()
            except Exception:
                conn.execute(
                    "UPDATE actions SET status = 'failed', updated_at = ? WHERE id = ?",
                    (now, action_id),
                )
                conn.commit()

        updated = conn.execute(
            """SELECT id, email_id, action_type, description, suggested_title,
               due_date, calendar_start, calendar_end, status, external_id, executed_at
               FROM actions WHERE id = ?""",
            (action_id,),
        ).fetchone()
        return dict(updated)
    finally:
        conn.close()
