import pygame     # Import pygame graphics library
import os    # for OS calls
import time 

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')

IS_QUIT = False
def cb(a):
    global IS_QUIT
    IS_QUIT = True

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.FALLING, callback=cb, bouncetime=300)


pygame.init()

size = width, height = 320, 240 
speed = [2,2] 
speed2 = [1,-2] 
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball1.png")
ball2 = pygame.image.load("ball1.png")
ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()

ballrect2 = ballrect2.move(speed2)    

while not IS_QUIT:    
    time.sleep(.1)
    ballrect = ballrect.move(speed)    
    ballrect2 = ballrect2.move(speed2)    
    if ballrect.left < 0 or ballrect.right > width:        
        speed[0] = -speed[0]    
    if ballrect.top < 0 or ballrect.bottom > height:        
        speed[1] = -speed[1]
    if ballrect2.left < 0 or ballrect2.right > width:        
        speed2[0] = -speed2[0]    
    if ballrect2.top < 0 or ballrect2.bottom > height:        
        speed2[1] = -speed2[1]
    screen.fill(black)               # Erase the Work space
    screen.blit(ball, ballrect)   # Combine Ball surface with workspace surface
    #pygame.display.flip()        # display workspace on screen

    #screen.fill(black)               # Erase the Work space
    screen.blit(ball2, ballrect2)   # Combine Ball surface with workspace surface
    pygame.display.flip()        # display workspace on screen

