# Create a function it should return using *args
#output should have :
#     "count": ...,
#     "sum": ...,
#     "largest": ...,
#     "smallest": ...,
#     "even_count": ...,
#     "odd_count": ...

def analyze_numbers(*args):
    count = 0
    total = 0
    largest = args[0]
    smallest = args[0]
    even_count = 0
    odd_count = 0

    for i in args:
        count+=1
        total+= i
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
        if i%2==0:
            even_count +=1
        if i%2!=0:
            odd_count+=1
    return {"count":count,"total":total,"largest":largest,"smallest":smallest,"even_count":even_count,"odd_count":odd_count}

print(analyze_numbers(-10, -20, -5))   

# Write a function:
# The function receives any number of strings.
# It should return a dictionary containing:
# total_words → total number of strings received
# longest → longest string
# shortest → shortest string
# total_characters → total characters across all strings
# uppercase_count → number of strings that are completely uppercase
# lowercase_count → number of strings that are completely lowercase
# Rules
# Use *args
# Don't use max() or min()
# Don't use len(args) for total_words; count using your loop
# The comparison for longest/shortest must work regardless of the order of the inputs
# Return a dictionary
# Don't print inside the function

def analyze_text(*args):
    total_words = 0
    longest = args[0]
    shortest = args[0]
    total_characters = 0
    uppercase_count = 0
    lowercase_count = 0

    for i in args:
        total_words+=1
        total_characters += len(i)
        if len(longest)<len(i):
            longest = i
        if len(shortest)>len(i):
            shortest = i
        if i.isupper():
            uppercase_count+=1
        if i.islower():
            lowercase_count+=1
    
    return {"total_words":total_words,"total_characters":total_characters,"longest":longest,"shortest":shortest,"uppercase_count":uppercase_count,"lowercase_count":lowercase_count}


print(analyze_text("Python", "SQL", "DATA", "science"))

# Write:
# The function receives product names and prices as keyword arguments.
# Example:
# filter_products(
#     apple=50,
#     banana=30,
#     orange=80,
#     mango=120
# )
# Return a dictionary containing only products priced above 50.
# Expected:

# {
#     "orange": 80,
#     "mango": 120
# }
# Rules
# Use **kwargs
# Don't use dictionary comprehension
# Don't modify the original kwargs
# Return a new dictionary
# Don't print inside the function


def filter_products(**kwargs):
    products = {}
    for key,value in kwargs.items():
        if value>50:
            products[key] = value
    return products

print(filter_products(
    apple=50,
    banana=30,
    orange=80,
    mango=120
))


# Build:
# def calculate(*args, **kwargs):
# The function receives:
# positional numbers through args
# named options through kwargs
# Example:
# calculate(10, 20, 30, operation="sum")
# should return: 60 And:
# calculate(10, 20, 30, operation="average")
# should return: 20
# It should support these operations:
# "sum"
# "average"
# "largest"
# "smallest"
# Requirements
# Use *args for the numbers.
# Use **kwargs for the operation.
# Do not use sum(), max(), or min().
# Return the result.
# Don't print inside the function.
# Assume the caller provides a valid operation.

def calculate(*args, **kwargs):
    total = 0
    largest = args[0]
    smallest = args[0]
    for i in args:
        total+=i
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    operation = kwargs["operation"]
    if operation == "sum":
        return total
    elif operation == "average":
        return total / len(args)
    elif operation == "largest":
        return largest
    elif operation == "smallest":
        return smallest

print(calculate(10, 20, 30, operation="sum"),
calculate(10, 20, 30, operation="average"),
calculate(10, 20, 30, operation="largest"),
calculate(10, 20, 30, operation="smallest"))

# Write:
# def summarize_students(*args, **kwargs):
# Each positional argument is a student's marks.
# The function should return a dictionary containing:
# total_students
# passed
# failed
# average
# highest
# lowest
# Requirements
# Use *args for marks.
# Use **kwargs for passing_mark.
# Don't use sum(), max(), or min().
# Calculate everything using your own loop.
# Use the supplied passing_mark rather than hardcoding 40.
# Return a dictionary.
# Don't print inside the function.
# Your solution should also work if the passing mark changes.
# Test it with:
# summarize_students(35, 50, 72, 20, 90, passing_mark=40)
# Expected logic:
# 3 passed
# 2 failed

def summarize_students(*args, **kwargs):
    passing_mark = kwargs["passing_mark"]
    total_students = 0
    total = 0
    passed = 0
    failed = 0
    highest = args[0]
    lowest = args[0]
    for i in args:
        total += i
        total_students+=1
        if i >= passing_mark:
            passed += 1
        else:
            failed += 1
        if highest<i:
            highest = i
        if lowest > i:
            lowest = i
    average = total/len(args)
    
    return {"total_students":total_students,"passed":passed,"failed":failed,"average":average,"highest":highest,"lowest":lowest}

print(summarize_students(35, 40, 72, 20, 90, passing_mark=40))

# Write:
# def analyze_scores(*args):
# It should return:
# {
#     "count": ...,
#     "average": ...,
#     "highest": ...,
#     "lowest": ...
# }
# But there is one requirement:
# If the function receives no scores, it must return:
# {
#     "count": 0,
#     "average": 0,
#     "highest": None,
#     "lowest": None
# }
# No sum(), max(), or min().

def analyze_scores(*args):
    if not args:
        return {        
        "count": 0,
        "average": 0,
        "highest": None,
        "lowest": None
        } 
    count = 0
    total = 0
    highest = args[0]
    lowest = args[0]
    for score in args:    
        count+=1
        total+=score 
        if highest < score:
            highest = score
        if lowest > score:
            lowest = score
    average = total/count
    return {"count":count,"average":average,"highest":highest,"lowest":lowest}
print(analyze_scores())


# Day 17 — Mini Challenge 🧠
# building a small sales analysis function.
# Write:
# def analyze_sales(*args, **kwargs):
# Input
# *args → sales amounts
# **kwargs → options
# Example:
# analyze_sales(
#     1200, 800, 1500, 600, 2000,
#     target=1000
# )
# Return a dictionary containing:
# total_sales
# average_sale
# highest_sale
# lowest_sale
# sales_above_target
# sales_below_target
# target_reached
# Requirements
# Use *args and **kwargs.
# Don't use sum(), max(), or min().
# Don't hardcode the target.
# Handle negative numbers correctly.
# Handle no sales without an error.
# Return a dictionary.
# Don't print inside the function.


def analyze_sales(*args, **kwargs):
    if not args:
        return{
        "total_sales":0,
        "average_sale":0,
        "highest_sale":None,
        "lowest_sale":None,
        "sales_above_target":0,
        "sales_below_target":0,
        "target_reached":False            
        }
    total_sales = 0
    total = 0
    highest_sale = args[0]
    lowest_sale = args[0]
    sales_above_target = 0
    sales_below_target = 0
    target_reached = False
    target = kwargs["target"]
    for i in args:
        total_sales+=1
        total+=i
        if i > highest_sale:
            highest_sale = i
        if i < lowest_sale:
            lowest_sale = i
        if i > target:
            sales_above_target+=1
        if i < target:
            sales_below_target+=1
        if i >= target:
            target_reached = True
    average_sale = total/total_sales
    return{
        "total_sales":total_sales,
        "average_sale":average_sale,
        "highest_sale":highest_sale,
        "lowest_sale":lowest_sale,
        "sales_above_target":sales_above_target,
        "sales_below_target":sales_below_target,
        "target_reached":target_reached
    }

print(analyze_sales(1000,500,1500, target=1000))