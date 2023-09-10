# DCMotor-Driver-Pi
Raspberry Pi code to communicate with the DCMotor-Driver-Board

PS3 Controller MAC  dc:a6:32:75:2e:ad

## I2C Setup

Full instructions are on the [Raspberry_Pi_Master_for_ESP32_I2C_SLAVE](https://github.com/MkLHX/Raspberry_Pi_Master_for_ESP32_I2C_SLAVE/tree/master) Github page.

## XBox Controller 
The xBox One controller works.  The knowoff PS3 controllers will not connect.
Test with jstest /dev/input/js0.

## CANBus
Using the [Waveshare RS485-CAN-HAT](https://www.waveshare.com/wiki/RS485_CAN_HAT), that uses the MCP2515 CAN controller and the SN65HVD230 transceiver. On the RPi it uses the [SocketCan python library](python-can.readthedocs.io)

Edit the `/boot/config.txt` file to turn on SPI, and add the device configuration for the MCP2515 CAN controller.  The version I have has a 12Mh clock:

    dtparam=spi=on
    dtoverlay=mcp2515-can0,oscillater=12000000,spimaxfrequency=1000000

Check if the MCP2515 has been installed after rebooting the Raspberry Pi:

    dmesg | grep -i '\(can\|spi\)'

You should see something like:

    [    7.756563] CAN device driver interface
    [    7.780813] mcp251x spi0.0 can0: MCP2515 successfully initialized.

Install the can-utils

    sudo apt install can-utils

Useful commands:

    sudo ip link set can0 type can bitrate 500000
    sudo ifconfig can0 up/down
    ifconfig
    ip -details -statistics link show can0

Read and Enable heartbeat.  Zero is disabled.

    cocomm "1 read 0x1017 0 u16"
    cocomm "1 write 0x1017 0 u16 1000"

## CANOpen Editor
Clone https://github.com/CANopenNode/CANopenEditor

Install `mono`, which is a linux utility from running Windows C# programs.
    sudo apt install mono-complete    

Start app:
    mono CANEditor.exe







