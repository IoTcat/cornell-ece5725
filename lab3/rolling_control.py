
FPS = 100

import os
import sys
from turtle import position
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



b0.func = lambda b=b1:print('stop') if b.status==0 else print('17')
b1.func = lambda b=b0:print('stop') if b.status==0 else print('22')

motor = [
    Motor(IN1=5, IN2=6, PWM=26),
    Motor(IN1=20, IN2=21, PWM=16)
]

button = [Button(pin) for pin in [17, 22, 23, 27]]

button[0].func = lambda motor=motor:motor[0].speed=0 if button[1].status==0 else motor[0].speed=100
button[1].func = lambda motor=motor:motor[0].speed=0 if button[0].status==0 else motor[0].speed=-100
button[2].func = lambda motor=motor:motor[1].speed=0 if button[3].status==0 else motor[1].speed=100
button[3].func = lambda motor=motor:motor[1].speed=0 if button[2].status==0 else motor[1].speed=-100



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
    position = screen%(50, 80),
    size = (80, 40)
)

banner = Text(text='', position = screen%[50,20])

ball[1].move(screen%[50,50])    
vbutton.enable = True
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

            

    # for event in pygame.event.get():
       


    screen.clear()
    screen << ball[0]
    screen << ball[1]
    screen << banner
    screen << vbutton
    pygame.display.flip()        # display workspace on screen

    pos = (0,0)       
    for event in pygame.event.get():        

        if(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 
            x,y = pos
            print(event.type, " ")
            print(pygame.mouse.get_pos())
            banner.text = "touch at" + str(pos)
            banner.refresh()
            if (vbutton.collidepoint(pos)):
                #button_quit.plus()
                ball[1].enable = not ball[1].enable
    


