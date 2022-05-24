import logging
import time
import RPi.GPIO as GPIO
from LickLibrary import Settings, Control, myAnalog, ZooDatabase

GPIO.cleanup()
GPIO.setup(Settings.button_pin, GPIO.IN, GPIO.PUD_DOWN)

# Specify logging format
logFormatter = logging.Formatter("%(asctime)s [%(funcName)-15s] [%(levelname)-5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("history.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

rootLogger.setLevel(logging.DEBUG)

# Start of example
use_analog = False

feeder = Control.Feeder()
analog = myAnalog.myAnalog()
detector = Control.LickDetector(analog=use_analog)
database = ZooDatabase.ZooDatabase(verbose=True)

while True:
    lick_state = detector.get_lick()
    analog_value = analog.get_value(0)
    button = GPIO.input(Settings.button_pin)
    logging.info('State: ' + time.asctime() + ' ' + str(lick_state))

    feeder.on()
    time.sleep(3)
    feeder.off()
    time.sleep(1)

    database.add_data([time.asctime(), 'testing'])
