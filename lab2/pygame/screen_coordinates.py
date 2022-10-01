#!/usr/bin/env python3
#
# Script Name : two_bounce.py
# Created By  : Yimian Liu (yl996), Zhihui Liu (zl826)
# Group Number: 7
#
FPS = 100

import time

import os
import sys
from turtle import position
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
# timeout after 30s
timeout(30, button_quit.plus)

pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

# create a screen from self-defined classes
screen = Screen(width = 320, height = 240)
# create a button from self-defined classes
vbutton = VButton(
    text = Text('quit'),
    position = [100, 200],
    size = (80, 40)
)
# create a banner with text from self-defined
banner = Text(text='', position = [160,50])

while not button_quit.cnt:    
    clock.tick(FPS) 

    # clear screen
    screen.clear()
    # draw banner and button onto the screen
    screen << banner
    screen << vbutton
    pygame.display.flip()        # display workspace on screen
    
    for event in pygame.event.get():        
        if(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 

            # print touch location on banner
            banner.text = "touch at" + str(pos)
            banner.refresh()
            # touch quit button to quit
            if (vbutton.rect.collidepoint(pos)):
                button_quit.plus()
            
    


