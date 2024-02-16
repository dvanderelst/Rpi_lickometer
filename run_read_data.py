import pandas
import numpy
from LickLibrary import myTimeSeriesPlot
from matplotlib import pyplot
from scipy.interpolate import interp1d
from LickLibrary import LickCounter
from matplotlib import pyplot

file_name = 'recordings/Thu_Feb_8_14_20_14_2024.txt'
time_column = 4
lick_column = 1
rate = 100

data = pandas.read_csv(file_name,skiprows=1, header=None)
data = data.iloc[:,[time_column, lick_column]]
data.columns = ['time', 'lick']
data['binary'] =  data['lick'] > 10000
data['time'] = data['time'] - numpy.min(data['time'])
#data = data.iloc[15500:17000,:]


min_lick_length = 3
max_lick_length = 10
max_bout_gap = 20
min_licks_per_bout = 3

lc = LickCounter.LickCounter(min_lick_length, max_lick_length, max_bout_gap, min_licks_per_bout)
lc.process_samples(data.binary)
lc.plot_history()

# ts = myTimeSeriesPlot.myTimeSeriesPlot(data.binary, 100)
# ts.measure_time_difference()

# x = data.loc[:,'time']
# y = data.loc[:,'lick']
#
# start_time = numpy.min(x)
# end_time = numpy.max(x)
#
# interpolation_x = numpy.arange(start_time, end_time, 1/rate)
# interp = interp1d(x,y, kind='nearest')
# new_y= interp(interpolation_x)
#
# pyplot.figure()
# pyplot.plot(interpolation_x, new_y)
# pyplot.show()
