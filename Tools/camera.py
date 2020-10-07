#!/usr/bin/env python3
from time import sleep
from smbus import SMBus

from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.port import LegoPort
import os
import sys

port = int(sys.argv[1])
portMap = {
            1: INPUT_1,
            2: INPUT_2,
            3: INPUT_3,
            4: INPUT_4,
        }
lego_port =portMap.get(port,'Invalid Port')



# EV3 Display
lcd = Display()

# Connect ToucSensor
ts = TouchSensor(INPUT_4)

# Set LEGO port for Pixy2 on input port 1
in1 = LegoPort(lego_port)
in1.mode = 'other-i2c'
# Short wait for the port to get ready
sleep(0.5)

# Settings for I2C (SMBus(3) for INPUT_1)
bus = SMBus(port+2)
# Make sure the same address is set in Pixy2
address = 0x54

# Signatures we're interested in (SIG1)
sigs = 255

# Data for requesting block
data = [174, 193, 32, 2, sigs, 1]

f = open('tmp_camera_data.txt', 'r+', os.O_NONBLOCK)

def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
# Read and display data until TouchSensor is pressed
while not ts.value():
    #if not f.exists():
    #f = open('tmp_camera_data.txt', 'a+', os.O_NONBLOCK)
    # Clear display
    lcd.clear()
    # Request block
    bus.write_i2c_block_data(address, 0, data)
    # Read block
    block = bus.read_i2c_block_data(address, 0, 20)
    # Extract data
    sig = block[7]*256 + block[6]
    x = block[9]*256 + block[8]
    y = block[11]*256 + block[10]
    w = block[13]*256 + block[12]
    h = block[15]*256 + block[14]
    #f.truncate(0)
    f.seek(0)
    file_data = f.readlines()
    updated_line_string=str(x)+','+str(y)+','+str(h)+','+ str(h)+'\n'
    debug_print(len(file_data))
    if len(file_data)!=8:
        file_data=['\n'] * 8
        debug_print('Created 8 new Lines')
    #file_data.pop(sig)
    #file_data.insert(sig,updated_line_string)
    if sig<9:
        file_data[sig]=updated_line_string
    else:
        debug_print('signature to large')


    f.writelines(file_data)
    # f.write('\n'+str(sig)+',')
    # f.write(str(x)+',')
    # f.write(str(y)+',')
    # f.write(str(w)+',')
    # f.write(str(h))
    f.flush()
    # Scale to resolution of EV3 display:
    # Resolution Pixy2 while color tracking; (316x208)
    # Resolution EV3 display: (178x128)
    x *= 0.6
    y *= 0.6
    w *= 0.6
    h *= 0.6
    # Calculate rectangle to draw on display
    dx = int(w/2)
    dy = int(h/2)
    xa = x - dx
    ya = y + dy
    xb = x + dx
    yb = y - dy
    # Draw rectangle on display
    lcd.draw.rectangle((xa, ya, xb, yb), fill='black')
    # Update display to how rectangle
    lcd.update()
    #f.close()

f.close()