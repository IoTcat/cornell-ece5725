
import time
import sys
sys.path.append('modules/gpio')

import numpy as np
from motor import Motor
from button import Button
import RPi.GPIO as GPIO

#motor = [
#    Motor(IN1=20, IN2=21, PWM=16),
#    Motor(IN1=5, IN2=6, PWM=26)
#]

button = [Button(pin) for pin in [17, 22, 23, 27]]

GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


def changeD(in1, in2, D):
    if D==True:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    else:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)

m1 = GPIO.PWM(16, 50)
m2 = GPIO.PWM(26, 50)

m1.start(0)
m2.start(0)

button[0].func = lambda m1=m1, m2=m2:m1.ChangeDutyCycle(0) if button[1].status==0 else (m1.ChangeDutyCycle(80) or changeD(20, 21, True))
button[1].func = lambda m1=m1, m2=m2:m1.ChangeDutyCycle(0) if button[0].status==0 else (m1.ChangeDutyCycle(80) or changeD(20, 21, False))
button[2].func = lambda m1=m1, m2=m2:m2.ChangeDutyCycle(0) if button[3].status==0 else (m2.ChangeDutyCycle(80) or changeD(5, 6, True))
button[3].func = lambda m1=m1, m2=m2:m2.ChangeDutyCycle(0) if button[2].status==0 else (m2.ChangeDutyCycle(80) or changeD(5, 6, False))
#button[1].func = lambda motor=motor:motor[0].setSpeed(0) if button[0].status==0 else motor[0].setSpeed(-100)
#button[2].func = lambda motor=motor:motor[1].setSpeed(0) if button[3].status==0 else motor[1].setSpeed(100)
#button[3].func = lambda motor=motor:motor[1].setSpeed(0) if button[2].status==0 else motor[1].setSpeed(-100)


while True:
    pass