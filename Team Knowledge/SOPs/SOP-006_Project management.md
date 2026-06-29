# SOP-006 — Project Management

**Geldig voor:** gehele myPKA vault
**Laatste update:** 2026-05-10

---

## Principe

Een project is een afgebakende reeks taken met een duidelijk eindpunt, gekoppeld aan één Goal. Een project is klaar of niet klaar — het heeft een duidelijk eindpunt.

---

## Hiërarchie

```
Goal
└── Project
    └── Taken
```

Een project zonder Goal bestaat niet. Een project zonder taken is een lege huls.

---

## Naamgeving

Format: `P-Projectnaam` — Title Case, geen spaties rond het koppelteken.

Voorbeelden:
- `P-Scheiding`
- `P-Geldstroom Regie`
- `P-Broederweekend 2026`

Raadpleeg altijd [[GL-001_File naming conventions]] voor aanmaken of hernoemen.

---

## Projectstructuur

Elk project bestaat uit:

1. **Map op disk** — `PKM/My Life/Projects/P-Projectnaam/`
2. **project.md** — in de projectmap, bevat doel, eindpunt, status en notities
3. **Todoist project** — taken onder hetzelfde naam `P-Projectnaam`

### Minimale project.md inhoud

```markdown
# P-Projectnaam

**Goal:** [[G-Goalnaam]]
**Status:** actief / afgerond / gepauzeerd
**Do Date:** YYYY-MM-DD (verwachte afrondingsdatum)

## Doel

Wat wil je bereiken met dit project?

## Eindpunt (wanneer is dit project klaar?)

- Concrete checkpoints

## Notities
```

---

## Lifecycle

### Aanmaken

1. Lees [[GL-001_File naming conventions]] voor de juiste naamgeving
2. Maak map aan: `PKM/My Life/Projects/P-Projectnaam/`
3. Maak `project.md` aan in de map
4. Maak Todoist project aan onder `👤 PROJECTS` met naam `P-Projectnaam`
5. Registreer in `Team Knowledge/Core/project-index.md`

### Actief

- Taken worden aangemaakt in het Todoist project
- Do Dates worden gezet naarmate taken ingepland worden
- project.md wordt bijgehouden als status verandert

### Afsluiten

1. Sluit alle openstaande taken in Todoist
2. Archiveer het Todoist project
3. Verplaats de projectmap naar `PKM/My Life/Projects/Archive/`
4. Markeer als afgerond in `project-index.md`

---

## Huidige tooling

### Op disk

Projectmappen staan in `PKM/My Life/Projects/`. Elk project heeft minimaal een `project.md`.

### Todoist

Todoist projecten staan genest onder `👤 PROJECTS` (id: `6c8XR7HXhgMWMWwj`). Naam volgt exact de mapnaam.

### Project-index

Alle actieve en gearchiveerde projecten worden bijgehouden in `Team Knowledge/Core/project-index.md`.
