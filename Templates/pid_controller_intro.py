#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# TODO: Initialisiere Sensoren
gyro_sensor = 

motor_left = 
motor_right=


program_running = True
while program_running:
    # Bei der Regelung geht es darum, aus einem gegebenen Sollwert(gewollter Zustand das Roboters) eine sinnvolle Reaktion
    # zu berechen mit denen der Sollwert ohne großes Überschwingen möglichst schnell erreicht wird.
    # Für eine Regelung muss zunächst der Regelfehler berechnet werden. Das ist die abweichung des tatsächlichen 
    # Zustandes vom Sollwert. Hier wird 
