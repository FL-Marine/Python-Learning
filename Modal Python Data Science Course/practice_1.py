
# coding: utf-8

# ## Practice 1: First Steps in Python
# 
# In this practice assignment, you'll start your Python journey by learning some of the basics in manipulating data of various types, and using the `print()` function to see what is happening in your Python program. 
# 
# Throughout the practice, this [documentation on mathematical operators](https://www.tutorialspoint.com/python/python_basic_operators.htm) may be helpful. 

# ### Using the `print()` Function
# 
# `print()` is a built-in function that allows you, the human, to see what is going on with code. It does not transform or transmit anything to the Python program.
# 
# For example, we've printed the message, "Hello World!" below.

# In[1]:


print('Hello World!')


# ### Comments
# 
# Sometimes, we want to explain and organize our code without telling the computer to do anything. Enter comments! The `#` symbol tells Python that you are writing a comment for another human to read. Python will ignore anything written on the line after the `#` symbol. 

# In[2]:


# Print 'Hello World!'
print('Hello World') # Another comment


# ### Basic Data Types
# 
# In Python, there are a number of different data types that we can use to store information. The four most common are integers, floats, strings, and booleans. 

# In[3]:


print(3)              # integer value
print(3.5)            # float value
print('Hello World')  # string value
print(True)           # boolean value


# ### Variables
# 
# Variables allow us to store data for manipulation or visualization across various parts of our Python program. This reduces repetitive code and makes our program more readable.
# 
# For example, imagine that we are writing a program to create a receipt for an online shopper. We might want to print the cost of the order in multiple places. Therefore, we could store that value in a variable named `cost`.

# In[4]:


cost = 21.27
print('The cost of your order is $', cost)
print('Please press the green button to accept the charge of $', cost)


# ### Edge Case: Quotation Marks Inside Strings
# 
# One edge case to think about is how to create a string that contains quotes inside of it. 

# In[5]:


# Edge Case! Quotes in Quotes


# Use single quote to encapsulate the string if you need to use a double quote inside
print('She said, "You have to use a single quote on the outside if you want to quote me."')

# Use double quote to encapsulate the string if you need to use a single quote inside
print("I'm using contractions and so I've got to use double quotes.")

# You can also use the escape character (\) to tell python to ignore the character that comes after
print('Here I\'ll use the backslash to use single quotes and a contraction.')


# ### Mathematical Operators
# 
# Python has a number of built-in mathematical operators. These operators can be used to perform transformations on data.
# 
# It is important to note that operators work differently for different data types.

# In[7]:


# Create variables for math in later cells

a = 2
b = 4
c = 'Hello '
d = 'World!'


# Notice that when you run the cell above you don't see anything in the output. Python is storing the variables in memory but not doing anything else with them.

# In[8]:


# Addition (+)
print(a + b)


# In[9]:


# Addition of strings
print(c + d)


# In[10]:


# Subtraction (-)
print(a - b)


# In[11]:


# Multiplication (*)
print(a * b)


# In[12]:


# Exponent (**)
print(b ** a)


# In[13]:


# Division (/)
print(b / a)


# Division always produces a `float` data type, even if the division results in a whole number.

# In[14]:


# Modulo (%)

x = 5
y = 2

print('The remainder of dividing x by y is:', x%y)


# Modulo `%` first does a division, and then returns the remainder left over after the division. The code above does the following operation: 
# 
# 5 divided by 2 equals 2 with a remainder of 1, so 5%2 outputs 1

# In[15]:


# Floor division (//)

# regular division (/) returns a precise float value
print('Two divides into nine', 9/2, 'times')

# floor division (//) returns only the whole integer
print('Two floor divides into nine', 9//2, 'times')


# ### Practical Example
# 
# Suppose we work at a car dealership and want to know how many cars to sell to get to $100,000 in profit. Using division will result in a `float` value, which does not tell us how many whole cars to sell to reach our goal. 
# 
# One idea is to use floor division to get the number of cars before the threshold is reached, and then add one. 

# In[16]:


# Save relevant values
avg_sales_price = 54853
avg_distribution_cost = 45734
profit_per_car = avg_sales_price - avg_distribution_cost
profit_goal = 100000


cars_to_sell = profit_goal / profit_per_car                  # this is a float
cars_to_sell_pretty = (profit_goal // profit_per_car) + 1    # this is the number of cars to sell


print(cars_to_sell)
print(cars_to_sell_pretty)


# ## Practice on Your Own
# 
# Complete the following prompts to practice your skills. 
# 
# To establish good habits, create variables to solve the prompts first, then print the variables. 

# #### 1. Run the code in the cell to see the error/s. Fix the errors in the code. 

# In[19]:


# 1

print('This is not the error. Its somewhere else.')
print('Mark Twain said: "I never met a quote I did not like."') # he didn't really say that as far as we know


# #### 2. Run the code in the cell to see the error. Fix the error in the code.

# In[29]:


# 2

# print('This produces' + 1 + 'error')

print('This produces + 1 + error')


# ### For the remaining questions, use the data below:
# 
# Imagine that you work for Edison Car Company, and have the following information about car sales:
# - `edisons_sold` is the number of cars sold in the past month
# - `avg_sales_price` is the average sales price of each car
# - `avg_distribution_cost` is the average amount that it costs you to distribute each car
# 
# Run the cell below to create and save the data.

# In[43]:


# 'Edison Car Company' data for the remaining practice challenges

edisons_sold = 35
avg_sales_price = 54853
avg_distribution_cost = 45734


# #### 3. Calculate the average profit per car using the 'Edison Car Company' sales data and save the result as a variable. Print out the result.

# In[44]:


# 3
# YOUR CODE GOES HERE

avg_profit_per_car = (avg_sales_price - avg_distribution_cost) // 35
print(avg_profit_per_car)


# #### 4. Find and print the total profit for this month based on the 'Edison Car Company' sales data.

# In[49]:


# 4
# YOUR CODE GOES HERE

total_profit = (avg_sales_price - avg_distribution_cost) * 35
print(total_profit)


# #### 5. Assuming identical sales and profit margins from this month, how many months of sales are needed to make \$1,000,000 profit or more? Calculate and print your answer.

# In[8]:


# 5
# YOUR CODE GOES HERE

avg_sales_price_1m = 54853
avg_distribution_cost_1m = 45734
profit_per_car_1m = avg_sales_price_1m - avg_distribution_cost_1m
profit_goal = 1000000
total_profit = 319165
months = 12

target_months = profit_goal // total_profit
print(target_months)

