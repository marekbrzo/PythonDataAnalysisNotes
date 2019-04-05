# Sometime data is not found on one tables. Therefor we need to concatenate data to our specific needs.
# When we concatenate data, we create new data sets, using seperate distinct data sources.
# We combine Series and DataFrames to help us further analyze data from many sources.
# We will be using the pd.concat() function, found in pandas

# Transforming data converts the data to the format that we desired to help facilitate analysis.
# Below we will: Drop data, Add Data, and Sort Data

#%%
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#%%
DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj

#%%
DF_obj2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj2


#%%
# To concatedate we use the pd.concat([obj_1, obj_2], axis=1) method
DF_joined = pd.concat([DF_obj,DF_obj2],axis=1)
DF_joined
#%%
# By default Python concatenates by column values, axis = 0
DF_joined_default = pd.concat([DF_obj,DF_obj2])
DF_joined_default

#%%
# We will clean up some of this data.
DF_dropped = DF_obj.drop([0,2])
DF_dropped

#%%
# Cleaning up columns
DF_dropped_col = DF_obj.drop([0,2],axis=1)
DF_dropped_col

#%%
# Adding data
# Setting up an array
series_obj = Series(np.arange(6))
series_obj.name = 'Added Variable'
series_obj

#%%
# With our array let us add it to our variable
# To add two sets of data into one DataFrame we will use .join(Add1, Add2) together
variable_added = DataFrame.join(DF_obj,series_obj)
variable_added

#%%
# Another method using Pandas is the append method.
# Let us append the table onto itself. 
# Using the ignore_index allows us to skip the duplicated indexing concern
added_datatable = variable_added.append(variable_added, ignore_index = False)
added_datatable

#%%
# Using the ignore_index  as true "RE-Indexes"
added_datatable_index = variable_added.append(variable_added, ignore_index = True)
added_datatable_index

#%%
# Finally let us sort our data
# Python does it by using .sort_values(by =[index value], ascending = [BOOL])
# Python sorts BY, where by dictates which index
DF_sorted = DF_obj.sort_values(by=[5],ascending=False)
DF_sorted

#%%
