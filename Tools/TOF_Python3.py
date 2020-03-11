#!/usr/bin/env python3

from time import sleep
from smbus import SMBus
import sys
from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.port import LegoPort

port = int(sys.argv[1])

    
def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
def output(*args, **kwargs):
    print(*args, **kwargs, file=sys.stdout)

def distance():
    bus = SMBus(port+2)
    raw_data = bus.read_i2c_block_data( 0x01,0x42, 2)
    data = raw_data[0]+255*raw_data[1]
    return data

while True:
    #debug_print(distance())
    output(distance())
        
        
    


    


