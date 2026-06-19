"""
rename_365academy_module3.py

Renames all lesson files in the Module 3. Essentie folder to:
    Les <nr>. <titel>.<ext>

Title is extracted from the <h1> tag in the corresponding .txt file.
The .jpg wallpaper is matched by les-<nr> in its filename.

Usage:
    python rename_365academy_module3.py [--execute]

Without --execute: preview mode (default).
With --execute: performs the actual renames.
"""

import os
import re
import argparse

FOLDER = "/opt/myPKA/Team Inbox/3. Essentie"
SKIP_FILES = {
    "Introductie - De Eenvoud van Essentie vrede met het nu.txt",
}


def extract_h1_title(txt_path: str) -> str:
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"<h1>(.*?)</h1>", content)
    if not match:
        raise ValueError(f"No <h1> found in {txt_path}")
    h1_text = match.group(1)
    stripped = re.sub(r"^\d+\.\s*", "", h1_text)
    stripped = stripped.replace(":", ";")
    stripped = stripped.rstrip(".")
    return stripped.strip()


def build_rename_map(folder: str) -> list[tuple[str, str]]:
    files = os.listdir(folder)
    renames = []

    lesson_txt_re = re.compile(r"^365-academy - 3\.(\d+) .+\.txt$")
    jpg_re = re.compile(r"^.+-miracle-roadmap[-_]les-(\d+)\.jpg$")
    media_re = re.compile(r"^365-academy - 3\.(\d+) .+\.(mp4|srt|txt)$")

    lesson_titles: dict[int, str] = {}
    for fname in files:
        if fname in SKIP_FILES:
            continue
        m = lesson_txt_re.match(fname)
        if m:
            nr = int(m.group(1))
            txt_path = os.path.join(folder, fname)
            title = extract_h1_title(txt_path)
            lesson_titles[nr] = title

    for fname in files:
        if fname in SKIP_FILES:
            continue
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
    print(f"\n{'PREVIEW — 365 Academy Module 3 rename':^80}")
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
    parser = argparse.ArgumentParser(description="Rename 365 Academy Module 3 lesson files.")
    parser.add_argument("--execute", action="store_true")
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
