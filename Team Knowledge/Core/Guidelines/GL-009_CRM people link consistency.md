---
id: GL-009
title: CRM people link consistency
version: 1.0
---

# GL-009 — CRM People Link Consistency

## Rule

When any agent creates or updates a PKM entity that involves a person from the CRM, that agent must update the `## Related to` section in that person's CRM file.

This rule applies to every agent, without exception.

## What counts as "involves a person"

- A project, goal, or topic that explicitly names or directly relates to a person
- A journal entry that mentions a person
- A document, WhatsApp conversation, or deliverable related to a person
- Any interaction, event, or context where a specific person plays a role

## How to update

1. Open `PKM/CRM/People/Achternaam, Voornaam.md`
2. Find the `## Related to` section
3. Add the wikilink under the correct category: **Goals**, **Projects**, **Topics**, **Key Elements**, **Journal**, or **WhatsApp**
4. Use wikilink format: `[[Entity name]]`
5. If no CRM file exists for the person yet: create a stub first, then add the link

## Standard Related to structure

```markdown
## Related to

**Goals**
- [[G-...]]

**Projects**
- [[P-...]]

**Key Elements**
- [[KE-...]]

**Topics**
- [[T-...]]

**Ideas**
- [[I-...]]

**Journal**
- [[YYYYMMDD_onderwerp]]

**WhatsApp**
- [[CRM/WhatsApp/voornaam-achternaam]]

**People**
- [[Achternaam, Voornaam]]
```

Always include all categories, even when empty, for consistency.

## Which agents apply this rule

All agents that create or update PKM content. Primary responsibility:

| Agent | Trigger |
|---|---|
| Penn | Every journal entry that mentions a person |
| Sienna | New personal project, goal, or document involving a person |
| Marcus | New project (any domain) involving a person |
| Larry | When orchestrating work that results in a new PKM entity linked to a person |

## Enforcement

Larry checks CRM link consistency at session close as part of his Librarian duty.
