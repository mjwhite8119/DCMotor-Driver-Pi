import struct
import numpy as np


def int16(n):
      return struct.unpack('H', struct.pack('h', n))

class Data:
  def __init__(self):
     
    motors = np.array([0,0,0,0,0,0], dtype='int8') 
    encoderResets = np.array([0,0,0,0,0,0], dtype='int8') 
    encoders = np.array([0,0,0,0,0,0], dtype='int16') 
    # motor1 = 0 
    # motor2 = 0
    # motor1 = 0 
    # motor2 = 0
    # motor1 = 0 
    # motor2 = 0
    # resetEncoder1 = False 
    # resetEncoder2 = False
    # resetEncoder3 = False
    # resetEncoder4 = False
    # resetEncoder5 = False
    # resetEncoder6 = False
    # encoder1 = int16(0)
    # encoder2 = int16(0)
    # encoder3 = int16(0)
    # encoder4 = int16(0)
    # encoder5 = int16(0)
    # encoder6 = int16(0)

def packBuffer(data):
    high1, low1 = bytes(data.encoder1)
    high2, low2 = bytes(data.encoder2)
    high3, low3 = bytes(data.encoder3)
    high4, low4 = bytes(data.encoder4)
    high5, low5 = bytes(data.encoder5)
    high6, low6 = bytes(data.encoder6)

    buffer = np.concatenate((data.motors, data.encoderResets, data.encoders,), axis=None)
    #   buffer = [data.motor1, data.motor2, data.motor3, 
    #             data.motor4, data.motor5, data.motor6,
    #             data.resetEncoder1, data.resetEncoder2, data.resetEncoder3,
    #             data.resetEncoder4, data.resetEncoder5, data.resetEncoder6,
    #             high1, low1, high2, low2, high3, low3,
    #             high4, low4, high5, low5, high6, low6] 
    return buffer