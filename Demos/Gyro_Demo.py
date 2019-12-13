#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import GyroSensor

#Gyro Sensor auf Port 4
gyro = GyroSensor(Port.S4)

#Aktuelle Position als Nullposition festlegen
gyro.reset_angle(0)

#aktuellen Winkel lesen
rot = gyro.angle()

#aktuelle Winkelgeschwindigkeit lesen
rot_speed = gyro.speed()


while not Button.DOWN in brick.buttons():
    print(gyro.angle())
