#!/usr/bin/env python3

# from pybricks import ev3brick as brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
#from pybricks.parameters import (Port, Stop, Direction, Button, Color,
#                                  SoundFile, ImageFile, Align)
#from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase
from time import sleep
from smbus import SMBus
import sys
from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.port import LegoPort
#from pybricks.tools import print


#port2 = LegoPort(address='ev3-ports:in2')
##port2.mode = 'other-i2c'
#port1 = LegoPort(address='ev3-ports:in1')
#port1.mode = 'other-i2c'
#bus = SMBus('/dev/i2c-in2')

#bus = SMBus('/dev/i2c-2')
bus = SMBus(3)
class TOF:
    
    def debug_print(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)

    def distance():
        global bus
        raw_data = bus.read_i2c_block_data( 0x01,0x42, 2)
        data = raw_data[0]+255*raw_data[1]
        #print(data)
        #debug_print(raw_data)
        #debug_print(data)
        return data
    
    
    
    while True:
        debug_print(distance())

    def __init__(self, port,mode):
        portIntMap = {
            Port.S1: 3,
            Port.S2: 4,
            Port.S3: 5,
            Port.S4: 6,
        }
        self.bus=SMBus(portStringMap.get(port, 3))
        
        
    


    #brick.display.clear()
    #data = bus.read_byte(0x42)
    #data = bus.read_byte_data(0x08, 0x42)
    #data = (raw_data[1]<<8)+raw_data[0]
    #data = bus.read_byte_data(0x01, 0x42)
    #bytes(bus.read_i2c_block_data(0x42, 2)).decode().strip()
    
    #adc0_upper8 = bus.read_byte_data(0x01, 0x42)
    #adc0_lower2 = bus.read_byte_data(0x01, 0x42)
    #data = (adc0_upper8 << 2) + adc0_lower2
    
    
    #debug_print('upper'+str(adc0_upper8))
    #debug_print('upper'+str(adc0_lower2))

    #brick.display.text('IMU: ' + str(imu1.angle()),(0, 50))
    #wait(0.1)


