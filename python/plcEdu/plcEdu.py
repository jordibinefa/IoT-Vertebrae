"""
plcEdu.py
https://www.iotvertebrae.com
20250331
"""
import i2c_iotv as iotv
from can_iotv import v2aout,ain2v

def dout(nibble): # nibble: a value between 0x0 and 0xF
    iotv.dout('0000','A',nibble)

def doutbit(bit,value): # bit: 0..3    value: 0..1
    iotv.doutbit('0000','A',bit,value)

def din():
    byte = iotv.din('0000','B')
    return byte[4:]

def dinbit(bit): # bit: 0..3
    return din()[3-bit:4-bit]

def aout(canal,valor): # canal: 1..4  valor: 0.0..10.0
    return iotv.aout('0000','B',canal,v2aout(valor))

def ain(canal): # canal: 1..4
    return ain2v(iotv.ain('0000','A',canal))
