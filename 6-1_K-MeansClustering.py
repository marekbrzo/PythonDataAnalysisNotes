# K-MEANS
# K-means clustering algorithm is  a simple UNSUPERVISED algorith that is used for quickly predicting groupings
# from within an unlabeled dataset.
# Predictions are based on: the number of cluster centers present (k), nearest menas values (measured in Euclidian distance
# between observations)
# Used in: market price and cost modeling, customer segmentation, insurance claim fraud detection, and hedge fund classification.
# Things to consider when using K-means
# Scale your variables
# Look at a scatterplot or the data table to estimate the number of centroids, or cluster centers, to set for the k parameter in 
# the model.

#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as ply 
import sklearn 
import sklearn.metrics as sm

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.metrics import confusion_matrix, classification_report
from mpl_toolkits.mplot3d import Axes3D

#%%
plt.figure(figsize=(7,4))

#%%
# Using the iris database
iris = datasets.load_iris()

scaled_flower = scale(iris.data)
target_variable = pd.DataFrame(iris.target)
variable_names = iris.feature_names
scaled_flower[0:10,]

#%%
# Let us build and run the model. First let us obstaintate a cluster.
clustering = KMeans(n_clusters = 3, random_state =5)
clustering.fit(scaled_flower)

#%%
# Plotting our model outputs
iris_df = pd.DataFrame(iris.data)
iris_df.columns=['Sepal_Length','Sepal_Width', 'Petal_Lenght','Petal_Width']
target_variable.columns = ['Target']

# iris_df.loc[:,'Petal Length'].head()
#%%
color_theme = np.array(['darkgrey','lightsalmon','powderblue'])
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Lenght, y=iris_df.Petal_Width, c =color_theme[iris.target], s=50) 
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Lenght, y=iris_df.Petal_Width, c =color_theme[clustering.labels_], s=50) 
plt.title('K-Means Classification')

#%%
# Change the color number scheme
relabel = np.choose(clustering.labels_, [2,0,1]).astype(np.int64)
plt.subplot(1,2,1)
plt.scatter(x=iris_df.Petal_Lenght, y=iris_df.Petal_Width, c =color_theme[iris.target], s=50) 
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Lenght, y=iris_df.Petal_Width, c =color_theme[relabel], s=50) 
plt.title('K-Means Classification')

#%%
# We can evaluate the clustering results using classification_report method
print(classification_report(target_variable,relabel))

#%%
# Precision: A measure of the model's relevancy
# Recall: a measure of the model's completeness