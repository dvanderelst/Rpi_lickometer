import time

from LickLibrary import Control

feeder = Control.Feeder()

for i in range(10):
    feeder.on()
    time.sleep(1)
    feeder.off()
    time.sleep(1)

