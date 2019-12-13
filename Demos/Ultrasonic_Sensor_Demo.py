#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import UltrasonicSensor

#Ultraschallsensor auf Port 1
ultrasonicSensor =  UltrasonicSensor(Port.S1)

#Gemessene Distanz lesen (in Millimeter)
d=ultrasonicSensor.distance()

#Distanz so lange ausgeben bis das Programm mit dem unteren Button beendet wird
while not Button.DOWN in brick.buttons():
    print(ultrasonicSensor.distance())
