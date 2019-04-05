# Factor Analysis 
# A method used to explore data to find ROOT causes that explain why dat a is acting a certain way.
# Factors or also know as variables, that are quite meaninful but are inferred and not directly observable.
# Example: Variable 1, 2 ,3, 4 are providing use with data. However, percentages of A and B cause all other 
# variables (1,2,3,4). They are the root factors

# Assumptions for factor analysis
# 1. Features are metric
# 2. Features are continous or ordinal
# 3. There is r> 0.3 correlation between the features in your data set.
# 4. You have more than 100 observations and more than 5 observations per feature
# 5. Sample is homogenous

# In this demonstrations we will use the IRIS dataset, built with scikit learn

#%%
# Factor Analysis is found from the scikit-learn library
import numpy as np 
import pandas as pd 
import sklearn

from sklearn.decomposition import FactorAnalysis

# from sklearn import datasets
from sklearn.datasets import load_iris

#%% 
# Loading data
iris = load_iris()

#%%
# Transforming data into scalable variable
iris_data = iris.data

#%%
# Retrieving the feature names, and prinitng out first 10, a small preview
variable_names = iris.feature_names
iris_data[0:10,:]


#%%
factor = FactorAnalysis().fit(iris_data)
# Data frame formulations
pd.DataFrame(factor.components_,columns = variable_names)

#%%
