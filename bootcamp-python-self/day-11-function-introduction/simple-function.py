# simple-function.py
# Demonstrates basic Python function concepts: defining, calling, arguments, return values, and multiple return values.

# Define a function to greet a user (no arguments, no return value)
def greet_user():
    print("Hello, Python learner!")
    print("Welcome to Day 11!")

# Call the greet_user function twice to show repeated execution
print("Function greet_user() Output:")
greet_user()
greet_user()  # Call the function again to see the output again

# Note: Functions must be called to execute their code

# Define a function that takes a 'name' as an argument and prints a personalized greeting
def greet_name(name):
    print(f"Hello, {name}!")
    print("Glad to have you learning Python!")
    
# Call the greet_name function with different arguments
print("Function greet_name(name) Output:")
greet_name("Matei")
greet_name("Bob")

# Define a function with multiple arguments to check server health
def check_server_health(server_name, status):
    if status == "running":
        print(f"Server {server_name} is Up and running!")
    else:
        print(f"Server {server_name} is {status}. Please investigate!")

# Call the check_server_health function with different server statuses
print("Function check_server_health(server_name, status) Output:")
check_server_health("web-01", "running")
check_server_health("db-01", "stopped")

# Define a function that returns a value (sum of two numbers)
def add_numbers(num1, num2):
    result = num1 + num2
    return result # Send the 'result' back to the caller

# Call add_numbers and store the returned value
print("Function add_numbers(num1, num2) Output:")
sum_value = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {sum_value}")  # Output: The sum of 5 and 10 is: 15

# You can also use the return value directly in a print statement
print(f"The sum of 20 and 30 is: {add_numbers(20, 30)}")  # Output: The sum of 20 and 30 is: 50

# Define a function that returns multiple values (as a tuple)
def get_server_stats(cpu, mem):
    average_load = (cpu + mem) / 2
    if average_load < 75:
        return average_load, "Not OK"
    else:
        return average_load, "OK"

# Call get_server_stats and unpack the returned tuple
load, status = get_server_stats(7, 80)
print(f"Server load: {load}, Status: {status}")  # Output: Server load: 75.0, Status: OK