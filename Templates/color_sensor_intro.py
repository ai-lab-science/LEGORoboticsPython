#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# TODO: Initialisiere Sensoren
color_sensor = 
gyro_sensor = 

motor_left = 
motor_right=


program_running = True
while program_running:
    # Aufgabe 1
    # Lest die Messwerte vom Farbsensor aus, speichert sie in einer Variable 
    # und gebt sie zum Testen in der Konsole aus.
    # TODO: Aufgabe bearbeiten
    #color =

    # Aufgabe 2:
    # Der Roboter soll nach vorne fahren. Wenn er mit dem Farbsensor rot sieht, soll er anhalten.
    # TODO: Aufgabe bearbeiten

    # Aufgabe 3:
    # Wenn er mit dem Farbsensor grün erkennt , soll er sich um 90 Grad nach rechts drehen und weiter fahren.
    # Für die 90 Grad Drehung könnt ihr einfach eine Wartezeit benutzen, die ihr durch ausprobieren herausbekommt. 
    # Die Drehung muss nicht exakt 90 Gad sein.
    # TODO: Aufgabe bearbeiten

    # Aufgabe 4: Jetzt soll der Roboter auch Tischkanten erkennen. 
    # Dafür könnt ihr messen wie stark ein Licht reflektiert wird(color_sensor.reflection()).
    # Wenn dieser Messwert also sehr niedrig ist, wurde die Tischkante erreicht und der Roboter muss anhalten.
    # Um dafür einen guten Schwellwert zu finden, solltet ihr den Reflektionsmesswert ebenfalls ausgeben.
    # TODO: Aufgabe bearbeiten


    # Aufgabe 5: Das Verhalten aus Aufgabe 4 soll jetzt so geändert werden, dass der Roboter sich 
    # um 180 Grad dreht wenn er eine Tischkante erkennt. Dafür sollt ihr jetzt aber den Gyro-Sensor 
    # benutzten statt einer Wartezeit. Tipp: Führt reset_angle(0) aus wenn ihr die Tischkannte erkennt.
    # TODO: Aufgabe bearbeiten



