# Visually formating plots help individuals easily read the data presented.
# Some ways to improve the plots are: Plot colours, customizing line styles, setting marker styles.
# Matplotlib has many colour options and you can even use hex color codes for more customization.
# Matplotlib also has many different linestyles, such as dots, dash, dot-dash.
# Matplotlib also has different marker styles

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
# Simple data with Bar plot
x = range(1,10)
y =[1,2,3,4,0.5,4,3,2,1]

plt.bar(x,y)

#%%
# Simple formatting of the same bar plot
wide = [0.5,0.5,0.5,0.9,0.9,0.9,0.5,0.5,0.5]
color = ['salmon']
plt.bar(x,y,width = wide, color = color,align='center')

#%%
# Plotting some cars data
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

DF_2_3 = cars[['CYL','MPG', "WT"]]
DF_2_3.plot()


#%%
# Formating the color theme of the plot
color_theme = ['darkgrey','lightsalmon','powderblue']
DF_2_3.plot(color=color_theme)

#%%
# Simple pie chart coloring using Hex Color Code
z = [1,2,3,4,0.5]
color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.pie(z, colors = color_theme)
plt.show()

#%%
# Customizing line styles
x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x,y,color = 'black')
plt.plot(x1,y1,color ='DarkRed')

#%%
plt.plot(x,y,color = 'black', ls='steps',lw=5)
plt.plot(x1,y1,color ='DarkRed',ls='--', lw=10)

#%%
# Setting plot markers
plt.plot(x,y,color = 'black',marker ='1', mew =20)
plt.plot(x1,y1,color ='DarkRed',marker='+', mew=15)

#%%
