import requests

# SRE/DevOps relevance: checking a service's health endpoint
print("Making a GET request to a public API...")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    
    print(f"Status Code: {response.status_code}")  # Print the HTTP status code
    print(f"Context Type: {response.headers['Content-Type']}")  # Print the content type of the response
    print("Response JSON:", response.json())  # Print the JSON response content
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")