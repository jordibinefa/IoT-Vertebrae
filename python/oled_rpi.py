import serial
import ifaddr
import os
import time

pidFile = '/home/pi/bin/oled_rpi.pid'
if not os.path.isfile(pidFile):
    global pid

    pid = "%d"%os.getpid()
    f = open(pidFile, "a")
    f.write(pid)
    f.close()
    adapters = ifaddr.get_adapters()
    IPAddr = '127.0.0.1'
    for adapter in adapters:
        if adapter.nice_name == 'wlan0':
            IPAddr = adapter.ips[0].ip
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.open()
    ser.write(IPAddr.encode())
    ser.close()
    time.sleep(2)
    os.remove(pidFile)
