#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Button, Color)
from pybricks.tools import (wait, print)
from pybricks.ev3devices import ColorSensor

colorSensor =  ColorSensor(Port.S1)

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
    print("Lichtstaerke"+str(colorSensor.ambient()))

    wait(300)
    
