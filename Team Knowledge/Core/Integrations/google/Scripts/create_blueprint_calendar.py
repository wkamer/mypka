"""
Create Blueprint calendar and add 6 daily recurring events for the Blueprint evening routine.
"""

import sys
import os
from datetime import datetime, date

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import calendar

EVENTS = [
    {"summary": "Blueprint: Laatste cafeïne",           "hour": 14, "minute": 0},
    {"summary": "Blueprint: Geen vloeistoffen meer",    "hour": 16, "minute": 0},
    {"summary": "Blueprint: Laatste maaltijd",           "hour": 18, "minute": 0},
    {"summary": "Blueprint: Schermen uit + wind-down",  "hour": 21, "minute": 0},
    {"summary": "Blueprint: Sleep Cycle aan",            "hour": 21, "minute": 30},
    {"summary": "Blueprint: Bed",                        "hour": 22, "minute": 0},
]

START_DATE = date(2026, 5, 30)


def main():
    svc = calendar()

    # Step 1: Create the Blueprint calendar
    calendar_body = {
        "summary": "Blueprint",
        "timeZone": "Europe/Amsterdam",
        "backgroundColor": "#0B8043",  # Google Calendar green
        "foregroundColor": "#ffffff",
    }
    new_cal = svc.calendars().insert(body=calendar_body).execute()
    calendar_id = new_cal["id"]
    print(f"Calendar created: Blueprint  (id: {calendar_id})")

    # Set the calendar color via calendarList patch
    svc.calendarList().patch(
        calendarId=calendar_id,
        body={"backgroundColor": "#0B8043", "foregroundColor": "#ffffff"},
        colorRgbFormat=True,
    ).execute()

    # Step 2: Add 6 daily recurring events
    for ev in EVENTS:
        start_dt = datetime(
            START_DATE.year, START_DATE.month, START_DATE.day,
            ev["hour"], ev["minute"], 0
        )
        end_dt = datetime(
            START_DATE.year, START_DATE.month, START_DATE.day,
            ev["hour"], ev["minute"] + 15, 0
        ) if ev["minute"] <= 44 else datetime(
            START_DATE.year, START_DATE.month, START_DATE.day,
            ev["hour"] + 1, (ev["minute"] + 15) % 60, 0
        )

        event_body = {
            "summary": ev["summary"],
            "start": {
                "dateTime": start_dt.strftime("%Y-%m-%dT%H:%M:%S"),
                "timeZone": "Europe/Amsterdam",
            },
            "end": {
                "dateTime": end_dt.strftime("%Y-%m-%dT%H:%M:%S"),
                "timeZone": "Europe/Amsterdam",
            },
            "recurrence": ["RRULE:FREQ=DAILY"],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "popup", "minutes": 5},
                ],
            },
        }

        created = svc.events().insert(calendarId=calendar_id, body=event_body).execute()
        print(f"  Event added: {ev['summary']}  {ev['hour']:02d}:{ev['minute']:02d}  (id: {created['id']})")

    print("\nDone.")


if __name__ == "__main__":
    main()
