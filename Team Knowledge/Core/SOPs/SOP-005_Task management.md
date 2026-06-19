# SOP-005 — Task Management

**Geldig voor:** gehele myPKA vault
**Laatste update:** 2026-05-10

---

## Principe

Een taak is een concrete, uitvoerbare actie met één eigenaar. Taken zijn altijd onderdeel van een Project, dat onderdeel is van een Goal. Losse taken zonder context bestaan niet — ze horen ergens.

---

## Hiërarchie

```
Goal
└── Project
    └── Taak
```

- **Goal** — de gewenste uitkomst op kwartaalniveau
- **Project** — een reeks samenhangende taken die naar dat Goal leiden
- **Taak** — één concrete actie, uitvoerbaar door één persoon in één sessie

---

## Highlight-check

Vóór elke aanmaak of toewijzing van een Highlight:
1. Check of er al een taak met label `highlight` en due date vandaag bestaat
2. Zo ja → vraag de owner welke de echte Highlight is; verwijder het `highlight` label bij de andere
3. Zo nee → ga verder met aanmaken

Eén Highlight per dag — altijd.

---

## Taaktypen

Elke taak is bij aanmaak een **Task** of een **Speedy** (per ICOR Module Task Management):

| Type | Doorlooptijd | Todoist label |
|---|---|---|
| **Task** | 15 min – 3 uur | — |
| **Speedy** | < 15 min | `speedy` |

Bij elke nieuwe taak schat de AI het type in en toont dit als voorstel. De owner valideert. Bij Speedy wordt het label `speedy` toegevoegd in Todoist.

---

## Taakeisen

Een geldige taak voldoet aan:

1. **Actiegericht** — begint met een werkwoord (bel, koop, schrijf, stuur)
2. **Concreet** — duidelijk wanneer hij klaar is
3. **Één eigenaar** — of de owner, of één teamlid
4. **Correct geplaatst** — onder het juiste Project

---

## Planning via Do Date

Taken worden gepland via een **Do Date**: de dag waarop je van plan bent de taak uit te voeren. Geen urgentie-prioriteit, geen labelsysteem voor haast. De hiërarchie (Goal → Project → Taak) bepaalt de prioriteit impliciet.

- Do Date = planningsinstrument, geen deadline
- Geen Do Date = taak staat in de backlog van het project
- Overdue taken worden meegenomen in de dagelijkse planning

---

## Highlight van de dag

Elke dag wordt één taak aangewezen als Highlight: de taak die vandaag het meest bijdraagt aan een actief Goal. De Highlight wordt gekozen tijdens de Morning Routine.

Regels:
- Eén Highlight per dag
- Gekozen uit taken van het Goal dat je die dag beweegt
- Krijgt label `highlight` en Do Date vandaag (als die er nog niet was)

---

## Twee taaksystemen

### 1. Persoonlijk taaksysteem (owner-facing)

Taken die de owner zelf uitvoert. Zichtbaar en beheerbaar door de owner.

Domeinen:
- Persoonlijk leven → eigen project onder Goals
- Kamer E-commerce → business project

### 2. Team delegatiesysteem (AI-facing)

Interne taken voor het AI-team. De owner handelt hier niet op — dit is logistiek voor de specialists.

Opgeslagen in `team_tasks` tabel per domein-database. Niet zichtbaar in het persoonlijk taaksysteem.

---

## Werkwijze bij nieuwe taak

1. Bepaal het domein (persoonlijk / business / AI-team)
2. Koppel aan het juiste Project en Goal
3. Schrijf de taak actiegericht en concreet
4. Stel een Do Date in als de taak deze week of volgende week uitgevoerd wordt
5. Laat taken zonder Do Date in de projectbacklog staan

---

## Dagelijkse routines

De drie dagelijkse routines vormen de uitvoeringslaag van dit systeem. Elke routine is een aparte skill die de owner handmatig start.

| Routine | Skill | Moment |
|---|---|---|
| Morning Routine | `/start-morning-routine` | Start van de dag |
| Afternoon Routine | `/start-afternoon-routine` | Na de deep work sessie |
| End-of-the-Day Routine | `/start-end-of-the-day-routine` | Einde van de werkdag |

### Daily Planning

De Daily Planning (ICOR Workflow 3) is onderdeel van de End-of-Day Routine. Hij wordt uitgevoerd als Stap 3 via de skill `/start-daily-planning`.

Doel: in rust bepalen wat morgen gedaan wordt, zodat de dag georganiseerd begint.

Stappen:
1. Taken reviewen (backlog + actief)
2. Kiezen wat morgen haalbaar is (do-date zetten)
3. Highlight van morgen aanwijzen (label `highlight`) — wordt altijd als eerste uitgevoerd
4. **Goal-commitment check** — voor elk Goal zonder beweging de afgelopen 3 dagen: één concrete mini-actie benoemen en inplannen. Geen goal verlaat de planning zonder een committed actie of expliciete "wacht op extern."

---

## Huidige tooling

### Persoonlijk taaksysteem — Todoist

**Project routing:**

| Domein | Todoist Project | Project ID |
|---|---|---|
| Persoonlijk | 👤 PERSONAL | 6cFcm2MpmHvc2F3H |
| Kamer E-commerce | 💼 KAMER E-COMMERCE | 6fC99W283Jw2cjV2 |

**Weergaveregels:**
- Kolom heet altijd **Do Date** (nooit "Due Date")
- Nooit taak-ID of prioriteit tonen
- Filter voor vandaag: `(today | overdue) & #<project>`
- Geen Do Date → toon `—`

**Aanmaakrege ls:**
- Altijd in het Nederlands
- Altijd beginnen met een werkwoord in de gebiedende wijs (Bel, Koop, Schrijf, Stuur)
- Kort en actiegericht
- Domein bepaalt het project; bij twijfel vragen voor aanmaken

### Team delegatiesysteem — SQLite

Opgeslagen in `team_tasks` per domein-database:
- Persoonlijk: `PKM/personal.db`
- Kamer E-commerce: `Team Knowledge/Kamer E-commerce/kamer e-commerce.db`
- Geldstroom Regie: `Team Knowledge/Geldstroom Regie/geldstroom-regie.db`
