"""
rebuild_budget_sheet.py — Rebuilds "Budget 2026 — Walter Kamer"
Sheet ID: 1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg

Clears all content and rebuilds with:
  Tab 1: Dashboard
  Tab 2: Inkomsten
  Tab 3: Uitgaven
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_helper import sheets

SPREADSHEET_ID = "1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg"

# ── Colours ──────────────────────────────────────────────────────────────────
def rgb(r, g, b):
    return {"red": r / 255, "green": g / 255, "blue": b / 255}

DARK_BLUE   = rgb(28,  69, 135)   # header rows
LIGHT_BLUE  = rgb(197, 217, 241)  # section header Vaste lasten etc.
LIGHT_GREEN = rgb(198, 239, 206)  # income / positive
LIGHT_RED   = rgb(255, 199, 206)  # expenses / negative
ACCENT_BLUE = rgb(189, 215, 238)  # spaarsaldo
TOTAL_BG    = rgb(242, 242, 242)  # subtotal / total rows
WHITE       = rgb(255, 255, 255)
HEADER_TEXT = rgb(255, 255, 255)
BLACK       = rgb(0,   0,   0)

EURO_FMT = "€#,##0.00"


def cell_data(value, bold=False, bg=None, fg=None, fmt=None, italic=False):
    ud = {}
    if fmt:
        ud["numberFormat"] = {"type": "CURRENCY", "pattern": fmt}
    cell = {"userEnteredValue": {}}
    if isinstance(value, (int, float)):
        cell["userEnteredValue"]["numberValue"] = value
    elif isinstance(value, str) and value.startswith("="):
        cell["userEnteredValue"]["formulaValue"] = value
    else:
        cell["userEnteredValue"]["stringValue"] = str(value) if value is not None else ""

    fmt_obj = {}
    if bold or fg or bg or italic:
        fmt_obj["textFormat"] = {}
        if bold:
            fmt_obj["textFormat"]["bold"] = True
        if italic:
            fmt_obj["textFormat"]["italic"] = True
        if fg:
            fmt_obj["textFormat"]["foregroundColor"] = fg
    if bg:
        fmt_obj["backgroundColor"] = bg
    if ud:
        fmt_obj.update(ud)
    if fmt_obj:
        cell["userEnteredFormat"] = fmt_obj
    return cell


def row(cells):
    return {"values": cells}


# ─────────────────────────────────────────────────────────────────────────────
# Sheet builders
# ─────────────────────────────────────────────────────────────────────────────

def build_dashboard_data():
    """
    Tab 1: Dashboard
    Columns: Omschrijving | Bedrag/maand
    Rows:    header, Totaal Inkomsten, Totaal Uitgaven, Spaarsaldo, Vrije ruimte
    """
    rows = []

    # Title row (merged later via merge request)
    rows.append(row([
        cell_data("Budget 2026 — Walter Kamer", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("", bg=DARK_BLUE),
    ]))

    # Column headers
    rows.append(row([
        cell_data("Omschrijving", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Bedrag/maand", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
    ]))

    # Totaal Inkomsten — references Inkomsten tab totaal row (row 12 = last row)
    rows.append(row([
        cell_data("Totaal Inkomsten", bold=True, bg=LIGHT_GREEN),
        cell_data("=Inkomsten!C3", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))

    # Totaal Uitgaven — references Uitgaven tab totaal
    rows.append(row([
        cell_data("Totaal Uitgaven", bold=True, bg=LIGHT_RED),
        cell_data("=Uitgaven!C28", bold=True, bg=LIGHT_RED, fmt=EURO_FMT),
    ]))

    # Spaarsaldo
    rows.append(row([
        cell_data("Spaarsaldo", bold=True, bg=ACCENT_BLUE),
        cell_data("=B3-B4", bold=True, bg=ACCENT_BLUE, fmt=EURO_FMT),
    ]))

    # Vrije ruimte (inkomsten - uitgaven excl. sparen)
    rows.append(row([
        cell_data("Vrije ruimte", bold=True, bg=LIGHT_GREEN),
        cell_data("=B3-(B4-Uitgaven!C25)", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))

    return rows


def build_inkomsten_data():
    """
    Tab 2: Inkomsten
    Columns: Categorie | Omschrijving | Bedrag/maand
    """
    rows = []

    # Column headers
    rows.append(row([
        cell_data("Categorie", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Omschrijving", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Bedrag/maand", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
    ]))

    # Data
    rows.append(row([
        cell_data("Salaris"),
        cell_data("PostNL"),
        cell_data(3600.78, fmt=EURO_FMT),
    ]))

    # Totaal
    rows.append(row([
        cell_data(""),
        cell_data("Totaal Inkomsten", bold=True, bg=LIGHT_GREEN),
        cell_data("=SUM(C2:C2)", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))

    return rows


def build_uitgaven_data():
    """
    Tab 3: Uitgaven
    Columns: Categorie | Omschrijving | Bedrag/maand

    Row layout (1-indexed):
     1  header row
     2  --- Vaste lasten section header ---
     3  Hypotheek
     4  Servicekosten
     5  Alimentatie
     6  Mobiel
     7  1Password
     8  Heptabase
     9  ChatGPT
    10  iCloud+
    11  Spotify
    12  Claude Code
    13  Zorgverzekering
    14  Uitvaartverzekering
    15  Fietsverzekering
    16  Aansprakelijkheid
    17  Reisverzekering
    18  Autoverzekering
    19  Subtotaal Vaste lasten   → SUM(C3:C18)
    20  --- Boodschappen section header ---
    21  Boodschappen
    22  Subtotaal Boodschappen   → SUM(C21:C21)
    23  --- Sparen section header ---
    24  Sparen
    25  Subtotaal Sparen         → SUM(C24:C24)
    26  (empty spacer)
    27  (empty)
    28  Totaal Uitgaven          → C19+C22+C25
    """
    rows = []

    # Row 1: headers
    rows.append(row([
        cell_data("Categorie", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Omschrijving", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Bedrag/maand", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
    ]))

    # Row 2: section header Vaste lasten
    rows.append(row([
        cell_data("Vaste lasten", bold=True, bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
    ]))

    # Rows 3–18: vaste lasten items
    vaste = [
        ("Wonen",         "Hypotheek",            1000.00),
        ("Wonen",         "Servicekosten",          250.00),
        ("Wonen",         "Alimentatie",            524.00),
        ("Abonnementen",  "Mobiel (Vodafone)",       24.60),
        ("Abonnementen",  "1Password",                5.00),
        ("Abonnementen",  "Heptabase",               13.00),
        ("Abonnementen",  "ChatGPT",                 19.01),
        ("Abonnementen",  "iCloud+",                  0.99),
        ("Abonnementen",  "Spotify",                 12.99),
        ("Abonnementen",  "Claude Code",             18.00),
        ("Verzekering",   "Zorgverzekering",        210.13),
        ("Verzekering",   "Uitvaartverzekering",     11.60),
        ("Verzekering",   "Fietsverzekering",         5.84),
        ("Verzekering",   "Aansprakelijkheid",        7.59),
        ("Verzekering",   "Reisverzekering",         15.95),
        ("Verzekering",   "Autoverzekering",         80.00),
    ]
    for cat, omschr, bedrag in vaste:
        rows.append(row([
            cell_data(cat),
            cell_data(omschr),
            cell_data(bedrag, fmt=EURO_FMT),
        ]))

    # Row 19: subtotaal vaste lasten
    rows.append(row([
        cell_data(""),
        cell_data("Subtotaal Vaste lasten", bold=True, bg=TOTAL_BG),
        cell_data("=SUM(C3:C18)", bold=True, bg=TOTAL_BG, fmt=EURO_FMT),
    ]))

    # Row 20: section header Boodschappen
    rows.append(row([
        cell_data("Boodschappen", bold=True, bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
    ]))

    # Row 21: boodschappen
    rows.append(row([
        cell_data("Boodschappen"),
        cell_data("Boodschappen"),
        cell_data(400.00, fmt=EURO_FMT),
    ]))

    # Row 22: subtotaal boodschappen
    rows.append(row([
        cell_data(""),
        cell_data("Subtotaal Boodschappen", bold=True, bg=TOTAL_BG),
        cell_data("=SUM(C21:C21)", bold=True, bg=TOTAL_BG, fmt=EURO_FMT),
    ]))

    # Row 23: section header Sparen
    rows.append(row([
        cell_data("Sparen", bold=True, bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
        cell_data("", bg=LIGHT_BLUE),
    ]))

    # Row 24: sparen
    rows.append(row([
        cell_data("Sparen"),
        cell_data("Sparen"),
        cell_data(250.00, fmt=EURO_FMT),
    ]))

    # Row 25: subtotaal sparen
    rows.append(row([
        cell_data(""),
        cell_data("Subtotaal Sparen", bold=True, bg=TOTAL_BG),
        cell_data("=SUM(C24:C24)", bold=True, bg=TOTAL_BG, fmt=EURO_FMT),
    ]))

    # Row 26: empty spacer
    rows.append(row([cell_data(""), cell_data(""), cell_data("")]))

    # Row 27: empty
    rows.append(row([cell_data(""), cell_data(""), cell_data("")]))

    # Row 28: totaal uitgaven
    rows.append(row([
        cell_data(""),
        cell_data("Totaal Uitgaven", bold=True, bg=LIGHT_RED),
        cell_data("=C19+C22+C25", bold=True, bg=LIGHT_RED, fmt=EURO_FMT),
    ]))

    return rows


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    svc = sheets()
    api = svc.spreadsheets()

    # 1. Get existing sheet metadata to find sheet IDs
    meta = api.get(spreadsheetId=SPREADSHEET_ID).execute()
    existing_sheets = {s["properties"]["title"]: s["properties"]["sheetId"]
                       for s in meta["sheets"]}
    print("Existing sheets:", list(existing_sheets.keys()))

    # 2. Build batch update requests
    requests = []

    # ── Ensure exactly three tabs exist with correct names ──────────────────
    desired = ["Dashboard", "Inkomsten", "Uitgaven"]

    for title in desired:
        if title not in existing_sheets:
            requests.append({"addSheet": {"properties": {"title": title}}})

    # Delete sheets not in desired list (keep at least one at all times —
    # Google requires ≥1 sheet, so delete only after adds)
    for title, sid in existing_sheets.items():
        if title not in desired:
            requests.append({"deleteSheet": {"sheetId": sid}})

    if requests:
        api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": requests}).execute()
        print("Tabs created/deleted.")
        # Refresh metadata
        meta = api.get(spreadsheetId=SPREADSHEET_ID).execute()
        existing_sheets = {s["properties"]["title"]: s["properties"]["sheetId"]
                           for s in meta["sheets"]}

    sheet_ids = {title: existing_sheets[title] for title in desired}
    print("Sheet IDs:", sheet_ids)

    # ── Unfreeze rows/cols + unmerge all cells in all three tabs first ───────
    unmerge_requests = []
    for title in desired:
        sid = existing_sheets[title]
        # Unfreeze rows and columns
        unmerge_requests.append({
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sid,
                    "gridProperties": {
                        "frozenRowCount": 0,
                        "frozenColumnCount": 0,
                    }
                },
                "fields": "gridProperties.frozenRowCount,gridProperties.frozenColumnCount",
            }
        })
        unmerge_requests.append({
            "unmergeCells": {
                "range": {
                    "sheetId": sid,
                    "startRowIndex": 0, "endRowIndex": 1000,
                    "startColumnIndex": 0, "endColumnIndex": 26,
                }
            }
        })
    api.batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": unmerge_requests}
    ).execute()
    print("Unmerged all cells.")

    # ── Clear all three tabs ─────────────────────────────────────────────────
    ranges = [f"{t}!A1:Z1000" for t in desired]
    svc.spreadsheets().values().batchClear(
        spreadsheetId=SPREADSHEET_ID,
        body={"ranges": ranges}
    ).execute()
    print("Cleared existing content.")

    # ── Write data ───────────────────────────────────────────────────────────
    tab_data = {
        "Dashboard": build_dashboard_data(),
        "Inkomsten": build_inkomsten_data(),
        "Uitgaven":  build_uitgaven_data(),
    }

    format_requests = []

    for tab_name, rows_data in tab_data.items():
        sid = sheet_ids[tab_name]

        # Write values + inline cell formats via updateCells
        format_requests.append({
            "updateCells": {
                "rows": rows_data,
                "fields": "userEnteredValue,userEnteredFormat",
                "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0},
            }
        })

        # Auto-resize columns A–C
        format_requests.append({
            "autoResizeDimensions": {
                "dimensions": {
                    "sheetId": sid,
                    "dimension": "COLUMNS",
                    "startIndex": 0,
                    "endIndex": 3,
                }
            }
        })

    # ── Dashboard: merge title row A1:B1 ────────────────────────────────────
    dash_id = sheet_ids["Dashboard"]
    format_requests.append({
        "mergeCells": {
            "range": {
                "sheetId": dash_id,
                "startRowIndex": 0, "endRowIndex": 1,
                "startColumnIndex": 0, "endColumnIndex": 2,
            },
            "mergeType": "MERGE_ALL",
        }
    })

    # ── Uitgaven: merge section header cells across columns ──────────────────
    uit_id = sheet_ids["Uitgaven"]
    # section header rows (0-indexed): row 1 = Vaste lasten, row 19 = Boodschappen, row 22 = Sparen
    for ri in [1, 19, 22]:
        format_requests.append({
            "mergeCells": {
                "range": {
                    "sheetId": uit_id,
                    "startRowIndex": ri, "endRowIndex": ri + 1,
                    "startColumnIndex": 0, "endColumnIndex": 3,
                },
                "mergeType": "MERGE_ALL",
            }
        })

    # ── Inkomsten: merge header cells for totaal row label ───────────────────
    # (no merge needed — totaal label is in col B, amount in col C)

    api.batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": format_requests}
    ).execute()
    print("Data written and formatted.")

    print("\nDone. Sheet rebuilt: https://docs.google.com/spreadsheets/d/1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg")


if __name__ == "__main__":
    main()
