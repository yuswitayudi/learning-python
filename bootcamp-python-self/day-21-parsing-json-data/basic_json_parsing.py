#!/usr/bin/env python3
"""
Basic JSON Parsing Examples
This script demonstrates fundamental JSON parsing operations in Python.
"""

import json
import os

def load_json_file(filename):
    """Load and parse a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filename}': {e}")
        return None
    except Exception as e:
        print(f"Error loading '{filename}': {e}")
        return None

def save_json_file(filename, data):
    """Save data to a JSON file with pretty formatting."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"Data saved to '{filename}'")
    except Exception as e:
        print(f"Error saving to '{filename}': {e}")

def basic_parsing_example():
    """Demonstrate basic JSON parsing operations."""
    print("=== Basic JSON Parsing Example ===\n")
    
    # Load sample data
    data = load_json_file('sample_data.json')
    if data is None:
        return
    
    print("1. Loaded JSON data structure:")
    print(f"   Type: {type(data)}")
    print(f"   Keys: {list(data.keys())}")
    print()
    
    # Access nested data
    print("2. Accessing nested data:")
    users = data['users']
    print(f"   Number of users: {len(users)}")
    print(f"   First user name: {users[0]['name']}")
    print(f"   First user email: {users[0]['email']}")
    print()
    
    # Access nested objects
    print("3. Accessing nested objects:")
    first_user_address = users[0]['address']
    print(f"   First user's city: {first_user_address['city']}")
    print(f"   First user's state: {first_user_address['state']}")
    print()
    
    # Access arrays
    print("4. Accessing arrays:")
    first_user_hobbies = users[0]['hobbies']
    print(f"   First user's hobbies: {first_user_hobbies}")
    print(f"   Number of hobbies: {len(first_user_hobbies)}")
    print(f"   First hobby: {first_user_hobbies[0]}")
    print()
    
    # Access metadata
    print("5. Accessing metadata:")
    metadata = data['metadata']
    print(f"   Total users: {metadata['total_users']}")
    print(f"   Last updated: {metadata['last_updated']}")
    print(f"   Version: {metadata['version']}")

def json_string_parsing():
    """Demonstrate parsing JSON from strings."""
    print("\n=== JSON String Parsing Example ===\n")
    
    # JSON string
    json_string = '''
    {
        "name": "Alice",
        "age": 28,
        "city": "Boston",
        "is_student": true,
        "grades": [85, 92, 78, 96]
    }
    '''
    
    try:
        # Parse JSON string
        data = json.loads(json_string)
        print("1. Parsed JSON string:")
        print(f"   Name: {data['name']}")
        print(f"   Age: {data['age']}")
        print(f"   City: {data['city']}")
        print(f"   Is student: {data['is_student']}")
        print(f"   Grades: {data['grades']}")
        print(f"   Average grade: {sum(data['grades']) / len(data['grades']):.1f}")
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON string: {e}")

def create_and_save_json():
    """Demonstrate creating and saving JSON data."""
    print("\n=== Creating and Saving JSON Example ===\n")
    
    # Create a Python dictionary
    student_data = {
        "students": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "major": "Computer Science",
                "gpa": 3.8,
                "courses": ["Python Programming", "Data Structures", "Algorithms"]
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "major": "Mathematics",
                "gpa": 3.6,
                "courses": ["Calculus", "Linear Algebra", "Statistics"]
            }
        ],
        "school_info": {
            "name": "University of Example",
            "year_established": 1950,
            "total_students": 15000
        }
    }
    
    # Save to JSON file
    save_json_file('student_data.json', student_data)
    
    # Verify by loading it back
    loaded_data = load_json_file('student_data.json')
    if loaded_data:
        print("2. Verification - loaded data:")
        print(f"   Number of students: {len(loaded_data['students'])}")
        print(f"   School name: {loaded_data['school_info']['name']}")

def main():
    """Main function to run all examples."""
    print("JSON Parsing Examples")
    print("=" * 50)
    
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run examples
    basic_parsing_example()
    json_string_parsing()
    create_and_save_json()
    
    print("\n" + "=" * 50)
    print("All examples completed!")

if __name__ == "__main__":
    main()


