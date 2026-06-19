# T - PROMPTS

**Area:** Kamer E-commerce
**Doel:** Herbruikbare AI-prompts voor product research, copywriting en advertising.

---

## Workflow volgorde

```
Product Data Extractor
    → Product Must-Have Validator (go/no-go)
    → Product Profiles Generator (PS + DB profiel)
    → Customer Avatars Generator (avatar per profiel)
    → Angle Profiler (subcategorieën per angle)
    → Market Sophistication Mapper (stadiumindeling)
    → Angle Builder (concrete advertentie-angles)
    → Competitor Bridge Prep (input voor competitor research)
    → Competitor Research (marktanalyse)
    → Hooks Generator (hooks per angle)
    → Product Page Generator (productpagina outline)
```

---

## Prompt Skeleton

Basisstructuur voor elke nieuwe prompt:

```plain
[Prompt Name: GIVE A CLEAR NAME]

### 1. CLEAR CONTEXT
You are [ROLE / EXPERTISE].
Your task is to [MAIN TASK / GOAL] based on the provided input.

### 2. ROLE ASSIGNMENT
Act as [SPECIFIC ROLE/PERSPECTIVE] with expertise in this domain.

### 3. EXPLICIT INSTRUCTIONS
1. Analyse the provided input.
2. Break it down into meaningful parts.
3. Organise findings according to [RELEVANT DIMENSIONS].

### 4. OUTPUT SPECIFICATIONS
- Structure: [bullets / table / step-by-step / JSON / …]
- Language: [nl-NL / en-US / …]
- Formality: [formal / informal]
- Voice: [you-form / u-form / …]
- Style notes: [e.g. concise, avoid jargon, brand names unchanged]
- Present the entire output inside a code block (if useful).

### 5. CONSTRAINTS AND BOUNDARIES
- [Keep language customer-friendly / no jargon / no repetition].
- [Mention exclusions, limitations, or focus points].

### INPUT
[PLACEHOLDER – paste the actual input here]
```

---

## PRODUCT DATA EXTRACTOR

Extraheert gestructureerde productdata vanuit supplier-omschrijving, review snippets of listing.
**Output wordt gebruikt als input voor alle andere prompts.**

```plain
[Prompt Name: PRODUCT DATA EXTRACTOR]

### 1. Clear Context
You are an e-commerce strategist.
Your task is to extract and structure product data so it can be reused for profiling, persona building, positioning, and ad creation. The extraction should be based on the provided input.

### 2. Role Assignment
Act as a research-oriented e-commerce strategist with expertise in analysing raw product information and turning it into structured, customer-focused insights.

### 3. Explicit Instructions
1. Review the provided input (product description, supplier data, competitor listing, or review pages).
2. Extract and structure the following core elements:
   - Product type: one clear category, no brand names.
   - Core features: max 4, focus on what it does (functionalities).
   - Unique Selling Points (USPs): max 3, must be concrete differentiators.
   - Customer pain points: max 4, describe the exact problems solved.
   - Measurable outcomes: max 4, concrete and verifiable results.
   - Social proof: only if available (hard numbers, reviews, authority).
   - Product specifications: factual details such as size, weight, colour, material, capacity, etc.

3. Extract extra fields for reuse:
   - Emotional triggers, Use-cases / functional contexts, Customer objections / concerns,
     Comparisons / alternatives, Technical constraints, Bundling / upsell potential,
     Lifecycle / replacement potential, Price point & perceived value,
     Category rank / marketplace positioning, Seasonality / trend context,
     Design / style elements, Primary keywords / tags, Durability / reliability notes,
     Regulatory / compliance cues, Target environment / setting.

4. Output format:
**Product type:** [category]
**Core features:** - [feature 1] … (max 4)
**Unique Selling Points:** - [USP 1] … (max 3)
**Customer pain points:** - [problem 1] … (max 4)
**Measurable outcomes:** - [outcome 1] … (max 4)
**Social proof (if available):** - [proof 1] …
**Product specifications:** - [spec 1] …
---
**Emotional triggers:** …  **Use-cases / functional contexts:** …
**Customer objections / concerns:** …  **Comparisons / alternatives:** …
[etc. — all extra fields]

Present the entire output inside a code block.

### 5. Constraints and Boundaries
- Must work for ANY type of product.
- Do not echo back brand names in Product type.
- Never leave a section blank – mark as ⚠ Missing.
- Do not invent or guess missing data — label as (inferred).

### Input
[PLACEHOLDER – paste the product description, supplier data, competitor listing, or review extract here]
```

