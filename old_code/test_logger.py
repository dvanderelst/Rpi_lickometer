from LickLibrary import ZooLogger
import time

zl = ZooLogger.ZooDatabase()
zl.add_data([1,time.asctime(), 100])
