#!/usr/bin/env python
# coding: utf-8

# # 7 Ways to Loop Through a List in Python
# 
# - Link https://learnpython.com/blog/python-list-loop/#:~:text=%207%20Ways%20to%20Loop%20Through%20a%20List,range%20%28%29...%204%20The%20NumPy%20Library%20More%20
# 

# - Lists are one of the 6 fundamental data types in Python
# - Lists can store multiple elements in a single variable
# - Can have multiple data types 
# - Lists (like arrays in other langugaes) can be nested lists within lists
# 

# # 1. A Simple for Loop
# 
# - **for** loop is one of the simplest methods for iterating over a list or any other sequence (e.g. TUPLES, SETS, OR DICTIONARIES).
# 
# - Python Loop Link: https://learnpython.com/blog/write-for-loop-python/

# In[2]:


fruits = ["Apple", "Mango", "Banana", "Peach"]
for fruit in fruits:
    print(fruit)
# the for loop has printed each of the list items
# loop has called the print() function four times, each time printing the current item in the list – i.e. the name of a fruit.


# In[3]:


bjj = ["RNC", "Triangle", "Kimura", "Guillotine"]
for moves in bjj:
    print(moves)


# # 2. List Comprehension
# 
# - list comprehension is similar to for loop but allows to create list in single line.
# 
# - Lists Article: https://learnpython.com/blog/python-lists-list-comprehension-new-year-resolutions/
# 

# In[6]:


fruits = ["Apple", "Mango", "Banana", "Peach"]
[print(fruit + " juice") for fruit in fruits]
# for..in is encliosed with print() inside of [square brackets]
# this is what makes a list comprehension


# In[1]:


bjj = ["RNC", "Triangle", "Kimura", "Guillotine"]
[print(move + " submission") for move in bjj]


# # 3. A for Loop with range()
# 
# - range() generates a sequence of integers from the provided starting and stopping indexes.
# 
# - An index refers to the position of elements in a list.
# 
# - The first item has an index of 0, the second list item is 1, and so on.

# In[ ]:


# syntax range function

range(start, stop, step)

# start and step arguments are optional
# only the stop argument is required
# step determines if you skip list items, default is 1 meaning no items is skipped
# If you only specify one parameter (i.e. the stop index), the function constructs a range object containing all elements from 0 to stop-1.


# In[3]:


fruits = ["Apple", "Mango", "Banana", "Peach"]
 
# Constructs range object containing elements from 0 to 3
for i in range(len(fruits)):
  print("The list at index", i, "contains a", fruits[i])


# In[14]:


fruits = ["Apple", "Mango", "Banana", "Peach"]
 
# Constructs range object containing only 1 and 2
for i in range(1, 3):
  print(fruits[i])
# index 3 is stopping point and index goes 


# # 4. A for Loop with enumerate()
# 
# - enumerate() shows the index of the element I am accessing

# In[15]:


fruits = ["Apple", "Mango", "Banana", "Peach"]
 
for index, element in enumerate(fruits):
  print(index, ":", element)


# # 5. A for Loop with lambda
# 
# - lambda function is an anonymous function in which a mathematical expression is evaluated and then returned.
# 

# In[1]:


lst1 = [1, 2, 3, 4, 5]
lst2 = []
  
# Lambda function to square number
temp = lambda i:i**2
 
for i in lst1:
 
    # Add to lst2
    lst2.append(temp(i))
   
print(lst2)


# In[4]:


lst1 = [1, 2, 3, 4, 5]
   
lst1 = list(map(lambda v: v ** 2, lst1))
   
print(lst1)
# map() produces a map object (which is an iterator) of the results


# # 6. A while Loop
# 
# - while loop executes until a certain condition is met
# 
# - the while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# 
# - In the code below, that condition is the length of the list; the i counter is set to zero, then it adds 1 every time the loop prints one item in the list. When i becomes greater than the number of items in the list, the while loop terminates.
# 
# - code ensures that the condition i < len(fruits) will be satisfied after a certain number of iterations.

# In[7]:


fruits = ["Apple", "Mango",  "Banana", "Peach"]
 
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1


# # 7. The NumPy Library
# 
# - NumPy is the best way to loop through big lists.
# 
# - NumPy reduces the overhead by making iteration more efficient. This is done by converting the lists into NumPy ARRAYS. 

# In[8]:


import numpy as np
 
nums = np.array([1, 2, 3, 4, 5])
 
for num in nums:
  print(num)


# In[ ]:




