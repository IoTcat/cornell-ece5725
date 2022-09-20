import pygame     # Import pygame graphics library
import os    # for OS calls
import time 
import numpy as np
from col import col

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

COL_LOCK = 0
IS_QUIT = False
def cb(a):
    global IS_QUIT
    IS_QUIT = True

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.FALLING, callback=cb, bouncetime=300)


pygame.init()

clock = pygame.time.Clock()

size = width, height = 320, 240 
speed = np.array([2,2])
speed2 = np.array([1,-2])
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball1.png")
ball = pygame.transform.scale(ball, (120, 120))
ball2 = pygame.transform.scale(ball, (60,60))
ballrect = ball.get_rect()#.inflate(-2, -2)
ballrect2 = ball2.get_rect()#.inflate(-10, -10)

ballrect2 = ballrect2.move([160,160])    

while not IS_QUIT:    
    clock.tick(100)
    ballrect = ballrect.move(speed.astype(int))    
    ballrect2 = ballrect2.move(speed2.astype(int))    

    COL_LOCK -= 1

    if COL_LOCK <= 0 and pygame.Rect.colliderect(ballrect, ballrect2):
        speed, speed2 = col({
                'v': speed,
                'r': np.array([ballrect.x, ballrect.y])
            }, {
                'v': speed2,
                'r': np.array([ballrect2.x, ballrect2.y])
            }, 3, 1)

        ballrect = ballrect.move(speed.astype(int)*5)    
        ballrect2 = ballrect2.move(speed2.astype(int)*5)    

        COL_LOCK = 10
    else:
        if ballrect.left < 0 or ballrect.right > width:        
            speed[0] = -speed[0]    
            ballrect = ballrect.move(speed*5)    
            ballrect2 = ballrect2.move(speed2*5)    
        if ballrect.top < 0 or ballrect.bottom > height:        
            speed[1] = -speed[1]
            ballrect = ballrect.move(speed*5)    
            ballrect2 = ballrect2.move(speed2*5)    
        if ballrect2.left < 0 or ballrect2.right > width:        
            speed2[0] = -speed2[0]    
            ballrect = ballrect.move(speed*5)    
            ballrect2 = ballrect2.move(speed2*5)    
        if ballrect2.top < 0 or ballrect2.bottom > height:        
            speed2[1] = -speed2[1]
            ballrect = ballrect.move(speed*5)    
            ballrect2 = ballrect2.move(speed2*5)    

    screen.fill(black)               # Erase the Work space
    screen.blit(ball, ballrect)   # Combine Ball surface with workspace surface

    screen.blit(ball2, ballrect2)   # Combine Ball surface with workspace surface
    pygame.display.flip()        # display workspace on screen

