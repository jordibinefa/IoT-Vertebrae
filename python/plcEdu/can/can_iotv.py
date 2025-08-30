#!/usr/bin/env python
"""
MIRAR: https://github.com/hardbyte/python-can/blob/main/examples/asyncio_demo.py
pi@raspberrypi:~/codis/canbus $ sudo ip link set can0 type can bitrate 100000
pi@raspberrypi:~/codis/canbus $ sudo ifconfig can0 up
pi@raspberrypi:~/codis/canbus $ sudo ifconfig can0 down

"""
import os
import can
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO

USE_LEDS = False
VERBOSE = False
LED_W = 12
LED_B = 13
TIMEOUT_RCV = 0.5

if USE_LEDS:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_W,GPIO.OUT)
    GPIO.setup(LED_B,GPIO.OUT)

def dVertCfgFromNumber(n):
    cfg = "A:?, B:?"
    if n == 17:
        cfg = "A:din, B:din"
    elif n == 33:
        cfg = "A:din, B:dout"
    elif n == 18:
        cfg = "A:dout, B:din"
    elif n == 34:
        cfg = "A:dout, B:dout"
    elif n == 20:
        cfg = "A:pwm, B:din"
    elif n == 36:
        cfg = "A:pwm, B:dout"
    elif n == 65:
        cfg = "A:din, B:pwm"
    elif n == 66:
        cfg = "A:dout, B:pwm"
    elif n == 130:
        cfg = "A:dout, B:touch"
    elif n == 129:
        cfg = "A:din, B:touch"
    elif n == 132:
        cfg = "A:pwm, B:touch"
    return cfg

def ain2v(ainValue):
    return round((((20*float(ainValue))/26624)-10)*100)/100

def v2aout(voltage0_10):
    retV = round((voltage0_10*4095)/10)
    if retV < 0:
        retV = 0
    if retV > 4095:
        retV = 4095
    return retV

def aVertCfgFromNumber(byRibA,byRibB):
    cfg = "A:"
    if byRibA == 1:
        cfg += "ain, B:"
    elif byRibA == 2:
        cfg += "aout, B:"
    else:
        cfg += "?, B:"
    if byRibB == 1:
        cfg += "ain"
    elif byRibB == 2:
        cfg += "aout"
    else:
        cfg += "?"
    return cfg

def ainMsg(addr,side) -> can.Message:
    i2cAddr = int(addr,2)
    msg = []
    return can.Message(
        arbitration_id = 16 + i2cAddr + (0 if side.lower() == 'a' else 256),
        data = msg,
        is_extended_id = False,
        is_remote_frame = True,
        dlc = 0,
        timestamp = datetime.timestamp(datetime.now())
    )
    
