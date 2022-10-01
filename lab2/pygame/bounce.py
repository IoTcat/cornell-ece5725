#!/usr/bin/env python3
#
# Script Name : bounce.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 

import os
import sys
sys.path.append('modules/display')

import numpy as np
import RPi.GPIO as GPIO
import pygame

# import self defined class
from screen import Screen
from ball import Ball

# set env var to play video on pitft
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

# FLAG for quit
IS_QUIT = False
def cb(a):
    global IS_QUIT
    IS_QUIT = True

# quit button
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.FALLING, callback=cb, bouncetime=300)


pygame.init()
clock = pygame.time.Clock()

# create a screen from self-defined screen Class
screen = Screen(width = 320, height = 240)
# create a ball instance from self-defined ball Class
ball = [
    Ball(speed = [2,2], radius = 50)
]

# loop
while not IS_QUIT:    
    # set FPS
    clock.tick(100) 

    # let ball move
    ball[0].move()
    # let ball bounce in the screen
    screen.constrain(ball[0])

    # clear screen
    screen.clear()
    # draw ball onto the screen
    screen << ball[0]
    pygame.display.flip()        # display workspace on screen

