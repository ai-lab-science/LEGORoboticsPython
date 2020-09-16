#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from pybricks.ev3devices import Motor
import time




#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn TOF.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")
from pixy_camera import Camera

ev3=EV3Brick()
#Port des Seonsors festlegen
camera = Camera(Port.S1)
rightMotor = Motor(Port.A)
leftMotor = Motor(Port.B)
speed=150
while not Button.DOWN in ev3.buttons.pressed():
    
    x,y,w,h=camera.getObjectData(1) 
    result = ' Camera x: ' + str(x)
    print(result)
    if x<2000:
        diff_from_center=x-100
        leftMotor.run(speed+diff_from_center)
        rightMotor.run(speed-diff_from_center)
    else:
        leftMotor.stop()
        rightMotor.stop()
        
    wait(200)

camera.close()
leftMotor.stop()
rightMotor.stop()