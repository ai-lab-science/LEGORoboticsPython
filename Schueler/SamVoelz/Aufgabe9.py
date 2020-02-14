#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

touchSensor1 = TouchSensor(Port.S1) #Defnieren des linken Drucksensors
touchSensor2 = TouchSensor(Port.S2) #Definieren des reichten Drucksensors
colorSensor =  ColorSensor(Port.S3) #Definieren des Farbsensors
c = ColorSensor.color #Definieren der Variablen für die Farben
Band = Motor(Port.C) #Definition des Motors, welcher das Band antreibt 
Motor = Motor(Port.A) #Definition des Motors, welcher die Steine aus der Maschine schmeißt

    #Rot-Grün-Gelb-Blau

speicher=[] #Einfügen einer list/eines Speichers
e=0 #Definieren einer Variablen, die die 8 Steine abzählt

down_pressed = Button.DOWN in brick.buttons() #Testet, ob der untere Knopf auf dem Brick gedrückt wurde
while (e<8): #Solange noch nicht alle 8 Steine gescannt wurden, 
    while (down_pressed !=1): #Solange der untere Knopf auf dem Brick nicht gedrückt wurde, 
        down_pressed = Button.DOWN in brick.buttons() #Testet, ob der untere Knopf auf dem Brick gedrückt wurde
        brick.display.image(ImageFile.BACKWARD) #Zeigt auf dem Bildschirm des Bricks einen Pfeil, der runter zeigt
    if (down_pressed==1): #Sobald der untere Knopf auf dem Brick gedrückt wurde, 
        brick.display.image(ImageFile.RIGHT) #Zeigt auf dem Bildschirm des Bricks einen Pfeil, der runter zeigt
        c = colorSensor.color() #Fügt die Farbe, die der FArbsensor scannt, in die Variable c ein 
        speicher.append(c) #Fügt c in den Speicher ein
        wait(1000) #Wartet 1 Sekunde
        down_pressed = Button.DOWN in brick.buttons() #Testet, ob der untere Knopf auf dem Brick gedrückt wurde
        e=e+1 #Addiert der VAriable e 1 

for c in speicher:
    print(c)
    brick.display.clear

wait(5000) #Warte 5 Sekunden

for c in speicher: #Solange sich was in der Variable c befindet,
    if (c == 5): #Wenn c = 5,
        is_pressed = touchSensor1.pressed() #Testet,ob der linke Drucksensor gedrückt ist
        while(is_pressed != 1): #Wenn der linke Drucksensor nicht gedrückt ist, 
            Band.run(-300) #Fährt das Band den Aufsatz nach links
            is_pressed =touchSensor1.pressed() #Testet,ob der linke Drucksensor gedrückt ist     
        if (is_pressed == 1): #Wenn der linke Drucksensor gedrückt ist, 
            Band.stop() #Band stoppt
            Motor.run(-110) #Der Motor schmeißt den Stein aus dem Aufsatz raus
            wait(1100) #Wartet 1,1 Sekunden
            Motor.run(110) #Der Motor fährt sich zurück in die Startposition
            wait(1150) #Wartet 1,15 Sekunden
            Motor.stop() #Motor stoppt 
            print("ROT")
    if (c == 2):
        Is_pressed = touchSensor2.pressed() #Testet,ob der rechte Drucksensor gedrückt ist 
        while(Is_pressed != 1): #Wenn der rechte Drucksensor nicht gedrückt ist, 
            Band.run(300) #Fährt das Band de Aufsatz nach rechts
            Is_pressed =touchSensor2.pressed() #Testet,ob der rechte Drucksensor gedrückt ist       
        if (is_pressed == 1): #Wenn der rechte Drucksensor gedrückt ist, 
            Band.stop() #Band stoppt
            Motor.run(-110) #Der Motor schmeißt den Stein aus dem Aufsatz raus
            wait(1100) #Wartet 1,1 Sekunden
            Motor.run(110) #Der Motor fährt sich zurück in die Startposition
            wait(1150) #Wartet 1,15 Sekunden
            Motor.stop() #Motor stoppt 
            print ("BLAU")

    if (c == 3):
        Band.run_target(300,220) #Aufsatz fährt an eine bestimmte Position
        Motor.run(-110) #Der Motor schmeißt den Stein aus dem Aufsatz raus
        wait(1100) #Wartet 1,1 Sekunden
        Motor.run(110) #Der Motor fährt sich zurück in die Startposition
        wait(1150) #Wartet 1,15 Sekunden
        Motor.stop() #Motor stoppt 
        print ("GRÜN")

    if (c == 4):
        Band.run_target(300,360) #Aufsatz fährt an eine bestimmte Position
        Motor.run(-110) #Der Motor schmeißt den Stein aus dem Aufsatz raus
        wait(1100) #Wartet 1,1 Sekunden
        Motor.run(110) #Der Motor fährt sich zurück in die Startposition
        wait(1150) #Wartet 1,15 Sekunden
        Motor.stop() #Motor stoppt 
        print("GELB")

is_pressed = touchSensor1.pressed() #Testet, ob der linke Drucksensor gedrückt  ist
while (is_pressed != 1): #Solange der linke Drucksensor nicht gedrückt ist, 
    Band.run(-300) #Aufsatz fährt nach links
    is_pressed = touchSensor1.pressed() #Testet, ob der linke Drucksensor gedrückt  ist
    print ("ENDE")