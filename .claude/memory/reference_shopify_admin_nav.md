---
name: reference_shopify_admin_nav
description: Shopify Admin navigation for creating a Custom App (Dev Dashboard)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9ee1fbf6-8402-49f6-9abd-4682dad011f1
---

Creating a Custom App in Shopify Admin (2025/2026):

**Settings → Apps → Build apps in Dev Dashboard**

Previous path (no longer correct): Settings → Apps and sales channels → Develop apps

Steps:
1. Settings → Apps → Build apps in Dev Dashboard
2. Create an app → give it a name (e.g. "myPKA")
3. Configuration → set Admin API scopes
4. Save
5. API credentials → Install app
6. Copy Admin API access token (starts with `shpat_`) — visible only once

Store token in: `Team Knowledge/Core/Integrations/shopify/.env` as `SHOPIFY_ADMIN_TOKEN=shpat_...`
