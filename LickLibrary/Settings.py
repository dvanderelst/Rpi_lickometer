import board
import RPi.GPIO as GPIO
from os import path

data_dir = 'data'

# Database settings
database = path.join(data_dir, 'test.db')
database_log = path.join(data_dir, 'log.html') # used to log the write actions to the DB
buffer_file = path.join(data_dir, 'buffer.pck') # used to store data locally before writing to db. Can be handy in case the DB is remote and connections fails
table = 'lick_data'
omit_fields = ['row_id']

# Board settings
# Pin numbers assume BCM mode
GPIO.setmode(GPIO.BCM)
lick_pin = 5 #29
button_pin = 16 #36
feeder_pin = 6 #31

scale1_dt = 11
scale1_sck = 13
scale2_dt = 15
scale2_sck = 16

analog_lick_channel = 0
max_analog_value = 65472
cs_pin = board.D8

