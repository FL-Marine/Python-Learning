#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation with Pandas

# In[3]:


import pandas as pd
import numpy as np

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')

# drop null values
data_BM = data_BM.dropna(how='any')

# view top results
data_BM.head()


# # Sorting dataframes

# In[6]:


# sort by year
sorted_data = data_BM.sort_values(by='Outlet_Establishment_Year')

# print sorted data
sorted_data[:5]


# In[7]:


# sort in place and descending order
data_BM.sort_values(by='Outlet_Establishment_Year', ascending=False, inplace=True)
data_BM[:5]
#inplace means relfect changes in original dataframe


# In[8]:


# reloading original dataframe to do the next set of code

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')

# drop null values
data_BM = data_BM.dropna(how='any')

# sort by multiple columns
data_BM.sort_values(by=['Outlet_Establishment_Year','Item_Outlet_Sales'], ascending=False)[:5]


# In[9]:


# changed the order of columns
data_BM.sort_values(by=['Item_Outlet_Sales', 'Outlet_Establishment_Year'], ascending=False, inplace=True)
data_BM[:5]


# In[10]:


# sort by index

data_BM.sort_index(inplace=True)
data_BM[:5]


# # Merging Dataframes

# In[10]:


import pandas as pd
import numpy as np


# cerate dummy data

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                      index=[0, 1, 2, 3])



df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                         'B': ['B4', 'B5', 'B6', 'B7'],
                         'C': ['C4', 'C5', 'C6', 'C7'],
                         'D': ['D4', 'D5', 'D6', 'D7']},
                      index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                         'B': ['B8', 'B9', 'B10', 'B11'],
                         'C': ['C8', 'C9', 'C10', 'C11'],
                         'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
   


# In[11]:


# combine datasets
result = pd.concat([df1, df2, df3])
result


# ## concat is like union dataframes on top or the side

# In[12]:


# combine dataframes
result = pd.concat([df1, df2, df3], keys =['x', 'y', 'z'])
result
# this represents which result came from which dataframe


# In[13]:


# get second dataframe
result.loc['y']


# In[15]:


#outer join
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                            'D': ['D2', 'D3', 'D6', 'D7'],
                            'F': ['F2', 'F3', 'F6', 'F7']},
                           index=[2, 3, 6, 7])
result = pd.concat([df1, df4], axis=1, sort=False)
result


# In[16]:


# inner join

result = pd.concat([df1, df4], axis=1, join='inner')
result


# ## merge in python is like joining dataframes based on common values

# In[19]:


df_a = pd.DataFrame({
            'subject_id': ['1', '2', '3', '4', '5'],
            'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
            'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']})
    
df_b = pd.DataFrame({
            'subject_id': ['4', '5', '6', '7', '8'],
            'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
            'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']})

df_c = pd.DataFrame({
            'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
            'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]})


# In[20]:


# merging(joining) 1st and 3rd data frame
pd.merge(df_a, df_c, on='subject_id')


# In[21]:


# merge outer join
pd.merge(df_a, df_b, on='subject_id', how='outer')
# subject 1,2,3 are not in dataframe which is why there are NA's
# 5,6,7 are the same result not in first dataframe


# In[22]:


# merge inner join
pd.merge(df_a, df_b, on ='subject_id', how='inner')


# In[23]:


# merge right join
pd.merge(df_a, df_b, on='subject_id', how ='right')


# In[24]:


# merge left join
pd.merge(df_a, df_b, on='subject_id', how ='left')


# # Apply function 

# In[26]:


import pandas as pd
import numpy as np

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')


# In[33]:


# accessing row wise
data_BM.apply(lambda x: x)


# In[34]:


# access first row
data_BM.apply(lambda x: x[0])


# In[35]:


# access first column by index
data_BM.apply(lambda x: x[0], axis=1)


# In[36]:


# access by column name
data_BM.apply(lambda x: x["Item_Fat_Content"], axis=1)


# In[37]:


# before clipping
data_BM["Item_MRP"][:5]


# In[39]:


# clip price if greater than 200, clipping means lower price here to 200
def clip_price(price):
    if price > 200:
        price= 200
    return price
# after clipping 
data_BM["Item_MRP"].apply(lambda x: clip_price(x))[:5]


# In[40]:


# label encode outlet locations
def label_encode(city):
    if city == 'Tier 1' :
        label = 0
    elif city == 'Tier 2':
        label = 1
    else:
        label = 2
    return label
# Changing city tiers from Tier 1, 2 to 1 and 2


# In[41]:


# before label encoding
data_BM["Outlet_Location_Type"][:5]


# In[42]:


def label_encode(city):
    if city == 'Tier 1' :
        label = 0
    elif city == 'Tier 2':
        label = 1
    else:
        label = 2
    return label
# operate label_encode on every row of Outlet_Location_Type
data_BM["Outlet_Location_Type"] = data_BM["Outlet_Location_Type"].apply(label_encode)


# In[43]:


# after lebel encoding
data_BM["Outlet_Location_Type"][:5]


# # Aggregating Data

# In[48]:


import pandas as pd
import numpy as np

# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')

# drop null values
data_BM = data_BM.dropna(how='any')

#reset index after dropping
data_BM = data_BM.reset_index(drop=True)

# view top results
data_BM.head()


# ## Aggregating Data

# In[51]:


# group price based on item type
price_by_item = data_BM.groupby('Item_Type')

# display first few roes
price_by_item.first()


# In[52]:


# mean price by item
price_by_item.Item_MRP.mean()


# In[53]:


# group on multiple colums
multiple_groups = data_BM[:10].groupby(['Item_Type', 'Item_Fat_Content'])
multiple_groups.first()


# In[54]:


# generate crosstab of outlet size and outlet location type
pd.crosstab(data_BM["Outlet_Size"], data_BM["Outlet_Location_Type"], margins=True)


# In[55]:


# create pivot table
pd.pivot_table(data_BM, index=['Outlet_Establishment_Year'], values= "Item_Outlet_Sales")


# In[56]:


# create pivot table
pd.pivot_table(data_BM, index=['Outlet_Establishment_Year', 'Outlet_Location_Type', 'Outlet_Size'], values= "Item_Outlet_Sales")


# In[57]:


# summary stats
pd.pivot_table(data_BM, index=['Outlet_Establishment_Year', 'Outlet_Location_Type', 'Outlet_Size'], values= "Item_Outlet_Sales", aggfunc= [np.mean, np.median, min, max, np.std])


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




