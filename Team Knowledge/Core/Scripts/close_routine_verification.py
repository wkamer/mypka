"""
close_routine_verification.py — Verified session log writes for close routines.

Writes session_log to SQLite and UMC, verifies each write,
outputs structured JSON result. Exit code 1 if any step failed.

Interpreter: /opt/mypka-memory/venv/bin/python

Usage:
    /opt/mypka-memory/venv/bin/python close_routine_verification.py \
        --session-date 2026-05-21 \
        --session-title "Morning Routine" \
        --summary "..." \
        --domain personal \
        --topics "routine, morning" \
        --db personal
"""

import argparse
import json
import os
import re
import sqlite3
import sys

_SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
_MEMORY_DB_DIR = os.path.abspath(os.path.join(_SCRIPTS_DIR, '..', 'Integrations', 'memory-db'))
sys.path.insert(0, _SCRIPTS_DIR)
sys.path.insert(0, _MEMORY_DB_DIR)

from db_helper import personal_db, team_db, ke_db, gr_db

_DB_MAP = {
    'personal': personal_db,
    'team': team_db,
    'ke': ke_db,
    'gr': gr_db,
}

# Map CLI short forms to canonical UMC domain names
_DOMAIN_CANONICAL = {
    'personal': 'personal',
    'team': 'core',
    'ke': 'kamer-ecommerce',
    'gr': 'geldstroom-regie',
}

_THREAD_ID = 'daily-routines'
_SESSION_LOGS_ROOT = os.path.abspath(
    os.path.join(_SCRIPTS_DIR, '..', 'session-logs')
)


def _make_slug(session_title):
    slug = session_title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug.strip())
    slug = re.sub(r'-+', '-', slug)
    return slug[:60].rstrip('-')


def _write_markdown_mirror(session_date, session_title, topics, summary):
    try:
        date_part = session_date.replace('-', '')  # YYYYMMDD
        year = session_date[:4]
        month = session_date[5:7]
        slug = _make_slug(session_title)
        filename = f"{date_part}_{slug}.md"
        dir_path = os.path.join(_SESSION_LOGS_ROOT, year, month)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, filename)

        if os.path.exists(file_path):
            return {"ok": True, "path": file_path, "skipped": True}

        content = (
            f"# {session_title} — {session_date}\n"
            f"\n"
            f"**Session date:** {session_date}\n"
            f"**Topics:** {topics}\n"
            f"\n"
            f"## Summary\n"
            f"\n"
            f"{summary}\n"
        )
        with open(file_path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        return {"ok": True, "path": file_path}
    except Exception as e:
        return {"ok": False, "path": None, "error": str(e)}


def _write_session_log(db_path, session_date, session_title, topics, summary):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            "SELECT id FROM session_logs WHERE session_date=? AND session_title=?",
            (session_date, session_title),
        )
        existing = cur.fetchone()
        if existing:
            conn.close()
            return {"ok": True, "id": existing[0], "skipped": True}

        cur.execute(
            "INSERT INTO session_logs (session_date, session_title, topics, summary) VALUES (?,?,?,?)",
            (session_date, session_title, topics, summary),
        )
        row_id = cur.lastrowid
        conn.commit()

        cur.execute("SELECT id FROM session_logs WHERE id=?", (row_id,))
        verified = cur.fetchone()
        conn.close()

        if verified:
            return {"ok": True, "id": row_id}
        return {"ok": False, "id": None, "error": "insert succeeded but row missing on verify"}
    except Exception as e:
        return {"ok": False, "id": None, "error": str(e)}


def _write_umc(session_date, session_title, summary, domain, source_type="session_log"):
    try:
        from memory_config import get_dsn
        os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
        from memory_manager import get_manager
        mm = get_manager()

        sid = mm.write_summary(
            full_content=summary,
            summary=summary,
            description=f"{session_title} — {session_date}",
            domain=domain,
            source_type=source_type,
        )
        mm.write_message(
            thread_id=_THREAD_ID,
            role='assistant',
            content=f"[{session_date} {session_title}] {summary}",
        )

        with mm.conn.cursor() as cur:
            cur.execute("SELECT id FROM memory_summaries WHERE id=%s", (sid,))
            verified = cur.fetchone()

        if verified:
            return {"ok": True, "id": sid}
        return {"ok": False, "id": None, "error": "UMC write returned id but row missing on verify"}
    except Exception as e:
        return {"ok": False, "id": None, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Verified session log write for close routines.")
    parser.add_argument('--session-date', required=True)
    parser.add_argument('--session-title', required=True)
    parser.add_argument('--summary', required=True)
    parser.add_argument('--domain', default='personal', choices=['personal', 'team', 'ke', 'gr'])
    parser.add_argument('--topics', default='')
    parser.add_argument('--db', default='personal', choices=['personal', 'team', 'ke', 'gr'])
    args = parser.parse_args()

    sl_result = _write_session_log(
        _DB_MAP[args.db],
        args.session_date,
        args.session_title,
        args.topics,
        args.summary,
    )

    mirror_result = (
        _write_markdown_mirror(
            args.session_date,
            args.session_title,
            args.topics,
            args.summary,
        )
        if sl_result.get("ok")
        else {"ok": False, "path": None, "error": "skipped — session_log write failed"}
    )

    result = {
        "session_log": sl_result,
        "umc": _write_umc(
            args.session_date,
            args.session_title,
            args.summary,
            _DOMAIN_CANONICAL[args.domain],
        ),
        "markdown_mirror": mirror_result,
    }

    print(json.dumps(result, indent=2))

    if not all(v.get("ok") for v in result.values()):
        sys.exit(1)


if __name__ == '__main__':
    main()
