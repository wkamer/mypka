#!/opt/mypka-memory/venv/bin/python
"""
WhatsApp export handler — Dropbox integration for myPKA.

Usage:
    python whatsapp_export_handler.py <path_to_chat_txt> --chat-slug <slug>

Exit codes:
    0 — processing successful (or all messages already processed), .md files written to Team Inbox
    1 — error (file not found, parse failure, write failure)

Logs to: Team Knowledge/Core/Integrations/dropbox/logs/whatsapp_export.log
State:   Team Knowledge/Core/Integrations/dropbox/whatsapp_export_state_<chat-slug>.json
"""

import sys
import os
import re
import json
import hashlib
import logging
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# UMC path bootstrapping — inserted before the handler's own logging so imports
# are resolved before logging.basicConfig is called further below.
_MEMORY_DB_DIR = Path(__file__).resolve().parents[1] / "memory-db"
sys.path.insert(0, str(_MEMORY_DB_DIR))

# ---------------------------------------------------------------------------
# Paths — resolved relative to this script so nothing is hardcoded
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
LOG_DIR = SCRIPT_DIR / "logs"
LOG_FILE = LOG_DIR / "whatsapp_export.log"

# Team Inbox is two levels up from Integrations/dropbox:
#   Integrations/dropbox -> Integrations -> Core -> Team Knowledge -> myPKA
MYPKA_ROOT = SCRIPT_DIR.parents[3]  # /opt/myPKA
TEAM_INBOX = MYPKA_ROOT / "Team Inbox"

# ---------------------------------------------------------------------------
# Logging — file + stderr so cron captures both
# ---------------------------------------------------------------------------
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr),
    ],
)
log = logging.getLogger("whatsapp_export_handler")

# ---------------------------------------------------------------------------
# WhatsApp message regex
# Format: [DD/MM/YYYY, HH:MM:SS] Name: Message
# ---------------------------------------------------------------------------
MESSAGE_PATTERN = re.compile(
    r"^\[(\d{2}/\d{2}/\d{4}),\s+(\d{2}:\d{2}:\d{2})\]\s+(.+?):\s+(.+)$"
)

# System messages to skip (no real content)
SYSTEM_PREFIXES = (
    "‎",  # left-to-right mark (WhatsApp system messages)
    "‏",  # right-to-left mark
)


def state_file_for(chat_slug: str) -> Path:
    """Return the state file path for a given chat slug."""
    return SCRIPT_DIR / f"whatsapp_export_state_{chat_slug}.json"


def load_state(chat_slug: str) -> set:
    """Load processed message hashes from state file. Returns a set of hash strings."""
    state_file = state_file_for(chat_slug)
    if not state_file.exists():
        return set()
    try:
        with state_file.open(encoding="utf-8") as f:
            data = json.load(f)
        return set(data.get("processed_hashes", []))
    except Exception as exc:
        log.warning("Could not load state file, starting fresh: %s", exc)
        return set()


def save_state(processed_hashes: set, chat_slug: str) -> None:
    """Persist processed message hashes to state file."""
    state_file = state_file_for(chat_slug)
    try:
        data = {"processed_hashes": sorted(processed_hashes)}
        with state_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        log.info("State saved — %d hashes", len(processed_hashes))
    except Exception as exc:
        log.error("Failed to save state: %s", exc)


