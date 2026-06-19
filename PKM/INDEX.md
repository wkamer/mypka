# PKM — Master Index

This is the owner's personal knowledge. The team's operations side lives in `Team Knowledge/`.

## Sections

- **My Life** — the five life concepts: Topics, Habits, Goals, Projects, Key Elements
- **Documents** — passports, contracts, identity files. Markdown stubs that point at where the real file lives
- **CRM** — People and Organizations. Cross-linked into Journal entries via `[[wikilinks]]`
- **Images** — single shared image bucket, nested by `YYYY/MM/`. Images live here, never duplicated elsewhere
- **Journal** — daily entries, one file per day, nested by `YYYY/MM/`. The inbox of the vault

## How the wiki connects

- The Journal is where new information lands first
- **Penn** cross-links Journal entries to People, Organizations, Topics, Projects, and Goals via `[[wikilinks]]`
- Concept folders (Topics, Habits, Goals, Projects, Key Elements, People, Organizations, Documents) stay flat — one file per concept
- Date-driven folders (Journal, Images) nest by `YYYY/MM/`

## SSOT rule

If the same fact about a person, project, or topic appears in two places, the file in the relevant concept folder is the source of truth. The Journal entry references it via `[[wikilinks]]`. No duplication.

## How the team writes here

- **Penn** writes Journal entries, saves images, and creates stubs in CRM and My Life as needed
- **Sienna** reads and updates Personal domain content on owner request
- **Pax** flags new people, organizations, or topics surfaced during research, but does not write to PKM directly
- **Larry** does the Librarian pass at session close: broken links, orphan files, missing index entries
- The owner owns final content — the team handles capture and connective tissue

## Database

`PKM/personal.db` — tables: `journal`, `session_logs`, `team_tasks`, `agent_learnings`
