---
status: raw
datum: 2026-05-11
---

# I-AI-platform voor klantintake en data-aanlevering

## Idee

Een iteratief, AI-gedreven platform waarop de klant zelfstandig de intake kan doorlopen en bankdata kan aanleveren. De scan wordt dan deels of volledig geautomatiseerd uitgevoerd op basis van de aangeleverde data.

## Aanleiding

De scan-methodiek (SOP-002) stelt concrete eisen aan input: rekeningstructuur, bankexports, situatieschets. Dit is herhaalbaar en gestructureerd — en daarmee geschikt voor automatisering via een platform.

## Kernideeën

- Klant doorloopt een gestructureerde intake via een AI-interface (chatbot of formulier)
- Klant levert bankexport aan (CSV upload)
- Platform verwerkt de data per geldstroom op basis van de scan-methodiek
- Iteratief: platform stelt gerichte vervolgvragen waar data ontbreekt of onduidelijk is
- Output: conceptscan die de adviseur reviewt en finaliseert

## Waarom dit past

- De intake-vragen (SOP-002 Stap 0–4) zijn gestandaardiseerd en herhaalbaar
- Het iteratieve bevragingsmodel is al bewezen in de testcase
- Schaalbaar: meerdere klanten tegelijk zonder evenredige tijdsinvestering van de adviseur

## Open vragen

- Welk platform / technologie? (Claude API, custom app, no-code tool)
- Wie beheert en bouwt dit? (Finn voor techniek, Vera voor methodiek)
- Hoe verhoudt dit zich tot de AFM-afbakening? (platform levert scan, geen advies)
- Wat is de MVP — minimale versie die al waarde levert?
- Hoe ga je om met privacygevoelige bankdata (AVG)?
