# Cron sessie-start via claude -p — 2026-06-07

**Session date:** 2026-06-07
**Topics:** cron,claude-cli,session-management,infrastructure

## Summary

Onderzocht hoe een nieuwe Claude sessie automatisch getriggerd kan worden om 02:00. Remote Trigger API bleek niet geschikt: die draait in Anthropic cloud los van het eigen abonnement. Lokale claude -p aanroep werkt wel: sessie verschijnt in het eigen claude.ai account. Cron job ingesteld op de Raspberry Pi: dagelijks 02:00, claude -p Hello World, log naar /tmp/claude-session-start.log. Remote routine trig_01C2jnzg71mDPtPwgRrEm9Gw aangemaakt maar niet de juiste aanpak.
