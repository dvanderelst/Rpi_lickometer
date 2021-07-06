import RPi.GPIO as GPIO
import time
from LickLibrary import myOLED, Settings, Control, myAnalog, Misc
GPIO.cleanup()
display = myOLED.myOLED(flipped=True)

GPIO.setup(Settings.button_pin, GPIO.IN, GPIO.PUD_DOWN)

feeder = Control.Feeder()
analog = myAnalog.myAnalog()
counter = Misc.Counter(1)
detector = Control.LickDetector(analog=True)

while True:
    if counter.value == 0: symbol = '-'
    if counter.value == 1: symbol = '+'
    display.set_text(0, symbol, update=False)
    counter.increase()

    lick_state = detector.get_lick()
    distance = analog.get_value(0)
    button = GPIO.input(Settings.button_pin)

    print(time.asctime(), lick_state)

    display.set_text(1, 'Lick: %s' % lick_state, update=False)
    display.set_text(2, 'Button: %s' % button, update=False)
    display.set_text(3, 'Distance: %s' % distance, update=True)

    feeder.on()
    time.sleep(3)
    feeder.off()
    time.sleep(1)

#
# out_pin = 31
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(out_pin , GPIO.OUT)
# GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# display = myOLED.myOLED()
# print('start')
# analog = myAnalog.myAnalog()
# #ASada
# for i in range(3):
#     GPIO.output(out_pin, True)
#     time.sleep(1)
#     GPIO.output(out_pin, False)
#     time.sleep(1)
#     print(i)
#
#     x = GPIO.input(36)
#     print('button', x)
#
#     # display.clear()
#     # display.set_text(0,i, update=False)
#     # display.set_text(3, i, update=True)
#
#     display.set_text(1, i)
#     display.set_text(2, analog.get_voltage(0))
#     display.set_text(3, x)
#
# display.set_text(1, 'done')
# print('don')
# #
# # import RPi.GPIO as GPIO
# # import time
# # import Settings
# # import myAnalog
# #
# # import myOLED
# #
# # analog = myAnalog.myAnalog()
# #
# # for i in range(10):
# #
# #     a = time.time()
# #     print(analog.get_voltage(1))
# #     b = time.time()
# #
# # print((b-a)*1000)