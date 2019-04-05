# CATEGORICAL DATA
# A categorical values, accepts only a limited and fixed number of values. Each observation is assigned to a specific
# subgroup.
# Example, types of fruits
# Cross-tabulatios are functions taht summarizes or combines two (or more) features.
# By default crosstabs show frequency counts for features

#%%
import numpy as np
import pandas as pd

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch03/03_03/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

cars.head(15)


#%%
carb = cars['CARB']
carb.value_counts()

#%%
cars_category = cars[['CYL','VS','AM','GEAR','CARB']]
cars_category.head()

#%%
# Now lets group the DataFrame by its values in a particular column. The function is called .groupby() found in DataFrame library
gears_group = cars_category.groupby('GEAR')
gears_group.describe()

#%%
# Let us transform variables to categorical data type
# We do this by running the pd.Series() method, but within we pass in the dtype = 'category' argument.
cars['GROUP'] = pd.Series(cars['GEAR'], dtype ='category')
cars['GROUP'].dtypes


#%%
cars.head()

#%%
# Describing categorical data with crosstabs
# To do this we call the pd.crosstab() function
pd.crosstab(cars['AM'],cars['GEAR'])

#%%
