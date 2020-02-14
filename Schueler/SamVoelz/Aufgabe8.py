#!/usr/bin/env pybricks-micropython
import math
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

UltrasonicSensor = UltrasonicSensor(Port.S1) #Definieren des Ultraschallsensors 
leftcolorsensor = ColorSensor(Port.S2) #Definieren des linken Farbsensors 
rightcolorsensor = ColorSensor(Port.S3) #Definieren des rechten Farbsensors
gyro = GyroSensor(Port.s4) #Definieren des Gyrosensors

rightMotor = Motor(Port.A) #Definition des rechten Motors
leftMotor = Motor(Port.B) #Definition des linken Motors

watch=StopWatch() #Definieren der Stoppuhr
navi=[] #Einbauen einer list/eines Speichers

V=300 #Definieren der Geschwindigkeit

gyro.reset_angle(0) #Setzen des Winkelwertes auf 0 
rot = gyro.angle() #Messen des Winkelwertes
while abs(rot)<85: #Solange der Wert der Rotation kleiner ist als 85,  
    seconds = watch.time()/1000 #Zähle Zeit in Sekunden
    print(seconds) 
    
    leftMotor.run(V) #Beide Motoren fahren vorwärts
    rightMotor.run(V)
    
    rot = gyro.angle() #Messen des Winkelwerts

if abs(rot)>=85: #Sobald Der Wert der Rotation größer oder gleich 85 ist, 
    navi.append(seconds) #Fügt dem Speicher "Navi" die aktuelle Zeit in Sekunden ein
    seconds=0 #Setzt die Sekunden auf 0 
    seconds = watch.time()/1000 #Zählt die Zeit in Sekunden
    
    if rot>=85: #Wenn die Rotation größer oder gleich 85 ist, 
        leftMotor.run(-V) #Dreht auf der Stelle nach links
        rightMotor.run(V)
        
        navi.append(-1) #Fügt dem Speicher "NAvi" -1 hinzu
        
        gyro.reset.angle(0) #Setzt die Rotation auf 0 
    if rot<=-85: #Wenn die Rotation kleiner oder gleich -85 ist, 
        leftMotor.run(V) #Dreht auf der Stelle nach rechts
        rightMotor.run(-V)
        
        navi.append(-2) #Fügt dem Speicher "Navi" -2 hinzu
        gyro.reset.angle #Setzt die Rotation auf 0 

    down_pressed = Button.DOWN in brick.buttons() #Testet, ob der untere Knopf auf dem Brick gedrückt wurde

while down_pressed == 1: #Sobald der untere Knopf auf dem Brick gedrückt wurde, 
    wait(2000) #Wartet 2 Sekunden
    downpressed = Button.UP in brick.buttons() #Testet, ob der obere Knopf auf dem Brick gedrückt wurde


if downpressed == 1: #Sobald der obere Knopf auf dem Brick gedrückt wurde, 
    for seconds>0 in navi: #Solange die Sekunden aus dem Speicher "Navi" über 0 sind, 
        leftMotor.run(V) #Beide Motoren fahren vorwärts
        rightMotor.run(V)
    
    for seconds=-1 in navi: #Sobald die Sekunden aus dem Speicher "Navi" gleich -1 sind, 
        leftMotor.run(-V) #Dreht sich der Roboter auf der Stelle nach links
        rightMotor.run(V)
    
    for seconds=-2 in navi: #Sobald die Sekunden aus dem Speicher "Navi" gleich -2 sind, 
        leftMotor.run(V) #Dreht sich der Roboter auf der Stelle nach rechts
        rightMotor.run(-V)