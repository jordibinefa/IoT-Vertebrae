import serial
import ifaddr

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
