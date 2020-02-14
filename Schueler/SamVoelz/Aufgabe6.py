#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase 

ultrasonicSensor = UltrasonicSensor(Port.S1)
leftcolorsensor = ColorSensor(Port.S2)
rightcolorsensor = ColorSensor(Port.S3)
GyroSensor = GyroSensor(Port.S4)

rightMotor = Motor(Port.A)
leftMotor = Motor(Port.B)

state = 1
V = 200

def Cruise(): #Definition des states Cruise
    global state
    print("State: Cruise")
    leftMotor.run(V) #Der linke Motor fährt
    rightMotor.run(V-10) #Der rechte Motor fährt, allerdings langsamer als der Linke
    
    color=rightcolorsensor.color #Sucht nach Farben
    color=leftcolorsensor.color
    d=ultrasonicSensor.distance #Misst die  Distanz zwischen Roboter und Würfel 
    
    if color == Color.BLACK: #Wenn Farbe = Schwarz,
        state=2 #Wechselt state zu 2 
    if color == Color.WHITE: #Wenn Farbe = Weiß,                             
        state=4 #Wechselt state zu 4 
    if d<40: #Wenn d kleiner ist als 40, 
        state=3 #Wechselt state zu 3 
    


def Rand(): #Definition state Rand
    global state
    print("State: Rand")
    leftMotor.run(-V) #Beide Motoren fahren rückwärts
    rightMotor.run(-V)
    wait(200) #Wartet 0,2 Sekunden
    rightMotor.stop() #Der rechte Motor stoppt
    wait(200) #Wartet 0,2 Sekunden
    
    color=rightcolorsensor.color #Sucht nach Farben
    color=leftcolorsensor.color
    d=UltrasonicSensor.distance #Misst die  Distanz zwischen Roboter und Würfel 
    
    if color == Color.WHITE: #Wenn Farbe = Weiß, 
        state=4 #Wechselt state zu 4 
    if d<40: #Wenn d kleiner als 40, 
        state=3 #Wechselt state zu 3 
    if color != Color.BLACK and color != Color.WHITE: #Wenn Farbe weder Weiß noch Schwarz,    
        state=1 #Wechselt state zu 1 

def Würfel(): #Definition state Würfel
    global state
    print("State: Rand")
    brick.sound.beep() #Roboter piept
    color=rightcolorsensor.color #Sucht nach Farben
    color=leftcolorsensor.color
    d=UltrasonicSensor.distance #Misst die  Distanz zwischen Roboter und Würfel 
    
    if color == Color.BLACK: #Wenn Farbe = Schwarz,
        state=2 #Wechselt state zu 2 
    if color == Color.WHITE: #Wenn Farbe = Weiß,
        state=4 #Wechselt state zu 4 
    if color != Color.BLACK and color != Color.WHITE:#Wenn Farbe weder Weiß noch Schwarz, 
        state=1 #Wechselt state zu 1 

def Ziel(): #Definition state Ziel
    global state 
    print("State: Ziel")
    brick.sound.beep #Roboter piept
    wait(500) #Wartet 0,5 Sekunden
    brick.sound.beep #Roboter piept
    state = 5 #Wechselt state zu 5 

while(state != 5): #Solange state nicht gleich 5,
    
    state_switch={ #Wechselt states
        1:Cruise,
        2:Rand,
        3:Würfel,
        4:Ziel
    }
    func=state_switch.get(state,lambda :print('Invalid State'))
    func()
    wait(100) #Wartet 0,1 Sekunde