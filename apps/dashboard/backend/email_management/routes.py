from datetime import datetime, timezone
from fastapi import APIRouter, Cookie, HTTPException
from auth import decode_token
from .db import _get_db
from .models import ActionStatusUpdate, ActionCreate, DisposeRequest
from .ai import _call_ai, _extract_body
from .executors import (
    get_credentials, build,
    execute_todoist_action, execute_calendar_action,
    execute_archive_action, execute_delete_action,
)
from .serializers import _email_to_dict, _action_to_dict


router = APIRouter()


# TODO LOW:    migration path not tested (only fresh DB tested).
# TODO LOW:    action row INSERT not asserted in test_run_triage_inserts_emails.


def _require_auth(pka_token: str | None) -> None:
    if pka_token is None or decode_token(pka_token) is None:
        raise HTTPException(status_code=401, detail="Not authenticated")


@router.post("/api/email-management/run")
def run_triage(pka_token: str = Cookie(default=None)):
    _require_auth(pka_token)

    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)

    result = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX"], maxResults=50)
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
                    classification, ai_summary, triage_status,
                    created_at, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    msg_id, thread_id, subject, sender, received_at,
                    snippet, classification, ai_summary,
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


@router.get("/api/email-management/emails")
def get_emails(pka_token: str = Cookie(default=None)):
    _require_auth(pka_token)
    conn = _get_db()
    try:
        email_rows = conn.execute(
            """SELECT id, thread_id, subject, sender, received_at, snippet,
               ai_summary, classification, triage_status
               FROM emails
               ORDER BY received_at DESC"""
        ).fetchall()

        if not email_rows:
            return {"emails": []}

        # Build email dicts and collect ids for actions lookup
        emails = [_email_to_dict(r) for r in email_rows]
        email_ids = [e["id"] for e in emails]

        # Fetch all actions for these emails in one query
        placeholders = ",".join("?" * len(email_ids))
        action_rows = conn.execute(
            f"""SELECT id, email_id, action_type, suggested_title,
                calendar_start, status, external_id, executed_at
                FROM actions WHERE email_id IN ({placeholders})""",
            email_ids,
        ).fetchall()

        # Group actions by email_id
        actions_by_email: dict = {e["id"]: [] for e in emails}
        for a in action_rows:
            actions_by_email[a["email_id"]].append(_action_to_dict(a))

        # Attach actions array to each email
        for email in emails:
            email["actions"] = actions_by_email[email["id"]]

        return {"emails": emails}
    finally:
        conn.close()


@router.get("/api/email-management/emails/{email_id}/actions")
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
            """SELECT id, email_id, action_type, suggested_title,
               calendar_start, status, external_id, executed_at
               FROM actions WHERE email_id = ?""",
            (email_id,),
        ).fetchall()
        return {"actions": [_action_to_dict(r) for r in rows]}
    finally:
        conn.close()


@router.post("/api/email-management/emails/{email_id}/actions")
def create_action(
    email_id: str,
    body: ActionCreate,
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

        now = datetime.now(timezone.utc).isoformat()
        cursor = conn.execute(
            """INSERT INTO actions
               (email_id, action_type, description, suggested_title,
                due_date, calendar_start, calendar_end, status,
                created_at, updated_at)
               VALUES (?, ?, NULL, ?, NULL, ?, NULL, 'pending', ?, ?)""",
            (email_id, body.type, body.name, body.event_datetime, now, now),
        )
        conn.commit()

        inserted = conn.execute(
            """SELECT id, email_id, action_type, suggested_title,
               calendar_start, status, external_id, executed_at
               FROM actions WHERE id = ?""",
            (cursor.lastrowid,),
        ).fetchone()
        return _action_to_dict(inserted)
    finally:
        conn.close()


@router.get("/api/email-management/emails/{email_id}/log")
def get_execution_log(
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
            """SELECT action_type, suggested_title, calendar_start, executed_at
               FROM actions
               WHERE email_id = ? AND status = 'approved'
               ORDER BY executed_at DESC""",
            (email_id,),
        ).fetchall()

        entries = [
            {
                "action_type": row["action_type"],
                "name": row["suggested_title"],
                "event_datetime": row["calendar_start"],
                "executed_at": row["executed_at"],
            }
            for row in rows
        ]
        return {"entries": entries}
    finally:
        conn.close()


@router.patch("/api/email-management/actions/{action_id}")
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
            # approved — apply owner-supplied overrides, then execute
            effective_row = dict(row_dict)
            effective_row["suggested_title"] = (
                body.name if body.name is not None
                else (row_dict["suggested_title"] or "")
            )
            effective_row["calendar_start"] = (
                body.event_datetime if body.event_datetime is not None
                else row_dict["calendar_start"]
            )

            action_type = row_dict["action_type"]
            try:
                if action_type == "Task":
                    external_id = execute_todoist_action(effective_row)
                elif action_type == "Event":
                    external_id = execute_calendar_action(effective_row)
                else:
                    external_id = None
            except Exception:
                raise HTTPException(
                    status_code=502, detail="External execution failed"
                )

            conn.execute(
                """UPDATE actions
                   SET status = 'approved', external_id = ?,
                       executed_at = ?, updated_at = ?,
                       suggested_title = ?,
                       calendar_start = ?
                   WHERE id = ?""",
                (
                    external_id,
                    now,
                    now,
                    effective_row["suggested_title"],
                    effective_row["calendar_start"],
                    action_id,
                ),
            )
            conn.commit()

        updated = conn.execute(
            """SELECT id, email_id, action_type, suggested_title,
               calendar_start, status, external_id, executed_at
               FROM actions WHERE id = ?""",
            (action_id,),
        ).fetchone()
        return _action_to_dict(updated)
    finally:
        conn.close()


@router.post("/api/email-management/emails/{email_id}/dispose")
def dispose_email(
    email_id: str,
    body: DisposeRequest,
    pka_token: str = Cookie(default=None),
):
    _require_auth(pka_token)

    if body.action not in ("archive", "delete"):
        raise HTTPException(status_code=422, detail="Invalid action value")

    conn = _get_db()
    try:
        email = conn.execute(
            "SELECT id FROM emails WHERE id = ?", (email_id,)
        ).fetchone()
        if not email:
            raise HTTPException(status_code=404, detail="Email not found")

        # All actions must be resolved before disposition
        pending = conn.execute(
            """SELECT id FROM actions
               WHERE email_id = ? AND status NOT IN ('approved', 'declined')""",
            (email_id,),
        ).fetchall()
        if pending:
            raise HTTPException(
                status_code=409,
                detail="All actions must be approved or declined before disposition",
            )

        try:
            if body.action == "archive":
                execute_archive_action({"email_id": email_id})
                new_status = "archived"
            else:
                execute_delete_action(email_id)
                new_status = "deleted"
        except Exception:
            raise HTTPException(status_code=502, detail="Gmail API failure")

        now = datetime.now(timezone.utc).isoformat()
        conn.execute(
            "UPDATE emails SET triage_status = ?, updated_at = ? WHERE id = ?",
            (new_status, now, email_id),
        )
        conn.commit()

        return {"id": email_id, "triage_status": new_status}
    finally:
        conn.close()
