#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
ev3 = EV3Brick()

ultrasonicSensor =  UltrasonicSensor(Port.S2)

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

program_running = True
distance = ultrasonicSensor.distance()

left_motor.run(800)
right_motor.run(800)
while  distance > 195:
    distance = ultrasonicSensor.distance()
    print(distance)
left_motor.stop()
right_motor.stop()

