#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

state = 1 #Definieren des Wertes für state
rightMotor = Motor(Port.A) #Definition des rechten Motors
leftMotor = Motor(Port.B) #Definition des linken Motors

ultrasonicSensor =  UltrasonicSensor(Port.S1) #Definieren des Ultraschallsensors
colorSensor1 =  ColorSensor(Port.S2) #Definieren des rechten Farbsensors
colorSensor2 =  ColorSensor(Port.S3) #Definieren des linken Farbsensors

def cruise(): #Definition des states cruise
    global state
    print("State: Cruise")
    leftMotor.run(480) #Der linke Motor soll fahren
    rightMotor.run(500) #Der rechte Motor soll etwas schneller fahren als der Linke
    d=ultrasonicSensor.distance() #Messen der Distanz von Roboter zu möglichen Hindernissen
    if d<180: #Wenn d<180,
        state=2 #Wechselt der state zu 2 
    if d<100: #Wenn d<100, 
        state=3 #Wechselt der state zu 3
    reflection = colorSensor1.reflection() #Die Reflektion des rechten Farbsensors wird gemessen 
    if (reflection == 0): #Wenn die Reflektion = 0,
        state = 5 #Wechselt der state zu 5 
    

def avoid(): #Definition des states avoid
    global state
    print("State: Avoid")
    rightMotor.stop() #Der rechte Motor soll stoppen, der Linke fährt weiter
    d=ultrasonicSensor.distance() #Messen der Distanz von Roboter zu möglichen Hindernissen
    if (d<180): #Wenn d<180,
        state=1 #Wechselt den state zu 1 
    if (d>100): #Wenn d>100,
        state=3 #Wechselt state zu 3
    reflection = colorSensor1.reflection() #Misst die Reflektion des rechten Farbsensors
    if (reflection == 0): #Wenn die Reflektion = 0,
        state = 5 #Wechselt state zu 5

def escape(): #Definition des states escape
    global state
    print("State: Escape")
    rightMotor.run(-480) #Der rechte Motor soll rückwärts fahren, sodass sich der Roboter auf der Stelle dreht
    d=ultrasonicSensor.distance() #Messen der Distanz von Roboter zu möglichen Hindernissen
    if d>100 and d<180: #Wenn d zwischen 100 und 180 liegt, 
        state=2 #Weschselt state zu 2 
    if (d>180): #Wenn d größer als 180,
        state=1 #Wechsel state zu 1 
    reflection = colorSensor1.reflection() #Misst die Reflektion des rechten Farbsensors
    if (reflection == 0): #Wenn die Reflektion = 0, 
        state = 5 #Wechselt state zu 5


def revine(): #Definition des states revine
    global state
    print("State: Revine")
    reflection = colorSensor1.reflection() #Misst die Reflekton des rechten Farbsensors
    if (reflection == 0): #Wenn die Reflektion = 0,
        leftMotor.run(-200) #Fährt mit beiden Motoren rückwärts
        rightMotor.run(-200)
        wait(1000) #Wartet 1 Sekunde
        leftMotor.stop() #Stoppt beide Motoren 
        rightMotor.stop()
        wait(1000) #Wartet 1 Sekunde
        leftMotor.run(200) #Dreht sich nach rechts
        wait(1000) #Wartet 1 Sekunde
    d=ultrasonicSensor.distance() #Misst die Distanz von Roboter zu möglichem Hindernis
    if (d>180): #Wenn d größer als 180, 
        state=1 #Wechselt state zu 1
    if (100<d<180): #Wenn d zwischen 100 und 180,
        state=2 #Wechselt state zu 2
    if (d<100): #Wenn d kleiner als 100
        state=3 #Wechselt state zu 3 

while(state != 4): #Solange state nicht 4,
    
    state_switch={ #Wechselt zwischen states
        1:cruise,
        2:avoid,
        3:escape,
        5:revine
    }
    func=state_switch.get(state,lambda :print('Invalid State'))
    func()
    wait(100) #wartet 0,1 Sekunde