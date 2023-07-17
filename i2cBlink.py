#  Raspberry Pi Master for ESP32 Slave
#  i2c_master_pi.py
#  Connects to ESP32 via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus
import struct
import numpy as np
from shmem_buffer import *


addr = 0x55 # Client address
bus = SMBus(1) # indicates /dev/ic2-1
BUFFER_LENGTH = 37
# data_received_from_ESP32 = ""

data =  Data()
motors = np.array([0,0,0,0,0,0], dtype='int8') 
encoderResets = np.array([0,0,0,0,0,0], dtype='int8') 
encoders = np.array([0,0,0,0,0,0], dtype='int16') 

numb = 1

def bytes(i):
    #  return divmod(i, 0x100)
    high, low = divmod(i, 0x100)
    return [high, low]

def int16(n):
      return struct.unpack('H', struct.pack('h', n))

def readMessage():
    global smsMessage
    # client address, register, length
    data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0, BUFFER_LENGTH)
    for i in range(len(data_received_from_ESP32)):
        smsMessage += chr(data_received_from_ESP32[i])

    print(smsMessage.encode('utf-8'))
    print(smsMessage)
    data_received_from_ESP32 =""
    smsMessage = ""

def readNumber():
    global smsNumber
    data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0,15)
    for i in range(len(data_received_from_ESP32)):
        smsNumber += chr(data_received_from_ESP32[i])

    print(smsNumber.encode('utf-8'))
    data_received_from_ESP32 = ""
    smsNumber = ""

smsMessage = ""
smsNumber = ""

def StringToBytes(val):
    retVal = []
    for c in val:
            retVal.append(ord(c))
    return retVal

print ("Enter 1 for ON or 0 for OFF")
while numb == 1:

    ledstate = input(">>>>   ")

    if ledstate == "1":
        motors[0] = 100
        # high, low = bytes(buffer.motor1)
        motors[1] = -90
        motors[5] = 38
        encoders[0] = 1045
        encoders[1] = 3445
        encoders[5] = 512
 
        high1, low1 = bytes(encoders[0])
        high2, low2 = bytes(encoders[1])
        high3, low3 = bytes(encoders[2])
        high4, low4 = bytes(encoders[3])
        high5, low5 = bytes(encoders[4])
        high6, low6 = bytes(encoders[5])
        print(high1)
        print(low1)
        expanded_encoders = np.concatenate((bytes(encoders[0]),bytes(encoders[1]),bytes(encoders[2]),
                                            bytes(encoders[3]),bytes(encoders[4]),bytes(encoders[5])), axis=None)

        print(expanded_encoders)
        array_buffer = np.concatenate((motors, encoderResets, expanded_encoders), axis=None)
        print(array_buffer)
        data_to_send_to_ESP32 = array_buffer.tolist()
        # data_to_send_to_ESP32 = packBuffer(data)
        # high1, low1 = bytes(buffer.motor2)

        # data_to_send_to_ESP32 = [high, low, high1, low1]
        # bus.write_byte(addr,3)
        print(data_to_send_to_ESP32)
        bus.write_i2c_block_data(addr, 0x00, data_to_send_to_ESP32)
    # bus.write_byte(addr, 0x1) # switch it on
    elif ledstate == "0":
        # readNumber()
        data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0, 32)
        print(data_received_from_ESP32)
        # string = ''.join([hex(item) for item in data_received_from_ESP32])
        # print(string)
        motor1 = data_received_from_ESP32[0:2]
        print(motor1)
        # readMessage()
                
    # bus.write_byte(addr, 0x0) # switch it on
    else:
        numb = 0