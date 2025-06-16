# try-finally.py
# Demonstrates robust error handling and resource cleanup using try-finally in Python.
# This script simulates deploying an artifact and ensures logs are handled safely.

import os
import shutil  # Import the shutil module for file operations

# Directory where deployment logs will be persisted
PERSISTENT_LOG_DIR = "/tmp/app_deployments/"  # Example persistent log directory

def deploy_artifact(artifact_path):
    """
    Deploys an artifact and logs the process.
    - Writes deployment logs to a temporary file.
    - Handles errors such as missing artifact or unexpected exceptions.
    - Ensures the log file is always closed and copied to a persistent location.
    - Cleans up temporary files after use.

    Args:
        artifact_path (str): Path to the artifact to deploy.
    """
    temp_log_file = None  # initialize to None for safety
    try:
        print(f"Attempting to deploy {artifact_path}...")
        temp_log_file = open("/tmp/deploy_log.txt", "w")  # Open a temporary log file
        temp_log_file.write(f"Starting deployment for {artifact_path}\n")
        
        # Simulate deployment step that might fail
        if not os.path.exists(artifact_path):
            raise FileNotFoundError(f"Artifact {artifact_path} does not exist.")
        
        # Simulate successful deployment
        temp_log_file.write(f"Successfully deployed {artifact_path}\n")
        print(f"Deployment of {artifact_path} completed successfully!")
    
    except FileNotFoundError as e:
        print(f"Deployment failed: {e}")
        if temp_log_file:
            temp_log_file.write(f"Deployment failed: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred during deployment: {e}")
        if temp_log_file:
            temp_log_file.write(f"Unexpected error: {e}\n")
    finally:
        # This block always runs, even if an error occurred
        if temp_log_file:
            temp_log_file.close()
            print("Temporary log file closed.")
            # SRE/DevOps Action: For production, you might copy this log
            # to a persistent location before deleting.
            if not os.path.exists(PERSISTENT_LOG_DIR):
                os.makedirs(PERSISTENT_LOG_DIR, exist_ok=True)  # Create persistent dir if not exists
            
            persistent_log_path = os.path.join(PERSISTENT_LOG_DIR, "deploy_log.txt")
            try:
                shutil.copy("/tmp/deploy_log.txt", persistent_log_path)
                print(f"Log file copied to {persistent_log_path}")
            except Exception as e:
                print(f"Failed to copy log file to persistent storage: {e}")
            
            os.remove("/tmp/deploy_log.txt")  # Clean up the temporary log file
            print("Temporary log file removed.")
        print("Deployment function finished")

# Example calls
# The first call simulates a failed deployment (artifact does not exist)
deploy_artifact("artifact.zip")  # Assuming this file does not exist
# The second call should be updated with a valid path to test successful deployment
deploy_artifact("/path/to/valid/artifact.zip")  # Replace with a valid path to test successful deployment