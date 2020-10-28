#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
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
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
left_motor_speed = 0
right_motor_speed = 0

def cruise():
    global state
    print("State: Cruise")
    #TODO Fahre gerade nach vorne
    #TODO Wechsle den state abhängig von aktuellen Sensorwerten

def avoid():
    global state
    print("State: Avoid")
    #TODO Fahre nach vorne, aber lenke gleichzeitig zur Seite um einem Hindernis auszuweichen
    #TODO Wechsle den state abhängig von aktuellen Sensorwerten


def escape():
    global state
    print("State: Escape")
    #TODO Fahre ein Stück zurück und drehe dann auf der Stelle
    #TODO Wechsle den state abhängig von aktuellen Sensorwerten

    


while program_running:
    
    if state == 1:
        cruise()
    elif state == 2:
        avoid()
    elif state == 3:
        escape
    elif state == 4:
        program_running = False
    else:
        print("State: "+str(state)+" ist nicht definiert")
    
    wait(60)







