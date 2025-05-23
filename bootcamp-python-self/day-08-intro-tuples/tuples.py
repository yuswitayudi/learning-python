#creating tuples
empy_tuple = ()  # An empty tuple
single_item_tuple = (1,)  # A tuple with a single item. Note the trailing comma!
number_tuple = (1, 2, 3, 4, 5)  # A tuple containing only numbers
string_tuple = ("alpha", "beta", "gamma")  # A tuple containing only strings
mixed_tuple = (1, "Hello", 3.14, True)  # A tuple with mixed data types
nested_tuple = ((1, 2), (3, 4), (5, 6))  # A tuple containing other tuples (nested)

# printing tuples above
# This section demonstrates how the created tuples are displayed when printed.
print("Empty Tuple:", empy_tuple)
print("Single Item Tuple:", single_item_tuple)
print("Number Tuple:", number_tuple)
print("String Tuple:", string_tuple)
print("Mixed Tuple:", mixed_tuple)
print("Nested Tuple:", nested_tuple)
print("-" * 20) # Separator for better readability

# accessing tuple elements
servers = ("web_01", "db_01", "app_01")

# Accessing elements using zero-based indexing
print("First server:", servers[0])  # Output: web_01

# Accessing elements using negative indexing (from the end)
print("Last server:", servers[-1]) # Output: app_01

# Slicing tuples to get a sub-tuple
# This gets elements from index 1 up to (but not including) index 3
print("Sliced servers:", servers[1:3])  # Output: ('db_01', 'app_01')
print("-" * 20) # Separator

# immutability in actions
# Tuples are immutable, meaning their contents cannot be changed after creation.
status_codes = (200, 404, 500)
# Attempting to change an element will result in a TypeError.
# status_codes[0] = 300 # Uncommenting this line will raise a TypeError
print(status_codes)

# Tuples do not have methods like .append() or .remove() because they are immutable.
# status_codes.append(401) # Uncommenting this line will raise an AttributeError
# print(status_codes)