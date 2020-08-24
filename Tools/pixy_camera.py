#!/usr/bin/env pybricks-micropython
import os
from pybricks.tools import print
from pybricks.parameters import Port
import time



class Camera:
    
    def __init__(self, port):
        portIntMap = {
            Port.S1: 1,
            Port.S2: 2,
            Port.S3: 3,
            Port.S4: 4,
        }
        port = portIntMap.get(port,1)

        self.file = open('tmp_camera_data.txt', 'r', os.O_NONBLOCK)

        self.process = os.popen('python3 /home/robot/LEGORoboticsPython/Tools/camera.py '+str(port))
    


    def printTime(self):
        t = time.localtime()
        current_time = time.strftime("MICRO: %H:%M:%S", t)
        print(current_time)

    def update(self):
        self.file.seek(0)
        text= self.file.read()
    
        data = text.split(',')
        if data[0]!='' and data[0]!='32896':  
            self.x=int(data[0])
            self.y=int(data[1])
            self.w=int(data[2])
            self.h=int(data[3])
            print(self.x)
        
        return data

    def getX(self):
        self.update()
        return self.x

    def getY(self):
        self.update()
        return self.y

    def getWidth(self):
        self.update()
        return self.w

    def getHeight(self):
        self.update()
        return self.h

    def close(self):
        self.process.close()
    





