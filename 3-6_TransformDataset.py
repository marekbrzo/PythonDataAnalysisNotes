# Scaling and Transforming Data
# We scale our data to prevent differing magnitude amoung variables from producing erroneous or misleading statsitics.
# Prepare our data
# Two ways of scaling our data. 
# 1. Normalization - putting each observation on a relative scale between 0 and 1.
# 2. Standardization - rescaling data so it has a zero mean and unit variance.
# Here we will use Scikit-learn preprocessing.
# Used for: scale data, center data, normalize data, bin data, impute data

#%%
import numpy as np
import pandas as pd 
import scipy
import sklearn
import matplotlib.pyplot as plt 
import seaborn as sb

from sklearn import preprocessing
from sklearn.preprocessing import scale
from matplotlib import rcParams

#%%
rcParams['figure.figsize'] = 8, 4
plt.style.use('seaborn-whitegrid')

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch03/03_03/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

#%%
mpg = cars['MPG']
plt.plot(mpg)

#%%
mpg.describe()

#%%
# Reshaping values
mpg_matrix = mpg.values.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

#%%
# Reshaping values with a specific range
mpg_matrix = mpg.values.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)

#%%
# Time to standardize using scale()
standardized_mpg =scale(mpg,axis =0, with_mean =False, with_std = False)
plt.plot(standardized_mpg)

#%%
# Standards to mean of zero
standardized_mpg =scale(mpg)
plt.plot(standardized_mpg)

#%%
