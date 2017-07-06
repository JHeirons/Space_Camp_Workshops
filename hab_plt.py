import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
import datetime
import urllib
from StringIO import StringIO

#---------------------------------------------------------------------------------

fp=urllib.urlopen()

# We then use the numpy function .genfromtext to read in the the data from the URL and save into a massive array called data.
data = np.genfromtxt(StringIO(fp.read()), dtype=None, delimiter=',', names=True)

#  Now we can get our x and y data from that data array.


#  This line of code converts the string into integers for matplotlib to plot on the graph
x = [datetime.datetime.strptime(elem, '%H:%M:%S') for elem in x]

#  Plot the data you want to see
plt.plot()

# Sets the the intervals and the way the data is shown on the x axis of the graph
plt.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
plt.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.xaxis.set_minor_locator(mdates.MinuteLocator(interval=5))

#   Set your titles and axis labels for the graph
plt.set_title('Altitude vs Time')
plt.setp(plt.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.set_ylabel('Altitude (m)')
plt.set_xlabel('Time')


plt.show()
