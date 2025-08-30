from plcEdu_can import *

canOn()
reading = din()
print("Reading: %s"%reading)
canOff()


