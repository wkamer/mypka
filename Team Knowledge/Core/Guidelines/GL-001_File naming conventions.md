# GL-001 — File Naming Conventions

**Applies to:** entire myPKA vault
**Exception:** scripts (Python, PowerShell) use kebab-case without spaces

---

## General Rule

Use spaces in file names and folder names. No underscores as word separators, no camelCase.

---

## Folder Names

Title Case everywhere.

```
Team Knowledge/
PKM/My Life/
Kamer E-commerce/
```

---

## File Names by Type

| Type | Format | Example |
|---|---|---|
| General | Descriptive name with spaces | `project overview.md` |
| Journal | `YYYYMMDD_subject 1, subject 2.md` | `20260509_football, daughter, paris.md` |
| Session log | `YYYYMMDD_description.md` in `YYYY/MM/` | `2026/05/20260509_scaffold restructure.md` |
| Deliverable | `YYYYMMDD_Domain_description/` | `20260509_Kamer E-commerce_US store audit/` |
| Image | `YYYYMMDD_description.ext` | `20260509_business card anna.jpg` |
| CRM People | `LastName, FirstName.md` | `De Vries, Ylana.md` |
| CRM Organizations | `Full Name.md` | `Kamer E-commerce.md` |
| Topic | `T-Name.md` | `T-AI.md`, `T-Trading.md` |
| Key Element | `KE-Domain.md` | `KE-Finance.md`, `KE-Self.md` |
| Project (folder) | `P-ProjectName` | `P-Geldstroom Regie` |
| Goal (folder) | `G-Title` | `G-Financiële vrijheid` |
| SOP | `SOP-001_Title.md` | `SOP-001_How to hire a new team member.md` |
| Guideline | `GL-001_Title.md` | `GL-001_File naming conventions.md` |
| Workstream | `WS-001_Title.md` | `WS-001_Daily journaling.md` |
| Script (Python) | `snake_case.py` | `add_task.py`, `session_open.py` |
| Script (PowerShell) | `kebab-case.ps1` | `session-open.ps1` |

---

## ALL CAPS

Only for Project, Topic, and Key Element names in the file name itself (after the prefix):
- `T-AI.md`, `T-TRADING.md` → only when it is an abbreviation or proper noun
- Regular words: lowercase after prefix: `T-nutrition.md`, `KE-health.md`

---

## Numbering (SOP/GL/WS)

- Numbers are unique per domain, not globally
- Format: three digits (`001`, `002`, ...)
- Order: chronologically created

---

## Wikilinks

Always use the exact file name without the extension:
```
[[De Vries, Ylana]]
[[T-AI]]
[[SOP-001_How to hire a new team member]]
```

---

## Changelog

- 2026-06-04 (Larry, B-063): Full English translation. No convention rules changed. Approved by Owner Walter Kamer.
