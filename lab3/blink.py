#!/usr/bin/env python3
#
# Script Name : blink.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 

import time
import RPi.GPIO as GPIO
from threading import Thread
import sys
sys.path.append('modules/gpio')
from button import Button


# blink frequency in Hz
freq = 1

# physical quit button
button_quit = Button(27)

GPIO.setmode(GPIO.BCM)   # Set for GPIO numbering not pin numbers...
GPIO.setup(26, GPIO.OUT) # set GPIO 26 as output to blink LED

def blink():
    global freq
    global button_quit
    # loop until quit button pressed
    while not button_quit.cnt:
        GPIO.output(26, GPIO.HIGH)
        time.sleep(.5/freq)
        GPIO.output(26, GPIO.LOW)
        time.sleep(.5/freq)

# blink program on another thread
Thread(target=blink).start()

# wait for input
while not button_quit.cnt:
    freq = float(input('New frequency = '))

GPIO.cleanup()