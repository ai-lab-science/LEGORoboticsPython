#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Tag 3: Konvoi

ev3 = EV3Brick()


# 1. ToDo: Zuweisung der Motoren und benutzten Sensoren


# 2. ToDo: Initialisierung aller notwendigen Variblen
# speed:        aktuelle Geschwindigkeit
# distance:     aktueller Abstand zum Vordermann
# setpoint:     gewünschter Abstand zum Vordermann
# error:        aktueller Fehler (gewünschter Abstand - aktueller Abstand)
# accError:     summierter Fehler (Addition aller vergangenen Fehlerwerte)
# lastError:    vorheriger Fehler 
# diffError:    Veränderung des Fehlers (vorheriger Fehler - aktueller Fehler)


# 3. ToDo: Setzen der Parameter des PID-Reglers 
#    Die passenden Parameter müsst ihr selbst durch Tests heraus finden!
#    Tipp: Zu Beginn setzt nur kP = 1 und den Rest auf Null. 
#          Anschließend könnt ihr andere Parametereinstellungen durchführen.
# kP:   Parameter des P-Anteils 
# kI:   Parameter des I-Anteils
# kD:   Parameter des D-Anteils


# Initialisieung einer Liste, um vergangene Abstandsmessungen zu speichern.
# Diese ist notwendig damit am Ende, der durchschnittliche Abstand zum Vordermann bestimmt werden kann
dist = []

# Initialisierung eines Timers, um kontinuierlich den Abstand zum Vordermann zu messen 
# und ihn in der Liste zu speichern.
clockDist = StopWatch()
clockDist.reset()
clockDist.resume()
durationDist = 0

programRunning = True

while programRunning:
    # 4. ToDo: Implementierung der Linien-Verfolgung
    # Sobald eines der beiden Farbsensoren die Linie detektiert, soll der passende Motor stoppen.
    # Ansonsten sollen beide Motoren mit der aktuellen Geschwindigkeit laufen.

    # Abstandsmessung zum Vordermann (distance) und speichern in der Liste
    if clockDist.time() > durationDist:
        distance = ultraSensor.distance()
        dist.append(distance)
        durationDist = 500
        clockDist.reset()

    # 5. ToDo: Berechnung der unterschiedlichen Fehlerwerte (error, accError, diffError)
   
    # 6. ToDo: Berechnung der aktuellen Geschwindigkeit mit der Formel zur Regelung
    # Tipp: Geschwindigkeit = (kP * aktuelle Fehler) + (kI * summierter Fehlerwert) + (kD * Veränderung des Fehlerwertes)

    # 7. ToDo: Nach der Berechnung den aktuellen Fehlerwert als vorherigen Fehler überschreiben

    # Programm stoppt, wenn die untere Taste gedrückt wird
    if Button.DOWN in brick.buttons():
        rightMotor.stop()
        leftMotor.stop()
        programRunning = False

# Berechnung des durchschnittlichen Abstands zum Vordermann und die Anzeige auf dem Brick
avrgDist = int(sum(dist)/len(dist))
ev3.screen.clear()
ev3.screen.print(str(avrgDist))
wait(100000)
