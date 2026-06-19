# Runbook — Whisper Transcriptie Integratie

**Service:** whisper (voice memo transcriptie)
**Eigenaar:** Kai
**Laatste update:** 2026-05-21
**Onderdeel van pipeline:** Dropbox → Team Inbox

---

## Overzicht

```
iPhone Shortcut
  → Dropbox /Recorded Audio
    → sync_handler.sh (cron, elke minuut)
      → rclone copy → /opt/myPKA/Team Inbox/Recorded Audio/
        → transcribe_handler.py
          → /opt/myPKA/Team Inbox/YYYYMMDD_HHMMSS_voice-memo.md
          → verwijdert .m4a (lokaal + Dropbox) bij exit 0
```

---

## 1. Initiële setup (eenmalig)

### Venv aanmaken (vereist sudo)

```bash
sudo mkdir -p /opt/whisper
sudo chown admin:admin /opt/whisper
python3 -m venv /opt/whisper/venv
/opt/whisper/venv/bin/pip install --upgrade pip
/opt/whisper/venv/bin/pip install faster-whisper
```

### Verificeer installatie

```bash
/opt/whisper/venv/bin/python -c "import faster_whisper; print(faster_whisper.__version__)"
# Verwacht: 1.x.x of hoger
```

### Environment configureren (optioneel)

```bash
cp "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/.env.template" \
   "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/.env"
# Pas .env aan indien nodig
```

### Eerste model download

Het Whisper model (`small`, ~244 MB) wordt automatisch gedownload bij de eerste transcriptie. Dit vereist internetverbinding en duurt 1-3 minuten. Daarna lokaal gecached in `~/.cache/huggingface/hub/`.

Handmatig pre-downloaden:

```bash
/opt/whisper/venv/bin/python -c "
from faster_whisper import WhisperModel
model = WhisperModel('small', device='cpu')
print('Model loaded OK')
"
```

---

## 2. Handmatige transcriptie

```bash
/opt/whisper/venv/bin/python \
  "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py" \
  "/opt/myPKA/Team Inbox/Recorded Audio/opname.m4a"
```

Verwachte output (stdout): pad naar het geschreven .md bestand.
Logfile: `/opt/myPKA/Team Knowledge/Core/Integrations/whisper/logs/transcribe.log`

---

## 3. Diagnose

### Controleer recente logs

```bash
tail -50 "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/logs/transcribe.log"
```

### Controleer of venv en model bereikbaar zijn

```bash
/opt/whisper/venv/bin/python -c "from faster_whisper import WhisperModel; print('OK')"
```

### Controleer sync_handler.sh logs

```bash
tail -50 "/opt/myPKA/Team Knowledge/Core/Integrations/dropbox/logs/dropbox-recorded-audio-sync.log"
```

### Controleer welke bestanden in Recorded Audio staan

```bash
ls -la "/opt/myPKA/Team Inbox/Recorded Audio/"
```

---

## 4. Symptomen en herstel

### Symptoom: .m4a bestanden blijven staan in Recorded Audio

**Oorzaak:** Transcriptie is mislukt (exit code != 0). Het bestand is bewust bewaard.

**Diagnose:**
```bash
tail -100 "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/logs/transcribe.log" | grep -i error
```

**Herstel:**
1. Fix de fout (zie foutmelding in log)
2. Transcribeer handmatig (zie sectie 2)
3. Verwijder .m4a handmatig na succesvolle transcriptie:
   ```bash
   rm "/opt/myPKA/Team Inbox/Recorded Audio/opname.m4a"
   ```

---

### Symptoom: `ModuleNotFoundError: No module named 'faster_whisper'`

**Oorzaak:** Venv niet aangemaakt of verkeerde Python gebruikt.

**Herstel:**
```bash
# Controleer of venv bestaat
ls /opt/whisper/venv/bin/python

# Indien niet: venv opnieuw aanmaken (zie sectie 1)
# Controleer dat sync_handler.sh WHISPER_PYTHON naar /opt/whisper/venv/bin/python wijst
head -20 "/opt/myPKA/Team Knowledge/Core/Integrations/dropbox/sync_handler.sh" | grep WHISPER_PYTHON
```

---

### Symptoom: Model download mislukt (geen internet)

**Oorzaak:** Pi heeft geen internetverbinding tijdens eerste run.

**Herstel:**
1. Zorg voor internetverbinding
2. Voer handmatige model download uit (zie sectie 1)
3. Retry transcriptie

---

### Symptoom: Transcript leeg of `(geen spraak herkend)`

**Oorzaak:** Stille opname, zeer slechte audiokwaliteit, of verkeerde taalinstelling.

**Herstel:**
1. Controleer audiobestand: afspelen via Clipchamp of andere tool
2. Probeer `WHISPER_MODEL=medium` voor betere herkenning:
   ```bash
   WHISPER_MODEL=medium /opt/whisper/venv/bin/python \
     "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py" \
     "/pad/naar/audio.m4a"
   ```

---

### Symptoom: Transcriptie werkt maar in verkeerde taal

**Oorzaak:** `WHISPER_LANGUAGE` niet correct ingesteld.

**Herstel:**
```bash
WHISPER_LANGUAGE=en /opt/whisper/venv/bin/python \
  "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py" \
  "/pad/naar/audio.m4a"
```
Of pas `.env` aan.

---

## 5. Restore

De whisper integratie heeft geen eigen data store. Herstel bestaat uit:

1. Venv opnieuw aanmaken: zie sectie 1
2. Script terugplaatsen uit git/backup:
   ```
   /opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py
   ```
3. sync_handler.sh controleren op WHISPER_PYTHON en TRANSCRIBE variabelen

---

## 6. Verificatie na herstel

```bash
# Maak een test .m4a (of gebruik een bestaand bestand)
/opt/whisper/venv/bin/python \
  "/opt/myPKA/Team Knowledge/Core/Integrations/whisper/transcribe_handler.py" \
  "/pad/naar/test.m4a"
echo "Exit code: $?"
# Verwacht: 0

# Controleer output in Team Inbox
ls -la "/opt/myPKA/Team Inbox/"*voice-memo.md 2>/dev/null | tail -3
```

---

## 7. Afhankelijkheden

| Component | Versie | Status |
|---|---|---|
| faster-whisper | 1.x+ | Vereist |
| Python | 3.x (system) | Aanwezig |
| /opt/whisper/venv | - | Handmatig aanmaken bij deploy |
| sync_handler.sh | - | Uitgebreid met transcriptie-aanroep |
| rclone | - | Aanwezig (Dropbox sync) |

---

## 8. Configuratie referenties

- Config: `Team Knowledge/Core/Integrations/whisper/config.md`
- Handler: `Team Knowledge/Core/Integrations/whisper/transcribe_handler.py`
- Logs: `Team Knowledge/Core/Integrations/whisper/logs/transcribe.log`
- Dropbox sync logs: `Team Knowledge/Core/Integrations/dropbox/logs/dropbox-recorded-audio-sync.log`
