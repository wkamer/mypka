"""
send_email.py — stuur een e-mail via Gmail API.

Body altijd als Markdown meegeven; wordt automatisch naar HTML geconverteerd.

Gebruik (import):
    from send_email import send_email
    send_email(to, subject, body_md, cc=None, bcc=None, attachments=None,
               reply_to_gmail_id=None)

    to                : str of list van adressen
    body_md           : Markdown-string
    cc                : str of list (optioneel)
    bcc               : str of list (optioneel) — niet zichtbaar voor andere ontvangers
    attachments       : list van bestandspaden (optioneel)
    reply_to_gmail_id : Gmail message-id (bijv. '19e3fc6b9b09f1b5') om in de thread
                        te antwoorden en de originele mail geciteerd mee te sturen
"""
import base64
import mimetypes
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import markdown as md
from google_helper import gmail

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<body style="font-family: sans-serif; font-size: 14px; color: #222; max-width: 600px;">
{body}
</body>
</html>
"""

SIGNATURE = """\
<br>
Met liefdevolle groet,<br>
<br>
Walter Kamer
"""

QUOTE_BLOCK = """\
<br><br>
<div style="color:#555; border-left:3px solid #ccc; padding-left:10px; margin-left:4px;">
<p style="color:#888; font-size:12px;">Op {date} schreef {sender}:</p>
{quoted_body}
</div>
"""


def _get_header(headers, name):
    for h in headers:
        if h['name'].lower() == name.lower():
            return h['value']
    return ''


def _extract_plain(payload):
    mime = payload.get('mimeType', '')
    if mime == 'text/plain':
        data = payload.get('body', {}).get('data', '')
        if data:
            return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
    if mime == 'text/html':
        return ''
    for p in payload.get('parts', []):
        if p.get('mimeType') == 'text/plain':
            text = _extract_plain(p)
            if text:
                return text
    for p in payload.get('parts', []):
        text = _extract_plain(p)
        if text:
            return text
    return ''


def send_email(
    to: str | list,
    subject: str,
    body_md: str,
    cc: str | list | None = None,
    bcc: str | list | None = None,
    attachments: list | None = None,
    reply_to_gmail_id: str | None = None,
):
    service = gmail()
    recipients = [to] if isinstance(to, str) else list(to)
    cc_list  = ([cc]  if isinstance(cc,  str) else list(cc))  if cc  else []
    bcc_list = ([bcc] if isinstance(bcc, str) else list(bcc)) if bcc else []

    clean_md = re.sub(r"^#{1,6}\s+", "", body_md, flags=re.MULTILINE)
    body_html = md.markdown(clean_md, extensions=["extra", "nl2br"]) + SIGNATURE

    thread_id = None
    if reply_to_gmail_id:
        orig = service.users().messages().get(
            userId="me", id=reply_to_gmail_id, format='full'
        ).execute()
        orig_headers  = orig['payload'].get('headers', [])
        orig_msg_id   = _get_header(orig_headers, 'Message-ID')
        orig_date     = _get_header(orig_headers, 'Date')
        orig_from     = _get_header(orig_headers, 'From')
        orig_body     = _extract_plain(orig['payload']).strip()
        thread_id     = orig.get('threadId')

        quoted_lines  = '\n'.join(f'> {l}' for l in orig_body.splitlines())
        quoted_html   = '<br>'.join(
            f'<span style="color:#555">&gt; {l}</span>'
            for l in orig_body.splitlines()
        )
        body_html += QUOTE_BLOCK.format(
            date=orig_date,
            sender=orig_from,
            quoted_body=quoted_html,
        )

    full_html = HTML_TEMPLATE.format(body=body_html)

    msg = MIMEMultipart("mixed")
    msg["to"]      = ", ".join(recipients)
    msg["subject"] = subject
    if cc_list:
        msg["cc"] = ", ".join(cc_list)
    if bcc_list:
        msg["bcc"] = ", ".join(bcc_list)
    if reply_to_gmail_id and orig_msg_id:
        msg["In-Reply-To"] = orig_msg_id
        msg["References"]  = orig_msg_id

    msg.attach(MIMEText(full_html, "html"))

    for path in (attachments or []):
        mime_type, _ = mimetypes.guess_type(path)
        main_type, sub_type = (mime_type or "application/octet-stream").split("/", 1)
        with open(path, "rb") as f:
            part = MIMEBase(main_type, sub_type)
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(path))
        msg.attach(part)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    api_body = {"raw": raw}
    if thread_id:
        api_body["threadId"] = thread_id

    result = service.users().messages().send(userId="me", body=api_body).execute()
    all_shown = recipients + cc_list + [f"BCC:{b}" for b in bcc_list]
    print(f"Sent to {', '.join(all_shown)} — id: {result['id']}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send_email.py <to> <subject> <body_md> [attachment_path ...]")
        sys.exit(1)
    to_arg = sys.argv[1].split(",")
    send_email(
        to=to_arg if len(to_arg) > 1 else to_arg[0],
        subject=sys.argv[2],
        body_md=sys.argv[3],
        attachments=sys.argv[4:] if len(sys.argv) > 4 else None,
    )
