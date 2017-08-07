import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime
import pandas as pd

data = pd.read_csv('http://habitat.habhub.org/habitat/_design/ept/_list/csv/payload_telemetry/flight_payload_time?include_docs=true&startkey=[%22a23da9109e2fc0079960e9a1d11f15db%22,%22a23da9109e2fc0079960e9a1d10e89ab%22]&endkey=[%22a23da9109e2fc0079960e9a1d11f15db%22,%22a23da9109e2fc0079960e9a1d10e89ab%22,[]]&fields=sentence_id,time,latitude,longitude,altitude,speed,direction,satellites,temperature_external,battery,bmp')
data2 = pd.DataFrame(data)

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

for index, row in data2.iterrows():
    for l in launch:
        if l == row['time']:
            start = index
            break

data2 = data2[start:]



#-----------------------------------------------------------------------------------------------------

fig, ax  = plt.subplots()
x = data2['time']
y = data2['altitude']

x = [datetime.datetime.strptime(elem, '%H:%M:%S') for elem in x]
plt.plot(x, y)


ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=5))


ax.set_title('Altitude vs Time')
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')



plt.show()
