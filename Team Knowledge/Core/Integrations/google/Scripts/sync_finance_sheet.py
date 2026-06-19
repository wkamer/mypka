"""
Sync KE-Finance data.md → Income & Expenses sheet (Expenses tab).
Sheet ID: 1QT3MD1yvtPB3GbKINis-Bv98UBviuWZkHJHrOzYtsxY

Wijzigingen:
- Hypotheek Amount: €1,250 → €1,000
- Toevoegen: Servicekosten, Claude Code, Fietsverzekering, Aansprakelijkheidsverzekering,
             Doorlopende reisverzekering, Autoverzekering
"""

import sys
import os
import os as _os; import sys as _sys
_sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from google_helper import sheets

SHEET_ID = "1QT3MD1yvtPB3GbKINis-Bv98UBviuWZkHJHrOzYtsxY"
EXPENSES_TAB = "Expenses"

def get_expenses():
    svc = sheets()
    result = svc.spreadsheets().values().get(
        spreadsheetId=SHEET_ID,
        range=f"{EXPENSES_TAB}!A:J"
    ).execute()
    return result.get("values", [])

def find_row(rows, description):
    for i, row in enumerate(rows):
        if any(description.lower() in str(cell).lower() for cell in row):
            return i + 1  # 1-indexed
    return None

def main():
    svc = sheets()
    rows = get_expenses()

    print("=== Huidige Expenses tab ===")
    for i, row in enumerate(rows, 1):
        print(f"{i}: {row}")

    # Zoek Hypotheek rij
    hypotheek_row = find_row(rows, "Hypotheek")
    print(f"\nHypotheek gevonden op rij: {hypotheek_row}")

    if hypotheek_row is None:
        print("FOUT: Hypotheek rij niet gevonden.")
        return

    # Vind Amount kolom index in Hypotheek rij (kolom D = index 3)
    # Huidig: Hypotheek,€ 1.250,00,monthly,...
    # Kolommen: A=Category, B=Description, C=Payee, D=Amount, E=Period, F=Monthly, G=Monthly+3%, H=50-30-20, I=Payment method, J=Bank
    # Maar de rij lijkt: Description alleen, geen category/payee
    # Laten we de exacte positie zien
    hyp_row_data = rows[hypotheek_row - 1]
    print(f"Hypotheek rij data: {hyp_row_data}")

    # Update Hypotheek Amount naar 1000
    # Zoek in welke kolom het bedrag staat
    amount_col = None
    for j, cell in enumerate(hyp_row_data):
        if "1.250" in str(cell) or "1250" in str(cell):
            amount_col = j
            break

    if amount_col is None:
        print("FOUT: Amount kolom voor Hypotheek niet gevonden.")
        return

    col_letter = chr(ord('A') + amount_col)
    range_ref = f"{EXPENSES_TAB}!{col_letter}{hypotheek_row}"
    print(f"\nUpdate Hypotheek Amount: {range_ref} -> 1.000,00")

    svc.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=range_ref,
        valueInputOption="USER_ENTERED",
        body={"values": [["1000"]]}
    ).execute()
    print("Hypotheek bijgewerkt.")

    # Zoek de totaalrij (lege rij met alleen een somformule — rij 13)
    total_row = None
    for i, row in enumerate(rows):
        # Totaalrij heeft geen Description maar wel een bedrag
        if row and row[0] == "" and len(row) > 5 and "," in str(row[5]):
            if not any(c.isalpha() for c in str(row[1])):
                total_row = i + 1
                break

    if total_row is None:
        total_row = len(rows) + 1  # Fallback: onderaan

    print(f"Totaalrij op rij: {total_row} — nieuwe rijen worden daarvoor ingevoegd")

    # Nieuwe rijen invoegen via batchUpdate insertDimension + values update
    sheet_meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
    sheet_id = None
    for s in sheet_meta["sheets"]:
        if s["properties"]["title"] == EXPENSES_TAB:
            sheet_id = s["properties"]["sheetId"]
            break

    new_rows = [
        ["Housing", "Servicekosten", "n/a", "250", "monthly", "", "", "Needs", "", ""],
        ["Subscriptions and memberships", "Claude Code", "n/a", "18", "monthly", "", "", "Wants", "credit card", "bunq"],
        ["Insurance", "Fietsverzekering", "Unive", "5.84", "monthly", "", "", "Needs", "direct debit", "bunq"],
        ["Insurance", "Aansprakelijkheidsverzekering", "Unive", "7.59", "monthly", "", "", "Needs", "direct debit", "bunq"],
        ["Insurance", "Doorlopende reisverzekering", "Unive", "15.95", "monthly", "", "", "Needs", "direct debit", "bunq"],
        ["Insurance", "Autoverzekering", "Unive", "80", "monthly", "", "", "Needs", "direct debit", "bunq"],
    ]

    insert_at = total_row - 1  # 0-indexed voor insertDimension

    # Stap 1: rijen invoegen
    svc.spreadsheets().batchUpdate(
        spreadsheetId=SHEET_ID,
        body={"requests": [{
            "insertDimension": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "ROWS",
                    "startIndex": insert_at,
                    "endIndex": insert_at + len(new_rows)
                },
                "inheritFromBefore": True
            }
        }]}
    ).execute()

    # Stap 2: waarden schrijven
    range_write = f"{EXPENSES_TAB}!A{insert_at + 1}:J{insert_at + len(new_rows)}"
    svc.spreadsheets().values().update(
        spreadsheetId=SHEET_ID,
        range=range_write,
        valueInputOption="USER_ENTERED",
        body={"values": new_rows}
    ).execute()

    print(f"{len(new_rows)} nieuwe rijen ingevoegd op rij {insert_at + 1}.")
    print("Sync voltooid.")

if __name__ == "__main__":
    main()
