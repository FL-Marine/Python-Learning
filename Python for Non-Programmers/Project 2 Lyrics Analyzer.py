# Splitting a string

# using triple quotes allows for large text to be pasted using multilines 
text = """
I’m the best ever. I’m the most brutal, vicious, and most ruthless champion there’s ever been. There’s no one can stop me,” said Tyson, who remains the youngest boxer to ever capture the WBC, WBA, and IBF world heavyweight titles.

“Lennox (Lewis) is a conqueror? No. I’m Alexander. He’s no Alexander. I’m the best ever. There’s never been anybody as ruthless. I’m Sonny Liston. I’m Jack Dempsey. There’s no one like me. I’m from their cloth. There’s no one that can match me. My style is impetuous. My defense is impregnable. And I’m just ferocious. I want your heart. I want to eat his children. Praise be to Allah. """

print(len(text))
# 619 characters

print(text.split())
# List of strings

print(len(text.split()))
# 109 words

# Counting the words
word_count ={}
# empty dictionary

for word in text.split():
  print(word)
# print out word by looping thru list

# Assigning words as keys to dictionary & provide a # as value
for word in text.split():
  word_count[word] = 1

print(word_count)

# Counting multiple values if they appear more then once
for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)

# test
text1 = """
a b c A a b
"""
print(len(text1.split()))
# 6 words
print(text1.split())

word_count1 ={}
# empty dictionary

for word in text1.split():
  print(word)
# print out word by looping thru list

# Assigning words as keys to dictionary & provide a # as value
for word in text1.split():
  word_count1[word] = 1

print(word_count1)

# Counting multiple values if they appear more then once
for word in text1.lower().split():
  if word in word_count1:
    word_count1[word] += 1
  else:
    word_count1[word] = 1

print(word_count1)
#.lower() ignores captilaztion 