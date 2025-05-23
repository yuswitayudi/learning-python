# List of raw server information strings, each containing server details separated by semicolons
raw_server_info = [
    "server_name:web-01;ip_address:192.168.1.10;status:running",
    "server_name:db-01;ip_address:192.168.1.20;status:stopped",
    "server_name:app-01;ip_address:192.168.1.30;status:running"
]

# Initialize an empty dictionary to store server inventory
server_inventory = {}

# Iterate over each server info string in the list
for server_info in raw_server_info:
    # Split the string into individual details (server_name, ip_address, status)
    server_details = server_info.split(";")
    
    # Extract server_name, ip_address, and status from the details
    server_name = server_details[0].split(":")[1]
    ip_address = server_details[1].split(":")[1]
    status = server_details[2].split(":")[1]
    
    # Create a dictionary for each server and add it to the inventory
    server_inventory[server_name] = {
        "ip_address": ip_address,
        "status": status
    }

# Print the final server inventory dictionary
print(server_inventory)