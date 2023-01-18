# List

fav_movies = ["Superbad", "Pineapple Express", "Step Brothers"]

print(fav_movies[2])
# lists use zero base counting it goes 0,1,2....

# Make a list of your 3 favorite numbers and print the firs number from the list

fav_numbers = [3,0,5]
print(fav_numbers[0])

# Lists: Add, insert, delete

fav_movies = ["Superbad", "Pineapple Express", "Step Brothers"]

# len() figures out length of list

print(len(fav_movies))

# .append adds to list

fav_movies.append("Tropic Thunder")

print(len(fav_movies))
# list was 3 now is 4
print(fav_movies)

# insert inputs data in a specifc place

fav_movies.insert(1,"Blades of Glory")
print(fav_movies)

# Delete data from list
del(fav_movies[2])
print(fav_movies)

# Remove enough items from fav_movies until there's only one movie left

del(fav_movies[0])
print(fav_movies)

# For loops
# Allows python to execute the same line of code over & over again

for number in range(10):
  print('Yo')
  print('Yoyoyo')
# specifying a range of numbers and going through it x10
# for loops just like lists using zero base counting just like lists

# list and for loops work together to go through list
fav_movies = ["Superbad", "Pineapple Express", "Step Brothers"]

for movie in fav_movies:
  print(movie)

# Loop 40 times and print the number of the loop times 2 Ex 2,4,6,8
for num in range(40):
  print((num + 1) * 2)

# Dictionaries - key - value pair
# Cousin of lists somewhat related
# Word looking up is the key and the definition is the value

# lists use [], dictionaries use {}
cats = {"Jane":6, "Tom":14, "Sara":8}

cats["Wilson"] = 1
#adding to dictornary

del(cats["Tom"])
# deleting from dictonary
len(cats)
# length of dictionary
print(len(cats))
# Can search by value and prints out key value

# Create a dictionary with ints for keys and Booleans for vaues

int_bool = {"True":1, "False":2}
print(int_bool)
