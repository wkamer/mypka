# B-026 Pre-existing Dutch System Content Cleanup Proposal v0.2

**Date:** 2026-06-03
**Prepared by:** Larry
**Status:** Concept — awaiting Owner's explicit approval
**Governance:** Fully compliant with GL-014 AI Team Governance v1.1 (§10 System File Language Rule)
**No changes executed**
**Changes vs v0.1:** All sections now contain full exact English replacement text. Nolan's Domain Knowledge fully translated. Sienna Owner's Growth Context decision applied (Option A). B-027 recommendation added. Execution Checklist added.

---

## 1. Executive Summary

Four AGENT.md files contain pre-existing Dutch system-file content that was out of scope for B-024. This proposal provides execution-ready exact English replacements for every affected section. The most substantial translation is Nolan's Domain Knowledge — seven subsections, fully translated below. All other replacements are smaller in scope. No functional meaning is altered in any translation.

---

## 2. Why this cleanup is needed

GL-014 §10 System File Language Rule states: "All system files must be written in English." The four inspected files contain Dutch headings, Dutch active instructions and Dutch code comments that constitute system-file content, not user-facing content.

---

## 3. Files inspected

| File | Pre-existing Dutch found |
|---|---|
| `Team/Sienna - The Personal Assistant/AGENT.md` | Collaboration section, Owner's Growth Context, UMC comments, Links text |
| `Team/Penn - The Journal Writer/AGENT.md` | Collaboration section, Dutch bullet content |
| `Team/Pax - The Research Specialist/AGENT.md` | Collaboration section, Hiring Research section, Knowledge Refresh section |
| `Team/Nolan - The HR Specialist/AGENT.md` | Collaboration section, Responsibilities bullet, Domain Knowledge (7 subsections), UMC comments |

---

## 4. Dutch system-file content found

| File | Section | Type |
|---|---|---|
| Sienna | `## Samenwerking` heading + body | Active system instruction |
| Sienna | `## Walter's Groeicontext` heading + body | Active system instruction (see §6) |
| Sienna | UMC Python comments | Active system instruction |
| Sienna | Links section (2 lines) | Active system instruction |
| Penn | `## Samenwerking` heading + body | Active system instruction |
| Pax | `## Samenwerking` heading + body | Active system instruction |
| Pax | `## Hiring Research (verplichte trigger)` heading + full body | Active system instruction |
| Pax | `## Kennisverversing (Knowledge Refresh)` heading + full body | Active system instruction |
| Nolan | `## Samenwerking` heading + body | Active system instruction |
| Nolan | Responsibilities bullet (1 line) | Active system instruction |
| Nolan | `## Domain Knowledge` — all 7 subsections | Active system instruction |
| Nolan | UMC Python comments | Active system instruction |

---

## 5. Full proposed replacements per file

---

### SIENNA — The Personal Assistant

#### `## Samenwerking` → `## Collaboration`

```markdown
## Collaboration

**Incoming** — Sienna receives from:
- **Larry**: Priority Gate trigger when Owner introduces a new initiative (all domains)
- **Larry**: personal domain delegations (inbox, projects, life admin)
- **Marcus**: objective signal that planned work is not being done → Sienna investigates the behavioral layer

**Outgoing** — Sienna signals to:
- **Larry**: Priority Gate confirmed (Owner is deliberate) → Larry routes to Marcus for ICOR classification
- **Larry**: business-relevant signals encountered in the personal domain
- **Penn**: all journalable content — personal narratives, reflections, insights — always, without asking permission

**Interrupt Trigger — Sienna speaks up when:**
- A new initiative is executed without a Priority Gate check (any domain)
- The Owner postpones or avoids the same theme twice without Sienna naming it
- A behavioral pattern is visible that connects to an active growth theme but has not been flagged
```

#### `## Walter's Groeicontext` → `## Owner's Growth Context` (see also §6)

```markdown
## Owner's Growth Context

Owner is in a deep personal growth journey (Miracle Roadmap); core themes are being seen, releasing control and visibility from authenticity. See `[[what-about-me]]` (Miracle Roadmap section) for the full profile including coaching signals.
```

#### UMC Python comments

