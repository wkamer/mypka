"""
test_email_management.py — Backend tests for Email Management feature.

Tests are grouped by slice:
- Slice 1: Triage trigger and email list (8 tests)
- Slice 2: Approve or decline email classification (5 tests)
- Slice 3: View, approve, and execute actions (12 tests)
- Regression: Existing endpoints unaffected (7 tests)

Written BEFORE implementation per SOP-018 TDD protocol.
"""

import os
import sys
import json
import sqlite3
import tempfile
import subprocess
import pytest
from unittest.mock import patch, MagicMock

# ── Environment setup BEFORE any local imports ──
_TEST_DB_FD, TEST_DB_PATH = tempfile.mkstemp(suffix="-test-email-management.db")
os.close(_TEST_DB_FD)
os.environ["EMAIL_MANAGEMENT_DB"] = TEST_DB_PATH

import bcrypt as _bcrypt

_TEST_PASSWORD_HASH = _bcrypt.hashpw(b"testpass", _bcrypt.gensalt()).decode()
os.environ.setdefault("JWT_SECRET", "test-secret-1234567890abcdef")
os.environ.setdefault("APP_USERNAME", "testuser")
os.environ.setdefault("PASSWORD_HASH", _TEST_PASSWORD_HASH)

# ── Local imports (after env is set) ──
from fastapi import FastAPI
from fastapi.testclient import TestClient

import auth
import email_management

# Build test app with email management router
_test_app = FastAPI()
_test_app.include_router(email_management.router)
client = TestClient(_test_app, raise_server_exceptions=False)


# ── Helpers ──

def _auth_cookies():
    return {"pka_token": auth.create_token("testuser")}


def _insert_email(
    email_id="msg1",
    classification="Information",
    triage_status="pending",
    received_at="2026-06-25T12:00:00+00:00",
):
    conn = sqlite3.connect(TEST_DB_PATH)
    conn.execute(
        """INSERT OR IGNORE INTO emails
           (id, thread_id, subject, sender, received_at, snippet,
            classification, ai_summary, triage_status, created_at, updated_at)
           VALUES (?, 'thread1', 'Test Subject', 'test@example.com', ?,
           'snippet', ?, 'test summary', ?, datetime('now'), datetime('now'))""",
        (email_id, received_at, classification, triage_status),
    )
    conn.commit()
    conn.close()


def _insert_action(email_id="msg1", action_type="todoist", status="pending"):
    conn = sqlite3.connect(TEST_DB_PATH)
    conn.execute(
        """INSERT INTO actions
           (email_id, action_type, description, suggested_title,
            due_date, calendar_start, calendar_end, status, created_at, updated_at)
           VALUES (?, ?, 'Do something', 'Task Title', null, null, null, ?, datetime('now'), datetime('now'))""",
        (email_id, action_type, status),
    )
    conn.commit()
    last_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
    conn.close()
    return last_id


def _make_gmail_msg(msg_id, subject="Test Subject", sender="sender@test.com"):
    return {
        "id": msg_id,
        "threadId": f"thread-{msg_id}",
        "internalDate": "1750852800000",
        "snippet": f"snippet for {msg_id}",
        "payload": {
            "headers": [
                {"name": "Subject", "value": subject},
                {"name": "From", "value": sender},
            ],
            "mimeType": "text/plain",
            "body": {"data": ""},
            "parts": [],
        },
    }


def _make_ai_result(classification="Information", actions=None):
    return MagicMock(
        stdout=json.dumps({
            "classification": classification,
            "summary": "Test summary",
            "actions": actions or [],
        }),
        returncode=0,
        check_returncode=MagicMock(),
    )


# ── Fixtures ──

@pytest.fixture(autouse=True)
def clean_db():
    conn = sqlite3.connect(TEST_DB_PATH)
    conn.execute("DELETE FROM actions")
    conn.execute("DELETE FROM emails")
    conn.commit()
    conn.close()
    yield


# ════════════════════════════════════════════════════════════
# SLICE 1 — Triage trigger and email list
# ════════════════════════════════════════════════════════════

