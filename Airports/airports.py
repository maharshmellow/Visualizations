"""
Airports Graphing
By: Maharsh Patel
maharsh@live.ca
maharsh.net/airports

Source: http://ourairports.com/data/
"""

#imports
import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

with open('airports.csv', 'rb') as f:
    reader = csv.reader(f)
    airportsList = list(reader)


small_airport_latitude = []
small_airport_longitude = []
small_airport_elevation = []

medium_airport_latitude = []
medium_airport_longitude = []
medium_airport_elevation = []

large_airport_latitude = []
large_airport_longitude = []
large_airport_elevation = []

seaplane_base_latitude = []
seaplane_base_longitude = []

heliport_latitude = []
heliport_longitude = []

balloonport_latitude = []
balloonport_longitude = []

closed_airport_latitude = []
closed_airport_longitude = []


for i in range(len(airportsList)):
    # Types: heliport, small_airport, medium_airport, large_airport, seaplane_base, balloonport, closed
    if (airportsList[i][0] == "small_airport"):
        small_airport_latitude.append(float(airportsList[i][1]))
        small_airport_longitude.append(float(airportsList[i][2]))
        # if (airportsList[i][3] != ""):
        #     small_airport_elevation.append(int(airportsList[i][3]))
        # else:
        #     small_airport_elevation.append(1210)
    elif (airportsList[i][0] == "medium_airport"):
        medium_airport_latitude.append(float(airportsList[i][1]))
        medium_airport_longitude.append(float(airportsList[i][2]))
        # if (airportsList[i][3] != ""):
        #     medium_airport_elevation.append(int(airportsList[i][3]))
        # else:
        #     medium_airport_elevation.append(1210)
    elif (airportsList[i][0] == "large_airport"):
        large_airport_latitude.append(float(airportsList[i][1]))
        large_airport_longitude.append(float(airportsList[i][2]))
        # if (airportsList[i][3] != ""):
        #     large_airport_elevation.append(int(airportsList[i][3]))
        # else:
        #     large_airport_elevation.append(1210)
    elif (airportsList[i][0] == "seaplane_base"):
        seaplane_base_latitude.append(float(airportsList[i][1]))
        seaplane_base_longitude.append(float(airportsList[i][2]))
    elif (airportsList[i][0] == "heliport"):
        heliport_latitude.append(float(airportsList[i][1]))
        heliport_longitude.append(float(airportsList[i][2]))
    elif (airportsList[i][0] == "balloonport"):
        balloonport_latitude.append(float(airportsList[i][1]))
        balloonport_longitude.append(float(airportsList[i][2]))
    elif (airportsList[i][0] == "closed"):
        closed_airport_latitude.append(float(airportsList[i][1]))
        closed_airport_longitude.append(float(airportsList[i][2]))

print("Small Airport: " + str(len(small_airport_latitude)))
print("Medium Airport: " + str(len(medium_airport_latitude)))
print("Large Airport: " + str(len(large_airport_latitude)))
print("Seaplane Base: " + str(len(seaplane_base_latitude)))
print("Heliport: " + str(len(heliport_latitude)))
print("Closed: " + str(len(closed_airport_latitude)))
#Enable if graphing elevation
# for i in range(len(small_airport_elevation)):
#     if (small_airport_elevation[i] <= 1200):
#         small_airport_elevation[i] = 1200/900
#     else:
#         small_airport_elevation[i] /= 900
# for i in range(len(medium_airport_elevation)):
#     if (medium_airport_elevation[i] <= 1200):
#         medium_airport_elevation[i] = 1200/900
#     else:
#         medium_airport_elevation[i] /= 900
# for i in range(len(large_airport_elevation)):
#     if (large_airport_elevation[i] <= 1200):
#         large_airport_elevation[i] = 1200/900
#     else:
#         large_airport_elevation[i] /= 900

df = pd.DataFrame.from_items([('Longitude', small_airport_longitude), ('Latitude', small_airport_latitude)])
df2 = pd.DataFrame.from_items([('Longitude', medium_airport_longitude), ('Latitude', medium_airport_latitude)])
df3 = pd.DataFrame.from_items([('Longitude', large_airport_longitude), ('Latitude', large_airport_latitude)])

pd.options.display.mpl_style = 'default' #Better Styling
new_style = {'grid': False} #Remove grid
matplotlib.rc('axes', **new_style)

ax=df.plot(kind='scatter', x='Longitude', y='Latitude',color='white',xlim=(-180,180),ylim=(-90, 90),s=0.5,alpha=.4)
df2.plot(kind='scatter', x='Longitude', y='Latitude',color='white',xlim=(-180,180),ylim=(-90, 90), s=1,alpha=.5, ax=ax)
df3.plot(kind='scatter', x='Longitude', y='Latitude',color='white',xlim=(-180,180),ylim=(-90, 90), s=1.5,alpha=.6, ax=ax)

ax.set_axis_bgcolor('#1B1E25') #Background Color
fig = ax.get_figure()
fig.set_size_inches(34, 17)
fig.savefig("s-m-l airports.png", dpi=600)
