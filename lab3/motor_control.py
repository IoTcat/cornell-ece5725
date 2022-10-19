#!/usr/bin/env python3
#
# Script Name : motor_control.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 
import time
import sys
sys.path.append('modules/gpio')

import numpy as np
from motor import Motor

# create a motor
motor = Motor(IN1=5, IN2=6, PWM=26)

motor.speed = 0
print('stop')
time.sleep(3)
motor.speed = 50
print('clockwise 50')
time.sleep(3)
motor.speed = 100
print('clockwise 100')
time.sleep(3)


motor.speed = 0
print('stop')
time.sleep(3)
motor.speed = -50
print('count-clockwise 50')
time.sleep(3)
motor.speed = -100
print('count-clockwise 100')
time.sleep(3)

# stop motor before quit
motor.speed = 0
