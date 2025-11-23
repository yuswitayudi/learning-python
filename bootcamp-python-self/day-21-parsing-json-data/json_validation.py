#!/usr/bin/env python3
"""
JSON Validation and Error Handling Examples
This script demonstrates robust JSON parsing with comprehensive error handling,
data validation, and schema checking.
"""

import json
import os
from typing import Dict, List, Any, Optional, Union
from datetime import datetime

class JSONValidator:
    """A class for validating JSON data against expected schemas."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_user_schema(self, user: Dict[str, Any]) -> bool:
        """Validate a user object against expected schema."""
        is_valid = True
        
        # Required fields
        required_fields = ['id', 'name', 'email', 'age', 'is_active']
        for field in required_fields:
            if field not in user:
                self.errors.append(f"Missing required field: {field}")
                is_valid = False
        
        # Type validations
        if 'id' in user and not isinstance(user['id'], int):
            self.errors.append("Field 'id' must be an integer")
            is_valid = False
        
        if 'name' in user and not isinstance(user['name'], str):
            self.errors.append("Field 'name' must be a string")
            is_valid = False
        
        if 'email' in user and not isinstance(user['email'], str):
            self.errors.append("Field 'email' must be a string")
            is_valid = False
        
        if 'age' in user and not isinstance(user['age'], int):
            self.errors.append("Field 'age' must be an integer")
            is_valid = False
        
        if 'is_active' in user and not isinstance(user['is_active'], bool):
            self.errors.append("Field 'is_active' must be a boolean")
            is_valid = False
        
        # Value validations
        if 'age' in user and (user['age'] < 0 or user['age'] > 150):
            self.warnings.append(f"Age {user['age']} seems unusual")
        
        if 'email' in user and '@' not in user['email']:
            self.errors.append(f"Invalid email format: {user['email']}")
            is_valid = False
        
        return is_valid
    
    def validate_address_schema(self, address: Dict[str, Any]) -> bool:
        """Validate an address object."""
        is_valid = True
        required_fields = ['street', 'city', 'state', 'zipcode']
        
        for field in required_fields:
            if field not in address:
                self.errors.append(f"Address missing required field: {field}")
                is_valid = False
            elif not isinstance(address[field], str):
                self.errors.append(f"Address field '{field}' must be a string")
                is_valid = False
        
        return is_valid
    
    def validate_hobbies(self, hobbies: List[str]) -> bool:
        """Validate hobbies list."""
        if not isinstance(hobbies, list):
            self.errors.append("Hobbies must be a list")
            return False
        
        for hobby in hobbies:
            if not isinstance(hobby, str):
                self.errors.append(f"All hobbies must be strings, found: {type(hobby)}")
                return False
        
        return True
    
    def get_validation_summary(self) -> Dict[str, Any]:
        """Get a summary of validation results."""
        return {
            'is_valid': len(self.errors) == 0,
            'error_count': len(self.errors),
            'warning_count': len(self.warnings),
            'errors': self.errors,
            'warnings': self.warnings
        }

def safe_json_load(filename: str) -> Optional[Dict[str, Any]]:
    """Safely load JSON file with comprehensive error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in '{filename}'")
        print(f"   Line {e.lineno}, Column {e.colno}: {e.msg}")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied accessing '{filename}'")
        return None
    except UnicodeDecodeError as e:
        print(f"❌ Error: File encoding issue in '{filename}': {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error loading '{filename}': {e}")
        return None

def validate_json_file(filename: str) -> bool:
    """Validate a JSON file against expected schema."""
    print(f"\n=== Validating {filename} ===\n")
    
    data = safe_json_load(filename)
    if data is None:
        return False
    
    validator = JSONValidator()
    
    # Validate top-level structure
    if 'users' not in data:
        validator.errors.append("Missing 'users' key in root object")
    else:
        users = data['users']
        if not isinstance(users, list):
            validator.errors.append("'users' must be a list")
        else:
            # Validate each user
            for i, user in enumerate(users):
                print(f"Validating user {i + 1}...")
                if not validator.validate_user_schema(user):
                    print(f"  ❌ User {i + 1} validation failed")
                else:
                    print(f"  ✅ User {i + 1} validation passed")
                
                # Validate address if present
                if 'address' in user:
                    if not validator.validate_address_schema(user['address']):
                        print(f"  ❌ User {i + 1} address validation failed")
                    else:
                        print(f"  ✅ User {i + 1} address validation passed")
                
                # Validate hobbies if present
                if 'hobbies' in user:
                    if not validator.validate_hobbies(user['hobbies']):
                        print(f"  ❌ User {i + 1} hobbies validation failed")
                    else:
                        print(f"  ✅ User {i + 1} hobbies validation passed")
    
    # Print validation summary
    summary = validator.get_validation_summary()
    print(f"\nValidation Summary:")
    print(f"  Valid: {'✅ Yes' if summary['is_valid'] else '❌ No'}")
    print(f"  Errors: {summary['error_count']}")
    print(f"  Warnings: {summary['warning_count']}")
    
    if summary['errors']:
        print(f"\nErrors:")
        for error in summary['errors']:
            print(f"  - {error}")
    
    if summary['warnings']:
        print(f"\nWarnings:")
        for warning in summary['warnings']:
            print(f"  - {warning}")
    
    return summary['is_valid']

