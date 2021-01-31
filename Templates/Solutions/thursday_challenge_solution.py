#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import (Port, Button, Color)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import Motor, ColorSensor
import time




#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn pixy_camera.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")
from pixy_camera import Camera

ev3=EV3Brick()
#Port des Seonsors festlegen
camera = Camera(Port.S4)
rightMotor = Motor(Port.D)
leftMotor = Motor(Port.A)

#Farbsensor auf Port 3
colorSensorLeft =  ColorSensor(Port.S3)

#Farbsensor auf Port 1
colorSensorRight =  ColorSensor(Port.S1)

speed=150
backwardsSpeed = -150
turningSpeed= 150

camera.lamp_on()

while not Button.DOWN in ev3.buttons.pressed():
    
    x2,y2,w2,h2=camera.getObjectData(2,False)
    x1,y1,w1,h1=camera.getObjectData(1,True)    
    result = ' Camera x: ' + str(x1)
    print(result)   

    if colorSensorLeft.color()==Color.BLACK:
        print("Left Line")
        leftMotor.run(speed)
        rightMotor.run(speed)
        wait(100)
        leftMotor.run(backwardsSpeed)
        rightMotor.run(backwardsSpeed)
        wait(1100)
        leftMotor.run(turningSpeed)
        rightMotor.run(-turningSpeed)
        wait(1000)
    elif colorSensorRight.color()==Color.BLACK:
        print("Left Line")
        leftMotor.run(speed)
        rightMotor.run(speed)
        wait(100)
        leftMotor.run(backwardsSpeed)
        rightMotor.run(backwardsSpeed)
        wait(1100)
        leftMotor.run(-turningSpeed)
        rightMotor.run(turningSpeed) 
        wait(1000)

    elif x1<2000:
        print("Signatur 1")
        diff_from_center=x1-100
        leftMotor.run(speed+diff_from_center)
        rightMotor.run(speed-diff_from_center)
    elif x2<2000:
        print("Signatur 2")
        diff_from_center=x2-100
        leftMotor.run(speed-diff_from_center)
        rightMotor.run(speed+diff_from_center)
    else:
        print("Cruise")
        leftMotor.run(speed)
        rightMotor.run(speed)
        
    wait(200)

camera.close()
leftMotor.stop()
rightMotor.stop()