# %% [markdown]
# # What Is a For Loop in Python?
# 
# - A for loop allows you to iterate over a sequence that can be either a list, a tuple, a set, a dictionary, or a string. You use it if you need to execute the same code for each item of a sequence.
# 

# %%
new_students_countries = ['Great Britain', 'Germany', 'Italy']
for country in new_students_countries:
    print(country)

# %% [markdown]
# # syntax of the *for* loop ^:
# 
# 1. It starts with the for keyword, followed by a value name that we assign to the item of the sequence (country in this case).
# 
# 2. Then, the in keyword is followed by the name of the sequence that we want to iterate.
# 
# 3. The initializer section ends with “:”.
# 
# 4. The body of the loop is indented and includes the code that we want to execute for each item of the sequence.

# %%
student_countries = ['Belgium', 'Czech Republic', 'France',
                    'Germany', 'Hungary', 'Ireland',
                    'Netherlands', 'Spain']
new_countries = 0
for country in new_students_countries:
    if country not in student_countries:
        new_countries += 1
print('We have students from', new_countries, 'new countries.')


# %% [markdown]
# # syntax of the *for* loop ^:
# 
# 1. start by initializing the variable new_countries with 0 value.
# 
# 2. iterate over the list new_students_countries, and check for each country in this list if it is in the list students_countries.
# 
# 3. if no new country in list it is a new country and increase new_countries by 1.
# 
# 4. Since there are three items in new_students_countries, the for loop runs three times.
# 
# 5. Already have students from Germany, Great Britain and Italy are new countries for the student community.

# %% [markdown]
# # For Loops to Iterate Over Different Sequence Types
# 
# - Sets are used to store multiple items in a single variable

# %%
new_students_countries = {'Great Britain', 'Germany', 'Italy',
'Italy'}
new_countries = 0
for country in new_students_countries:
    if country not in student_countries:
        new_countries += 1
print('We have students from', new_countries, 'new countries.')

# %% [markdown]
# # syntax of the *for* loop ^:
# 
# 1. {sets are within curly brackets}
# 
# 2. There are 4 new students 2 come from Italy.
# 
# 3. This is counting several new students from several countries instead of counting multiple new countries.

# %% [markdown]
#  # For Loops and Tuples

# %%
new_students = ('Albert Bellamy', 'Matty Brattin', 'Abe Diaz')
for name in new_students:
    print('Where does', name, 'come from?')

# interating over a tuple to ask where is the home country for each student

# %% [markdown]
# # For Loops and Dictionaries

# %%
new_student_state_dict = {'Albert Bellamy': 'Ohio',
                         'Matty Brattin' : 'California',
                         'Abe Diaz': 'Florida'}
for key, value in new_student_state_dict.items():
    print(key, ' is from ', value, '.', sep='')

# Dictionaries are used to store data values in key:value pairs.

# %% [markdown]
# # For Loops and Strings 
# 
# - strings are also sequences and can be iterated over using a for loop

# %%
uppercase = False
password = "i@mHappy"
for char in password:
    if char.isupper():
        uppercase = True
print(uppercase)

# %% [markdown]
# # syntax of the *for* loop ^:
# 
# - initalized the variable uppercase as False
# 
# - iterating over every (char) of the string password to check if it is uppercase
# 
# - if condition is met the uppercase variable is set to True

# %% [markdown]
# # For Loops to Iterate Over a Range

# %% [markdown]
# ## For Loops With range()
# 
# - can use range() function to repeat something a certain number of times 

# %%
import random
import string
letters = string.ascii_letters
password_new = ''
for i in range(8):
    password_new += random.choice(letters)
print(password_new)

# creating a password consisting of 8 random characters and merging into new string called password_new

# %%
for i in range(4, 11, 2):
    print(i)

# range function also accepts start and step arguments 

# can defeind starting and ending numbers of the sequence along with difference between numbers

# 4 is start, 11 is stop, 2 is step

# %%
exam_rank = ['Adele', 'James', 'Leonardo']
for i in range(len(exam_rank)):
    print(exam_rank[i], ' gets the #', i+1, ' result.', sep='')

# can use the range() function to access the iteration number within the body of the for loop

# %% [markdown]
# ## For Loops With enumerate()
# 
# - A “Pythonic” way to track the index value in the for loop requires using the enumerate() function. 
# 
# -  It allows you to iterate over lists and tuples while also accessing the index of each element in the body of the for loop

# %%
exam_rank = ['Adele', 'James', 'Leonardo']
for place, student in enumerate(exam_rank, start = 1):
    print(student, ' gets the #', place, ' result.', sep='')

# %%



