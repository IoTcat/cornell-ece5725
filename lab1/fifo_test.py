#!/usr/bin/env python3
#
# Script Name : fifo_test.py
# Created By  : Zhihui Liu (zl826), Yimian Liu (yl996)
# Group Number: 7
# Created Date: 9/7/2022
# 
"""Description:
The Lab Code for ECE5725 Lab1 Week2 Step3.
A python routine sending the pause command to the FIFO
to prove the feasibility of controlling the mplayer.
"""
"""Usage:
Input 'pause' from the keyboard followed by an Enter to
pause the mplayer.
Input 'q' from the keyboard followed by an Enter to quit 
the script.
"""
#
# Import the standard os module to interact with the shell 
import os

# A endless loop 
while True:
    # Wait for inputs from the keyboard
    str=input("Please enter the command\n")
    # When the input is 'pause', send 'pause' command 
    # to the test_fifo file
    if (str == "pause"):
        os.system('echo "pause" > test_fifo')
    # When 'q' is typed, jump out of the loop to exit the
    # script.
    if (str == 'q'):
        break


