#  Raspberry Pi Master for Arduino Slave
#  i2c_master_pi.py
#  Connects to Arduino via I2C
  
#  DroneBot Workshop 2019
#  https://dronebotworkshop.com

from smbus import SMBus

addr = 0x55 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
data_received_from_ESP32 = ""
data_to_send_to_ESP32 = "Hello ESP32"

numb = 1

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
		data_received_from_ESP32 = bus.read_i2c_block_data(addr, 0,12)
		print(data_received_from_ESP32)
		# bus.write_byte(addr, 0x0) # switch it on
	else:
		numb = 0