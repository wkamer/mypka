# Dropbox-iPhone notification refactor — Discord SSOT — 2026-05-21

**Session date:** 2026-05-21
**Topics:** integrations, team-inbox-watcher, discord, architecture

## Summary

Notification architectuur voor Team Inbox gerefactord. SSOT-script notify_team_inbox.sh aangemaakt in Discord integratie voor format en webhook URL. sync_handler.sh (Dropbox) stuurt nu zelf een notification per bestand na succesvolle sync (source: iPhone). team-inbox-watcher vereenvoudigd tot alleen direct geplaatste bestanden — Recorded Audio/ wordt overgeslagen. .partial filtering ook doorgevoerd.
