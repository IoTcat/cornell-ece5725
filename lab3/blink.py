import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   # Set for GPIO numbering not pin numbers...
GPIO.setup(26, GPIO.OUT) # set GPIO 13 as output to blink LED
i = 0
while (i < 10):
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.5)
    i = i + 1

GPIO.cleanup()