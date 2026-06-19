# Cloudflare SSH tunnel fix ProxyCommand Windows — 2026-06-04

**Session date:** 2026-06-04
**Topics:** cloudflare,ssh,infrastructure,tunnel

## Summary

SSH verbinding naar ssh.kmerbase.com werkte niet meer na reboot Pi. Kai diagnosticeerde dat op 25 mei de cloudflared config was gewijzigd van tcp:// naar ssh:// mode, waardoor een ProxyCommand vereist werd op de client. Fix: ProxyCommand toegevoegd aan Windows SSH config van Walter. Verbinding werkt nu weer via Cloudflare tunnel.
