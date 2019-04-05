# OTHER DATA CHARTS: Histograms, Box Plot, Scatterplots
# Histograms: Shows a variable's distribution as a set of adjacent rectangles on a data chart. Represemts counts 
# of data within a numerical range of values.
# Scatterplots: Useful for exploring interrelations or dependencies between two different variables. Ideal for 
# visually spotting outliers and trends in data.

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from pandas import Series, DataFrame
from pandas.plotting import scatter_matrix
from pylab import rcParams

#%%
%matplotlib inline
rcParams['figure.figsize'] = [5,4]
sb.set_style('whitegrid')

#%%
# Method 1 of displaying histogram
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

mpg =cars['MPG']

mpg.plot(kind='hist')

#%%
# Method 2 of displaying chart
plt.hist(mpg)
plt.show()

#%%
# Seaborn version of Histogram plotting, it includes a trend line
sb.distplot(mpg)

#%%
# Scatterplot using Matplotlib
cars.plot(kind='scatter' , x='HP',y ='MPG', c =['Darkgrey'],s=150)

#%%
# Seaborn version of Histogram
sb.regplot(x='HP',y='MPG', data =cars, scatter =True)

#%%
# Scatterplot matrix. Seaborn is the easiest way of doing it
sb.pairplot(cars)

#%%
# Adding a third dimension to the graphs
cars_df = pd.DataFrame((cars.iloc[:,[1,3,4,6]].values), columns = ['MPG','DISP','HP','WT'])
cars_target = cars.iloc[:,9].values
target_names =[0, 1] #Automatic Car = 0, Manual Cars = 1

cars_df['group'] = pd.Series(cars_target,dtype='category')
sb.pairplot(cars_df, hue ='group',palette='hls')

#%%
# Plotting Boxplots
cars.boxplot(column = 'MPG', by = 'AM')
cars.boxplot(column = 'WT', by = 'AM')

#%%
# Seaborn Boxplots
sb.boxplot(x='AM',y='MPG',data=cars,palette='hls')

#%%
