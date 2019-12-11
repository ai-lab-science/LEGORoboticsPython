#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import UltrasonicSensor


ultrasonicSensor =  UltrasonicSensor(Port.S1)

while not Button.DOWN in brick.buttons():
    print(ultrasonicSensor.distance())
