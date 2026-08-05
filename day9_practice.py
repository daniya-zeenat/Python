# Exercise 1
# Ask the user for a number.
# If they type text instead of a number, print:
# Invalid input.

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input.Write a valid number.")

# Exercise 2
# Ask for two numbers.
# Divide them.
# Handle:
# Invalid number
# Division by zero

try:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2 :"))
    result = number1/number2
    print(result)
except ValueError:
    print("Invalid input.Write a valid number.")
except ZeroDivisionError:
    print("Cannot be divided by zero")

# Exercise 3
# Use else.
# If there is no error, print:
# Calculation successful.

try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2 :"))
    answer = a/b
    print(answer)
except ValueError:
    print("Invalid input.Write a valid number.")
except ZeroDivisionError:
    print("Cannot be divided by zero")
else:
    print("Calculation Successful")

# Exercise 4
# Use finally.
# Print:
# Program finished.
# whether an error happens or not.

try:
    c = int(input("Enter number 1: "))
    d = int(input("Enter number 2 :"))
    div = c/d
    print(div)
except ValueError:
    print("Invalid input.Write a valid number.")
except ZeroDivisionError:
    print("Cannot be divided by zero")
finally:
    print("Program finished")

# ⭐ Mini Project – Safe Calculator
# Requirements:
# Ask the user for two numbers.
# Ask for an operation:
# +
# -
# *
# /
# Perform the calculation.
# Handle:
# Invalid numbers (ValueError)
# Division by zero (ZeroDivisionError)
# Invalid operator (using else or an if statement)

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2 :"))
    operation = input("Enter a operation:+,-,/,*")
    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '/':
        print(num1/num2)
    elif operation == '*':
        print(num1*num2)
    else:
        print("Invalid operator.Please enter a valid operator from : +,-,/,*")
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Division with zero not possible")


