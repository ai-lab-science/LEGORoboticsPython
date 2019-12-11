#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

leftMotor = Motor(Port.C)

# Mit maximal 300 Grad pro Sekunde den Motor um 90 Grad zum Ursprung drehen
leftMotor.run_target(300,90)

#Warte 2 Sekunden
wait(2000)

# Mit maximal 200 Grad pro Sekunde den Motor nach vor
leftMotor.run(200)

#Warte 2 Sekunden waehrend der Motor laeuft
wait(5000)

#Stoppe den Motor nach 5 Sekunden
leftMotor.stop()





    
