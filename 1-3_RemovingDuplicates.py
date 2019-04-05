# In the following section we will remove duplicates.
# We remove duplicates to mainain consistent and accurate datasets. Attempt to remove erronous
# or misleading  data and statistics
# Example. One customer buy 4 different ways (ie, Credit card 1, Credit card 2, cash, Bank transfer)
# We need to make sure it is only one customer and not a duplicated customer.

#%%
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#%%
# Lets create a DataFrame using a dictionary for our example
DF_obj = DataFrame({'column 1' : [1,1,2,2,3,3,3],
                    'column 2' : ['a','a','b','b','c','c','c'],
                    'column 3' : ['A','A','B','B','C','C','C']})
DF_obj

#%%
# Let us find the duplicates by using the .duplicated() method
# Returns Boolean statement, where the row is a duplicate or not
DF_obj.duplicated()

#%%
# To drop duplicates we can use the .drop_duplicates(['column_name']) method
DF_dropped = DF_obj.drop_duplicates()
DF_dropped

#%%
# Finally we look at drop duplicates for columns.
DF_obj2 = DataFrame({'column 1' : [1,1,2,2,3,3,3],
                    'column 2' : ['a','a','b','b','c','c','c'],
                    'column 3' : ['A','A','B','B','C','D','C']})
DF_obj2

#%%
# Drops all duplicated rows only found in the last column
DF_dropped_col = DF_obj.drop_duplicates(['column 3'])
DF_dropped_col