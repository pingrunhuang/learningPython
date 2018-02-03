
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


def is_outlier(points, threshold=3.5):
    if len(points.shape) == 1:
        # Two dimensional numpy arrays are indexed using a[i,j]
        points = points[:,None]
    median = np.median(points, axis=0)
    # sum up the square value
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)
    # compute modified z zone
    modified_z_score = 0.6745 * diff / med_abs_deviation 
    # return a mask for each outlier
    return modified_z_score > threshold


# In[4]:


x = np.random.random(100)


# In[5]:


buckets = 50


# In[6]:


x=np.r_[x,-49,95,100,-100]


# In[7]:


filterd=x[~is_outlier(x)]


# In[8]:


plt.figure()


# In[9]:


plt.subplot(211)
plt.hist(x, buckets)
plt.xlabel('Raw')


# In[11]:


plt.subplot(212)
plt.hist(filterd, buckets)
plt.xlabel('Cleaned')


# In[12]:


plt.show()


# In[2]:


# another way of identify outliers with scatter plots 
# fake up data
from pylab import *
spread = rand(50) * 100
center = ones(25) * 50
flier_high = rand(10) * 100 + 100
# numpy.array multiply -100 for each element
flier_low = rand(10) * -100
boxplot(data, 0, 'gx')


# In[ ]:





# In[10]:




