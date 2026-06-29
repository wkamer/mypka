import os
import sqlite3


DB_PATH = os.environ.get(
    "EMAIL_MANAGEMENT_DB",
    "/opt/myPKA/apps/dashboard/email-management.db",
)


# TODO MEDIUM: indexes/triggers on the emails table are not recreated after
#              _migrate_drop_body_text() runs the table-rename-recreate pattern.


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


def _migrate_drop_body_text() -> None:
    """Drop body_text column from emails table if it still exists.

    SQLite older than 3.35.0 does not support ALTER TABLE DROP COLUMN.
    Uses the table-rename-recreate pattern, which works on all SQLite versions.
    Safe to call multiple times — exits immediately when body_text is absent.
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        cols = {r[1] for r in conn.execute("PRAGMA table_info(emails)").fetchall()}
        if "body_text" not in cols:
            return
        conn.executescript("""
            BEGIN;
            DROP TABLE IF EXISTS emails_new;
            CREATE TABLE emails_new (
                id            TEXT PRIMARY KEY,
                thread_id     TEXT NOT NULL,
                subject       TEXT,
                sender        TEXT,
                received_at   TEXT NOT NULL,
                snippet       TEXT,
                classification TEXT,
                ai_summary    TEXT,
                triage_status TEXT NOT NULL DEFAULT 'pending',
                created_at    TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at    TEXT NOT NULL DEFAULT (datetime('now'))
            );
            INSERT INTO emails_new
            SELECT id, thread_id, subject, sender, received_at, snippet,
                   classification, ai_summary, triage_status, created_at, updated_at
            FROM emails;
            DROP TABLE emails;
            ALTER TABLE emails_new RENAME TO emails;
            COMMIT;
        """)
    finally:
        conn.close()


def _get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
