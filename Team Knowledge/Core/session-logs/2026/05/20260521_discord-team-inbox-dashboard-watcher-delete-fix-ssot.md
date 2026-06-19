# Discord Team Inbox Dashboard — watcher, delete fix, SSOT — 2026-05-21

**Session date:** 2026-05-21
**Topics:** discord,team-inbox,watcher,infrastructure

## Summary

Fixed multiple bugs in Discord Team Inbox Dashboard: PermissionError op state file (Path.resolve), delete flow via directe REST API, Decline handler herstelt file+buttons. Team Inbox Watcher gebouwd als background asyncio task die Team Inbox folder bewaakt en button-berichten post voor alle bronnen. handle_inbox_upload vereenvoudigd. Architectuurkeuze gemaakt: watcher is SSOT voor inbox-to-Discord.
