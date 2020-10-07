#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from pybricks.ev3devices import Motor

# Objekt der EV3Brick Klasse erstellen
ev3 = EV3Brick()

# Die Sprachausgabe des EV3s auf Deutsch stellen. 
# Für Ausgaben in Englisch kann dieser Schritt weggelassen werden
ev3.speaker.set_speech_options('de')

# Der übergebene Text wird über die Lautsprecher mit text-to-speech ausgegeben
ev3.speaker.say("Das ist ein Test")

# Stelle die Lautstärke auf 20%
ev3.speaker.set_volume(20)

ev3.speaker.say("Jetzt spreche ich leiser")


ev3.speaker.play_notes(['C4/4', 'C4/4', 'G4/4', 'G4/4'])


#ev3.speaker.say("Tennisball gefunden Barcode Nummer 5 Box")

# 