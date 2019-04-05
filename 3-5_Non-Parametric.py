# Used to calculate non-continous , non-distributed variable, categorical correlations
# We will used Spearman's rank correlation and Chi-Square test
# Spearman's Rank Correlation works on ordinal data type. Ordinal data is a numeric variable that can be categorized.
# These variable pairs are then able to be ranked according to the strength of the correlation between them.
# R tends to 1 (Strong Positive Relationship)
# R tends 0 (Not linearly correlated)
# R tends to -1 (Strong Negative Relationship)
# SpearmanR requires these assumptions: DATA is NOT normally distribution, ORDINAL data, nonlinearly related.
# CHi-Square Tables Test for independence.
# A p value LESS than 0.05, we REJECT the null hypothesis and conclude that the variables are correlated.
# A p value MORE than 0.05, we ACCEPT the null hypothesis and conclude that the variables are independent.
# Chi-Squared test needs categorical or numeric varaiables. We must bin the numeric varaibles.


#%%
import numpy as np 
import pandas as pd 
import scipy
import matplotlib.pyplot as plt 
import seaborn as sb

from pandas import Series, DataFrame
from pylab import rcParams
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency

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
cars_cyl_vs_am_gear = cars[['CYL','VS','AM','GEAR']]
sb.pairplot(cars_cyl_vs_am_gear)

#%%
# Isolating variables
cyl = cars['CYL']
vs = cars['VS']
gear = cars['GEAR']
am = cars['AM']

# SPEARMANR 
spearmanr_coefficient, p_value = spearmanr(cyl,vs)
print('Spearman R Correlation Coefficient %0.3f' %(spearmanr_coefficient))

#%%
spearmanr_coefficient, p_value = spearmanr(cyl,am)
print('Spearman R Correlation Coefficient %0.3f' %(spearmanr_coefficient))

#%%
spearmanr_coefficient, p_value = spearmanr(cyl,gear)
print('Spearman R Correlation Coefficient %0.3f' %(spearmanr_coefficient))

#%%
# CHI-SQUARED
table = pd.crosstab(cyl,am)

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-squared Statistic %0.3f p_value %0.3f' %(chi2,p))

#%%
table = pd.crosstab(cyl,vs)

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-squared Statistic %0.3f p_value %0.3f' %(chi2,p))

#%%
table = pd.crosstab(cyl,gear)

chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-squared Statistic %0.3f p_value %0.3f' %(chi2,p))

#%%
