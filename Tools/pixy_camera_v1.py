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

        self.x=[None] * 8
        self.y=[None] * 8
        self.w=[None] * 8
        self.h=[None] * 8

        #self.file = open('tmp_camera_data.txt', 'r', os.O_NONBLOCK)
        self.file_name='tmp_camera_data.txt'
        self.file = open(self.file_name, 'a+', os.O_NONBLOCK)

        self.process = os.popen('python3 /home/robot/LEGORoboticsPython/Tools/camera.py '+str(port))
    


    def printTime(self):
        t = time.localtime()
        current_time = time.strftime("MICRO: %H:%M:%S", t)
        print(current_time)

    def update(self):
        #self.file = open(self.file_name, 'a+', os.O_NONBLOCK)

        self.file.seek(0)
        Lines= self.file.readlines()
        for line in Lines:
            data = line.split(',')
            #print(data)
            if len(data)==5 and data[1]!='' and data[1]!='32896':  
                sig=int(data[0])
                #print("Signatur: "+str(sig))
            
                self.x[sig]=int(data[1])
                self.y[sig]=int(data[2])
                self.w[sig]=int(data[3])
                self.h[sig]=int(data[4])
                #print(self.x[sig])
        #self.file.close()
       # os.remove(self.file_name)
        
        return Lines

    def getX(self,sig):
        self.update()
        return self.x[sig]

    def getY(self, sig):
        self.update()
        return self.y[sig]

    def getWidth(self, sig):
        self.update()
        return self.w[sig]

    def getHeight(self, sig):
        self.update()
        return self.h[sig]

    def close(self):
        self.process.close()
    





