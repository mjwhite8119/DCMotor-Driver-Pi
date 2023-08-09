import os
import can

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

try:
    while True:
        with can.interface.Bus(channel = 'can0', bustype = 'socketcan') as can0:
            msg = can0.recv(10.0)
            print (msg)
            if msg is None:
                print('Timeout occurred, no message.')

except KeyboardInterrupt:
    os.system('sudo ifconfig can0 down')