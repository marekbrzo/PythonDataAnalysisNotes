# Linear Regression is a statistical machine learning method you can use to quantify, and make predictions based on, 
# relationships between numerical variables
# Simple linear regressions: One predictor and one predictant
# Multiple linear regressions: Multiple predictors and one predictant
# Uses for linear regression: 
# Sales forecasting
# Resource consumption forecasting
# Supply cost forecasting
# Telecom services lifecycle forecasting
# HEAVY ASSUMPTIONS
# All variables are continous numeric, not categorical.
# Data is free of missing values and outliers.
# There's aa linear relationship between predictors and predictant
# All predictors are independent of each other.
# Residuals(prediction errors) are normally distributed.

# Multiple linear regressions examples

#%%
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb

import sklearn

from pylab import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter

#%%
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

#%%
# Multiple linear regression on the enrollment data
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch08/08_01/enrollment_forecast.csv"
enroll = pd.read_csv(address)
enroll.columns = ["Year","Enrollment", 'Unemployment','H.S. Graduation','Income']
enroll.head()


#%%
# Lets look for a linear relationship, by using scatterplot (pair plot) matrix
sb.pairplot(enroll)

#%%
# Quick correlation
print(enroll.corr())

#%%
enroll_data = enroll.iloc[:,2:4].values
enroll_target = enroll.iloc[:,1].values

X, y = scale(enroll_data), enroll_target

#%%
# Checking for missing values
missing_values = X==np.NAN
X[missing_values == True]

#%%
LinReg = LinearRegression(normalize =True)
LinReg.fit(X,y)

print(LinReg.score(X,y))
