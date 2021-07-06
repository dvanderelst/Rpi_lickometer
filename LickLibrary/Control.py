from LickLibrary import Settings, myAnalog
import RPi.GPIO as GPIO


class LickDetector:
    def __init__(self, analog=False):
        self.analog = analog
        if analog:
            self.input = myAnalog.myAnalog()
        if not analog:
            GPIO.setup(Settings.lick_pin, GPIO.IN)

    def get_lick(self):
        if self.analog:
            value = (Settings.max_analog_value - self.input.analog_lick())
            if value < 0: value = 0
            return value
        if not self.analog:
            return (1 - GPIO.input(Settings.lick_pin))


class Feeder:
    def __init__(self):
        GPIO.setup(Settings.feeder_pin, GPIO.OUT)

    def on(self):
        GPIO.output(Settings.feeder_pin, True)

    def off(self):
        GPIO.output(Settings.feeder_pin, False)
