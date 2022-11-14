import time
from LickLibrary import myDigitalPin
from LickLibrary import Settings

led = myDigitalPin.myDigitalPin('output', Settings.button_led_pin)
button = myDigitalPin.myDigitalPin('input', Settings.button_pin)

value = button.get()

for i in range(5):
    print('Button state: ', value)
    led.set(True)
    time.sleep(0.1)
    led.set(False)
    time.sleep(0.1)

