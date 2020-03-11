#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait


#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn TOF.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")
from TOF import TOF

#Port des Seonsors festlegen
tof = TOF(Port.S1)

while not Button.DOWN in brick.buttons():
    result = 'TOF: ' + str(tof.distance())
    print(result)
tof.close()
