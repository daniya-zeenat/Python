# Exercise  — API + loop
# Suppose an API returns:

# {
#     "users": [
#         {"name": "Alex", "age": 25},
#         {"name": "Sara", "age": 28},
#         {"name": "John", "age": 30}
#     ]
# }

# Write a loop that prints only the names of users whose age is greater than 25.
# Expected output:
# Sara
# John

data = {
    "users": [
        {"name": "Alex", "age": 25},
        {"name": "Sara", "age": 28},
        {"name": "John", "age": 30}
    ]
}

for user in data["users"]:
    if user["age"] > 25:
        print(user["name"])

# Exercise 
# Using the same data, write a loop that prints:
# Alex - 25
# Sara - 28
# John - 30

data = {
    "users": [
        {"name": "Alex", "age": 25},
        {"name": "Sara", "age": 28},
        {"name": "John", "age": 30}
    ]
}

for user in data["users"]:
    print(user["name"] ,'-' ,user["age"])

# Exercise — API data + filtering
# Suppose the API returns:
# data = {
#     "products": [
#         {"name": "Laptop", "price": 60000},
#         {"name": "Mouse", "price": 800},
#         {"name": "Keyboard", "price": 1500},
#         {"name": "Monitor", "price": 12000}
#     ]
# }

# Write a loop that prints only products costing more than ₹10,000.
# Expected output:
# Laptop 60000
# Monitor 12000
    
data = {
    "products": [
        {"name": "Laptop", "price": 60000},
        {"name": "Mouse", "price": 800},
        {"name": "Keyboard", "price": 1500},
        {"name": "Monitor", "price": 12000}
    ]
}

for product in data["products"]:
    if product["price"] > 10000:
        print(product["name"],product["price"])

# Exercise — Mini Challenge
# Write a function:
# Requirements:
# Make a GET request with a 5-second timeout.
# Check for HTTP errors.
# Convert the response to JSON.
# Loop through data["users"].
# Collect the names of users aged 18 or above into a list.
# Return the list.
# Handle timeout and HTTP errors by returning:
# "Request timed out"
# "HTTP error"
# Example expected result:
# ["Sara", "Maya"]

import requests
def get_adult_names(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()

        data = response.json()
        adult_names = []
        for user in data["users"]:
            if user["age"] >=18:
                adult_names.append(user["name"])
        return adult_names

    except requests.exceptions.Timeout:
        return "Request timed out"
    
    except requests.exceptions.HTTPError:
        return "HTTP error"

