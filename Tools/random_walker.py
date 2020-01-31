#!/usr/bin/env pybricks-micropython
import random
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait


#Motor auf Port C
leftMotor = Motor(Port.B)

#Motor auf Port C
rightMotor = Motor(Port.C)

rightSpeed = 200
leftSpeed = 200

randomness = 40
max_speed = 250
min_speed = 150

while not Button.DOWN in brick.buttons():


    if rightSpeed<min_speed:
        rightSpeed+=random.randrange(randomness)
    elif rightSpeed>max_speed:
        rightSpeed-=random.randrange(randomness)
    else:
        rightSpeed+=random.randrange(-randomness,randomness)


    if leftSpeed<min_speed:
        leftSpeed+=random.randrange(randomness)
    elif leftSpeed>max_speed:
        leftSpeed-=random.randrange(randomness)
    else:
        leftSpeed+=random.randrange(-randomness,randomness)
      


    leftMotor.run(abs(leftSpeed))
    rightMotor.run(abs(rightSpeed))
    print("right speed: "+str(rightSpeed)+" left speed: "+str(leftSpeed))
    wait(100)


rightMotor.stop()
leftMotor.stop()










    
