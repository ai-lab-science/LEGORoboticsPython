#!/usr/bin/env python3

from time import sleep
from smbus import SMBus
import sys
from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.port import LegoPort
import time

port = int(sys.argv[1])

    
def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
def output(*args, **kwargs):
    print(*args, **kwargs, file=sys.stdout)

def printTime():
        t = time.localtime()
        current_time = time.strftime("PY3: %H:%M:%S", t)
        #debug_print(current_time)
        return current_time

def distance():
    bus = SMBus(port+2)
    try:
        raw_data = bus.read_i2c_block_data( 0x01,0x42, 2)
        data = raw_data[0]+255*raw_data[1]
    except:
        data = "Device not found"
    #return printTime()
    return data


while True:
    #debug_print(distance())
    output(distance())
    time.sleep(0.05)
        
        
    


    


