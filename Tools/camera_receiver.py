#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import os

process = os.popen('python3 /home/robot/LEGORoboticsPython/Tools/camera.py') 

f = open('tmp_camera_tracking_data.txt', 'r', os.O_NONBLOCK)
while not Button.UP in brick.buttons():
    f.seek(0)
    text= f.read()
    
    data = text.split(',')
    if data[0]=='' or data[0]=='32896':
        continue
    x=int(data[0])
    y=int(data[1])
    w=int(data[2])
    h=int(data[3])
    #print('running')
    wait(100)
    print('x'+str(x))
    print('y'+str(y))

#f.close()
process.close()