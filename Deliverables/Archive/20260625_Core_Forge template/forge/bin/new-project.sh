#!/usr/bin/env bash
#
# Forge — new project bootstrapper.
# Prompts for key metadata, stamps the template, and hands you a ready-to-work
# project folder. Start the project by: cd <project> && claude .
#
set -euo pipefail

FORGE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE_DIR="$FORGE_DIR/template"

bold() { printf "\033[1m%b\033[0m\n" "$1"; }
ask() {  # ask "Prompt" "default" -> echoes answer
  local prompt="$1" def="${2:-}" ans
  if [ -n "$def" ]; then read -r -p "$prompt [$def]: " ans; echo "${ans:-$def}";
  else read -r -p "$prompt: " ans; echo "$ans"; fi
}
askyn() {  # askyn "Prompt" "y|n" -> echoes y or n
  local prompt="$1" def="${2:-y}" ans
  read -r -p "$prompt ($([ "$def" = y ] && echo "Y/n" || echo "y/N")): " ans
  ans="${ans:-$def}"; case "$ans" in [Yy]*) echo y;; *) echo n;; esac
}

[ -d "$TEMPLATE_DIR" ] || { echo "ERROR: template/ not found at $TEMPLATE_DIR"; exit 1; }

bold "── Forge · new project ─────────────────────────────"
NAME="$(ask 'Project name (display)')"
[ -n "$NAME" ] || { echo "Project name is required."; exit 1; }
DEFAULT_SLUG="$(echo "$NAME" | tr '[:upper:] ' '[:lower:]-' | tr -cd 'a-z0-9-')"
SLUG="$(ask 'Folder/repo slug' "$DEFAULT_SLUG")"
VISION="$(ask 'One-line vision / north star')"
OWNER="$(ask 'Owner name' "$(git config user.name 2>/dev/null || echo "$USER")")"
STACK="$(ask 'Primary stack (free text, Arch finalises later)' 'TBD — Arch gate')"
DEST="$(ask 'Destination directory' "$(dirname "$FORGE_DIR")")"
HAS_UI="$(askyn 'Human-facing UI? (activates UX + accessibility gate)' y)"
HAS_AI="$(askyn 'LLM / AI components? (activates eval + prompt-versioning gate)' y)"
DO_GIT="$(askyn 'Initialise git + first commit?' y)"

TARGET="$DEST/$SLUG"
[ -e "$TARGET" ] && { echo "ERROR: $TARGET already exists. Aborting."; exit 1; }

UX_GATE=$([ "$HAS_UI" = y ] && echo "ACTIVE — human-facing surface present" || echo "inactive — no human-facing surface")
EVAL_GATE=$([ "$HAS_AI" = y ] && echo "ACTIVE — LLM/agent components present" || echo "inactive — no AI components")
TODAY="$(date +%F)"

bold "\nCreating $TARGET ..."
cp -R "$TEMPLATE_DIR" "$TARGET"

# Seed runnable env files from the examples (secrets left blank on purpose).
[ -f "$TARGET/.env.example" ]         && cp "$TARGET/.env.example" "$TARGET/.env"
[ -f "$TARGET/.env.secrets.example" ] && cp "$TARGET/.env.secrets.example" "$TARGET/.env.secrets"

# Stamp placeholders across every template file (perl -i is portable mac/linux).
export PROJECT="$NAME" SLUG VISION OWNER STACK TODAY UX_GATE EVAL_GATE
grep -rIl '{{' "$TARGET" | while IFS= read -r f; do
  perl -pi -e '
    s/\{\{PROJECT\}\}/$ENV{PROJECT}/g;
    s/\{\{SLUG\}\}/$ENV{SLUG}/g;
    s/\{\{VISION\}\}/$ENV{VISION}/g;
    s/\{\{OWNER\}\}/$ENV{OWNER}/g;
    s/\{\{STACK\}\}/$ENV{STACK}/g;
    s/\{\{DATE\}\}/$ENV{TODAY}/g;
    s/\{\{UX_GATE\}\}/$ENV{UX_GATE}/g;
    s/\{\{EVAL_GATE\}\}/$ENV{EVAL_GATE}/g;
  ' "$f"
done

if [ "$DO_GIT" = y ]; then
  git -C "$TARGET" init -q
  git -C "$TARGET" add -A
  git -C "$TARGET" commit -qm "chore: scaffold $SLUG from Forge" >/dev/null
  echo "git initialised + first commit made."
fi

bold "\n✓ Project ready: $TARGET"
cat <<EOF

Next:
  cd "$TARGET"
  claude .          # Larry boots from CLAUDE.md — Gate 1 (Discovery) is open

Profile baked in:  UX gate: $UX_GATE
                   Eval gate: $EVAL_GATE
EOF
