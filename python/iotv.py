"""
iotv.py
Written by Xavier Pi and Jordi Binefa
www.iotvertebrae.com
20231105
"""
import sys
from smbus import SMBus
import time

def ain(addr, side, ndac):
    # ndac: 1, 2, 3 or 4
    if   addr == '0000':
        i2cAddr = 0x10
    elif addr == '0001':
        i2cAddr = 0x11
    elif addr == '0010':
        i2cAddr = 0x12
    elif addr == '0011':
        i2cAddr = 0x13
    elif addr == '0100':
        i2cAddr = 0x14
    elif addr == '0101':
        i2cAddr = 0x15
    elif addr == '0110':
        i2cAddr = 0x16
    elif addr == '0111':
        i2cAddr = 0x17
    elif addr == '1000':
        i2cAddr = 0x18
    elif addr == '1001':
        i2cAddr = 0x19
    elif addr == '1010':
        i2cAddr = 0x1A
    elif addr == '1011':
        i2cAddr = 0x1B
    elif addr == '1100':
        i2cAddr = 0x1C
    elif addr == '1101':
        i2cAddr = 0x1D
    elif addr == '1110':
        i2cAddr = 0x1E
    elif addr == '1111':
        i2cAddr = 0x1F

    if   ndac == 1:
        if side.lower() == 'a':
            addrChannel = 0x01
        if side.lower() == 'b':
            addrChannel = 0x11
    elif ndac == 2:
        if side.lower() == 'a':
            addrChannel = 0x21
        if side.lower() == 'b':
            addrChannel = 0x31
    elif ndac == 3:
        if side.lower() == 'a':
            addrChannel = 0x41
        if side.lower() == 'b':
            addrChannel = 0x51
    elif ndac == 4:
        if side.lower() == 'a':
            addrChannel = 0x61
        if side.lower() == 'b':
            addrChannel = 0x71

    i2c = SMBus(1)
    res = i2c.read_word_data(i2cAddr, addrChannel)
    res = i2c.read_word_data(i2cAddr, addrChannel)
    i2c.close()

#    res = 14000
    return res


def ainv(addr, side, ndac):
    # ndac: 1, 2, 3 or 4
    if   addr == '0000':
        i2cAddr = 0x10
    elif addr == '0001':
        i2cAddr = 0x11
    elif addr == '0010':
        i2cAddr = 0x12
    elif addr == '0011':
        i2cAddr = 0x13
    elif addr == '0100':
        i2cAddr = 0x14
    elif addr == '0101':
        i2cAddr = 0x15
    elif addr == '0110':
        i2cAddr = 0x16
    elif addr == '0111':
        i2cAddr = 0x17
    elif addr == '1000':
        i2cAddr = 0x18
    elif addr == '1001':
        i2cAddr = 0x19
    elif addr == '1010':
        i2cAddr = 0x1A
    elif addr == '1011':
        i2cAddr = 0x1B
    elif addr == '1100':
        i2cAddr = 0x1C
    elif addr == '1101':
        i2cAddr = 0x1D
    elif addr == '1110':
        i2cAddr = 0x1E
    elif addr == '1111':
        i2cAddr = 0x1F

    if   ndac == 1:
        if side.lower() == 'a':
            addrChannel = 0x01
        if side.lower() == 'b':
            addrChannel = 0x11
    elif ndac == 2:
        if side.lower() == 'a':
            addrChannel = 0x21
        if side.lower() == 'b':
            addrChannel = 0x31
    elif ndac == 3:
        if side.lower() == 'a':
            addrChannel = 0x41
        if side.lower() == 'b':
            addrChannel = 0x51
    elif ndac == 4:
        if side.lower() == 'a':
            addrChannel = 0x61
        if side.lower() == 'b':
            addrChannel = 0x71

    print("i2cAddr: 0x%X, addrChannel: 0x%X"%(i2cAddr, addrChannel))
    
    i2c = SMBus(1)
    res = i2c.read_word_data(i2cAddr, addrChannel)
    res = i2c.read_word_data(i2cAddr, addrChannel)
    i2c.close()

#    res = 14000
    
    print("res: 0x%X: %d"%(res,res))
    # print("0x%X --> %d --> %.2fV"%(res, res, (19.78 * float(res) / 26640) - 10))
    print("0x%X --> %d --> %.2fV"%(res, res, (20 * float(res) / 26624) - 10))

    return res


