#Exercise - Timeout
import requests

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.HTTPError:
    print("HTTP error")

# Exercise  — Query parameters
import requests

params = {
    "city": "Hyderabad",
    "units": "metric"
}

response = requests.get(url, params=params)

#Exercise  — Headers
headers = {
    "Authorization": "Bearer abc123"
}

response = requests.get(url, headers=headers)

# Write a function:
# It should:
# Make a GET request to url.
# Set a timeout of 5 seconds.
# Raise an HTTP error if the status isn't successful.
# Return the JSON response.
# Handle:
# Timeout → return "Request timed out"
# HTTPError → return "HTTP error"

import requests
def get_user(url):
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.HTTPError:
        return "HTTP error"

