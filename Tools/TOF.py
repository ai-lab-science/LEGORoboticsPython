#!/usr/bin/env pybricks-micropython
import os
from pybricks.tools import print
from pybricks.parameters import Port
import time



class TOF:
    
    def __init__(self, port):
        portIntMap = {
            Port.S1: 1,
            Port.S2: 2,
            Port.S3: 3,
            Port.S4: 4,
        }
        port = portIntMap.get(port,1)
        self.process = os.popen('python3 /home/robot/LEGORoboticsPython/Tools/TOF_Python3.py '+str(port))
    


    def printTime(self):
        t = time.localtime()
        current_time = time.strftime("MICRO: %H:%M:%S", t)
        print(current_time)

    def distance(self):
        preprocessed = int(self.process.readline())
        #preprocessed = self.process.readline()
        #self.printTime()
        return preprocessed

    def close(self):
        self.process.close()
    





