# Tricolarae — US Store Content Audit

**Prepared by:** Pax (Deep Research)
**For:** Tricolarae (tricolarae.com) — pre-launch
**Market:** United States
**Model:** Shopify dropshipping (supplier: Trendsi, US-based) — women's fashion

---

## Executive Summary

Tricolarae is preparing to sell physical goods to US consumers — including consumers in California and 15+ other states with active privacy laws. That triggers a stack of legal, platform, and trust requirements. This audit lists every page or piece of content a US-targeted Shopify fashion store should have before launch, and flags which ones carry actual legal risk vs. which are trust/conversion plays.

The audit is split into three sections:
1. **Legal and platform-required** (High priority — launch-blocking)
2. **Customer trust essentials** (Medium-High — strongly impacts conversion)
3. **Nice to have** (Low — add post-launch)

A Shopify store at minimum is required by Shopify's own terms to publish: public-facing contact info, Terms of Service, Refund Policy, and Shipping Policy. Add a Privacy Policy on top of that, because CCPA/CPRA and 15+ other US state privacy laws apply the moment a Californian (or Virginian, Coloradan, Texan, etc.) lands on the site.

---

## Section 1 — Legal & Platform-Required (Priority: HIGH)

These pages are either legally required, required by Shopify's TOS, or expose the owner to direct legal/financial risk if missing. Launch should not happen without all of them.

| Required / Expected | Why it matters | Priority |
|---|---|---|
| **Privacy Policy** (with CCPA/CPRA section) | Required by Shopify TOS. Required by CCPA/CPRA for any business serving California consumers, and by 15+ other US state privacy laws (VA, CO, CT, UT, TX, OR, etc.). Must disclose: categories of personal info collected, purposes, third parties (Shopify, Trendsi, Meta/Google pixels), consumer rights (access, delete, opt-out of sale/share), and a "Do Not Sell or Share My Personal Information" link. | HIGH |
| **Terms of Service** (Terms & Conditions) | Required by Shopify TOS. Defines the contract between Tricolarae and the buyer: governing law (state of incorporation), limitation of liability, dispute resolution / arbitration clause, intellectual property, account/eligibility rules. Without this, any dispute defaults to consumer-friendly law of the buyer's state. | HIGH |
| **Refund / Return Policy** | Required by Shopify TOS. Must be conspicuously displayed before purchase (FTC requirement). Should match Trendsi's actual policy: 7-day window, customer pays return shipping, no exchanges, list of non-returnable categories (bodysuits, swimwear, lingerie, jewelry, beauty). Must also explain the refund mechanism, timeline, and how to initiate a return. | HIGH |
| **Shipping Policy** | Required by Shopify TOS. Must state processing time, carriers, transit time (2–5 business days via Trendsi US), domestic-only restriction (if applicable), shipping cost rules, lost/stolen package handling. FTC's Mail/Internet Order Rule requires shipping within the timeframe promised; if no timeframe is stated, the default is 30 days. | HIGH |
| **Contact Page** with business identity | Shopify TOS requires public-facing contact info. The INFORM Consumers Act (federal, 2023) requires online sellers to disclose business name and a working contact channel. CAN-SPAM Act requires a valid physical postal address (P.O. box is acceptable) on commercial email — and best practice is to put it on the site too. Minimum: business name, support email, response-time expectation. Phone is not strictly required but raises trust significantly. | HIGH |
| **Cookie banner / consent management** | CCPA/CPRA requires a clear opt-out for "sale or sharing" of personal info — including most ad-tech pixels (Meta, Google, TikTok). The cookie banner is the visible mechanism. Shopify has a built-in Customer Privacy API; a GCM (Google Consent Mode) compatible app like Pandectes, Consentmo, or Shopify's own banner must be enabled. Without this, running Meta/Google ads to California traffic is non-compliant. | HIGH |
| **"Do Not Sell or Share My Personal Information" link** (in footer) | Specifically required by CCPA/CPRA when the site uses ad pixels, retargeting, or analytics that count as "sharing." Must be a clear link in the site footer, not buried in the privacy policy. | HIGH |
| **Accurate product descriptions & imagery** | FTC requires advertising to be truthful. Product copy and photos must match what Trendsi actually ships. Avoid any "Made in USA" claim unless verified — the FTC's March 2026 Executive Order specifically targets false country-of-origin claims, common in dropshipping. | HIGH |
| **Pricing & checkout transparency** | All fees (shipping, taxes) must be disclosed before the customer commits to purchase. No hidden fees. Sales tax must be calculated correctly via Shopify Tax for US states where Tricolarae has nexus. | HIGH |
| **Business registration & sales tax setup** (off-site, but blocks legal launch) | Selling in the US requires either a sole proprietorship, LLC, or other entity, plus sales tax registration in any state where the store has economic nexus (commonly $100K in sales OR 200 transactions in a state). Trendsi as the shipper does not absolve Tricolarae of nexus obligations — the seller of record is Tricolarae. | HIGH |

