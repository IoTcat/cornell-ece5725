

import os
import sys
sys.path.append('modules/display')

import numpy as np
import RPi.GPIO as GPIO
import pygame

from screen import Screen
from ball import Ball

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

IS_QUIT = False
def cb(a):
    global IS_QUIT
    IS_QUIT = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.FALLING, callback=cb, bouncetime=300)


pygame.init()
clock = pygame.time.Clock()

screen = Screen(width = 320, height = 240)
ball = [
    Ball(speed = [2,2], radius = 50),
    Ball(speed = [1,-2], radius = 20)
]


ball[1].move([160,160])    

while not IS_QUIT:    
    clock.tick(100) 

    ball[0].move()
    ball[1].move()    

    screen.constrain(ball[0])
    screen.constrain(ball[1])



    screen.clear()
    screen << ball[0]
    screen << ball[1]
    pygame.display.flip()        # display workspace on screen

