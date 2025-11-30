import yaml
import tomlkit # We need this library for TOML manipulation
import os # Kept for good file handling practice

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# 1. Define the Python dictionary containing configuration data
service_config = {
    "name": "wallet-service",
    "port": 8080,
    "owner": "yudi",
    "allowed_hosts": ["localhost", "127.0.0.1", "::1"],
    "database": {
        "host": "db.prod.local",
        "timeout_seconds": 30
    }
}

print("Starting configuration file generation...")

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


# --- Part 2: Write to TOML (Using tomlkit) --- 
toml_filename = os.path.join(current_dir, "service_config.toml")
try:
    # Use tomlkit.dumps() to convert the Python dict to a TOML string.
    # tomlkit handles the conversion of nested dicts into [section] headers.
    toml_string = tomlkit.dumps(service_config)

    # Open the TOML file in write mode ('w').
    # The 'with' statement ensures the file is properly closed after its suite finishes.
    # Write the TOML formatted string to the file.
    with open(toml_filename, "w") as f:
        f.write(toml_string)
    print(f"-> Successfully created {toml_filename}")
except Exception as e:
    print(f"Error writing TOML file: {e}")

print("Configuration file generation complete.")