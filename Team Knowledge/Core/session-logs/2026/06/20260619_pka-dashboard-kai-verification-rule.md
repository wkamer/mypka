# PKA dashboard setup + Kai verification rule

**Date:** 2026-06-19
**Agent:** Larry
**Domain:** Team
**DB row:** team-knowledge.db session_logs id 245

---

## What happened

Set up `https://dashboard.kmerbase.com` as the first PKA dashboard. nginx was not yet installed — added as part of the deployment. Dashboard stored at `/opt/myPKA/apps/dashboard/`, nginx server block created at `/etc/nginx/sites-available/dashboard.kmerbase.com`, serving on `127.0.0.1:8080`.

Diagnosed a 404 after deployment: the Cloudflare Tunnel uses remote-managed ingress config (via Zero Trust dashboard), not the local `config.yml` ingress section. The local file was updated but the running tunnel ignored it. CNAME was successfully created via `cloudflared tunnel route dns`. Dashboard route must be added manually in Cloudflare Zero Trust (Networks > Tunnels > Configure > Public Hostnames).

Discussed Karpathy's three-layer framework (Spec, Verifier, Environment). Confirmed it is already implemented system-wide via GL-023 (Pre-Build Protocol) and GL-005 (AI Engineering Operating System). The gap was that Kai reported success after checking localhost only — the verify plan did not reach the public endpoint. Updated Kai's AGENT.md with a Never Does rule anchored to GL-023 Step 3.

Dashboard confirmed live at HTTP 200 after DNS propagation.

---

## Decisions

- Dashboard stored at `/opt/myPKA/apps/dashboard/` (scale-proof, room for future apps)
- nginx on port 8080, Cloudflare Tunnel for external access (no open ports)
- Full site name as nginx config filename: `dashboard.kmerbase.com`
- Verify plans must reach the actual public endpoint, not just localhost (GL-023 Step 3)

---

## Actions taken

- nginx 1.26.3 installed and enabled
- `/opt/myPKA/apps/dashboard/index.html` created (Hello World)
- `/etc/nginx/sites-available/dashboard.kmerbase.com` created and symlinked to sites-enabled
- CNAME `dashboard.kmerbase.com` registered via `cloudflared tunnel route dns`
- Kai AGENT.md updated: Never Does rule for GL-023 Step 3 (verify plan must cover public endpoint)

---

## Open items

- Add `dashboard.kmerbase.com → http://127.0.0.1:8080` in Cloudflare Zero Trust dashboard (Networks > Tunnels > Configure > Public Hostnames) — tunnel uses remote-managed config only, local ingress ignored.
