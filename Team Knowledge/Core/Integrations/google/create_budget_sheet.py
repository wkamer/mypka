"""
create_budget_sheet.py

Creates "Budget 2026 — Walter Kamer" Google Sheet with:
  - Tab 1: Dashboard (summary formulas referencing other tabs)
  - Tab 2: Inkomsten (income per month)
  - Tab 3: Uitgaven (expenses: Vaste lasten, Boodschappen, Sparen)

Usage:
    python3 create_budget_sheet.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_helper import sheets, drive, get_credentials

SHEET_TITLE = "Budget 2026 — Walter Kamer"
OWNER_EMAIL = "wkamer@gmail.com"
YEAR = 2026

MONTHS = ["Jan", "Feb", "Mrt", "Apr", "Mei", "Jun",
          "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]

# Column letters for months: C=Jan ... N=Dec, O=Totaal
MONTH_COLS = [chr(ord('C') + i) for i in range(12)]  # C through N
TOTAL_COL = "O"


def col_range(start_row, end_row, col):
    return f"{col}{start_row}:{col}{end_row}"


def month_sum_formula(sheet_name, col, data_start, data_end):
    """SUM formula referencing a range in another sheet."""
    return f"=SUM('{sheet_name}'!{col}{data_start}:{col}{data_end})"


def create_spreadsheet(svc):
    body = {
        "properties": {"title": SHEET_TITLE},
        "sheets": [
            {"properties": {"sheetId": 0, "title": "Dashboard", "index": 0}},
            {"properties": {"sheetId": 1, "title": "Inkomsten", "index": 1}},
            {"properties": {"sheetId": 2, "title": "Uitgaven", "index": 2}},
        ]
    }
    result = svc.spreadsheets().create(body=body).execute()
    return result["spreadsheetId"], result.get("properties", {}).get("title", SHEET_TITLE)


def build_inkomsten_data():
    """
    Returns a list of (row_values) for the Inkomsten sheet.
    Layout:
      Row 1: Headers — Categorie | Omschrijving | Jan ... Dec | Totaal
      Row 2+: data rows (leave empty for user to fill)
      Last row: Totaal row
    """
    header = ["Categorie", "Omschrijving"] + MONTHS + ["Totaal jaar"]
    # 5 blank input rows
    blank_rows = [["", ""] + [""] * 13 for _ in range(5)]
    # Totaal row with SUM formulas — we'll add these via batchUpdate
    return header, blank_rows


def build_uitgaven_data():
    """
    Returns header + section rows for Uitgaven.
    Three sections: Vaste lasten, Boodschappen, Sparen
    Each section: section header row + 4 blank data rows + subtotaal row
    """
    header = ["Categorie", "Omschrijving"] + MONTHS + ["Totaal jaar"]
    sections = ["Vaste lasten", "Boodschappen", "Sparen"]
    return header, sections


def get_column_widths_request(sheet_id):
    """Set column widths: A=140, B=200, C-N=75, O=90"""
    requests = []
    # Column A (index 0) = 140
    requests.append({"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
        "properties": {"pixelSize": 140},
        "fields": "pixelSize"
    }})
    # Column B (index 1) = 200
    requests.append({"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 1, "endIndex": 2},
        "properties": {"pixelSize": 200},
        "fields": "pixelSize"
    }})
    # Columns C-N (index 2-13) = 75
    requests.append({"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 2, "endIndex": 14},
        "properties": {"pixelSize": 75},
        "fields": "pixelSize"
    }})
    # Column O (index 14) = 90
    requests.append({"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 14, "endIndex": 15},
        "properties": {"pixelSize": 90},
        "fields": "pixelSize"
    }})
    return requests


def header_format_request(sheet_id, row_index, num_cols=15):
    """Bold, grey background, centered header row."""
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_index,
                "endRowIndex": row_index + 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.85, "green": 0.85, "blue": 0.85},
                    "textFormat": {"bold": True},
                    "horizontalAlignment": "CENTER"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
        }
    }


def section_header_format_request(sheet_id, row_index, num_cols=15):
    """Bold, light blue background for section headers."""
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_index,
                "endRowIndex": row_index + 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.78, "green": 0.87, "blue": 0.95},
                    "textFormat": {"bold": True},
                    "horizontalAlignment": "LEFT"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
        }
    }


def totaal_row_format_request(sheet_id, row_index, num_cols=15):
    """Bold, slightly darker background for totaal rows."""
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_index,
                "endRowIndex": row_index + 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.75, "green": 0.75, "blue": 0.75},
                    "textFormat": {"bold": True}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    }


def currency_format_request(sheet_id, start_row, end_row, start_col=2, end_col=15):
    """Apply € currency format to amount columns."""
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": start_row,
                "endRowIndex": end_row,
                "startColumnIndex": start_col,
                "endColumnIndex": end_col
            },
            "cell": {
                "userEnteredFormat": {
                    "numberFormat": {
                        "type": "CURRENCY",
                        "pattern": "€#,##0.00"
                    }
                }
            },
            "fields": "userEnteredFormat.numberFormat"
        }
    }


def freeze_row_request(sheet_id, row_count=1, col_count=2):
    return {
        "updateSheetProperties": {
            "properties": {
                "sheetId": sheet_id,
                "gridProperties": {
                    "frozenRowCount": row_count,
                    "frozenColumnCount": col_count
                }
            },
            "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount"
        }
    }


def dashboard_highlight_format(sheet_id, row_index, num_cols=15):
    """Green highlight for spaarsaldo row."""
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_index,
                "endRowIndex": row_index + 1,
                "startColumnIndex": 0,
                "endColumnIndex": num_cols
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.72, "green": 0.88, "blue": 0.72},
                    "textFormat": {"bold": True}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    }


def main():
    svc_sheets = sheets()
    svc_drive = drive()

    print("Creating spreadsheet...")
    spreadsheet_id, _ = create_spreadsheet(svc_sheets)
    sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit"
    print(f"Created: {sheet_url}")

    # ---------------------------------------------------------------
    # Build all batch data and format requests
    # ---------------------------------------------------------------
    requests = []
    value_updates = []

    # ---------------------------------------------------------------
    # TAB: Inkomsten (sheetId=1)
    # ---------------------------------------------------------------
    ink_sheet_id = 1
    ink_header = ["Categorie", "Omschrijving"] + MONTHS + ["Totaal jaar"]
    # 5 blank data rows (rows 2-6, 0-indexed rows 1-5)
    # Totaal row at row 7 (0-indexed row 6)
    ink_data_start = 2  # 1-indexed
    ink_data_end = 6    # 1-indexed (5 rows)
    ink_totaal_row = 7  # 1-indexed

    ink_values = [ink_header]
    for _ in range(5):
        ink_values.append(["", ""] + [""] * 13)

    # Totaal row with SUM formulas for each month col + year total
    ink_totaal = ["Totaal", ""]
    for col in MONTH_COLS:
        ink_totaal.append(f"=SUM({col}{ink_data_start}:{col}{ink_data_end})")
    # Year total = sum of month totals in totaal row
    first_month_ref = f"C{ink_totaal_row}"
    last_month_ref = f"N{ink_totaal_row}"
    ink_totaal.append(f"=SUM({first_month_ref}:{last_month_ref})")
    ink_values.append(ink_totaal)

    value_updates.append({
        "range": "Inkomsten!A1",
        "values": ink_values
    })

    # Inkomsten formats
    requests += get_column_widths_request(ink_sheet_id)
    requests.append(header_format_request(ink_sheet_id, 0))
    requests.append(totaal_row_format_request(ink_sheet_id, ink_totaal_row - 1))
    requests.append(currency_format_request(ink_sheet_id, 1, ink_totaal_row))
    requests.append(freeze_row_request(ink_sheet_id))

    # ---------------------------------------------------------------
    # TAB: Uitgaven (sheetId=2)
    # ---------------------------------------------------------------
    uit_sheet_id = 2
    uit_header = ["Categorie", "Omschrijving"] + MONTHS + ["Totaal jaar"]
    sections = ["Vaste lasten", "Boodschappen", "Sparen"]
    ROWS_PER_SECTION = 4  # blank data rows per section

    uit_values = [uit_header]
    # Track row indices for section headers and subtotaal rows (1-indexed)
    section_header_rows = []   # 1-indexed
    subtotaal_rows = []        # 1-indexed
    data_ranges = []           # (start, end) 1-indexed

    current_row = 2  # 1-indexed, after header
    for section in sections:
        # Section header row
        section_header_rows.append(current_row)
        uit_values.append([section, ""] + [""] * 13)
        current_row += 1

        # Blank data rows
        data_start = current_row
        for _ in range(ROWS_PER_SECTION):
            uit_values.append(["", ""] + [""] * 13)
            current_row += 1
        data_end = current_row - 1
        data_ranges.append((data_start, data_end))

        # Subtotaal row
        subtotaal_rows.append(current_row)
        sub_row = [f"Subtotaal {section}", ""]
        for col in MONTH_COLS:
            sub_row.append(f"=SUM({col}{data_start}:{col}{data_end})")
        sub_row.append(f"=SUM(C{current_row}:N{current_row})")
        uit_values.append(sub_row)
        current_row += 1

    # Grand totaal row
    grand_totaal_row = current_row
    grand_totaal = ["Totaal Uitgaven", ""]
    for i, col in enumerate(MONTH_COLS):
        refs = "+".join([f"{col}{r}" for r in subtotaal_rows])
        grand_totaal.append(f"={refs}")
    grand_totaal.append(f"=SUM(C{grand_totaal_row}:N{grand_totaal_row})")
    uit_values.append(grand_totaal)

    value_updates.append({
        "range": "Uitgaven!A1",
        "values": uit_values
    })

    # Uitgaven formats
    requests += get_column_widths_request(uit_sheet_id)
    requests.append(header_format_request(uit_sheet_id, 0))
    for sh_row in section_header_rows:
        requests.append(section_header_format_request(uit_sheet_id, sh_row - 1))
    for st_row in subtotaal_rows:
        requests.append(totaal_row_format_request(uit_sheet_id, st_row - 1))
    requests.append(totaal_row_format_request(uit_sheet_id, grand_totaal_row - 1))
    requests.append(currency_format_request(uit_sheet_id, 1, grand_totaal_row))
    requests.append(freeze_row_request(uit_sheet_id))

    # ---------------------------------------------------------------
    # TAB: Dashboard (sheetId=0)
    # ---------------------------------------------------------------
    dash_sheet_id = 0
    dash_values = []

    # Title
    dash_values.append([f"Budget {YEAR} — Walter Kamer"] + [""] * 14)
    dash_values.append([""] * 15)  # spacer

    # Header row
    dash_values.append([""] + [""] + MONTHS + ["Totaal jaar"])

    # Totaal Inkomsten row
    inkomsten_row = []
    inkomsten_row.append("Totaal Inkomsten")
    inkomsten_row.append("")
    for col in MONTH_COLS:
        inkomsten_row.append(f"=Inkomsten!{col}{ink_totaal_row}")
    inkomsten_row.append(f"=Inkomsten!{TOTAL_COL}{ink_totaal_row}")
    dash_values.append(inkomsten_row)

    # Totaal Uitgaven row
    uitgaven_row = []
    uitgaven_row.append("Totaal Uitgaven")
    uitgaven_row.append("")
    for col in MONTH_COLS:
        uitgaven_row.append(f"=Uitgaven!{col}{grand_totaal_row}")
    uitgaven_row.append(f"=Uitgaven!{TOTAL_COL}{grand_totaal_row}")
    dash_values.append(uitgaven_row)

    # Spaarsaldo row (Inkomsten - Uitgaven)
    spaar_row = []
    spaar_row.append("Spaarsaldo")
    spaar_row.append("")
    # Dashboard rows: 1=title, 2=spacer, 3=header, 4=inkomsten, 5=uitgaven, 6=spaarsaldo
    for col in MONTH_COLS:
        spaar_row.append(f"={col}4-{col}5")
    spaar_row.append(f"={TOTAL_COL}4-{TOTAL_COL}5")
    dash_values.append(spaar_row)

    value_updates.append({
        "range": "Dashboard!A1",
        "values": dash_values
    })

    # Dashboard formats
    requests += get_column_widths_request(dash_sheet_id)

    # Title: merge A1:O1, bold, large
    requests.append({
        "mergeCells": {
            "range": {"sheetId": dash_sheet_id, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 15},
            "mergeType": "MERGE_ALL"
        }
    })
    requests.append({
        "repeatCell": {
            "range": {"sheetId": dash_sheet_id, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 15},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.23, "green": 0.47, "blue": 0.72},
                    "textFormat": {"bold": True, "fontSize": 14, "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
                    "horizontalAlignment": "CENTER",
                    "verticalAlignment": "MIDDLE"
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment,verticalAlignment)"
        }
    })
    # Header row (row 3, 0-indexed row 2)
    requests.append(header_format_request(dash_sheet_id, 2))
    # Inkomsten row (row 4, 0-indexed row 3) — blue tint
    requests.append({
        "repeatCell": {
            "range": {"sheetId": dash_sheet_id, "startRowIndex": 3, "endRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 15},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.78, "green": 0.87, "blue": 0.95},
                    "textFormat": {"bold": True}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    })
    # Uitgaven row (row 5, 0-indexed row 4) — salmon tint
    requests.append({
        "repeatCell": {
            "range": {"sheetId": dash_sheet_id, "startRowIndex": 4, "endRowIndex": 5, "startColumnIndex": 0, "endColumnIndex": 15},
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": {"red": 0.95, "green": 0.80, "blue": 0.80},
                    "textFormat": {"bold": True}
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)"
        }
    })
    # Spaarsaldo row (row 6, 0-indexed row 5) — green
    requests.append(dashboard_highlight_format(dash_sheet_id, 5))
    # Currency format for data rows (rows 4-6, 0-indexed 3-5), columns C-O
    requests.append(currency_format_request(dash_sheet_id, 3, 6))
    # Row height for title
    requests.append({
        "updateDimensionProperties": {
            "range": {"sheetId": dash_sheet_id, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 40},
            "fields": "pixelSize"
        }
    })

    # ---------------------------------------------------------------
    # Execute batch value update first (for formula references to work)
    # ---------------------------------------------------------------
    print("Writing values...")
    svc_sheets.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": value_updates
        }
    ).execute()

    # ---------------------------------------------------------------
    # Execute batch format requests
    # ---------------------------------------------------------------
    print("Applying formatting...")
    svc_sheets.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"requests": requests}
    ).execute()

    # ---------------------------------------------------------------
    # Share with wkamer@gmail.com as owner
    # ---------------------------------------------------------------
    print(f"Sharing with {OWNER_EMAIL}...")
    svc_drive.permissions().create(
        fileId=spreadsheet_id,
        body={
            "type": "user",
            "role": "owner",
            "emailAddress": OWNER_EMAIL
        },
        transferOwnership=True
    ).execute()

    print(f"\nDone.")
    print(f"Sheet URL: {sheet_url}")
    return sheet_url


if __name__ == "__main__":
    main()
