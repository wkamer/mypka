# PKA Dashboard: scaffold, auth, CF integration, team roles

**Date:** 2026-06-19
**Agent:** Larry
**Domain:** team
**DB id:** 247

---

## Summary

Built the PKA dashboard from Hello World to a working authenticated web app at dashboard.kmerbase.com. Stack: FastAPI backend + React + Vite + Tailwind. Delivered login page, session cookie auth, Projects tile and page. Fixed CF/nginx/cookie/redirect issues through multiple iterations. Updated Larry and Kai AGENT.md to clarify that Kai owns technical verification and git commits — not Larry.

---

## Decisions

1. FastAPI + React + Vite + Tailwind as dashboard stack
2. CF Zero Trust as outer gate + app login as inner layer (defense in depth)
3. Vite proxy for /api routes (device-agnostic API calls)
4. Kai owns end-to-end verification and git commits — not Larry
5. Commit after owner confirmation, one clean commit per feature
6. App developer specialist review trigger at 5 dashboard tiles

---

## Actions taken

- Scaffold built at /opt/myPKA/apps/dashboard/ (FastAPI backend + React frontend)
- Login page with JWT session cookie (httpOnly, secure=True, samesite=lax, 7 days)
- Nginx proxy config for dashboard.kmerbase.com → Vite on :5173
- Vite allowedHosts: raspberrypi.local + dashboard.kmerbase.com
- Vite proxy: /api → localhost:8000 (device-agnostic)
- Fix: secure=True on set_cookie and delete_cookie
- Fix: window.location.href for login/logout redirect (AuthGate stale state)
- Projects tile on dashboard + /projects page (Personal + Business sections)
- GET /api/projects endpoint parsing project-index.md files
- Larry AGENT.md: Kai owns verification and git, Larry never runs technical checks or git
- Kai AGENT.md: Build and Commit Discipline, verification checklist item, Never Does updated
- Memory: feedback_verify_before_reporting, feedback_commit_and_push, project_dashboard_app_specialist_trigger

---

## Open items

- Change default password (admin/admin) before external use
- Key Elements tile (iteration 3)
- Topics tile (future)
- Systemd auto-start for backend + frontend (deferred)
- Nolan: communicatie_verzender → Sienna AGENT.md (team_task 103)
- Nolan: health_resources_ke → Lena AGENT.md (team_task 104)
- Team Inbox: Deelmomenten MR routing (Penn or Kai?) — awaiting owner decision
- G-Geldstroom Regie deadline 30 juni — on-hold confirm
- Gmail auth expired — re-authentication needed
- Conversation with Rajko Acimovic — still pending
