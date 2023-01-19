# Game Loop

#guess = int(input("What is your guess?: "))
# making a guessing game where the input is converted to int aka whole #
#correct_number = 5 
#guess_count = 1

# while loop is combination of if statement and for loop together
#while guess != correct_number:
  #guess_count += 1
  #guess = int(input("What is your guess?: "))

#print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
# while guess is not = to the variablle correct_number
# this is counting the guesses and printing the attempts made to get correct number

# Higher, lower, polish
# Making the game better by telling user they guesses too high or low

import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100.")
print("Picking a number")

time.sleep(3)
print("Picking a number...")
time.sleep(2)
#time.sleep is giving the game a pause


guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
  time.sleep(1)
  guess_count += 1
  if guess < correct_number:
    guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
  else:
    guess = int(input("Wrong. You need to guess lower. What is your guess?: "))

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")

