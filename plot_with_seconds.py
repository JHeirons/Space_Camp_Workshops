import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np
import datetime
import urllib
from StringIO import StringIO



# Set the hour and minutes we want to start plotting data from


#-------------------------------------------------------------
#   Add from last example
def addSeconds():
    t = '10:45:'
    s1 = ['0','1','2','3','4','5']
    s2 = ['0','1','2','3','4','5','6','7','8','9']
    launch = []
    for i in s1:
        for j in s2:
            s = i + j
            ntime = t + s
            launch.append(ntime)
        
    return launch 

launch = addSeconds()

#--------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------
#   We will create a function that make use of string concatinationto make reading the data in more reuseable
#   Inbetween the square brackets in the url that are = to start key and end key remove that string from the url
#   Now between the two %22 remove the 32 character number the first is the flight id and the second is the payload id.
#   For the function will pass in the flight and payload id and create a key that we will input to the skeleton url.
#   How do we do this thinking back to the first example


flight_id = '3f2e3ebf76f973da7d395e753752fec8'
payload_id = '3f2e3ebf76f973da7d395e75374d9f06'


def getData(f_id, p_id):
    key = '%22' + f_id + '%22,%22' + p_id + '%22'
    
    fp=urllib.urlopen('http://habitat.habhub.org/habitat/_design/ept/_list/csv/payload_telemetry/flight_payload_time?include_docs=true&startkey=['+key+']&endkey=['+key+',[]]&fields=sentence_id,time,latitude,longitude,altitude,satellites,speed,heading,temperature_external,battery,bmp,temperature_external2,humidity,pressure,pitch,roll,yaw,x,y,z')
    data = np.genfromtxt(StringIO(fp.read()), dtype=None, delimiter=',', names=True)
    return data

data = getData(flight_id, payload_id)

#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#   We need to search through the data file and compare the time we want to start plotting from next to the first row of data with that time
#   So we need a for loop that will search through the data using np.nditer
#   And for each row of data we need to check the seconds so we use a nested loop to loop throught the launch time string 
#   If it matches we set the start to the variable that has been counting each row through the data array
#   We can then set data to only be the rows between the start time and the last row

def fromTime(data, launch):
    z = 0
    for x in np.nditer(data):
        z += 1
        for l in launch:
            if l == x['time']:
                start = z
                break  
    data = data[start:]
    return data

data = fromTime(data, launch)
#-----------------------------------------------------------------------------------------------------

fig, ax  = plt.subplots()
x = data['time']
y = data['altitude']

x = [datetime.datetime.strptime(elem, '%H:%M:%S') for elem in x]
plt.plot(x, y)


ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=5))


ax.set_title('Altitude vs Time')
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')



plt.show()
