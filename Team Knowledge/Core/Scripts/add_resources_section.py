"""
add_resources_section.py

Adds a standard ## Resources section to all existing entity files
that don't already have one.

Entity files: KE, Project (project.md), Goal (goal.md), Topic (T-*.md), Habit (H-*.md)
"""

import os
import glob

VAULT = "/opt/myPKA/PKM/My Life"

RESOURCES_BLOCK = """## Resources

**Articles**
-

**Audios**
-

**Books**
-

**Emails**
-

**Files**
-

**Notes**
-

**Recipes**
-

**Videos**
-

**Websites**
-

---

"""

def find_files():
    patterns = [
        f"{VAULT}/Key Elements/KE-*.md",
        f"{VAULT}/Projects/P-*/project.md",
        f"{VAULT}/Goals/G-*/goal.md",
        f"{VAULT}/Topics/T-*.md",
        f"{VAULT}/Habits/H-*.md",
    ]
    files = []
    for pattern in patterns:
        files.extend(glob.glob(pattern, recursive=False))
    return sorted(files)


def add_resources(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "## Resources" in content:
        return "skip"

    # Determine insertion point
    markers = ["## Related\n", "*Delivered on:*", "*Aangemaakt:*"]
    insert_pos = None
    for marker in markers:
        idx = content.find(marker)
        if idx != -1:
            insert_pos = idx
            break

    if insert_pos is not None:
        new_content = content[:insert_pos] + RESOURCES_BLOCK + content[insert_pos:]
    else:
        new_content = content.rstrip() + "\n\n---\n\n" + RESOURCES_BLOCK

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return "added"


def main():
    files = find_files()
    added, skipped = [], []

    for path in files:
        result = add_resources(path)
        name = os.path.relpath(path, VAULT)
        if result == "added":
            added.append(name)
        else:
            skipped.append(name)

    print(f"Added Resources section: {len(added)} files")
    for f in added:
        print(f"  + {f}")
    print(f"\nSkipped (already have Resources): {len(skipped)} files")
    for f in skipped:
        print(f"  = {f}")


if __name__ == "__main__":
    main()
