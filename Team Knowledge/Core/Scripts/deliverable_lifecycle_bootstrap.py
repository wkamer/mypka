#!/usr/bin/env python3
"""
One-time bootstrap: scan Deliverables/ and register existing artifacts
in the deliverable_lifecycle table in team-knowledge.db.

Usage:
    python deliverable_lifecycle_bootstrap.py [--db-path PATH]

Idempotent: existing rows are skipped, never overwritten.
"""

import os
import sys
import sqlite3
import argparse
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from db_helper import team_db

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
DELIVERABLES_DIR = os.path.join(BASE, 'Deliverables')

CLASSIFICATION_RULES = {
    "proposal": {
        "default_state": "ready",
        "proposed_destination": "BKM: GL or SOP update (if approved) or Reference only (if superseded)",
        "destination_domain": "core",
    },
    "execution_report": {
        "default_state": "ready",
        "proposed_destination": "BKM: project/workstream notes + agent_learnings",
        "destination_domain": "core",
    },
    "status_report": {
        "default_state": "ready",
        "proposed_destination": "Archived directly (no extraction if all-green)",
        "destination_domain": "core",
    },
    "closure_report": {
        "default_state": "ready",
        "proposed_destination": "BKM: project notes + decision record + agent_learnings",
        "destination_domain": "core",
    },
    "audit_report": {
        "default_state": "active",
        "proposed_destination": "BKM: team-knowledge.db patterns + agent_learnings (when acted on)",
        "destination_domain": "core",
    },
    "decision_record": {
        "default_state": "active",
        "proposed_destination": "BKM: team-knowledge.db decisions table",
        "destination_domain": "core",
    },
    "research_brief": {
        "default_state": "ready",
        "proposed_destination": "BKM: domain database or AGENT.md of relevant specialist",
        "destination_domain": "core",
    },
    "domain_knowledge_update": {
        "default_state": "ready",
        "proposed_destination": "BKM: AGENT.md + GL/SOP if applicable",
        "destination_domain": "core",
    },
    "triage_document": {
        "default_state": "ready",
        "proposed_destination": "Reference only (link from relevant project or GL)",
        "destination_domain": "core",
    },
}

NAME_PATTERNS = [
    ("Closure Record",            "closure_report"),
    ("Decision Record",           "decision_record"),
    ("Smoke Test",                "status_report"),
    ("Implementation Readiness",  "status_report"),
    ("Readiness Gate",            "status_report"),
    ("Test Plan",                 "status_report"),
    ("Dry-Run",                   "status_report"),
    ("Scan testcase",             "status_report"),
    ("Audit",                     "audit_report"),
    ("Graduation Candidate",      "triage_document"),
    ("Triage",                    "triage_document"),
    ("Discovery",                 "proposal"),
    ("Scope Proposal",            "proposal"),
    ("Write-List",                "proposal"),
    ("Amendment",                 "domain_knowledge_update"),
    ("Research",                  "research_brief"),
    ("architectuur",              "triage_document"),
    ("diagnose",                  "triage_document"),
    ("aanbevelingen",             "triage_document"),
    ("Blueprint",                 "domain_knowledge_update"),
    ("Schema",                    "domain_knowledge_update"),
    ("Routine",                   "domain_knowledge_update"),
    ("One-pager",                 "domain_knowledge_update"),
    ("Design",                    "proposal"),
]

DOMAIN_PATTERNS = [
    ("Personal",          "personal"),
    ("Kamer E-commerce",  "kamer-ecommerce"),
    ("Geldstroom Regie",  "geldstroom-regie"),
]


def classify(folder_name):
    artifact_type = "proposal"
    needs_review = True
    for keyword, atype in NAME_PATTERNS:
        if keyword.lower() in folder_name.lower():
            artifact_type = atype
            needs_review = False
            break

    destination_domain = "core"
    for keyword, domain in DOMAIN_PATTERNS:
        if keyword.lower() in folder_name.lower():
            destination_domain = domain
            break

    rules = CLASSIFICATION_RULES[artifact_type]
    return {
        "artifact_type": artifact_type,
        "state": rules["default_state"],
        "proposed_destination": rules["proposed_destination"],
        "destination_domain": destination_domain,
        "needs_review": needs_review,
    }


def main():
    parser = argparse.ArgumentParser(description="Bootstrap deliverable_lifecycle table")
    parser.add_argument("--db-path", default=team_db)
    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)

    subfolders = sorted(
        f for f in os.listdir(DELIVERABLES_DIR)
        if os.path.isdir(os.path.join(DELIVERABLES_DIR, f)) and f != "Archive"
    )

    registered = 0
    skipped = 0
    needs_review_list = []

    for folder in subfolders:
        existing = conn.execute(
            "SELECT id FROM deliverable_lifecycle WHERE artifact_name = ?", (folder,)
        ).fetchone()
        if existing:
            skipped += 1
            continue

        info = classify(folder)
        conn.execute("""
            INSERT INTO deliverable_lifecycle
                (artifact_name, artifact_type, state, proposed_destination,
                 destination_domain, registered_at)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        """, (
            folder,
            info["artifact_type"],
            info["state"],
            info["proposed_destination"],
            info["destination_domain"],
        ))
        registered += 1
        if info["needs_review"]:
            needs_review_list.append((folder, info["artifact_type"]))

    conn.commit()
    conn.close()

    print(f"Deliverable Lifecycle Bootstrap — {datetime.now().strftime('%Y-%m-%d')}")
    print()
    print(f"Deliverables registered: {registered}")
    print(f"Deliverables skipped (already registered): {skipped}")
    print(f"Deliverables misclassified by fallback: {len(needs_review_list)}")
    if needs_review_list:
        print()
        print("Manual review needed:")
        for folder, atype in needs_review_list:
            print(f"  - {folder}  (classified as: {atype})")
    print()
    print("Run complete. No state changes written.")


if __name__ == "__main__":
    main()
