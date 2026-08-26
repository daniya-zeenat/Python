import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

age = int(row[1])

# Exercise 2 — Skipping the header
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)

# Exercise 3
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Employee:", row)

# Exercise 4 — Accessing columns
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        age = int(row[1])

        print(name, age)

# # Exercise 5 — Finding employees by age
# Write a program that prints only employees whose age is greater than 25.
# Expected output:
# Sara 28
# John 30

import csv

with open ("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        name = row[0]
        age = int(row[1])
        if age > 25:
            print(name,age)

# Exercise 6: Writing CSV Files
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Alex", 25])
    writer.writerow(["Sara", 28])

# Exercise 7 — Writing multiple rows
import csv

employees = [
    ["name", "age"],
    ["Alex", 25],
    ["Sara", 28],
    ["John", 30]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)

# Exercise 8 — CSV + dictionaries
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["department"])

# Exercise 9 — Why DictReader is useful
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        age = int(row["age"])

        if age > 25:
            print(row["name"])

# Exercise 10 — Final Day 24 challenge
# Create a function:
# The CSV contains:
# name,department,salary
# Alex,IT,50000
# Sara,HR,45000
# John,Finance,65000
# Maya,IT,70000
# Your function should:
# Read the CSV using csv.DictReader.
# Convert salary to an integer.
# Print the name and salary of employees whose salary is greater than min_salary.
# Test it with:
# filter_employees("employees.csv", 60000)
# Expected output:
# John 65000
# Maya 70000

import csv
def filter_employees(filename, min_salary):
    with open (filename,'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            salary = int(row["salary"])
            if salary > min_salary:
                print(row["name"],row["salary"])

filter_employees("employees.csv", 60000)



