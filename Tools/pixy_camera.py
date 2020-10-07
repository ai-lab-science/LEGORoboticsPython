#!/usr/bin/env pybricks-micropython
import os
from pybricks.tools import print, wait
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port
import time
import math




class Camera:
    
    def __init__(self, port):
        self.ev3=EV3Brick()
        self.cam = I2CDevice(port, 0x54)
        wait(200)



    def printTime(self):
        t = time.localtime()
        current_time = time.strftime("MICRO: %H:%M:%S", t)
        print(current_time)
        
    # def getObjectData(self,signature, draw=True):
    #     self.cam.write(0,bytes((174,193, 32, 2,signature ,1)))

    #     block = self.cam.read(0,20)
    #     sig = block[7]*256 + block[6]
    #     x = block[9]*256 + block[8]
    #     y = block[11]*256 + block[10]
    #     w = block[13]*256 + block[12]
    #     h = block[15]*256 + block[14]
        
    def getObjectData(self,signature, draw=True):
        self.cam.write(0,bytes((174,193, 32, 2,signature ,1)))

        block = self.cam.read(0,20)
        sig = block[7]*256 + block[6]
        x = block[9]*256 + block[8]
        y = block[11]*256 + block[10]
        w = block[13]*256 + block[12]
        h = block[15]*256 + block[14]
        
        if draw:
            x *= 0.6
            y *= 0.6
            w *= 0.6
            h *= 0.6
            dx = int(w/2)
            dy = int(h/2)
            xa = x - dx
            ya = y + dy
            xb = x + dx
            yb = y - dy
            self.ev3.screen.clear()
            self.ev3.screen.draw_box(xa, ya, xb, yb)
        
        return x,y,w,h
    
    def lamp_on(self):
        self.cam.write(0,bytes((174, 193, 22, 2, 1, 0)))

    def lamp_off(self):
        self.cam.write(0,bytes((174, 193, 22, 2, 0, 0)))

    
    def get_line_tracking_data(self):
        mainfeatures = MainFeatures()
        vector = Vector()
        intersection = Intersection()
        branch = Branch()
        barcode = Barcode()
        payload_read = 0

        # Request
        self.cam.write(0,bytes((174, 193, 48, 2, 0, 7)))

        # Read header info
        response = self.cam.read(0,6)


        # Parse header info
        if response[2] == 49:
            mainfeatures.type_of_packet = response[2]
        else:
            mainfeatures.error = True
            return mainfeatures
        mainfeatures.length_of_payload = response[3]

        # Read payload data
        while payload_read < mainfeatures.length_of_payload:
            response = self.cam.read(0,2)

            feature_type = response[0]
            feature_length = response[1]

            if feature_type == 1:
                # Feature type is 'vector'
                response = self.cam.read(0,feature_length)

                vector.x0 = response[0]
                vector.y0 = response[1]
                vector.x1 = response[2]
                vector.y1 = response[3]
                vector.index = response[4]
                vector.flags = response[5]
                mainfeatures.add_vector(vector)
            elif feature_type == 2:
                # feature type is 'intersection'
                response = self.cam.read(0,feature_length)

                #response = self.smbus.read_i2c_block_data(self.i2c_address,
                 #                                         0, feature_length)
                intersection.x = response[0]
                intersection.y = response[1]
                intersection.nr_of_branches = response[2]
                for i in range(0, intersection.nr_of_branches):
                    i4 = i*4
                    #print(response)
                    #print(i4)
                    branch.index = response[i4+0]
                    branch.angle = response[14+1]
                    branch.angle_byte1 = response[i4+2]
                    branch.angle_byte2 = response[i4+3]
                    intersection.add_branch(branch)
                mainfeatures.add_intersection(intersection)
            elif feature_type == 4:
                # Feature type is 'barcode'
                response = self.cam.read(0,feature_length)

                #response = self.smbus.read_i2c_block_data(self.i2c_address,
                 #                                         0, feature_length)
                barcode.x = response[0]
                barcode.y = response[1]
                barcode.flags = response[2]
                barcode.code = response[3]
                mainfeatures.add_barcode(barcode)
            else:
                # Unknown feature type
                mainfeatures.error = True

            payload_read += feature_length + 2
        return mainfeatures

    def get_line_tracking_angle(self):
        data = self.get_line_tracking_data()
        angle = 0
        if len(data.vectors)>0:
            v = data.vectors[0]
            angle = math.degrees(math.atan2((abs(v.y1)-abs(v.y0)),(abs(v.x1)-abs(v.x0))))+90
        return angle,data


    def set_vector(self, index):
        """Set vector for Pixy2 to follow."""
        self.cam.write(0,bytes((174, 193, 56, 1, index)))
        response = self.cam.read(0,10)

        #request_block = [174, 193, 56, 1, index]
        #self.smbus.write_i2c_block_data(self.i2c_address, 0, request_block)
        #response = self.smbus.read_i2c_block_data(self.i2c_address, 0, 10)
        
        return response

    def set_next_turn(self, angle):
        """Set direction robot has to take at intersection."""
        if angle >= 0:
            request_block = (174, 193, 58, 2, angle, 0)
        else:
            request_block = (174, 193, 58, 2, angle, -1)
        self.cam.write(0,bytes(request_block))
        response = self.cam.read(0,10)

        #self.smbus.write_i2c_block_data(self.i2c_address, 0, request_block)
        #response = self.smbus.read_i2c_block_data(self.i2c_address, 0, 10)
        self._next_turn = angle
        return response

    def set_default_turn(self, angle):
        """"Set direction robot has to take at intersection."""
        if angle >= 0:
            request_block = (174, 193, 60, 2, angle, 0)
        else:
            request_block = (174, 193, 60, 2, angle, -1)
        
        self.cam.write(0,bytes(request_block))
        response = self.cam.read(0,10)

        #self.smbus.write_i2c_block_data(self.i2c_address, 0, request_block)
        #response = self.smbus.read_i2c_block_data(self.i2c_address, 0, 10)
        self._next_turn = angle
        return response


