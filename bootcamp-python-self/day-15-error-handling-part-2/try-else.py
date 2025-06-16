# try-else.py
# Demonstrates the use of try-else for error handling in Python when making HTTP requests.
# The else block runs only if no exceptions are raised in the try block.

import requests

def fetch_service_status(url):
    """
    Attempts to fetch the status of a web service at the given URL.
    - Handles connection errors, timeouts, HTTP errors, and unexpected exceptions.
    - If the request is successful, prints the status and returns the JSON response.
    - Returns None if any error occurs.

    Args:
        url (str): The URL of the web service to check.

    Returns:
        dict or None: The JSON response from the service if successful, otherwise None.
    """
    print(f"Attempting to fetch service status from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
    except requests.exceptions.ConnectionError:
        print(f"Error: could not connect to service at {url}. Network issue?")
    except requests.exceptions.Timeout:
        print(f"Error: request to {url} timed out. Service slow or unresponsive?")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error {e.response.status_code} from {url}. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        # This block runs if no exceptions were raised in the try block
        print(f"Service at {url} is up and running! Status code: {response.status_code}")
        return response.json()
    return None

# Example usage:
# The first call (commented) is for a valid URL; the second is for an invalid URL to demonstrate error handling.
# fetch_service_status("https://jsonplaceholder.typicode.com/posts/1")  # Valid URL
fetch_service_status("http://yuswitayudi.site")  # Invalid URL (assuming this is not a valid service)