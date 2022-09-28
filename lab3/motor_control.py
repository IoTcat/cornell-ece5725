import time
sys.path.append('modules/gpio')

import numpy as np
from motor import Motor

motor = Motor(IN1=5, IN2=6, PWM=26)

motor.speed = 0
time.sleep(3)
motor.speed = 50
time.sleep(3)
motor.speed = 100
time.sleep(3)


motor.speed = 0
time.sleep(3)
motor.speed = -50
time.sleep(3)
motor.speed = -100
time.sleep(3)


motor.speed = 0
