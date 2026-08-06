#Excercise 1 
# Create two files.
# calculator.py
# Create four functions:
# add()
# subtract()
# multiply()
# divide()
# main.py
# Import the calculator module.
# Call all four functions.

import calculator

print(calculator.add(10,2))
print(calculator.subtract(10,2))
print(calculator.multiply(10,2))
print(calculator.divide(10,2))

# Exercise 2
# Use:
# import math
# Print:
# Square root of 49
# Value of π

import math
print(math.sqrt(49))
print(math.pi)

# Exercise 3
# Use:
# import random
# Print:
# A random number between 1 and 100.

import random
print(random.randint(1,100))

# Exercise 4
# Create a list:
# colors = ["Red", "Blue", "Green", "Black"]
# Print a random color.

import random
colors = ["Red", "Blue", "Green", "Black"]
print(random.choice(colors))

# ⭐ Mini Project – Number Guessing Game (Improved)
# You've already built a guessing game on Day 3.
# Now improve it using the random module.
# Requirements:
# Computer chooses a random number from 1 to 50.
# User keeps guessing.
# Print:
# "Too High"
# "Too Low"
# "Correct!"
# Count how many attempts the user took.

import random
secret_number = random.randint(1,50)
print(secret_number)
attempt = 0
guess = int(input("Guess a number : "))
attempt+=1
while guess!=secret_number:
    if guess > secret_number:
        print("Too High")
        guess = int(input("Guess the secret number:"))
        attempt+=1
    else:
        print("Too Low")
        guess = int(input("Guess the secret number:"))
        attempt+=1
        
print("Correct!")
print("The number of attempts is ",attempt)



