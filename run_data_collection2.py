import time
from os import path
import math
from LickLibrary import Control
from LickLibrary import myKeypad
from LickLibrary import Recorder
from datetime import datetime
from LickLibrary import Misc
from LickLibrary import LickCounter

############################################
use_analog = True
sample_rate = 100
lick_threshold = 1000
print_interval = 1

min_lick_duration = 0.1 #in seconds
max_lick_duration = 1 #in seconds
max_bout_gap_duration = 1 #in seconds
min_licks_per_bout = 3
bouts_to_deployment = 3
deployment_time = 3 #in seconds
############################################
max_counter_value = 1000000

detector = Control.LickDetector(analog=use_analog)
keypad = myKeypad.myKeypad()
feeder = Control.Feeder()

min_lick_length = math.ceil(sample_rate * min_lick_duration)
max_lick_length = math.ceil(sample_rate * max_lick_duration)
max_bout_gap = math.ceil(sample_rate * max_bout_gap_duration)
lick_counter = LickCounter.LickCounter(min_lick_length, max_lick_length, max_bout_gap, min_licks_per_bout)

name = Recorder.time2name()
output_file = path.join('recordings', name + '.txt')
print('Recording to', output_file)
comment = input('Enter a comment:')
last_lick_time = -10000
counter = 0
# Open a file in write mode
with open(output_file, 'w') as file:
    file.write(comment + '\n')
    while True:
        counter = counter + 1
        clock_time = time.time()
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        value = detector.get_lick()
        binary = value > lick_threshold
        if binary: last_lick_time = time.time()
        lick_counter.process_sample(binary)
        detected_bouts = lick_counter.get_bout_count()
        key = keypad.get_key()
        action = 'measuring'
        time_since_last_lick = time.time() - last_lick_time

        lick_length = lick_counter.lick_length
        lick_count = lick_counter.lick_count
        bout_count = lick_counter.bout_count
        if counter % print_interval == 0: print('C', counter, 'LC', lick_count, 'BOUTS', bout_count)

        enough_bouts = detected_bouts >= (bouts_to_deployment-1)
        enough_time = True#time_since_last_lick > max_bout_gap_duration
        enough_licks = lick_count >= min_licks_per_bout

        if enough_bouts and enough_time and enough_licks:
            action = 'deploying'
            feeder.on()
            time.sleep(deployment_time)
            feeder.off()
            lick_counter.reset_bout_count()

        line = Misc.lst2line([timestamp, clock_time, action, value, lick_length, lick_count, bout_count, key])
        file.write(line + '\n')

        time_taken = time.time() - clock_time
        time_remaining = (1 / sample_rate) - time_taken
        time_remaining = max(0, time_remaining)
        time.sleep(time_remaining)

        if counter >= max_counter_value:counter %= max_counter_value

