#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import random


state = 1
NO_CUBE_STATE = 1
PICKING_UP_STATE = 2
PICKED_UP_CUBE_STATE = 3
GOAL_REACHED_STATE = 4

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

#Farbsensor auf Port 3
color_sensor_left =  ColorSensor(Port.S3)

#Farbsensor auf Port 1
color_sensor_right =  ColorSensor(Port.S1)

ultrasonic_sensor = UltrasonicSensor(Port.S2)


velocity = 185
velocity_diff = 80

while not state == GOAL_REACHED_STATE:
    color_left = color_sensor_left.color()
    color_right = color_sensor_right.color()
    velocity_left = velocity
    velocity_right = velocity

    if color_left == Color.BLACK:
        velocity_left-=velocity_diff
        velocity_right+=velocity_diff
    elif color_right == Color.BLACK:
        velocity_left+=velocity_diff
        velocity_right-=velocity_diff
    
    if (color_left == Color.RED or color_right == Color.RED) and state == NO_CUBE_STATE:
        state = PICKING_UP_STATE
    elif (color_left == Color.RED or color_right == Color.RED) and state == PICKING_UP_STATE:
        velocity_left = velocity
        velocity_right = velocity
    elif color_left != Color.RED and color_right != Color.RED and state == PICKING_UP_STATE:
        state = PICKED_UP_CUBE_STATE
    elif (color_left == Color.RED or color_right == Color.RED) and state == PICKED_UP_CUBE_STATE:
        state = GOAL_REACHED_STATE
    
    right_motor.run(velocity_right)
    left_motor.run(velocity_left)
    print(state)

