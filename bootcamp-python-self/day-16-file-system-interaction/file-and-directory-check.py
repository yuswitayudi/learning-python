# file-and-directory-check.py
# Demonstrates how to check for the existence of directories and files before performing file system operations in Python.

import os

# Set the log directory path
log_directory = "/var/log/my_app"
# Check if the log directory exists before attempting to write logs
if not os.path.exists(log_directory):
    print(f"Creating log directory: {log_directory}")
    os.makedirs(log_directory, exist_ok=True)  # Create directory if it doesn't exist
    print("Directory creation skipped for example purposes.")  # Example message
else:
    print(f"Log directory '{log_directory}' already exists.")
    

# Set the deployment script path
script_path = "deploy_script.sh"
# Check if a deployment script exists before attempting to execute
if os.path.isfile(script_path):
    print(f"Deployment script '{script_path}' found. Ready to execute.")
else:
    print(f"Error: Deployment script '{script_path}' does not exist. Please check the path.")
