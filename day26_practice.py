# Write a function:
# get_product_names(data)
# that:
# loops through data["products"]
# collects only the product names
# returns them as a list

data = {
    "products": [
        {"name": "Laptop", "price": 60000},
        {"name": "Mouse", "price": 800},
        {"name": "Keyboard", "price": 1500},
        {"name": "Monitor", "price": 12000}
    ]
}

def get_product_names(data):
    product_names = []
    for product in data['products']:
        product_names.append(product["name"])
    return product_names

print(get_product_names(data))

#Exercise 2
# Using the same data, write:
# get_expensive_products(data)
# Requirements:
# Loop through data["products"]
# Only select products with price greater than 10,000
# Add their names to a new list
# Return the list

def get_expensive_products(data):
    product_names = []
    for product in data['products']:
        if product['price'] > 10000:
            product_names.append(product['name'])
    return product_names

print(get_expensive_products(data))

# #Exercise 3
# Using the same data, write:
# get_expensive_product_details(data)
# For products costing more than ₹10,000, collect their name and price.

def get_expensive_product_details(data):
    product_details = []
    for product in data['products']:
        if product['price'] > 10000:
            tuple_d = (product['name'],product['price'])
            product_details.append(tuple_d)
    return product_details

print(get_expensive_product_details(data))

#Exercise 4: Actual API
# Write a function:
# get_users(url)
# Requirements:
# Make a GET request using requests.get().
# Use a 5-second timeout.
# Check for HTTP errors.
# Convert the response to JSON.
# Loop through the users.
# Collect the names of users whose id is greater than 5.
# Return the list.
# Expected result should be the names of users with IDs 6–10.

import requests
def get_users(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()

        data = response.json()
        user_names = []
        for user in data:
            if user['id'] > 5:
                user_names.append(user['name'])
        return user_names

    except requests.exceptions.Timeout:
        return "Request timed out"

    except requests.exceptions.HTTPError:
        return "HTTP error"

if __name__ == '__main__':
    print(get_users('https://jsonplaceholder.typicode.com/users'))

#Exercise 5
# https://jsonplaceholder.typicode.com/posts
# Write a function:
# get_user_posts(url, user_id)
# Requirements:
# Make a GET request.
# Use params to send userId.
# Use a 5-second timeout.
# Check for HTTP errors.
# Convert the response to JSON.
# Loop through the returned posts.
# Collect the titles into a list.
# Return that list.
# Handle timeout and HTTP errors as before.

import requests
def get_user_posts(url, user_id):
    try:
        titles = []
        params = {
        "userId": user_id }
        response = requests.get(url,timeout=5,params=params)
        response.raise_for_status()
        data = response.json()
        print(type(data))
        for user in data:
            titles.append(user['title'])
        return titles

    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.HTTPError:
        return 'HTTP error'

if __name__ == "__main__":
    print(get_user_posts("https://jsonplaceholder.typicode.com/posts", 2))

#Exercise 6: Multiple Query Parameters
# Create a function:
# get_filtered_posts(url, user_id, post_id)
# It should:
# Send a GET request to:
# https://jsonplaceholder.typicode.com/posts
# Use both query parameters:
# userId
# id
# Set a timeout of 5 seconds
# Use raise_for_status()
# Convert the response to JSON.
# Return the title of the matching post.
# Handle:
# Timeout → "Request timed out"
# HTTPError → "HTTP error"

import requests
url = 'https://jsonplaceholder.typicode.com/posts'
def get_filtered_posts(url, user_id, post_id):
    try:
        params = {
            "userId" : user_id,
            "id" : post_id
        }
        response = requests.get(url,timeout=5,params=params)
        response.raise_for_status()
        data = response.json()
        titles = []
        for post in data:
            titles.append(post['title'])
        return titles

    except requests.exceptions.HTTPError:
        return 'HTTP Error'
    except requests.exceptions.Timeout:
        return 'Request timed out'

if __name__ == '__main__':
    print(get_filtered_posts(url,2,12))

# Exercise 7: API Data + Filtering
# get_completed_tasks(url)
# Use this API:
# https://jsonplaceholder.typicode.com/todos
# Your function should:
# Send a GET request with a 5-second timeout.
# Use raise_for_status().
# Convert the response to JSON.
# Loop through the returned todos.
# Find todos where:
# completed is True
# id is greater than 20
# Collect their titles in a list.
# Return the list.
# Handle Timeout and HTTPError like the previous exercises.

import requests
url = 'https://jsonplaceholder.typicode.com/todos'
def get_completed_tasks(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        title_list = []
        for i in data:
            if i['id'] > 20 and i['completed'] == True:
                title_list.append(i['title'])
        return title_list
    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.HTTPError:
        return 'HTTP Error'

if __name__ == '__main__':
    print(get_completed_tasks(url))
        
# #Exercise 8
# Use:
# https://jsonplaceholder.typicode.com/todos
# Create:
# get_completed_count(url)

# Requirements:
# Send a GET request with timeout=5.
# Use raise_for_status().
# Convert the response to JSON.
# Loop through the todos.

# Count how many todos have:
# completed == True
# Return the count.
# Handle Timeout and HTTPError.

import requests
url = 'https://jsonplaceholder.typicode.com/todos'
def get_completed_count(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        count = 0
        for todo in data:
            if todo['completed'] == True:
                count+=1
        return count
    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.HTTPError:
        return 'HTTP Error'

if __name__ == '__main__':
    print(get_completed_count(url))

#Exercise 9: API Data Transformation
# Use:
# https://jsonplaceholder.typicode.com/users

# Create:
# get_user_emails(url)

# Requirements:
# Send a GET request with timeout=5.
# Use raise_for_status().
# Convert the response to JSON.
# Loop through the users.
# Collect the email addresses of users whose id is greater than 5.
# Return the list of emails.
# Handle Timeout and HTTPError.

import requests
url = 'https://jsonplaceholder.typicode.com/users'
def get_user_emails(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        email_list = []
        for user in data:
            if user['id'] > 5:
                email_list.append(user['email'])
        return email_list
    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.HTTPError:
        return 'HTTP Error'

if __name__ == '__main__':
    print(get_user_emails(url))

# Use:
# https://jsonplaceholder.typicode.com/posts

# Create:
# get_user_post_titles(url, user_id)

# Requirements:
# Send a GET request with timeout=5.
# Use raise_for_status().
# Convert the response to JSON.
# Use userId as a query parameter to get posts for the specified user.
# From the returned posts, collect only titles whose title length is greater than 30 characters.
# Return the list of matching titles.
# Handle:
# Timeout → "Request timed out"
# HTTPError → "HTTP Error"

import requests
url = 'https://jsonplaceholder.typicode.com/posts'
def get_user_post_titles(url, user_id):
    try:
        params = {'userId':user_id}
        response = requests.get(url,timeout=5,params=params)
        response.raise_for_status()
        data = response.json()
        titlelist = []
        for post in data:
            if len(post['title']) > 30:
                titlelist.append(post['title'])
        return titlelist
    except requests.exceptions.Timeout:
        return 'Request timed out'
    except requests.exceptions.HTTPError:
        return 'HTTP Error'

if __name__ == '__main__':
    print(get_user_post_titles(url,2))

