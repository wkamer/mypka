# Sync KE-Finance MD naar Google Sheets Expenses tab

**Datum:** 2026-05-13
**Duur:** ~1,5 uur
**Topics:** finance-sync, google-sheets, geldstroom, scripting
**DB:** geldstroom-regie.db (session_id=8)

## Samenvatting

KE-Finance data.md gesynchroniseerd met Google Sheets Expenses tab via directe Sheets API calls. Hypotheek bijgewerkt naar 1.000, Servicekosten als aparte regel toegevoegd, zes nieuwe posten toegevoegd (Claude Code, vier Univé verzekeringen). Meerdere correcties doorgevoerd: formule separatoren, kommanotatie voor bedragen, categorie-sortering (Housing dan Insurance dan rest), ontbrekende Uitvaartverzekering hersteld, Univé encoding gefixed met python -X utf8. Een open item: Univé staat niet in de Table dropdown validation en moet handmatig worden toegevoegd.

## Besluiten

- MD (KE-Finance data.md) is leidend boven sheet
- Alleen Amount en Period schrijven; berekende kolommen nooit overschrijven
- Bedragen altijd met komma als decimaalteken
- Formules altijd met puntkomma als scheidingsteken
- Housing eerst, Insurance daarna in Expenses tab

## Acties

- Hypotheek 1.250 naar 1.000
- Servicekosten 250 toegevoegd (Housing, rij 3)
- Claude Code, Fietsverzekering, Aansprakelijkheidsverzekering, Doorlopende reisverzekering, Autoverzekering toegevoegd
- Uitvaartverzekering hersteld na verlies bij sortering
- Formules hersteld in alle nieuwe rijen
- Univé correct geschreven via python -X utf8

## Delegaties

Geen

## Open items

- Univé handmatig toevoegen aan Payee dropdown validation in Expenses tab (Table-level, niet via API bereikbaar)
