#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from IMU import IMU

#specify Port and mode of Sensor. Possible Modes are TILT, ACCEL, COMPASS, MAG, GYRO
#TODO: implement ALL mode 
#more info:http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html
imu = IMU(Port.S3, 'GYRO')

while not Button.DOWN in brick.buttons():
    result = 'IMU: ' + str(imu.angle())
    brick.display.clear()
    brick.display.text(result, (0, 50))
    print(result)
    wait(0.1)
