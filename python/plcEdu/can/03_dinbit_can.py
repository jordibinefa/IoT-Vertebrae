from plcEdu_can import *
import time 

canOn()
for bit in range(4):
    readBit = dinbit(bit)
    print("bit %d: %s"%(bit,readBit))
    time.sleep(0.1)
canOff()


