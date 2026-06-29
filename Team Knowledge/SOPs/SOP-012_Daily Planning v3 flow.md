# SOP-012 — Daily Planning v3 flow

## Kernprincipes

- **Top-down altijd** — goals bepalen de agenda, niet de takenlijst
- **One question per step** — each step ends with a question; "nee" en "geen" zijn altijd geldige antwoorden
- **Nooit auto-chaining** — each step waits for owner response before the next starts
- **Consistente flow** — de volgorde verandert nooit
- **Commitment per domein** — PPM volledig afsluiten (Step 4) voor BPM start (Step 5)

---

## Flow

De planning doorloopt acht stappen — PPM (stappen 1–4) gevolgd door BPM (stappen 5–8).

**PPM** — persoonlijk domein (👤 projecten, persoonlijke goals)
Step 1 → Step 2 → Step 3 → Step 4

**BPM** — business domein (💼 projecten, business goals)
Step 5 → Step 6 → Step 7 → Step 8

BPM start pas na afsluiting van Step 4.

---

## Steps

### Step 1 — Review (PPM)

**Doel:** bewuste beslissing nemen over alle PPM-taken die beoordeeld moeten worden.

**Data:** twee API-calls aan het begin van Step 1. Resultaten cachen — hergebruiken bij Step 5.
1. Completed tasks vandaag — bouw een set van afgeronde task-ID's
2. Alle open taken — filter daarna: een taak die in de completed-set zit, verschijnt alleen in Planned Today - Completed, niet in Planned Today - Open

Een taak staat altijd in precies één sectie.

**Timezone:** gebruik `since=gisteren 22:00 UTC` (= lokale middernacht Nederland, UTC+2) — niet `since=vandaag 00:00 UTC`. Anders vallen taken afgesloten tussen 00:00–02:00 lokale tijd buiten de scope.

**Scope PPM:** Inbox + 👤-projecten.
**Filter weg:** resource-taken die beginnen met `*`, `📂`, `🎯`, `📅`, `♻️`.

**Altijd drie secties tonen — ook als leeg. Elke sectie bevat drie vaste tiers:**

Per sectie: **Highlight of the Day** / **Support Tasks** / **Buffer Tasks**
Lege tier binnen een sectie → tiernaam op één regel, *(none)* op de volgende regel
Alle drie secties volledig leeg → meld dit, ga direct naar Step 2.

**Tabelopmaak per tier:**

| # | Taak | Project |
|---|---|---|

- Geen Type-kolom
- Speedy-taken: ⚡ vóór de taaknaam in de Taak-kolom
- Highlight of the Day: ⭐ vóór de tier-titel én vóór de taaknaam in de tabel
- Doorlopende nummering over alle tiers en secties

**Planned - Overdue** — due date in het verleden, nog open
**Planned Today - Open** — due = today, nog open
**Planned Today - Completed** — due = today, afgerond

**Volgorde van weergave:**

1. Sectie Planned - Overdue (tiers + tabellen)
   → Direct onder de sectie, alleen als de sectie taken bevat:
   Actions: **Backlog / Reschedule / Complete / Delete**

2. Sectie Planned Today - Open (tiers + tabellen)
   → Direct onder de sectie, alleen als de sectie taken bevat:
   Actions: **Keep / Backlog / Reschedule / Postpone / Complete / Delete**

3. Sectie Planned Today - Completed (tiers + tabellen — geen actions)

4. Eenmalig onderaan, na alle drie secties:
   > "What's your action for each task?"

"Continue" is altijd een geldig antwoord — geen wijzigingen, ga direct naar de volgende stap.

**Lege stap:** alle drie secties leeg → meld dit, ga direct naar Step 2.

**Verwerking:**

| Actie | Effect |
|---|---|
| Keep | Geen wijziging |
| Backlog | Due date verwijderen + planning labels verwijderen |
| Reschedule | Nieuwe due date instellen (today of toekomst) |
| Postpone | Due date verschuiven naar toekomst (niet today) |
| Complete | Taak afsluiten |
| Delete | Taak verwijderen |

---

### Step 2 — Goals / Project Alignment (PPM)

