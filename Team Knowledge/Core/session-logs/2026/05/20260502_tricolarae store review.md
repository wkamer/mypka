# Tricolarae store review via Vera and Sasha

**Date:** 2026-05-02
**Session ID:** 6 (kamer e-commerce.db)
**Topics:** tricolarae, shopify, business-setup, vera, sasha

## Summary

Vera assessed overall Tricolarae business setup status. Sasha reviewed the Tricolarae Shopify store pages via the Admin API, reading the Privacy Policy and 15 other live pages. Several critical issues were found: Privacy Policy missing CCPA section, references Netherlands law (wrong jurisdiction), Trendsi not listed as data processor, FAQ page empty, Track Your Order page empty, two duplicate shipping pages, and Terms of Service governed by Netherlands law. Sasha drafted improvements but the Privacy Policy rewrite was not yet finalized.

## Decisions

- Use Shopify Admin API (shopify store execute --allow-mutations) as Sasha's primary tool for store reads/writes
- Privacy Policy needs: CCPA section, Netherlands reference removed, Trendsi added as processor

## Actions Taken

- Vera reviewed business setup status and reported gaps
- Sasha read Privacy Policy and 15 store pages via Admin API
- Identified critical issues: Privacy Policy, FAQ, Track Your Order, duplicate shipping pages, ToS jurisdiction

## Delegations

- Vera: assessed Tricolarae business setup status (success)
- Sasha: reviewed store pages via Admin API, identified content issues (success)

## Open Items

- Sasha: rewrite Privacy Policy (add CCPA, remove Netherlands ref, add Trendsi as processor)
- Fix empty FAQ page
- Fix empty Track Your Order page
- Resolve duplicate shipping pages
- Fix ToS Netherlands law reference

---

Delivered on: 2026-05-02
Delivered at: Kamer E-commerce/Knowledge/session-logs/2026-05-02-tricolarae-store-review.md
