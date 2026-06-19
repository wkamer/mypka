"""
Google API helper — herbruikbare connectie voor Sheets, Gmail, Calendar en Drive.
"""

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'token.json')

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
]


def get_credentials():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def gmail():
    return build("gmail", "v1", credentials=get_credentials())


def sheets():
    return build("sheets", "v4", credentials=get_credentials())


def calendar():
    return build("calendar", "v3", credentials=get_credentials())


def drive():
    return build("drive", "v3", credentials=get_credentials())
