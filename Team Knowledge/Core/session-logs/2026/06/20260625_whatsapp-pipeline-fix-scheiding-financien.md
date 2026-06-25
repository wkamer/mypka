# WhatsApp pipeline fix + scheiding financiën analyse

**Datum:** 2026-06-25
**Agent:** Larry
**Domain:** Personal + Team (infra)
**DB row:** personal.db session_logs id=77

---

## Wat is er gebeurd

WhatsApp export pipeline was kapot door een ontbrekend Python venv pad (`/opt/mypka-memory/venv/bin/python`). Kai heeft het pad gefixt naar `/usr/bin/python3` in `sync_handler.sh` (r134) en `whatsapp_export_handler.py` (shebang), commit `f73396d`. Pipeline verwerkte direct 8 nieuwe dagen (17–24 juni).

Analyse van Wendy's €13,11 claim (deo, dextro, lactose tabletten): dit is dagelijks levensonderhoud, geen overkosten. Vera analyseerde gevolgen van stoppen coulance: niet abrupt stoppen zolang huis niet overgedragen is; boodschappenstop (€289) kan eerder (per 1 augustus). Penn journaliseerde Walters frustratie (id=75). Sienna draftte een WhatsApp bericht naar Wendy over stoppen extra betalingen. Walter laat het voorlopig rusten.

---

## Besluiten

- Lactose tabletten, deo en dextro zijn dagelijks levensonderhoud, geen overkosten
- Niet abrupt stoppen met coulance zolang huis niet overgedragen is
- Boodschappenbijdrage (€289) kan eerder stoppen, per 1 augustus is verdedigbaar
- WhatsApp bericht klaar maar Walter wacht op goed moment om te sturen

---

## Acties uitgevoerd

- Kai: Python pad gefixt, commit f73396d, gepusht
- Pipeline: 8 nieuwe WA-bestanden verwerkt (17–24 juni)
- Penn: journal entry id=75 geschreven over coulance frustratie
- Vera: financiële analyse coulancestopping
- Sienna: concept WhatsApp bericht gedraft en gereviewd

---

## Open items

- WhatsApp bericht naar Wendy klaar — Walter stuurt zelf op goed moment (vanavond of later)
- Huisoverdracht is sleutelmoment voor stoppen volledige coulance — nog open
- Formele alimentatiestart nog open
