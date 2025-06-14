# while-loop.py
# Demonstrates basic while loop usage and a practical example of polling for server status.

# Example 1: simple counter
count = 0
while count < 3:
    # Print the current count value
    print(f"Current count: {count}")
    count += 1  # Increment the counter by 1
print("Loop finished!")

# Example 2: Simulating waiting for server status
import time
server_running = False  # Initial server status (not running)
attempts = 0  # Number of attempts made to start the server

print("\nAttempting to start the server...")
while not server_running and attempts < 2:
    # Print the current attempt and status
    print(f"  Attempt {attempts + 1}: Server is not ready yet.")
    time.sleep(1)  # Simulate waiting for 1 second
    attempts += 1
    # In real scenarios, you would check the server status here
    if attempts == 1:
        server_running = True  # Simulate the server becoming ready after the first attempt
        
# After the loop, check if the server is running or failed to start
if server_running:
    print("Server is now running!")
else:
    print("Failed to start the server after multiple attempts.")
    

# break statement
# Example 3: Searching a list and stopped early
devices = ["router", "switch", "firewall", "server-01", "load-balancer"]
target_device = "firewall"

print(f"\nSearching for {target_device} in the devices list...")
for device in devices:
    print(f"Checking device: {device}")
    if device == target_device:
        print(f"Found {target_device}! Stopping the search.")
        break  # Exit the loop when the target device is found
print("Search completed.")


# Example 4: Password attempts with a while loop
correct_password = "securepass"
attempts_left = 3

print(f"\nEnter your password (you have 3 attempts):")
while attempts_left > 0:
    user_input = input(f"You have {attempts_left} attempts left. Enter password: ")
    if user_input == correct_password:
        print("Access granted!")
        break  # Exit the loop if the password is correct
    else:
        attempts_left -= 1
        print("Incorrect password. Try again.")
else:
    print("Too many failed attempts. Access denied.")

