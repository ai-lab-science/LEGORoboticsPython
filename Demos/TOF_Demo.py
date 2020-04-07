#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from pybricks.ev3devices import ColorSensor



#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn TOF.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")
from TOF import TOF

#Port des Seonsors festlegen
tof = TOF(Port.S2)
c = ColorSensor(Port.S3)

while not Button.DOWN in brick.buttons():
    result = 'TOF: ' + str(tof.distance())
    print(result)
    print("Color"+str(c.color()))
tof.close()
