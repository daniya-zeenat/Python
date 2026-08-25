# Exercise 1 — Importing JSON 
import json
student = {
    "name": "Daniya",
    "age": 22,
    "skills": ["Python", "SQL"]
}
data = json.dumps(student)
print(data)
print(type(data))

# Exercise 2 — JSON back to Python
import json
data = '{"name": "Alex", "age": 25}'
student = json.loads(data)
print(student)
print(type(student))

# Exercise 3 — Accessing JSON data
import json
data = '{"name": "Alex", "age": 25, "skills": ["Python", "SQL"]}'
student = json.loads(data)
print(student["name"])
print(student["skills"][0])

# Exercise 4 — JSON files
import json

with open("Python\students.json", "r") as file:
    student = json.load(file)

print(student["name"])
print(student["skills"][1])

# Exercise 5 — dump()

import json

student = {
    "name": "Alex",
    "age": 25
}

with open("Python\students.json", "w") as file:
    json.dump(student, file)

# Exercise 6

import json

student = {
    "name": "Alex",
    "age": 25
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])

# Exercise 7 — Nested JSON

import json

data = '''
{
    "name": "Alex",
    "marks": {
        "Python": 85,
        "SQL": 92
    }
}
'''

student = json.loads(data)

print(student["marks"]["SQL"])

# Exercise 8 — JSON conversion

import json

student = {
    "name": "Alex",
    "age": 25,
    "passed": True,
    "skills": None
}

data = json.dumps(student)

print(data)

# Exercise 9
import json

data = '{"passed": true, "skills": null}'

student = json.loads(data)

print(student["passed"])
print(student["skills"])
print(type(student["passed"]))
print(type(student["skills"]))

# Exercise 10 — Final JSON challenge
# Write a function:
# It should:
# Open filename in write mode.
# Save the student dictionary as JSON using json.dump().
# Handle any FileNotFoundError by returning "File error".
# If successful, return "Student saved".

# Test it with:

# student = {
#     "name": "Alex",
#     "age": 25,
#     "skills": ["Python", "SQL"]
# }

import json
def save_student(filename, student):
    try:
        with open (filename,'w') as file:
            json.dump(student,file)
        return "Student saved"
    
    except FileNotFoundError:
        return ("File error")

student = {
    "name": "Alex",
    "age": 25,
    "skills": ["Python", "SQL"]
}    

print(save_student("student.json", student))

