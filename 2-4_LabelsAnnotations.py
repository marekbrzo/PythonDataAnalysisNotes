# Labels and Annotations: Labeling plot features, adding a legend to your plot, annotation your plot
# You may want to detail the visualizations more to give more information.
# Two methods to detail the graph, Functional and ObjectOriented
# We will use the .annotated functions to add these features
# .annotate(xy,xytext, arrowprop)
# Here are some parameters:
# xy = the location being annotated
# xytext = the location of the text
# arrowprop = draws an arrow from the text to the annotated point by giving a dictionary of arrow properties.
# .legend(label and loc) placing a legend on plot axes
# label = variable or category label
# loc = location of legend

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from pandas import Series, DataFrame
from pylab import rcParams

#%%
rcParams['figure.figsize'] = [5,4]
sb.set_style('whitegrid')

#%%
# Labelling simple bar plots
x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

plt.bar(x,y)

plt.xlabel('The X-Axis Label')
plt.ylabel('The Y-Axis Label')


#%%
# Labelling simple pie charts
# Pie charts need a special type of 'description' labels.
z = [1,2,3,4,0.5]

vehicle_type =['Train','Bicycle','Bus','Car','Boat']

plt.pie(z,labels=vehicle_type)
plt.show()


#%%
# Now lets label the chart using the object oriented method
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

mpg =cars.MPG

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(10))

ax.set_xticklabels(cars.iloc[0],rotation=60, fontsize = 'medium')
ax.set_title("Miles per Gallon of Cars in mtcars")

ax.set_xlabel(' Car Names ')
ax.set_ylabel(' Miles/Gallon')

#%%
# Adding a Legend by The functional method - Graph made first
plt.pie(z)
plt.legend(vehicle_type,loc ='best')
plt.show()

#%%
# Adding a Legend using the Oriented 
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.iloc[0],rotation=60, fontsize = 'medium')
ax.set_title("Miles per Gallon of Cars in mtcars")
ax.set_xlabel(' Car Names ')
ax.set_ylabel(' Miles/Gallon')

ax.legend(loc ='best')

#%%
# Annotating our plots
mpg.max()

#%%
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title("Miles per Gallon of Cars in mtcars")
ax.set_ylabel(' Miles/Gallon')
ax.set_ylim([0,45])

ax.annotate('Toyota Corolla', xy=(19,33.9), xytext = (21,35),
            arrowprops = dict(facecolor = 'black', shrink = 0.05))

#%%
