#!/bin/bash

interface=can0
if [ $# -gt 0 ]; then
    interface=$1
fi

# Use the following for Canable Pro.  -s6 for 500000 bitrate
sudo slcand -o -c -s6 /dev/ttyACM0 can0

sudo ip link set $interface up
sudo ip link set $interface txqueuelen 1000
