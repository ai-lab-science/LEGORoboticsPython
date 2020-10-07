#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.tools import (wait, print)
from pybricks.media.ev3dev import Image, ImageFile


#Erstelle ein EV3-Objekt
ev3 =EV3Brick()

#Püfe ob der untere Button gedrückt wurde
down_pressed = Button.DOWN in ev3.buttons.pressed()

#Spiele einen Ton
ev3.speaker.beep()

#Zeige den Text "Hallo" auf dem Display
ev3.screen.print("Hallo")

#Lade eines der von Lego bereitgestellten Bilder. 
image1 = Image(ImageFile.WINKING)

#Alternativ kann auch eine png-Datei geladen werden
image2 = Image("DemoPic.png")

# Zwischen Laden des Bildes und dem Zeichnen 
# sollte am Besten etwas Zeit liegen(wenige Milisekunden reichen)
wait(3000)

# Zeichne das erste Bild
ev3.screen.load_image(image1)

wait(2000)

#Lösche alles was vorher auf dem Display angezeigt wurde
ev3.screen.clear()

# Zeichne das zweite Bild
ev3.screen.load_image(image2)

# Stelle das Statuslicht auf Rot
ev3.light.on(Color.RED)

print(down_pressed)

wait(10000)