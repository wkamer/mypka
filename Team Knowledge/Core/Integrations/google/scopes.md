# Google OAuth Scopes

**Application:** myPKA ecosystem scripts via `google_helper.py`

## Active scopes

| Scope | Purpose |
|---|---|
| `https://www.googleapis.com/auth/spreadsheets` | Read/write Google Sheets (finance, planning data) |
| `https://www.googleapis.com/auth/gmail.modify` | Read, send, and label Gmail (not delete) |
| `https://www.googleapis.com/auth/calendar` | Read/write Google Calendar events |
| `https://www.googleapis.com/auth/drive` | Read/write Google Drive files |

## Notes

- Scopes are defined in `google_helper.py` (`SCOPES` list)
- `token.json` is the OAuth 2.0 refresh token — never commit to git
- `client_secret.json` is the OAuth 2.0 client credentials — never commit to git
- To re-authenticate: delete `token.json` and run any script that calls `get_credentials()` — it will open a browser auth flow
- Token refreshes automatically when expired (via `creds.refresh()` in `google_helper.py`)
