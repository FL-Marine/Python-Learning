#!/usr/bin/env python
# coding: utf-8

# # Visualization With Seaborn

# In[1]:


# importing required libraries
import seaborn as sns
sns.set()
sns.set(style="darkgrid")

import numpy as np
import pandas as pd

# importing matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings("ignore")


# ## Loading dataset

# In[4]:


# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')

# drop the null values
data_BM = data_BM.dropna(how="any")

# multiply Item Visibility by 100 to increase size
data_BM["Visibility_Scaled"] = data_BM["Item_Visibility"] * 100

# View the top results
data_BM.head()


# ## 1. Creating basic plots

# In[5]:


# line plit using lineplot()
sns.lineplot(x="Item_Weight", y="Item_MRP", data=data_BM[:50])


# In[6]:


# bar chart
sns.barplot(x="Item_Type", y="Item_MRP", data=data_BM[:5])


# In[8]:


# histogram
sns.distplot(data_BM['Item_MRP'])


# In[16]:


# boxplot
sns.boxplot(data_BM['Item_Outlet_Sales'], orient='vertical')
#this should be vertical? change orient to horizontal and it should be like what is shown


# In[20]:


# violin plot
sns.violinplot(data_BM['Item_Outlet_Sales'], orient='vertical', color ='magenta')


# In[19]:


# scatter plot
sns.relplot(x="Item_MRP", y="Item_Outlet_Sales", data=data_BM[:200], kind="scatter");


# ### Hue semantic
# 
# Adds another dimension to the plot by coloring the points according to a 3rd variable.

# In[21]:


sns.relplot(x="Item_MRP", y="Item_Outlet_Sales", hue="Item_Type", data=data_BM[:200]);


# In[22]:


# line plot using hue semantic
sns.lineplot(x="Item_Weight", y="Item_MRP", hue='Outlet_Size', data=data_BM[:150]);


# In[23]:


# bubble plot
sns.relplot(x="Item_MRP", y="Item_Outlet_Sales", data=data_BM[:200], kind="scatter", size="Visibility_Scaled", hue="Visibility_Scaled")


# In[24]:


# category wise scatter plot
sns.relplot(x="Item_Weight", y="Item_Visibility", hue="Outlet_Size", style="Outlet_Size", col="Outlet_Size", data=data_BM[:100])


# ## 2. Advance categorical plots in seaborn
# 
# 3 categorical variables in seaborn
# 
# - cateogrical scatterplots:
#     - stripplot() (with kind="strip": the default)
#     - swarmplot() (with kind="swarm")
# - Categorical distribution plots:
#     -  boxplot() (with kind="box")
#     - violinplot() (with kind="violin")
# - Categorical estimate plots:
#     - barplot() (with kind="bar")

# ### a. Categorical scatterplots

# In[29]:


# strip plot
# draws a sctterplot where one variable is categorical, other is continous
# create this by passing kind=strip in the catplot()

sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='strip',data=data_BM[:250]);


# In[30]:


# swarmplot
# simialr to stripplot() but points are adjusted (only along the categorical axis) so they don't overlap

sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='swarm' ,data=data_BM[:250]);


# ### Categorical distribution plots

# In[31]:


# boxplot

sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='box' ,data=data_BM)


# In[33]:


# violin plot
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='violin' ,data=data_BM)


# In[34]:


# barplot

sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='bar' ,data=data_BM)


# ## 3. Density plots

# In[35]:


# distribution of Item Visibility
plt.figure(figsize=(7,7))
sns.kdeplot(data_BM['Item_Visibility'], shade=True)

# rather then histogram this plot uses a kernel density estimation which seaborn does with sns.kdeplot


# In[36]:


# distribution of Item MRP
plt.figure(figsize=(7,7))
sns.kdeplot(data_BM['Item_MRP'], shade=True)


# ### Histogram and Density Plot

# In[38]:


# histograms and KDE can be comnined using distplot
plt.figure(figsize=(7,7))
sns.distplot(data_BM['Item_Outlet_Sales'])


# ## Pair plots
# 
# Are usefeul when exploring correlations between multidimensional data, when you like to plot all pairs of value against each other
# 

# In[39]:


iris = sns.load_dataset("iris")
iris.head()


# In[40]:


sns.pairplot(iris, hue='species', height=2.5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




