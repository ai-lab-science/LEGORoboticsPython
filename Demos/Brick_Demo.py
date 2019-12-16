#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Button, Color
from pybricks.tools import (wait, print)

#Püfe ob der untere Button gedrückt wurde
down_pressed = Button.DOWN in brick.buttons()

#Spiele einen Ton
brick.sound.beep()

#Lösche alles was vorher auf dem Display angezeigt wurde
brick.display.clear()

#Zeige den Text "Hallo" auf dem Display and den Koordinaten (0,50)
brick.display.text("Hallo", (0, 50))

# Stelle das Statuslicht auf Rot
brick.light(Color.RED)

print(down_pressed)

wait(10000)