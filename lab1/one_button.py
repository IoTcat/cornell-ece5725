#!/usr/bin/env python3
#
# Script Name : one_button.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# Created Date: 9/7/2022
# 
"""Description:
The Lab Code for ECE5725 Lab1 Week2 Step4.
A python routine displaying a message when the button 
on the PiTFT plugged at the GPIO 17 of RPi is pressed.
"""
"""Usage:
Press the button at the upper edge of PiTFT to display
a message onto the terminal.
"""
#
# Import the RPi.GPIO module for interacting with 
# RiP's GPIO
import RPi.GPIO as GPIO
# Import the standard time module for future use.
import time

# Set the RPi GPIO to broadcom numbering
GPIO.setmode(GPIO.BCM)
# Setup the GPIO 17 for the edge PiTFT button.
# The pin is pulled up to avoid the voltage floating
# at the beginning. 
# Notice: This button is Active Low!
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    # Sleep for a while so the mplayer has the idle
    # CPU resource to compute and output the video 
    # to the screen.
    time.sleep(0.2)

   # When the edge button is pressed, print the message.
    if ( not GPIO.input(17) ):
        print (" ") 
        print ("Button 17 has been pressed....")


