"""
rename_365academy_module1.py

Renames all lesson files in the Module 1. Vrijheid folder to the pattern:
    Les <nr>. <titel>.<ext>

Strips the prefix "Module 1. Vrijheid - " from the current filenames.
Title is extracted from the <h1> tag in the corresponding .txt file.
The .jpg wallpaper is matched by les-<nr> in its filename.

Usage:
    python rename_365academy_module1.py [--execute]

Without --execute: preview mode (default).
With --execute: performs the actual renames.
"""

import os
import re
import sys
import argparse

FOLDER = "/opt/myPKA/Team Inbox/1. Vrijheid"
SKIP_FILE = "Introductie - Vrij van verlangen vrede met jezelf.txt"
OLD_PREFIX = "Module 1. Vrijheid - "


def extract_h1_title(txt_path: str) -> str:
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"<h1>(.*?)</h1>", content)
    if not match:
        raise ValueError(f"No <h1> found in {txt_path}")
    h1_text = match.group(1)
    # Strip leading "N. " number prefix from h1 content
    stripped = re.sub(r"^\d+\.\s+", "", h1_text)
    # Windows-compatibility: replace colons with semicolons
    stripped = stripped.replace(":", ";")
    return stripped


def build_rename_map(folder: str) -> list[tuple[str, str]]:
    """Returns list of (old_name, new_name) pairs (filenames only, not full paths)."""
    files = os.listdir(folder)
    renames = []

    # Current filenames after previous rename:
    # "Module 1. Vrijheid - Les <nr>. <title>.<ext>"
    # Target: "Les <nr>. <title>.<ext>"
    current_re = re.compile(
        r"^Module 1\. Vrijheid - (Les \d+\. .+\.(mp4|srt|txt|jpg))$"
    )

    # Also handle any original source files that were not yet renamed
    # (365-academy pattern), so the script remains idempotent for fresh runs.
    lesson_txt_re = re.compile(r"^365-academy - 1\.(\d+) .+\.txt$")
    jpg_re = re.compile(r"^.+-miracle-roadmap_les-(\d+)\.jpg$")
    media_re = re.compile(r"^365-academy - 1\.(\d+) .+\.(mp4|srt|txt)$")

    # --- Path 1: strip OLD_PREFIX from already-renamed files ---
    for fname in files:
        if fname == SKIP_FILE:
            continue
        m = current_re.match(fname)
        if m:
            new_name = m.group(1)  # everything after the prefix
            if fname != new_name:
                renames.append((fname, new_name))

    # --- Path 2: original source files (fresh run, no prior rename) ---
    if not renames:
        # Build lesson number -> title map from txt files
        lesson_titles: dict[int, str] = {}
        for fname in files:
            m = lesson_txt_re.match(fname)
            if m:
                nr = int(m.group(1))
                txt_path = os.path.join(folder, fname)
                title = extract_h1_title(txt_path)
                lesson_titles[nr] = title

        for fname in files:
            m = media_re.match(fname)
            if m:
                nr = int(m.group(1))
                ext = m.group(2)
                title = lesson_titles.get(nr)
                if title is None:
                    raise ValueError(f"No title found for lesson {nr}")
                new_name = f"Les {nr}. {title}.{ext}"
                if fname != new_name:
                    renames.append((fname, new_name))

        for fname in files:
            m = jpg_re.match(fname)
            if m:
                nr = int(m.group(1))
                title = lesson_titles.get(nr)
                if title is None:
                    raise ValueError(f"No title found for lesson {nr} (jpg)")
                new_name = f"Les {nr}. {title}.jpg"
                if fname != new_name:
                    renames.append((fname, new_name))

    # Sort by lesson number, then extension
    ext_order = {"mp4": 0, "srt": 1, "txt": 2, "jpg": 3}
    les_re = re.compile(r"Les (\d+)\.")

    def sort_key(item):
        fname = item[0]
        m = les_re.search(fname)
        nr = int(m.group(1)) if m else 0
        ext = os.path.splitext(fname)[1].lstrip(".")
        return (nr, ext_order.get(ext, 9))

    renames.sort(key=sort_key)
    return renames


def print_preview(renames: list[tuple[str, str]]) -> None:
    if not renames:
        print("Nothing to rename — all files already match the target pattern.")
        return
    col_width = max(len(old) for old, _ in renames) + 2
    print(f"\n{'PREVIEW — 365 Academy Module 1 rename':^80}")
    print("=" * 80)
    print(f"{'OLD':<{col_width}} NEW")
    print("-" * 80)
    for old, new in renames:
        print(f"{old:<{col_width}} {new}")
    print("-" * 80)
    print(f"{len(renames)} files will be renamed.\n")


def execute_renames(folder: str, renames: list[tuple[str, str]]) -> None:
    for old, new in renames:
        old_path = os.path.join(folder, old)
        new_path = os.path.join(folder, new)
        os.rename(old_path, new_path)
        print(f"  Renamed: {old}  ->  {new}")
    print(f"\nDone. {len(renames)} files renamed.")


def main():
    parser = argparse.ArgumentParser(description="Rename 365 Academy Module 1 lesson files.")
    parser.add_argument("--execute", action="store_true", help="Perform the actual renames (default: preview only)")
    args = parser.parse_args()

    renames = build_rename_map(FOLDER)
    print_preview(renames)

    if args.execute:
        if not renames:
            return
        print("Executing renames...")
        execute_renames(FOLDER, renames)
    else:
        if renames:
            print("Preview only. Run with --execute to apply.")


if __name__ == "__main__":
    main()
