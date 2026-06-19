"""
Fix Income & Expenses sheet:
1. Corrigeer bedragen met punt naar komma (Fietsverzekering, Aansprakelijkheid, Doorlopende reisverzekering)
2. Verplaats Servicekosten naar rij 3 (direct na Hypotheek)
"""

import sys
import os
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import sheets

SHEET_ID = "1QT3MD1yvtPB3GbKINis-Bv98UBviuWZkHJHrOzYtsxY"
TAB = "Expenses"

def get_rows():
    svc = sheets()
    result = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=f"{TAB}!A:J"
    ).execute()
    return result.get("values", [])

def find_row(rows, description):
    for i, row in enumerate(rows):
        if len(row) > 1 and description.lower() in row[1].lower():
            return i + 1  # 1-indexed
    return None

def get_sheet_id():
    svc = sheets()
    meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    for s in meta["sheets"]:
        if s["properties"]["title"] == TAB:
            return s["properties"]["sheetId"]

def main():
    svc = sheets()
    rows = get_rows()

    # Zoek rijen
    fiets_row = find_row(rows, "Fietsverzekering")
    aansprak_row = find_row(rows, "Aansprakelijkheidsverzekering")
    doorlopend_row = find_row(rows, "Doorlopende reisverzekering")
    servicekosten_row = find_row(rows, "Servicekosten")
    hypotheek_row = find_row(rows, "Hypotheek")

    print(f"Hypotheek: rij {hypotheek_row}")
    print(f"Servicekosten: rij {servicekosten_row}")
    print(f"Fietsverzekering: rij {fiets_row}")
    print(f"Aansprakelijkheidsverzekering: rij {aansprak_row}")
    print(f"Doorlopende reisverzekering: rij {doorlopend_row}")

    # Stap 1: Fix bedragen (D kolom = kolom 4)
    fixes = [
        (fiets_row, "5,84"),
        (aansprak_row, "7,59"),
        (doorlopend_row, "15,95"),
    ]

    for row_num, amount in fixes:
        if row_num:
            svc.spreadsheets().values().update(
                spreadsheetId=SHEET_ID,
                range=f"{TAB}!D{row_num}",
                valueInputOption="USER_ENTERED",
                body={"values": [[amount]]}
            ).execute()
            print(f"Rij {row_num} Amount gecorrigeerd naar {amount}")

    # Stap 2: Verplaats Servicekosten naar rij 3 (na Hypotheek rij 2)
    # Lees de Servicekosten rij data
    sk_data = rows[servicekosten_row - 1]
    print(f"\nServicekosten data: {sk_data}")

    sheet_id = get_sheet_id()

    # cutPaste: verplaats servicekosten_row naar hypotheek_row + 1
    target_row = hypotheek_row  # 0-indexed insert point = hypotheek_row (na hypotheek)

    svc.spreadsheets().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={"requests": [{
            "cutPaste": {
                "source": {
                    "sheetId": sheet_id,
                    "startRowIndex": servicekosten_row - 1,
                    "endRowIndex": servicekosten_row,
                    "startColumnIndex": 0,
                    "endColumnIndex": 10
                },
                "destination": {
                    "sheetId": sheet_id,
                    "rowIndex": target_row,
                    "columnIndex": 0
                },
                "pasteType": "PASTE_NORMAL"
            }
        }]}
    ).execute()
    print(f"Servicekosten verplaatst naar rij {target_row + 1} (na Hypotheek).")
    print("\nFix voltooid.")

if __name__ == "__main__":
    main()