def test_db_init_creates_tables():
    """After import, email-management.db contains emails and actions tables with all columns."""
    conn = sqlite3.connect(TEST_DB_PATH)
    tables = {r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()}

    assert "emails" in tables, "emails table missing"
    assert "actions" in tables, "actions table missing"

    email_cols = {r[1] for r in conn.execute("PRAGMA table_info(emails)").fetchall()}
    for col in [
        "id", "thread_id", "subject", "sender", "received_at", "snippet",
        "classification", "ai_summary", "triage_status",
        "created_at", "updated_at",
    ]:
        assert col in email_cols, f"emails table missing column: {col}"
    assert "body_text" not in email_cols, "body_text must not exist — SSOT violation"

    action_cols = {r[1] for r in conn.execute("PRAGMA table_info(actions)").fetchall()}
    for col in [
        "id", "email_id", "action_type", "description", "suggested_title",
        "due_date", "calendar_start", "calendar_end", "status", "external_id",
        "executed_at", "created_at", "updated_at",
    ]:
        assert col in action_cols, f"actions table missing column: {col}"

    conn.close()


def test_run_triage_requires_auth():
    res = client.post("/api/email-management/run")
    assert res.status_code == 401


def test_get_emails_requires_auth():
    res = client.get("/api/email-management/emails")
    assert res.status_code == 401


def test_run_triage_empty_inbox():
    """With Gmail returning 0 messages: processed=0, skipped=0, errors=0, email list empty."""
    mock_svc = MagicMock()
    mock_svc.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": []
    }

    with patch("email_management.build", return_value=mock_svc), \
         patch("email_management.get_credentials", return_value=MagicMock()):
        res = client.post("/api/email-management/run", cookies=_auth_cookies())

    assert res.status_code == 200
    assert res.json() == {"processed": 0, "skipped": 0, "errors": 0}

    list_res = client.get("/api/email-management/emails", cookies=_auth_cookies())
    assert list_res.json()["emails"] == []


def test_run_triage_inserts_emails():
    """With 2 mocked Gmail messages and mocked AI, both emails appear in DB with correct classification."""
    mock_svc = MagicMock()
    mock_svc.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}, {"id": "msg2"}]
    }
    mock_svc.users.return_value.messages.return_value.get.return_value.execute.side_effect = [
        _make_gmail_msg("msg1", "Invoice due", "billing@acme.com"),
        _make_gmail_msg("msg2", "Meeting notes", "boss@corp.com"),
    ]

    ai_side_effects = [
        _make_ai_result("Action", [
            {"type": "todoist", "description": "Pay invoice",
             "suggested_title": "Pay ACME", "due_date": "2026-07-01",
             "calendar_start": None, "calendar_end": None}
        ]),
        _make_ai_result("Information"),
    ]

    with patch("email_management.build", return_value=mock_svc), \
         patch("email_management.get_credentials", return_value=MagicMock()), \
         patch("email_management.subprocess.run", side_effect=ai_side_effects):
        res = client.post("/api/email-management/run", cookies=_auth_cookies())

    assert res.status_code == 200
    data = res.json()
    assert data["processed"] == 2
    assert data["skipped"] == 0
    assert data["errors"] == 0

    list_res = client.get("/api/email-management/emails", cookies=_auth_cookies())
    emails = list_res.json()["emails"]
    assert len(emails) == 2

    by_id = {e["id"]: e for e in emails}
    assert by_id["msg1"]["classification"] == "Action"
    assert by_id["msg2"]["classification"] == "Information"
    assert by_id["msg1"]["gmail_url"] == "https://mail.google.com/mail/u/0/#all/msg1"
    assert by_id["msg2"]["gmail_url"] == "https://mail.google.com/mail/u/0/#all/msg2"


def test_run_triage_skips_existing():
    """Running triage twice with same Gmail message IDs produces 0 new rows on second run."""
    _insert_email("msg1")
    _insert_email("msg2")

    mock_svc = MagicMock()
    mock_svc.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}, {"id": "msg2"}]
    }

    with patch("email_management.build", return_value=mock_svc), \
         patch("email_management.get_credentials", return_value=MagicMock()):
        res = client.post("/api/email-management/run", cookies=_auth_cookies())

    assert res.status_code == 200
    data = res.json()
    assert data["processed"] == 0
    assert data["skipped"] == 2
    assert data["errors"] == 0

    list_res = client.get("/api/email-management/emails", cookies=_auth_cookies())
    assert len(list_res.json()["emails"]) == 2


