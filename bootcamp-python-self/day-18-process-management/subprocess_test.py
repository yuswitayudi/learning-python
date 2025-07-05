import subprocess  # Import the subprocess module to run system commands


# Running a simple command to list files in the current directory
print('Running "ls -l" to list files in the current directory:')
# Run the 'ls -l' command, capture output, and raise an error if the command fails
result = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)
# Print the standard output from the command
print("Stdout: ", result.stdout)
# Print the standard error from the command (should be empty if no error)
print("Stderr: ", result.stderr)
# Print the return code (0 means success)
print("Return code: ", result.returncode)



# Example: error handling when running a command that will fail

print("\n--- Running a command that will fail (SRE troubleshooting example) ---")
# Uncomment the following lines to see error handling in action for a non-existent command
# try:
#     subprocess.run(['non_existent_command'], capture_output=True, text=True, check=True)  # This will raise CalledProcessError
# except subprocess.CalledProcessError as e:
#     print("Error occurred:")
#     print("Stdout: ", e.stdout)  # Output from the command (if any)
#     print("Stderr: ", e.stderr)  # Error output from the command
#     print("Return code: ", e.returncode)  # Non-zero return code indicates failure

# Example: check nginx service status using systemctl
try:
    # Run 'systemctl is-active nginx' to check if nginx service is active
    subprocess.run(['systemctl', 'is-active', 'nginx'], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    # If nginx is not active or not found, print a message
    print("Nginx service is not active or not found.")