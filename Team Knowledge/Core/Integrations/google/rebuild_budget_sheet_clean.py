"""
rebuild_budget_sheet_clean.py — Full format-reset + rebuild "Budget 2026 — Walter Kamer"
Sheet ID: 1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg

Step 1: repeatCell over full range with default/empty format → wipes all cell formatting
Step 2: unmerge all cells
Step 3: unfreeze rows/cols
Step 4: clear content
Step 5: rebuild tabs with correct data + formatting
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_helper import sheets

SPREADSHEET_ID = "1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg"

# ── Colours ──────────────────────────────────────────────────────────────────
def rgb(r, g, b):
    return {"red": r / 255, "green": g / 255, "blue": b / 255}

DARK_BLUE   = rgb(28,  69, 135)
LIGHT_BLUE  = rgb(197, 217, 241)
LIGHT_GREEN = rgb(198, 239, 206)
LIGHT_RED   = rgb(255, 199, 206)
ACCENT_BLUE = rgb(189, 215, 238)
TOTAL_BG    = rgb(242, 242, 242)
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
# Sheet builders (identical to rebuild_budget_sheet.py)
# ─────────────────────────────────────────────────────────────────────────────

def build_dashboard_data():
    rows = []
    rows.append(row([
        cell_data("Budget 2026 — Walter Kamer", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("", bg=DARK_BLUE),
    ]))
    rows.append(row([
        cell_data("Omschrijving", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Bedrag/maand", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
    ]))
    rows.append(row([
        cell_data("Totaal Inkomsten", bold=True, bg=LIGHT_GREEN),
        cell_data("=Inkomsten!C3", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))
    rows.append(row([
        cell_data("Totaal Uitgaven", bold=True, bg=LIGHT_RED),
        cell_data("=Uitgaven!C28", bold=True, bg=LIGHT_RED, fmt=EURO_FMT),
    ]))
    rows.append(row([
        cell_data("Spaarsaldo", bold=True, bg=ACCENT_BLUE),
        cell_data("=B3-B4", bold=True, bg=ACCENT_BLUE, fmt=EURO_FMT),
    ]))
    rows.append(row([
        cell_data("Vrije ruimte", bold=True, bg=LIGHT_GREEN),
        cell_data("=B3-(B4-Uitgaven!C25)", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))
    return rows


def build_inkomsten_data():
    rows = []
    rows.append(row([
        cell_data("Categorie", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Omschrijving", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
        cell_data("Bedrag/maand", bold=True, bg=DARK_BLUE, fg=HEADER_TEXT),
    ]))
    rows.append(row([
        cell_data("Salaris"),
        cell_data("PostNL"),
        cell_data(3600.78, fmt=EURO_FMT),
    ]))
    rows.append(row([
        cell_data(""),
        cell_data("Totaal Inkomsten", bold=True, bg=LIGHT_GREEN),
        cell_data("=SUM(C2:C2)", bold=True, bg=LIGHT_GREEN, fmt=EURO_FMT),
    ]))
    return rows


def build_uitgaven_data():
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

    # 1. Get sheet metadata
    meta = api.get(spreadsheetId=SPREADSHEET_ID).execute()
    existing_sheets = {s["properties"]["title"]: s["properties"]["sheetId"]
                       for s in meta["sheets"]}
    print("Existing sheets:", list(existing_sheets.keys()))

    # 2. Ensure exactly the three required tabs exist
    desired = ["Dashboard", "Inkomsten", "Uitgaven"]
    tab_requests = []
    for title in desired:
        if title not in existing_sheets:
            tab_requests.append({"addSheet": {"properties": {"title": title}}})
    for title, sid in existing_sheets.items():
        if title not in desired:
            tab_requests.append({"deleteSheet": {"sheetId": sid}})

    if tab_requests:
        api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": tab_requests}).execute()
        print("Tabs created/deleted.")
        meta = api.get(spreadsheetId=SPREADSHEET_ID).execute()
        existing_sheets = {s["properties"]["title"]: s["properties"]["sheetId"]
                           for s in meta["sheets"]}

    sheet_ids = {title: existing_sheets[title] for title in desired}
    print("Sheet IDs:", sheet_ids)

    # ── STEP 1: Full format reset via repeatCell with default/empty format ─────
    # This is the critical step missing from the previous rebuild.
    # repeatCell with an empty userEnteredFormat and fields covering all
    # format properties resets every cell to the default state.
    reset_requests = []
    for title in desired:
        sid = sheet_ids[title]
        reset_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": sid,
                    "startRowIndex": 0,
                    "endRowIndex": 1000,
                    "startColumnIndex": 0,
                    "endColumnIndex": 26,
                },
                "cell": {
                    "userEnteredFormat": {
                        "backgroundColor": {"red": 1, "green": 1, "blue": 1},
                        "textFormat": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "foregroundColor": {"red": 0, "green": 0, "blue": 0},
                            "fontSize": 10,
                        },
                        "horizontalAlignment": "LEFT",
                        "verticalAlignment": "BOTTOM",
                        "wrapStrategy": "OVERFLOW_CELL",
                        "numberFormat": {"type": "TEXT", "pattern": ""},
                        "borders": {
                            "top":    {"style": "NONE"},
                            "bottom": {"style": "NONE"},
                            "left":   {"style": "NONE"},
                            "right":  {"style": "NONE"},
                        },
                        "padding": {
                            "top": 2, "right": 3, "bottom": 2, "left": 3
                        },
                    }
                },
                "fields": (
                    "userEnteredFormat.backgroundColor,"
                    "userEnteredFormat.textFormat,"
                    "userEnteredFormat.horizontalAlignment,"
                    "userEnteredFormat.verticalAlignment,"
                    "userEnteredFormat.wrapStrategy,"
                    "userEnteredFormat.numberFormat,"
                    "userEnteredFormat.borders,"
                    "userEnteredFormat.padding"
                ),
            }
        })

    api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": reset_requests}).execute()
    print("Format reset done (repeatCell).")

    # ── STEP 2: Unmerge all cells ─────────────────────────────────────────────
    unmerge_requests = []
    for title in desired:
        sid = sheet_ids[title]
        unmerge_requests.append({
            "unmergeCells": {
                "range": {
                    "sheetId": sid,
                    "startRowIndex": 0, "endRowIndex": 1000,
                    "startColumnIndex": 0, "endColumnIndex": 26,
                }
            }
        })
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

    api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": unmerge_requests}).execute()
    print("Unmerged all cells and unfroze rows/cols.")

    # ── STEP 3: Clear all content ─────────────────────────────────────────────
    ranges = [f"{t}!A1:Z1000" for t in desired]
    svc.spreadsheets().values().batchClear(
        spreadsheetId=SPREADSHEET_ID,
        body={"ranges": ranges}
    ).execute()
    print("Cleared existing content.")

    # ── STEP 4: Write data + formatting ──────────────────────────────────────
    tab_data = {
        "Dashboard": build_dashboard_data(),
        "Inkomsten": build_inkomsten_data(),
        "Uitgaven":  build_uitgaven_data(),
    }

    format_requests = []

    for tab_name, rows_data in tab_data.items():
        sid = sheet_ids[tab_name]

        format_requests.append({
            "updateCells": {
                "rows": rows_data,
                "fields": "userEnteredValue,userEnteredFormat",
                "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0},
            }
        })

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

    # Dashboard: merge title row A1:B1
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

    # Uitgaven: merge section header cells (rows 1, 19, 22 — 0-indexed)
    uit_id = sheet_ids["Uitgaven"]
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

    api.batchUpdate(spreadsheetId=SPREADSHEET_ID, body={"requests": format_requests}).execute()
    print("Data written and formatted.")

    print("\nDone. Sheet rebuilt: https://docs.google.com/spreadsheets/d/1H0J2ZLnBmtqXi_S97nW5mHfZaookonBesd-GDgr_iwg")


if __name__ == "__main__":
    main()
