import requests

# SRE/DevOps relevance: Triggering a webhook, sneding metics or creating a resources via API
print("Making a POST request")

post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data, timeout=5)
    response.raise_for_status()  # Raise an error for bad responses
    
    print(f"status code: {response.status_code}")  # Print the HTTP status code
    print(f"Content Type: {response.headers['Content-Type']}")  # Print the content type of the response
    print("Response JSON:", response.json())  # Print the JSON
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")