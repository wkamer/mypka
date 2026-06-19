"""
Herstel ontbrekende formules in Expenses tab + verwijder lege artefactrij 13.
Rijen zonder formule: 3, 14-18.
Lege rij 13 verwijderen.
"""

import sys
import os
import os as _os; import sys as _sys
_sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import sheets

SHEET_ID = "1QT3MD1yvtPB3GbKINis-Bv98UBviuWZkHJHrOzYtsxY"
TAB = "Expenses"

FORMULA_F = (
    '=IF(EXPENSES[Amount]="";"";'
    'IF(EXPENSES[Period]="monthly";EXPENSES[Amount];'
    'IF(EXPENSES[Period]="quarterly";EXPENSES[Amount]/4;'
    'IF(EXPENSES[Period]="yearly";EXPENSES[Amount]/12;""))))'
)

def get_sheet_id():
    svc = sheets()
    meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    for s in meta["sheets"]:
        if s["properties"]["title"] == TAB:
            return s["properties"]["sheetId"]

def main():
    svc = sheets()
    sheet_id = get_sheet_id()

    # Rijen met ontbrekende/foutieve formules
    rows_to_fix = [3, 13, 14, 15, 16, 17]

    updates = []
    for row in rows_to_fix:
        updates.append({
            "range": f"{TAB}!F{row}",
            "values": [[FORMULA_F]]
        })
        updates.append({
            "range": f"{TAB}!G{row}",
            "values": [[f"=F{row}*1,03"]]
        })

    svc.spreadsheets().values().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": updates
        }
    ).execute()
    print(f"Formules hersteld in rijen: {rows_to_fix}")
    print("Klaar.")

if __name__ == "__main__":
    main()
