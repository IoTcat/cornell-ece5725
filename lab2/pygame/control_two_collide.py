
FPS = 100

import time
START_TIME = time.time()

import os
import sys
import time
from turtle import back, position
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

start_flag = False
pause_flag = False
button_quit = Button(27)

# timeout(30, button_quit.plus)

last_click_time = 0

pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
banner = Text(text='', position = [160,50])
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

vbutton2 = VButton(
    text = Text('start'),
    position = [200, 200],
    size = (80, 40)
)

pause_button = VButton(
    text = Text('pause'),
    position = [30, 200],
    size = (60, 30)
)

fast_button = VButton(
    text = Text('fast'),
    position = [100, 200],
    size = (60, 30)
)

slow_button = VButton(
    text = Text('slow'),
    position = [170, 200],
    size = (60, 30)
)

back_button = VButton(
    text = Text('back'),
    position = [240, 200],
    size = (60, 30)
)

ball[1].move([160,160])    


while not button_quit.cnt and time.time()<START_TIME+300:    
    clock.tick(FPS) 


    if not pause_flag and start_flag:
        ball[0].move()
        ball[1].move()

    # If two ball overlap
    if ball[0] - ball[1] < ball[0].radius + ball[1].radius:
        # Do the collidsion
        ball[0] ** ball[1]

    screen.constrain(ball[0])
    screen.constrain(ball[1])
       


    screen.clear()
    if start_flag:
        screen << ball[0]
        screen << ball[1]
        screen << pause_button
        screen << slow_button
        screen << back_button
        screen << fast_button
    
    if not start_flag:
        screen << vbutton
        screen << vbutton2

    screen << banner

    
    pygame.display.flip()        # display workspace on screen

    pos = (0,0)       
    for event in pygame.event.get():        


        if(event.type is MOUSEBUTTONUP and last_click_time < time.time()-1):            
            last_click_time = time.time()
            pos = pygame.mouse.get_pos() 
            x,y = pos
            print(event.type, " ")
            print(pygame.mouse.get_pos())
            banner.text = "touch at" + str(pos)
            banner.refresh()
            print(start_flag, pause_flag)
            if (vbutton.rect.collidepoint(pos) and start_flag == False):
                button_quit.plus()
            elif (vbutton2.rect.collidepoint(pos) and start_flag == False):
                start_flag = True
            elif (pause_button.rect.collidepoint(pos) and start_flag == True and pause_flag == True):
                pause_flag = False
            elif (pause_button.rect.collidepoint(pos) and start_flag == True and pause_flag == False):
                pause_flag = True

            elif (fast_button.rect.collidepoint(pos) and start_flag == True):
                FPS = FPS + 50
            elif (slow_button.rect.collidepoint(pos) and start_flag == True):
                FPS = max(FPS-50, 5)
#                if ball.speed[0] >= 50:
#                    ball.speed[0] = ball.speed[0] - 50
#                if ball.speed[1] >= 50:
#                    ball.speed[1] = ball.speed[1] - 50
            elif (back_button.rect.collidepoint(pos) and start_flag == True):
                start_flag = False
                FPS = 100
                pause_flag = False
                print('back')
    