def aoutMsg(addr,side,ndac,value) -> can.Message:
    # ndac: 1, 2, 3 or 4
    # value: between 0 and 4095 (or 0x0000 and 0x0FFF). 0 is 0 volts. 4095 is 10 volts.
    global VERBOSE
    i2cAddr = int(addr,2)
    msg = []
    # print("A") if a > b else print("=") if a == b else print("B")
    msg.append((2 if side.lower() == 'a' else 18)+
               (0 if ndac==1 else 32 if ndac==2 else 64 if ndac==3 else 96 if ndac==4 else 0))
    msg.append(value//256)
    msg.append(value%256)
    if VERBOSE:
        print(msg)
    return can.Message(
        arbitration_id = 784 + i2cAddr,
        data = msg,
        is_extended_id = False,
        is_remote_frame = False,
        dlc = 3,
        timestamp = datetime.timestamp(datetime.now())
    )
   
def doutMsg(addr,side,value) -> can.Message:
    global VERBOSE
    i2cAddr = int(addr,2)
    msg = []
    msg.append(2 if side.lower() == 'a' else 18)
    msg.append(value)
    if VERBOSE:
        print(msg)
    return can.Message(
        arbitration_id = 800 + i2cAddr,
        data = msg,
        is_extended_id = False,
        is_remote_frame = False,
        dlc = 2,
        timestamp = datetime.timestamp(datetime.now())
    )

def doutbitMsg(addr,side,posbyte,value) -> can.Message:
    global VERBOSE
    i2cAddr = int(addr,2)
    val = (10 if side.lower() == 'a' else 26) + 32 * posbyte
    msg = []
    msg.append(val)
    msg.append(value)
    if VERBOSE:
        print(msg)
    return can.Message(
        arbitration_id = 800 + i2cAddr,
        data = msg,
        is_extended_id = False,
        is_remote_frame = False,
        dlc = 2,
        timestamp = datetime.timestamp(datetime.now())
    )
               
def dinMsg(addr) -> can.Message:
    i2cAddr = int(addr,2)
    msg = []
    return can.Message(
        arbitration_id = 800 + i2cAddr,
        data = msg,
        is_extended_id = False,
        is_remote_frame = True,
        dlc = 0,
        timestamp = datetime.timestamp(datetime.now())
    )

def dversionMsg(addr) -> can.Message:
    i2cAddr = int(addr,2)
    msg = []
    return can.Message(
        arbitration_id = 800 + i2cAddr,
        data = msg,
        is_extended_id = False,
        is_remote_frame = True,
        dlc = 0,
        timestamp = datetime.timestamp(datetime.now())
    )

def aversionMsg(addr) -> can.Message:
    i2cAddr = int(addr,2)
    msg = []
    return can.Message(
        arbitration_id = 16 + i2cAddr + 512,
        data = msg,
        is_extended_id = False,
        is_remote_frame = True,
        dlc = 0,
        timestamp = datetime.timestamp(datetime.now())
    )

def send_can(bus,msg):
    global USE_LEDS
    if USE_LEDS:
        GPIO.output(LED_W,GPIO.HIGH)
    bus.send(msg)
    sleep(0.001) # per a que no es llegeixi el que trameto
    if USE_LEDS:
        GPIO.output(LED_W,GPIO.LOW)

def recv_can(bus):
    global USE_LEDS
    if USE_LEDS:
        GPIO.output(LED_B,GPIO.HIGH)
    
    msg = bus.recv(TIMEOUT_RCV)
    if USE_LEDS:
        GPIO.output(LED_B,GPIO.LOW)
    return msg

def ain(addr, side, ndac):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,ainMsg(addr,side))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg) 
        if msg.is_remote_frame:
            print("Remote")
        else:
            print("Non remote")
    if msg is not None:
        # dinData = bin(msg.data[3] if side.lower() == 'a' else msg.data[4])[2::].zfill(8)
        # dinData = bin(msg.data[3] if side.lower() == 'a' else msg.data[4])
        if VERBOSE:
            print("msg.data: ",msg.data)
            print("msg.dlc: ",msg.dlc)
            pass
        pos = ndac * 2 - 2
        ainData = 256 * msg.data[pos] + msg.data[pos + 1]
    else:
        ainData = "Error"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return ainData

def din(addr, side):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,dinMsg(addr))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg) 
        if msg.is_remote_frame:
            print("Remote")
        else:
            print("Non remote")
    if msg is not None:
        # dinData = bin(msg.data[3] if side.lower() == 'a' else msg.data[4])[2::].zfill(8)
        # dinData = bin(msg.data[3] if side.lower() == 'a' else msg.data[4])
        if VERBOSE:
            print("msg.data: ",msg.data)
            print("msg.dlc: ",msg.dlc)
            # print("Digital vert %s --> Cfg: %s. Version: %s"%(addr,dVertCfgFromNumber(msg.data[0]),version))
            pass
        valor = msg.data[3] if side.lower() == 'a' else msg.data[4]
        dinData = format(~valor & 255, 'b').zfill(8)
        # dinData = bin(msg.data[3] if side.lower() == 'a' else msg.data[4])[2::].zfill(8)
    else:
        dinData = "Error"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return dinData

