# Exercise 1
# Print numbers from 1 to 10 using a for loop.

for i in range(1,11):
        print(i)


# Exercise 1
# Print all even numbers from 1 to 20.
print()     
for i in range(21):
    if i%2==0:
          print(i)

# Exercise 3
# Print the multiplication table of any number entered by the user.

number = int(input("Enter a number :"))
for i in range(1,11):
      print(f"{number}*{i}={number*i}")

# Exercise 4
# Ask the user for a number and calculate the sum from 1 to that number.
      
number = int(input("enter a number:"))
total = 0
for i in range(1,number+1):
      total+=i
print(total)

# Exercise 5
# Using a while loop, print numbers from 10 down to 1.

i=10
while i>=1:
    print(i)
    i=i-1

# Exercise 6
# Print all numbers from 1 to 20, but skip multiples of 3 using continue.

for i in range(1,21):
    if i%3==0:
        continue
    print(i)



# ⭐ Mini Project
# Number Guessing Game

# Requirements:

# Store a secret number (e.g., 7).
# Ask the user to guess it.
# Keep asking until they guess correctly.
# If the guess is too high, print "Too high".
# If the guess is too low, print "Too low".
# When correct, print "Congratulations!" and stop the loop.

secret_number= 7
guess = int(input("Guess the secret number:"))
while guess!=secret_number:
    if guess>secret_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess the secret number:"))
print("Congratulations!")
 





      

