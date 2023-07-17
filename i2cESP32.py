#  Raspberry Pi Master for ESP32 Slave
#  i2c_master_pi.py
#  Connects to ESP32 via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus
import struct
import numpy as np

addr = 0x55 # Client address
bus = SMBus(1) # indicates /dev/ic2-1
BUFFER_LENGTH = 24

motors = np.array([0,0,0,0,0,0], dtype='int8') 
encoderResets = np.array([0,0,0,0,0,0], dtype='int8') 
encoders = np.array([0,0,0,0,0,0], dtype='int16') 

numb = 1

# Splits an int16 into its two parts for transmission
def bytes(i):
    high, low = divmod(i, 0x100)
    return [low, high]

# Pack the buffer ready for sending to the ESP32
def packBuffer():
    expanded_encoders = np.concatenate((bytes(encoders[0]),bytes(encoders[1]),bytes(encoders[2]),
                                        bytes(encoders[3]),bytes(encoders[4]),bytes(encoders[5])), axis=None)

    print(expanded_encoders)
    array_buffer = np.concatenate((motors, encoderResets, expanded_encoders), axis=None)
    return array_buffer.tolist()
    
# Unpack the buffer received from the ESP32    
def unpackBuffer(buffer):
    for i in range(len(motors)):
        motors[i] = buffer[i]
        
    offset = len(motors)    
    for i in range(len(encoderResets)):
        encoderResets[i] = buffer[offset + i]

    offset = len(motors) + len(encoderResets)   
    for i in range(len(encoders)):
        encoders[i] = (buffer[offset + (i*2)+1] * 256) + buffer[offset + (i*2)]   

# --------------------------------------------------------
# Main routine
# --------------------------------------------------------
print ("Enter 1 to Send or 0 to Receive")
while numb == 1:

    direction = input(">>>>   ")

    if direction == "1": # Send to ESP32
        motors[0] = 47
        motors[1] = -9
        motors[5] = 38

        encoders[0] = 325
        encoders[1] = 23777
        encoders[5] = 7969
   
        # Pack up the data
        data_to_send_to_ESP32 = packBuffer()      
        print(data_to_send_to_ESP32)

        # Send it
        bus.write_i2c_block_data(addr, 0x00, data_to_send_to_ESP32)
    

    elif direction == "0": # Read from ESP32

        # Request the data from the ESP32
        data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0x00, BUFFER_LENGTH)
        print(data_received_from_ESP32)

        # Unpack the buffer received from the ESP32
        unpackBuffer(data_received_from_ESP32)
        # print(encoders)

        print(encoders[0])
        print(encoders[1])
        print(encoders[2])
        print(encoders[3])
        print(encoders[4])
        print(encoders[5])
        
    else:
        numb = 0