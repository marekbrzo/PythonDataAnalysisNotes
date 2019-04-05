# In this section we will deal with missing values.
# First we need to find these missing values then you can work with them (fill them in, drop them, etc)
# But becarful when working on DataSets with missing values, you first need to determine whether the missing
# values are significant or not. FOr significant missing values can alter fitting.

# Suppose you have a chart full of ratings with 5 rows of data. In one column a couple values have been omitted.
# You do not want to drop all the data from the rows with the missing column values. You can drop in values
# but what would be better is to approximate missing values ie (averages, median, percentails)

# In this section we will be covering:
# Discover missing
# Filling in for missing values
# COunting missing values
# Filtering out missing values


#%%
import numpy as np
import pandas as pd

from pandas import Series, DataFrame


#%%
# Making a series with missing values. Defining a missing variable equal to null
missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4', 'row 5', 'row 6', missing, 'row 8'])
series_obj

#%%
# Calling the .isnull() function calls the Series, and states whether data is NULL (TRUE) or NOT NULL(FALSE)
series_obj.isnull()

#%%
# Now lets fill in missing values.
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj

#%%
DF_obj.iloc[3:5,0] = missing
DF_obj.iloc[1:4,5] = missing
DF_obj

#%%
# We can fill in missing values with .fillna(#value)
DF_noNaN_WithZero= DF_obj.fillna(0)
DF_noNaN_WithZero

#%%
# We can fill in the missing values also using a dictionary to specify more values
DF_noNaN_Dict = DF_obj.fillna({0:0.1, 5:1.25 })
DF_noNaN_Dict

#%%
# We can also fill forward. THis command fills all NaN values with the previous NONE NaN value
DF_noNaN_Forward = DF_obj.fillna(method='ffill')
DF_noNaN_Forward

#%%
# Time to count all NULL values. We can use the .sum() feature to count.
DF_obj.isnull().sum()

# Results show col 0 has 2 while col 5 has 3 missing values

#%%
# Filtering out missing values. We can drop all rows with missing values using
#  .DROPNA(). But this is dangerous at times. Lose lots of data
DF_no_NaN = DF_obj.dropna()
DF_no_NaN

#%% 
# Dropping out missing value COLUMNS. Set .dropna(axis = 1 )
DF_no_NaN_col = DF_obj.dropna(axis=1)
DF_no_NaN_col

#%%
# Drops only rows that have ALL missing values.
DF_no_NaN_ALL = DF_obj.dropna(how='all')
DF_no_NaN_ALL

#%%
