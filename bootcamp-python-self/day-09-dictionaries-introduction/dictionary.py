# creating dictionaries
emtpy_dict = {}  # An empty dictionary
server_tags = {
    "web_01": "frontend",
    "db_01": "backend",
    "app_01": "microservice"
}

print(server_tags) # Output: {'web_01': 'frontend', 'db_01': 'backend', 'app_01': 'microservice'}

#accessing dictionary values
config = {"port": 8080, "timeout": 30}
print(config["port"])  # Standard access (raises KeyError if key DNE) -> Output: 8080
print(config.get("timeout")) # Safer: returns None if key DNE -> Output: 30
print(config.get("max_connections", 100)) # Safer: returns default if key DNE -> Output: 100 (since "max_connections" doesn't exist)

# adding new key-value pairs
metrics = {"cpu_util": 75, "mem_util": 60}
metrics["disk_util"] = 90 # Adds a new key-value pair
metrics["cpu_util"] = 80  # Overwrites existing key "cpu_util"
print(metrics) # Output: {'cpu_util': 80, 'mem_util': 60, 'disk_util': 90}