# ADR-001: Cloudflare Tunnel als externe toegangsmethode

**Status:** Accepted
**Datum:** 2026-05-19
**Eigenaar:** Kai

---

## Context

Het myPKA ecosysteem draait op een Raspberry Pi 5 thuis. Externe toegang tot interne services (primair n8n) is vereist voor webhook-ontvangst van externe platforms (Discord, Telegram, Meta) en voor toegang via browser buiten het thuisnetwerk.

Er zijn drie gangbare methoden voor externe toegang bij een self-hosted homelab:

1. **Port forwarding** — router-poorten openzetten en direct naar de service routeren
2. **VPN** (WireGuard, Tailscale) — versleutelde tunnel, toegang via VPN-client
3. **Cloudflare Tunnel** — uitgaande tunnel via Cloudflare-netwerk, geen open poorten vereist

---

## Beslissing

Cloudflare Tunnel (`cloudflared`) is de primaire externe toegangsmethode voor het myPKA ecosysteem.

---

## Redenering

**Port forwarding afgewezen:**
- Vereist een open poort op de router — direct aanvalsoppervlak op het thuisnetwerk
- IP-adres van de ISP is dynamisch — vereist DDNS-oplossing als extra afhankelijkheid
- Geen ingebouwde authenticatie of TLS-terminatie op het netwerkniveau

**VPN overwogen maar niet gekozen als primaire methode:**
- Geschikt voor persoonlijke toegang, niet voor webhook-ontvangst van externe systemen
- Externe platforms (Discord, Meta, Telegram) kunnen geen VPN-client gebruiken om webhooks af te leveren
- Complexer te beheren bij meerdere inkomende integratiestromen

**Cloudflare Tunnel gekozen:**
- Geen open poorten op de router — aanvalsoppervlak nul op netwerkniveau
- Cloudflare termineert TLS — automatisch geldig certificaat via Cloudflare-netwerk
- DNS beheerd via Cloudflare — consistente routering zonder DDNS
- Gratis tier volstaat voor dit gebruik
- Externe platforms kunnen webhooks afleveren op `https://n8n.kmerbase.com` zonder speciale configuratie
- Cloudflare biedt DDoS-bescherming en rate limiting als extra laag

---

## Consequenties

**Voordelen:**
- Geen open poorten op thuisrouter
- Automatische TLS zonder certificaatbeheer
- Stabiele publieke hostname ongeacht ISP-IP
- Externe webhooks werken direct

**Nadelen en beperkingen:**
- Afhankelijkheid van Cloudflare als externe partij — bij Cloudflare-storing is externe toegang niet beschikbaar
- Tunnel-configuratie bevat credential-bestand dat buiten git valt — vereist apart secrets-beheer
- Cloudflare Tunnel ondersteunt geen raw TCP (alleen HTTP/HTTPS) — services die non-HTTP protocols vereisen zijn niet via deze methode te ontsluiten

**Compenserende maatregelen:**
- Cloudflare heeft een historisch hoge uptime (>99,9%) — risico is acceptabel voor dit gebruik
- Tunnel config (`config.yml`) staat in `/etc/cloudflared/` en moet als onderdeel van de disaster recovery worden meegenomen
- Voor toekomstige non-HTTP services: WireGuard of Tailscale als aanvullende methode evalueren

---

## Referenties

- Service catalog: `Team Knowledge/Core/Integrations/service-catalog.md`
- Huidige tunnel-config: `/etc/cloudflared/config.yml`