def aout(addr, side, ndac, value):
    # ndac: 1, 2, 3 or 4
    # value: between 0 and 4095 (or 0x0000 and 0x0FFF). 0 is 0 volts. 4095 is 10 volts.
    if   addr == '0000':
        i2cAddr = 0x10
    elif addr == '0001':
        i2cAddr = 0x11
    elif addr == '0010':
        i2cAddr = 0x12
    elif addr == '0011':
        i2cAddr = 0x13
    elif addr == '0100':
        i2cAddr = 0x14
    elif addr == '0101':
        i2cAddr = 0x15
    elif addr == '0110':
        i2cAddr = 0x16
    elif addr == '0111':
        i2cAddr = 0x17
    elif addr == '1000':
        i2cAddr = 0x18
    elif addr == '1001':
        i2cAddr = 0x19
    elif addr == '1010':
        i2cAddr = 0x1A
    elif addr == '1011':
        i2cAddr = 0x1B
    elif addr == '1100':
        i2cAddr = 0x1C
    elif addr == '1101':
        i2cAddr = 0x1D
    elif addr == '1110':
        i2cAddr = 0x1E
    elif addr == '1111':
        i2cAddr = 0x1F

    if   ndac == 1:
        if side.lower() == 'a':
            dacCommand = 0x02
        if side.lower() == 'b':
            dacCommand = 0x12
    elif ndac == 2:
        if side.lower() == 'a':
            dacCommand = 0x22
        if side.lower() == 'b':
            dacCommand = 0x32
    elif ndac == 3:
        if side.lower() == 'a':
            dacCommand = 0x42
        if side.lower() == 'b':
            dacCommand = 0x52
    elif ndac == 4:
        if side.lower() == 'a':
            dacCommand = 0x62
        if side.lower() == 'b':
            dacCommand = 0x72

    i2c = SMBus(1)
    i2c.write_i2c_block_data(i2cAddr, dacCommand, [(value&0xFF00)>>8,value&0xFF])
    i2c.close()
    
    print("dacCommand: 0x%X"%(dacCommand))
    print("It has been sent 0x%X (%.2f volts) to DAC %d"%(value,float(value)*10/4095,ndac))
    
def din(addr, side):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    i2c = SMBus(1)
    if side.lower() == 'a':
        res = i2c.read_byte_data(i2cAddr,0x01)
        res = i2c.read_byte_data(i2cAddr,0x01)
    if side.lower() == 'b':
        res = i2c.read_byte_data(i2cAddr,0x11)
        res = i2c.read_byte_data(i2cAddr,0x11)
    i2c.close()

#    res = 0b10111111
    
    resp = bin(res)[2::].zfill(8)

    return resp


def dout(addr, side, value):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    i2c = SMBus(1)
    if side.lower() == 'a':
        i2c.write_i2c_block_data(i2cAddr, 0x02, [value])
    if side.lower() == 'b':
        i2c.write_i2c_block_data(i2cAddr, 0x12, [value])
    i2c.close()

def doutpwm(addr, side, value):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    i2c = SMBus(1)
    if side.lower() == 'a':
        i2c.write_i2c_block_data(i2cAddr, 0x03, [value])
    if side.lower() == 'b':
        i2c.write_i2c_block_data(i2cAddr, 0x13, [value])
    i2c.close()

def doutbit(addr, side, posbyte, value):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    if side.lower() == 'a':
        if posbyte == 0:
            bitCfg = 0x0A;
        elif posbyte == 1:
            bitCfg = 0x2A;
        elif posbyte == 2:
            bitCfg = 0x4A;
        elif posbyte == 3:
            bitCfg = 0x6A;
        elif posbyte == 4:
            bitCfg = 0x8A;
        elif posbyte == 5:
            bitCfg = 0xAA;
        elif posbyte == 6:
            bitCfg = 0xCA;
        elif posbyte == 7:
            bitCfg = 0xEA;

    if side.lower() == 'b':
        if posbyte == 0:
            bitCfg = 0x1A;
        elif posbyte == 1:
            bitCfg = 0x3A;
        elif posbyte == 2:
            bitCfg = 0x5A;
        elif posbyte == 3:
            bitCfg = 0x7A;
        elif posbyte == 4:
            bitCfg = 0x9A;
        elif posbyte == 5:
            bitCfg = 0xBA;
        elif posbyte == 6:
            bitCfg = 0xDA;
        elif posbyte == 7:
            bitCfg = 0xFA;

    i2c = SMBus(1)
    i2c.write_i2c_block_data(i2cAddr, bitCfg, [value])
    i2c.close()

