#!/opt/whisper/venv/bin/python
"""
Voice memo transcription handler — Whisper integration for myPKA.

Usage:
    python transcribe_handler.py <path_to_audio_file>

Exit codes:
    0 — transcription successful, .md written to Team Inbox
    1 — error (file not found, model failure, write failure)

Logs to: Team Knowledge/Core/Integrations/whisper/logs/transcribe.log
"""

import sys
import os
import logging
import argparse
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths — resolved relative to this script so nothing is hardcoded
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
LOG_DIR = SCRIPT_DIR / "logs"
LOG_FILE = LOG_DIR / "transcribe.log"

# Team Inbox is two levels up from Integrations/whisper:
#   Integrations/whisper -> Integrations -> Core -> Team Knowledge -> myPKA
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
log = logging.getLogger("transcribe_handler")

# ---------------------------------------------------------------------------
# Whisper model config — configurable via environment variables
# ---------------------------------------------------------------------------
WHISPER_MODEL = os.environ.get("WHISPER_MODEL", "small")
WHISPER_DEVICE = os.environ.get("WHISPER_DEVICE", "cpu")
WHISPER_LANGUAGE = os.environ.get("WHISPER_LANGUAGE", "nl")


def transcribe(audio_path: Path) -> str:
    """Run faster-whisper on audio_path and return the full transcript text."""
    from faster_whisper import WhisperModel

    log.info("Loading WhisperModel(model=%s, device=%s)", WHISPER_MODEL, WHISPER_DEVICE)
    model = WhisperModel(WHISPER_MODEL, device=WHISPER_DEVICE)

    log.info("Transcribing: %s", audio_path)
    segments, info = model.transcribe(
        str(audio_path),
        language=WHISPER_LANGUAGE,
        beam_size=5,
    )

    log.info(
        "Detected language '%s' with probability %.2f",
        info.language,
        info.language_probability,
    )

    lines = []
    for seg in segments:
        lines.append(seg.text.strip())

    transcript = " ".join(lines).strip()
    log.info("Transcription complete — %d characters", len(transcript))
    return transcript


def build_markdown(transcript: str, source_filename: str, timestamp: datetime) -> str:
    """Compose the output Markdown document."""
    ts_human = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return f"""# Voice Memo — {ts_human}

**Source file:** {source_filename}
**Transcribed at:** {ts_human}
**Language:** {WHISPER_LANGUAGE}
**Model:** {WHISPER_MODEL}

---

## Transcript

{transcript}
"""


def output_filename(timestamp: datetime) -> str:
    """Return output filename: YYYYMMDD_HHMMSS_voice-memo.md"""
    return timestamp.strftime("%Y%m%d_%H%M%S") + "_voice-memo.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe a voice memo to Markdown.")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    args = parser.parse_args()

    audio_path = Path(args.audio_file).resolve()

    # --- Validate input ---
    if not audio_path.exists():
        log.error("Audio file not found: %s", audio_path)
        return 1

    if not audio_path.is_file():
        log.error("Path is not a file: %s", audio_path)
        return 1

    log.info("Starting transcription pipeline for: %s", audio_path.name)

    # --- Transcribe ---
    try:
        transcript = transcribe(audio_path)
    except Exception as exc:
        log.error("Transcription failed: %s", exc, exc_info=True)
        return 1

    if not transcript:
        log.warning("Transcription returned empty result for: %s", audio_path.name)
        transcript = "(geen spraak herkend)"

    # --- Build output ---
    now = datetime.now()
    md_content = build_markdown(transcript, audio_path.name, now)
    out_filename = output_filename(now)
    out_path = TEAM_INBOX / out_filename

    # --- Write output ---
    try:
        TEAM_INBOX.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md_content, encoding="utf-8")
        log.info("Transcript written to: %s", out_path)
    except Exception as exc:
        log.error("Failed to write transcript: %s", exc, exc_info=True)
        return 1

    print(str(out_path))  # stdout: caller gets the output path
    return 0


if __name__ == "__main__":
    sys.exit(main())
