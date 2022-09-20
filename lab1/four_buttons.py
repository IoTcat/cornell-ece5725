#!/usr/bin/env python3
#
# Script Name : four_button.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# Created Date: 9/7/2022
# 
"""Description:
The Lab Code for ECE5725 Lab1 Week2 Step5.
A python routine displaying a message when any button 
on the PiTFT is pressed.
"""
"""Usage:
Press the button at the upper edge of PiTFT to display
a message onto the terminal and quit.
Press any other buttons to display the corresponding
message.
"""
#
# Import the RPi.GPIO module for interacting with 
# RiP's GPIO
import RPi.GPIO as GPIO
# Import the standard time module for future use.
import time

# Declare the GPIOs that the button will use.
buttons = [17, 22, 23, 27]

# Set the RPi GPIO to broadcom numbering
GPIO.setmode(GPIO.BCM)
# Setup the GPIO for the each PiTFT button.
# All the pins are pulled up to avoid the voltage floating
# at the beginning. 
# Notice: These buttons are Active Low!
for button in buttons:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # Sleep for a while so the mplayer has the idle
    # CPU resource to compute and output the video 
    # to the screen.
    time.sleep(0.2)

    for button in buttons:
        # When a button is pressed (Logical Low), do...
        if ( not GPIO.input(button) ):
            # Print the corresponding message
            print (" ") 
            print ("Button "+ str(button) +" has been pressed....")
            # If the upper edge button is pressed, exit the python script
            if button == 17:
                exit()



