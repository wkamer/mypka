# Dashboard login debug + Restart=always fix

**Date:** 2026-06-29
**Agent:** Larry
**Domain:** Team

## What happened

Walter meldde een login failure op het dashboard ("Username or password is incorrect"). Diagnose toonde aan dat auth.py en .env correct zijn (admin/admin hash verified via bcrypt). De backend service mypka-dashboard-backend was gisteren om 20:26 clean gestopt via SIGTERM. Omdat de service file Restart=on-failure gebruikte, herstartte de service niet automatisch na een clean stop.

## Decisions

- Dashboard app bugs routen naar Devon (niet Kai).

## Actions taken

- Devon diagnosticeerde de oorzaak: service clean gestopt, Restart=on-failure dekt geen clean stops.
- Devon wijzigde Restart=on-failure naar Restart=always in `/etc/systemd/system/mypka-dashboard-backend.service`.

## Open items

- Walter moet zelf activeren: `sudo systemctl daemon-reload && sudo systemctl restart mypka-dashboard-backend`
- Default password (admin/admin) nog niet gewijzigd — staat nog open in active-context.md
