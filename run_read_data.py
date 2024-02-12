import pandas
import numpy
from matplotlib import pyplot
from scipy.interpolate import interp1d
from matplotlib import pyplot

file_name = 'recordings/Thu_Feb_8_13_27_00_2024.txt'
time_column = 4
lick_column = 1
rate = 100

data = pandas.read_csv(file_name,skiprows=1, header=None)
data = data.iloc[:,[time_column, lick_column]]
data.columns = ['time', 'lick']

x = data.loc[:,'time']
y = data.loc[:,'lick']

start_time = numpy.min(x)
end_time = numpy.max(x)

interpolation_x = numpy.arange(start_time, end_time, 1/rate)
interp = interp1d(x,y, kind='nearest')
new_y= interp(interpolation_x)

pyplot.figure()
pyplot.plot(interpolation_x, new_y)
pyplot.show()
