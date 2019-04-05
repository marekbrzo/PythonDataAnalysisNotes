# TIME SERIES
# A measure of unit change over time. Useful for predicting and forcasting from historical data
# Frequent models used: ARMA, ARIMA (Box-Jenkins)
# A bunch of trends: Constant time Series, Trended Time Series, Untrendede Seasonal Time Series, Trended Seasonal Time Series

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from pandas import Series, DataFrame
from pylab import rcParams

#%%
address = "C:/Users/Marek/Desktop/Python/Ex_Files_Python_Data_Science_EssT/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch02/02_05/Superstore-Sales.csv"
supersale = pd.read_csv(address, index_col = 'Order Date', parse_dates = True, encoding = "ISO-8859-1")
supersale.head()

#%%
# Plotting time series
supersale['Order Quantity'].plot()

#%%
# Previous plot was very messy with lots of data. Lets take a random sample of 100 data points
supersale_100 = supersale.sample(n=100, random_state=25, axis =0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

supersale_100['Order Quantity'].plot()

#%%
