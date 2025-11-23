import requests
import json
import sys

def fetch_and_parse_user_data(username):
    """
    Fetches user data from the GitHub API, parses the sjon resopnse,
    and prints key information.
    """
    api_url = f"https://api.github.com/users/{username}"
    print(f"Fetching data from: {username} ----")
    
    try:
        # 1. Make the request with a timeout
        response = requests.get(api_url, timeout=5)
        
        # 2. check for bad status codes (4xx, 5xx)
        response.raise_for_status()
        
        # 3. parse the JSON response directly into a Python dictionary
        # This is the core data parsing step for API responses
        user_data = response.json()
        
        # 4. Access and print specific values from the dictionary
        # We use .get() for safe access, providing a default value if the key is not found
        print(f"Username: {user_data.get('login', 'N/A')}")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Public Repositories: {user_data.get('public_repos', 0)}")
        print(f"Followers: {user_data.get('followers', 0)}")
        print("-" * 20)
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Error: User '{username}' not found on GitHub.")
        else:
            print(f"Error: HTTP error {response.status_code} from GitHub API.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    
# Run the script with various examples
if __name__ == "__main__":
    fetch_and_parse_user_data("yuswitayudi")
    fetch_and_parse_user_data("google")
    fetch_and_parse_user_data("nonexistent-user")