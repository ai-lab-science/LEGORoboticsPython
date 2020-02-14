#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

V=400 #Definition Geschwindigkeit
rightMotor = Motor(Port.A) #Definition rechter Motor
leftMotor = Motor(Port.B) #Definition linker Motor 

ultrasonicSensor =  UltrasonicSensor(Port.S1)
colorSensor1 =  ColorSensor(Port.S2) #Definieren des linken Farbsensors
colorSensor2 =  ColorSensor(Port.S3) #Definieren des rechten Farbsensors

reflection1 = colorSensor1.reflection() #Sucht nach Reflektionen
reflection2= colorSensor2.reflection()

if reflection1==reflection2 and reflection1>1: #Sobald beide Reflektionen größer als 1,
    leftMotor.run(V) #Beide Motoren fahren
    rightMotor.run(V)

if (reflection1==reflection2) and reflecion1<1: #Sobald beide Reflektionen kleiner als 1, 
    leftMotor.run(V-200) #Beide Motoren fahren langsamer
    rightMotor.run(V-200)

if (reflection1>reflection2): #Sobald Reflektion 1 größer ist als Reflektion 2, 
    leftMotor.run(V) #Dreht nach links
    rightMotor.run(V-200)

if (reflection1<reflection2): #Sobald Reflektion 1 kleiner ist als Reflektion 2, 
    leftMotor.run(V-200) #Dreht nach rechts
    rightMotor.run(V)