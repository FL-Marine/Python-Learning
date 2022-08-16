#!/usr/bin/env python
# coding: utf-8

# ### Basics of Python
# 
# Fill valid code/values in place of blanks. 
# Demo
# initialize variable 'msg' with the string 'Hello World'
msg = _____

# Solution
msg = "Hello World"
# In[1]:


# initialize variables 'a' and 'b' with 5 and 6 respectively
a = 5 
b = 6

# add 'a' and 'b' and assign the result into a new variable 'c'
c = 5 + 6
print(c)


# In[3]:


# build a function to add 2 numbers
def addition(x,y):
    return(x + y)

# use the function 'addition' to add 'a' and 'b'
addition(a,b)


# In[4]:


# create a list consisting of first 5 even numbers and print the list
my_list = [2,4,6,8,10]
print(my_list)


# In[5]:


# access the 3rd element of the list 'my_list'
my_list[2]


# In[6]:


# given below is a dictionary having 4 unique keys, i.e., 'name', 'age', 'gender', 'is_employed'
my_dict = {'name':'Smith',
           'age':34,
           'gender': 'Male',
           'is_employed': False}

# print 'my_dict'
print(my_dict)


# In[7]:


# access value under 'name' key from 'my_dict'
my_dict['name']


# In[ ]:


# update 'is_employed' key to True
my_dict.update({'is_employed': _____})

# print the updated dictionary
print(my_dict)


# In[ ]:


# use a for loop to print only even numbers from the first 20 numbers, i.e. 1-20
for i in range(1,21):
    if i % 2 == 0:
        print(_____)


# ### Please download the file "data_python.csv".

# In[ ]:


# import required libraries
import pandas as pd
import numpy as np


# In[ ]:


## read data_python.csv using pandas
mydata = pd._____("data_python.csv")


# In[ ]:


## print the number of rows and number of columns of mydata
mydata._____


# In[ ]:


## assign a variable 'target' with the 'Loan_Status' feature from mydata dataframe
target = mydata[_____]


# In[ ]:


## print the datatype of ApplicantIncome feature
print(mydata['ApplicantIncome']._____)


# In[ ]:


## conditional statement - print 'Yes' if the 21st element of 'Education' feature is 'Graduate' else print 'No'
if(mydata['Education'][20] == 'Graduate'):
    print(_____)
else:
    print(_____)   


# In[ ]:


## print 31st to 35th rows of mydata
mydata.iloc[_____:_____]


# In[ ]:


## print first 5 rows of 2nd and 3rd column only
mydata.iloc[:_____,_____:_____]