def test_run_triage_ai_failure_stored_as_error():
    """When AI subprocess raises CalledProcessError for one message, that row has triage_error; others unaffected."""
    mock_svc = MagicMock()
    mock_svc.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}, {"id": "msg2"}]
    }
    mock_svc.users.return_value.messages.return_value.get.return_value.execute.side_effect = [
        _make_gmail_msg("msg1"),
        _make_gmail_msg("msg2"),
    ]

    def ai_side_effect(*args, **kwargs):
        count = getattr(ai_side_effect, "count", 0)
        ai_side_effect.count = count + 1
        if count == 0:
            m = MagicMock(returncode=1, stdout="")
            m.check_returncode.side_effect = subprocess.CalledProcessError(1, "claude")
            return m
        return _make_ai_result("Information")

    with patch("email_management.build", return_value=mock_svc), \
         patch("email_management.get_credentials", return_value=MagicMock()), \
         patch("email_management.subprocess.run", side_effect=ai_side_effect):
        res = client.post("/api/email-management/run", cookies=_auth_cookies())

    assert res.status_code == 200
    data = res.json()
    assert data["errors"] == 1
    assert data["processed"] == 1

    list_res = client.get("/api/email-management/emails", cookies=_auth_cookies())
    emails = list_res.json()["emails"]
    assert len(emails) == 2

    by_id = {e["id"]: e for e in emails}
    assert by_id["msg1"]["triage_status"] == "triage_error"
    assert by_id["msg2"]["triage_status"] == "pending"


def test_get_emails_returns_all_ordered():
    """GET /api/email-management/emails returns all rows ordered by received_at DESC."""
    _insert_email("older", received_at="2026-06-24T10:00:00+00:00")
    _insert_email("newer", received_at="2026-06-25T10:00:00+00:00")

    res = client.get("/api/email-management/emails", cookies=_auth_cookies())
    assert res.status_code == 200
    emails = res.json()["emails"]
    assert len(emails) == 2
    assert emails[0]["id"] == "newer"
    assert emails[1]["id"] == "older"
    assert emails[0]["gmail_url"] == "https://mail.google.com/mail/u/0/#all/newer"
    assert emails[1]["gmail_url"] == "https://mail.google.com/mail/u/0/#all/older"


# ════════════════════════════════════════════════════════════
# SLICE 2 — Approve or decline email classification
# ════════════════════════════════════════════════════════════

