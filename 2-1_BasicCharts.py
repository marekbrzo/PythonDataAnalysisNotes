# In this sub chapter we will be printing out Basic charts using MatplotLib and Seaborn.
# Charts in question are: Line, Bar, Pie plots
# Line chart are good for continous data, Time Plots
# Bar plots are good for categorical data, Which age group BLANK
# Pie proportion data, compared to a whole

# Two types of plot building in Python.
# 1. Functional Method: You build plots by calling the plot function on a variable or set of variables
# 2. Object-oriented Method: You build a plot by generating a blank "figure" object, and then populated that object with plots and plot elements.

# Most common plot langauges in Matplotlib and Seaborn.

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from pandas import Series, DataFrame
from matplotlib import rcParams

#%%
# Runs matplotlib within the output window. FOR Juypter 
# %matplotlib inline
# Set the size of all figures, to a box of 5 width by 4 height ratio
rcParams['figure.figsize'] = [5,4]
# Display style found in Seaborn
sb.set_style('whitegrid')

#%%
# The simplest line plot
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

plt.plot(x,y)

#%%
# We are calling up a CSV file with data located
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']
cars.head()

#%%
# Declaring new variable of a single column
mpg = cars['MPG']
mpg.head()

#%%
# Plotting the new variable
mpg.plot()

#%%
# Plotting multiple variables
DF_CylWtMpg = cars[['CYL','WT','MPG']]
DF_CylWtMpg.plot()

#%%
# Simplest Bar chart
plt.bar(x,y)


#%%
# Plotting using Pandas object DataFrame.plot(kind ='type of plot (bar,line, etc'))
mpg.plot(kind='Bar')


#%%
# Horizontal plot (barh)
mpg.plot(kind ='barh')

#%%
# Simple pie chart. Use show to just print the graph
x_pie = [1,2,3,4,0.5]
plt.pie(x_pie)
plt.show()

#%%
# Saving a plot as an image
plt.savefig('pie_chart.jpeg')
plt.show()

#%%
# Using Juypter we can find the directory using this
%pwd

#%%
