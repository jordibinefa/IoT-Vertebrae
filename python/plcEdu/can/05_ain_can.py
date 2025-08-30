from plcEdu_can import *

canOn()
canal = 4
aVal = ain(canal)
print("Reading ",aVal," volts at canal ",canal)
canOff()
