
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Motor():
    PIN = {
        'IN1': 0,
        'IN2': 0,
        'PWM': 0
    }
    obj_pwm = None
    def __init__(self, IN1, IN2, PWM, freq = 50):
        self.PIN['IN1'] = IN1
        self.PIN['IN2'] = IN2
        self.PIN['PWM'] = PWM
        # gpio setup
        print([pin for pin in self.PIN.values()])
        [GPIO.setup(pin, GPIO.OUT) for pin in self.PIN.values()] 
        # pwm setup
        self.pwm_obj = GPIO.PWM(self.PIN['PWM'], freq)
        self.pwm_obj.start(0)
    
    def __setattr__(self, name, value):
        if name == 'speed':
            if value > 0:
                GPIO.output(self.PIN['IN1'], GPIO.HIGH)
                GPIO.output(self.PIN['IN2'], GPIO.LOW)
            else:
                GPIO.output(self.PIN['IN1'], GPIO.LOW)
                GPIO.output(self.PIN['IN2'], GPIO.HIGH)
            self.pwm_obj.ChangeDutyCycle(abs(value))
        else:
            self.__dict__[name] = value

    def setSpeed(self, value):
        if value > 0:
            GPIO.output(self.PIN['IN1'], GPIO.HIGH)
            GPIO.output(self.PIN['IN2'], GPIO.LOW)
        else:
            GPIO.output(self.PIN['IN1'], GPIO.LOW)
            GPIO.output(self.PIN['IN2'], GPIO.HIGH)
        self.pwm_obj.ChangeDutyCycle(abs(value))