def test_invalid_json():
    """Test handling of invalid JSON data."""
    print("\n=== Testing Invalid JSON Handling ===\n")
    
    # Create a file with invalid JSON
    invalid_json_content = '''
    {
        "users": [
            {
                "id": "not_a_number",
                "name": "John Doe",
                "email": "invalid_email",
                "age": -5,
                "is_active": "not_boolean",
                "address": {
                    "street": "123 Main St",
                    "city": "New York"
                    // Missing state and zipcode
                },
                "hobbies": ["reading", 123, "swimming"]
            }
        ]
    }
    '''
    
    with open('invalid_sample.json', 'w') as file:
        file.write(invalid_json_content)
    
    print("Created invalid JSON file for testing...")
    validate_json_file('invalid_sample.json')
    
    # Clean up
    os.remove('invalid_sample.json')
    print("\nCleaned up test file.")

def create_json_schema():
    """Create a JSON schema for validation."""
    print("\n=== Creating JSON Schema ===\n")
    
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "minimum": 1},
                        "name": {"type": "string", "minLength": 1},
                        "email": {"type": "string", "format": "email"},
                        "age": {"type": "integer", "minimum": 0, "maximum": 150},
                        "is_active": {"type": "boolean"},
                        "address": {
                            "type": "object",
                            "properties": {
                                "street": {"type": "string"},
                                "city": {"type": "string"},
                                "state": {"type": "string"},
                                "zipcode": {"type": "string"}
                            },
                            "required": ["street", "city", "state", "zipcode"]
                        },
                        "hobbies": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["id", "name", "email", "age", "is_active"]
                }
            },
            "metadata": {
                "type": "object",
                "properties": {
                    "total_users": {"type": "integer", "minimum": 0},
                    "last_updated": {"type": "string"},
                    "version": {"type": "string"}
                }
            }
        },
        "required": ["users"]
    }
    
    with open('user_schema.json', 'w') as file:
        json.dump(schema, file, indent=2)
    
    print("✅ Created JSON schema file: user_schema.json")
    print("This schema can be used with libraries like jsonschema for validation.")

def performance_test():
    """Test JSON parsing performance with large data."""
    print("\n=== Performance Test ===\n")
    
    # Create a large JSON file
    large_data = {
        "users": []
    }
    
    # Generate 1000 users
    for i in range(1000):
        user = {
            "id": i + 1,
            "name": f"User {i + 1}",
            "email": f"user{i + 1}@example.com",
            "age": 20 + (i % 50),
            "is_active": i % 2 == 0,
            "address": {
                "street": f"{i + 1} Main St",
                "city": f"City {i % 10}",
                "state": f"ST{i % 5}",
                "zipcode": f"{10000 + i}"
            },
            "hobbies": [f"hobby{j}" for j in range(i % 5 + 1)]
        }
        large_data["users"].append(user)
    
    # Save large file
    with open('large_data.json', 'w') as file:
        json.dump(large_data, file)
    
    print(f"Created large JSON file with {len(large_data['users'])} users")
    
    # Test loading performance
    import time
    start_time = time.time()
    
    with open('large_data.json', 'r') as file:
        loaded_data = json.load(file)
    
    end_time = time.time()
    load_time = end_time - start_time
    
    print(f"✅ Loaded {len(loaded_data['users'])} users in {load_time:.4f} seconds")
    print(f"   Average: {load_time / len(loaded_data['users']) * 1000:.4f} ms per user")
    
    # Clean up
    os.remove('large_data.json')
    print("Cleaned up large test file.")

def main():
    """Main function to run all validation examples."""
    print("JSON Validation and Error Handling Examples")
    print("=" * 60)
    
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Run examples
    validate_json_file('sample_data.json')
    test_invalid_json()
    create_json_schema()
    performance_test()
    
    print("\n" + "=" * 60)
    print("All validation examples completed!")

if __name__ == "__main__":
    main()