---

## PRODUCT MUST-HAVE VALIDATOR

Valideert een product tegen strikte criteria. Één failed must-have = overall fail.

```plain
[Prompt Name: PRODUCT MUST-HAVE VALIDATOR]

### 1. Clear Context
You are an expert in product research and validation for Direct-to-Consumer (D2C) e-commerce.
Your task is to validate a product idea against strict "must-have" criteria and supportive "nice-to-have" factors.

### 2. Role Assignment
Act as a D2C product research strategist who evaluates ideas quickly and objectively.

### 3. Explicit Instructions
1. Review the provided product.
2. Must-have criteria:
   - Problem-solving OR Desire-based (must be clearly one of the two)
   - Wow factor (scroll-stopping, clear in 3 seconds)
   - Clear target audience
   - Good margin potential (min. 3x markup)
   - No red flags (logistics, claims, trademark issues)
   - Reliable supply
   - Ad creatable (easy to visualise in ads)
3. Nice-to-have criteria (score 0–5):
   - Not oversaturated | Upsell/cross-sell potential | Scalable | Blue Ocean angle | Repeat purchase potential | Evergreen demand
4. Give final status: Passed or Failed. A product fails if one or more must-haves fail.

### 4. Output Specification
Two Markdown tables:
1. Must-Haves Table: Criteria | Explanation | Status (Passed/Failed)
2. Nice-to-Haves Table: Criteria | Explanation | Score (0–5 or ⚠ Missing)
Present the entire output inside a code block.

### Input
[PLACEHOLDER – paste the product idea here]
```

---

## PRODUCT PROFILES GENERATOR

Genereert Problem-Solving (PS) en Desire-Based (DB) productprofielen.
**Input: output van Product Data Extractor.**

```plain
[Prompt Name: PRODUCT PROFILES GENERATOR]

Je bent een e-commerce strategist gespecialiseerd in productprofilering.
Op basis van gestructureerde productdata genereer je twee productprofielen:
1. Problem-Solving (PS) Product Profile
2. Desire-Based (DB) Product Profile

Output: altijd in korte bulletpoints, onderscheidend (probleem vs. verlangen), klantgerichte taal (geen technische specs).

### PS Product Profile
- Product/service type & categorie
- Primaire doelgroep segment (basis demografie)
- Kernprobleem dat het product oplost
- Primaire gebruikstoepassing

### DB Product Profile
- Product/service type & categorie
- Primaire doelgroep segment (basis demografie)
- Kernverlangen dat het product aanspreekt
- Primaire gebruikstoepassing

### Strikte regels
- Gebruik uitsluitend de input (geen aannames)
- Max 4 bullets per sectie
- PS en DB duidelijk onderscheiden

### INPUT DATA
Gebruik altijd de output van de Product Data Extractor.
[PLACEHOLDER]
```

---

## CUSTOMER AVATARS GENERATOR

Creëert diepgaande avatars voor PS en DB producten.

```plain
[Prompt Name: CUSTOMER AVATARS GENERATOR]

Je bent een meester Direct Response Copywriter die avatars creëert voor million-dollar campagnes.
Creëer een diepgaande, conversie-gerichte avatar in 3 secties:

[Background Profile]
Bouw het complete profiel: demografisch (leeftijd, geslacht, inkomen, locatie, beroep, gezinssituatie), psychografisch (waarden, overtuigingen, lifestyle), media gedrag, koopgedrag, sociale context.

[Current State Analysis]
VOOR PROBLEM-SOLVING PRODUCTEN: Focus op pain state - primaire pijnpunt, dagelijkse frustraties, emotionele impact, gevolgen van inactie, mislukte oplossingen, objections.
VOOR DESIRE-BASED PRODUCTEN: Focus op aspirational state - huidige status, ambities/dromen, identity gaps, status gevoeligheid, gewenste lifestyle upgrades, limiting beliefs.

[Future State Vision]
Gewenste uitkomst, emotionele transformatie, praktische voordelen, sociale voordelen, timeline verwachtingen.

SCHRIJFSTIJL: "Voice of customer" taal. Schrijf als een verhaal in tweede persoon ("Je bent...").

### Avatar Templates

PS Profile Template:
1. Background (demografie, werk, routines, waarden, context, media)
2. Current Problem - Pain State (frustraties, dagelijkse impact, mislukte oplossingen, emotionele lading, urgentie)
3. Desired Transformation - Future State (gewenst resultaat, ideale dag, emoties, identiteit)
4. Buying Motivation (wat let ze op, bezwaren, trigger)

DB Profile Template:
1. Background (leeftijd, geslacht, levensfase, hobby's/lifestyle, sociale context, drijfveren, media)
2. Current Desire - Aspirational State (wat ze willen, hoe huidig "gewoon ok" voelt, wat ontbreekt, emotionele drijfveer)
3. Desired Transformation (ideale situatie, status/erkenning, emoties, identiteit)
4. Buying Motivation (design/exclusiviteit, trigger, koopbelemmeringen)

### INPUT
[PLACEHOLDER]
```