def doutbitpwm(addr, side, posbyte, value):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    if side.lower() == 'a':
        if posbyte == 0:
            bitCfg = 0x0B;
        elif posbyte == 1:
            bitCfg = 0x2B;
        elif posbyte == 2:
            bitCfg = 0x4B;
        elif posbyte == 3:
            bitCfg = 0x6B;
        elif posbyte == 4:
            bitCfg = 0x8B;
        elif posbyte == 5:
            bitCfg = 0xAB;
        elif posbyte == 6:
            bitCfg = 0xCB;
        elif posbyte == 7:
            bitCfg = 0xEB;

    if side.lower() == 'b':
        if posbyte == 0:
            bitCfg = 0x1B;
        elif posbyte == 1:
            bitCfg = 0x3B;
        elif posbyte == 2:
            bitCfg = 0x5B;
        elif posbyte == 3:
            bitCfg = 0x7B;
        elif posbyte == 4:
            bitCfg = 0x9B;
        elif posbyte == 5:
            bitCfg = 0xBB;
        elif posbyte == 6:
            bitCfg = 0xDB;
        elif posbyte == 7:
            bitCfg = 0xFB;

    i2c = SMBus(1)
    i2c.write_i2c_block_data(i2cAddr, bitCfg, [value])
    i2c.close()

def dversion(addr):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    i2c = SMBus(1)
    resp = i2c.read_word_data(i2cAddr, 0x06)
    resp = i2c.read_word_data(i2cAddr, 0x06)
    i2c.close()

#    resp = 0

    print("Digital rib version: %d.%d"%(((0xFF00&resp)>>8),0x00FF&resp))

    return bin(resp)[2::].zfill(16)

def aversion(addr):
    if   addr == '0000':
        i2cAddr = 0x10
    elif addr == '0001':
        i2cAddr = 0x11
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x13
    elif addr == '0100':
        i2cAddr = 0x14
    elif addr == '0101':
        i2cAddr = 0x15
    elif addr == '0110':
        i2cAddr = 0x16
    elif addr == '0111':
        i2cAddr = 0x17
    elif addr == '1000':
        i2cAddr = 0x18
    elif addr == '1001':
        i2cAddr = 0x19
    elif addr == '1010':
        i2cAddr = 0x1A
    elif addr == '1011':
        i2cAddr = 0x1B
    elif addr == '1100':
        i2cAddr = 0x1C
    elif addr == '1101':
        i2cAddr = 0x1D
    elif addr == '1110':
        i2cAddr = 0x1E
    elif addr == '1111':
        i2cAddr = 0x1F

    i2c = SMBus(1)
    resp = i2c.read_word_data(i2cAddr, 0x06)
    resp = i2c.read_word_data(i2cAddr, 0x06)
    i2c.close()

#    resp = 0
 
    print("Analog rib version: %d.%d"%(((0xFF00&resp)>>8),0x00FF&resp))

    return bin(resp)[2::].zfill(16)

def getdsetup(addr):
    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    i2c = SMBus(1)
    resp = i2c.read_byte_data(i2cAddr, 0x05)
    resp = i2c.read_byte_data(i2cAddr, 0x05)
    i2c.close()

#    resp = 0
    
    if (resp & 0x01) == 0x01:
    	print("A digital input, ", end = "")
    if (resp & 0x02) == 0x02:
    	print("A digital output, ", end = "")
    if (resp & 0x04) == 0x04:
    	print("A PWM output, ", end = "")
    if (resp & 0x10) == 0x10:
    	print("B digital input")
    if (resp & 0x20) == 0x20:
    	print("B digital output")
    if (resp & 0x40) == 0x40:
    	print("B PWM output")
    if (resp & 0x80) == 0x80 :
    	print("B touch input")
    
    return bin(resp)[2::].zfill(8)

def getasetup(addr):
    if   addr == '0000':
        i2cAddr = 0x10
    elif addr == '0001':
        i2cAddr = 0x11
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x13
    elif addr == '0100':
        i2cAddr = 0x14
    elif addr == '0101':
        i2cAddr = 0x15
    elif addr == '0110':
        i2cAddr = 0x16
    elif addr == '0111':
        i2cAddr = 0x17
    elif addr == '1000':
        i2cAddr = 0x18
    elif addr == '1001':
        i2cAddr = 0x19
    elif addr == '1010':
        i2cAddr = 0x1A
    elif addr == '1011':
        i2cAddr = 0x1B
    elif addr == '1100':
        i2cAddr = 0x1C
    elif addr == '1101':
        i2cAddr = 0x1D
    elif addr == '1110':
        i2cAddr = 0x1E
    elif addr == '1111':
        i2cAddr = 0x1F

    i2c = SMBus(1)
    respA = i2c.read_byte_data(i2cAddr, 0x25)
    respA = i2c.read_byte_data(i2cAddr, 0x25)
    respB = i2c.read_byte_data(i2cAddr, 0x35)
    respB = i2c.read_byte_data(i2cAddr, 0x35)
    i2c.close()

