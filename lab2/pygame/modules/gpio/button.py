
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class Button():
    pin = 0
    cnt = 0
    func = None
    def __init__(self, pin, func = lambda a:None, pull_up_down=GPIO.PUD_UP):
        self.pin = pin
        self.func = func
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=pull_up_down)
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.__callback, bouncetime=300)

    def __callback(self, a):
        self.plus()
        self.func(a)

    def plus(self):
        self.cnt += 1

