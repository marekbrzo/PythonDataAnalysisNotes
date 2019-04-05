# Why use Panda library? The Panda library provides fast cleaning, preperation, and analysis for data. It is easy to use for data visulaizations and machine learning.
# Pandas is built on top of NumPy, which makes it easy to work with arrays, matrices. In Panda arrays are called Series, while Matrices are called DataFrames.
# A DataFrame is a set of Series (similar to matrices and arrays).
# Index is a list of integers or labels you use to uniquely identify rows or columns. We use square brackets [] to index.

# Operators to consider in Python
#  == TRUE if two operands are equal
#  != TRUE if two operands are NOT equal
#  <> TRUE if two operands are NOT equal
#  > TRUE if LEFT operand is larger than the RIGHT operand
#  < TRUE if LEFT operand is smaller than the RIGHT operand
#  >= TRUE if LEFT operand is larger than or equal to the RIGHT operand
#  >= TRUE if LEFT operand is smaller than or equal to the RIGHT operand

#%%
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#%%
# Developing rows
series_obj = Series(np.arange(8), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'])
series_obj

#%%
# Calling row with specific text
series_obj['row 7']

#%%
# Calling row with indexers
series_obj[[0,7]]

#%%
# Develping random DataFrame with 36 values.
np.random.seed(25)
DF_obj  = DataFrame(np.random.rand(36).reshape((6,6)), 
                    index= ['row 1','row 2','row 3','row 4','row 5','row 6'],
                    columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
DF_obj

#%%
# Retrieveing data using .loc for string, .iloc for index, 
# NOTE ix has depreciated as of Python 3.6
DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']]

#%%
# Data Slicing
# Work in the similar method as retrival, however it has a COLON (:) seperating the starting and ending indicies
series_obj['row 3': 'row 7']

#%%
# Comparing with scalars. 
# We will be using the conditional operands seen above to determine whether the comparison is true or false
DF_obj < 0.2

#%%
# We can use this condtional operand to create filters
series_obj[series_obj > 6]


#%%
# Finally let us set values within a Series, this will work also in DataFrame, because they are just multiple Series
series_obj['row 1', 'row 5', 'row 8'] =8
series_obj