# K NEAREST NEIGHBOR CLASSIFICATION
# K-NN is  a supervised classifier that memorizes observations from within a labeled test set to predicti classification labels
# for new, unlabeled observations. Prediction cars transmission by gears, weight and other parameters.
# K-NN makes predictions based on how similar training observations are to the new, incoming observations.
# The more similar the observation's value the more likely they will be classified with the same label.
# K-NN Used cases: Stock Price Prediction, Recommendation Systems, Credit Risk Analysis, Predicitve Trip Planning.
# K-NN Assumptions
# Data has little noise.
# Data is labeled.
# Data only contains relevant features.
# Dataset has distinguishable subgroups.
# Avoid using K-NN on large datasets. It will take a long time.

#%%

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as ply  
import scipy
import sklearn 
import urllib

from pylab import rcParams
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split

#%%
np.set_printoptions(precision =4, suppress = True)
plt.figure(figsize=(10,3))
plt.style.use('seaborn-whitegrid')


#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch06/06_02/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']
car_data_prime = cars.iloc[:,[1,3,4,6]].values

target_data = cars.iloc[:,[9]].values


# Scale our Data
scaled_data = preprocessing.scale(car_data_prime)

#%%
# Let us split the data into test and training sets.
# Training set, is what builds the model, Test set is what we test the trained set on.
car_train, car_test, target_train,target_test = train_test_split(scaled_data, target_data, test_size = 0.33, random_state =17)
# x_train , X_test, y_train, y_test = train_test_split(scaled_data, target_data, test_size = 0.33, random_state =17)

# print(train_car,'ONE')
# print(test_car,'TWO')
# print(train_target,'THREE')
# print(test_target)
#%%
# Building and training our model with training data
model_KNN = neighbors.KNeighborsClassifier()
model_KNN.fit(car_train,target_train.ravel())
print(model_KNN)
predict = model_KNN.predict(car_test)
print(metrics.classification_report(target_test,predict))

#%%
# KNN example 
# Recall is a measure of your model's completeness
# Of all our points labeled 1, only 67% of the results returned were truly relevant.