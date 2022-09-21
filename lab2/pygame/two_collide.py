


FPS = 100


import os
import sys
sys.path.append('modules/display')
sys.path.append('modules/gpio')

import numpy as np
import pygame

from screen import Screen
from ball import Ball
from button import Button

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')


button_quit = Button(27)


pygame.init()
clock = pygame.time.Clock()

screen = Screen(width = 320, height = 240)
ball = [
    Ball(speed = [2,2], radius = 50),
    Ball(speed = [1,-2], radius = 20)
]


ball[1].move([160,160])    

while not button_quit.cnt:    
    clock.tick(FPS) 

    ball[0].move()
    ball[1].move()

    # If two ball overlap
    if ball[0] - ball[1] < ball[0].radius + ball[1].radius:
        # Do the collidsion
        ball[0] ** ball[1]

    screen.constrain(ball[0])
    screen.constrain(ball[1])


    screen.clear()
    screen << ball[0]
    screen << ball[1]
    pygame.display.flip()        # display workspace on screen

