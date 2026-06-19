"""
Google API authenticatie voor Sheets, Gmail en Calendar.
Eerste run toont een URL — open die in je browser, geef toestemming, plak de code terug.
Daarna werkt het automatisch via token.json.

Gebruik:
    python google_auth.py
"""

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
]

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CREDENTIALS_FILE = os.path.join(BASE, 'client_secret.json')
TOKEN_FILE = os.path.join(BASE, 'token.json')


def authenticate():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None
        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            flow.redirect_uri = 'http://localhost'
            auth_url, _ = flow.authorization_url(access_type='offline', prompt='consent')
            print('\nOpen deze URL in je browser:')
            print(auth_url)
            print('\nNa het klikken op "Allow" word je doorgestuurd naar localhost.')
            print('Die pagina laadt niet — dat is normaal.')
            print('Kopieer de volledige URL uit de adresbalk en plak hem hier.')
            redirect_response = input('\nVolledige redirect URL: ').strip()
            flow.fetch_token(authorization_response=redirect_response)
            creds = flow.credentials

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    print("Authenticatie geslaagd.")
    print(f"Token opgeslagen in: {TOKEN_FILE}")
    return creds


if __name__ == "__main__":
    authenticate()
