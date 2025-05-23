# List of raw server information strings, each containing server details separated by semicolons
raw_server_info = [
    "server_name:web-01;ip_address:192.168.1.10;status:running",
    "server_name:db-01;ip_address:192.168.1.20;status:stopped",
    "server_name:app-01;ip_address:192.168.1.30;status:running"
]

# Initialize an empty dictionary to store server inventory
server_inventory = {}

# # Iterate over each server info string in the list
# for server_info in raw_server_info:
#     # Split the string into individual details (server_name, ip_address, status)
#     server_details = server_info.split(";")
    
#     # Extract server_name, ip_address, and status from the details
#     server_name = server_details[0].split(":")[1]
#     ip_address = server_details[1].split(":")[1]
#     status = server_details[2].split(":")[1]
    
#     # Create a dictionary for each server and add it to the inventory
#     server_inventory[server_name] = {
#         "ip_address": ip_address,
#         "status": status
#     }

# Optional Level-Up: More Robust Parsing
server_inventory_robust = {}
for server_info in raw_server_info:
    server_details = server_info.split(";")
    
    current_server_data = {}
    server_name_key = "" # Temporary variable to hold the server_name for the main dict key

    for detail_string in server_details:
        # Split each detail string into its key and value.
        # .split(":", 1) ensures we only split on the *first* colon,
        # useful if values themselves could contain colons (e.g., a URL)
        key, value = detail_string.split(":", 1)

        if key == "server_name":
            server_name_key = value # Store this to use as the main key later
        else:
            current_server_data[key] = value # Add other key-value pairs to the inner dict
    
    # After processing all details for one server, add it to the main inventory
    server_inventory_robust[server_name_key] = current_server_data

print(server_inventory_robust) # Uncomment to test this version

# Print the final server inventory dictionary
# print(server_inventory)