#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Motors
leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Sensors
ultraSensor = UltrasonicSensor(Port.S3)
leftColorSensor = ColorSensor(Port.S1)
rightColorSensor = ColorSensor(Port.S4)

# Button pressed
#up_pressed = Button.Up in brick.buttons()
programRunning = True

# Speed 
speed = 0

# Clock
clockDist = StopWatch()
clockDist.reset()
clockDist.resume()
durationDist = 0

# Distance array
dist = []
distance = 0

# Desired constant distance 
setpoint = 100

# Error
error = 0
accError = 0
lastError = 0
diffError = 0

# PID parameter 
kP = 2
kI = 0
kD = 2

while programRunning:
    # Linefollowing
    if (leftColorSensor.color() == Color.BROWN):
        leftMotor.stop()
    elif (rightColorSensor.color() == Color.BROWN):
        rightMotor.stop()
    else:
        leftMotor.run(-speed)
        rightMotor.run(-speed)

    # Distance measurement 
    if clockDist.time() > durationDist:
        distance = ultraSensor.distance()
        dist.append(distance)
        durationDist = 500
        clockDist.reset()

    # Calculate error
    error = setpoint - distance
    accError += error
    diffError = lastError - error   
    
    speed = kP*error + kI*accError + kD*diffError
    print(speed, distance)

    lastError = error


    # Stop while-loop
    if Button.DOWN in brick.buttons():
        rightMotor.stop()
        leftMotor.stop()
        programRunning = False


avrgDist = int(sum(dist)/len(dist))
variance = sum((xi - avrgDist) ** 2 for xi in dist) / len(dist)
print(avrgDist, variance)

brick.display.clear()
brick.display.text(str(variance), (0, 50))

wait(10000)
