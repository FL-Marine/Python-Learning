# Functions 

# functions give a name to chunk of code def = define

def bark():
  print("Woof woof!")
  print("Imma dawg!")
# nothing shows up if function is not called
bark() 

for x in range(10):
  bark()
# putting code in for loop:
  
# Create a function called hello that prints "Hello Abe!"

def hello():
  print("Hello Abe!")
hello()

# Parameters

# Parameters is a way to pass some information into a function

# Making function passing a new persons name that is printed
# parameter is in the first hello()
def hello(name):
  print(f"Hello {name}!")
hello("Matt")

def add_numbers(num1,num2):
  print(num1 + num2)

add_numbers(4,8)
add_numbers(3,7)

# Create a function called dog_info that takes in a dog's age and name and prints a sentence about the dog

def dog_info(age, name):
  print(f'Hi my name is {name} and I am {age} years old')

dog_info(4,"Jitz")

# Return

# retunring passes out information that passes thru fucntions and parameters

def double(number):
  return number * 2
new_number = double(5)
print(new_number)

# Create a function that returns a string in all caps

def uppercase(text):
  return text.upper()

print(uppercase("abe"))

names = ['abe', 'matt', 'albert']
for name in names:
  print(uppercase(name))

# Taking a list of names and running them thru for loop to print in all caps

  # Comments 

wallet = 40 # variable for wallet

wallet -= 8 # I bought food

wallet += 40 # I got paid!

# Need to uppercase this
'abe'.upper()

# Input 
# allows users tp insert a value into a program
user_text = input('Enter some text: ')
#print(user_text.upper())

# user_number = input("What do you want to double? ")

# print(int(user_number) * 2)

# First ask for some text, and then prompt "Enter 1 to uppercase and 2 to lowercase: "  then either upper or lowercase it

upper_or_lower = input("Enter 1 to uppercase and 2 to lowercase: ")

if upper_or_lower == "1":
  print(user_text.upper())
else:
  print(user_text.lower())