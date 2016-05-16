"""
By: Maharsh Patel
maharsh@live.ca

"""

import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def returnIntPrice(strPrice):
    price = int(strPrice.replace("$", ""))
    return(price)


with open('./data/properties.csv', 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    properties = list(reader)

# ranges
# 1 = 0-100000
# 2 = 100000-200000
# 3 = 200000-300000
# 3 = 300000-500000
# 4 = 500000 - 700000
# 5 = 700000-1000000
# 6 = 1000000-2000000
# 7 = 2000000-5000000
# 8 = 5000000-10000000
# 9 = 10 million - 100 million
latitudes = [[] for i in range(10)]
longitudes = [[] for i in range(10)]

print(latitudes, longitudes)


for i in range(len(properties)):
    propertyType = properties[i][5]
    if propertyType == "Residential":
        price = returnIntPrice(properties[i][4])
        latitude = float(properties[i][8])
        longitude = float(properties[i][9])

        if price >= 0 and price < 100000:
            latitudes[0].append(latitude)
            longitudes[0].append(longitude)
        elif price >= 100000 and price < 200000:
            latitudes[1].append(latitude)
            longitudes[1].append(longitude)
        elif price >= 200000 and price < 300000:
            latitudes[2].append(latitude)
            longitudes[2].append(longitude)
        elif price >= 300000 and price < 500000:
            latitudes[3].append(latitude)
            longitudes[3].append(longitude)
        elif price >= 500000 and price < 700000:
            latitudes[4].append(latitude)
            longitudes[4].append(longitude)
        elif price >= 700000 and price < 1000000:
            latitudes[5].append(latitude)
            longitudes[5].append(longitude)
        elif price >= 1000000 and price < 2000000:
            latitudes[6].append(latitude)
            longitudes[6].append(longitude)
        elif price >= 2000000 and price < 5000000:
            latitudes[7].append(latitude)
            longitudes[7].append(longitude)
        elif price >= 5000000 and price < 10000000:
            latitudes[8].append(latitude)
            longitudes[8].append(longitude)
        else:
            latitudes[9].append(latitude)
            longitudes[9].append(longitude)

minLatitude = 10000
maxLatitude = 0

for latitudeList in latitudes:
    if min(latitudeList) < minLatitude:
        minLatitude = min(latitudeList)
    if max(latitudeList) > maxLatitude:
        maxLatitude = max(latitudeList)



minLongitude = 0
maxLongitude = -10000   #have to set a negative number because longitudes are negative

for longitudeList in longitudes:
    print(min(longitudeList), max(longitudeList))
    if min(longitudeList) < minLongitude:
        minLongitude = min(longitudeList)
    if max(longitudeList) > maxLongitude:
        maxLongitude = max(longitudeList)
        print(maxLongitude)
print(minLatitude, maxLatitude, minLongitude, maxLongitude)
df = pd.DataFrame.from_items([('Longitude', longitudes[0]), ('Latitude', latitudes[0])])
df2 = pd.DataFrame.from_items([('Longitude', longitudes[1]), ('Latitude', latitudes[1])])
df3 = pd.DataFrame.from_items([('Longitude', longitudes[2]), ('Latitude', latitudes[2])])
df4 = pd.DataFrame.from_items([('Longitude', longitudes[3]), ('Latitude', latitudes[3])])
df5 = pd.DataFrame.from_items([('Longitude', longitudes[4]), ('Latitude', latitudes[4])])
df6 = pd.DataFrame.from_items([('Longitude', longitudes[5]), ('Latitude', latitudes[5])])
df7 = pd.DataFrame.from_items([('Longitude', longitudes[6]), ('Latitude', latitudes[6])])
df8 = pd.DataFrame.from_items([('Longitude', longitudes[7]), ('Latitude', latitudes[7])])
df9 = pd.DataFrame.from_items([('Longitude', longitudes[8]), ('Latitude', latitudes[8])])
df10 = pd.DataFrame.from_items([('Longitude', longitudes[9]), ('Latitude', latitudes[9])])
df=df.astype(float)

pd.options.display.mpl_style = 'default' #Better Styling
new_style = {'grid': False} #Remove grid
matplotlib.rc('axes', **new_style)

ax=df.plot(kind='scatter', x='Longitude', y='Latitude',color='#ffffff',xlim=(min(longitudes[0]),max(longitudes[0])),ylim=(min(latitudes[0]), max(latitudes[0])),s=0.01,alpha=0.8)
df2.plot(kind='scatter', x='Longitude', y='Latitude',color='#fde6e4',xlim=(min(longitudes[1]),max(longitudes[1])),ylim=(min(latitudes[1]), max(latitudes[1])), s=0.04,alpha=.8, ax=ax)
df3.plot(kind='scatter', x='Longitude', y='Latitude',color='#fcceca',xlim=(min(longitudes[2]),max(longitudes[2])),ylim=(min(latitudes[2]), max(latitudes[2])), s=0.07,alpha=.8, ax=ax)
df4.plot(kind='scatter', x='Longitude', y='Latitude',color='#fab6b0',xlim=(min(longitudes[3]),max(longitudes[3])),ylim=(min(latitudes[3]), max(latitudes[3])), s=0.1,alpha=.8, ax=ax)
df5.plot(kind='scatter', x='Longitude', y='Latitude',color='#f99e96',xlim=(min(longitudes[4]),max(longitudes[4])),ylim=(min(latitudes[4]), max(latitudes[4])), s=0.13,alpha=0.8, ax=ax)
df6.plot(kind='scatter', x='Longitude', y='Latitude',color='#f7867b',xlim=(min(longitudes[5]),max(longitudes[5])),ylim=(min(latitudes[5]), max(latitudes[5])), s=0.16,alpha=1, ax=ax)
df7.plot(kind='scatter', x='Longitude', y='Latitude',color='#f66e61',xlim=(min(longitudes[6]),max(longitudes[6])),ylim=(min(latitudes[6]), max(latitudes[6])), s=0.19,alpha=1, ax=ax)
df8.plot(kind='scatter', x='Longitude', y='Latitude',color='#f45647',xlim=(min(longitudes[7]),max(longitudes[7])),ylim=(min(latitudes[7]), max(latitudes[7])), s=0.22,alpha=1, ax=ax)
df9.plot(kind='scatter', x='Longitude', y='Latitude',color='#f33e2d',xlim=(min(longitudes[8]),max(longitudes[8])),ylim=(min(latitudes[8]), max(latitudes[8])), s=0.25,alpha=1, ax=ax)
df10.plot(kind='scatter', x='Longitude', y='Latitude',color='#f22613',xlim=(min(longitudes[9]),max(longitudes[9])),ylim=(min(latitudes[9]), max(latitudes[9])), s=0.28,alpha=1, ax=ax)

ax.set_axis_bgcolor('#000021') #Background Color
fig = ax.get_figure()
fig.set_size_inches((maxLongitude- minLongitude)*50, (maxLatitude - minLatitude)*50)
fig.savefig("houses3.png", dpi=600)
