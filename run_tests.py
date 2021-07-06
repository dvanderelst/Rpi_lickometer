import RPi.GPIO as GPIO
import time
from LickLibrary import Settings, Control, myAnalog, Misc, ZooLogger
GPIO.cleanup()

GPIO.setup(Settings.button_pin, GPIO.IN, GPIO.PUD_DOWN)

use_analog = True


feeder = Control.Feeder()
analog = myAnalog.myAnalog()
counter = Misc.Counter(1)
detector = Control.LickDetector(analog=use_analog)
db_logger = ZooLogger.ZooLogger(verbose=True, log_actions=True)


lick_counter = 0
last_lick_time = 'None'


while True:
    lick_state = detector.get_lick()
    distance = analog.get_value(0)
    button = GPIO.input(Settings.button_pin)
    print(time.asctime(), lick_state)

    feeder.on()
    time.sleep(3)
    feeder.off()
    time.sleep(1)

    db_logger.add_data([time.asctime(), 'testing'])