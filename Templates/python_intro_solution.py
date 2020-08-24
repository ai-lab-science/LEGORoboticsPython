#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase



# Aufgabe 1: Hello World
# Erzeuge einer Konsolenausgabe(print-Befehl). Es soll "Program starting" ausgegeben werden. 
# Dieser String(Text) soll erst in einer Variable gespeichert werden und dann ausgegeben werden.
# TODO: Aufgabe bearbeiten
textausgabe='Program starting'
print(textausgabe)



# Aufgabe 2: While-Schleife
# Jetzt soll ein Countdown von 10 ausgegeben werden. 
# Dafür sollt ihr eine While-Schleife benutzen und die Variable count ausgeben,
# die mit 10 initialisiert wird und in jeder Iteration der Schleife verringert werden soll.
# Baut auch eine Pause in jeder Iteration mit de wait-Befehl ein. 
# Später könnt ihr diese Wartezeit auskommentieren(mit '#') damit ihr nicht bei jedem Test warten müsst.
count = 10
while (count>0):
    print(count)
    count =count-1
    #wait(2000)
# TODO: Aufgabe bearbeiten



# Aufgabe 3: EV3 Button
# Das Programm soll erst gestartet werden wenn der mittlere Button auf dem EV3 gedrückt wird. 
# Dafür sollt ihr eine While-Schleife und die brick.button() Funktion benutzten.
# Wenn der Button gedrückt wurde soll in der Konsole "Program started" ausgegeben werden
center_pressed = Button.CENTER in brick.buttons() 
# Zustand des mittleren Button. Variable muss in 
# Schleife aktualisiert werden

while(not center_pressed):
    center_pressed = Button.CENTER in brick.buttons()

print('Program startet')

# TODO: Aufgabe bearbeiten


# Da ein Roboter in der Regel immer wieder die Sensorwerte aktualisieren und evaluieren muss 
# und die Motoren entsprechend steuern soll, ist es fast immer sinnvoll 
# eine "Dauerschleife" zu haben, die solange läuft bis das Programm beendet ist.
# Für die nächsten Aufgaben soll diese While-Schleife also nicht beendet werden.

# Um Motoren und Sensoren zu benutzen müsst ihr sie erst initialisieren. 
# Dabei müsst ihr angeben an welchen Port die Motoren/ Sensoren angeschlossen sind.
# Ändert also in den nächsten Zeilen die Ports so, dass sie zu eurem Roboter passen
# und entfernt das '#' um den Kommentar aufzuheben
# TODO: Ports anpassen:

touchSensor = TouchSensor(Port.S4)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.D)

program_running = True
while program_running:
    upButtonPressed = Button.UP in brick.buttons()
    wait(5)
    if upButtonPressed:
        brick.sound.beep()

    # Aufgabe 4: If-Satz und Soundausgabe
    # Wenn der obere Button gedrückt ist soll ein Ton über brick.sound.beep() gespielt werden.
    # TODO: Aufgabe bearbeiten
    # Motorsteuerung und Berührungssensor
    
    

    

