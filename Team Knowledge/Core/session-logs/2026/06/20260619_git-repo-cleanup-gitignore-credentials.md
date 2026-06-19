# Git repo cleanup — .gitignore, credentials, history rewrite

**Date:** 2026-06-19
**Agent:** Larry
**Domain:** Team

## What happened

Fixed /doctor issues: removed leftover npm claude-code installation at /usr/bin/claude. Added auto git commit + push step to /close-session skill. Committed all 2123 previously untracked files to the private GitHub repo. Built out .gitignore iteratively (logs, pycache, env files, credential files). Removed credential files (client_secret.json, token.json, larry-bridge.env) from full git history using git filter-repo and force-pushed. Fixed VSC "publish branch" issue by restoring upstream tracking reference.

## Decisions

- All files committed to private GitHub repo — safe because repo is private
- Blanket .gitignore rules: `**/*.log`, `**/__pycache__/`, `**/*.pyc`, `**/*.env`, `**/client_secret*.json`, `**/token.json`
- Credentials removed from full history, not just HEAD
- /close-session now auto-commits and pushes at every session close

## Actions taken

- npm uninstall @anthropic-ai/claude-code (leftover at /usr/bin/claude)
- git add -A + commit + push (2123 files)
- .gitignore built iteratively: logs → pycache → env/credentials
- git rm --cached for all excluded files
- git filter-repo to rewrite history and purge credentials
- Force push to remote
- git branch --set-upstream-to to restore VSC sync button

## Open items

None
