#!/usr/bin/env python
# coding: utf-8

# # Extracomg Information Using Regular Expressions (RegEx)
# 
# **r** expression is used to create a raw string. Python raw string treats backslash(\) as a literal character.

# In[1]:


# normal string vs raw string
path = "C:\desktop\nathan" #string
print("string:",path)


# In[2]:


path = r"C:\desktop\nathan" # raw string
print("raw string:",path)


# It is always recommended to use raw strings while dealing with regex
# 
# Python has built-in module to work with regex called **re**.
# 
# Commonly used methods:
#     1. re.match()
#     2. re.search()
#     3. re.findall()

# In[3]:


#  1. re.match()
# returns a match object on success and none on failure

import re

# match a word at the beginning of a string

result = re.match('Analytics', r'Analytics Vidhya is the largest data science community of India')
print(result)

result_2 = re.match('largest', r'Analytics Vidhya is the largest data science community of India')
print(result_2)


# In[4]:


# since output of re.match is an object must use grounp() function to get the matched expression
print(result.group())


# In[5]:


# 2. re.search()
# matches the single occurence of a pattern in the entire string

# search for the pattern "founded" in a given string
result = re.search('founded', r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(result.group())


# In[8]:


#  3. re.findall()
# returns all the occureneces of the pattern from the string. always recommended to use re.findal() always as it can work
# both re.search() and re.match()

result = re.findall('founded', r'Andrew NG founded Coursera. He also founded deeplearning.ai')
print(result)


# ## Special sequences 
# 
# These are used to extract different kinds of information from a given text.
# 

# In[13]:


# 1. \b returns a match where the specified pattern is at the end of a word

str = r'Analytics Vidhya is the largest Analytics Community in India'

# check if there is any word that ends with "est"
x=re.findall(r"est\b",str)
print(x)


# In[16]:


# 2. \d returns a match where string contains digits(numbers from 0-9)

str = "2 million monthly visits in Jan'19."

# check if string contains any digits (numbers from 0-9):
x = re.findall("\d", str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
    print("No Match")
# need to comnbine 1,9 into 19


# In[17]:


str = "2 million monthly visits in Jan'19."

# check if string contains any digits (numbers from 0-9):
# adding '+' sign after'\d' will continue to extract digits until it encounters a space
x = re.findall("\d+", str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
    print("No Match")


# In[18]:


# 3. \D returns a match where the string does not contain any digit

str = "2 million monthly visits in Jan'19."

# check if string contains any digits (numbers from 0-9):
x = re.findall("\D", str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
    print("No Match")
# need to put all of the output together


# In[23]:


str = "2 million monthly visits'19"

# check if string contains any digits (numbers from 0-9):
x = re.findall("\D+", str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
    print("No Match")


# In[ ]:


# 4. \w helps in extraction of alphanumeric characters only (characters from a to Z, digits from 0-9, 
# and the underscore_character)


# In[24]:


str = "2 million monthly_visits!"

# returns a match at every word character (characters from a to Z, digits from 0-9, and the underscore_character)
x = re.findall("\w",str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
    print("No Match")
# add a + sigh to bring letters together


# In[25]:


str = "2 million monthly_visits!"

# returns a match at every word character (characters from a to Z, digits from 0-9, and the underscore_character)
x = re.findall("\w+",str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
     print("No Match")


# In[26]:


# 5. \W returns a match at every non alphanumeric character

str = "2 million monthly visits9!"

# returns a match at every NON word character (character NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W",str)

print(x)

if(x):
    print("Yes, there at least once match!")
else:
     print("No Match")


# # Metacharacters
# 
# Are characters with special meaning

# In[28]:


# 1. (.) matches any character (except newline character)

str = "rohan and rohit recently published a research paper!"

# search for a string that starts with "ro", followed by a certain number of characters

x = re.findall("ro.", str)
x2 = re.findall("ro...", str)

print(x)
print(x2)


# In[29]:


# 2 (^) starts with given pattern

str = "Data Science"

# Check if the string starts with 'Data':
x = re.findall("^Data", str)

if (x):
    print("Yes, the string starts with 'Data'")
else:
    print("No Match")


# In[32]:


# try with different string

str2 = "Big Data"

# Check if the string starts with 'Data':
x2 = re.findall("^Big", str2)

if(x2):
    print("Yes, the string starts with 'data'")
else:
    print("No match")
print(x2)


# In[34]:


# 3. ($) string ends with given pattern

str = "Data Science"

# Check if the string ends with 'Science':

x = re.findall("Science$", str)

if(x):
    print("Yes, the string starts with 'Science'")
else:
    print("No match")
print(x)


# In[36]:


# 4. (*) matches for zero or more occurences of the pattern to the left of it
str = "easy easssy eay ey"

# Check if the string contains "ea" following by 0 or more "s" characters ending with y
x = re.findall("eas*y", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[37]:


# 5. (+) matches one or more occureces of the pattern to the left of it

str = "easy easssy eay ey"

# Check if the string contains "ea" following by 1 or more "s" characters ending with y
x = re.findall("eas+y", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[38]:


# 6. (?) matches zero or once occurence of the pattern to the left of it

str = "easy easssy eay ey"

x = re.findall("eas?y", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[40]:


# 7. "|" pipe operation either or

str = 'Analytics Vidhya is the largest Analytics Community in India'

# check if the string contains either "data or India":

x = re.findall("data|India", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[42]:


# try with different string

str = 'Analytics Vidhya is the largest data science communitites'

# check if the string contains either "data or India":

x = re.findall("data|India", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# # Set
# A set is a bunch of characters inside a pair of square brackets[].

# In[45]:


str = 'Analytics Vidhya is the largest data science community of India'

# check for the characters y, d, or h, in the above string

x = re.findall("[ydh]", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[46]:


str = 'Analytics Vidhya is the largest data science community of India'

# check for the characters between a and g (range) in the above string
x = re.findall("[a-g]", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# #### Lets solve a problem.

# In[48]:


str = "Mars'average distance from the Sun is roughly 230 million km and its orbital period is 687 (Earth) days."

# extract the numbers starting with 0 to 4 from the above string
x = re.findall(r"[5-9]\d+",str)
if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[49]:


# [^] check whether string has other characters mentioned after ^

str = 'Analytics Vidhya is the largest data science community of India'

# check if there are other characters besides y, d, or h
x = re.findall("[^ydh]", str)

if(x):
    print("Yes, there is at least one match!")
else:
    print("No match")
print(x)


# In[54]:


# [a-zA-Z0-9] check whether string has terms starting with characters other than alphamuneric

str = "@AV Largest Data Science community #AV!!"

# extract words that start with special character
x = re.findall("[^a-zA-Z0-9 ]\w+", str)

print(x)


# # Solove complex queries
# 
# ### Extracting Email IDs

# In[58]:


str = 'Send a email to rohan.1997@gmail.com, smith_david34@yahoo.com and priya@yahoo.com about the meeting @2PM'

# \w matches any alpha numberic character
# + for repeats a character one or more times
# x = re.findall('\w+@\w.com', str)
x = re.findall('[a-zA-Z0-9._-]+@\w+\.com', str)
               
print(x)


# ### Extracting Dates

# In[60]:


text = "London Olympic 2012 was held from 2012-07-27 to 2012/08/12."

# '\{4}' repeats '\d' 4 times
match = re.findall('\d{4}.\d{2}.\d{2}', text) 
print(match)


# In[62]:


text = "London Olympic 2012 was held from 27 Jul 2012 to 12-Aug-2012."

# '\{4}' repeats '\d' 4 times
match = re.findall('\d{2}.\w{3}.\d{4}', text) 
print(match)


# In[63]:


#extracting dates with varying lengths
text = "London Olympic 2012 was held from 27 September 2012 to 12 August 2012."

# '\w3,10}' repeats '\w' 3 to 10 times
match = re.findall('\d{2}.\w{3,10}.\d{4}', text)
print(match)


# In[76]:


# Extracting title from names - Titance Dataset
import pandas as pd

#load dataset
data=pd.read_csv("titanic.csv")


# In[77]:


data.head()


# In[78]:


# print first 10 names
data['Name'].head(10)


# ## Methold 1: Split on pandas dataframe and extract the title

# In[79]:


name = "Allen, Mr. William Henry"
name2 = name.split(".")
name2


# In[80]:


name2[0].split('.')


# In[81]:


title=data['Name'].apply(lambda x: x.split(".")[0].split(",")[1])
title.value_counts()


# ## Method 2: Use RegEx to extract titles

# In[82]:


def split_it(name):
    return re.findall("\w+\.", name)[0]


# In[83]:


title= data['Name'].apply(lambda x: split_it(x))
title.value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




