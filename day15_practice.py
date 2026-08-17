# Write the code to:
# Create the tuple.
# Unpack it into name, age, and course.
# Print all three variables.

student = ('Rahul',24,'Python')
name,age,course = student
print(name)
print(age)
print(course)

# Exercise 7 — Swapping values

a = 10
b = 20

a,b = b,a
print(a)
print(b)

# Exercise 10 — Tuple conversion
# You have:
# numbers = [10, 20, 30, 40]
# Convert this list into a tuple and store the result in a variable called numbers_tuple.
# Expected:
# (10, 20, 30, 40)
# Use the appropriate built-in function.

numbers = [10, 20, 30, 40]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# Write a function that returns
# How many times 20 appears.
# The index of the first 20.
data = (10, 20, 30, 20, 40, 10, 20)
print(data.count(20))
print(data.index(20))

# Write a function called tuple_info(data) that:
# receives a tuple
# counts how many times 20 appears
# finds the index of the first 20
# returns both values

data = (10, 20, 30, 20, 40, 10, 20)
def tuple_info(data):
    count = data.count(20)
    index = data.index(20)
    return(count,index)
print(tuple_info(data))
count,index = tuple_info(data)
print("Count:",count)
print("Index:",index)
