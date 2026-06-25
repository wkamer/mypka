# Guidelines Index — Core

| Nr | Bestand | Omschrijving |
|----|---------|--------------|
| GL-001 | [[GL-001_File naming conventions]] | Naamgevingsconventies voor bestanden en mappen |
| GL-002 | [[GL-002_Frontmatter conventions]] | YAML frontmatter schema's per entiteitstype + standaard resource types |
| GL-003 | [[GL-003_Email setup]] | Email setup via Gmail API (send_email.py) |
| GL-004 | [[GL-004_Canonical paths]] | Alle canonical paden in de vault — SSOT voor agents en skills |
| GL-005 | [[GL-005_AI Engineering Operating System]] | Engineering standaard voor het volledige AI team — bewaakt door Larry |
| GL-006 | [[GL-006_Notification Format]] | Universeel notification format: Source · Entity · Status · Message |
| GL-007 | [[GL-007_Integration naming convention]] | Naamgevingsconventie voor integrations: mapstructuur, connection.py, handler naming, verboden namen, security |
| GL-008 | [[GL-008_WhatsApp conversatie borging]] | Standaard werkwijze voor opslaan van WhatsApp-conversaties: formaat, aanhalingstekens, reply-quotes, tijdstempels |
| GL-009 | [[GL-009_CRM people link consistency]] | Elke agent die een PKM-entiteit aanmaakt die een CRM-persoon betreft, werkt de ## Related to sectie bij in dat persoons CRM-bestand |
| GL-010 | [[GL-010_Session logs purpose and discipline]] | Waarom session-logs het teamgeheugen zijn en hoe de discipline werkt |
| GL-011 | [[GL-011_Project documentation conventions]] | Verplichte conventies voor project.md: tijdlijn-format, mail-links, secties — eigenaar Marcus |
| GL-012 | [[GL-012_ChatGPT prompt ICOR module-verwerking]] | ChatGPT prompt voor ICOR module-verwerking (hernoemd van GL-002, 2026-06-03) |
| GL-014 | [[GL-014_AI Team Governance]] | Authoritative governance voor het myPKA AI-team: approval-gates, escalation, changelog-protocol, secret handling, SSOT-hiërarchie |
| GL-020 | [[GL-020_Intent Classification Taxonomy]] | Six intent categories (CAT-1 to CAT-6), routing table, approval gates, Learning Value Filter (three levels), Iris review threshold, clarification protocol, and misrouting risks |
| GL-021 | [[GL-021_Owner Interaction Rule and Write Authorization Boundary]] | Owner answers only yes/no/correction; every write requires explicit Owner confirmation; Iris review vs Owner authorization distinction; pre-authorized CAT-1 writes; /close-session batched confirmation protocol |
| GL-023 | [[GL-023_Pre-Build Protocol]] | Mandatory five-step pre-build sequence for all specialists: Interview, Spec, Verify plan, Tool check, Murphy scan — no file written until all five complete |

## Archived Guidelines

| Nr | Bestand | Reden archivering |
|----|---------|-------------------|
| GL-013 | GL-013_Memory Core Architecture | Replaced by current memory system implementation in GL-004 and team-knowledge.db schema |
| GL-015 | GL-015_Memory Domain Routing Protocol | Replaced by AGENT.md routing sections and GL-004 canonical paths |
| GL-016 | GL-016_Review Gate for Governance-Relevant Deliverables | Principle layer for SOP-016; consolidated into SOP-015 (2026-06-18) |
| GL-017 | GL-017_Deliverable Lifecycle Knowledge Processing and Archiving | Principle layer for SOP-017; consolidated into SOP-015 (2026-06-18) |
| GL-018 | GL-018_Idea Routing and Implementation Governance Principles | Principle layer for SOP-018; consolidated into SOP-015 (2026-06-18) |
| GL-019 | GL-019_Governance Gatekeeper Principles | Principle layer for SOP-019; consolidated into SOP-015 (2026-06-18) |
| GL-020 | GL-020_Intent Classification Taxonomy | Superseded by GL-021 and GL-014 governance model; kept in archive for reference |
| GL-022 | GL-022_Learning Candidate Lifecycle | Replaced by learning_candidates table in team-knowledge.db and Task Discipline section in AGENT.md files |
