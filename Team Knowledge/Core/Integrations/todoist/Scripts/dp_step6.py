#!/usr/bin/env python3
"""dp_step6.py — Step 6: BPM Goals & Projects."""
import sys, os, subprocess
script = os.path.join(os.path.dirname(__file__), 'dp_step2.py')
subprocess.run([sys.executable, script, '--domain', 'bpm'] + sys.argv[1:])
