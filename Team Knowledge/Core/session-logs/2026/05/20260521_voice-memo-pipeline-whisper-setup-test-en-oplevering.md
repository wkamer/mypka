# Voice memo pipeline — Whisper setup, test en oplevering — 2026-05-21

**Session date:** 2026-05-21
**Topics:** voice-memo,whisper,infrastructure,kai

## Summary

Onderzocht hoe voice memos via Whisper (faster-whisper, small model) lokaal getranscribeerd kunnen worden. Pipeline ontworpen en door Kai gebouwd: sync_handler.sh uitgebreid met transcribe_handler.py in eigen venv. Kai AGENT.md bijgewerkt met gedragsregel: simplest extension point first, niet standaard naar n8n. Inbox verwerkt: getranscribeerde voice memo omgezet naar Google Calendar event (kapper 15:00).
