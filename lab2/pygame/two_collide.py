#!/usr/bin/env python3
#
# Script Name : two_bounce.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 
# fps for animation
FPS = 100

import os
import sys
sys.path.append('modules/display')
sys.path.append('modules/gpio')

import numpy as np
import pygame

# import self defined classes
from screen import Screen
from ball import Ball
from button import Button

# play on pitft
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

# quit button
button_quit = Button(27)

pygame.init()
clock = pygame.time.Clock()

# create self-defined screen instance
screen = Screen(width = 320, height = 240)
# create two self-defined ball
ball = [
    Ball(speed = [2,2], radius = 50),
    Ball(speed = [1,-2], radius = 20)
]

# ball move to intial position
ball[1].move([160,160])    

while not button_quit.cnt:    
    clock.tick(FPS) 

    # ball move
    ball[0].move()
    ball[1].move()

    # If two ball overlap
    if ball[0] - ball[1] < ball[0].radius + ball[1].radius:
        # Do the collidsion
        ball[0] ** ball[1]

    # ball bounce in the screen
    screen.constrain(ball[0])
    screen.constrain(ball[1])

    # clear screen
    screen.clear()
    # draw balls onto the screen
    screen << ball[0]
    screen << ball[1]
    pygame.display.flip()        # display workspace on screen

