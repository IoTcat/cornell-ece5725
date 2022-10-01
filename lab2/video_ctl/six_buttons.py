#!/usr/bin/env python3
#
# Script Name : six_buttons.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 
#
import RPi.GPIO as GPIO
import time

buttons = [17, 22, 23, 27, 19, 26]


GPIO.setmode(GPIO.BCM)   # Set for broadcom numbering not board numbers...
# setup piTFT buttons
#                        V need this so that button doesn't 'float'!
#                        V   When button NOT pressed, this guarantees 
#                        V             signal = logical 1 = 3.3 Volts
for button in buttons:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.2)  # Without sleep, no screen output!
    for button in buttons:
        if ( not GPIO.input(button) ):
            print (" ") 
            print ("Button "+ str(button) +" has been pressed....")
            if button == 17:
                exit()
