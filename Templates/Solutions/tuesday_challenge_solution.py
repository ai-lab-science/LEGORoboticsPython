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
right_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.B)
ultrasonic_sensor = UltrasonicSensor(Port.S1)

def cruise():
    global state
    print("State: Cruise")
    # Fahre gerade nach vorne
    left_motor.run(200)
    right_motor.run(200)
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    if color_sensor.color() == Color.RED:
        state = 4
    elif ulrasonic_sensor.distance()<300:
        state = 2
    elif ulrasonic_sensor.distance()<100:
        state = 3
    
        

def avoid():
    global state
    print("State: Avoid")
    # Fahre nach vorne, aber lenke gleichzeitig zur Seite um einem Hindernis auszuweichen
    left_motor.run(300)
    right_motor.run(150)
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    if color_sensor.color() == Color.RED:
        state = 4
    elif ulrasonic_sensor.distance()<300:
        state = 2
    elif ulrasonic_sensor.distance()<100:
        state = 3

def escape():
    global state
    print("State: Escape")
    # Fahre ein Stück zurück und drehe dann auf der Stelle
    left_motor.run(-200)
    right_motor.run(-200)
    wait(1500)
    left_motor.run(200)
    wait(2000)
    left_motor.stop()
    right_motor.stop()
    
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    if color_sensor.color() == Color.RED:
        state = 4
    elif ulrasonic_sensor.distance()<300:
        state = 2
    elif ulrasonic_sensor.distance()<100:
        state = 3
    


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







