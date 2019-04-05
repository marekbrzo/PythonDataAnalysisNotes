# DBSCAN for Outlier Detection
# DBSCAN is an unsupervised method that clusters core samples (dense areas of a dataset) and denotes non-core
# samples (spares portions of the datasets)
# Example: Self driving cars, Lanes from Lines.
# Use to identify collective outlers
# Outliers should make up less than or equal to 5% of the total observations.
# IMPORTANT DBSCAN model parameters
# eps: the maximum distance between two samples for them to be clustered in the same neighborhood (start at eps = 0.1)
# min_samples: the minimum number of samples in a neighbourhood for a data point to qualify as a core point (start with
# very loow sample size).

#%%
import numpy as np
import pandas as pd 
import matplotlib.pylab as plt
import seaborn as sb 
import sklearn

from pylab import rcParams
from sklearn.cluster import DBSCAN
from collections import Counter

#%%
rcParams['figure.figsize'] =5,4
sb.set_style('whitegrid')

#%%
# Visually inspecting boxplots
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_02/iris.data.csv"
# Indication that comma seperates data
flower_data = pd.read_csv(address,
                    header = None,
                    sep = ',')
flower_data.columns=['Sepal Length','Sepal Width', 'Petal Lenght','Petal Width', 'Species']
# X and Y values of the data
flower_data_x = flower_data.iloc[:,0:4].values
flower_data_y = flower_data.iloc[:,4].values

flower_data[:5]

#%%
model = DBSCAN(eps = 0.8, min_samples =19).fit(flower_data_x)
print(model)

#%%
# Negative 1 label are outliers. Let us fish them out.
outliers_flower = pd.DataFrame(flower_data_x)
print (Counter(model.labels_))
print (outliers_flower[model.labels_ ==-1])

#%%
# Visualize
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

colors = model.labels_

ax.scatter(flower_data_x[:,2],flower_data_x[:,1],c =colors, s =120)
ax.set_xlabel('Petal Lenght')
ax.set_ylabel('Sepal Width')
plt.title('DBSCAN for Outlier Detection')

#%%
