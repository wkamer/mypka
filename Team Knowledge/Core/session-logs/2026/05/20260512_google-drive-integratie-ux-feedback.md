# Google Drive integratie + UX feedback borging

**Datum:** 2026-05-12
**Duur:** ~2 uur
**Topics:** google-api, drive, ux-feedback, routing
**DB id:** 44 (team-knowledge.db)

## Samenvatting

Google Drive scope toegevoegd aan google_helper.py en google_auth.py, token vernieuwd. Drive operaties uitgevoerd: testdoc aangemaakt en verwijderd, 7 rootbestanden verplaatst naar /myPKA - Archive. Feedback regels voor tabelweergave geborgd in memory. Claude.ai MCP connectors voor Gmail/Calendar kunnen alleen via web UI verwijderd worden.

## Besluiten

- Drive API via google_helper.py ipv MCP
- Google mutaties altijd met bevestigingstabel
- Highlight of the Day als aparte tabel #0 boven taakoverzicht

## Acties

- Drive scope toegevoegd aan google_helper.py + google_auth.py
- Token vernieuwd
- /myPKA - Archive folder aangemaakt in Google Drive
- 7 rootbestanden verplaatst naar /myPKA - Archive
- 4 memory feedback files bijgewerkt

## Delegaties

Geen

## Open items

- Claude.ai Gmail + Calendar MCP verwijderen via web UI
