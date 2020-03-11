#!/usr/bin/env pybricks-micropython
import os
from pybricks.tools import print
from pybricks.parameters import Port


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

    def distance(self):
        preprocessed = int(self.process.readline())
        return preprocessed
        #print("yaaay"+str(preprocessed))
    def close(self):
        self.process.close()





