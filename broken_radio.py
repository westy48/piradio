#!/usr/bin/python

import time
import datetime
import os
import config
import subprocess
from time import sleep
from gpiozero import Button
from speakerphat import clear, show, set_led
from signal import pause
from subprocess import check_call

def shutdown():
    config.proc_Popen.kill()
    os.system("mpc stop")
    clear()
    config.segment.clear()
    config.segment.write_display()
    check_call(['sudo', 'poweroff'])

def retune():
    config.station += 1
    # Assumes there are 7 stations
    if config.station > 7:
        config.station = 1
    os.system("mpc play "  + str(config.station))
    # updates the Speaker pHat LEDs to show the station
    clear()
    for x in range(config.station):
        set_led(x,180)
    show()
    # stops the clock subprocess and shows the station on the 7 seg  
    config.proc_Popen.kill()
    config.segment.clear()
    config.segment.write_display()
    config.segment.set_digit(3,config.station)
    config.segment.write_display()
    time.sleep(4.0)
    config.segment.clear()
    config.segment.write_display()
    config.proc_Popen # This is the bit that's got me baffled.

shutdown_btn = Button(17, hold_time=3)
shutdown_btn.when_held = shutdown

retune_btn = Button(23)
retune_btn.when_pressed = retune

# starts clock.py
config.proc_Popen

# sets the Speaker pHat LEDS to indicate the station
clear()
for x in range(config.station):
    set_led(x,128)
show()
os.system("mpc play " + str(config.station))
pause()
