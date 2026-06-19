# Google API setup herontdekt en geborgd

**Datum:** 2026-05-13
**Duur:** ~15 min
**Topics:** google-api, infrastructure, memory, scripts
**DB:** team-knowledge.db (session_id=45)

## Samenvatting

Ontdekt dat alle Google communicatie verloopt via google_helper.py scripts in Team Knowledge/Core/Scripts/ en niet via MCP integraties. Dit was eerder opgezet maar niet geborgd in memory. Setup geborgd: token.json authenticatie, Sheets/Gmail/Calendar/Drive beschikbaar. Memory bijgewerkt met aanpak en UTF-8 vereiste voor speciale tekens.

## Besluiten

- Alle Google API calls via google_helper.py
- MCP Google integraties worden niet gebruikt
- Scripts met speciale tekens uitvoeren met python -X utf8

## Acties

- Memory aangemaakt: reference_google_api.md
- Memory aangemaakt: feedback_sheet_sync_columns.md
- Memory aangemaakt: feedback_sheet_amount_format.md

## Delegaties

Geen

## Open items

Geen