**Doel:** volledig overzicht van alle actieve goals en projecten; bewuste keuze welke goal tomorrow aandacht krijgt.

**Scope PPM:** persoonlijke goals + alle actieve 👤 projecten.
**Data:** `project.md` bestanden lokaal lezen — geen API-call. Completed tasks: lazy, alleen voor goals zonder `Waiting on:`.

**Altijd drie secties tonen:**

---

**Goals**

| # | Goal | Project | Status | Deadline | Description |
|---|---|---|---|---|---|

**Projects - Event-driven**

| # | Project | Event | Deadline | Description |
|---|---|---|---|---|

**Projects - Other**

| # | Project | Description |
|---|---|---|

---

**Project type — SSOT is project.md, nooit Todoist:**
- `**Type:** Goal-driven` — gekoppeld aan een goal; vereist `**Goal:**` veld
- `**Type:** Event-driven` — gekoppeld aan een specifieke datum; vereist `**Event:**` veld (formaat: `[omschrijving] — [datum]`)
- Geen Type of onbekend type → toon in Projects - Other als ⚠️ en help de owner classificeren vóór je verdergaat
- Alleen Goal-driven en Event-driven zijn geldige types — Larry helpt altijd om elk project in een van deze twee te plaatsen

**Plaatsing per type:**
- Goal-driven → verschijnt in Goals-sectie naast het gekoppelde goal
- Event-driven → verschijnt in Projects - Event-driven
- Onbekend / ontbrekend Type → verschijnt in Projects - Other als ⚠️

**Deadline-kolom:** datum + resterende dagen tussen haakjes + urgentie-indicator.
- ≤ 14 dagen: `27 mei (3d) 🔥`
- ≤ 45 dagen: `17 jun (24d) ⚠️`
- \> 45 dagen of geen deadline: datum zonder indicator, of —

**Description-kolom Goals:** waarde van `Waiting on:` voor ⏳ goals. Voor overige goals —.

**Sorteervolgorde — primair op deadline, secundair op status:**
1. Goals/projecten met deadline → nauwste deadline eerst (ongeacht status)
2. Goals/projecten zonder deadline → status-volgorde: 🔴 → 🟡 → 🟢 → ⏳

**Status-classificatie goals:**
- ⏳ Waiting — `Waiting on:` is gevuld
- 🔴 Stagnant — geen completed tasks afgelopen 3 dagen, `Waiting on:` leeg
- 🟡 Active — completed tasks aanwezig, deadline ≤ 14 dagen of geen deadline
- 🟢 On track — completed tasks aanwezig, deadline > 14 dagen

Bij 🔴 Stagnant goals: vraag eerst naar blocker voor de standaardvraag.

**Event-driven projecten — verstreken events:**
Als de event-datum in het verleden ligt: markeer als *(verstreken)* en vraag de owner of het project gearchiveerd moet worden.

**"Continue" is altijd geldig** — geen wijzigingen, ga direct naar Step 3.

**Vaste vraag:**
> "Which goal / project gets movement?"

**Verwerking:**
- Goal met beweging → meenemen als prioriteit in Step 3
- Blocker opgegeven → update `Waiting on:` in goal.md
- Project zonder Type → classificeer eerst, dan verder
- "Geen" → ga door naar Step 3

---

### Step 3 — Plan (PPM)

**Doel:** actieve keuzes maken voor tomorrow — Highlight, Support, Buffer en beschikbaar aanbod.

**Data:** één API-call voor alle open taken. Resultaat cachen — hergebruiken in Step 4 en Step 7.

**Altijd vier blokken tonen:**

| Blok | Label | Max | Type | Do Date |
|---|---|---|---|---|
| ⭐ Highlight of the Day | `highlight` | 1 | Task | — |
| Support Tasks | `support` | 3 | Task of Speedy | — |
| Buffer Tasks | — | onbeperkt | Task of Speedy | alleen due = today |
| Available to Plan | — | onbeperkt | Task of Speedy | altijd tonen |

**Capaciteitsindicator — achter elke sectietitel met max:**
- `⭐ Highlight of the Day (X/1)` — X = aantal taken met `highlight` label
- `Support Tasks (X/3)` — X = aantal taken met `support` label
- Buffer Tasks en Available to Plan: geen indicator

