# PARAMETRIC CORRELATIONS
# Correlation does not imply causation: One does not always cause another
# In this section we will discuss the pearson correlation coefficient
# R tends to 1 (Strong Positive Relationship)
# R tends 0 (Not linearly correlated)
# R tends to -1 (Strong Negative Relationship)
# Pearson requires these assumptions: DATA is NORMALLY DISTRIBUTED, CONTINOUS NUMERIC VALUES, LINEARLY RELATED
# Uses: to determine linear relationships between variables. Also we do not rule out possible nonlinear relationships

#%%
import numpy as np 
import pandas as pd 
import scipy
import matplotlib.pyplot as plt 
import seaborn as sb

from pandas import Series, DataFrame
from pylab import rcParams
from scipy.stats import pearsonr

#%%
rcParams['figure.figsize'] = 20, 16
plt.style.use('seaborn-whitegrid')

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch03/03_03/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['Car Name', 'MPG', 'CYL', 'DISP','HP','DRAT','WT','QSEC','VS','AM','GEAR','CARB']

#%%
sb.pairplot(cars)

#%%
car_mpg_wt_qsec_hp = cars[['MPG','HP','QSEC','WT']]
sb.pairplot(car_mpg_wt_qsec_hp)

#%%
# From our pairplot we can see that the data is normally distibuted, linearly related, and continously numeric
# Non continous numeric values are multinomial or binomial variables these are categorical
mpg = cars['MPG']
hp = cars['HP']
qsec = cars['QSEC']
wt = cars['WT']

pearsonr_coefficient, p_value = pearsonr(mpg,hp)
print('Pearson R Correlation Coefficient %0.3f' %(pearsonr_coefficient))

# P value (probability value)is the hypothesis is the probability for a given statitical model that, when the null hypothesis
# is true.
#%%
pearsonr_coefficient, p_value = pearsonr(mpg,qsec)
print('Pearson R Correlation Coefficient %0.3f' %(pearsonr_coefficient))

#%%
pearsonr_coefficient, p_value = pearsonr(mpg,wt)
print('Pearson R Correlation Coefficient %0.3f' %(pearsonr_coefficient))

#%%
# We can also use pandas to calculate the Pearson correlation coefficient
# A simple method will recieve all combinations of the PearsonR values for the data
pearson_car_group = car_mpg_wt_qsec_hp.corr()
pearson_car_group

#%%
# One nice visualization to see these correlations is to use Seaborn heat map function.
sb.heatmap(pearson_car_group, xticklabels = pearson_car_group.columns.values,
                                yticklabels = pearson_car_group.columns.values)

#%%
