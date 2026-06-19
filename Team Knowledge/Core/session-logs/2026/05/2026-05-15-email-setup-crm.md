# Email setup, CRM uitbreiding en send_email.py

**Datum:** 2026-05-15
**Topics:** email, crm, tooling, borging
**Agent:** Larry

## Samenvatting

Sessie gericht op het opzetten van een volwaardige email-workflow via Gmail API. `send_email.py` gebouwd en iteratief verfijnd: MD naar HTML conversie, automatische signature, juiste opmaak en tone of voice. Daarnaast CRM uitgebreid met Accu-Chek en owner.md (Walter Kamer). Alles geborgd in memory, GL-003 en de guidelines index.

## Beslissingen

- Email altijd via `send_email.py` met MD als input
- Draft altijd als plaintext codeblock tonen voor verzending
- Signature automatisch toegevoegd, nooit in body meegeven
- Tone of voice: warm, direct, nuchter, Hi `<naam>` als aanhef

## Acties genomen

- `send_email.py` gebouwd met Gmail API, MD conversie, HTML template en signature
- `PKM/CRM/Organizations/Accu-Chek.md` aangemaakt
- `PKM/CRM/People/owner.md` aangemaakt (Walter Kamer)
- `GL-003_Email setup.md` aangemaakt en `gl-index.md` opgezet
- Memory geborgd: tone of voice, email setup, email opmaak, draft bevestiging

## Delegaties

Geen.

## Open items

Geen.
