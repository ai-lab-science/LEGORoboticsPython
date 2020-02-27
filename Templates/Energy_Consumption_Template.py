#!/usr/bin/env pybricks-micropython
import math
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

running = True
energy_used = 0
energy_watch=StopWatch()

motorR = Motor(Port.A)
motorL = Motor(Port.B)

while running:
    #Manuelle Steuerung der Motoren. Kann entfernt werden
    if Button.DOWN in brick.buttons():
        motorR.run(400)
    else:
        motorR.stop()
    if Button.UP in brick.buttons():
        motorL.run(400)
    else:
        motorL.stop()
    wait(100)

    #Messung der verbrauchten Arbeit
    energy_used += brick.battery.current()*brick.battery.voltage()*energy_watch.time()/math.pow(10,9)
    energy_watch.reset()
    brick.display.clear()
    r="Arbeit: "+str('%.2f' % round(energy_used,2))+"J"
    brick.display.text(r,(40, 60))

    






