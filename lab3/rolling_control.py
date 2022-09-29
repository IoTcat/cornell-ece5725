
FPS = 100
IS_QUIT = False

import os
import sys
import time
from turtle import position
sys.path.append('modules/display')
sys.path.append('modules/gpio')
sys.path.append('modules/sys')

import numpy as np
import pygame
from pygame.locals import *   # for event MOUSE variables
from screen import Screen
from button import Button
from motor import Motor
from timeout import timeout
from text import Text
from vbutton import VButton

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

from test_queue import Test_queue

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
    color = (255,0,0),
    shape = 'ellipse'
)

log_left = Test_queue(
    title = Text('Left History'),
    position = screen%(20,50)
)
log_right = Test_queue(
    title = Text('Right History'),
    position = screen%(80,50)
)

def add_time(text, start_time = time.time()):
    return text +' ' + str(int(time.time() - start_time))


motor = [
    Motor(IN1=5, IN2=6, PWM=26,
        callback = lambda speed,log_left=log_left:log_left.push(Text(add_time('stop') if speed == 0 else add_time('clockwise') if speed > 0 else add_time('counter-clockwise'), size=15))
    ),
    Motor(IN1=20, IN2=21, PWM=16,
        callback = lambda speed,log_right=log_right:log_right.push(Text(add_time('stop') if speed == 0 else add_time('clockwise') if speed > 0 else add_time('counter-clockwise'), size=15))
    )
]

button = [Button(pin) for pin in [17, 22, 23, 27]]


button[0].func = lambda motor=motor:motor[0].setSpeed(0) if button[1].status==0 else motor[0].setSpeed(100)
button[1].func = lambda motor=motor:motor[0].setSpeed(0) if button[0].status==0 else motor[0].setSpeed(-100)
button[2].func = lambda motor=motor:motor[1].setSpeed(0) if button[3].status==0 else motor[1].setSpeed(100)
button[3].func = lambda motor=motor:motor[1].setSpeed(0) if button[2].status==0 else motor[1].setSpeed(-100)



while not (IS_QUIT or all([b.status==0 for b in button])):    
    clock.tick(FPS) 


    screen.clear()
    screen << log_left
    screen << log_right
    screen << button_quit
    screen << button_panic
    pygame.display.flip()        # display workspace on screen

    for event in pygame.event.get():        

        if(event.type is MOUSEBUTTONUP):            
            pos = pygame.mouse.get_pos() 
            if (button_quit.collidepoint(pos)):
                IS_QUIT = True
            if (button_panic.collidepoint(pos)):
                if button_panic.text.text == 'stop':
                    [m.stop() for m in motor]
                    button_panic.color = (0,255,0)
                    button_panic.text = Text('resume')
                elif button_panic.text.text == 'resume':
                    [m.resume() for m in motor]
                    button_panic.color = (255,0,0)
                    button_panic.text = Text('stop')
                button_panic.refresh()
    


    


