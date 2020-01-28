#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


#state of the robot
# 1: Cruise
# 2: Avoid
# 3: Escape
# 4: Goal reached
# TODO: more States
state = 1

def cruise():
    global state
    print("State: Cruise")

def avoid():
    global state
    print("State: Avoid")

def escape():
    global state
    print("State: Escape")
    


while(state != 4):
    
    state_switch={
        1:cruise,
        2:avoid,
        3:escape
    }
    func=state_switch.get(state,lambda :print('Invalid State'))
    func()
    wait(100)