def message_hash(date_str: str, time_str: str, sender: str, text: str) -> str:
    """Compute a stable hash for a single message."""
    raw = f"{date_str}|{time_str}|{sender}|{text}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def parse_chat(chat_path: Path) -> list[dict]:
    """
    Parse _chat.txt into a list of message dicts.
    Returns: [{date, time, sender, text, reply_quote, hash}]

    reply_quote is set when the line directly following the message header
    starts with '> ' (WhatsApp reply format). The quoted text is stored
    separately so build_markdown() can render it per GL-008.
    """
    messages = []
    current = None
    expecting_quote = False  # True immediately after a new message header

    with chat_path.open(encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\r\n")
            match = MESSAGE_PATTERN.match(line)
            if match:
                # Save previous message
                if current is not None:
                    messages.append(current)
                date_str, time_str, sender, text = match.groups()
                sender = sender.lstrip("~‎‏").strip()
                if not sender:
                    current = None
                    expecting_quote = False
                    continue
                text = text.strip()
                if text.startswith(SYSTEM_PREFIXES):
                    current = None
                    expecting_quote = False
                    continue
                h = message_hash(date_str, time_str, sender, text)
                current = {
                    "date": date_str,
                    "time": time_str,
                    "sender": sender,
                    "text": text,
                    "reply_quote": None,
                    "hash": h,
                }
                expecting_quote = True
            else:
                stripped = line.strip()
                if not stripped or current is None:
                    expecting_quote = False
                    continue
                if expecting_quote and stripped.startswith("> "):
                    # First continuation line is a reply-quote
                    current["reply_quote"] = stripped[2:].strip()
                    expecting_quote = False
                    # Recompute hash to include quote
                    current["hash"] = message_hash(
                        current["date"], current["time"], current["sender"],
                        current["text"] + "|" + current["reply_quote"]
                    )
                else:
                    # Regular continuation line
                    current["text"] += "\n" + stripped
                    current["hash"] = message_hash(
                        current["date"], current["time"], current["sender"],
                        current["text"] + ("|" + current["reply_quote"] if current["reply_quote"] else "")
                    )
                    expecting_quote = False

    if current is not None:
        messages.append(current)

    return messages


def filter_new(messages: list[dict], processed: set) -> list[dict]:
    """Return only messages whose hash is not yet in processed."""
    return [m for m in messages if m["hash"] not in processed]


def group_by_day(messages: list[dict]) -> dict:
    """Group messages by date string (DD/MM/YYYY). Returns {date_str: [messages]}."""
    groups = defaultdict(list)
    for m in messages:
        groups[m["date"]].append(m)
    return dict(groups)


def collect_participants(messages: list[dict]) -> list[str]:
    """Return sorted unique sender names."""
    return sorted(set(m["sender"] for m in messages))


def build_markdown(date_str: str, messages: list[dict], exported_at: datetime) -> str:
    """
    Build the Markdown document for one day.

    date_str format: DD/MM/YYYY
    """
    day, month, year = date_str.split("/")
    date_human = f"{day}-{month}-{year}"
    exported_ts = exported_at.strftime("%Y-%m-%d %H:%M:%S")
    participants = collect_participants(messages)

    lines = [
        f"# WhatsApp Export — {date_human}",
        "",
        f"**Geexporteerd:** {exported_ts}",
        f"**Deelnemers:** {', '.join(participants)}",
        "",
        "---",
        "",
        "## Conversatie",
        "",
    ]

    for m in messages:
        h, m_min = m["time"].split(":")[:2]
        time_short = f"{h}:{m_min}"
        quote = m.get("reply_quote")
        if quote:
            lines.append(f'**{time_short} — {m["sender"]}** *(reply op: "{quote}")*')
        else:
            lines.append(f"**{time_short} — {m['sender']}**")
        for text_line in m["text"].splitlines():
            lines.append(f'"{text_line}"')
        lines.append("")

    return "\n".join(lines)


def output_filename(date_str: str, chat_slug: str) -> str:
    """
    Build output filename from date string (DD/MM/YYYY) and chat slug.
    Uses midnight (000000) as time component since we group by day.
    Format: YYYYMMDD_000000_whatsapp-<chat-slug>.md
    """
    day, month, year = date_str.split("/")
    return f"{year}{month}{day}_000000_whatsapp-{chat_slug}.md"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Parse a WhatsApp _chat.txt export and write per-day Markdown files to Team Inbox."
    )
    parser.add_argument("chat_file", help="Path to the _chat.txt file from the WhatsApp export")
    parser.add_argument(
        "--chat-slug",
        required=True,
        help="Unique identifier for this chat (e.g. wendy-opdam). Used in filenames and state file.",
    )
    parser.add_argument(
        "--from-date",
        default="01/01/2026",
        help="Only process messages on or after this date (DD/MM/YYYY). Default: 01/01/2026",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory to write per-day .md files to. Defaults to PKM/My Life/WhatsApp/<chat-slug>/",
    )
    args = parser.parse_args()

    chat_path = Path(args.chat_file).resolve()
    chat_slug = args.chat_slug

    try:
        from_date = datetime.strptime(args.from_date, "%d/%m/%Y")
    except ValueError:
        log.error("Invalid --from-date format: %s (expected DD/MM/YYYY)", args.from_date)
        return 1

    if not chat_path.exists():
        log.error("Chat file not found: %s", chat_path)
        return 1

    if not chat_path.is_file():
        log.error("Path is not a file: %s", chat_path)
        return 1

    # Resolve output directory — default: PKM/My Life/WhatsApp/<chat-slug>/
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = MYPKA_ROOT / "PKM" / "My Life" / "WhatsApp" / chat_slug
    output_dir.mkdir(parents=True, exist_ok=True)
    log.info("Output directory: %s", output_dir)

    log.info("Processing WhatsApp export: %s", chat_path)

    # --- Load deduplication state ---
    processed = load_state(chat_slug)
    log.info("Loaded state — %d previously processed hashes", len(processed))

    # --- Parse ---
    try:
        all_messages = parse_chat(chat_path)
    except Exception as exc:
        log.error("Failed to parse chat file: %s", exc, exc_info=True)
        return 1

    log.info("Parsed %d messages total", len(all_messages))

    # --- Filter by date ---
    all_messages = [
        m for m in all_messages
        if datetime.strptime(m["date"], "%d/%m/%Y") >= from_date
    ]
    log.info("%d messages after %s filter", len(all_messages), args.from_date)

    new_messages = filter_new(all_messages, processed)
    log.info("%d new messages to process", len(new_messages))

    if not new_messages:
        log.info("No new messages — nothing to write")
        return 0

    # --- Group ALL messages by day (not just new) ---
    # This ensures each day file contains the full chronology, not just incremental additions.
    all_by_day = group_by_day(all_messages)

    # Determine which days have at least one new message — only those days get (re)written.
    days_with_new = {m["date"] for m in new_messages}

    log.info(
        "Days with new messages: %d (out of %d total days in export)",
        len(days_with_new),
        len(all_by_day),
    )

    # --- Write one canonical .md per day that has new messages ---
    now = datetime.now()
    written_paths = []

    for date_str in sorted(days_with_new, key=lambda d: datetime.strptime(d, "%d/%m/%Y")):
        # Use ALL messages for this day from the current export — not just new ones.
        day_messages = all_by_day[date_str]
        out_filename = output_filename(date_str, chat_slug)
        out_path = output_dir / out_filename

        md_content = build_markdown(date_str, day_messages, now)

        try:
            out_path.write_text(md_content, encoding="utf-8")
            log.info(
                "Written: %s (%d total messages, file %s)",
                out_path,
                len(day_messages),
                "updated" if out_path.exists() else "created",
            )
            written_paths.append(str(out_path))
        except Exception as exc:
            log.error("Failed to write %s: %s", out_path, exc, exc_info=True)
            return 1

        # --- UMC indexing — non-fatal ---
        try:
            from memory_config import get_dsn
            os.environ.setdefault("MEMORY_DB_DSN", get_dsn())
            from memory_manager import get_manager as _get_manager
            from knowledge_indexer import chunk_markdown, extract_date_from_filename

            _mm = _get_manager()
            _rel = str(out_path.relative_to(MYPKA_ROOT))
            _date_ref = extract_date_from_filename(out_path.name)
            _text = md_content
            _chunks = chunk_markdown(_text)
            for _i, _chunk in enumerate(_chunks):
                _mm.write_knowledge(
                    domain="personal",
                    file_path=_rel,
                    chunk_text=_chunk,
                    chunk_index=_i,
                    date_ref=_date_ref,
                    source_type="whatsapp",
                )
            log.info("UMC indexed: %s (%d chunks)", _rel, len(_chunks))
        except Exception as _umc_exc:
            log.warning("UMC indexing skipped (non-fatal): %s", _umc_exc)

    # --- Update state ---
    new_hashes = {m["hash"] for m in new_messages}
    processed.update(new_hashes)
    save_state(processed, chat_slug)

    # --- Print output paths to stdout (one per line) ---
    for path in written_paths:
        print(path)

    log.info("Done — %d file(s) written", len(written_paths))
    return 0


if __name__ == "__main__":
    sys.exit(main())
