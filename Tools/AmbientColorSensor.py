#!/usr/bin/env pybricks-micropython

from ev3dev2.sensor import Sensor
from pybricks.parameters import Port
from pybricks.tools import print
from ev3dev2.sensor.lego import ColorSensor

class AmbientColorSensor:
    colorSensor = ColorSensor('in1')

    def __init__(self, port):
        portStringMap = {
            Port.S1: "in1",
            Port.S2: "in2",
            Port.S3: "in3",
            Port.S4: "in4",
        }
        portString =portStringMap.get(port,'Invalid Port')
        #self.colorSensor.mode='RGB-RAW'
        

    
    def color(self):
        # res=[]
        # for i in range(self.abs.num_values):
        #     res.append(self.abs.value(i))
        res = self.colorSensor.rgb
        return res
    