class Vector:
    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.index = 0
        self.flags = 0


class Intersection:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.nr_of_branches = 0
        self.branches = []

    def add_branch(self, branch):
        b = Branch()
        b.index = branch.index
        b.angle = branch.angle
        self.branches.append(b)


class Branch:
    def __init__(self):
        self.index = 0
        self.angle = 0
        self.angle_byte1 = 0
        self.angle_byte2 = 0


class Barcode:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.flags = 0
        self.code = 0


class MainFeatures:
    def __init__(self):
        self.error = False
        self.type_of_packet = 49
        self.length_of_payload = 0
        self.number_of_vectors = 0
        self.number_of_intersections = 0
        self.number_of_barcodes = 0
        self.vectors = []
        self.intersections = []
        self.barcodes = []

    def add_vector(self, vector):
        v = Vector()
        v.x0 = vector.x0
        v.y0 = vector.y0
        v.x1 = vector.x1
        v.y1 = vector.y1
        v.index = vector.index
        v.flags = vector.flags
        self.vectors.append(v)
        self.number_of_vectors += 1

    def add_intersection(self, intersection):
        ints = Intersection()
        b = Branch()
        ints.x = intersection.x
        ints.y = intersection.y
        ints.nr_of_branches = intersection.nr_of_branches
        for branch in intersection.branches:
            b.index = branch.index
            b.angle = branch.angle
            b.angle_byte1 = branch.angle_byte1
            b.angle_byte2 = branch.angle_byte2
            ints.add_branch(b)
        self.intersections.append(ints)
        self.number_of_intersections += 1

    def add_barcode(self, barcode):
        b = Barcode()
        b.x = barcode.x
        b.y = barcode.y
        b.flags = barcode.flags
        b.code = barcode.code
        self.barcodes.append(b)
        self.number_of_barcodes += 1

    def clear(self):
        self.length_of_payload = 0
        self.number_of_vectors = 0
        self.number_of_intersections = 0
        self.number_of_barcodes = 0
        self.vectors.clear()
        self.intersections.clear()
        self.barcodes.clear()






