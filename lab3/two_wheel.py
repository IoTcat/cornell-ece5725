
import time
import sys
sys.path.append('modules/gpio')

import numpy as np
from motor import Motor
from button import Button

motor = [
    Motor(IN1=5, IN2=6, PWM=26),
    Motor(IN1=20, IN2=21, PWM=16)
]

button = [Button(pin) for pin in [17, 22, 23, 27]]


button[0].func = lambda motor=motor:motor[0].setSpeed(0) if button[1].status==0 else motor[0].setSpeed(100)
button[1].func = lambda motor=motor:motor[0].setSpeed(0) if button[0].status==0 else motor[0].setSpeed(-100)
button[2].func = lambda motor=motor:motor[1].setSpeed(0) if button[3].status==0 else motor[1].setSpeed(100)
button[3].func = lambda motor=motor:motor[1].setSpeed(0) if button[2].status==0 else motor[1].setSpeed(-100)


while True:
    pass