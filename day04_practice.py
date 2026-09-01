# Exercise 1
# Create a function:
# def welcome()

def welcome():
    print("Welcome to Python")
welcome()
welcome()
welcome()


# Exercise 2
# Create
# def greet(name):

def greet(name):
    print("Hello",name)

greet("User")
greet("User2")
greet("User3")

# Exercise 3
# Create:
# def add(a, b):
# Return the sum.

def add(a,b):
    return a+b
result = add(10,20)
print(result)

# Exercise 4
# Create a function that returns the square of a number.
# Example:
# square(5)

def square(n):
    return n*n
result = square(5)
print(result)

# Exercise 5
# Create a function that checks whether a number is even or odd.
# Example:
# check_even_odd(8)

def check_even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
result = check_even_odd(8)
print(result)



# Mini Project

# Take your calculator from Day 2 and rewrite it using functions.
# Instead of everything in one block, create:
# addition(a, b)
# subtraction(a, b)
# multiplication(a, b)
# division(a, b)
# Then call the correct function based on the user's choice.

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        print("Division with zero is not possible")
    else:
        return a/b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation: +,-,*,/:  ")
if operation == '+':
    print(addition(a,b))
elif operation == '-':
    print(subtraction(a,b))
elif operation == '*':
    print(multiplication(a,b))
elif operation == '/':
        print(division(a,b))
else:
    print("The entered operator is invalid.Please enter a valid operator from +,-,*,/")



