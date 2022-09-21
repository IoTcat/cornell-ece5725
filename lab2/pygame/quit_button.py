
FPS = 100


import os
import sys
sys.path.append('modules/display')
sys.path.append('modules/gpio')
sys.path.append('modules/sys')

import numpy as np
import pygame
from pygame.locals import *   # for event MOUSE variables
from screen import Screen
from ball import Ball
from button import Button
from timeout import timeout
from text import Text
from vbutton import VButton

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')



button_quit = Button(27)

# timeout(30, button_quit.plus)


pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

screen = Screen(width = 320, height = 240)
ball = [
    Ball(speed = [2,2], radius = 50),
    Ball(speed = [1,-2], radius = 20)
]

vbutton = VButton(
    text = Text('quit'),
    position = [100, 200],
    size = (80, 40)
)

ball[1].move([160,160])    

while not button_quit.cnt:    
    print('ff')
    clock.tick(FPS) 


    ball[0].move()
    ball[1].move()

    # If two ball overlap
    if ball[0] - ball[1] < ball[0].radius + ball[1].radius:
        # Do the collidsion
        ball[0] ** ball[1]

    screen.constrain(ball[0])
    screen.constrain(ball[1])

            

    # for event in pygame.event.get():
       


    screen.clear()
    screen << ball[0]
    screen << ball[1]
    screen << vbutton
    pygame.display.flip()        # display workspace on screen

    pos = (0,0)       
    for event in pygame.event.get():        
        if(event.type is MOUSEBUTTONDOWN):            
            pos = pygame.mouse.get_pos() 
            print(event.type, " ")
            print(pygame.mouse.get_pos()) 

        elif(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 
            x,y = pos
            print(event.type, " ")
            print(pygame.mouse.get_pos())

        if (vbutton.rect.collidepoint(pos)):
            button_quit.plus()
            print(button_quit.cnt)
    print(button_quit.cnt)


