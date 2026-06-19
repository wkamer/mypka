"""
Sorteer Expenses tab: Housing eerst, Insurance daarna, rest ongewijzigd.
Zet ook Category van Hypotheek op Housing.
Herschrijft formules in F en G correct per rij.
"""

import sys
import os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import sheets

SHEET_ID = "1QT3MD1yvtPB3GbKINis-Bv98UBviuWZkHJHrOzYtsxY"
TAB = "Expenses"

FORMULA_F = (
    '=IF(EXPENSES[Amount]="";"";'
    'IF(EXPENSES[Period]="monthly";EXPENSES[Amount];'
    'IF(EXPENSES[Period]="quarterly";EXPENSES[Amount]/4;'
    'IF(EXPENSES[Period]="yearly";EXPENSES[Amount]/12;""))))'
)

CATEGORY_ORDER = ["housing", "insurance"]

def category_sort_key(row):
    cat = row[0].lower() if row else ""
    for i, c in enumerate(CATEGORY_ORDER):
        if c in cat:
            return i
    return len(CATEGORY_ORDER)

def get_sheet_id():
    svc = sheets()
    meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    for s in meta["sheets"]:
        if s["properties"]["title"] == TAB:
            return s["properties"]["sheetId"]

def main():
    svc = sheets()

    # Lees waarden (niet formules) voor data
    result = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=f"{TAB}!A:J",
        valueRenderOption="UNFORMATTED_VALUE"
    ).execute()
    all_rows = result.get("values", [])

    header = all_rows[0]       # Rij 1
    total_row = all_rows[-1]   # Laatste rij (totaal/som)
    data_rows = all_rows[1:-1] # Rijen 2 t/m 18

    # Zet Hypotheek Category op Housing
    for row in data_rows:
        if len(row) > 1 and "hypotheek" in str(row[1]).lower():
            row[0] = "Housing"
            print(f"Hypotheek Category gezet op Housing")

    # Sorteer: Housing, Insurance, dan de rest (volgorde binnen groep behouden)
    sorted_rows = sorted(data_rows, key=category_sort_key)

    print("\nNieuwe volgorde:")
    for i, row in enumerate(sorted_rows, 2):
        cat = row[0] if row else ""
        desc = row[1] if len(row) > 1 else ""
        print(f"  Rij {i}: [{cat}] {desc}")

    # Wis bestaande data (rijen 2 t/m 18, kolommen A:J)
    num_data = len(data_rows)
    clear_range = f"{TAB}!A2:J{1 + num_data}"
    svc.spreadsheets().values().clear(
        spreadsheetId=SHEET_ID,
        range=clear_range
    ).execute()
    print(f"\nData gewist: {clear_range}")

    # Schrijf gesorteerde data terug (A:E en H:J — niet F en G)
    updates = []
    for i, row in enumerate(sorted_rows):
        row_num = i + 2  # Start op rij 2

        # Pad rij tot 10 kolommen
        padded = (row + [""] * 10)[:10]

        # Schrijf A:E (kolommen 0-4)
        updates.append({
            "range": f"{TAB}!A{row_num}:E{row_num}",
            "values": [padded[0:5]]
        })
        # Schrijf H:J (kolommen 7-9)
        updates.append({
            "range": f"{TAB}!H{row_num}:J{row_num}",
            "values": [padded[7:10]]
        })
        # Schrijf formules F en G
        updates.append({
            "range": f"{TAB}!F{row_num}",
            "values": [[FORMULA_F]]
        })
        updates.append({
            "range": f"{TAB}!G{row_num}",
            "values": [[f"=F{row_num}*1,03"]]
        })

    svc.spreadsheets().values().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": updates
        }
    ).execute()
    print("Data en formules teruggeschreven.")
    print("Klaar.")

if __name__ == "__main__":
    main()
