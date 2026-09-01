# Exercise 1
# Create a list of five fruits.
# Print the whole list.
# Print the first fruit.
# Print the last fruit.

fruits = ['kiwi','apple','mango','litchi','berry']
print(fruits)
print(fruits[0])
print(fruits[-1])

# Exercise 2
# Create a list of numbers.[10, 20, 30, 40]
# Add:50 using append().
# Print the list.

numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)

# Exercise 3
# Using the same list,insert: 25 between 20 and 30.Print the list.

numbers = [10, 20, 30, 40]
numbers.insert(2,25)
print(numbers)

# Exercise 4
# Remove: 30 using remove().Print the list.\

numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

# Exercise 5
# Create a list of student names.Print each name using a for loop.

names = ['Sia','Ria','Mini']
for name in names:
    print(name)

# Exercise 6 
# Ask the user for a fruit.Check whether it exists in the list.

fruits = ['kiwi','apple','mango']
user_input = input("Enter a fruit name: ")
if user_input in fruits:
    print('Available')
else:
    print('Not Available')

# # Mini Project – Student Marks Manager
# # Create two lists:
# # students = ["Ali", "Sara", "John"]
# # marks = [85, 90, 78]
# # Using a loop, print:
# # Ali : 85
# # Sara : 90
# # John : 78
# # Hint: Think about how you'll access the matching item from both lists.
# #  We haven't explicitly covered it yet, so try solving it yourself first.

students = ["Ali", "Sara", "John"]
marks = [85, 90, 78]
for i in range(len(students)):
    print(students[i],marks[i])
