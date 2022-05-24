import time
import RPi.GPIO as GPIO
from LickLibrary import myOLED, Settings, Control, myAnalog, Misc
from LickLibrary import ZooLogger




GPIO.cleanup()
display = myOLED.myOLED(flipped=True)

GPIO.setup(Settings.button_pin, GPIO.IN, GPIO.PUD_DOWN)

use_analog = True


feeder = Control.Feeder()
analog = myAnalog.myAnalog()
counter = Misc.Counter(1)
detector = Control.LickDetector(analog=use_analog)
logger = ZooLogger.ZooDatabase(verbose=True)

lick_counter = 0
last_lick_time = 'None'



while True:
    if counter.value == 0: symbol = '-'
    if counter.value == 1: symbol = '+'
    display.set_text(0, symbol, update=False)
    counter.increase()

    lick_state = detector.get_lick()
    if use_analog and lick_state < 1000: lick_state = 0
    if lick_state > -1: lick_counter = lick_counter + 1
    print(lick_state)

    if lick_counter > 5:
        logger.add_data([lick_state, time.asctime(), counter.value])
        last_lick_time = time.asctime()
        lick_counter = 0
        feeder.on()
        time.sleep(5)
        feeder.off()

        data = logger.get_data()
        print(data)





    # distance = analog.get_value(0)
    # button = GPIO.input(Settings.button_pin)
    #
    # print(time.asctime(), lick_state)

    display.set_text(1, 'Lick counter: %s' % lick_counter, update=False)
    display.set_text(2, last_lick_time, update=True)


