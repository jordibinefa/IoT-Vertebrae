from plcEdu import *
import time 

for bit in range(4):
    readBit = dinbit(bit)
    print("bit %d: %s"%(bit,readBit))
    time.sleep(0.1)



