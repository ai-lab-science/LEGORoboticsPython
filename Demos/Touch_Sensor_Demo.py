#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button, Color)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import TouchSensor

#Touchsensor auf Port 4
touchSensor = TouchSensor(Port.S4)

#Zustand des Berührungssensor lesen
is_pressed = touchSensor.pressed()

#Zustand des Berührungssensor so lange ausgeben bis das Programm mit dem unteren Button beendet wird
while not Button.DOWN in brick.buttons():
    print(touchSensor.pressed())
