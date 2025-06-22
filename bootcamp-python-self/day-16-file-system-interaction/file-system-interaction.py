# file-system-interaction.py
# Demonstrates basic file system interactions in Python: reading, writing, and appending to files.

# Example: Reading a configuration file
config_file_path = "app_config.json"

try:
    # Open the config file for reading
    with open(config_file_path, 'r') as f:
        content = f.read()
        # Print the first 100 characters of the file for preview
        print(f"Content of {config_file_path}:\n {content[:100]}...")
        # SRE/DevOps action: You'd typically parse this JSON content here
except FileNotFoundError:
    # Handle the case where the config file does not exist
    print(f"Error: The file {config_file_path} does not exist.")
except Exception as e:
    # Handle any other errors that may occur
    print(f"An error occurred while reading the file: {e}")
    
    
# Example: Writing to a new configuration or appending to a log
new_config_path = "new_app_settings.ini"
log_report_path = "deployment_audit.log"

# Write a new config (overwrites if exists)
with open(new_config_path, 'w') as f:
    # Write database configuration settings
    f.write("[database]\n")
    f.write("host=localhost\n")
    f.write("port=5432\n")
    print(f"New configuration written to {new_config_path}")
    
# Append to a deployment log
from datetime import datetime
# Get the current timestamp for the log entry
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_report_path, 'a') as f:
    # Append a deployment success message with timestamp
    f.write(f"{timestamp} - Deployment successful.\n")
print(f"Appended entry at {log_report_path}")