def test_patch_email_approve():
    _insert_email("msg1")
    res = client.patch(
        "/api/email-management/emails/msg1",
        json={"triage_status": "approved"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 200
    data = res.json()
    assert data["triage_status"] == "approved"
    assert data["gmail_url"] == "https://mail.google.com/mail/u/0/#all/msg1"

    conn = sqlite3.connect(TEST_DB_PATH)
    row = conn.execute(
        "SELECT triage_status, updated_at FROM emails WHERE id = 'msg1'"
    ).fetchone()
    conn.close()
    assert row[0] == "approved"
    assert row[1] is not None


def test_patch_email_decline():
    _insert_email("msg1")
    res = client.patch(
        "/api/email-management/emails/msg1",
        json={"triage_status": "declined"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 200
    assert res.json()["triage_status"] == "declined"


def test_patch_email_not_found():
    res = client.patch(
        "/api/email-management/emails/nonexistent",
        json={"triage_status": "approved"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 404


def test_patch_email_invalid_status():
    _insert_email("msg1")
    res = client.patch(
        "/api/email-management/emails/msg1",
        json={"triage_status": "banana"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 422


def test_patch_email_requires_auth():
    _insert_email("msg1")
    res = client.patch(
        "/api/email-management/emails/msg1",
        json={"triage_status": "approved"},
    )
    assert res.status_code == 401


# ════════════════════════════════════════════════════════════
# SLICE 3 — View, approve, and execute actions
# ════════════════════════════════════════════════════════════

def test_get_actions_for_email():
    _insert_email("msg1", classification="Action")
    _insert_action("msg1", "todoist")
    _insert_action("msg1", "calendar")

    res = client.get("/api/email-management/emails/msg1/actions", cookies=_auth_cookies())
    assert res.status_code == 200
    actions = res.json()["actions"]
    assert len(actions) == 2


def test_get_actions_empty_for_information_email():
    _insert_email("msg1", classification="Information")

    res = client.get("/api/email-management/emails/msg1/actions", cookies=_auth_cookies())
    assert res.status_code == 200
    assert res.json()["actions"] == []


def test_get_actions_not_found():
    res = client.get("/api/email-management/emails/nonexistent/actions", cookies=_auth_cookies())
    assert res.status_code == 404


def test_get_actions_requires_auth():
    res = client.get("/api/email-management/emails/msg1/actions")
    assert res.status_code == 401


def test_patch_action_decline():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "todoist")

    with patch("email_management.execute_todoist_action") as mock_exec:
        res = client.patch(
            f"/api/email-management/actions/{action_id}",
            json={"status": "declined"},
            cookies=_auth_cookies(),
        )

    assert res.status_code == 200
    assert res.json()["status"] == "declined"
    mock_exec.assert_not_called()


def test_patch_action_approve_todoist():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "todoist")

    with patch("email_management.execute_todoist_action", return_value="todoist-task-123"):
        res = client.patch(
            f"/api/email-management/actions/{action_id}",
            json={"status": "approved"},
            cookies=_auth_cookies(),
        )

    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "executed"
    assert data["external_id"] == "todoist-task-123"
    assert data["executed_at"] is not None


def test_patch_action_approve_calendar():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "calendar")

    with patch("email_management.execute_calendar_action", return_value="cal-event-456"):
        res = client.patch(
            f"/api/email-management/actions/{action_id}",
            json={"status": "approved"},
            cookies=_auth_cookies(),
        )

    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "executed"
    assert data["external_id"] == "cal-event-456"


def test_patch_action_approve_archive():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "archive")

    with patch("email_management.execute_archive_action", return_value="msg1") as mock_archive:
        res = client.patch(
            f"/api/email-management/actions/{action_id}",
            json={"status": "approved"},
            cookies=_auth_cookies(),
        )

    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "executed"
    mock_archive.assert_called_once()


def test_patch_action_execution_fails():
    """When execution helper raises an exception: status=failed, no 500, response is 200."""
    _insert_email("msg1")
    action_id = _insert_action("msg1", "todoist")

    with patch("email_management.execute_todoist_action", side_effect=Exception("Todoist unavailable")):
        res = client.patch(
            f"/api/email-management/actions/{action_id}",
            json={"status": "approved"},
            cookies=_auth_cookies(),
        )

    assert res.status_code == 200
    assert res.json()["status"] == "failed"


def test_patch_action_not_found():
    res = client.patch(
        "/api/email-management/actions/99999",
        json={"status": "declined"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 404


def test_patch_action_invalid_status():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "todoist")

    res = client.patch(
        f"/api/email-management/actions/{action_id}",
        json={"status": "banana"},
        cookies=_auth_cookies(),
    )
    assert res.status_code == 422


def test_patch_action_requires_auth():
    _insert_email("msg1")
    action_id = _insert_action("msg1", "todoist")

    res = client.patch(
        f"/api/email-management/actions/{action_id}",
        json={"status": "declined"},
    )
    assert res.status_code == 401


# ════════════════════════════════════════════════════════════
# REGRESSION — Existing endpoints unaffected after router mount
# ════════════════════════════════════════════════════════════

# These tests run against the full main.py app after the router is mounted.
# They verify that existing endpoints still respond correctly.

import importlib
import main as _main_module


_regression_client = TestClient(_main_module.app, raise_server_exceptions=False)


def _regression_auth_cookie():
    """Create a valid JWT for the regression test client (uses real credentials from .env)."""
    from auth import create_token as _ct
    return {"pka_token": _ct(os.environ["APP_USERNAME"])}


def test_regression_login_valid():
    """POST /api/login returns 200 with valid credentials."""
    # Use the actual env credentials
    res = _regression_client.post(
        "/api/login",
        json={"username": os.environ["APP_USERNAME"], "password": "testpass"},
    )
    assert res.status_code == 200
    assert res.json()["ok"] is True


def test_regression_me():
    """GET /api/me returns username with valid cookie."""
    res = _regression_client.get("/api/me", cookies=_regression_auth_cookie())
    assert res.status_code == 200
    assert "username" in res.json()


def test_regression_logout():
    """POST /api/logout clears cookie."""
    res = _regression_client.post("/api/logout", cookies=_regression_auth_cookie())
    assert res.status_code == 200
    assert res.json()["ok"] is True


def test_regression_projects():
    """GET /api/projects returns project lists without error."""
    res = _regression_client.get("/api/projects", cookies=_regression_auth_cookie())
    assert res.status_code == 200
    data = res.json()
    assert "personal" in data
    assert "business" in data


def test_regression_key_elements():
    """GET /api/key-elements returns item list without error."""
    res = _regression_client.get("/api/key-elements", cookies=_regression_auth_cookie())
    assert res.status_code == 200
    assert "items" in res.json()


def test_regression_topics():
    """GET /api/topics returns topic list without error."""
    res = _regression_client.get("/api/topics", cookies=_regression_auth_cookie())
    assert res.status_code == 200
    assert "items" in res.json()


def test_regression_new_routes_exist():
    """New email-management routes are accessible on the main app."""
    res = _regression_client.get("/api/email-management/emails", cookies=_regression_auth_cookie())
    assert res.status_code == 200
