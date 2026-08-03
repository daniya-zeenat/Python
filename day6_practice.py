# Exercise 1
# Create a tuple of five cities. Print:
# First city
# Last city

city = ('Nagpur','Jaipur','Delhi','Mumbai','Udaipur')
print(city[0])
print(city[-1])

# Exercise 2
# Try changing one value in the tuple.Observe the error.

# city[0] = 'Assam'

# Exercise 3
# Create a set:{10, 20, 20, 30, 30, 40} .Print it.

numbers = {10, 20, 20, 30, 30, 40} 
print(numbers)
#Sets are printed in a different order as compared to initial order.

# Exercise 4
# Create a set.Add:50.Remove:20.Print the result.

number = {1,2,3,4,20}
number.add(50)
number.remove(20)
print(number)

# Exercise 5
# Create a dictionary.
# Print:Name,Marks

student = {
    "name": "Ali",
    "age": 22,
    "marks": 90
}
print(student["name"])
print(student["marks"])

# Exercise 6
# Update the marks to:95.Then print the whole dictionary.

student['marks']=95
print(student)

# ⭐ Mini Project  Student Database
# Create a dictionary:
# Challenge: Can you print each skill using a loop instead of writing four separate print() statements?

student = {
    "name": "Tia",
    "course": "BCA",
    "city": "Jaipur",
    "skills": ["Python", "SQL", "Excel"]
}

for key in student:
    if key == 'skills':
        print("Skills:")
        for skill in student[key]:

            print(f"{skill}")
    else:
        print(f"{key}:{student[key]}")