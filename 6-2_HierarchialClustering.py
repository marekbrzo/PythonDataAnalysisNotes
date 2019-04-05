# HIERACHIAL CLUSTERING
# Hierarchial clustering methods predict subgroups within data by: 
# Finding distancces between each data point and its nearest neighbours.
# Linking the most nearby neighbours.
# Dendrofram are tree graphs that is usually displaying taxonomies, linkages, and relatedness.
#  We can find subgroups by looking at dendrograms.
# Uses for hierarchial clustering: Hospital resource manangement, business process manangement, customer segmentation, social network analysis.
#  For hierarchial clustering we need to find how many centriods to use, we can determine centriods by counting the set of branches in a dendrogram.
# Important parameters for Hierachial clustering
# Distance Metrics: Euclidian, Manhattan, Cosine
# Linkage Paramters: Ward, Complete, Average
# Use trial and error to determine the best

#%%

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as ply 
import seaborn as sb 
import scipy
import sklearn 
import sklearn.metrics as sm

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster,cophenet
from scipy.spatial.distance import pdist
from pylab import rcParams

from sklearn.cluster import AgglomerativeClustering
#%%
np.set_printoptions(precision =4, suppress = True)
plt.figure(figsize=(10,3))
plt.style.use('seaborn-whitegrid')


#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch06/06_02/mtcars.csv"
cars = pd.read_csv(address)

cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']
car_data = cars.iloc[:,[1,3,4,6]].values

target_data = cars.iloc[:,[9]].values

#%%
# Using scipy to generate dendropgrams
# First let us create a linkage
link = linkage(car_data,'ward')

#%%
dendrogram(link,truncate_mode='lastp',p=12,leaf_rotation=45,leaf_font_size=15,show_contracted=True)

plt.title("Truncated Hierarchial Clustering Dendrogram")
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.axhline(y=500,color='black')
plt.axhline(y=150,color='black')
plt.show()

#%%
# Based on the data, and the knowledge of cars, we can suspect there will be two centriods. AM and none-AM
# Therefor we set our max idstance at 500, because at 500 we see two clusters.
# Let do some analysis.

number_cluster =2
HClustering = AgglomerativeClustering(n_clusters = number_cluster, affinity = 'euclidean', linkage ='ward')
HClustering.fit(car_data)

sm.accuracy_score(target_data, HClustering.labels_)
# Result 0.78125 is the best outcome found here and with euclidean and average.

#%%
HClustering = AgglomerativeClustering(n_clusters = number_cluster, affinity = 'euclidean', linkage ='complete')
HClustering.fit(car_data)

sm.accuracy_score(target_data, HClustering.labels_)

#%%
HClustering = AgglomerativeClustering(n_clusters = number_cluster, affinity = 'euclidean', linkage ='average')
HClustering.fit(car_data)

sm.accuracy_score(target_data, HClustering.labels_)

#%%
HClustering = AgglomerativeClustering(n_clusters = number_cluster, affinity = 'manhattan', linkage ='average')
HClustering.fit(car_data)

sm.accuracy_score(target_data, HClustering.labels_)

#%%
