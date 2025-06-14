# continue.py
# Demonstrates the use of 'continue' in for loops to skip certain iterations based on conditions.

# Example 1: Processing only 'active' servers
server_list = [
    {"name": "web-01", "status": "active"},
    {"name": "db-01", "status": "maintenance"},
    {"name": "app-01", "status": "active"}
]

print("\nPerforming health checks on active servers:")
for server in server_list:
    # Skip servers that are not 'active'
    if server["status"] != "active":
        print(f"  Skipping {server['name']} (status: {server['status']}).")
        continue # Skip the rest of this iteration, go to the next server
    print(f"  Running health check on {server['name']}...")
    # ... rest of health check logic would go here
print("Health checks complete.")

# Example 2: Filtering log entries (skipping debug messages)
log_messages = [
    "INFO: System startup",
    "DEBUG: Temp var x=5",
    "WARNING: Low disk space",
    "DEBUG: Function call",
    "ERROR: Service down"
]
print("\nProcessing critical log messages (ignoring DEBUG):")
for msg in log_messages:
    # Skip log messages that start with 'DEBUG'
    if msg.startswith("DEBUG"):
        continue # Skip this log message, go to the next one
    print(f"  Processing: {msg}")