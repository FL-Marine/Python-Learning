#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing required libraries
import numpy as np
import pandas as pd

# importing matplotlib
import matplotlib.pyplot as plt

# display plots in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Matplot lib basics

# In[2]:


#basic chart
height = [150, 160, 165, 185]
weight = [70, 80, 90, 100]

# draw the plot
plt.plot(height, weight)


# ### Customize the plot 

# In[3]:


# draw the plot
plt.plot(height, weight)

# add title
plt.title("Relationship between height and weight")

# label x axis
plt.xlabel("Height")

# label y axix
plt.ylabel("Weight")


# In[4]:


calories_burnt = [65, 75, 95, 99]

# draw the plot for calories burnt
plt.plot(calories_burnt)

# draw the plot for weight
plt.plot(weight)


# In[5]:


# add legends

# drae the plot for calories burnt
plt.plot(calories_burnt)

# draw the plot for weight
plt.plot(weight)

# add legend in the lower right part of the figure
 plt.legend(labels=['Calories Burnt', 'Weight'], loc = 'lower right')


# In[7]:


# adding labels for tick marks

# draw the plot for calories burnt and weight
plt.plot(calories_burnt)
plt.plot(weight)

# add legend in the lower right part of the figure
plt.legend(labels=['Calories Burnt', 'Weight'], loc = 'lower right')

# set labels for each of these persons
plt.xticks(ticks=[0,1,2,3], labels = ['p1', 'p2', 'p3', 'p4']);


# In[9]:


# figure size in inches
plt.figure(figsize=(15,5))

# draw the plot for calories burnt and weight
plt.plot(calories_burnt)
plt.plot(weight)

# add legend in the lower right part of the figure
plt.legend(labels=['Calories Burnt', 'Weight'], loc = 'lower right')

# set labels for each of these persons
plt.xticks(ticks=[0,1,2,3], labels = ['p1', 'p2', 'p3', 'p4']);


# In[11]:


# draw the plot for calories burnt and weight
plt.plot(calories_burnt, 'go')
plt.plot(weight, 'y--')

# add legend in the lower right part of the figure
plt.legend(labels=['Calories Burnt', 'Weight'], loc = 'lower right')

# set labels for each of these persons
plt.xticks(ticks=[0,1,2,3], labels = ['p1', 'p2', 'p3', 'p4']);


# ## subplots

# In[12]:


# create 2 plots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6,6))

# plot on 0 row and 0 column
ax[0,0].plot(calories_burnt, 'go')

# plot on 0 row and 1 column
ax[0,1].plot(weight)

# set titeles for subplots
ax[0,0].set_title("Calories Burnt")
ax[0,1].set_title("Weight")

# set ticks for each of these person
ax[0,0].set_xticks(ticks=[0,1,2,3]);
ax[0,1].set_xticks(ticks=[0,1,2,3]);

# set labes for each of these persons
ax[0,0].set_xticklabels(labels=['p1', 'p2', 'p3', 'p4']);
ax[0,1].set_xticklabels(labels=['p1', 'p2', 'p3', 'p4']);


# In[13]:


# same as code above just using sharey=True to have same y axis

# create 2 plots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6,6), sharey=True)

# plot on 0 row and 0 column
ax[0,0].plot(calories_burnt, 'go')

# plot on 0 row and 1 column
ax[0,1].plot(weight)

# set titeles for subplots
ax[0,0].set_title("Calories Burnt")
ax[0,1].set_title("Weight")

# set ticks for each of these person
ax[0,0].set_xticks(ticks=[0,1,2,3]);
ax[0,1].set_xticks(ticks=[0,1,2,3]);

# set labes for each of these persons
ax[0,0].set_xticklabels(labels=['p1', 'p2', 'p3', 'p4']);
ax[0,1].set_xticklabels(labels=['p1', 'p2', 'p3', 'p4']);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




