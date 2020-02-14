#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

ultrasonicSensor =  UltrasonicSensor(Port.S1)
leftMotor = Motor(Port.B) #Definition des linken Motors
rightMotor = Motor(Port.A) #Definition des rechten Motors

d=ultrasonicSensor.distance() #Messen der Distanz zwischen Roboter und potenziellem Hindernis

while (d>175): #solange d>175, 
    leftMotor.run(800) #fährt der linke Motor
    rightMotor.run(800) #und der rechte Motor
    d=ultrasonicSensor.distance() #und die Distanz wird wieder gemessen.

    #sobald die Distanz niedriger als 175 ist, stoppt der Roboter und das Programm
    