import RPi.GPIO as GPIO


class myDigitalPin:
    def __init__(self, pintype, number):
        self.pintype = pintype
        self.number = number

        if self.pintype == 'output': GPIO.setup(number, GPIO.OUT)
        if self.pintype == 'input': GPIO.setup(number, GPIO.IN)

    def set(self, value):
        if not self.pintype == 'output': return
        GPIO.output(self.number, value)
        return value

    def get(self):
        if not self.pintype == 'input': return
        value = GPIO.input(self.number)
        return value

    # class Feeder:
    #     def __init__(self):
    #         GPIO.setup(Settings.feeder_pin, GPIO.OUT)
    #
    #     def on(self):
    #         logging.info('Feeder on')
    #         GPIO.output(Settings.feeder_pin, True)
    #
    #     def off(self):
    #         logging.info('Feeder off')
    #         GPIO.output(Settings.feeder_pin, False)
