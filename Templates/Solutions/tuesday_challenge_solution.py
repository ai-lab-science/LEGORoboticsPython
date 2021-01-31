#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import random


#state of the robot
# 1: Cruise
# 2: Avoid
# 3: Escape
# 4: Goal reached
# TODO: more States
state = 1
CRUISE_STATE = 1
AVOID_STATE = 2
ESCAPE_LEFT_STATE = 3
ESCAPE_RIGHT_STATE = 5
GOAL_REACHED_STATE = 4

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

#Farbsensor auf Port 3
color_sensor_left =  ColorSensor(Port.S3)

#Farbsensor auf Port 1
color_sensor_right =  ColorSensor(Port.S1)

ultrasonic_sensor = UltrasonicSensor(Port.S2)

velocity = 200

def cruise():
    global state
    print("State: Cruise")
    # Fahre gerade nach vorne
    left_motor.run(velocity)
    right_motor.run(velocity)
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    update_state()
   
    
        

def avoid():
    global state
    print("State: Avoid")
    # Fahre nach vorne, aber lenke gleichzeitig zur Seite um einem Hindernis auszuweichen
    velocity_diff = 65
    left_motor.run(velocity + velocity_diff)
    right_motor.run(velocity - velocity_diff)
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    update_state()
    

def escape_left():
    global state
    print("State: Escape")
    # Fahre ein Stück zurück und drehe dann auf der Stelle
    
        
    left_motor.run(-velocity)
    right_motor.run(-velocity)
    wait(1100)
    right_motor.run(velocity)

    wait(1000)
    left_motor.stop()
    right_motor.stop()
    
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    update_state()

def escape_right():
    global state
    print("State: Escape")
    # Fahre ein Stück zurück und drehe dann auf der Stelle
    
        
    left_motor.run(-velocity)
    right_motor.run(-velocity)
    wait(1100)
    left_motor.run(velocity)

    wait(1000)
    left_motor.stop()
    right_motor.stop()
    
    
    # Wechsle den state abhängig von aktuellen Sensorwerten
    update_state()



def update_state():
    global state
    color_left = color_sensor_left.color()
    color_right = color_sensor_right.color()
    distance = ultrasonic_sensor.distance()
    reflection_left = color_sensor_left.reflection()
    reflection_right = color_sensor_right.reflection()
    print("Reflection"+ str(reflection_left))
    if color_left == Color.RED or color_right == Color.RED:
        state = GOAL_REACHED_STATE
    # elif distance<130 or color_left == Color.BLACK or color_right == Color.BLACK:
    #     state = 3
    elif reflection_left < 2:
        state = ESCAPE_RIGHT_STATE
    elif reflection_right < 2:
        state = ESCAPE_LEFT_STATE
    elif distance<130 :
        if random.random()>0.5:
            state = ESCAPE_LEFT_STATE
        else:
            state = ESCAPE_RIGHT_STATE
    elif distance<450:
        state = AVOID_STATE
    else:
        state = CRUISE_STATE
    
    
program_running = True

while program_running:
    
    if state == CRUISE_STATE:
        cruise()
    elif state == AVOID_STATE:
        avoid()
    elif state == ESCAPE_LEFT_STATE:
        escape_left()
    elif state == ESCAPE_RIGHT_STATE:
        escape_right()
    elif state == GOAL_REACHED_STATE:
        program_running = False
    else:
        print("State: "+str(state)+" ist nicht definiert")
    
    wait(20)







