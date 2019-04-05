# Exploring data and subgroups. We can easily view.
# Reason for grouping data: comparing subsets, deduce reason why subgroups differ, subset your data 
# for analysis

#%%
import numpy as np
import pandas as pd
from pandas import Series, DataFrame



#%%
# We are calling up a CSV file with data located
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv"
# Using the pandas .read_csv to open the data 
cars = pd.read_csv(address)

# Changing column names
cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

# First 5 rows
cars.head()

#%%
# We want to group our data by cylinders in a car
cars_groups = cars.groupby(cars['CYL'])

# Take a means of each subset
cars_groups.mean()

#%%
