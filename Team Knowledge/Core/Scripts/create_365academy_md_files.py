#!/opt/mypka-memory/venv/bin/python
"""
create_365academy_md_files.py

Generates 3 Markdown files per lesson for the 365 Academy module 1 (Vrijheid):
  1. Les <nr>. <titel> - Transcript.md   — clean text from .srt
  2. Les <nr>. <titel> - Samenvatting.md — structured summary via Claude API
  3. Les <nr>. <titel> - Opdracht.md     — HTML-to-Markdown from .txt

Usage:
    /opt/mypka-memory/venv/bin/python create_365academy_md_files.py [--folder <path>]

Environment:
    ANTHROPIC_API_KEY — required for summary generation

On API errors: writes empty file with error message, continues processing.
"""

import os
import re
import sys
import argparse
from pathlib import Path

import html2text
import anthropic

# Load ANTHROPIC_API_KEY from memory_config if not already in environment
try:
    import sys as _sys
    _sys.path.insert(0, "/opt/myPKA/Team Knowledge/Core/Integrations/memory-db")
    from memory_config import load_anthropic_key as _load_key
    _load_key()
except Exception:
    pass  # Fall back to environment variable as-is

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DEFAULT_FOLDER = "/opt/myPKA/Team Inbox/1. Vrijheid"
LESSON_PATTERN = re.compile(r"^(Les \d+\. .+)\.srt$")
SRT_TIMESTAMP_RE = re.compile(
    r"^\d+\s*$|^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\s*$"
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_srt(content: str) -> str:
    """Remove SRT sequence numbers and timestamps; return clean running text."""
    lines = content.splitlines()
    clean = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r"^\d+$", line):
            continue
        if re.match(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", line):
            continue
        clean.append(line)
    # Join with spaces — SRT lines are mid-sentence fragments
    text = " ".join(clean)
    # Collapse multiple spaces
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def html_to_markdown(html_content: str) -> str:
    """Convert HTML string to clean Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0  # no line wrapping
    return h.handle(html_content).strip()


def generate_summary(lesson_number: str, lesson_title: str, transcript: str, client: anthropic.Anthropic) -> str:
    """Call Claude API to generate a structured Dutch summary of the transcript."""
    prompt = f"""Je bent een assistent die lessen samenvat voor een persoonlijke kennisbank.

Schrijf een gestructureerde samenvatting van de onderstaande lesinhoud.

Toon: warm, direct, nuchter. Geen zweverig taalgebruik. Korte zinnen.
Taal: Nederlands.

Gebruik EXACT dit format (geen extra secties, geen extra uitleg):

# Les {lesson_number}. {lesson_title}

## Kernboodschap
<1-2 zinnen die de essentie van de les bevatten>

## Inzichten
- <inzicht 1>
- <inzicht 2>
- <inzicht 3>
- <meer inzichten indien relevant>

## Quote
<één krachtige, concrete zin uit de les — letterlijk of sterk parafraseert>

---

Transcript:
{transcript}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate MD files for 365 Academy lessons")
    parser.add_argument("--folder", default=DEFAULT_FOLDER, help="Path to lesson folder")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        print(f"ERROR: folder not found: {folder}")
        sys.exit(1)

    # Get ANTHROPIC_API_KEY
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        # Try loading from .env files
        for env_path in [folder.parent.parent / ".env", Path("/opt/myPKA/.env")]:
            if env_path.exists():
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("ANTHROPIC_API_KEY="):
                            api_key = line.split("=", 1)[1].strip()
                            break
            if api_key:
                break

    client = None
    if api_key:
        client = anthropic.Anthropic(api_key=api_key)
    else:
        print("WARNING: ANTHROPIC_API_KEY not set — summaries will contain error message")

    # Discover all lessons from .srt files
    srt_files = sorted(folder.glob("Les *.srt"), key=lambda p: _lesson_sort_key(p.stem))

    if not srt_files:
        print("No lesson .srt files found.")
        sys.exit(0)

    counts = {"transcript": 0, "samenvatting": 0, "opdracht": 0}
    errors = []

    for srt_path in srt_files:
        stem = srt_path.stem  # e.g. "Les 1. Leven in vrijheid"
        txt_path = folder / (stem + ".txt")

        # Extract lesson number and title from stem
        m = re.match(r"^Les (\d+)\. (.+)$", stem)
        if not m:
            print(f"  SKIP (unexpected filename): {srt_path.name}")
            continue

        lesson_number = m.group(1)
        lesson_title = m.group(2)

        print(f"\nProcessing: {stem}")

        # --- 1. Transcript ---
        transcript_path = folder / f"{stem} - Transcript.md"
        try:
            srt_content = srt_path.read_text(encoding="utf-8", errors="replace")
            clean_text = strip_srt(srt_content)
            transcript_path.write_text(clean_text, encoding="utf-8")
            counts["transcript"] += 1
            print(f"  [OK] Transcript")
        except Exception as e:
            msg = f"ERROR generating transcript: {e}"
            transcript_path.write_text(msg, encoding="utf-8")
            errors.append(f"{stem} - Transcript: {e}")
            print(f"  [ERROR] Transcript: {e}")
            clean_text = ""

        # --- 2. Samenvatting ---
        samenvatting_path = folder / f"{stem} - Samenvatting.md"
        try:
            if not client:
                raise RuntimeError("ANTHROPIC_API_KEY not available")
            if not clean_text:
                # Re-read if transcript step failed
                srt_content = srt_path.read_text(encoding="utf-8", errors="replace")
                clean_text = strip_srt(srt_content)
            summary = generate_summary(lesson_number, lesson_title, clean_text, client)
            samenvatting_path.write_text(summary, encoding="utf-8")
            counts["samenvatting"] += 1
            print(f"  [OK] Samenvatting")
        except Exception as e:
            msg = f"ERROR generating summary: {e}"
            samenvatting_path.write_text(msg, encoding="utf-8")
            errors.append(f"{stem} - Samenvatting: {e}")
            print(f"  [ERROR] Samenvatting: {e}")

        # --- 3. Opdracht ---
        opdracht_path = folder / f"{stem} - Opdracht.md"
        try:
            if not txt_path.exists():
                raise FileNotFoundError(f".txt file not found: {txt_path}")
            html_content = txt_path.read_text(encoding="utf-8", errors="replace")
            md_content = html_to_markdown(html_content)
            # Normalize title: "# 22\. Titel" → "# Les 22. Titel"
            md_content = re.sub(r'^# (\d+)\\?\. ', f'# Les {lesson_number}. ', md_content, count=1)
            opdracht_path.write_text(md_content, encoding="utf-8")
            counts["opdracht"] += 1
            print(f"  [OK] Opdracht")
        except Exception as e:
            msg = f"ERROR generating opdracht: {e}"
            opdracht_path.write_text(msg, encoding="utf-8")
            errors.append(f"{stem} - Opdracht: {e}")
            print(f"  [ERROR] Opdracht: {e}")

    # --- Summary ---
    print("\n" + "=" * 50)
    print("DONE")
    print(f"  Transcripts  : {counts['transcript']}")
    print(f"  Samenvattingen: {counts['samenvatting']}")
    print(f"  Opdrachten   : {counts['opdracht']}")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
    else:
        print("  No errors.")


def _lesson_sort_key(stem: str) -> int:
    """Sort by lesson number."""
    m = re.match(r"^Les (\d+)\.", stem)
    return int(m.group(1)) if m else 999


if __name__ == "__main__":
    main()
