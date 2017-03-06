
import subprocess
import sys
from Adafruit_LED_Backpack import SevenSegment
from subprocess import check_call

station = 5 # Default station is 5 live
proc_Popen = subprocess.Popen(["python", "clock.py"])
segment = SevenSegment.SevenSegment(address=0x70)
