#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

rightcolorSensor =  ColorSensor(Port.S2) #Definieren des rechten Farbsensors 
leftcolorSensor =  ColorSensor(Port.S3) #Definieren des linken Farbsensors
rightMotor = Motor(Port.A) #Definition des rechten Motors
leftMotor = Motor(Port.B) #Definition des linken Motors

V = 175 #Definieren der Geschwindigkeit

leftMotor.run(200)
rightMotor.run(200)

while True: #Immer
    color1 = leftcolorSensor.color() #Überprüfen, ob links vom Roboter  eine Linie ist
    color2 = rightcolorSensor.color() #Überprüfen, ob rechts vom Roboter  eine Linie ist
    if(color1==Color.BLACK) and (color2==Color.BLACK): #Wenn der Roboter frontal vor einer Linie steht,
        leftMotor.run(-V-2) #Fährt er links langsam rückwärts
        rightMotor.run(-V)  #Fährt er rechts etwas schneller als links rückwärts
    if(color1==Color.BLACK): #Wenn nur links vom Roboter eine Linie ist, 
        brick.display.text("Drehe n. Links", (0, 50)) #Wird dieser Text angezeigt
        leftMotor.run(-V-2) #Fährt er links langsam rückwärts
        rightMotor.run(-V) #Fährt er rechts etwas schneller als links rückwärts
        wait(200) #Wartet 0,2 Sekunden
        leftMotor.run(-V-2) #Dreht sich auf der Stelle
        rightMotor.run(V)
        wait(200) #Wartet 0,2 Sekunden 
    if(color2==Color.BLACK): #Wenn nur rechts vom Roboter eine Linie ist, 
        brick.display.text("Drehe n. Rechts", (0, 50)) #Wird dieser Text angezeigt
        leftMotor.run(-V-2) #Fährt er links langsam rückwärts
        rightMotor.run(-V) #Fährt er rechts etwas schneller als links rückwärts
        wait(200) #Wartet 0,2 Sekunden
        leftMotor.run(V-2) #Dreht sich auf der Stelle
        rightMotor.run(-V)
        wait(200) #Wartet 0,2 Sekunden
    else: #Ansonsten,
        rightMotor.run(V) #Fährt er geradeaus
        leftMotor.run(V)