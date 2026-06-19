"""
umc_write_summary.py — CLI wrapper for UMC write_summary.

Agents call this as their mandatory last step before returning to Larry.
Handles all boilerplate so AGENT.md instructions stay minimal.

Interpreter: /opt/mypka-memory/venv/bin/python

Usage:
    /opt/mypka-memory/venv/bin/python /opt/myPKA/Team\ Knowledge/Core/Scripts/umc_write_summary.py \
        --summary "Wat de agent heeft gedaan (1-2 zinnen)" \
        --description "Taaktitel" \
        --domain personal \
        --source-type sienna
"""

import argparse
import os
import sys

MEMORY_DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Integrations', 'memory-db')
sys.path.insert(0, os.path.abspath(MEMORY_DB_DIR))

VALID_DOMAINS = ('personal', 'kamer-ecommerce', 'geldstroom-regie', 'core')


def main():
    parser = argparse.ArgumentParser(description="Write a UMC summary for an agent task.")
    parser.add_argument('--summary', required=True, help="1-2 sentence summary of what was done")
    parser.add_argument('--description', required=True, help="Short task title")
    parser.add_argument('--domain', required=True, choices=VALID_DOMAINS)
    parser.add_argument('--source-type', required=True, help="Agent slug (e.g. sienna, penn, sasha)")
    args = parser.parse_args()

    try:
        from memory_config import get_dsn
        os.environ.setdefault('MEMORY_DB_DSN', get_dsn())
        from memory_manager import get_manager
        mm = get_manager()

        sid = mm.write_summary(
            full_content=args.summary,
            summary=args.summary,
            description=args.description,
            domain=args.domain,
            source_type=args.source_type,
        )
        print(f"UMC summary written (id={sid})")
    except Exception as e:
        print(f"⚠️ UMC niet bereikbaar: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == '__main__':
    main()
