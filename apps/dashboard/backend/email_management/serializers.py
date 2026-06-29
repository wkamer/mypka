import sqlite3


# TODO LOW:    _email_to_dict() has no guard for None id.


def _email_to_dict(row: sqlite3.Row) -> dict:
    """Convert an emails row to a dict and add the computed gmail_url field."""
    d = dict(row)
    d["gmail_url"] = f"https://mail.google.com/mail/u/0/#all/{d['id']}"
    d["status"] = d["triage_status"]
    return d


def _action_to_dict(row) -> dict:
    """Map an actions DB row to the API response shape."""
    d = dict(row)
    return {
        "id": d["id"],
        "email_id": d["email_id"],
        "type": d["action_type"],
        "name": d["suggested_title"],
        "event_datetime": d["calendar_start"],
        "status": d["status"],
        "external_id": d.get("external_id"),
        "executed_at": d.get("executed_at"),
        "approved_at": d.get("executed_at"),
    }
