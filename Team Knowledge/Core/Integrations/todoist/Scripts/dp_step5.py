#!/usr/bin/env python3
"""dp_step5.py — Step 5: BPM Review."""
import sys, os, subprocess
script = os.path.join(os.path.dirname(__file__), 'dp_step1.py')
subprocess.run([sys.executable, script, '--domain', 'bpm'] + sys.argv[1:])
