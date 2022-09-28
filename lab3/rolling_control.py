
FPS = 100
QUIT = False

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
from button import Button
from timeout import timeout
from text import Text
from vbutton import VButton

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')


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

button_quit = VButton(
    text = Text('quit'),
    position = screen%(50, 80),
    size = (80, 40)
)
button_panic = VButton(
    text = Text('stop'),
    position = screen%(50, 20),
    size = (80, 40),
    color = (255,0,0)
)

banner = Text(text='', position = screen%[50,20])

while not (QUIT or all([b.status==0 for b in button])):    
    clock.tick(FPS) 



    screen.clear()
    screen << button_quit
    screen << button_panic
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
            if (button_quit.collidepoint(pos)):
                QUIT = True
            if (button_panic.collidepoint(pos)):
                if button_panic.color == (255,0,0)
                    button_panic.color = (0,255,0)
                elif button_panic.color == (0,255,0)
                    button_panic.color = (255,0,0)
                button_panic.refresh()
    



                button_panic.refresh()
    


