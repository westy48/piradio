#!/usr/bin/python

import time
import os
import subprocess
import sys
from gpiozero import Button
from subprocess import check_call

pid = subprocess.Popen([sys.executable, "clock.py"])

def shutdown():
   check_call(['sudo', 'poweroff'])

shutdown_btn = Button(17, hold_time=3)
shutdown_btn.when_held = shutdown

# pause()

button = Button(23)

# set station to 5 live
station = 5

os.system("mpc play " + str(station))

while True:
  button.wait_for_press()
  station += 1
  # Assumes there are 7 stations
  if station > 7:
     station = 1
  os.system("mpc play "  + str(station))
  # pause to debounce - is quite long as found the buttons quite bouncy
  time.sleep(1.0)