| Current Dutch comment | Proposed English |
|---|---|
| `# laad de juiste context vóór actie` | `# load the right context before action` |
| `# Recente sessiestatus (Laag 8 — Summary)` | `# Recent session status (Layer 8 — Summary)` |
| `# Walter's voorkeuren en persoonlijke context (Laag 1 — Identity)` | `# Owner preferences and personal context (Layer 1 — Identity)` |
| `# Persoon opzoeken (Laag 2 — Entity)` | `# Look up person (Layer 2 — Entity)` |
| `# WhatsApp berichten (niet via bestandsontdekking)` | `# WhatsApp messages (not via file discovery)` |
| `# Persoonlijke update (Laag 1 — Identity of Laag 3 — Project)` | `# Personal update (Layer 1 — Identity or Layer 3 — Project)` |
| `content='Walter geeft aan dat hij ... prefereert bij ...'` | `content='Owner indicates preference for ... in context of ...'` |

#### Links section

| Current | Proposed |
|---|---|
| `Marcus (PM): verantwoordelijk voor taakplanning, time blocking en objectieve voortgang` | `Marcus (PM): responsible for task planning, time blocking and objective progress` |
| `Penn (Journal): ontvangt alle journaalwaardige content van Sienna` | `Penn (Journal): receives all journalable content from Sienna` |

---

### PENN — The Journal Writer

#### `## Samenwerking` → `## Collaboration`

```markdown
## Collaboration

**Incoming** — Penn receives from:
- **Sienna**: journalable content — personal narratives, reflections, sparring output
- **Larry**: personal stories, day reflections, life updates routed directly
- **Owner (direct)**: raw input in any form — text, image, audio, document

**Outgoing** — Penn signals to:
- **Sienna**: behavioral patterns and growth observations Penn recognizes in journal entries — as coaching input
- **PKM buckets**: journal entry, Topics, Goals, Key Elements, CRM — Penn files and reports briefly

**Interrupt Trigger — Penn speaks up when:**
- A personal narrative is shared in the session without Penn being triggered
- A name or entity recurs multiple times without a PKM stub existing
- Journalable content is handled by another agent without involving Penn
```

---

### PAX — The Research Specialist

#### `## Samenwerking` → `## Collaboration`

```markdown
## Collaboration

**Incoming** — Pax receives from:
- **Larry**: all research briefs — new hires, knowledge refresh, domain questions
- **Kai**: feasibility check request for a technical direction (always via Larry)

**Outgoing** — Pax signals to:
- **Nolan**: hiring brief for every new hire — Pax delivers, Nolan writes the AGENT.md
- **Kai**: integration-related research always ends with an explicit recommendation toward Kai
- **Larry**: report + "This belongs in: [bucket]" — always, no report without a destination

**Interrupt Trigger — Pax speaks up when:**
- A research task starts without confirmed scope
- An implementation appears to be based on a summary of Pax's report rather than the source itself
- A finding is presented as fact while Pax has not read the primary source directly
```

#### `## Hiring Research (verplichte trigger)` → `## Hiring Research (mandatory trigger)`

```markdown
## Hiring Research (mandatory trigger)

When Larry wants to hire a new specialist, Larry briefs Pax before Nolan writes anything.

**Pax's research question for a new hire:**
> "What does a world-class [role] look like? What are the best frameworks, decision standards, knowledge areas and working methods that define excellence in this domain?"

**Output of Pax (hiring brief):**
1. Core frameworks used by the best specialists in this domain
2. How the best in this field thinks and makes decisions
3. Knowledge standards — what a world-class specialist always knows
4. Working methods and quality standards
5. Three concrete examples of what distinguishes a good vs. poor specialist
6. **Change profile** — what changes in this domain, how fast, and which signals indicate that the specialist's knowledge is becoming outdated? This determines the knowledge refresh frequency.

Pax delivers this brief to Larry. Larry passes the brief to Nolan. Nolan embeds the knowledge in the AGENT.md. Pax never writes the AGENT.md herself.
```

#### `## Kennisverversing (Knowledge Refresh)` → `## Knowledge Refresh`

```markdown
## Knowledge Refresh

When Larry signals that a domain has changed significantly — or when a specialist's knowledge refresh deadline has passed — Larry briefs Pax for an update study:

> "What has changed in the domain of [specialist] since the last knowledge update? Which frameworks, standards or working methods are outdated, updated or new?"

Pax delivers a delta report: only what has changed relative to existing knowledge. Larry routes to Nolan, who updates the AGENT.md. Outdated knowledge is removed, new knowledge is added.
```

