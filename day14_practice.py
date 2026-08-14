# Exercise 2 — Creating a set
# You have:
# numbers = [10, 20, 10, 30, 20, 40]
# Create a set from this list and print it.

numbers = [10, 20, 10, 30, 20, 40]
print(set(numbers))

# Exercise 3 — Add elements to a set
# Start with:
# numbers = {10, 20, 30}
# Add 40 to the set.
# Then add 20 again.
# Finally, print the set.

numbers = {10, 20, 30}
numbers.add(40)
numbers.add(20)

# Exercise 4
# Start with:
# numbers = {10, 20}
# Use .update() to add these three values at once:30, 40, 50
# Then print the set.

numbers = {10, 20}
numbers.update({30,40,50})
print(numbers)

# Exercise 5 — Removing elements
# Start with:
# numbers = {10, 20, 30, 40, 50}
# Remove 30 from the set.

numbers = {10, 20, 30, 40, 50}
numbers.remove(30)
print(numbers)

# Exercise 6
# Given:
# numbers = {10, 20, 30, 40, 50}
# Try removing 100 using .discard().

numbers = {10, 20, 30, 40, 50}
numbers.discard(100)

# Exercise 7 — Set membership
# Given:
# numbers = {10, 20, 30, 40, 50}
# Write an if/else statement to check whether 30 is present in the set.
# If it exists, print: 30 exists
# Otherwise: 30 does not exist

numbers = {10, 20, 30, 40, 50}
if 30 in numbers:
    print("30 Exists")
else:
    print("30 does not exist")

# Exercise 8
# Try writing code that finds the intersection of:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# and prints the result.
# Use .intersection() first.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))

# Exercise 9 — Union

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))

# Exercise 10 — Difference
# # Now let's learn difference.
# Given:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))

# Exercise 11
# Now predict the result of:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set2.difference(set1))
#o/p - {6,7,8}

# Exercise 12 — Symmetri Difference Using:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))
print(set2^set1)

# Exercise 13 — Set + List
# Given:
# numbers = [10, 20, 10, 30, 20, 40, 30, 50]
# Write a function that returns a list containing only the unique numbers, while using a set to identify the duplicates.
# Expected output:
# [10, 20, 30, 40, 50]
# Don't simply do list(set(numbers)) yet.practice combining a set + loop + list.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]
result = set()
for number in numbers:
    result.add(number)
print(result)

# Day 14 — Exercise 14
# You have two lists of students:
# class_a = ["Ali", "Sara", "John", "Zoya"]
# class_b = ["John", "Zoya", "Omar", "Aisha"]
# Find the students who are present in both classes.
# Expected result:
# {"John", "Zoya"}

class_a = ["Ali", "Sara", "John", "Zoya"]
class_b = ["John", "Zoya", "Omar", "Aisha"]
class_a = set(class_a)
class_b = set(class_b)
print(class_a.intersection(class_b))

