# Logistic Regression is a simple machine learning method you can use to predict the value of a numeric 
# categorical variable based on its relationship with predictor variables.
# 
# HARD ASSUMPTIONS
# Data is free of missing values.
# The predictant variable is binary (only accepts two values) or ordinal( a categorical variable with 
# order values).
# All predictors are independent of each other.
# There are at least 50 observations per predictor variable (to ensure reliable results).


#%%
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import scipy

import sklearn

from pylab import rcParams
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.preprocessing import scale



#%%
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch08/08_02/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ["Car Names","Miles Per Gallon", 'Cylinders','Displacement','Horsepower','Drive Axel Ratio','Weight','1/4 Mile Time','VS (Cylinder Configuration)','Transmission','Number of Forward Gears','Number of Carburators']
cars.head()

#%%
cars_data = cars.iloc[:,[5,11]].values
cars_data_names = ['Drive Axel Ratio','Number of Carburators']

y = cars.iloc[:,9].values

#%%
# Checking for independance between features.
sb.regplot(x='Drive Axel Ratio', y='Number of Carburators', data = cars, scatter=True)

#%%
# Checking spearman correlation between Drive Axel and Carburators
drat = cars['Drive Axel Ratio']
carb = cars['Number of Carburators']

spearmanr_coefficient, p = spearmanr(drat,carb)
print('Spearman Rank Correlation Coeffcient %0.3f' %(spearmanr_coefficient))

#%%
# Checking for missing values
cars.isnull().sum()

#%%
# Check that our target is binary or ordinal
sb.countplot(x = 'Transmission', data=cars, palette='hls')

#%%
# Check our size is sufficient
cars.info()
# a little small so be a bit concerned.

#%%
#Deploying and evaluating our model
X = preprocessing.scale(cars_data)

LogReg = LogisticRegression(solver='lbfgs')

LogReg.fit(X,y)
print(LogReg.score(X,y))


#%%
# Evaluate model on precision and recall

y_pred = LogReg.predict(X)
print(classification_report(y,y_pred))

#%%
