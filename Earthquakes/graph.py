"""
Earthquake Graphing
By: Maharsh Patel
maharsh@live.ca

Source: http://earthquake.usgs.gov/earthquakes/search/
"""

#imports
import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

with open('earthquakes.csv', 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    earthquakesList = list(reader)

latitude5 = []
longitude5 = []

latitude6 = []
longitude6 = []

latitude7 = []
longitude7 = []

magnitude = []


for i in range(len(earthquakesList)):

    magnitude = float(earthquakesList[i][4])
    if magnitude >= 7:
        latitude7.append(float(earthquakesList[i][1]))
        longitude7.append(float(earthquakesList[i][2]))
    elif magnitude >= 6:
        latitude6.append(float(earthquakesList[i][1]))
        longitude6.append(float(earthquakesList[i][2]))
    else:
        latitude5.append(float(earthquakesList[i][1]))
        longitude5.append(float(earthquakesList[i][2]))


df = pd.DataFrame.from_items([('Longitude', longitude5), ('Latitude', latitude5)])
df2 = pd.DataFrame.from_items([('Longitude', longitude6), ('Latitude', latitude6)])
df3 = pd.DataFrame.from_items([('Longitude', longitude7), ('Latitude', latitude7)])
df=df.astype(float)


pd.options.display.mpl_style = 'default' #Better Styling
new_style = {'grid': False} #Remove grid
matplotlib.rc('axes', **new_style)

ax=df.plot(kind='scatter', x='Longitude', y='Latitude',color='white',xlim=(-180,180),ylim=(-90, 90),s=4,alpha=.4)
df2.plot(kind='scatter', x='Longitude', y='Latitude',color='#e67e22',xlim=(-180,180),ylim=(-90, 90), s=40,alpha=.4, ax=ax)
df3.plot(kind='scatter', x='Longitude', y='Latitude',color='#e74c3c',xlim=(-180,180),ylim=(-90, 90), s=80,alpha=.5, ax=ax)

ax.set_axis_bgcolor('#1B1E25') #Background Color
fig = ax.get_figure()
fig.set_size_inches(34, 17)
fig.savefig("earthquakes3.png", dpi=600)
