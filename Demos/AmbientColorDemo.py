#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait

#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn AmbientColorSensor.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")

#Importiere AmbientColorSensor.py
from AmbientColorSensor import AmbientColorSensor

#Port des Sensors festlegen.
colorSensor= AmbientColorSensor(Port.S1)

while not Button.DOWN in brick.buttons():
    result = 'Color: ' + str(colorSensor.color())
    brick.display.clear()
    brick.display.text(result, (0, 50))
    print(result)
    wait(0.1)
