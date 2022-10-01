#!/usr/bin/env python3
#
# Script Name : more_video_control_perf.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 


import time
t = time.time()

# Import the RPi.GPIO module for interacting with 
# RiP's GPIO
import RPi.GPIO as GPIO
# Import the standard time module for future use
import time
# import the standard os module to interact with shell
import os


# Declare the GPIOs that the button will use.
buttons = [17, 22, 23, 27, 19, 26]

# Set the RPi GPIO to broadcom numbering
GPIO.setmode(GPIO.BCM)
# Setup the GPIO for the each PiTFT button.
# All the pins are pulled up to avoid the voltage floating
# at the beginning. 
# Notice: These buttons are Active Low!
for button in buttons:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if time.time() > t+10:
        os.system('echo "quit" > test_fifo')
        exit()
    # Sleep for a while so the mplayer has the idle
    # CPU resource to compute and output the video 
    # to the screen.
    #time.sleep(0.00002)
    for button in buttons:
        # When a button is pressed (Logical Low), do...
        if ( not GPIO.input(button) ):
            # Print the corresponding message
            print (" ") 
            print ("Button "+ str(button) +" has been pressed....")
            # When the first button is pressed, send 'pause' to FIFO
            if button == buttons[0]:
                os.system('echo "pause" > test_fifo')
            # When the second button is pressed, send 'seek 10' to FIFO
            if button == buttons[1]:
                os.system('echo "seek 10" > test_fifo')
            # When the third button is pressed, send 'seek -10' to FIFO
            if button == buttons[2]:
                os.system('echo "seek -10" > test_fifo')
            # When the fourth button is pressed, send 'quit' to FIFO, and 
            # quit the python script
            if button == buttons[3]:
                os.system('echo "quit" > test_fifo')
                exit()
            if button == buttons[4]:
                os.system('echo "seek 30" > test_fifo')
            if button == buttons[5]:
                os.system('echo "seek -30" > test_fifo')
