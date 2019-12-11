#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import GyroSensor

gyro = GyroSensor(Port.S4)
gyro.reset_angle(0)


while not Button.DOWN in brick.buttons():
    print(gyro.angle())
