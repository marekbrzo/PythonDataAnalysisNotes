# OUTLIER ANALYSIS
# Outlier detection is useful for the following: Preprocessing task for analysis or machine learning. Analytical 
# methods of its own.

# Three main types of outliers:
# Point outliers: observations anomalous with respect to the majority of observation in a feature( univariate outlier)
# Contextual outliers: observations considered anomalous give a specific context. (E.g., Warm day, but where and when)
# Collective outliers: a collection of observations anomalous but appear to close to one another because they all have
# a similar anomalous value.

# Methods for Outlier Detection
# Extreme value analysis with the Tukey methods.
# Multivariate analysis with boxplots and scatterplot matrices.
# Machine learning - density-based spatial clustering of applications with noise (DBSCAN) and PCA.

# Outlier Analysis can be used for: Discovering anomalies such as, Equipment failure, Fraud, Cybersecurity event.

# In this section we will be using the Tukey method. They can be used to find extreme values outside the interquartile
# range.
# When looking at boxplots, the whiskers are set at 1.5 the interquartile range. Most likely data points outside the 
# whiskers are outliers. The most top whisker to the most top box bar represents the UPPER QUARTILE, here 25% of the 
# data points are higher then the box bar value. Analogues with the UPPER QUARTILE, is the LOWER QUARTILE, where the 
# extreme lows are.
# Instead of using the BOXPLOT we can determine the TUKEY Outlier Label mathematically.
# Interquartile Range (Spread: IQR) = Distance between the Lower Quartile (@25% [1st:Q1]) and the Upper Quartile(@75% [3rd:Q3])
#  a = Q1 - 1.5(IQR)
#  b = Q3 + 1.5(IQR)
# Mins below a or maxs above b, then the variable is suspect for outliers.

#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb
from matplotlib.pylab import rcParams


#%%
rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv"
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
# Lets make a BoxPlot
flower_data.boxplot(return_type = 'dict')
plt.plot()

#%%
# Notice in the Sepal width plot, values above 4 and below 2.05 are great outlier candidates. The lie outside the whiskers.
# Let us deal with this outliers. First we need to filter out the data.

sepal_width =flower_data.iloc[:,1]
iris_outliers = (sepal_width > 4)
flower_data[iris_outliers]

#%%
# Now values of sepal width less than 2.05
sepal_width =flower_data.iloc[:,1]
iris_outliers = (sepal_width < 2.05)
flower_data[iris_outliers]

# This is how visually we determine outliers

#%%
# Applying the Tukey outlier method.
pd.options.display.float_format = '{:.1f}'.format
x_flower_data = pd.DataFrame(flower_data_x)
print (x_flower_data.describe())

#%%
# We can determine the IQR mathematically.
# IQR = 3.3 - 2.8 = 0.5
# Tukey = (1.5)*IQR = 0.75
# Outliers in the first quartile = 2.8 - 0.75 = 2.05
# Our min values is less than that.
# Outliers in the third quartile = 3.3 + 0.75 = 4.05
# Our max value is more than that.