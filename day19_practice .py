# Exercise 1
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)

count(5)

#Exercise - 

def count(n):
    if n == 0:
        return
    count(n - 1)
    print(n)

count(5)

#Exercise 

def mystery(n):
    if n == 0:
        return
    print("Start", n)
    mystery(n - 1)
    print("End", n)

mystery(3)

#Exercise 

def mystery(n):
    if n == 0:
        return
    print(n)
    mystery(n - 1)
    print(n * 10)

mystery(3)

# o/p -
# 3
# 2
# 1
# 10
# 20
# 30

# Create:
# def factorial(n):
# It should calculate the factorial of n.
# Examples:
# factorial(5) → 120
# factorial(4) → 24
# factorial(1) → 1
# Use recursion, not a for or while loop.
# Also identify in your solution:
# What is the base case?
# What is the recursive case?

def factorial(n):
    if n==1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))

#Write a recursive funtion to add the 4 numbers you write.
#Example - 1234 = 10 

def sum_digits(n):
    if n == 0:
        return 0
    
    return n%10 + sum_digits(n//10)

print(sum_digits(1234))

# Write a recursive function:
# It should return the string reversed.
# Examples:
# reverse_string("Python") → "nohtyP"
# reverse_string("hello")  → "olleh"
# reverse_string("abc")    → "cba"
# Requirements
# Must use recursion.
# No for or while loops.
# Don't use [::-1].
# Handle an empty string.
# Identify your base case and recursive case.

def reverse_string(text):
    if text == '':
        return ''
    return reverse_string(text[1:])+text[0]

print(reverse_string("Python"))

# Problem 9
# Write a recursive function:
# Examples:
# power(2, 3) → 8
# power(5, 2) → 25
# power(10, 0) → 1
# Requirements:
# Use recursion.
# No **.
# No loops.
# Handle exponent 0.
# Identify the base case and recursive case.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base,exponent-1)

print(power(2,3))

    
