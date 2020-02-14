#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

ultrasonicSensor =  UltrasonicSensor(Port.S1) #Definieren des Ultraschallsensors
V = 800 #Definieren der Geschwinigkeit
leftMotor = Motor(Port.B) #Definition des rechten Motors
rightMotor = Motor (Port.A) #Definition des linken Motors

d=ultrasonicSensor.distance()
while True: #Immer
    if (d>=400): #solange d>=400,
        leftMotor.run(V) #fährt der reche Motor
        rightMotor.run(V) #fährt der linke Motor
        d=ultrasonicSensor.distance() #wird die Distanz neu gemessen
        print ("ok") #Ausgabe
    if (d<400): #sobald d<400,
        leftMotor.run(V) #fährt der linke Motor
        rightMotor.stop() #stoppt der rechte Motor
        d=ultrasonicSensor.distance() #wird die Distanz neu gemessen
        print ("Beep") #Ausgabe