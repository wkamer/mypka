#!/usr/bin/env python3
"""
generate_deliverable_index.py

Reads non-archived entries from deliverable_lifecycle, scans Deliverables/,
groups by workstream_code, and writes INDEX.md.

Usage: python3 generate_deliverable_index.py
"""

import sqlite3
import os
from datetime import datetime, timezone

# --- Config ---
DB_PATH = '/opt/myPKA/Team Knowledge/team-knowledge.db'
DELIVERABLES_DIR = '/opt/myPKA/Deliverables'
INDEX_PATH = '/opt/myPKA/Deliverables/INDEX.md'

# State display labels
STATE_LABELS = {
    'active': 'Active',
    'parked': 'Parked',
    'deferred': 'Deferred',
    'accepted_as_done': 'Done',
    'pending_lifecycle_decision': 'Awaiting lifecycle review',
    'archived': None,  # excluded from INDEX
    None: 'State unknown',
    '': 'State unknown',
}

def get_columns(conn, table):
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return [r[1] for r in rows]

def fetch_registry(conn):
    cols = get_columns(conn, 'deliverable_lifecycle')
    has_owner_decision = 'owner_decision' in cols
    has_created_at = 'registered_at' in cols

    select_cols = ['id', 'artifact_name', 'artifact_type', 'state_gl017', 'workstream_code']
    if has_owner_decision:
        select_cols.append('owner_decision')
    else:
        select_cols.append("NULL as owner_decision")

    if has_created_at:
        select_cols.append('registered_at')
    else:
        select_cols.append("NULL as registered_at")

    sql = f"""
        SELECT {', '.join(select_cols)}
        FROM deliverable_lifecycle
        WHERE (state_gl017 IS NULL OR state_gl017 != 'archived')
          AND state != 'archived'
        ORDER BY workstream_code, artifact_name
    """
    rows = conn.execute(sql).fetchall()
    result = []
    for r in rows:
        result.append({
            'id': r[0],
            'artifact_name': r[1],
            'artifact_type': r[2],
            'state_gl017': r[3],
            'workstream_code': r[4],
            'owner_decision': r[5],
            'registered_at': r[6],
        })
    return result

def scan_deliverables_dir():
    subfolders = set()
    try:
        for entry in os.scandir(DELIVERABLES_DIR):
            if entry.is_dir() and entry.name != 'Archive':
                subfolders.add(entry.name)
    except FileNotFoundError:
        pass
    return subfolders

def is_decision_pending(row):
    """Flag: owner_decision IS NULL and state warrants a decision and artifact_type is actionable."""
    decision_states = ('active', 'pending_lifecycle_decision')
    actionable_types = ('proposal', 'assessment', 'write_list', 'triage_document')
    return (
        row['owner_decision'] is None
        and row['state_gl017'] in decision_states
        and row['artifact_type'] in actionable_types
    )

def is_archive_candidate(row):
    """Flag: state is accepted_as_done and registered more than 14 days ago."""
    if row['state_gl017'] != 'accepted_as_done':
        return False
    if not row['registered_at']:
        return False
    try:
        # registered_at may be 'YYYY-MM-DD HH:MM:SS' or ISO format
        reg_str = row['registered_at'].replace('T', ' ').split('.')[0]
        reg_dt = datetime.strptime(reg_str, '%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        return (now - reg_dt).days >= 14
    except (ValueError, AttributeError):
        return False

def format_row(row, in_deliverables):
    name = row['artifact_name']
    state = row['state_gl017']
    state_label = STATE_LABELS.get(state, 'State unknown')
    atype = row['artifact_type'] or ''
    flags = []
    if is_decision_pending(row):
        flags.append('DECISION PENDING')
    if is_archive_candidate(row):
        flags.append('ARCHIVE CANDIDATE')
    present_marker = '' if in_deliverables else ' *(folder missing)*'
    flag_str = (' — **' + ', '.join(flags) + '**') if flags else ''
    return f"- {name}{present_marker} | {state_label} | {atype}{flag_str}"

def build_index(registry_rows, deliverables_folders):
    # Group by workstream_code; None → Standalone
    groups = {}
    for row in registry_rows:
        code = row['workstream_code'] or 'Standalone'
        groups.setdefault(code, []).append(row)

    # Build INDEX content
    lines = []
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    lines.append(f"# Deliverables Index")
    lines.append(f"")
    lines.append(f"*Generated: {now_str}*")
    lines.append(f"")

    # Counters for summary
    total_active = 0
    pending_decisions = 0
    archive_candidates = 0
    total_listed = 0

    # Ordered: known codes first, then Standalone
    known_order = ['DLH', 'GG', 'UMC', 'AUDIT', 'Standalone']
    all_codes = known_order + [c for c in sorted(groups.keys()) if c not in known_order]

    for code in all_codes:
        if code not in groups:
            continue
        rows = groups[code]
        section_title = f"## Workstream: {code}" if code != 'Standalone' else "## Standalone (no workstream)"
        lines.append(section_title)
        lines.append("")
        for row in rows:
            in_dir = row['artifact_name'] in deliverables_folders
            lines.append(format_row(row, in_dir))
            total_listed += 1
            if row['state_gl017'] == 'active':
                total_active += 1
            if is_decision_pending(row):
                pending_decisions += 1
            if is_archive_candidate(row):
                archive_candidates += 1
        lines.append("")

    # Unregistered: folders on disk not in registry
    registered_names = {r['artifact_name'] for r in registry_rows}
    # Also include archived entries (excluded from registry_rows) to avoid flagging them as unregistered
    conn = sqlite3.connect(DB_PATH)
    all_registered = {r[0] for r in conn.execute("SELECT artifact_name FROM deliverable_lifecycle").fetchall()}
    conn.close()
    unregistered = sorted(deliverables_folders - all_registered)
    unregistered_count = len(unregistered)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Count |")
    lines.append(f"|---|---|")
    lines.append(f"| Total listed (non-archived) | {total_listed} |")
    lines.append(f"| Active | {total_active} |")
    lines.append(f"| Pending lifecycle decisions | {pending_decisions} |")
    lines.append(f"| Archive candidates | {archive_candidates} |")
    lines.append(f"| Unregistered folders | {unregistered_count} |")
    lines.append("")

    if unregistered:
        lines.append("### Unregistered folders")
        lines.append("")
        for name in unregistered:
            lines.append(f"- {name}")
        lines.append("")

    summary_line = (
        f"Summary: {total_listed} listed | {total_active} active | "
        f"{pending_decisions} pending decisions | {archive_candidates} archive candidates | "
        f"{unregistered_count} unregistered"
    )
    return '\n'.join(lines), summary_line

def main():
    conn = sqlite3.connect(DB_PATH)
    registry_rows = fetch_registry(conn)
    conn.close()

    deliverables_folders = scan_deliverables_dir()
    index_content, summary_line = build_index(registry_rows, deliverables_folders)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"INDEX.md written to {INDEX_PATH}")
    print(summary_line)

if __name__ == '__main__':
    main()
