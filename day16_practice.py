# Exercise 
# Call this function using keyword arguments with:
# name   → Sara
# role   → Developer
# salary → 50000

def employee(name, role, salary):
    print(name)
    print(role)
    print(salary)

employee(name = 'Sara',role = 'developer', salary = 50000)

#Write a function:It should print:
# Hello Mina . When called 

def greet(name, message="Hello"):
    print ( message,name)
greet("Mina",'Welcome ')


#Exercise — Default argument practice

def calculate(price, tax=10):
    return price + tax

print(calculate(100))
print(calculate(100, 20))

# Exercise  - 
# It should return the number raised to the given exponent.

def power(number,exponent=2):
    return number**exponent
print(power(10))
print(power(10,3))

# Exercise
# Write this function:
# It should return the sum of all the numbers passed to it.

def total(*args):
    total = 0
    for i in args:
        total +=i
    return total
print(total(5, 10, 15, 20))

# Exercise: Write a function called largest(*args) that returns the largest number passed to it.

def largest(*args):
    largest_number = 0
    for i in args:
        if i > largest_number:
            largest_number = i
    return largest_number
print(largest(10,20,3000))

#Exercise — Fix the negative-number problem

def largest(*args):
    largest_number = args[0]
    for i in args:
        if i > largest_number:
            largest_number = i
    return largest_number
print(largest(-10, -20, -3))

# Write a function:
# It should:
# Print all positional arguments.
# Print all keyword arguments.

def student_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

student_info("Python", "SQL", name="Ali", age=23)