#!/usr/bin/env python3
#
# Script Name : two_wheel.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 
import time
import sys
sys.path.append('modules/gpio')

import numpy as np
from motor import Motor
from button import Button

# create two motors
motor = [
    Motor(IN1=5, IN2=6, PWM=26),
    Motor(IN1=20, IN2=21, PWM=16)
]

# create four buttons
button = [Button(pin) for pin in [17, 22, 23, 27]]

# for motor 0, button 0 to clockwise, button 1 to counter-clockwise, press both to stop
button[0].func = lambda motor=motor:motor[0].setSpeed(0) if button[1].status==0 else motor[0].setSpeed(100)
button[1].func = lambda motor=motor:motor[0].setSpeed(0) if button[0].status==0 else motor[0].setSpeed(-100)

# for motor 1, button 2 to clockwise, button 3 to counter-clockwise, press both to stop
button[2].func = lambda motor=motor:motor[1].setSpeed(0) if button[3].status==0 else motor[1].setSpeed(100)
button[3].func = lambda motor=motor:motor[1].setSpeed(0) if button[2].status==0 else motor[1].setSpeed(-100)

# block to avoid script quit
while True:
    pass