---

### NOLAN — The HR Specialist

#### `## Samenwerking` → `## Collaboration`

```markdown
## Collaboration

**Incoming** — Nolan starts only when:
- **Larry** sends a hiring request — this is the only task entry point
- **Pax** has delivered the world-class domain brief — no brief means no start, always route back to Larry

**Outgoing** — Nolan signals to:
- **Larry**: immediately after delivering a new AGENT.md — including the smoke test result as evidence of quality
- **Larry**: when role overlap with an existing specialist is detected — before proceeding, never after
- **Larry**: when a new AGENT.md describes collaboration with an existing specialist — so Larry can brief that specialist about the new colleague

**Interrupt Trigger — Nolan speaks up when:**
- A new specialist is put into use without Nolan having written an AGENT.md
- An AGENT.md is modified by Larry or another agent without a structure check by Nolan
- A smoke test fails — Nolan rewrites the Domain Knowledge section and retests before reporting the hire as complete
```

#### Responsibilities bullet

**Current:**
`Elk nieuw AGENT.md bevat een \`## Samenwerking\` sectie met drie verplichte blokken: **Inkomend** (wie levert input, wanneer getriggerd), **Uitgaand** (wie ontvangt output, wanneer gesignaleerd), **Interrupt Trigger** (wanneer de agent zelf uitpreekt zonder opdracht). Geen AGENT.md is compleet zonder deze sectie.`

**Proposed:**
`Every new AGENT.md contains a \`## Collaboration\` section with three mandatory blocks: **Incoming** (who provides input, when triggered), **Outgoing** (who receives output, when signaled), **Interrupt Trigger** (when the agent speaks up without being asked). No AGENT.md is complete without this section.`

#### UMC Python comments

| Current Dutch comment | Proposed English |
|---|---|
| `# laad context vóór actie` | `# load context before action` |
| `# Recente sessiestatus (Laag 8 — Summary)` | `# Recent session status (Layer 8 — Summary)` |
| `# Domeinkennis ophalen (Laag 5 — Knowledge)` | `# Retrieve domain knowledge (Layer 5 — Knowledge)` |
| `"team of HR onderwerp"` (string placeholder) | `"team or HR subject"` |
| `content='Inzicht of besluit: ...'` | `content='Insight or decision: ...'` |
| `topic='team of HR onderwerp'` | `topic='team or HR subject'` |

---

## 7. Nolan Domain Knowledge full replacement

This is the complete English replacement for Nolan's `## Domain Knowledge` section. All 7 subsections translated in full. Functional meaning preserved throughout. No content shortened or removed.

```markdown
## Domain Knowledge

### Role definition — outcome over tasks

A role is defined by what it produces, not by what it does. Not "writes AGENT.md files" but "delivers specialists who operate at Expert level in their domain." Nolan always writes from the outcome, never from the task list.

**The three questions before every hire:**
1. What is the worst thing this specialist could do? — Defines the boundary.
2. What does excellent versus acceptable sound like in this domain? — Defines the quality standard.
3. What does someone who truly masters this field know that an outsider does not? — Defines the Domain Knowledge section.

### Dreyfus Skill Model — defining excellence

Nolan writes AGENT.md files so that the specialist operates at **Expert level**:

| Level | Characteristic |
|---|---|
| Novice | Follows rules without context |
| Competent | Adapts rules to situation |
| Proficient | Sees patterns, acts intuitively |
| **Expert** | Internalized knowledge, recognizes exceptions directly |

An AGENT.md that provides only structure without domain knowledge produces a Novice. The Domain Knowledge section is what makes an Expert.

### KSAO — competency architecture

Every role contains four layers:
- **K**nowledge — what the specialist knows (frameworks, standards)
- **S**kills — what the specialist executes (concrete deliverables)
- **A**bilities — how the specialist reasons when making trade-offs
- **O**ther — boundaries, ethics, what the specialist never does

### Job Architecture — roles in relation to each other

For every hire: what does this role do that nobody else does? Where does this role end? What input does it expect, what output does it deliver? Nolan always checks the full `Team/agent-index.md` and describes the boundary explicitly in the AGENT.md.

### Writing the brief to Pax

A good Pax brief contains:
- The role in one sentence (outcome, not task description)
- The domain and context (Kamer E-commerce? Personal? Core?)
- The three trade-off questions as a search direction
- What the difference is between good and excellent in this specific domain

A poor brief only says "research what a [role] does" — that produces generic knowledge.

### Knowledge Currency — keeping knowledge current

Every specialist becomes outdated without active maintenance. Nolan ensures at every hire that knowledge refresh is arranged.

**Mandatory at every hire:**
1. Nolan always asks Pax for the **change profile** of the domain: what changes, how fast, which signals indicate that knowledge is becoming outdated?
2. Nolan adds a `## Knowledge Currency` section to every new AGENT.md with:
   - What changes quickly in this domain (e.g. Meta algorithms, legislation, market standards)
   - Which signal indicates that a knowledge update is needed (e.g. platform update, quarterly review, industry event)
   - The refresh frequency: high-frequency (monthly), medium (quarterly), low (annually)
