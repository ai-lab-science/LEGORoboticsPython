#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

ultrasonicSensor =  UltrasonicSensor(Port.S1) #Definieren des ultraschallsensors
rightcolorSensor =  ColorSensor(Port.S2) #Definieren des rechten Farbsensors
leftcolorSensor =  ColorSensor(Port.S3) #Definieren des linken Farbsensors
gyro = GyroSensor(Port.S4) #Definieren des Gyrosensors
rightMotor = Motor(Port.A) #Definition des rechten Motors
leftMotor = Motor(Port.B) #Definition des linken Motors


d=ultrasonicSensor.distance() #Messen der Distanz zwischen Roboter und Würfel

leftMotor.run(200) #Fahren des linken Motors bis 
rightMotor.run(200) #FAhren des rechten Motors bis 

while (d>65): #solange d über 65,
    color1 = leftcolorSensor.color() #Suchen nach schwarzer Linie links vom Roboter
    if(color1==Color.BLACK): #Wenn eine schwarze Linie zu sehen ist, 
        brick.display.text("Drehe n. Links", (0, 50)) #Wird dieser Text angezeigt
        leftMotor.run(200) #der linke Motor fährt 
        rightMotor.run(100) #der rechte Motor fährt langsamer als der Linke
    color2 = rightcolorSensor.color() #Suchen nach schwarzer Linie rechts vom Roboter
    if(color2==Color.BLACK): #Wenn eine schwarze Linie zu sehen ist,  
        brick.display.text("Drehe n. Rechts", (0, 50)) #Wird dieseer Text angezeigt
        rightMotor.run(200) #Der rechte Motor fährt
        leftMotor.run(100) #Der linke Motor fährt langsamer als der Rechte
    d=ultrasonicSensor.distance() #Die Distanz zwischen Roboter und Würfel wird gemessen
gyro.reset_angle(0) #Der Winkelwert des gyrosensors wird auf 0 gesetzt

#Der Würfel wird gegriffen

rot = abs(gyro.angle()) #Der totale Wert der Ausgabe des Gyrosensors wird gemessen
while rot<190: #Solange die Rotation unter 190 ist,
    leftMotor.run(800) #Dreht sich der Roboter, indem nur der linke Motor fährt
    rot = abs(gyro.angle()) #Der totale Wert der Ausgabe des Gyrosensors wird gemessen

leftMotor.run(200) #Ab hier wird Zeile 20-35 wiederholt
rightMotor.run(200)

while True:
    color1 = leftcolorSensor.color()
    if(color1==Color.BLACK):
        brick.display.text("Drehe n. Links", (0, 50))
        leftMotor.run(200)
        rightMotor.run(100)
    color2 = rightcolorSensor.color()
    if(color2==Color.BLACK):
        brick.display.text("Drehe n. Rechts", (0, 50))
        rightMotor.run(200)
        leftMotor.run(100)
    d=ultrasonicSensor.distance()
    rot = gyro.angle()