# Picking random numbers
# importing random module from python

import random

print(random.randint(1,10))
#random ints

print(random.random())
# random floats

# Make your own version of a magic 8 ball that prints yes, no, or maybe each time you ask it

answer = random.randint(1,8)

if answer == 1:
  print("Yes")
if answer == 2:
  print("No")
if answer == 8:
  print("Maybe")

# Chosing what fortune to show
import random  
lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will have a great day!'
if fortune_number == 2:
  fortune_text = 'Today will suck...but worth it'
if fortune_number == 3:
  fortune_text = 'You will be a world champion blue belt this year!'
  
print(f'{fortune_text} Your Lucky Number is: {lucky_number}')

