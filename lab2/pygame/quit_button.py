#!/usr/bin/env python3
#
# Script Name : two_bounce.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
# 
FPS = 100

import os
import sys
import time

sys.path.append('modules/display')
sys.path.append('modules/gpio')
sys.path.append('modules/sys')

import numpy as np
import pygame
from pygame.locals import *   # for event MOUSE variables

# import self-defined Classes
from screen import Screen
from ball import Ball
from button import Button
from timeout import timeout
from text import Text
from vbutton import VButton

# pitft setup
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# quit button
button_quit = Button(27)

# timeout quit after 30 s
timeout(30, button_quit.plus)

pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

# create self-defined screen instance
screen = Screen(width = 320, height = 240)

# create self-defined button instance
vbutton = VButton(
    text = Text('quit'),
    position = [100, 200],
    size = (80, 40)
)

while not button_quit.cnt:    
    clock.tick(FPS) 

    # clear screen
    screen.clear()
    # draw button onto the screen
    screen << vbutton
    pygame.display.flip()        # display workspace on screen
 
    for event in pygame.event.get():        
        if(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 
            # when click button, quit
            if (vbutton.rect.collidepoint(pos)):
                button_quit.plus()