**Overschrijding (X > max) → toon ❗:**
- Voorbeeld: `Support Tasks (4/3) ❗`
- Meld: "N te veel — demoteer [N] taken voor je verdergaat."
- Pas verder gaan als alle indicators ≤ max.

**Promote / Demote — altijd één level:**

Hiërarchie (top → bottom):
1. ⭐ Highlight of the Day — ceiling, kan niet verder worden gepromoot
2. Support Tasks
3. Buffer Tasks
4. Available to Plan — buiten de planning; kan niet verder worden gedemoteerd

| Actie | Van | Naar | Effect |
|---|---|---|---|
| Promote | Available to Plan | Buffer Task | due = today instellen |
| Promote | Buffer Task | Support Task | `support` label + due = target |
| Promote | Support Task | Highlight of the Day | `highlight` label + due = target; verwijder vorige highlight eerst |
| Promote | Highlight of the Day | ❌ | niet mogelijk — ceiling |
| Demote | Highlight of the Day | Support Task | `highlight` → `support` label |
| Demote | Support Task | Buffer Task | `support` label verwijderen; due = today behouden |
| Demote | Buffer Task | Available to Plan | due date verwijderen |
| Demote | Available to Plan | ❌ | niet mogelijk — buiten de planning |

**Buffer Tasks** — uitsluitend taken met due = today die nog niet in Highlight of Support zitten. Dit zijn taken die al gepland staan voor vandaag maar nog geen vaste positie hebben.

**Available to Plan** — alle overige open taken (geen due date of toekomstige due date). Toekomstige taken kunnen eerder opgepakt worden. Do Date kolom altijd tonen (`—` als geen due date).

**Type-kolom in Step 3 tabellen:**
- label `speedy` → Type = `Speedy` → wordt opgepakt in Shallow Work sessie
- geen `speedy` label → Type = `Task` → wordt opgepakt in Deep Work sessie

**Available to Plan filter — goal-status gedreven:**
Available to Plan toont uitsluitend taken van projecten die gekoppeld zijn aan een 🔴 Stagnant of 🟡 Active goal (status bepaald in Step 2).
⏳ Waiting goals → taken worden niet getoond (goal is geblokkeerd).
🟢 On track goals → taken worden niet getoond (geen urgentie).
Uitzondering: losse taken (geen goal-koppeling) en event-driven projecttaken altijd tonen.

**Volledig overzicht eerst**
Toon altijd alle vier blokken tegelijk vóór enige vraag. Nooit een vraag stellen voor het overzicht compleet is.

**Als er geen Highlight is:** stel één taak voor vanuit het hoogste-prioriteit beschikbare goal — voeg deze toe als `highlight` + due = target. Daarna toon het volledige overzicht.

**Actions onderaan het overzicht:**
> **Actions: Promote / Demote / Commit**

- `Promote [#]` — promoot taak één level omhoog
- `Demote [#]` — demoteer taak één level omlaag
- `Commit` — plan accepteren, door naar Step 4

STOP. Wacht op antwoord.

**Verwerking per actie:**

