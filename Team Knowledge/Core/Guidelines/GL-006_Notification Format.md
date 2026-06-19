# GL-006 — Notification Format

## Purpose

Universal format for all system notifications across the myPKA ecosystem. Every specialist and integration uses this format so notifications are consistent, readable, and actionable regardless of source.

---

## Format

Every notification contains exactly four fields, always in English:

| Field | Description | Example |
|---|---|---|
| **Source** | The system the notification originates from | `Shopify`, `Meta`, `Discord`, `myPKA` |
| **Subject** | The specific component within that system | `Order`, `Ad`, `Team Inbox` |
| **Status** | What happened | `New`, `Uploaded`, `Updated`, `Failed`, `Completed` |
| **Message** | Relevant details — one `key: value` per line | `location: /opt/myPKA/Team Inbox/brief.pdf` |

---

## Discord Embed Implementation

All four fields are rendered as embed fields — no title, no author. Color indicates status.

| Embed property | Value |
|---|---|
| `color` | Status color (see below) |
| Field 1 | `Source` |
| Field 2 | `Subject` |
| Field 3 | `Status` |
| Field 4 | `Message` — one key: value per line, not inline |
| `timestamp` | Always included — UTC |

### Status colors

| Status | Color | Hex | Discord int |
|---|---|---|---|
| Success / New / Uploaded / Completed | Green | `#57F287` | `5763719` |
| Warning / Pending / Attention | Orange | `#FEE75C` | `16638812` |
| Failed / Error | Red | `#ED4245` | `15548997` |

---

## Example

```json
{
  "embeds": [{
    "color": 5763719,
    "fields": [
      {"name": "Source",  "value": "Discord",                                     "inline": false},
      {"name": "Subject", "value": "Team Inbox",                                  "inline": false},
      {"name": "Status",  "value": "Uploaded",                                    "inline": false},
      {"name": "Message", "value": "location: /opt/myPKA/Team Inbox/brief.pdf",  "inline": false}
    ],
    "timestamp": "2026-05-18T18:00:00Z"
  }]
}
```

---

## Rules

- All field values in **English**
- Message uses `key: value` notation — one per line for multiple values
- Never omit a field — use `—` if a value is not applicable
- Color always reflects the Status, not the content
- No embed title or author — the four fields carry all context

---

*Aangemaakt: 2026-05-18 | Kai*
