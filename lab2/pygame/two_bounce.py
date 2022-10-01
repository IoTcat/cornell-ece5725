#!/usr/bin/env python3
#
# Script Name : two_bounce.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 

import os
import sys
sys.path.append('modules/display')

import numpy as np
import RPi.GPIO as GPIO
import pygame

# self defined classes
from screen import Screen
from ball import Ball

# play on pitft
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

# flag for quit
IS_QUIT = False
def cb(a):
    global IS_QUIT
    IS_QUIT = True

# button for quit
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.FALLING, callback=cb, bouncetime=300)


pygame.init()
clock = pygame.time.Clock()

# create a screen instance from self-defined class
screen = Screen(width = 320, height = 240)
# create a self-defined ball instance
ball = [
    Ball(speed = [2,2], radius = 50),
    Ball(speed = [1,-2], radius = 20)
]

# ball move to initial position
ball[1].move([160,160])    

while not IS_QUIT:    
    # set fps
    clock.tick(100) 

    # let two ball move
    ball[0].move()
    ball[1].move()    
    # let two ball bounce in the screen
    screen.constrain(ball[0])
    screen.constrain(ball[1])

    # clear the screen
    screen.clear()
    # draw two ball onto the screen
    screen << ball[0]
    screen << ball[1]
    pygame.display.flip()        # display workspace on screen