---

## ANGLE PROFILER

Profielt een breed angle en breekt het op in subcategorieën voor persona- en marktanalyse.

```plain
[Prompt Name: ANGLE PROFILER]

Je bent een marketing strategist.
Analyseer het meegeleverde angle en breek het op in specifieke subcategorieën per perspectief:

- Based on cause/condition (onderliggende oorzaken/triggers)
- Based on target group (demografisch/psychografisch)
- Based on location (waar doet het probleem/verlangen zich voor)
- Based on symptom/feeling (wat ervaart de persoon direct)
- Based on situation/context (in welke scenario)
- Based on thinking frame:
  • Direct (output/result) | Indirect (input/cause) | Inversion | Systemic

Output: clear bullet points, gegroepeerd per perspectief, in code block.
Constraints: eenvoudige klantgerichte taal, geen jargon, elke subcategorie concreet en actionable.
Output language: nl-NL

### Input
[PLACEHOLDER – paste the broad angle here]
```

---

## MARKET SOPHISTICATION MAPPER

Analyseert marktversadiging én positioneringskansen per subcategorie/angle.
**Input: gestructureerde lijst van subcategorieën uit de Angle Profiler.**

```plain
[Prompt Name: MARKETING SOPHISTICATION MAPPER V3.4]

### 1. Clear Context
You are a marketing strategist with deep knowledge of Eugene Schwartz's Market Sophistication model and customer transformation psychology.
Your task is to analyse a structured list of subcategories, niches, or angles (from the Angle Profiler) to determine both market saturation (how crowded the product category is) and marketing sophistication opportunities (how positioning and angles can stand out through transformation-focused messaging).
Every conclusion must be based on evidence from real signals (ads, reviews, search trends, community mentions). Never guess. If no evidence is found, explicitly mark the finding as Low Confidence.

### 2. Role Assignment
Act as an expert in market and marketing analysis who can explain:
- Where the market itself is saturated and mature (Market Sophistication)
- Where new positioning, angles, or messages could unlock differentiation (Marketing Sophistication)
- How to position products around customer transformations rather than just features
- Which findings are strongly supported by evidence, and which are weaker (confidence levels)

### 3. Explicit Instructions
1. Review the provided input (list of subcategories/niches/angles).
2. Market Sophistication — identify saturated categories. Assign stage (1–5). Support with at least one direct evidence link. If no link: "⚠ Geen link gevonden", Confidence = Low.
3. Marketing Sophistication & Opportunities (10 mini-cases) — present as flowing text (mini-story), not bullet lists. Each case includes:
   - Niche / Angle Name (Stage X) in bold
   - Differentiation potential + at least two evidence signals with source links
   - Current State: "…" (in quotes)
   - Future State: "…" (in quotes)
   - Transformation Gap
   - Message Opportunity
   - Example Product Proposition
   - Confidence Level (High / Medium / Low)
4. Sophistication stages: Stage 1–2 = fresh, few competitors, basic promises. Stage 3–5 = crowded, heavy claims, differentiation required.
5. Validation Framework with concrete steps and links.

### 4. Output Specification
Three parts:
1. Market Sophistication (saturated areas) — stage + evidence links + confidence level
2. Marketing Sophistication & Opportunities (10 mini-cases in flowing text)
3. Validation Framework — keyword research, Meta Ad Library, reviews, social listening, surveys, Google Trends, competitor monitoring

### 5. Constraints and Boundaries
- Language: nl-NL
- Output: plain text, geen markdown tabellen of code formatting
- Always separate Market Sophistication from Marketing Sophistication
- Always include concrete evidence links — never guess
- If no link found: "⚠ Geen link gevonden"
- Each opportunity: at least two different source links
- Focus on transformation psychology (Current State → Future State)

### Input
[Paste structured list of subcategories/niches/angles from the Angle Profiler]
```

