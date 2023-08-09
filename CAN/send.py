import os
import can
import time

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')# socketcan_native
try:
    while True:
        msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
        can0.send(msg)
        time.sleep(0.1)

except KeyboardInterrupt:
    os.system('sudo ifconfig can0 down')