from Adafruit_PureIO.smbus import SMBus  # pip install adafruit-blinka
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.packer import Packer
from Raspberry_Pi_Master_for_ESP32_I2C_SLAVE.unpacker import Unpacker
import time

DEVICE_ADDR = 0x21
REGISTER = 0x01

slave_address = 0x21  # slave address is 4
register = 0x01  # register to write is 0x01
value = 0x04


def write_from_rpi_to_esp32():
    try:
        # change 1 of SMBus(1) to bus number on your RPI
        smbus = SMBus(1)
        # prepare the data
        packed = None
        with Packer() as packer:
            packer.write(register)
            packer.write(value)
            packer.end()
            packed = packer.read()
        smbus.write_bytes(register, bytearray(packed))
        print("Written")
    except Exception as e:
        print("ERROR: {}".format(e))

# Test initializer open.
# i2c = SMBus(1)
# val = i2c.read_byte(DEVICE_ADDR)
# print("read_byte from 0x{0:0X}: 0x{1:0X}".format(REGISTER, val))
# i2c.close()

# Test various data writes.
# with SMBus(1) as i2c:
#     i2c.write_byte(DEVICE_ADDR, REGISTER)
#     i2c.write_byte_data(DEVICE_ADDR, REGISTER, 0x85)
#     i2c.write_word_data(DEVICE_ADDR, REGISTER, 0x8385)
#     i2c.write_i2c_block_data(DEVICE_ADDR, REGISTER, [0x85, 0x83])
#     # i2c.write_block_data(DEVICE_ADDR, REGISTER, [0x85, 0x83])
#     i2c.write_quick(DEVICE_ADDR)
#     print("Done")


while (True):
    write_from_rpi_to_esp32()
    time.sleep(0.5)