# Variables hold information

wallet = 41

print(wallet)

# Variables can change overtime

wallet = 32

print(wallet)

# Make a variable called day and set it to the date of the month
day = 15
print(day)

# Types
# int = whole number no decimals

# float = numbers with decimals
weight = 170.2

# numbers can be positive or negative

print(weight / 2)

# Find something around in your life to represent an int and a float. Put them in variables

car_value = 10000
height_inches = 67.5

print(car_value)
print(height_inches)

# Strings represent text in python

shirt = 'blue'
print(shirt)

store = 'Abe\'s Pizza Shop, the "best" there is'
print(store)

# Put the name of a movie you like into a variable called movie
movie = 'Fast Times at Ridgemount High'
print(movie)

# Using variables in strings

day = 15
month = 'January'
temp = 46

# placing f in front of quotes allow to place variables inside a string
print(f"Today is {month} {day} and it's {temp} degrees outside")

# Make a variable called day_name and set it to day of the week like Tuesday and add it to the string above

day_name = 'Sunday'
print(f"Today is {day_name} {month} {day} and it's {temp} degrees outside")

# Booleans and if statements
# Boolean is binary TRUE or FALSE

light_is_on = True
if light_is_on:
  print('The light is on!')
# if light_is_on = True code will run. If it says False or nothing will not run

# Find something around you that could be represented by a Boolean and make a variable for it

dinner_is_ready = True

# Comparision and else

light_is_on = True
if light_is_on:
  print('The light is on!')
else: 
  print("We're in the dark")

weight_lbs = 170.2

if weight_lbs < 175:
  print("You're under weight :)")
    
# Make a variable age, and if someone is 18 years or older, print that they are an adult. Otherwise print that they are a child

age = 31
if age >= 18:
  print('Is an adult')
else:
  print('They are a child')

# Questions

# 1. Booleans can only be True and False

# 2. What symbol would you use to see if two things are equal to each other? ==

# 3. What letter do we put in front of a String if we want to put variables in it? f

# 4. Which of the following is an Int? 43 whole number

# 5. Which of the following is not a String? 43 no quotes