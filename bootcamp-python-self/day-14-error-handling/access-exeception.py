# SRE/DevOps Example: Handling a file not found error during log analysis
def read_application_log(log_filepath):
    try:
        with open(log_filepath, 'r') as f:
            content = f.read()
        print(f"Successfully read log file: {log_filepath}")
        # Further SRE Action: Process content for error/metrics.
    except FileNotFoundError as e:
        print(f"SRE Alert: Log file not found: '{log_filepath}'. Details: {e}")
        # SRE action: Send alert, check deployment path, notify on-call.
    except PermissionError as e:
        print(f"SRE Alert: Permission denied to read: '{log_filepath}'. Details: {e}")
        # SRE action: Send alert, check script's execution user permissions.
    except Exception as e:
        print(f"An unexpected error occurred while reading log file: {e}")
        # SRE action: Log full traceback, alert on-call team for investigation.

print("\n--- SRE/DevOps Example: Reading Application Log ---")
read_application_log('application.log')  # Assuming this file exists