# GL-003 Email Setup

## Script

`Team Knowledge/Core/Scripts/send_email.py`

Gebruik (import):

```python
from send_email import send_email

send_email(
    to="adres@voorbeeld.com",        # str of list
    subject="Onderwerp",
    body_md="Markdown body",         # wordt automatisch naar HTML geconverteerd
    cc=None,                         # optioneel
    attachments=["pad/naar/bestand"] # optioneel
)
```

## Regels

- Bij ruwe input van de owner: altijd zelf structureren naar nette MD voor verzending
- Altijd tone of voice van Walter toepassen: warm, direct, nuchter, korte zinnen, geen formeel taalgebruik

- Body altijd in Markdown; wordt geconverteerd naar HTML via `markdown` library
- Headings (`#`, `##`, etc.) worden automatisch gestript
- Signature wordt automatisch toegevoegd — nooit meegeven in body
- Draft altijd tonen als plaintext codeblock voor verzending

## Signature

```
Met liefdevolle groet,

Walter Kamer
```

HTML in script (`SIGNATURE`):
```html
<br>
Met liefdevolle groet,<br>
<br>
Walter Kamer
```

## Afhankelijkheden

- `google_helper.py` — Gmail API authenticatie
- `token.json` — OAuth token (root van myPKA)
- Python package: `markdown`
