import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
df = pd.read_csv("GrowLocations.csv")
df=df.rename( columns={'Latitude': 'Longitude','Longitude':'Latitude'})
df = df[(df.Longitude != 0) & (df.Latitude != 0)]
df = df[df['Longitude'].between(-10.592, 1.6848) & df['Latitude'].between(50.681, 57.985)]
df = df.drop_duplicates(subset='Serial', keep='first')
df.to_csv('GrowLocationsClean.csv')
df = pd.read_csv('GrowLocationsClean.csv', header=0)
BBox = (-10.592, 1.6848,50.681, 57.985)
plotmap = 'map7.png'
truthplot = plt.imread(plotmap)
ax = df.plot.scatter(x='Longitude', y='Latitude', c='Red')
plottitle = "Plotting Grow Data"
ax.set_title(plottitle)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
ax.imshow(truthplot, zorder=0, extent = BBox, aspect= 'equal')
plt.show()