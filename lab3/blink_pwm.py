#!/usr/bin/env python3
#
# Script Name : blink_pwm.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 

import time
import RPi.GPIO as GPIO
import sys
sys.path.append('modules/gpio')
from button import Button

# physical quit button
button_quit = Button(27)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   # Set for GPIO numbering not pin numbers...
GPIO.setup(26, GPIO.OUT) # set GPIO 13 as output to blink LED
initial_time = time.time()

dc = 50
p = GPIO.PWM(26, 1)
p.start(dc)

while not button_quit.cnt:
    frequency = int(input("Please enter a PWM frequency: "))
    p.ChangeFrequency(frequency)


p.stop()
GPIO.cleanup()