def aout(addr, side, ndac, value):
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,aoutMsg(addr,side,ndac,value))

def dout(addr,side,value):
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,doutMsg(addr,side,value))

def doutbit(addr,side,posbyte,value):    
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,doutbitMsg(addr,side,posbyte,value))
    
def dsetup(addr, modeA, modeB):
    # Restrictions:
    # aoutpwm or boutpwm: Only one rib, A or B, is able to manage PWM. Because it is used an ESP32-S3 by vertebra.
    # bintouch (and it is not aintouch): Only B rib is able to manage 8 touch inputs. Because it is used an ESP32-S3 by vertebra.
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    
    i2cAddr = int(addr,2)
    if not( modeA.lower() == 'pwm' and modeB.lower() == 'pwm' ):
        if  modeA.lower() == 'dout' or modeA.lower() == 'pwm' :
            d1 = 0
        else:
            d1 = 255
        if  modeB.lower() == 'dout' or modeB.lower() == 'pwm' :
            d2 = 0
        else:
            d2 = 255
        msg = [0]
        msg.append(d1)
        msg.append(d2)
        if VERBOSE:
            print(msg)
        canMsg = can.Message(
            arbitration_id = 800 + i2cAddr,
            data = msg,
            is_extended_id = False,
            is_remote_frame = False,
            dlc = 3,
            timestamp = datetime.timestamp(datetime.now())
        )
        send_can(bus,canMsg)
        if  modeA.lower() == 'pwm' :
            msg = [4,0]
            canMsg = can.Message(
                arbitration_id = 800 + i2cAddr,
                data = msg,
                is_extended_id = False,
                is_remote_frame = False,
                dlc = 2,
                timestamp = datetime.timestamp(datetime.now())
            )
            send_can(bus,canMsg)
        else:
            if  modeB.lower() == 'pwm' :
                msg = [4,1]
                canMsg = can.Message(
                    arbitration_id = 800 + i2cAddr,
                    data = msg,
                    is_extended_id = False,
                    is_remote_frame = False,
                    dlc = 2,
                    timestamp = datetime.timestamp(datetime.now())
                )
                send_can(bus,canMsg)
        if  modeB.lower() == 'touch' :
            msg = [7,1]
            canMsg = can.Message(
                arbitration_id = 800 + i2cAddr,
                data = msg,
                is_extended_id = False,
                is_remote_frame = False,
                dlc = 2,
                timestamp = datetime.timestamp(datetime.now())
            )
            send_can(bus,canMsg)
        if  modeA.lower() == 'touch' :
            print("touch is only accepted at B side")
        else:
            print("a: %s, b: %s"%(modeA,modeB))
    else:
        print("PWM at only one side")
                        
def dversion(addr):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,dversionMsg(addr))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg)
    if msg is not None:
        version = "%d.%d"%(msg.data[1],msg.data[2])
        if VERBOSE:
            # print(msg.data)
            print("Digital vert %s --> Cfg: %s. Version: %s"%(addr,dVertCfgFromNumber(msg.data[0]),version))
    else:
        version = "0.0"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return version

def getdsetup(addr):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,dversionMsg(addr))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg)
    if msg is not None:
        version = "%d.%d"%(msg.data[1],msg.data[2])
        dsetup = dVertCfgFromNumber(msg.data[0])
        if VERBOSE:
            # print(msg.data)
            print("Digital vert %s --> Cfg: %s. Version: %s"%(addr,dsetup,version))
    else:
        version = "0.0"
        dsetup = "A:?, B:?"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return dsetup

def aversion(addr):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,aversionMsg(addr))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg)
    if msg is not None:
        version = "%d.%d"%(msg.data[1],msg.data[2])
        if VERBOSE:
            # print(msg.data)
            print("Analog vert %s --> Cfg: %s. Version: %s"%(addr,aVertCfgFromNumber(msg.data[0],msg.data[3]),version))
    else:
        version = "0.0"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return version

