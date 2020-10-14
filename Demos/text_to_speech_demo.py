#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from pybricks.ev3devices import Motor

# Objekt der EV3Brick Klasse erstellen
ev3 = EV3Brick()

ev3.speaker.set_volume(10)

#Spiele "Bruder Jakob" mit der play_notes Funktion
ev3.speaker.play_notes(['F4/4', 'G4/4', 'A4/4', 'F4/4'])
ev3.speaker.play_notes(['F4/4', 'G4/4', 'A4/4', 'F4/4'])
ev3.speaker.play_notes(['A4/4', 'Bb4/4', 'C5/2'])
ev3.speaker.play_notes(['A4/4', 'Bb4/4', 'C5/2'])
ev3.speaker.play_notes(['C5/8', 'D5/8', 'C5/8','Bb4/8','A4/4','F4/4'])
ev3.speaker.play_notes(['C5/8', 'D5/8', 'C5/8','Bb4/8','A4/4','F4/4'])
ev3.speaker.play_notes(['G4/4', 'C4/4', 'F4/2','G4/4', 'C4/4', 'F4/2'])



# Die Sprachausgabe des EV3s auf Deutsch stellen. 
# Für Ausgaben in Englisch kann dieser Schritt weggelassen werden
ev3.speaker.set_speech_options('de')

# Der übergebene Text wird über die Lautsprecher mit text-to-speech ausgegeben
ev3.speaker.say("Das ist ein Test")

# Stelle die Lautstärke auf 20%
ev3.speaker.set_volume(20)

ev3.speaker.say("Jetzt spreche ich leiser")

 


#ev3.speaker.say("Tennisball gefunden Barcode Nummer 5 Box")

# 