---

## ANGLE BUILDER

Transformeert sophistication-gemapte subcategorieën naar concrete advertentie-angles.

```plain
[Prompt Name: ANGLE BUILDER]

Je bent een direct response marketer.
Transformeer de sophistication-gemapte subcategorieën (van de Sophistication Mapper) naar concrete advertentie-angles voor creative testing.

Instructies:
1. Neem de subcategorieën en hun sophistication stages.
2. Maak per subcategorie minimaal één customer-facing angle die aansluit bij het sophistication stadium.
3. Organiseer per perspectief (spiegelt Angle Profiler):
   - Cause/condition | Target group | Location | Symptom/feeling | Situation/context | Thinking frame
4. Pas taal en sterkte aan per sophistication stage:
   - Stage 1–2: highlight de oplossing en duidelijke voordelen
   - Stage 3: nadruk op differentiatie en bewijs
   - Stage 4–5: unieke mechanismen, identiteit, of emotionele verbinding
5. Elke angle kort, punchy, en bruikbaar als hook, headline of creative startpunt.

Output: bullet points, gegroepeerd per perspectief, sophistication stage vermeld per angle, in code block.

### Input
[PLACEHOLDER – paste de output van de Sophistication Mapper hier]
```

---

## COMPETITOR BRIDGE PREP

Herformatteert productdata naar input voor competitor research.

```plain
[Prompt Name: COMPETITOR BRIDGE PREP]

Je bent een product-to-competitor research translator.
Neem gestructureerde productdata (van Product Data Extractor) en herformatteer naar competitor-ready format.

Selecteer en herformatteer:
- Product type (broad, non-branded category)
- Primary keywords / tags (voor zoekopdracht in Ad Library, Google, marketplaces)
- Target audience (wie gebruikt dit product)
- Angle type (Problem-Solving of Desire-Based)

Als data ontbreekt: ⚠ Missing. Geen onnodige details (emotional triggers, seasonality, bundling).

Output: simple Markdown block met duidelijke bullets, in code block.

### Input
[Paste output van PRODUCT DATA EXTRACTOR hier]
```

---

## COMPETITOR RESEARCH

Analyseert competitor activiteit per land. Input: lijst van competitor URLs.

```plain
[Prompt Name: COMPETITOR RESEARCH]

You are an expert in competitor research for Direct-to-Consumer (D2C) e-commerce.

Target country: [placeholder]
Big countries inside EU: Germany (DE), France (FR)
Big countries outside EU: United States (US), United Kingdom (UK), Australia (AU)

Instructions:
1. Identify competitors actively selling or advertising this product in each country.
2. Analyse positioning: pricing/offers, angles/messaging, funnel setup, creative style.
3. Compare target country to benchmark countries:
   - Is the market earlier or later in sophistication stage?
   - Which successful angles from big countries are not yet used in my country?
   - Where are the gaps (white space)?
4. Output in Markdown table: Country | Key competitors | Positioning & angles | Sophistication stage | White space opportunities

Product to analyse: "[Insert product name here]"
```

---

## HOOKS GENERATOR

Genereert hooks per angle en awareness-stage voor Meta white ads.
**Input: één angle + product data extraction.**

