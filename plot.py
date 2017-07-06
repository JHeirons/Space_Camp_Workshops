import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
import datetime
import urllib
from StringIO import StringIO

#---------------------------------------------------------------------------------
#
#   Import modules at the top give us additional functions to use to help us plotour data.
#   Now we need to do some investigation, go to http://habitat.habhub.org/ept/
#   Find a flight  a good one is EALPIT_01, then select the payload and select at the bottom CSV. 
#   CSV data is essentially excel file without cells, where each cell is seperated by a comma.

#   Copy and paste that url into your editor inside the brackets of urlopen(). 
#   What urlopen does is allows python to open the url it is supplied
fp=urllib.urlopen('http://habitat.habhub.org/habitat/_design/ept/_list/csv/payload_telemetry/flight_payload_time?include_docs=true&startkey=[%223f2e3ebf76f973da7d395e753752fec8%22,%223f2e3ebf76f973da7d395e75374d9f06%22]&endkey=[%223f2e3ebf76f973da7d395e753752fec8%22,%223f2e3ebf76f973da7d395e75374d9f06%22,[]]&fields=sentence_id,time,latitude,longitude,altitude,satellites,speed,heading,temperature_external,battery,bmp,temperature_external2,humidity,pressure,pitch,roll,yaw,x,y,z')

#   We then use the numpy function . genfromtext to read in the the data from the URL and save into a massive array called data.
data = np.genfromtxt(StringIO(fp.read()), dtype=None, delimiter=',', names=True)

#   Now we can get our x and y data from that data array, but instead of calling the index number we can use the name of the column.
x = data['time']
y = data['altitude']

#   This line of code converts the string into integers for matplotlib to plot on the graph
x = [datetime.datetime.strptime(elem, '%H:%M:%S') for elem in x]

#   Plot the data you want to see
plt.plot(x, y)

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
