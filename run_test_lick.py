import time
from LickLibrary import Control

#[BATTERY]
# LCK: <DETECTION ON, > DETECTION OFF
# SGN: <DIGITAL, >ANALOG
#[BOARD EDGE]

detector = Control.LickDetector(analog=False)

for i in range(10):
    data  = detector.get_lick()
    print(data)
    time.sleep(.5)

