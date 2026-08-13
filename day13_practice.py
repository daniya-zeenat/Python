# Exercise 1
# Create a dictionary called student containing:
# name → "li"
# age → 58
# course → "Python"
# Then print the student's name.

student = {
    "name": "li",
    "age": 58,
    "course": "Python"
}

print(student["name"])

# Exercise 2
# Using the same dictionary, print:
# The student's age
# The student's course
# Try accessing both values using their keys.

print(student['age'])
print(student["course"])

# Exercise 3 — Adding and changing values
# Now do two things:
# Add a new key "city" with the value "Delhi".
# Change "age" from 45 to 85.

student = {
    "name": "lii",
    "age": 45,
    "course": "Python"
}

student['city'] = 'Delhi'
student['age'] = 85

print(student["city"])
print(student["age"])

# Exercise 4 — Removing a key
# Using the same dictionary, remove the "course" key.
# Then print the dictionary to verify that "course" has been removed.

del student['course']

#Exercise 5 — Check whether a key exists
#Write an if statement that checks whether the key "course" exists.

student = {
    "name": "lii",
    "age": 85,
    "city": "jaipur"
}

if "course" in student:
    print("Course exists ")
else:
    print("Course does not exist")

#Exercise 6 — Dictionary loops
#Write a for loop that prints each key.

for key in student:
    print(key)

# Exercise 7: Now write a loop that prints only the values:

for key in student:
    print(student[key])

# Exercise 8 — .keys()
print(student.keys())

# #Exercise 9
# Use .items() and a loop to print only the subjects/keys whose value is a number greater than 80.
# For this example, "marks" should be identified.

student = {
    "name": "lii",
    "age": 23,
    "city": "Jaipur",
    "marks": 85
}

for key,value in student.items():
    if type(value) == int and value > 80 :
        print(key,value)

# #Exercise 10: Dictionary counting
# Given this list:
# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Expected result:
# {
#     "apple": 3,
#     "banana": 2,
#     "orange": 1
# }

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

def count_fruit(fruits):
    count = {}

    for fruit in fruits:
        if fruit in count:
            count[fruit] += 1
        else:
            count[fruit] = 1

    return count

print(count_fruit(fruits))

# Exercise 11
# Let's apply the same idea to something closer to interview questions.
# Given:
# numbers = [1, 2, 2, 3, 1, 4, 2, 3]
# Write a function that returns how many times each number appears.
# Expected:
# {1: 2, 2: 3, 3: 2, 4: 1}

numbers = [1, 2, 2, 3, 1, 4, 2, 3]
def count_num(numbers):
    count = {}
    for number in numbers:
        if number in count:
            count[number] +=1
        else:
            count[number] = 1
    return count
print(count_num(numbers))

# Exercise 12
# Given:
# numbers = [10, 15, 20, 10, 25, 15, 10, 30]
# Write a function that returns a dictionary containing only the numbers that appear more than once, along with their counts.
# Expected:
# {10: 3, 15: 2}

numbers = [10, 15, 20, 10, 25, 15, 10, 30]
def count_numbers(numbers):
    count = {}
    result = {}
    for number in numbers:
        if number in count:
            count[number]+=1
        else:
            count[number] = 1
    for key,value in count.items():
        if value>1:
            result[key] = value
    return result
print(count_numbers(numbers))

# Exercise 13: Given:
# student_marks = {
#     "Ali": 85,
#     "Sara": 72,
#     "John": 91,
#     "Zoya": 65,
#     "Omar": 88
# }
# Create a new dictionary containing only students who scored 80 or above.
# Expected:
# {"Ali": 85, "John": 91, "Omar": 88}

student_marks = {
    "Ali": 85,
    "Sara": 72,
    "John": 91,
    "Zoya": 65,
    "Omar": 88
}

def count_marks(student_marks):
    marks = {}
    for key,value in student_marks.items():
        if value > 80 :
            marks[key] = value 
    return marks
print(count_marks(student_marks))

# Exercise 14
# Convert this normal loop into a dictionary comprehension:
# numbers = [1, 2, 3, 4, 5]
# result = {}
# for number in numbers:
#     result[number] = number ** 2
# print(result)
# Expected:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

numbers = [1, 2, 3, 4, 5]
result = {number:number**2 for number in numbers}
print(result)

#Exercise 15
# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Create a dictionary containing only even numbers, where:
# the number is the key
# its square is the value
# Expected:
# {2: 4, 4: 16, 6: 36}
# Use a dictionary comprehension with if.

numbers = [1, 2, 3, 4, 5, 6]
result = {number:number**2 for number in numbers if number%2==0}
print(result)

#Exercise 16
#Create a new dictionary containing only products whose price is greater than 50, but increase their price by 10%

prices = {
    "apple": 50,
    "banana": 30,
    "orange": 80,
    "mango": 120
}

result = {key:value*1.10 for key,value in prices.items() if value>50}
print(result)