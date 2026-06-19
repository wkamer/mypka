# 2026-05-18 — Team Architecture Overhaul + Zara Hired

**session_id:** 66
**Date:** 2026-05-18
**Topics:** team-structure, hiring, meta-integration, knowledge-refresh

---

## Summary

De hiring flow is grondig herbouwd: Pax levert voortaan een world-class domeinbrief voordat Nolan een AGENT.md schrijft, met een verplichte Knowledge Currency sectie per specialist. Sienna's Priority Gate is uitgebreid van persoonlijk domein naar alle domeinen — zij bewaakt focus-verspringen ongeacht het domein, Marcus classificeert ICOR. Kai heeft mypka-meta-bridge.py gebouwd (aiohttp, poort 8766) als middleware tussen n8n en de Meta Graph API. Heptabase-kennis over het e-commerce process is gemigreerd naar KE-Advertising.md en KE-Fulfillment.md, bronbestanden verwijderd. Zara is aangenomen als Ads Intelligence Specialist voor Kamer E-commerce — eerste hire onder de nieuwe world-class flow, smoke test geslaagd.

---

## Decisions

- Pax-brief is harde voorwaarde voor elke nieuwe hire; Nolan schrijft niet zonder brief
- Knowledge Currency sectie is verplicht in elk AGENT.md
- Sienna bewaakt alle domeinen (niet alleen Personal)
- Marcus doet de ICOR-classificatie bij Priority Gate, niet Sienna
- Meta Bridge via aiohttp (Flask niet beschikbaar op server)

---

## Actions Taken

- CLAUDE.md: Hiring Rule herschreven, Sienna Priority Gate uitgebreid, Knowledge Refresh Protocol toegevoegd
- Sienna AGENT.md: scope uitgebreid naar alle domeinen, Priority Gate vereenvoudigd
- Marcus AGENT.md: Priority Gate Classification sectie toegevoegd
- Nolan AGENT.md: Domain Knowledge toegevoegd, upgrade naar Sonnet, Knowledge Currency sectie
- Pax AGENT.md: Hiring Research trigger en Knowledge Refresh protocol toegevoegd
- SOP-003: volledig herschreven met Pax-first flow
- KE-Advertising.md: Awareness x Funnel Matrix en hook types toegevoegd
- KE-Fulfillment.md: supplier validatie-checklist toegevoegd
- T-Prompts.md: Market Sophistication Mapper V3.4 ingevuld
- Zara AGENT.md aangemaakt, agent-index.md bijgewerkt
- mypka-meta-bridge.py + .env + systemd service aangemaakt en gestart

---

## Delegations

| Van | Naar | Brief | Uitkomst |
|---|---|---|---|
| Larry | Pax | World-class domeinbrief voor Ads Intelligence Specialist | Geslaagd — volledige brief inclusief Schwartz, Graduation System, Creative fatigue signals, Market Sophistication Mapper en change profile |
| Larry | Nolan | AGENT.md schrijven voor Zara + smoke test | Geslaagd — Domain Knowledge embedded, Knowledge Currency gedocumenteerd, smoke test geslaagd |
| Larry | Kai | mypka-meta-bridge.py bouwen + n8n workflow Meta-sectie | Geslaagd — bridge draait op poort 8766 als systemd service |

---

## Open Items

geen

---

## Team Log

**Architectural decision (all specialists):** Hiring flow herbouwd — Pax-first (world-class domeinbrief) → Nolan (AGENT.md met embedded Domain Knowledge + Knowledge Currency sectie). Knowledge Currency is voortaan verplicht in elk nieuw AGENT.md. Sienna bewaakt alle domeinen. Marcus is verantwoordelijk voor ICOR-classificatie bij Priority Gate.

---

## Agent Learnings

| Specialist | What Worked | To Improve |
|---|---|---|
| Pax | Hiring research bevat nu change profile (output 6): wat verandert, hoe snel, welke signalen | Zonder change profile kent Nolan de verversingsfrequentie niet |
| Nolan | Pax-brief is harde voorwaarde; smoke test is afwegingsvraag, niet taakvraag | Vorige Nolan schreef zonder onderzoek; resultaat was generieke structuur zonder expertise |
| Sienna | Priority Gate geldt alle domeinen; Marcus classificeert ICOR | Sienna greep niet in op KE-activiteiten — haar rol is domein-onafhankelijk |
| Marcus | Priority Gate Classification: Goal / Project / Workstream / Task / KE / Topic / Idea | Marcus was niet uitgerust voor ICOR-classificatie bij Priority Gate |
| Kai | Meta Bridge via aiohttp als Flask niet beschikbaar; credentials altijd via EnvironmentFile | Flask niet geïnstalleerd; aiohttp beschikbaar via discord bridge |
| Zara | Eerste smoke test geslaagd: correcte awareness + sophistication vertaald naar hook-richting | Eerste hire onder nieuwe world-class flow — bewijst dat de flow werkt |
