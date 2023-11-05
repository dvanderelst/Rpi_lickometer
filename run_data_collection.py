from LickLibrary import Recorder
from os import path
import time

recorder = Recorder.Recorder(rate=100)

time_stamp = time.asctime()
recorder.start()
input('When the cat starts licking, press enter to start the recording')
recorder.use_buffer = False
input('When the cat stops licking, press enter to stop the recording')
recorder.stop()
status = recorder.status(to_screen=True)
recorder.plot()

comment = input('Enter a comment:')

data = recorder.get_data()
data = comment + '\n'+ time_stamp + '\n' + status + '\n'  + data
name = Recorder.time2name()

output_file = path.join('recordings', name)
fl = open(output_file, 'w')
fl.write(data)
fl.close()

