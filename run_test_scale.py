from LickLibrary import myScales
import time

scales = myScales.myScales()

#scales.calibrate(scale_nr=2)
#scales.calibrate(scale_nr=2)

while True:
    r = scales.measure()
    print(r)
    time.sleep(0.5)