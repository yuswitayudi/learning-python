# Day 3: String Manipulation in Python

# Basic String Methods

text = "  Python for DevOps  "
print(f"Original text: '{text}'")

length = len(text)
print(f"Length: {length}")

lower_case = text.lower()
print(f"Lower case: '{lower_case}'")

upper_case = text.upper()
print(f"Upper case: '{upper_case}'")

stripped_text = text.strip()
print(f"Stripped text: '{stripped_text}'")

lstripped_text = text.lstrip()
print(f"Left stripped text: '{lstripped_text}'")

rstripped_text = text.rstrip()
print(f"Right stripped text: '{rstripped_text}'")

message = "error occurred"
find_error = message.find("error")
print(f"Index of 'error': {find_error}")

replace_error = message.replace("error", "warning")
print(f"Replaced 'error': '{replace_error}'")

print("-" * 20)

# More Useful Methods

log_line = "ERROR: File not found"
starts_with_error = log_line.startswith("ERROR")
print(f"Starts with 'ERROR': {starts_with_error}")

ends_with_found = log_line.endswith("found")
print(f"Ends with 'found': {ends_with_found}")

data = "server,cpu,memory"
parts = data.split(",")
print(f"Split by comma: {parts}")

ip_parts = ["192", "168", "1", "100"]
ip_address = ".".join(ip_parts)
print(f"Joined by dot: '{ip_address}'")

print("-" * 20)

# Finding and Counting Substrings (Covered later in Day 3)

log_data_count = "error: file not found, error: permission denied, error: connection refused"
substring_to_count = "error"
count = log_data_count.count(substring_to_count)
print(f"Count of '{substring_to_count}': {count}")

text_find_all = "This is a test string. This string has test in it."
substring_find = "test"
indices = []
start_index = 0
while True:
    index = text_find_all.find(substring_find, start_index)
    if index == -1:
        break
    indices.append(index)
    start_index = index + 1

print(f"Indices of '{substring_find}': {indices}")
print(f"Count of '{substring_find}' (via find): {len(indices)}")