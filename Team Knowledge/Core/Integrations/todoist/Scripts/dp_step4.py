#!/usr/bin/env python3
"""dp_step4.py — Step 4: PPM Commitment."""
import sys, os, subprocess
script = os.path.join(os.path.dirname(__file__), 'dp_step3.py')
subprocess.run([sys.executable, script, '--domain', 'ppm', '--no-fetch',
                '--step', '4', '--subtitle', 'Commitment'] + sys.argv[1:])
