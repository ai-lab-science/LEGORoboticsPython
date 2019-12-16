#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button, Color)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import ColorSensor

#Farbsensor auf Port 1
colorSensor =  ColorSensor(Port.S1)

#Lese aktuellen Farbwert
color = colorSensor.color()

#Mögliche Farbwerte sind Color.BLACK, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED, 
#Color.WHITE, Color.BROWN oder None

#Prüfe ob der Sensor Rot gemessen hat
if(color==Color.RED):
    print("Rot")
#Messe die Intensität des Umgebungslichts. (0 bis 100)
amb_light = colorSensor.ambient()

while not Button.DOWN in brick.buttons():
    #Farbe einer Oberflaeche messen und als Zahl ausgeben
    print("Farbe: "+str(colorSensor.color()))
    
    #Moegliche Farbwerte sind Color.BLACK, Color.BLUE, Color.GREEN, Color.YELLOW, Color.RED, 
    #Color.WHITE, Color.BROWN oder None
    if colorSensor.color() == Color.BLACK:
        print("Schwarz")
    elif colorSensor.color() == Color.RED:
        print("Rot")


    #Staerke des Umgebungslicht messen 
    print("Lichtstaerke: "+str(colorSensor.ambient()))

    wait(300)
    
