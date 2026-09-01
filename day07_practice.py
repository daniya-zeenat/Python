# Exercise 1
# Create a string:
# Python Programming
# Print:First character, Last character ,Length

sentence = 'Python Programming'
print(sentence[0])
print(sentence[-1])
print(len(sentence))

# Exercise 2
# Print:Python using slicing only.

print(sentence[0:6])

# Exercise 3
# Convert:python programming to: PYTHON PROGRAMMING

print(sentence.upper())

# Exercise 4
# Replace:Java with Python

sentence1 = 'Java Programming'
print(sentence.replace("Java","Python"))

# Exercise 5
# Count how many times: a appears in: banana

fruit = 'banana'
print(fruit.count('a'))

# Exercise 6
# Ask the user to enter their full name.Remove extra spaces using:.strip()

name = input("Enter your name:")
print('Hello',name.strip())


# ⭐ Mini Project – Password Strength Checker
# Ask the user to enter a password.
# Check:
# Length is at least 8
# Contains at least one number
# If both are true: Strong Password Otherwise:Weak Password


password = input("Enter a password: ")
length = len(password)
found = False
for letter in password:
    if letter.isdigit():
        found = True
        break
if length>=8 and found:
    print("Strong")
else:
    print("Weak")
