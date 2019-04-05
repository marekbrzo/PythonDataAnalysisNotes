# Adding plot elements to object oriented plotting
# Object-oriented plotting occurs in the following steps: 
# 1 Creating a blank figure object
# 2 Add axes to the figure
# 3 Generate plot(s) within the figure objects
# 4 Specify plotting and layout parameters for the plots the within the figure

# Generating subplots, have one or more plots in a plot

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from numpy.random import randn
from matplotlib import rcParams
from matplotlib.figure import Figure

#%%
rcParams['figure.figsize'] = [5,4]
sb.set_style('whitegrid')

#%%
# Object oriented plotting
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

# Step 1
fig = plt.figure()
# Step 2
ax = fig.add_axes([.1,.1,1,1])
# Step 3 & 4 
ax.plot(x,y)
ax.set_title("Object Oriented Plotting")


#%%
# Plotting visual improvements
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
ax.set_xlim([1,9])
ax.set_ylim([0,5])
ax.set_xticks([0,1,2,4,5,6,7,9,10])
ax.set_yticks([0,1,2,3,4,5])
ax.plot(x,y)

#%%
# Adding plot grids
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
ax.set_xlim([1,9])
ax.set_ylim([0,5])
ax.grid()
ax.plot(x,y)

#%%
# Lastly let us generate a multiple plot figure. Also called sub plots.
fig = plt.figure()
fig, (ax1,ax2) =plt.subplots(1,2)

ax1.plot(x)
ax2.plot(x,y)

#%%
