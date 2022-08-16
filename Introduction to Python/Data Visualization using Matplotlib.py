#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np

# importing matplotlib
import matplotlib.pyplot as plt

# display plots in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')

# drop null values
data_BM = data_BM.dropna(how='any')

# view top results
data_BM.head()


# # line chart

# In[2]:


# getting mean price per item
price_by_item = data_BM.groupby('Item_Type').Item_MRP.mean()[:10]
price_by_item


# In[10]:


# mean price based on item type
price_by_item = data_BM.groupby('Item_Type').Item_MRP.mean()[:10]

x = price_by_item.index.tolist()
y = price_by_item.values.tolist()

# set figure size
plt.figure(figsize=(14, 8))

# set title
plt.title('Mean price for each item type')

# set axis labels
plt.xlabel('Item Type')
plt.ylabel('Mean Price')

# set xticks
plt.xticks(labels=x, ticks=np.arange(len(x)))

plt.plot(x,y)


# # barchart

# In[12]:


# sales by outlet size
sales_by_outlet_size = data_BM.groupby('Outlet_Size').Item_Outlet_Sales.mean()

# sort by sales
sales_by_outlet_size.sort_values(inplace=True)

x = sales_by_outlet_size.index.tolist()
y = sales_by_outlet_size.values.tolist()

# set axis labels
plt.xlabel('Outlet Size')
plt.ylabel('Sales')

#set title
plt.title('Mean sales for each outlet size')

#set xticks
plt.xticks(labels=x, ticks=np.arange(len(x)))

plt.bar(x, y, color=['red', 'orange', 'magenta'])


# # histogram

# In[13]:


# title
plt.title('Item MRP (price) distribution')

# xlabel 
plt.xlabel('Item_MRP')

# ylabel
plt.ylabel('Frequency')

# plot histogram
plt.hist(data_BM['Item_MRP'], bins=20, color='lightblue');


# # boxplots

# In[14]:


data = data_BM[['Item_Outlet_Sales']]

# create outlier point shape
red_diamond = dict(markerfacecolor='r', marker='D')

# set title
plt.title('Item Sales distribution')

# make the boxplot

plt.boxplot(data.values, labels=['Item Sales'], flierprops=red_diamond);


# In[15]:


#multiple box plots

data = data_BM[['Item_Weight', 'Item_MRP']]

# create outlier point shape
red_diamond = dict(markerfacecolor='r', marker='D')

# generate subplots
fig, ax = plt.subplots()

# make the boxplot
plt.boxplot(data.values, labels =['Item_Weight', 'Item_MRP']);


# # violine plot

# In[16]:


data = data_BM[['Item_Weight', 'Item_MRP']]

# generate subplots
fig, ax = plt.subplots()

# add labels to x axis
plt.xticks(ticks=[1,2], labels=['Item_Weight', 'Item_MRP'])

# make the violinplot
plt.violinplot(data.values);


# # scatter plots

# In[17]:


# set label of axes
plt.xlabel('Item_Weight')
plt.ylabel('Item_Visibility')

# plt
plt.scatter(data_BM["Item_Weight"][:200], data_BM["Item_Visibility"][:200])


# # bubble plots

# In[25]:


# set label of axes
plt.xlabel('Item_MRP')
plt.ylabel('Item_Outlet_Sales')

# set title
plt.title('Item Outlet Sales vs Item MRP (price)')

# plot
plt.scatter(data_BM["Item_MRP"][:100], data_BM["Item_Outlet_Sales"][:100], s=data_BM["Item_Visibility"][:100]*1000,c='red')


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




