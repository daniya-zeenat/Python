# Exercise 1
# Write a function that receives a list of numbers and returns the largest number in the list.
# #Example - 
# Input:  [10, 25, 7, 42, 18]
# Output: 42

numbers = [10, 25, 7, 42, 18]
def num(numbers):
    numbers.sort()
    largest_number = numbers[-1]
    return largest_number

print(num(numbers))

# Exercise 2: Find the largest number without using sort() or max().

n = [10, 25, 7, 42, 18]
def largenum(n):
    largest_num = n[0]
    for i in n:
        if i>largest_num:
            largest_num = i

    return largest_num

print(largenum(n))

# Exercise 3 — Find the smallest number
# Write a function that receives a list and returns the smallest number.
# Example:
# numbers = [10, 25, 7, 42, 18]

numbers = [10, 25, 7, 42, 18]
def smallnum(numbers):
    smallest_num = numbers[0]
    for number in numbers:
        if number < smallest_num:
            smallest_num = number
    return smallest_num
print(smallnum(numbers))

# Exercise 4
# Now let's make it slightly harder.
# Write a function that receives a list of numbers and returns the sum of all the numbers.
# Example:
# numbers = [10, 20, 30, 40]
#Don't use sum() yet.

numbers = [10, 20, 30, 40]
def numsum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(numsum(numbers))

# Exercise 5
# Now combine the patterns you've learned.
# Write a function that receives a list of numbers and returns how many numbers are greater than 10.
# Example:
# numbers = [5, 12, 8, 20, 15, 3]
# Expected output:3
# Don't use count() or any other built-in counting function.

numbers = [5, 12, 8, 20, 15, 3]
def great(numbers):
    num = 0
    for number in numbers:
        if number>10:
            num += 1
    return num
print(great(numbers))

# Exercise 6
# Write a function that receives a list and returns how many even numbers are in the list.
# Example:
# numbers = [10, 15, 22, 7, 8, 13]

numbers = [10, 15, 22, 7, 8, 13]
def even_count(numbers):
    count = 0
    for number in numbers:
        if number%2==0:
            count+=1
    return count
print(even_count(numbers))

# Exercise 7
# Write a function that receives a list of numbers and returns a new list containing only the even numbers.
# Example:
# numbers = [10, 15, 22, 7, 8, 13]
# Expected output: [10, 22, 8]

numbers = [11, 12, 13, 15, 2]
def even_list(numbers):
    output_list = []
    for number in numbers:
        if number%2==0:
            output_list.append(number)
    return output_list
print(even_list(numbers))                                                                                                                                                                                                                                                                                       

# Exercise 8
# Now do the opposite:
# Write a function that receives a list and returns a new list containing only the odd numbers.
# Example
# numbers = [11, 12, 13, 15, 2]
# Expected output:
# [11, 13, 15]

numbers = [11, 12, 13, 15, 2]
def odd_list(numbers):
    output_list = []
    for number in numbers:
        if number%2!=0:
            output_list.append(number)
    return output_list
print(odd_list(numbers))

# Write a function that receives a list and returns a new list containing only numbers greater than 10.
# Example:
# numbers = [5, 12, 8, 20, 15, 3]
# Expected:
# [12, 20, 15]

numbers = [5, 12, 8, 20, 15, 3]
def greater_list(numbers):
    output_list = []
    for number in numbers:
        if number > 10:
            output_list.append(number)
    return output_list
print(greater_list(numbers))

# Write a function that receives a list and returns a new list containing only numbers that are divisible by both 3 and 5.
# Example:
# numbers = [10, 15, 20, 30, 45, 22, 60]
# Expected output:
# [15, 30, 45, 60]

numbers = [10, 15, 20, 30, 45, 22, 60]
def div_list(numbers):
    output_list = []
    for number in numbers:
        if number%3==0 and number%5==0:
            output_list.append(number)
    return output_list
print(div_list(numbers))

# List Comprehension 

# Exercise 1
# Convert this normal loop into a list comprehension:

# numbers = [2, 4, 6, 8, 10]
# result = []
# for number in numbers:
#     result.append(number * 3)

# print(result)

# Expected output:
# [6, 12, 18, 24, 30]
# Try writing only the list-comprehension version.

numbers = [2, 4, 6, 8, 10]
result = [number * 3 for number in numbers]
print(result)

# Exercise 2 — Filtering
# Now let's add a condition.
# Convert this into a list comprehension:
# numbers = [5, 12, 8, 20, 15, 3]
# result = []
# for number in numbers:
#     if number > 10:
#         result.append(number)
# print(result)
# Expected:
# [12, 20, 15]

numbers = [5, 12, 8, 20, 15, 3]
result = [number for number in numbers if number>10]
print(result)

# Exercise 3 — combine both
# Create a list containing the squares of only the even numbers.
# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Expected:
# [4, 16, 36]

numbers = [1, 2, 3, 4, 5, 6]
result = [number**2 for number in numbers if number%2==0]
print(result)

# Exercise 4 
# Given:
# numbers = [10, 15, 20, 25, 30, 35, 40]
# Create a new list containing only numbers divisible by 5 and greater than 20.
# Expected output
# [25, 30, 35, 40]
# Use a list comprehension and and.

numbers = [10, 15, 20, 25, 30, 35, 40]
result = [number for number in numbers if number%5==0 and number > 20 ]
print(result)

# Exercise 5
# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Create a list where:
# even numbers → "Even"
# odd numbers → "Odd"
# Expected:
# ["Odd", "Even", "Odd", "Even", "Odd", "Even"]
# Use a list comprehension with if/else.

numbers = [1, 2, 3, 4, 5, 6]
result = ["Even" if number%2==0 else "Odd" for number in numbers]
print(result)