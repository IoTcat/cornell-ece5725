import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   # Set for GPIO numbering not pin numbers...
GPIO.setup(26, GPIO.OUT) # set GPIO 13 as output to blink LED
initial_time = time.time()

frequency = int(input("Please enter a PWM frequency: "))
dc = 50
p = GPIO.PWM(26, frequency)
p.start(dc)

while True:
    print(time.time())

# p.stop()
# GPIO.cleanup()