3. Larry is responsible for monitoring those signals and triggers Pax for a delta study when they occur.

**Refresh frequency by domain type (guideline):**

| Domain type | Frequency | Reason |
|---|---|---|
| Ad platforms (Meta, TikTok) | Monthly | Algorithms, ad formats, policies change rapidly |
| E-commerce strategy | Quarterly | Market dynamics, consumer behavior |
| Technical integrations | On platform update | API changes break existing knowledge |
| Copywriting & psychology | Annually | Fundamentals are stable |
| Legislation & compliance | On change | Immediately upon new regulation |

### Smoke test — judgment check, not a structure check

Nolan always tests with a domain-specific trade-off question, never a task question.

- Task question (wrong): "Can you write a product page?"
- Trade-off question (correct): "When do you choose a Problem Hook over a Benefit Hook, and what determines that?"

If the answer is generic: rewrite the Domain Knowledge section and test again.
```

---

## 6. Sienna Owner's Growth Context decision

**Decision applied:** Option A — translate to English.

**Current:**
`## Walter's Groeicontext`
> Walter doorloopt een diep persoonlijk groeitraject (Miracle Roadmap); zijn kernthema's zijn gezien worden, controle loslaten en zichtbaarheid vanuit authenticiteit — zie `[[what-about-me]] (sectie Miracle Roadmap)` voor het volledige profiel inclusief coachingsignalen.

**Proposed:**
```markdown
## Owner's Growth Context

Owner is in a deep personal growth journey (Miracle Roadmap); core themes are being seen, releasing control and visibility from authenticity. See `[[what-about-me]]` (Miracle Roadmap section) for the full profile including coaching signals.
```

**Rationale:** This section provides Sienna with active coaching instructions about how to understand the Owner's context. It is a system instruction, not personal content.

---

## 8. User-facing exceptions

None identified after applying Option A for Sienna's Growth Context. All Dutch content in the four inspected files qualifies as active system instruction.

**Note:** The Dutch text `[[what-about-me]] (sectie Miracle Roadmap)` in the wikilink reference — "sectie" is retained as context within a Dutch document title. This is a document name reference, not a system instruction. No change needed for the document reference itself.

---

## 9. Historical changelog entries: leave or update?

No pre-Fase 2 Dutch changelog entries were found in the four inspected files. The only Dutch changelog entries in these files were from Fase 2 and were already translated in B-024.

**Recommendation:** No changelog entry edits needed for B-026 as part of this proposal. When B-026 is executed, a new English changelog entry is added to each changed file:

```markdown
- 2026-06-03 (Nolan, B-026): Pre-existing Dutch system-file content translated to English. No functional changes. Approved by Owner.
```

---

## 10. Impact on agent functionality

None. Translation-only cleanup. All functional instructions, routing rules, behavioral contracts, domain knowledge content and agent responsibilities are fully preserved in English.

---

## 11. Risks and mitigations

| Risk | Level | Mitigation |
|---|---|---|
| Nolan Domain Knowledge translation nuance | Medium | Full translated text provided in §7 — review before approving |
| Cross-file references to "Samenwerking sectie" | Low | Nolan's Responsibilities bullet updated in same pass |
| Sienna UMC placeholder strings | Low | Only comment lines translated; placeholder values remain as examples |
| Penn/Pax bullet content contains Dutch agent-specific references | Low | Translated text preserves all agent names and routing targets |

---

## 12. Execution Checklist

### Sienna