def getasetup(addr):
    global VERBOSE
    bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
    send_can(bus,aversionMsg(addr))
    msg = recv_can(bus)
    if VERBOSE:
        print(msg)
    if msg is not None:
        version = "%d.%d"%(msg.data[1],msg.data[2])
        asetup = aVertCfgFromNumber(msg.data[0],msg.data[3])
        if VERBOSE:
            # print(msg.data)
            print("Analog vert %s --> Cfg: %s. Version: %s"%(addr,asetup,version))
    else:
        version = "0.0"
        asetup = "A:?, B:?"
        if VERBOSE:
            print("No CAN answer in %.2f seconds"%TIMEOUT_RCV)
    return asetup

def canOn():
    # canOff()
    os.system('sudo /sbin/ip link set up can0 type can bitrate 100000')
    sleep(0.1)

def canOff():
    os.system('sudo /sbin/ifconfig can0 down')

if __name__ == "__main__":
    try:
        # bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
        espera = 0.5
        canOn()
        
        for i in range(10):
            for bit in range(8):
                doutbit('0000','A',bit,1)
                sleep(.05)
                doutbit('0000','A',bit,0)
        """dsetup('0000','din','dout')
        print("Digital vertebra version: %s"%dversion('0000'))
        print("Digital vertebra setup: %s"%getdsetup('0000'))
        print("Analog vertebra version: %s"%aversion('0000'))
        print("Analog vertebra setup: %s"%getasetup('0000'))
        sleep(espera)
        dsetup('0000','dout','din')
        print("Digital vertebra version: %s"%dversion('0000'))
        print("Digital vertebra setup: %s"%getdsetup('0000'))
        print("Analog vertebra version: %s"%aversion('0000'))
        print("Analog vertebra setup: %s"%getasetup('0000'))
        sleep(espera)

        dout('0000','A',0xFF)
        print("0xFF")
        print("din: %s"%din('0000','B'))
        sleep(0.02) # Necessari després de 5 trucades seguides a funcions CAN
        aout('0000','B',1,v2aout(4))
        aout('0000','B',2,v2aout(6))
        aout('0000','B',3,v2aout(8))
        aout('0000','B',4,v2aout(10))
        sleep(0.7) # Temps mímin entre escriptura i lectura analògica
        print(ain2v(ain('0000','A',1)))
        print(ain2v(ain('0000','A',2)))
        print(ain2v(ain('0000','A',3)))
        print(ain2v(ain('0000','A',4)))
        dout('0000','A',0x5A)
        print("0xA5")
        sleep(0.02) # Necessari després de 5 trucades seguides a funcions CAN
        print("din: %s"%din('0000','B'))
        sleep(espera)
        dout('0000','A',0xA5)
        print("0x5A")
        print("din: %s"%din('0000','B'))
        sleep(espera)
        dout('0000','A',0x00)
        print("0x00")
        print("din: %s"%din('0000','B'))
        sleep(0.02) # Necessari després de 5 trucades seguides a funcions CAN
        aout('0000','B',1,v2aout(0))
        aout('0000','B',2,v2aout(0))
        aout('0000','B',3,v2aout(0))
        sleep(0.02) # Necessari després de 5 trucades seguides a funcions CAN
        aout('0000','B',4,v2aout(0))
        sleep(0.7) # Temps mímin entre escriptura i lectura analògica
        print(ain2v(ain('0000','A',1)))
        print(ain2v(ain('0000','A',2)))
        print(ain2v(ain('0000','A',3)))
        print(ain2v(ain('0000','A',4)))"""
    except KeyboardInterrupt:
        dout('0000','A',0x00)
        print("0x00")
        print("din: %s"%din('0000','B'))
    canOff()

