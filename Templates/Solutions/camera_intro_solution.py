#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch

from pybricks.robotics import DriveBase
#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn TOF.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")

from pixy_camera import *

ev3=EV3Brick()

# Aufgabe 1
# Erstelle ein neues Camera-Objekt mit dem entsprechenden Port und initialisiert eure Motoren
camera = Camera(Port.S1)
motor_left = Motor(Port.A)
motor_right = Motor(Port.D)

# Aufgabe 2
# Für das Object-Tracking muss als erstes über PixyMon ein Objekt eingespeichert werden.
# Wie das funktioniert zeigen wir euch außerhalb von diesem Template.
# Speichert ein Objekt in Signatur 1 ein. 
# Das Objekt sollte eine grelle Farbe haben, und gut beleuchtet sein. 
# Probiert am Besten verschiedene Objekte aus.

# Aufgabe 3
# Aktiviert die Lampe des Roboters mit der lamp_on() Funktion(siehe Wiki)
# TODO aktiviere Lampe

while not Button.DOWN in ev3.buttons.pressed():
    # Aufgabe 4
    # Ruft die Daten über die abgespeicherte Signatur über
    # camera.getObjectData ab und speichert sie in Variablen.
    # Es wird hilfreich sein das zeichnen des Objektes zu aktivieren.
    # TODO rufe camera.getObjectData auf(siehe Wiki)
    # TODO gebt die X-Koordinate des Objektes über print aus

    # Aufgabe 5
    # Der Roboter soll sich jetzt in Richtung des Objektes drehen. Wenn die X Koordinate des Objektes 
    # auf der rechten Hälfte des Sichtfeldes der Kamera ist, soll er sich nach rechts drehen 
    # und auf der linken Seite entsprechend nach links.
    # Achtung: Wenn das Objekt nicht gefunden wurde, bekommt man eine sehr große X-Koordinate außerhalb des Sichtfeldes.
    # In diesem Fall soll sich der Roboter nicht drehen.
    # TODO Drehung in Richtung des Objektes

    # Aufgabe 6
    # Verändert das Programm jetzt so, dass der Roboter in Richtung des Objektes fährt anstatt sich nur zu drehen 
    
    
    wait(20)

camera.close()