| Actie | Van → Naar | Effect in Todoist |
|---|---|---|
| Promote [#] | Available to Plan → Buffer | due = today |
| Promote [#] | Buffer → Support | `support` label + due = target |
| Promote [#] | Support → Highlight of the Day | `highlight` label + due = target; verwijder vorige highlight label eerst |
| Demote [#] | Highlight of the Day → Support | `highlight` → `support` label |
| Demote [#] | Support → Buffer | `support` label verwijderen; due = today behouden |
| Commit | — | Plan bevestigd, ga naar Step 4 |

Na elke Promote of Demote: overzicht opnieuw tonen met bijgewerkte capaciteitsindicatoren.

---

### Step 4 — Commitment (PPM)

**Doel:** PPM-plan bevestigen en PPM-run afsluiten.

**Wat wordt getoond — eindplan PPM:**

⭐ Highlight of the Day
| Taak | Project | Goal | Type |
|---|---|---|---|

Support Tasks
| # | Taak | Project | Goal | Type |
|---|---|---|---|---|

Buffer Tasks (When there is time)
| # | Taak | Project | Goal | Type |
|---|---|---|---|---|

**Vaste vraag:**
> "Do you want to change anything?"

**Verwerking:**
- Aanpassing gewenst → terug naar Step 3 PPM
- Akkoord → start Step 5 (BPM)

---

### Step 5 — Review (BPM)

Zelfde structuur als Step 1. Domein: 💼-projecten (Kamer E-commerce + Geldstroom Regie).

**Scope BPM:** Inbox + 💼-projecten.

**Data:** hergebruik gecachte data van Step 1 — geen nieuwe API-call. Filter nu voor 💼-projecten.

---

### Step 6 — Goals / Project Alignment (BPM)

Zelfde structuur als Step 2. Scope: business goals (Kamer E-commerce + Geldstroom Regie).

---

### Step 7 — Plan (BPM)

Zelfde structuur als Step 3. Domein: 💼-projecten.

**Data:** hergebruik gecachte data van Step 3 — geen nieuwe API-call. Filter nu voor 💼-projecten.

---

### Step 8 — Commitment (BPM)

**Doel:** BPM-plan bevestigen. Afsluiting van de volledige planning.

**Wat wordt getoond — gecombineerd eindplan PPM + BPM:**

**PPM**
⭐ Highlight of the Day | Support Tasks | Buffer Tasks (When there is time)

**BPM**
⭐ Highlight of the Day | Support Tasks | Buffer Tasks (When there is time)

**Vaste vraag:**
> "Do you want to change anything?"

**Verwerking:**
- Aanpassing gewenst → terug naar Step 7 BPM
- Akkoord → afsluiting

**Afsluiting:**
> "Plan is set. Tomorrow you start with ⭐ [PPM Highlight]."

---

## Data-ophaalstrategie

| Step | Data | Moment |
|---|---|---|
| Step 1 | Alle taken (filter client-side op due ≤ today, PPM) | Begin Step 1 — één API-call, cache voor Step 5 |
| Step 2 | Goal-bestanden (lokaal) | Begin Step 2 — geen API |
| Step 2 | Completed tasks per goal | Lazy — alleen voor goals zonder `Waiting on:` |
| Step 3 | Alle open taken | Begin Step 3 — één API-call, cache voor Step 4 + Step 7 |
| Step 5 | Taken met due ≤ today (BPM) | Hergebruik cache Step 1 — geen nieuwe API-call |
| Step 7 | Alle open taken (BPM) | Hergebruik cache Step 3 — geen nieuwe API-call |

Nooit alles vooraf ophalen. Nooit twee keer dezelfde data ophalen.

---

## Gedragsregels

- **Drie secties altijd** — Review toont altijd Planned - Overdue / Planned Today - Open / Planned Today - Completed, ook als leeg
- **Drie tiers per sectie** — elke sectie toont altijd Highlight of the Day / Support Tasks / Buffer Tasks
- **Lege tier** → tiernaam gevolgd door *(none)*
- **Lege stap** (alle secties volledig leeg) → meld dit, direct door naar volgende stap
- **Geen Type-kolom in Review** — speedy-taken krijgen ⚡ vóór de taaknaam
- **Actions onder de sectie** — direct onder de sectie (niet per tier), alleen bij Overdue en Today - Open, alleen als de sectie taken bevat
- **Tabellen altijd** — nooit bullet lists voor taken of goals
- **Twee Must-Do's per dag** — één PPM, één BPM
- **Must-Do = Deep Work** — nooit ⚡ speedy voorstellen als Must-Do
- **Speedy = ⚡** — < 15 min, bundelen als Shallow Work batch
- **Label discipline** — `highlight` op Must-Do, `support` op Support Tasks
- **Promotie naar Support** — label toevoegen + due = tomorrow
- **Demotie naar Buffer** — label verwijderen + due date verwijderen
- **Losse taken horen erbij** — taken zonder goal-koppeling altijd tonen, na goal-taken
- **Blocker vastleggen** — stilstand zonder reden → schrijf naar `Waiting on:` in goal.md
- **AI faciliteert, owner beslist** — stel voor, nooit opleggen
