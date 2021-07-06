import board
import RPi.GPIO as GPIO
from os import path

# Database settings
database = 'test.db'
table = 'lick_data'
omit_fields = ['row_id']
data_dir = 'storage'

# Log settings
html_log = path.join(data_dir, 'log.html')
buffer_file = path.join(data_dir, 'buffer.pck')
buffer_csv_file = path.join(data_dir, 'buffer.csv')

# Board settings
# Pin numbers assume BCM mode
GPIO.setmode(GPIO.BCM)
lick_pin = 5 #29
button_pin = 16 #36
feeder_pin = 6 #31

e_tape_channel = 7
analog_lick_channel = 2
max_analog_value = 65472
cs_pin = board.D8

