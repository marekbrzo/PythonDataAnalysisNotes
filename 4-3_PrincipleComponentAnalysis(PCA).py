# PRINCIPAL COMPONENT ANALYSIS (PCA)

# Singular value decomposition (SVD)
# A linear algebra method that decomposes a matrix into three resultant matrices to reduce information redundancy and noise.
# Most commonly used in PCA.
# Basically we brake one original matrix into three smaller matrices:  A = u X s x v.
# Where u is the left orthogonal matrix; holds important, non redundant information about OBSERVATIONS
# matrix v is the right orthogonal matrix, and it too holds important, non redundant information but on FEATURES.
# and s is the diagonal matrix that contains all of the information about the decomposition process performed during the 
# compression.

# PCA looks at Principle Componenets
# Uncorrelated features taht embody a dataset's important infromation (its 'variance') with the redundancy, noise, and outliers
# stripped out.
# PCA is used for: Fraud detection, spam detection, image and speech recognition, and outlier removal.

# Using Factors and componenets. Both factors and components represent what is left of a dataset after information redundancy and 
# noise is stripped out.
# We can use them as input variables for machine learning algorithms, to generate predictions from these compressed representations
# of our data.

#%%
import numpy as np
import pandas as pd 
import sklearn
import matplotlib.pyplot as plt 
import seaborn as sb 

from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

#%%
rcParams['figure.figsize'] = [5,4]
sb.set_style('whitegrid')


#%%
iris = datasets.load_iris()
iris_data = iris.data 
variable_name = iris.feature_names
iris_data[0:10,]

#%%
# We are now to find the PCA object, call the fit method to find the principal componenets, and then apply the dimensionality
#  reduction on Iris_data by calling the transform method

pca = decomposition.PCA()
iris_pca = pca.fit_transform(iris_data)

# In order to determine the variance: The explained variance ratio tell you how much of the information is compressed into the
# first few components.
pca.explained_variance_ratio_

#%%
# Cumulative variance. When deciding how many componenets to keep, look at the percent of cumulative variance. We try to keep 
# at least 70% of the dataset's information.
pca.explained_variance_ratio_.sum()

#%%
# The goal with PCA is to remove the junk from the data. With a 70% information ratio we can throw out some noise and redundacies
# From our example we can see that most of our data is found in the first two componenets. So throwing out the last two would be a 
# smart idea. We would be retaining 97% of the data.
# Let's us look at our principal componenets.

components = pd.DataFrame(pca.components_,columns = variable_name)
components

#%%
# A visual representation using a heatmap
sb.heatmap(components)

#%%
# We look at the first two components. We can see that component 1 is strongly positively correlated with petal length, and moderately
# correlated with sepal length and petal width.
# These components can be used to determine the inputs for other machine learning programs.

