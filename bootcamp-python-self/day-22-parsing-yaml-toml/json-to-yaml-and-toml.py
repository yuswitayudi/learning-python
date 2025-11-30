import yaml
import tomlkit # We need this library for TOML manipulation
import os # Kept for good file handling practice
import json
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Define the input JSON file path by joining the current directory with the filename
json_filename = os.path.join(current_dir, "config_input.json")

def read_json_file():
    # This function reads a JSON file and returns its content as a Python dictionary.

    """
    Reads configuration data from a local json file using json.load()
    and returns it as a Python dictionary.
    """
    try:
        # use 'with open' for safe file handling
        with open(json_filename, 'r') as f:
            config_data = json.load(f)
            print(f"-> Successfully loaded config for services: {config_data.get('name', 'Uknown')}")
            return config_data # Return the loaded dictionary
    except FileNotFoundError:
        print(f"Error: Input file {json_filename} not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {json_filename}. Detail: {e}")
        sys.exit(1) # Exit the script if JSON is invalid
    except Exception as e:
        print(f"An unexpected error occurred while reading JSON: {e}")
        sys.exit(1) # Exit on any other unexpected errors

            
def write_config_files(service_config):
    # This function takes a Python dictionary (service_config) and writes it
    # to both YAML and TOML files.

    # --- YAML File Generation ---
    # --- Part 1: Write to YAML (Using PyYAML) ---
    yaml_filename = os.path.join(current_dir, "service_config.yaml")
    try:
        with open(yaml_filename, "w") as f:
            # Use yaml.dump() to write the Python dictionary to a YAML file.
            # sort_keys=False preserves the order in the output file.
            yaml.dump(service_config, f, sort_keys=False)
        print(f"-> Successfully created {yaml_filename}")
    except Exception as e:
        print(f"Error writing YAML file: {e}")

    # --- TOML File Generation ---

    # --- Part 2: Write to TOML (Using tomlkit) ---
    toml_filename = os.path.join(current_dir, "service_config.toml")
    try:
        # Use tomlkit.dumps() to convert the Python dict to a TOML string.
        # tomlkit handles the conversion of nested dicts into [section] headers.
        toml_string = tomlkit.dumps(service_config)

        # Open the TOML file in write mode and write the string
        with open(toml_filename, "w") as f:
            f.write(toml_string)
        print(f"-> Successfully created {toml_filename}")
    except Exception as e:
        print(f"Error writing TOML file: {e}")

    # Indicate completion of file generation
    print("Configuration file generation complete.")
    
if __name__ == "__main__":
    # This block runs when the script is executed directly.
    loaded_config = read_json_file()
    # Only proceed to write files if loaded_config is not empty (i.e., no error occurred)
    if loaded_config:
        write_config_files(loaded_config)