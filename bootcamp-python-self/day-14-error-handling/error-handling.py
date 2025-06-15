# Basic try-except for potentially risky operations
try:
    # Imagine this is a risky operation that might fail
    # If service down it migh raise an error
    result = 10 / 0  # This will raise a ZeroDivisionError
    print(f"Operation successful: {result}")
except:
    print("An error occurred during the operation.")
    # In SRE/DevOps, you would log this error and possibly alert.
    
# Handling specific exceptions
import json

def parse_server_config(config_string):
    """
    Tries to parse a server configuration string (simulating an API response or file content).
    Handles specific parsing errors and demonstrates SRE/DevOps-style error handling.
    Args:
        config_string (str): JSON string representing server config.
    Returns:
        dict: Parsed config if successful, None otherwise.
    """
    try:
        # Try to parse the JSON string
        config_data = json.loads(config_string) # might raise json.JSONDecodeError if not valid JSON
        # Try to access the 'name' key in the parsed dictionary
        server_name = config_data["name"] # might raise KeyError if "name" is not in the JSON
        print(f"Successfully config for server: {server_name}")
        return config_data
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in configuration string. Check syntax!")
        # SRE action: Log this as a configuration syntax error, trigger alert.
    except KeyError as e:
        print(f"Error: Missing expected key '{e}' in configuration data. Schema mismatch!")
        # SRE action: Log as a schema error, notify development.
    except Exception as e:
        print(f"An unexpected error occurred during config parsing: {e}")
        # SRE action: log full traceback for debugging, general alert.

print("\n--- SRE/DevOps Example: Parsing Server Config ---")
# Example 1: Valid JSON, all expected keys present
parse_server_config('{"name": "web-01", "ip": "192.168.1.1"}') # Valid JSON
# Example 2: Invalid JSON (missing closing brace)
parse_server_config('{"name": "web-02", "ip": "192.168.1.2",') # Invalid JSON
# Example 3: Valid JSON, but missing 'name' key
parse_server_config('{"ip": "192.168.1.3"}') # Missing 'name' key
# Example 4: JSON 'null' (not a dict, will cause KeyError)
parse_server_config('null')