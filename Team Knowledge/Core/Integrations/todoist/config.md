# Todoist Integration

## What it is

Todoist is the owner's personal task manager. The myPKA ecosystem reads and writes tasks via the Todoist REST API v2.

## Authentication

- **Method:** Bearer token (personal API token)
- **Bitwarden item:** "Todoist / API Token"
- **Token location:** passed via environment variable or script parameter — never hardcoded

## Permissions

Personal API tokens have full access to the account. Scoping is not available at token level — apply least-privilege at the code level (only call the endpoints needed).

## Key project IDs

Stored in CLAUDE.md and agent routing rules — not duplicated here. Read `[[CLAUDE.md]]` Task Management Rule section.

## Rate limits

- 450 requests per 15 minutes
- Burst: up to 100 requests per 10 seconds
- On 429: back off and retry after the `Retry-After` header value

## Used by

Sienna, Larry (task reads/writes via scripts in `Team Knowledge/Core/Scripts/`)
