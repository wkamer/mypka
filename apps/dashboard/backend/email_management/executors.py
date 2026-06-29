import os
import sys
import httpx

sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/google")
from google_helper import get_credentials
from googleapiclient.discovery import build


TODOIST_TOKEN_PATH = (
    "/opt/myPKA/Team Knowledge/Core/Integrations/todoist/.env"
)


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


def execute_delete_action(email_id: str) -> str:
    """Move Gmail message to Trash. Returns message ID. Raises on failure."""
    creds = get_credentials()
    service = build("gmail", "v1", credentials=creds)
    result = (
        service.users()
        .messages()
        .trash(userId="me", id=email_id)
        .execute()
    )
    return str(result["id"])
