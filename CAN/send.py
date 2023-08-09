import os
import can
import time

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

try:
    while True:
        with can.interface.Bus(channel = 'can0', bustype = 'socketcan') as can0:
            msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=False)
            can0.send(msg)
            time.sleep(1.0)

except KeyboardInterrupt:
    os.system('sudo ifconfig can0 down')