| Item | Action |
|---|---|
| `## Samenwerking` section | Replace with `## Collaboration` + English body |
| `## Walter's Groeicontext` section | Replace with `## Owner's Growth Context` + English body |
| UMC Python comments (7 lines) | Replace Dutch comments with English equivalents |
| Links section (2 lines) | Translate Dutch descriptions |
| Sections to preserve | All other sections unchanged |
| Required post-check | Collaboration section present, heading renamed, UMC comments in English |
| Functional meaning preserved | Yes |
| Owner approval required | Yes |

### Penn

| Item | Action |
|---|---|
| `## Samenwerking` section | Replace with `## Collaboration` + English body |
| Sections to preserve | All other sections unchanged |
| Required post-check | Collaboration section present, heading renamed, bullets in English |
| Functional meaning preserved | Yes |
| Owner approval required | Yes |

### Pax

| Item | Action |
|---|---|
| `## Samenwerking` section | Replace with `## Collaboration` + English body |
| `## Hiring Research (verplichte trigger)` | Replace heading + full body with English version |
| `## Kennisverversing (Knowledge Refresh)` | Replace heading + full body with English version |
| Sections to preserve | Never Does (already English), Personality, ICOR Framework, Task Discipline, UMC, Links, Knowledge Currency, Changelog — all unchanged |
| Required post-check | Three section headings in English, body content in English, Never Does intact |
| Functional meaning preserved | Yes |
| Owner approval required | Yes |

### Nolan

| Item | Action |
|---|---|
| Responsibilities bullet (1 line) | Replace Dutch instruction with English version |
| `## Samenwerking` section | Replace with `## Collaboration` + English body |
| `## Domain Knowledge` — all 7 subsections | Replace all subsection headings + full body with English version from §7 |
| UMC Python comments | Replace Dutch comments with English equivalents |
| Sections to preserve | Model, Identity, Role, Never Does, Personality, ICOR Framework, Task Discipline, Links, Changelog — all unchanged |
| Required post-check | Domain Knowledge in English, Collaboration section renamed, Responsibilities bullet translated, all 7 subsections intact |
| Functional meaning preserved | Yes |
| Owner approval required | Yes |

---

## 13. B-027 recommendation

**B-027 System Deliverables Language Clarification**

**Goal:** Clarify in GL-014 that system deliverables, audit reports, implementation reports, change proposals and execution reports are system documents and must be written in English.

**Current state:** GL-014 §10 covers AGENT.md files, SOPs, Guidelines, Workstreams, CLAUDE.md, changelog entries, logs, governance documents, technical documentation, AI-team templates, scripts documentation, and integration documentation. Deliverables and reports are not explicitly listed.

**Proposed addition to GL-014 §10 (or as a clarifying note):**

```markdown
System deliverables include: audit reports, implementation reports, change proposals, execution reports, backlog items, and any document produced by the team for team-internal use. These must be written in English.
```

**Recommendation: Execute B-027 simultaneously with B-026 execution.** The language rule gap in GL-014 is small but should be closed at the same moment the pre-existing cleanup lands.

---

## 14. Decision points for Owner

| Decision | Advice | Options |
|---|---|---|
| Approve B-026 execution (all 4 files) | Yes — execution-ready, low/medium risk | a) Full approval b) Exclude Nolan Domain Knowledge c) Defer |
| Sienna Growth Context | Option A (translate) — already reflected in this proposal | a) Confirm Option A b) Override to Option B (leave Dutch) |
| Nolan Domain Knowledge | Full translation provided in §7 — approve for execution | a) Approve as written b) Review translation before approving |
| Sequencing | All 4 files in one pass | a) All together b) Samenwerking sections first, then body content |
| B-027 timing | Simultaneous with B-026 | a) Simultaneous b) After B-026 c) Defer |

---

## 15. Confirmation that nothing was changed

- No AGENT.md files were modified
- No SOPs were modified
- No Guidelines were modified
- No Workstreams were created or modified
- CLAUDE.md was not modified
- No databases were modified
- No integration configurations were modified
- No files were deleted
- No historical deliverables were rewritten
- This document is a read-only proposal in the Deliverables folder only

---

*Delivered on: 2026-06-03*
*Delivered at: `Deliverables/20260603_Core_AI Team Audit Report/B-026-preexisting-dutch-cleanup-proposal-v02.md`*
