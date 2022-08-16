#!/usr/bin/env python
# coding: utf-8

# ### Basics of Python

# In[ ]:


# initialize variables 'a' and 'b' with 5 and 6 respectively
a = 5
b = 6

# add 'a' and 'b' and assign the result into a new variable 'c'
c = a+b
print(c)


# In[ ]:


# build a function to add 2 numbers
def addition(x,y):
    return(x+y)

# use the function 'addition' to add 'a' and 'b'
addition(a,b)


# In[ ]:


# create a list consisting of first 5 even numbers and print it
my_list = [2,4,6,8,10]
print(my_list)


# In[ ]:


# access the 3rd element of the list 'my_list'
my_list[2]


# In[ ]:


# given below is a dictionary having 4 unique keys, i.e., 'name', 'age', 'gender', 'is_employed'
my_dict = {'name':'Smith',
           'age':34,
           'gender': 'Male',
           'is_employed': False}

# print 'my_dict'
print(my_dict)


# In[ ]:


# access name 'my_dict'
my_dict['name']


# In[ ]:


# update 'is_employed' key to True
my_dict.update({'is_employed':True})

# print the updated dictionary
print(my_dict)


# In[ ]:


# use a for loop to print only even numbers from the first 20 numbers, i.e. 1-20
for i in range(1,21):
    if i % 2 == 0:
        print(i)


# ### Please download the file "data_python.csv".

# In[ ]:


# load required libraries
import pandas as pd
import numpy as np


# In[ ]:


## read data_python.csv using pandas
## start code
mydata = pd.read_csv("data_python.csv")
## end code


# In[ ]:


## print the number of rows and number of columns of mydata
## start code
mydata.shape
## end code


# In[ ]:


## assign a variable 'target' with the 'Loan_Status' feature from mydata dataframe
## start code
target = mydata['Loan_Status']
## end code


# In[ ]:


## print the datatype of ApplicantIncome feature
## start code
print(mydata['ApplicantIncome'].dtype)
## end code


# In[ ]:


## conditional statement - print 'Yes' if the 21st element of 'Education' feature is 'Graduate' else print 'No'
if(mydata['Education'][20] == 'Graduate'):
    ## start code
    print('Yes')
    ## end code
else:
    ## start code
    print('No')
    ## end code


# In[ ]:


## print 31st to 35th rows of mydata
## start code
mydata.iloc[30:35]
## end code


# In[ ]:


## print first 5 rows of 2nd and 3rd column only
## start code
mydata.iloc[:5,1:3]
## end code

