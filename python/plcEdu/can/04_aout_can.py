from plcEdu_can import *
import time 

canOn()
canal = 4
for value in range(11):
    aout(canal,value)
    print("Sending ", value," volts to channel ", canal)
    time.sleep(0.5)
    if value != 10:
        aout(canal,value+0.5)
        print("Sending ", value+0.5," volts to channel ", canal)
        time.sleep(0.5)
value = 5
aout(canal,value)
print("Sending ", value," volts to channel ", canal)
canOff()

