import sys
import os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import calendar

def main():
    event_id = sys.argv[1]
    cal = calendar()
    cal.events().delete(calendarId='primary', eventId=event_id).execute()
    print(f"Deleted: {event_id}")

if __name__ == '__main__':
    main()
