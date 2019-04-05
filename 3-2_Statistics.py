# Statistics
# Two categories of descriptive statistics:
# 1. Descriptive statistics that describe the values of observation in a variable: SUM, MEDIAN, MEAN, MAX
# 2. Descriptive statistics that describe a variable spread: STANDARD DEVIATION, VARIANCE, COUNTS, QUARTILES
#  Uses for descriptive statistics:
# Detecting outliers, 
# planning data preparations requirements for data preprocessing, 
# selecting features for use in machine learning

#%%
import numpy as np
import pandas as pd
import scipy

from pandas import Series, DataFrame
from scipy import stats

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch03/03_02/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

cars.head()

#%%
# Lets take a peek at the summary statistics that describe a variable's numeric value
# First lets look at the sum
cars.sum()

#%%
# Sum by row
cars.sum(axis=1)

#%%
# Median is the middle value in the data (in the columns, axis = 0)
cars.median()

#%%
# Mean is the average value in the data
cars.mean()

#%%
# Max is the maximum value found in each series
cars.max()

#%%
# To located the maximum value we call the .idxmax() method
mpg=cars['MPG']
mpg.idxmax()

#%%
# Now we will look into the summary statitics that describe the variable distribution
# The standard deviation is calculated by the following command
cars.std()

#%%
# The variance is the standard deviation squared, and it is called by the .var() command
cars.var()

#%%
# The counts the unique variables and tallys them up
gear = cars['GEAR']
gear.value_counts()

#%%
# The .describe() command gives us a nice statitical diagnosis of our data
cars.describe()

#%%
