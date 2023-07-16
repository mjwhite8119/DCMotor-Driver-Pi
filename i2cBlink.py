#  Raspberry Pi Master for ESP32 Slave
#  i2c_master_pi.py
#  Connects to ESP32 via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus

addr = 0x55 # Client address
bus = SMBus(1) # indicates /dev/ic2-1
BUFFER_LENGTH = 37
data_received_from_ESP32 = ""
data_to_send_to_ESP32 = "Hello ESP32"

numb = 1

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
		bus.write_byte(addr,3)
		print(StringToBytes(data_to_send_to_ESP32))
		bus.write_i2c_block_data(addr, 0x00,StringToBytes(data_to_send_to_ESP32))
			
	# bus.write_byte(addr, 0x1) # switch it on
	elif ledstate == "0":
		data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0, BUFFER_LENGTH)
        print(data_received_from_ESP32)
        buffer(data_received_from_ESP32)

		# readMessage()
				
	# bus.write_byte(addr, 0x0) # switch it on
	else:
		numb = 0