#    respA = 0
#    respB = 0
    
    print("respA: 0x%X, respB: 0x%X"%(respA,respB))
    if respA == 0x01:
        print("A rib is ADC, ",end="")
    elif respA == 0x02:
        print("A rib is DAC, ",end="")
    else:
        print("A rib is unconnected or it is unknown, ",end="")
    if respB == 0x01:
        print("B rib is ADC.")
    elif respB == 0x02:
        print("B rib is DAC.")
    else:
        print("B rib is unconnected or it is unknown.")
    resp = (respA *16) | respB

    return bin(resp)[2::].zfill(8)

def dsetup(addr, modeA, modeB):
    modeL = 0x00
    modeH = 0x00

    if   addr == '0000':
        i2cAddr = 0x20
    elif addr == '0001':
        i2cAddr = 0x21
    elif addr == '0010':
        i2cAddr = 0x22
    elif addr == '0011':
        i2cAddr = 0x23
    elif addr == '0100':
        i2cAddr = 0x24
    elif addr == '0101':
        i2cAddr = 0x25
    elif addr == '0110':
        i2cAddr = 0x26
    elif addr == '0111':
        i2cAddr = 0x27
    elif addr == '1000':
        i2cAddr = 0x28
    elif addr == '1001':
        i2cAddr = 0x29
    elif addr == '1010':
        i2cAddr = 0x2A
    elif addr == '1011':
        i2cAddr = 0x2B
    elif addr == '1100':
        i2cAddr = 0x2C
    elif addr == '1101':
        i2cAddr = 0x2D
    elif addr == '1110':
        i2cAddr = 0x2E
    elif addr == '1111':
        i2cAddr = 0x2F

    if  modeA.lower() == 'ain': # 0xFF__
        modeL |= 0x00
        modeH |= 0xFF
    if  modeA.lower() == 'aout': # 0x00__
        modeL |= 0x00
        modeH |= 0x00
    if  modeB.lower() == 'bin': # 0x__FF
        modeL |= 0xFF
        modeH |= 0x00
    if  modeB.lower() == 'bout': # 0x__00
        modeL |= 0x00
        modeH |= 0x00

    print("%s, %s"%(modeA.lower(),modeB.lower()))
    if (modeA.lower() == 'ain' or modeA.lower() == 'aout') and (modeB.lower() == 'bin' or modeB.lower() == 'bout'):
        i2c = SMBus(1)
        i2c.write_i2c_block_data(i2cAddr, 0x00, [modeL, modeH])
        i2c.close()
    elif (modeA.lower() == 'ain' or modeA.lower() == 'aout') and (modeB.lower() == 'boutpwm'):
        i2c = SMBus(1)
        i2c.write_i2c_block_data(i2cAddr, 0x00, [0x00, modeH])
        i2c.write_i2c_block_data(i2cAddr, 0x04, [0x01])
        i2c.close()
    elif (modeA.lower() == 'aoutpwm') and (modeB.lower() == 'bin' or modeB.lower() == 'bout'):
        i2c = SMBus(1)
        i2c.write_i2c_block_data(i2cAddr, 0x00, [modeL, 0x00])
        i2c.write_i2c_block_data(i2cAddr, 0x04, [0x00])
        i2c.close()
    elif (modeA.lower() == 'ain' or modeA.lower() == 'aout' or modeA.lower() == 'aoutpwm') and (modeB.lower() == 'bintouch'):
        i2c = SMBus(1)
        i2c.write_i2c_block_data(i2cAddr, 0x00, [0xFF, modeH])
        if (modeA.lower() == 'aoutpwm'):
            i2c.write_i2c_block_data(i2cAddr, 0x04, [0x00])
        i2c.write_i2c_block_data(i2cAddr, 0x07, [0x01])
        i2c.close()
    else:
        print('Setup has not been changed')
        # Restrictions:
        # aoutpwm or boutpwm: Only one rib, A or B, is able to manage PWM. Because it is used an ESP32-S3 by vertebra.
        # bintouch (and it is not aintouch): Only B rib is able to manage 8 touch inputs. Because it is used an ESP32-S3 by vertebra.
        return False


    return True        

