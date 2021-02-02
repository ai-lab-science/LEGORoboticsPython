#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random


# Create your objects here.
ev3 = EV3Brick()


# Motors
leftMotor = Motor(Port.A)
rightMotor = Motor(Port.D)

# Sensors
#ultraSensor = UltrasonicSensor(Port.S3)
leftColorSensor = ColorSensor(Port.S1)
rightColorSensor = ColorSensor(Port.S4)

# Button pressed
#up_pressed = Button.Up in brick.buttons()
programRunning = True

# Speed 
minSpeed = 100
maxSpeed = 400

# Clock
clockLine = StopWatch()
clockLine.reset()
clockLine.resume()
durationLine = 0

clockDist = StopWatch()
clockDist.reset()
clockDist.resume()
durationDist = 0

# Distance array
dist = []

while programRunning:
    print("GO")
    # Timer
    if clockLine.time() > durationLine:
        speed = random.randint(minSpeed, maxSpeed)
        durationLine = random.randint(2000, 3000)
        print(speed, durationLine)
        clockLine.reset()

    # Linefollowing
    if (leftColorSensor.color() == Color.BLUE):
        leftMotor.stop()
    elif (rightColorSensor.color() == Color.BLUE):
        rightMotor.stop()
    else:
        leftMotor.run(speed)
        rightMotor.run(speed)

    # Distance measurement 
    '''
    if clockDist.time() > durationDist:
        dist.append(ultraSensor.distance())
        durationDist = 500
        clockDist.reset()
    '''


