# GL-008 — WhatsApp conversatie borging

## Doel

Standaard werkwijze voor het opslaan van WhatsApp-conversaties in het PKM-systeem. Van toepassing op alle agents die chatgesprekken verwerken of archiveren.

---

## Opslaglocatie

Chatgesprekken met relevantie voor een project of dossier worden opgeslagen in de projectmap:

```
PKM/My Life/Projects/P-<Projectnaam>/YYYYMMDD_<persoon>-berichten-<onderwerp>.md
```

---

## Bestandsformaat

### Header

```
# <Persoon> — berichten <onderwerp>

**Datum:** YYYY-MM-DD
**Aanleiding:** <korte beschrijving van de context>

---

## Conversatie
```

### Berichtformaat

Elk bericht op deze manier:

```
**HH:MM — Naam**
"Berichttekst tussen aanhalingstekens."
```

### Reply-formaat

Wanneer een bericht een reply is op een eerder bericht:

```
**HH:MM — Naam** *(reply op: "exacte geciteerde tekst")*
"Berichtinhoud van de reply."
```

### Footer

```
---

*Gerelateerd: [[wikilinks]]*
*Delivered on: YYYY-MM-DD*
```

---

## Regels

1. **Alle berichtteksten tussen aanhalingstekens** — zowel de berichtinhoud als de geciteerde tekst in een reply.
2. **Reply-quotes zijn geen dubbeling** — WhatsApp toont de geciteerde tekst boven het reply-bericht. Beide altijd opslaan.
3. **Geciteerde tekst letterlijk** — nooit parafraseren, altijd de exacte woorden.
4. **Afzender altijd vermeld** — nooit een bericht zonder naam.
5. **Tijdstempel altijd vermeld** — formaat HH:MM.
6. **Niets weglaten** — ook berichten die kort of herhalend lijken kunnen in context belangrijk zijn.

---

## Voorbeeld

```
**09:11 — Walter**
"Wanneer heb jij tijd om het over het ouderschapsplan te hebben?"

**09:11 — Wendy** *(reply op: "Wanneer heb jij tijd om het over het ouderschapsplan te hebben?")*
"Waar wil je het over hebben?"

**09:12 — Walter** *(reply op: "Waar wil je het over hebben?")*
"Over de afspraken die er in gemaakt zijn."
```
