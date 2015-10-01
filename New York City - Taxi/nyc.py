import pandas as pd


df=pd.io.gbq.read_gbq("""
SELECT ROUND(pickup_latitude, 4) as lat, ROUND(pickup_longitude, 4) as long, COUNT(*) as num_pickups
FROM [nyc-tlc:yellow.trips_2015]
WHERE (fare_amount/trip_distance BETWEEN 2 AND 10) AND (pickup_latitude BETWEEN 40.61 AND 40.91) AND (pickup_longitude BETWEEN -74.06 AND -73.77 )
GROUP BY lat, long
""", project_id='nycanalysis')


import matplotlib
import matplotlib.pyplot as plt
# #Inline Plotting for Ipython Notebook
# %matplotlib inline

pd.options.display.mpl_style = 'default' #Better Styling
new_style = {'grid': False} #Remove grid
matplotlib.rc('axes', **new_style)
#from matplotlib import rcParams
#rcParams['figure.figsize'] = (17.5, 17) #Size of figure
#rcParams['figure.dpi'] = 250


P=df.plot(kind='scatter', x='long', y='lat',color='white',xlim=(-74.06,-73.77),ylim=(40.61, 40.91),s=.02,alpha=.6)
P.set_axis_bgcolor('#1B1E25') #Background Color
fig = P.get_figure()
fig.set_size_inches(17.5, 17)
fig.savefig("pickupCLEAN.png", dpi=300)
