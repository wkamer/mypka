# Quinn gate refactor: whitelist vervangen door evidence-based twee-vragengate

**Date:** 2026-06-29
**Agent:** Larry
**Domain:** Team
**DB id:** 266

## What happened

Owner vroeg naar de staat van de development gates en hoe de snelle feature-ontwikkeling landt. Discussie leidde tot de vraag of Quinn (UX/interaction designer) overhead is en Devon het werk kan absorberen.

Iris governance review adviseerde Option B: Quinn on-demand met een structurele whitelist (accordion, multi-step flows, async state, modals, form validation chains) in plaats van een subjectieve trigger. CLAUDE.md en Quinn AGENT.md werden bijgewerkt naar die whitelist.

Owner signaleerde dat de whitelist op aannames gebaseerd voelde, niet op hoe echte development teams werken. Pax werd gebrieft voor primaire-bron onderzoek.

Pax vond op basis van Lighthouse London, NN/G, Jeff Gothelf en Smashing Magazine dat echte teams een twee-vragengate gebruiken: (1) Novelty — staat het patroon gedocumenteerd in het design system? (2) Risk — is het een high-stakes user flow? Geen team gebruikt een componentlijst als trigger.

CLAUDE.md en Quinn AGENT.md zijn opnieuw bijgewerkt naar de evidence-based gate. Huidige staat: geen pattern-level design system beschikbaar, dus Question 1 defaultt naar Yes totdat het design system op patroonniveau bestaat.

## Decisions

- Quinn gate vervangen door Novelty+Risk twee-vragengate (evidence-based, niet aanname-gebaseerd)
- Whitelist afgewezen: gebaseerd op één incident (Email Management Slice 3), niet op hoe teams het in de praktijk doen
- Quinn scope uitgebreid met interaction contracts en edge-state behavior (niet alleen visueel UX)
- Huidige default: Question 1 = Yes totdat pattern-level design system bestaat

## Actions taken

- CLAUDE.md bijgewerkt (twee keer): eerst whitelist, daarna twee-vragengate
- Quinn AGENT.md bijgewerkt (twee keer): activatieregel + scope uitbreiding
- Twee commits + pushes: `9480372` (whitelist) en `45740b9` (twee-vragengate)

## Open items

- Quinn Part 2 design review email management — nog niet gestart
- Dashboard default password (admin/admin) — nog niet gewijzigd
- Geen pattern-level design system — Question 1 defaultt naar Yes; overwegen of dit een project wordt
