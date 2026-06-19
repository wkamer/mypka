# GL-002 — Frontmatter Conventions

**Applies to:** all entity files in the myPKA vault
**Last updated:** 2026-06-01

---

## Principle

Every entity file starts with YAML frontmatter. Frontmatter makes files machine-readable and queryable without a database. Free-form `**Field:** value` in the body is not acceptable for typed fields — use frontmatter.

---

## Required frontmatter per entity type

### Project

```yaml
---
title: ""
type: goal-driven | event-driven
status: active | on-hold | completed
domain: personal | kamer-ecommerce | geldstroom-regie
start_date: ""
end_date: ""
goal: ""
---
```

### Goal

```yaml
---
title: ""
status: active | completed | on-hold
key_element: ""
project: ""
deadline: ""
waiting_on: ""
---
```

### Person (CRM)

```yaml
---
name: ""
relationship: ""
last_contact: ""
email: ""
phone: ""
domain: personal | kamer-ecommerce | geldstroom-regie
---
```

### Organization (CRM)

```yaml
---
name: ""
type: ""
domain: personal | kamer-ecommerce | geldstroom-regie
website: ""
since: ""
---
```

### Topic

```yaml
---
title: ""
status: active | archived
domain: personal | kamer-ecommerce | geldstroom-regie
---
```

### Key Element

```yaml
---
title: ""
domain: personal | kamer-ecommerce | geldstroom-regie
---
```

### Habit

```yaml
---
title: ""
status: active | paused | archived
started: ""
---
```

### Session log

```yaml
---
title: ""
date: ""
agent: larry
topics: []
session_id: ""
domain: personal | kamer-ecommerce | geldstroom-regie | core
---
```

---

## Rules

- All frontmatter field names are lowercase with underscores
- All frontmatter values are in English
- Enum fields show all valid options separated by `|` — pick one value in the actual file
- Empty required fields use `""` — never omit the field
- New entity types get a frontmatter schema added to this document before the first file is created

---

## Standard Resource Types

Every entity that can hold external resources uses a `## Resources` section with these fixed types (in this order). Only include types that have content — omit empty types.

| Type | What goes here |
|---|---|
| Articles | Web articles, blog posts, online reads |
| Audios | Podcasts, audio recordings, voice memos |
| Books | Books, ebooks, long-form written works |
| Emails | Relevant emails by subject or sender |
| Files | Local files, PDFs, attachments |
| Notes | Internal notes, atomic notes from PKM |
| Recipes | Recipes (food, health, processes) |
| Videos | Individual video links (YouTube, Vimeo, etc.) |
| Websites | Channels, sites, tools, recurring web sources |

**Applies to:** Key Elements, Projects, Goals, Topics, Habits.

---

## Templates

All entity templates live in `Team Knowledge/Templates/`. Agents always start from the template — never create an entity file from scratch.

See: `[[Team Knowledge/Templates/INDEX.md]]`
