import time
from os import path
from LickLibrary import Control
from LickLibrary import myKeypad
from LickLibrary import Recorder
from datetime import datetime
from LickLibrary import Misc
from LickLibrary import SeriesCounter

############################################
use_analog = True
rate = 100
threshold = 1000
allowed_gap = 1 #in seconds
licks_to_deployment = 3
deployment_time = 1 #in seconds
############################################

detector = Control.LickDetector(analog=use_analog)
keypad = myKeypad.myKeypad()
feeder = Control.Feeder()

max_zeros_in_series = int(allowed_gap * rate)
series_counter = SeriesCounter.SeriesCounter(max_zeros_in_series)

name = Recorder.time2name()
output_file = path.join('recordings', name + '.txt')
print('Recording to', output_file)
comment = input('Enter a comment:')
# Open a file in write mode
with open(output_file, 'w') as file:
    counter = 1
    file.write(comment + '\n')
    while True:
        clock_time = time.time()
        timestamp = datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        value = detector.get_lick()
        binar = value > threshold
        series_counter.feed_sample(binar)
        detected_series = series_counter.get_series_count()
        key = keypad.get_key()

        if detected_series == licks_to_deployment and not binar:
            feeder.on()
            time.sleep(deployment_time)
            feeder.off()
            series_counter.reset_count()

        line = Misc.lst2line([timestamp, value, detected_series, key, clock_time])
        if binar: file.write(line + '\n') #only write lick events

        if counter%rate==0:
            print(line)
            counter = 0

        counter = counter + 1
        time.sleep(1/rate)