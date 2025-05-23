# Sample log line string
log_line = "timestamp=2025-05-16T08:15:00,level=ERROR,message=File not found"

# Split the log line into a list of individual "key=value" pairs.
# The delimiter used for splitting is the comma ",".
# Example: ["timestamp=2025-05-16T08:15:00", "level=ERROR", "message=File not found"]
split_log = log_line.split(",")

# Further process each "key=value" pair.
# This uses a list comprehension to iterate through each 'item' in 'split_log'.
# For each 'item' (e.g., "timestamp=2025-05-16T08:15:00"), it splits it by the equals sign "=".
# The result is a list of lists, where each inner list is [key, value].
# Example: [['timestamp', '2025-05-16T08:15:00'], ['level', 'ERROR'], ['message', 'File not found']]
split_log = [item.split("=") for item in split_log]
print(split_log) # Display the processed list of key-value pairs


# Define another sample log line string, this time with an additional 'user' field.
another_log_line = "timestamp=2025-05-16T08:15:00,level=ERROR,message=File not found,user=system"

# First, split the string into a list of "key=value" pairs using the comma as a delimiter.
# Example: ["timestamp=2025-05-16T08:15:00", "level=ERROR", "message=File not found", "user=system"]
another_log_line = another_log_line.split(",")

# Further split each "key=value" pair into a [key, value] list.
# This list comprehension iterates through the new 'another_log_line' list.
# Each string (e.g., "user=system") is split by "=" into a two-element list (e.g., ['user', 'system']).
# Example: [['timestamp', '2025-05-16T08:15:00'], ['level', 'ERROR'], ['message', 'File not found'], ['user', 'system']]
another_log_line = [item.split("=") for item in another_log_line]
print(another_log_line) # Display this second processed list of key-value pairs

# Filter the 'another_log_line' list.
# This list comprehension creates a new list called 'filtered_log'.
# It iterates through each 'item' (which is a [key, value] list) in 'another_log_line'.
# The 'if' condition checks if the first element of the item (item[0], which is the key),
# when converted to lowercase (item[0].lower()), starts with the letter "t" (startswith("t")).
# If the condition is true, the original 'item' (the [key, value] list) is included in 'filtered_log'.
filtered_log = [item for item in another_log_line if item[0].lower().startswith("t")]
print(filtered_log) # Display the filtered list, which should only contain items where the key starts with "t".
