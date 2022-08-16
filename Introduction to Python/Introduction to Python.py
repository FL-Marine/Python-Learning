#!/usr/bin/env python
# coding: utf-8

# # Arithmetic Operators
# 

# In[1]:


#Addition
3 + 5


# In[2]:


# Subtraction 

54 - 46


# In[3]:


# Multiplication

2 * 3


# In[4]:


# Division

35 / 7


# # Comparision Operators

# In[5]:


# greater than

45 >34


# In[6]:


# less than

56 < 23


# In[7]:


34 * 34 < 45*23


# In[8]:


45 == 45


# # Logical Operators

# In[9]:


# and operator

0 and 3


# In[10]:


3 and 0


# In[11]:


3 and 5


# In[12]:


# or operator

0 or 3


# In[13]:


3 or 5


# # How variables work in Python

# In[14]:


a = 5


# In[15]:


print(a)


# In[16]:


A = 4


# In[18]:


print(a)
print(A)


# In[20]:


a = 7
b = a
a = 3


# In[21]:


print(a)


# In[22]:


print(7)


# # Variable naming rules

# In[24]:


a = 5


# In[25]:


_a =5


# In[26]:


@a=5


# # Data Types

# In[27]:


a =5


# In[28]:


type(a)


# In[29]:


b="abe"


# In[30]:


type(b)


# # Implementing Conditional Statements in Python

# In[32]:


# Problem 1: take a variable x and print "Even" if the number is divisible by 2, otherwise print "Odd."

x=4

if(x%2==0):
    print("Even")
else:
    print("Odd")


# In[6]:


# Problem 2: Take a variable y and print "Grade A" if y is greater than 90, "Grade B" if y is greather than 60 but less than or equal to 90 and "Grade F" otherwise.

y=90

if(y>90):
    print("Grade A")
elif(y>60):
    print("Grade B")
else:
    print("Grade F")


# # Understanding Looping Constructs

# In[4]:


# problem 1: Write a for loop to print all the numbers between 10 and 50
for i in range(11,50):
    print(i)


# In[6]:


# problem 2: write a for loop to print all the odd numbers between 10 and 50

for i in range(11,50,2):
    print(i)


# # Understanding Functions

# In[2]:


#creating user define function

def area_circle(radius):
    area = 3.14*r*r
    return area


# In[2]:


# problem: create a function that takes two numbers as argument and returns the greaer of the two

def compare(a,b):
    if(a>b):
        greater=a
    else:
        greater=b
    return greater


# In[3]:


compare(10,50)


# In[4]:


compare(14,5)


# In[1]:


def min(a,b):
    if(a>b):
        return b
    elif (a==b):
        return 'The numbers are equal'
    else:
        return a


# In[2]:


min(200,400)


# # Creating a list

# In[3]:


# creating a list

marks=[1,2,3,4,5,6,7,8,9,10]


# In[4]:


marks


# In[5]:


marks[5]


# In[6]:


marks[0:6]


# In[7]:


# adding an element

marks.append(11)


# In[8]:


marks


# In[9]:


marks.extend([12,13])


# In[10]:


marks


# In[11]:


marks.append([14,15])


# In[12]:


marks


# In[13]:


# deleting elements

marks.remove([14,15])


# In[14]:


marks


# In[15]:


del marks[0]


# In[16]:


marks


# In[17]:


# accessing list elements 
for mark in marks:
    print(mark)


# In[18]:


for mark in marks:
    print(mark+1)


# # Implementing Dictionaries in Python

# In[19]:


# creating a dictionary

marks = {'history':45,'Geography':54,'Hindi':56}


# In[20]:


marks


# In[21]:


# acess elements

marks["Geography"]


# In[22]:


# adding elements

marks['english'] = 47


# In[23]:


marks


# In[24]:


marks.update({'Chemistry':89,'Physics':98})


# In[25]:


marks


# In[26]:


# delete element

del marks['Hindi']


# In[27]:


marks


# # Reading csv and excel

# In[45]:


# importing pandas library

import pandas as pd


# In[46]:


# reading csv file

df=pd.read_csv("data.csv")


# In[47]:


df.head()


# # Reading dataframes and conduct basic operations in Python

# In[48]:


# seeing the dimensions of the df dataframe

df.shape


# In[49]:


# top 5 rows

df.head()


# In[50]:


# bottom 5 rows

df.tail()


# In[51]:


# seeing column names in df

df.columns


# In[52]:


# select single column

df['Pclass']


# In[53]:


# selecting multiple columns

df[['Pclass', 'Cabin']]


# In[54]:


# select single column by name

df["Pclass"]


# In[55]:


df[['Survived', 'Embarked']]


# In[56]:


# selecting rows by positions

df.iloc[:5]


# In[57]:


# selecting columns by position

df.iloc[:,:2]


# In[58]:


#subsetting data by plcass

df[df['Pclass']==1]


# In[59]:


# reading csv file

df_index=pd.read_csv("index.csv")


# In[60]:


df_index.head()


# In[61]:


# access the 3rd column of the index dataframe

df_index['C']


# In[70]:


# access last two columns of the index dataframe using iloc function

df_index.iloc[:,-2:]


# In[74]:


#access last 10 rows and first two columns

df_index.iloc[-10:, 0:2]


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




