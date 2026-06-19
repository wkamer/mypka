# myPKA herstructurering — scaffold-alignering

**Datum:** 2026-05-09
**Session ID:** 34
**Topics:** structuur, scaffold, PKA, migratie

## Samenvatting

Volledige herstructurering van de myPKA vault naar de Paperless Movement scaffold (v1.0.0). Multi-domain structuur omgezet naar één root met Team/, Team Knowledge/, PKM/, Deliverables/ en Team Inbox/. Alle paden bijgewerkt in CLAUDE.md, agent-bestanden, scripts en memory. core.db hernoemd naar team-knowledge.db. CRM aangemaakt en gevuld, README/INDEX-bestanden geschreven.

## Beslissingen

- Eén root-structuur i.p.v. multi-domain mappen
- Team Knowledge per domein (Core, Kamer E-commerce, Geldstroom Regie)
- PKM op root niveau voor persoonlijke kennis
- SOPs en Guidelines per domein, niet in root
- core.db → team-knowledge.db
- Scripts naar Team Knowledge/Core/Scripts/

## Acties

- Memory gemigreerd van C--Users-wkame-My-AI naar C--Users-wkame-myPKA
- Alle "My AI" referenties vervangen door "myPKA" (33 bestanden)
- 8 agents verplaatst naar root Team/
- Team Knowledge/, PKM/, Deliverables/, Team Inbox/ aangemaakt
- Deliverables en Inboxes per domein gemigreerd
- core.db hernoemd naar team-knowledge.db (36 bestanden bijgewerkt)
- agent-index.md aangemaakt
- README's aangemaakt voor Deliverables, PKM, Team Inbox, PKM/My Life
- PKM/INDEX.md aangemaakt
- CRM gevuld (4 personen, 3 organisaties)
- Oude domeinmappen verwijderd

## Delegaties

None

## Open items

- /start-session en /close-session skills verwijzen nog naar oude paden
- session_open.py script controleren op nieuwe paden
