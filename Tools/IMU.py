#!/usr/bin/env pybricks-micropython

from ev3dev2.sensor import Sensor
from pybricks.parameters import Port
from pybricks.tools import print


class IMU:
    abs=Sensor()
    def __init__(self, port,mode):
        portStringMap = {
            Port.S1: "in1",
            Port.S2: "in2",
            Port.S3: "in3",
            Port.S4: "in4",
        }
        portString =portStringMap.get(port,'Invalid Port')
        self.abs = Sensor(address='ev3-ports:'+portString+':i2c1')
        self.abs.mode=mode
        

    
    def angle(self):
        res=[]
        for i in range(self.abs.num_values):
            res.append(self.abs.value(i))
        return res
    


