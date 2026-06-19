# KE-MYICOR

> Persoonlijke implementatie van het ICOR Framework. Hoe ICOR werkt in mijn leven en systeem.
> Lesdata (bronmateriaal Tom Solid) → zie [[T-ICOR Framework]]

---

## Wat ICOR voor mij betekent

ICOR is het besturingssysteem van mijn leven. Het geeft structuur aan hoe informatie binnenkomt, hoe ik het verwerk, wat ik ermee doe en hoe ik het systeem scherp houd.

```
INPUT → CONTROL → OUTPUT → REFINE
```

Zonder ICOR: informatie stapelt op, acties verdwijnen, prioriteiten zijn vaag.
Met ICOR: alles heeft een plek, het team weet wat te doen, ik houd grip op wat telt.

---

## Mijn Tool Ecosysteem — 4 Kwadranten

| Kwadrant | Doel | Mijn Tool |
|---|---|---|
| **PKM** — Personal Knowledge Management | Persoonlijke kennis, journaling, CRM | myPKA vault (Claude Code) |
| **BKM** — Business Knowledge Management | Zakelijke kennis, processen, klantdata | myPKA Team Knowledge (SQLite) |
| **PPM** — Personal Process Management | Persoonlijke taken, agenda, gewoonten | Todoist (👤 PERSONAL) |
| **BPM** — Business Process Management | Zakelijke taken, workflows, operaties | Todoist (💼 KAMER E-COMMERCE / 💼 GELDSTROOM REGIE) + team_tasks DB |

---

## Mijn MY LIFE Structuur

### Key Elements (permanent, multi-jaar)

| KE | Domein |
|---|---|
| [[KE-Self]] | Wie ik ben, groei, gezondheid |
| [[KE-Finance]] | Financiën, inkomen, uitgaven |
| [[KE-Work]] | Werk, ondernemerschap |
| [[KE-Relationships]] | Familie, vrienden, netwerk |
| [[KE-Environment]] | Thuis, omgeving, mancave |
| [[KE-Experience]] | Avontuur, reizen, beleving |

### Current Projects (tijdelijk, start + einddatum)

Zie `PKM/My Life/Projects/` voor actuele projecten.
Beheerd via Todoist (`👤 PROJECTS`) en project-index.md.

### Topics (roterend per kwartaal, exploratie)

Zie `PKM/My Life/Topics/` voor actieve topics.
Promotie naar KE zodra er een meetbaar resultaat aan verbonden wordt.

### Habits (terugkerend, ondersteunt Goals)

Worden bijgehouden via Todoist daily labels en dagelijkse routines.

---

## Hoe ICOR werkt in mijn dagelijks systeem

### INPUT — Wat binnenkomt

Alles wat binnenkomt gaat eerst naar een Inbox:

| Inbox | Wat |
|---|---|
| `Team Inbox/Personal/` | Persoonlijke inputs, materialen, lesdata |
| `Team Inbox/Kamer E-commerce/` | Business inputs |
| `Team Inbox/Geldstroom Regie/` | Financiële inputs |
| Todoist Inbox | Losse acties en ideeën |

**Capturing Beast filters** bij elke input:
1. Raakt dit een Key Element?
2. Dient dit een actief Project?
3. Ondersteunt dit een actieve Habit?
4. Verbindt dit met een Topic dat ik exploreer?

Als geen van de vier: loslaten.

---

### CONTROL — Verwerken en organiseren

Verwerking verloopt via het team. Elk domein heeft een specialist:

| Domein | Specialist | Verwerkt naar |
|---|---|---|
| Persoonlijk | Sienna / Penn | `PKM/` + `personal.db` |
| Kamer E-commerce | Sasha / Vera | `Team Knowledge/Kamer E-commerce/` |
| Geldstroom Regie | Finn | `Team Knowledge/Geldstroom Regie/` |
| Kennis & infrastructuur | Larry / Pax / Nolan | `Team Knowledge/` |

SSOT-principe: elk stuk informatie leeft op één plek. Wikilinks verbinden de rest.

---

### OUTPUT — Wat ik produceer

Twee niveaus:

**Persoonlijk (PPM):**
- Todoist `👤 PERSONAL` — dagelijkse taken
- Todoist `👤 PROJECTS` — projecttaken per P-Naam project
- Daily Routines: Morning · Afternoon · End-of-Day

**Team (BPM):**
- Todoist `💼 KAMER E-COMMERCE` + `💼 GELDSTROOM REGIE` — business taken
- `team_tasks` in SQLite DB's — interne teambriefings en delegaties
- Deliverables: `Deliverables/YYYYMMDD_Domain_beschrijving/`

**Output Formula:**
```
TOP-DOWN: Goals → Projects / Workstreams / Operations → Tasks
```

**PEA dagelijks:**
- **Plan** — Weekly Planning (zondag/maandag) + Daily Planning (ochtend)
- **Execute** — Deep Work eerst, dan routines, dan shallow werk
- **Align** — close-session check: doe ik wat ik zou moeten doen?

---

### REFINE — Systeem scherp houden

| Moment | Actie |
|---|---|
| Dagelijks | `/close-session` — log, sweep, SOP-check |
| Wekelijks | Weekly Review (<30 min) + Weekly Planning |
| Per kwartaal | Goals reviewen, Topics roteren, KE-promoties beoordelen |
| Per sessie | Larry als Librarian — SSOT-check, wikilinks, orphaned files |

---

## Mijn Execution Beast

```
CREATE (Sienna / Larry delegeert)
  Goals → Projects → Tasks

PLAN
  Team Knowledge / Todoist
  → Weekly Planning: this week / next week

EXECUTE
  Daily Planning → Deep Work → Routines
  → Energy Level / Urgent / Speedy / Unexpected

ALIGN
  close-session: doe ik wat ik zou moeten doen?
```

---

## Idea Incubator (persoonlijk)

Ideeën komen binnen via Inbox of Todoist.

```
CAPTURE → Team Inbox of Todoist
EVALUATE → Capturing Beast (4 filters)
PLAN → Todoist project of team_tasks delegatie
EXECUTE → Execution Beast
```

---

## Team Communication

Mijn team communiceert asynchroon via Claude Code sessies.

| Kanaal | Gebruik |
|---|---|
| Claude Code `/start-session` | Dag openen, inbox checken, delegeren |
| Claude Code `/close-session` | Dag sluiten, loggen, sweepen |
| `team_tasks` DB | Interne delegaties en statusupdates |
| Session logs | SSOT voor wat er beslist en gedaan is |

---

## Workstream → Workflow → Process

| Niveau | Definitie | Voorbeeld |
|---|---|---|
| **Workstream** | Terugkerend operationeel gebied | "Kamer E-commerce Operaties" |
| **Workflow** | Reeks stappen binnen Workstream | "Nieuwe product lanceren" |
| **Process** | Individuele taak binnen Workflow | "Productpagina schrijven" |

---

*Laatste update: 2026-05-10*

---

## Resources

**Articles**
-

**Audios**
-

**Books**
-

**Emails**
-

**Files**
-

**Notes**
-

**Recipes**
-

**Videos**
-

**Websites**
-

---

