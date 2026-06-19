# WS-001 — Kamer E-commerce Operational Process Framework

**Domain:** Kamer E-commerce
**Brand:** Tricolarae
**Market:** United States
**Supplier:** Trendsi (US-based)
**Phase:** 1 — Generic Dropshipping
**Created:** 2026-05-19
**Lead:** Nova (operational) + Vera (strategic)

---

## Purpose

This document describes the full operational process of Kamer E-commerce — from product discovery to post-sale. It is the foundation for all SOPs, workstreams, and automation built on top of it.

Each specialist knows what their step is, what the input is, what the output is, and to whom that output goes.

---

## Process Overview

```
Phase 1   Product Discovery          Bo + owner
   ↓
Phase 2   Product Validation         Bo
   ↓ Go signal
Phase 2b  Margin Check               Nova
   ↓ Break-even CPA + approval
Phase 3   Supplier Setup & Listing   Nova + Sasha
   ↓ Listing ready
Phase 4   Store Listing              Sasha
   ↓ Live
Phase 5   Ads Intelligence           Zara
   ↓ Creative briefs approved by owner
Phase 6   Campaign Launch            n8n / Kai
   ↓ Campaign active
Phase 7   Operational Monitoring     Nova
Phase 8   Performance Analysis       Zara
   ↓ Scale / Kill / Rotate
Phase 9   Strategic Decision         Vera + owner
   ↓
Phase 10  Post-Sale & Retention      Nova + Sasha
```

---

## Phase 1 — Product Discovery

**Lead:** Bo (supported by the owner)
**Trigger:** need for new products in the assortment

**Sources:**
- Trendsi app — browse by category and trending items
- Meta Ad Library — which apparel products are being actively advertised?
- TikTok Creative Center — trending fashion products
- Competitor stores — which products are competitors listing?

**Output:** longlist of candidate products with source and first impression

**Trigger to phase 2:** minimum 3–5 candidates that fit Tricolarae (feel, style, target audience)

---

## Phase 2 — Product Validation

**Lead:** Bo
**Trigger:** longlist received from phase 1

**Steps:**
1. Run Must-Have criteria for each product — see [[KE-Products]]
2. Assign Nice-to-Have score (0–5)
3. Apply Tricolarae-specific filters (brand fit, outfit context, season)
4. Document Go / No-Go decision with rationale

**Output:** shortlist of Go products only + rationale per product

**Trigger to phase 2b:** Go signal from Bo

---

## Phase 2b — Margin Check

**Lead:** Nova
**Trigger:** Go signal from Bo + product data (Trendsi wholesale price)

**Pricing formula:**
```
Selling price = Trendsi price + shipping + Shopify/Stripe fees + expected return costs + target margin
```

- Target contribution margin: ≥20% per order
- Calculate break-even CPA → this figure goes directly to Zara
- Products below 20% margin: return to Bo with finding (too expensive to source at this selling price)

**Output:** approved selling price per product + break-even CPA for Zara

**Trigger to phase 3:** margin approved

---

## Phase 3 — Supplier Setup & Listing Preparation

**Lead:** Nova (setup) + Sasha (Shopify execution)
**Trigger:** margin approved

**Steps:**
1. Import product from Trendsi app to Shopify (Sasha)
2. Set selling price based on phase 2b (Sasha)
3. Create supplier scorecard entry for this product (Nova)
4. Confirm dispatch time and stock availability with Trendsi (Nova)

**Output:** product ready in Shopify (not yet published), scorecard active

**Trigger to phase 4:** product ready to go live in Shopify

---

## Phase 4 — Store Listing

**Lead:** Sasha
**Trigger:** product ready in Shopify

**Steps:**
1. Write product title — no supplier names, Tricolarae tone
2. Product description and copy
3. Check images for quality and brand fit
4. Delivery time expectation clearly stated (Trendsi delivers 3–7 days in US)
5. Publish product

**Output:** live listing on Tricolarae

**Trigger to phase 5:** listing live

---

## Phase 5 — Ads Intelligence

**Lead:** Zara
**Trigger:** listing live + break-even CPA received from Nova

**Steps:**
1. Determine awareness level for this product in the US market
2. Determine market sophistication stage via Meta Ad Library analysis
3. Angle strategy: which angles to test, in which order
4. Creative brief per angle: hook, copy structure, visual direction
5. Campaign structure: ABO test phase, budget, target audience, exclusions

**Output:** creative briefs + campaign structure — for approval by owner

**Trigger to phase 6:** owner approves creative briefs

---

## Phase 6 — Campaign Launch

**Lead:** n8n / Kai
**Trigger:** approved creative briefs from Zara

**Parameters (test phase):**
- ABO, small test budget
- 6–8 creatives
- Minimum 3–5 days running before first review

**Output:** active test campaign in Meta

**Trigger to phases 7 + 8:** campaign active

---

## Phase 7 — Operational Monitoring

**Lead:** Nova
**Trigger:** campaign active + first orders received

**Daily:**
1. Orders without dispatch confirmation after 48h → escalate to Trendsi
2. Deliveries outside window (>7 days) → proactive customer contact
3. New return requests → register cause

**Monthly:** Update Trendsi scorecard (dispatch time, defect rate, communication)

**Output:** operational health report, return analysis

---

## Phase 8 — Performance Analysis

**Lead:** Zara
**Trigger:** minimum 3–5 campaign days + sufficient data

**Kill criteria:**
- Hook rate <15% after 1,000+ impressions
- CTR <1% without ATC after 1,500 impressions

**Keep criteria:**
- ROAS >break-even for 3+ consecutive days

**Scale criteria:**
- Duplicate winner to CBO
- Budget +20–30% per step, no more

**Output:** scale / kill / rotate decision per creative + winner analysis for hook database

**Trigger to phase 9:** winning product confirmed or decision to stop

---

## Phase 9 — Strategic Decision

**Lead:** Vera + owner
**Trigger:** performance analysis completed

**Standing review questions:**
1. Is the contribution margin in line with the target?
2. Is LTV:CAC moving toward 3:1?
3. Is this product a candidate for branded dropshipping (phase 2 growth path)?
4. Does performance justify more budget or a product expansion?

**Output:** go for scale / stop / branded dropshipping transition

**Phase transition check (Vera):** for every winning product, explicitly assess against [[KE-Strategy]] — when are we ready for the next phase?

---

## Phase 10 — Post-Sale & Retention

**Lead:** Nova (operational) + Sasha (technical)
**Trigger:** order delivered

**Steps:**
1. Customer receives tracking automatically via Shopify
2. On delay: proactive message before complaint
3. Handle return via Trendsi return policy
4. Document return cause
5. On structural pattern: product feedback to Bo + Nova for listing adjustment

**Output:** customer satisfaction, clean return data, structural improvements

---

## Open Items

- Update Bo's AGENT.md with Must-Have criteria and discovery sources (Pax → Nolan)
- Install Trendsi Shopify app and test connection (Sasha + Kai)
- Run first margin check on current assortment (Nova)
- Build campaign launch via n8n (Kai) — only after first approved creative brief
- Rewrite product titles in Shopify — remove supplier names (Sasha)
- Remove placeholder products from store (Sasha)

---

## References

- [[KE-Products]] — Must-Have criteria, Nice-to-Have scoring, current assortment
- [[KE-Research]] — Research workflow steps 1–8
- [[KE-Strategy]] — Growth path phases 1–5, phase decision criteria
- [[KE-Advertising]] — Hook database, creative intelligence, Graduation System
- [[KE-Fulfillment]] — Supplier validation and fulfillment standards