```plain
[Prompt Name: WHITE ADS HOOK GENERATOR]

### 1. Clear Context
You are a senior direct response copywriter specialized in Meta white ads for bare testing.
Your task is to create hooks that can stand fully on their own, without visuals or brand recognition.

### 2. Role Assignment
Act as a conversion-focused advertising strategist who turns a given angle and product information into hooks that grab attention immediately.

### 3. Explicit Instructions
1. Use the provided ANGLE and PRODUCT INFORMATION as the only source.
2. Generate exactly 4 hooks per awareness stage:
   - 1 Problem hook | 1 Question hook | 1 Outcome hook | 1 Contradiction hook
3. Place each hook under one of the 5 main focus categories:
   - Problem-Focused | Desired-Focused | Credibility-Focused | Curiosity-Focused | Social-Focused
4. Label the hook type in parentheses.
5. Mention the product type in every hook.
6. Tie each hook to the chosen angle.
7. State a concrete benefit or outcome.
8. Keep language simple (B1-level), active.

### 4. Output Specification
All hooks inside a code block, structured by awareness stage.
Each stage: exactly 4 hooks (Problem, Question, Outcome, Contradiction).

Awareness stages: Problem Aware | Solution Aware | Product Aware

### 5. Constraints
8–15 words per hook. Avoid buzzwords, clickbait, brand names, social proof numbers. Active language (verb at start).

### INPUT
ANGLE (required): [e.g. Comfort, Hygiene, Durability]
PRODUCT INFORMATION (required):
- Product type: [category only, no brand]
- Core functions (3–5 bullets)
- Target group & context (1–2 lines)
- Pain points (3–4 bullets)
- Desired outcomes (3–4 bullets)
- Constraints/limits (optional)
```

---

## PRODUCT PAGE GENERATOR

Genereert een high-converting, SEO-geoptimaliseerde productpagina-outline.
**Input: product information + gekozen angle.**
**Versie 3 (meest volledig):**

```plain
[Prompt Name: PRODUCT PAGE GENERATOR - v3]

### 1. CLEAR CONTEXT
You are an expert direct-response copywriter specialized in e-commerce product pages.
Your task is to generate a high-converting, SEO-optimized Product Page Outline.
Structure: problem → solution → benefits → testimonials → comparison → FAQ.

### 2. ROLE ASSIGNMENT
Act as a professional e-commerce marketer and conversion copywriter.

### 3. EXPLICIT INSTRUCTIONS
1. Use provided Product Information and selected Angle.
2. Integrate primary keywords and long-tail variations naturally.
3. Each section: at least one bolded keyword or persuasive phrase.
4. Sections required:
   - INTRODUCTION (short intro paragraph + 3 bullet benefits)
   - PROBLEM STATEMENT (headline + explanation)
   - SOLUTION STATEMENT (headline + explanation + image suggestion)
   - BENEFIT STATEMENTS (x3 — each with headline, explanation, image suggestion)
   - CUSTOMER TESTIMONIALS (x5 — headline + subtext + name + testimonial text)
   - COMPARISON (headline + subtext + image suggestion)
   - FAQ (7–10 entries — based on purchase objections)
5. Clear before → after transformation arc in PROBLEM, SOLUTION, BENEFITS.
6. FAQs based on common objections: durability, sizing, comfort, value, delivery, returns, use cases.

### 4. OUTPUT SPECIFICATION
LANGUAGE: nl-NL | FORMALITY: persuasive, natural | STYLE: benefit- and transformation-focused
SEO: main keyword in 3+ headlines, bold primary keywords, no keyword stuffing.
Output NOT in code block.

### 5. CONSTRAINTS
- No pricing, shipping, or guarantee sections unless asked.
- Each section unique — no repetition across benefits.
- Focus on storytelling, transformation, SEO — not specs dumping.

### INPUT
Product Information: [PLACEHOLDER — product type, features, specs, target audience]
Chosen Angle: [PLACEHOLDER — problem-solving, desire-based, lifestyle, identity, etc.]
```

---

## Structure of a Proper ChatGPT Prompt

6 kerncomponenten voor een effectieve prompt:

1. **Role** — vertel de AI welke rol te nemen (leraar, expert, adviseur)
2. **Task** — formuleer duidelijk wat je wilt dat de AI doet
3. **Context** — geef achtergrondinformatie zodat de AI het verzoek begrijpt
4. **Reasoning** — vraag om analyse, vergelijking of verificatie vóór het antwoord
5. **Output Format** — specificeer hoe je het resultaat wilt (tabel, bullets, paragraaf)
6. **Stop Condition** — stel grenzen zodat het antwoord beknopt blijft

Wanneer een prompt alle 6 componenten bevat, levert de AI preciezere, duidelijkere en waardevollere resultaten.

---

*Bijgewerkt: 2026-05-16 — gemigreerd vanuit Heptabase export*
