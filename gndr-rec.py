# File: gndr-rec.py

# Author: Daniel Douglsa

# Usage: python gndr-rec <wavfile>

# Function imports
from sys import argv
from speech import Speech
import subprocess
import numpy

# Main
# Instantiate speech instance
voice = Speech(argv[1])
voice.description()

print(voice.gender(20,2))
subprocess.call(['rm', voice.wavname])