---

## Section 2 — Customer Trust Essentials (Priority: MEDIUM-HIGH)

These are not legally required, but US fashion shoppers expect them. Their absence directly suppresses conversion — especially for an unknown new brand with no sales history. For a pre-launch dropshipping store, these are nearly as important as the legal pages because the conversion ceiling without them is very low.

| Required / Expected | Why it matters | Priority |
|---|---|---|
| **About Us page** | First-time visitors to an unknown brand check the About page to verify "is this real?" Should cover: who's behind the brand, the brand's point of view (aesthetic, who it's for), and why the owner started it. For dropshippers this page is critical — it's the main signal that distinguishes Tricolarae from a generic Shopify+AliExpress storefront. Avoid stock-photo "our story" templates; write it personally. | MEDIUM-HIGH |
| **Size Guide** | Sizing is the #1 cause of returns in fashion ecommerce — clear size guides cut size-related returns by ~33%. For US customers buying women's knitwear, include US sizing (XS–XXL), bust/waist/hip in inches, and ideally a model height/size reference. Trendsi typically provides size charts per product — either embed per product or build a single Size Guide page. | MEDIUM-HIGH |
| **FAQ page** | 69% of customers prefer self-service answers over emailing support. For fashion, the must-cover questions: shipping time, returns process, sizing, fabric/care, order tracking, payment methods, contact response time. Reduces support load and pre-empts purchase objections. | MEDIUM-HIGH |
| **Shipping Information page** (customer-facing version) | The legal Shipping Policy is dense and legalistic; customers need a friendlier page that says: "We ship within the US in 2–5 business days. Free shipping over $X. Tracking is sent via email." This can be a section of the FAQ or a standalone page. | MEDIUM |
| **Returns / Exchange Information page** (customer-facing) | Same logic as shipping — the legal policy is hard to scan. A short, plain-language page that says "7 days to return, you cover return shipping, here's how to start a return" reduces pre-purchase hesitation. | MEDIUM |
| **Contact form / customer support channel** | A form on the contact page (in addition to a listed email) lowers friction. Set expectations: "We reply within 24 hours, Mon–Fri." | MEDIUM |
| **Order tracking page or instructions** | US customers expect to track orders post-purchase. Shopify's order status page is auto-generated; supplement it with copy on the FAQ explaining how tracking emails work. | MEDIUM |
| **Trust badges at checkout** | "Secure checkout," accepted payment methods (Visa, Mastercard, Amex, PayPal, Apple Pay, Shop Pay), and an SSL/lock indicator. Shopify includes most of this by default — verify it's visible. | MEDIUM |
| **Social proof (eventual)** | No reviews yet because pre-launch. Plan to add a review app (Judge.me, Loox, Shopify Product Reviews) and wire up post-purchase review requests from day one so reviews accumulate from the first cohort of orders. | MEDIUM (build now, populate later) |
| **Newsletter signup with privacy disclosure** | Standard for fashion. Capture email with a small incentive (10% off first order is the category norm). Disclosure must say what they're subscribing to and link to the privacy policy. CAN-SPAM requires a working unsubscribe in every email sent. | MEDIUM |
| **Care instructions / fabric content (per product)** | Fashion buyers — especially knitwear buyers — expect fabric composition (e.g. "60% cotton / 40% acrylic") and care instructions ("hand wash cold, lay flat to dry"). Trendsi typically supplies this in the product feed; verify it's pulled into the Shopify product pages, don't leave it blank. | MEDIUM |

---

## Section 3 — Nice to Have (Priority: LOW)

These improve polish, SEO, and brand perception. Not required for launch; can be added in the first 60 days post-launch.

| Required / Expected | Why it matters | Priority |
|---|---|---|
| **Accessibility Statement** | The April 2026 ADA Title II rule technically applies to state and local government entities, not private retailers. However, private ecommerce stores are increasingly targeted by ADA Title III lawsuits for inaccessible sites. WCAG 2.1 AA is the de facto standard. An accessibility statement (committing to WCAG 2.1 AA, providing a contact for accessibility issues) is a reasonable defensive posture and a 1-hour task. | LOW (Medium if budget for litigation defense matters) |
| **Blog / Editorial section** | Drives organic SEO traffic for fashion long-tail terms ("best chunky cardigan for fall," "how to style a knit cardigan"). Compounds over time. Not needed at launch; start within 30–60 days. | LOW |
| **Lookbook / Style guide** | Fashion brands often have a lookbook that shows products styled together. Helps cross-sell. Can be a single landing page or an Instagram-style grid. | LOW |
| **Gift card support** | Shopify supports gift cards natively. Useful for Q4 holidays. | LOW |
| **Rewards / loyalty program** | Repeat-purchase driver. Premature pre-launch — add once there's a cohort to retain. | LOW |
| **Press / Media kit page** | Useful if Tricolarae starts pursuing PR or affiliate placements. Not needed for cold launch. | LOW |
| **Affiliate / Influencer page** | Same logic — add when there's an affiliate program to point to. | LOW |
| **Wishlist functionality** | Fashion shoppers use wishlists. Many free Shopify apps. Adds friction-free re-engagement. | LOW |

---

## Dropshipping-Specific Considerations

A few items deserve special attention because Tricolarae is dropshipping:

1. **Never claim "Made in USA"** unless the actual garment origin is verified — Trendsi sources globally. The FTC's March 2026 Executive Order specifically targets false country-of-origin claims, and the agency has historically prosecuted dropshippers for this exact violation.

2. **Set realistic shipping expectations.** Trendsi's stated 2–5 business days is an advantage over typical AliExpress dropshipping (10–30 days). Lean into this — but state it clearly and meet it. The FTC's Mail/Internet Order Rule requires the seller to ship within the promised window or notify and offer a refund.

3. **Do not imply Tricolarae owns or operates a warehouse.** Don't say "our warehouse" — it's Trendsi's. "Ships from our US fulfillment partner" is honest and acceptable.

4. **Trendsi is the supplier, Tricolarae is the seller of record.** That means Tricolarae — not Trendsi — is responsible to the customer, to the FTC, and to state tax authorities. The privacy policy must disclose that order data is shared with Trendsi for fulfillment.

5. **Product images and descriptions**: if Trendsi-supplied imagery is used, ensure Tricolarae has the right to use it (Trendsi grants this in their TOS for active resellers). Avoid copying language from other Trendsi reseller stores — duplicate content hurts SEO and looks generic.

6. **No fake reviews.** FTC rules in 2024 made fake reviews and AI-generated testimonials explicit violations. Wait for real reviews; do not seed.

7. **Consider product liability insurance.** As seller of record, Tricolarae is legally on the hook if a garment causes harm (skin reaction, choking hazard on a button, etc.). Affordable for low-volume sellers; worth pricing once revenue starts.

---

## Recommended Launch Checklist (Action Order)

**Block launch until done:**
1. Generate Privacy Policy, Terms of Service, Refund Policy, Shipping Policy via Shopify's built-in policy generator (Settings → Policies). Customize the Privacy Policy with a CCPA/CPRA section and a "Do Not Sell or Share" link.
2. Enable Shopify's Customer Privacy banner (or install Pandectes/Consentmo) and configure for CCPA opt-out.
3. Build a Contact page with business name, support email, physical address (P.O. box or registered address), and response-time expectation.
4. Verify business entity is registered and sales tax is set up in any state with nexus.
5. Audit every product page: accurate description, fabric content, care, no false origin claims, real photos.
6. Add a "Do Not Sell or Share My Personal Information" link to the site footer.

**Build before launch (trust layer):**
7. Write a personal About page (300–500 words, real story, real photos if possible).
8. Build a Size Guide page (US sizing, inches, model reference).
9. Build an FAQ page covering the 8–10 highest-frequency questions.
10. Write friendly customer-facing Shipping Info and Returns pages.
11. Install a review app (Judge.me / Loox) and wire up post-purchase review emails so reviews start collecting from order #1.
12. Add a newsletter signup with the 10% off welcome incentive and privacy disclosure.

**Add within 30–60 days post-launch:**
13. Accessibility statement.
14. Blog / editorial content for SEO.
15. Lookbook page.

---

## Sources

- [Privacy Policy for Shopify Store: Complete Guide (2026) — LegalForge](https://www.legalforge.app/blog/privacy-policy-for-shopify-store)
- [Shopify Help Center — US state privacy laws](https://help.shopify.com/en/manual/privacy-and-security/privacy/us-state-privacy-laws)
- [Shopify Help Center — Adding store policies](https://help.shopify.com/en/manual/checkout-settings/refund-privacy-tos)
- [How To Write a Website Privacy Policy (2026) — Shopify](https://www.shopify.com/blog/website-privacy-policy)
- [2026 US Privacy Laws: How to Prepare Your Shopify Store — Consentmo](https://www.consentmo.com/blog-posts/2026-us-privacy-laws-compliance-update)
- [Is Dropshipping Legal? A Practical Guide to Staying Compliant (2026) — Shopify](https://www.shopify.com/blog/is-dropshipping-legal)
- [Is Dropshipping Legal in 2026? Complete US Legal Guide — Minea](https://www.minea.com/dropshipping-legal)
- [Is Dropshipping Legal? How to Stay Compliant (2026) — TrueProfit](https://trueprofit.io/blog/is-dropshipping-legal)
- [INFORM Consumers Act: What E-Commerce Businesses Must Know — Revision Legal](https://revisionlegal.com/internet-law/inform-consumers-act-ecommerce-compliance/)
- [Website Legal Requirements – Contact and Company Information — Bodle Law](https://www.bodlelaw.com/e-commerce/website-legal-requirements-contact-information)
- [6 Essential Pages Every Fashion E-commerce Website Must Have — Lexi Studio](https://bonjourlexi.com/fashion-ecommerce-essential-pages/)
- [The 14 Steps to Write a Perfect FAQ For Clothing Websites — Robosize](https://robosize.com/blog/faq/)
- [7 Outstanding E-Commerce Size Guide Examples — Drip](https://www.drip.com/blog/e-commerce-size-guide-examples)
- [ADA Compliance for eCommerce Websites: 2026 Complete Guide — accessiBe](https://accessibe.com/blog/knowledgebase/ada-compliance-for-ecommerce)
- [ADA WCAG 2.1 Compliance 2026: What US Websites Need to Know — Flockler](https://flockler.com/blog/ada-wcag-accessibility-compliance-2026)
- [Refund Policy Generator — Free Template — Shopify](https://www.shopify.com/tools/policy-generator/refund)

---

Delivered on: 2026-05-02
Delivered at: Kamer E-commerce/Deliverables/2026-05-02_us-store-audit/
