
# coding: utf-8

# In[7]:





# In[38]:


from matplotlib import style
style.use('ggplot')
plt.plot([1,2,3,2,3,2,2,1])
plt.plot([4,3,2,1],[1,2,3,4])
plt.show()


# In[24]:


print(plt.style.available)


# In[43]:


x = [1,2,3,4]
y = [5,4,3,2]
plt.figure()
# devide subplots into 2 * 3 grid
plt.subplot(231)
plt.plot(x,y)

plt.subplot(232)
plt.bar(x,y)

plt.subplot(233)
# horizontal bar-charts
plt.barh(x,y)

plt.subplot(234)
y1 = [7,8,5,4]
plt.bar(x, y1, bottom=y, color='r')

plt.subplot(235)
plt.boxplot(x)

plt.subplot(236)
plt.scatter(x,y)

plt.show()


# In[47]:


# usage of boxplot
dataset = [113,115,119,121,124,
           124,125,126,126,126,
           127,127,128,129,130,
           130,131,132,133,136]
"""
boxplot contains:
    minimum value
    second quartile
    median value
    third quartile
    maximum value
"""
plt.subplot(121)
plt.boxplot(dataset, vert=False)

plt.subplot(122)
# hist shows the frequency for different distinct value in dataset
plt.hist(dataset)

plt.show()


# In[87]:


# sine and cosine
import numpy as np
# endpoint set to True means inclusive 
x = np.linspace(-np.pi, np.pi, num=256, endpoint=True)

y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()




# In[92]:


# centering the spine
plt.plot(x,y1)
# get current axis
ax = plt.gca()

# hide two spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# move bottom and left spine to 0,0
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# move ticks positions
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.show()


# In[83]:


# legend
x1 = np.random.normal(30, 3, 100)
x2 = np.random.normal(20, 2, 100)
x3 = np.random.normal(10, 3, 100)
style.use('classic')
plt.plot(x1, label='plot')
plt.plot(x2, label='2nd plot')
plt.plot(x3, label='last plot')
# draw legend with a bounding box start from position (0., 1.02) having width 1. and height 1.02
# borderaxespad defines the padding
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
# starting position of the text is defined by xytext, second argument is the target important point
plt.annotate("Important value", (55, 0), xycoords='data', xytext=(40, 38), arrowprops=dict(arrowstyle='->'))
plt.show()


# In[ ]:





# In[ ]:




