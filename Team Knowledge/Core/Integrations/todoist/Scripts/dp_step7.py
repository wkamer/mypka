#!/usr/bin/env python3
"""dp_step7.py — Step 7: BPM Plan."""
import sys, os, subprocess
script = os.path.join(os.path.dirname(__file__), 'dp_step3.py')
subprocess.run([sys.executable, script, '--domain', 'bpm'] + sys.argv[1:])
