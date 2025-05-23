# Demonstrating how to iterate through a dictionary in various ways

server_status = {
    "web_01": "running",
    "db_01": "stopped",
    "app_01": "restarting"
}

print("--- Server Names (Keys) ---")
# Iterate through dictionary keys using .keys()
for server_name in server_status.keys():
    print(server_name)

# Alternative: iterate directly through the dictionary (also gives keys)
for server_name in server_status:
    print(server_name)

print("\n--- Server Status (Values) ---")
# Iterate through dictionary values using .values()
for status in server_status.values():
    print(status)

print("\n--- Server Name and Status (Key-Value Pairs) ---")
# Iterate through key-value pairs using .items()
for server_name, status in server_status.items():
    print(f"{server_name}: {status}")


print("\n--- Separate line ---") 
# Demonstrating how to remove items from a dictionary

config_settings = {
    "port": 8080,
    "timeout": 30,
    "log_level": "INFO"
}

# Uncomment to update an existing key
# config_settings["log_level"] = "DEBUG"  # Update existing key
# print(f"Updated log level: {config_settings['log_level']}")  # Output: DEBUG

# Remove the "log_level" key from the dictionary
del config_settings["log_level"]
print(f"after deleting log_level: {config_settings}")  # Output: {'port': 8080, 'timeout': 30}

# Remove and return the value for the "port" key
removed_port = config_settings.pop("port")
print(f"After removing port: {config_settings}")  # Output: {'timeout': 30}
print(f"Removed port: {removed_port}")  # Output: 8080

# Remove and return the last inserted key-value pair as a tuple
last_item = config_settings.popitem()
print(f"After popping last item: {config_settings}")  # Output: {}
print(f"Removed last item: {last_item}")  # Output: ('timeout', 30)