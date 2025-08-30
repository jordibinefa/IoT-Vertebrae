from plcEdu_can import *
import time 

canOn()
dout(0xF) # 1111
print('1111')
time.sleep(1.5)
dout(0xC) # 1100
print('1100')
time.sleep(1.5)
dout(0x3) # 0011
print('0011')
time.sleep(1.5)
dout(0x0) # 0000
print('0000')
canOff()
