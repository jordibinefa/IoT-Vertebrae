from plcEdu import *
import time 

for count in range(4):
    print(count)
    doutbit(count,1)
    time.sleep(1.5)
    doutbit(count,0)
    time.sleep(1.5)


