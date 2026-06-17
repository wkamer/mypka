#!/usr/bin/env bash
# Stages all tracked modifications and commits with an auto-generated message.
# Run at session close. Untracked files are never auto-staged.

cd /opt/myPKA || exit 1

if git diff --quiet && git diff --cached --quiet; then
    echo "Nothing to commit."
    exit 0
fi

git add -u

FILES=$(git diff --cached --name-only | head -10 | paste -sd ', ')
COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

git commit -m "Session changes ($COUNT files) — $TIMESTAMP

$FILES"

echo "Committed $COUNT file(s)."
