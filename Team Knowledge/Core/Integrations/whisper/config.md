# Whisper Integration — Config

**Eigenaar:** Kai
**Laatste update:** 2026-05-21
**Status:** Actief

---

## Doel

Voice memo transcriptie. Converteert .m4a audiobestanden (afkomstig van de Dropbox sync) naar Markdown transcripten in Team Inbox. Gebruikt faster-whisper (lokale CPU inferentie — geen cloud, geen API key).

---

## Auth

Geen externe auth vereist. Whisper draait volledig lokaal.

---

## Model keuze

| Setting | Waarde | Reden |
|---|---|---|
| Model | `small` | Goede balans tussen snelheid en nauwkeurigheid op ARM64/CPU |
| Device | `cpu` | Raspberry Pi 5 heeft geen GPU |
| Language | `nl` | Primaire taal van de owner |

**Alternatieve modellen (indien nauwkeurigheid onvoldoende):**

| Model | Snelheid | Nauwkeurigheid | Aanbeveling |
|---|---|---|---|
| `tiny` | Zeer snel | Laag | Alleen voor testen |
| `base` | Snel | Redelijk | Alternatief voor low-load |
| `small` | Gemiddeld | Goed | **Huidig — aanbevolen** |
| `medium` | Langzaam | Beter | Upgrade als `small` onvoldoende |
| `large-v3` | Zeer langzaam | Beste | Alleen als Pi resources het toelaten |

Model keuze is overschrijfbaar via `WHISPER_MODEL` env var (zie .env.template).

---

## Python venv

| Pad | Doel |
|---|---|
| `/opt/whisper/venv/` | Eigen venv voor de whisper integratie |
| `/opt/whisper/venv/bin/python` | Interpreter die transcribe_handler.py gebruikt |

**Venv aanmaken (eenmalig, vereist sudo):**
```bash
sudo mkdir -p /opt/whisper
sudo chown admin:admin /opt/whisper
python3 -m venv /opt/whisper/venv
/opt/whisper/venv/bin/pip install faster-whisper
```

**Reden eigen venv:** Nooit de n8n venv (`/opt/n8n/venv/`) of memory-db venv (`/opt/mypka-memory/venv/`) gebruiken voor andere services — dependency isolatie is vereist.

---

## Gebruik

```bash
# Handmatig transcriberen
/opt/whisper/venv/bin/python \
  "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py" \
  "/pad/naar/audio.m4a"

# Output: /opt/myPKA/Team Inbox/YYYYMMDD_HHMMSS_voice-memo.md
# Logs:   /opt/myPKA/Team Knowledge/Core/Integrations/whisper/logs/transcribe.log
```

---

## Environment variables (optioneel)

| Variable | Default | Omschrijving |
|---|---|---|
| `WHISPER_MODEL` | `small` | Whisper model naam |
| `WHISPER_DEVICE` | `cpu` | Inferentie device (`cpu` of `cuda`) |
| `WHISPER_LANGUAGE` | `nl` | Taal voor transcriptie |

Stel in via `.env` in deze folder (zie `.env.template`).

---

## Integratie met Dropbox sync

`sync_handler.sh` roept `transcribe_handler.py` aan na elke succesvolle .m4a copy. Bestand wordt verwijderd (lokaal + Dropbox) **alleen na exit code 0**. Bij fout blijft het .m4a bestand staan voor handmatige retry.

---

## Logs

Locatie: `Team Knowledge/Core/Integrations/whisper/logs/transcribe.log`

Logformat: `YYYY-MM-DD HH:MM:SS  LEVEL     bericht`

---

## Crontab

Whisper heeft geen eigen crontab. Wordt aangeroepen door:
```
* * * * * /bin/bash "/opt/myPKA/Team Knowledge/Core/Integrations/dropbox/sync_handler.sh" 2>&1
```
(elke minuut, via admin crontab)
