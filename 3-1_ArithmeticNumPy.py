# Basic Math and Statistics using NumPy
# We will perform basic arithmetic
# Numpy works really well with arithmetic. Works well with arrays and matrices

#%%
import numpy as np

from numpy.random import randn
# randn generates both positive and negative numbers

# Print out more decimal values
np.set_printoptions(precision=2)

#%%
# Creating arrays
a = np.array([1,2,3,4,5,6])
a

#%%
# Simple Matrix
b = np.array([[10,20,30],[40,50,60]])
b

#%%
# Creating Arrays via assingment method
np.random.seed(25)
c = 36*np.random.randn(6)
c

#%%
# Last method to create an array
d = np.arange(1,35)
d

#%%
# Performing arthimetic on arrays and matrices
a*10

#%%
c+a

#%%
c-a

#%%
c*a

#%%
c/a

#%%
# Multiplying matrices and basic linear algebra
aa = np.array([[2.,4.,6.],
                [1.,3.,5.],
                [10.,20.,30.]])
aa

#%%
bb = np.array([[0.,1.,2.],
                [3.,4.,5.],
                [6.,7.,8.]])
bb

#%%
# Matrix multiplication
aa*bb

#%%
# Dot product is also matrix multiplication of matrices
np.dot(aa,bb)

#%%
