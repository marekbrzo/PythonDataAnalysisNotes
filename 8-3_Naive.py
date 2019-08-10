# NAIVE BAYES
# Machine learning method we can use to predict the likelihood that an event will occur 
# evidence that is present in your data.
# Conditional probability P(B|A) = P(A and B) / P(B).

# We can determine spam email by Naive Bayes
# Three types of Naive Bayes
# 1. Multinomial: Good when your features(categorical or continuous) describe discrete frequency
# counts (e.g. word count)
# 2. Bernoulli: Good when making predictions from binary features
# 3. Gaussian: Good when making predictions from normally distributed features.

# Naive Bayes uses: Spam detection, Customer classification, Credit Risk predictions, Health Risk prediction.

# Naive Bayes Assumptions
# Predictors are independant of each other.
# A priori assumptions: This is assumptions that the past CONDITIONS STILL HOLD TRUE.
# When we make predictions from historical values, we will get incorrect results if present circumstances have changed.
# Linear and Logistic Regression models maintain an a prior assumption as well.

#%%
import numpy as np
import pandas as pd

import urllib
import urllib.request

import sklearn

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

#%%
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
raw_data = urllib.request.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")
print (dataset[0])

#%%
X = dataset[:,0:48]
y = dataset[:,-1]

#%%
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .33, random_state = 17)

#%%
# Bernoulli Method
BernNB = BernoulliNB(binarize=True)
BernNB.fit(X_train,y_train)

print(BernNB)

y_predict = BernNB.predict(X_test)
print(accuracy_score(y_test,y_predict))

#%%
# Multinomial Method
MultNB = MultinomialNB()
MultNB.fit(X_train,y_train)

print(MultNB)

y_predict = MultNB.predict(X_test)
print(accuracy_score(y_test,y_predict))


#%%
# Gaussian Method
GausNB = GaussianNB()
GausNB.fit(X_train,y_train)

print(GausNB)

y_predict = GausNB.predict(X_test)
print(accuracy_score(y_test,y_predict))

#%%
# Optmizing Naive Models
BernNB = BernoulliNB(binarize=0.1)
BernNB.fit(X_train,y_train)

print(BernNB)

y_predict = BernNB.predict(X_test)
print(accuracy_score(y_test,y_predict))


#%%
