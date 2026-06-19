"""
Haal alle e-mails op uit Gmail label 'P - Schoolzorg Ylana' met volledige body.
Output: gesorteerd op datum (oudste eerst).
"""
import sys, os, base64
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import gmail

LABEL_NAME = '01 - PROJECTS/P - Schoolzorg Ylana'
USER = 'me'


def get_label_id(service, name):
    labels = service.users().labels().list(userId=USER).execute().get('labels', [])
    for l in labels:
        if l['name'] == name:
            return l['id']
    raise ValueError(f"Label niet gevonden: {name}")


def decode_body(part):
    data = part.get('body', {}).get('data', '')
    if data:
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
    return ''


def extract_text(payload):
    mime = payload.get('mimeType', '')
    if mime == 'text/plain':
        return decode_body(payload)
    if mime == 'text/html':
        return ''
    parts = payload.get('parts', [])
    for p in parts:
        if p.get('mimeType') == 'text/plain':
            text = decode_body(p)
            if text:
                return text
    for p in parts:
        text = extract_text(p)
        if text:
            return text
    return ''


def get_header(headers, name):
    for h in headers:
        if h['name'].lower() == name.lower():
            return h['value']
    return ''


def main():
    service = gmail()
    label_id = get_label_id(service, LABEL_NAME)
    print(f"Label ID: {label_id}", file=sys.stderr)

    messages = []
    page_token = None
    while True:
        kwargs = dict(userId=USER, labelIds=[label_id], maxResults=500)
        if page_token:
            kwargs['pageToken'] = page_token
        resp = service.users().messages().list(**kwargs).execute()
        messages.extend(resp.get('messages', []))
        page_token = resp.get('nextPageToken')
        if not page_token:
            break

    print(f"Aantal mails: {len(messages)}", file=sys.stderr)

    results = []
    for i, m in enumerate(messages):
        msg = service.users().messages().get(userId=USER, id=m['id'], format='full').execute()
        headers  = msg['payload'].get('headers', [])
        date     = get_header(headers, 'Date')
        sender   = get_header(headers, 'From')
        to       = get_header(headers, 'To')
        cc       = get_header(headers, 'Cc')
        subject  = get_header(headers, 'Subject')
        body     = extract_text(msg['payload'])
        ts       = int(msg.get('internalDate', 0))
        results.append((ts, m['id'], date, sender, to, cc, subject, body))
        print(f"  [{i+1}/{len(messages)}] {m['id']}", file=sys.stderr)

    results.sort(key=lambda x: x[0])

    for ts, mid, date, sender, to, cc, subject, body in results:
        print(f"\n{'='*60}")
        print(f"ID: {mid}")
        print(f"Datum: {date}")
        print(f"Van: {sender}")
        print(f"Aan: {to}")
        if cc:
            print(f"CC: {cc}")
        print(f"Onderwerp: {subject}")
        print(f"{'─'*40}")
        print(body.strip())


if __name__ == '__main__':
    main()
