#!/usr/bin/env python3
"""dp_step8.py — Step 8: BPM Commitment."""
import sys, os, subprocess
script = os.path.join(os.path.dirname(__file__), 'dp_step3.py')
subprocess.run([sys.executable, script, '--domain', 'bpm', '--no-fetch',
                '--step', '8', '--subtitle', 'Commitment'] + sys.argv[1:])
