# Demonstrates function scope, global/local variables, best practices, and default arguments in Python

# Global variable (accessible throughout the module)
global_message = "I am a global message."

def my_function():
    # Local variable (only accessible within this function)
    local_variable = "I am a local to my_function."
    print(f"Inside function: {local_variable}")
    print(f"Inside function, accessing global: {global_message}")

def another_function():
    # Local variable with the same name as in my_function, but scoped to this function
    local_variable = "I am local to another_function."
    print(f"Inside another_function: {local_variable}")

# Call functions to demonstrate local and global variable access
my_function()  # Call the first function
another_function()  # Call the second function

# Uncommenting the next line would raise an error because local_variable is not defined in this scope
# print(local_variable)
print(f"Outside functions, accessing global: {global_message}")

# Demonstrate modifying a global variable (not recommended in most cases)
# If you need to modify a global variable, use the 'global' keyword
global_counter = 0

def increment_counter():
    global global_counter  # Declare that we are using the global variable
    global_counter += 1
    print(f"Counter incremented to: {global_counter}")

# Call the function to increment the global counter
increment_counter()
increment_counter()
print(f"Outside function, final counter value: {global_counter}")

# Function best practices: use docstrings and handle edge cases
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Args:
        numbers (list): A list of numeric values.
    Returns:
        float: The average of the numbers in the list, or 0.0 if the list is empty.
    """
    if not numbers:
        return 0.0 # Handle empty list case
    return sum(numbers) / len(numbers)

# Print the docstring and demonstrate the function
print(calculate_average.__doc__)
print(f"Average: {calculate_average([10, 20, 30])}")

# Demonstrate default arguments in functions
def send_notification(message, recipient="admin", level="INFO"):
    """
    Sends a notification message to a recipient with a specified level.
    Args:
        message (str): The notification message.
        recipient (str, optional): The recipient of the notification. Defaults to 'admin'.
        level (str, optional): The level of the notification. Defaults to 'INFO'.
    """
    print(f"Sending {level} notification to {recipient}: {message}")

# Call send_notification with and without default arguments
send_notification("System reboot initiated.") # Uses default recipient and level
send_notification("High CPU usage!", recipient="devops_team", level="WARNING")