# Import the 're' module, which provides support for regular expressions.
import re

# Example 1: Searching for a simple string pattern.
# Define a sample log line string.
log_line = "Warning: High CPU usage on server-alpha-01"
# Define a raw string pattern to search for the literal string "CPU".
pattern = r"CPU"
# Use re.search() to find the first occurrence of the pattern in the log_line.
# re.search() returns a match object if the pattern is found, otherwise None.
result = re.search(pattern, log_line)

# Check if a match was found.
if result:
    # If found, print the pattern and its starting position in the string.
    print(f"Found '{pattern}' at position: {result.start()}")
else:
    # If not found, print a message indicating that.
    print(f"'{pattern}' not found in the log line.")
    
# Example 2: Searching for digits using a special character sequence.
# Define another sample log line.
log_line2 = "Error code 503 occured at 12:00"
# Define a pattern to find one or more digits (\d+).
# \d matches any digit (0-9).
# + means "one or more" occurrences of the preceding character/group.
pattern_digits = r"\d+"
# Search for the digit pattern in the second log line.
result_digits = re.search(pattern_digits, log_line2)

# Check if any digits were found.
if result_digits:
    # If found, print the matched digits using result_digits.group().
    # .group() returns the string matched by the regex.
    print(f"Found some digits: {result_digits.group()}")
    
# Example 3: Using the dot (.) wildcard character.
# Define a sample sentence.
line = "The quick brown fox jumps over the lazy dog"
# Define a pattern "f.x", where "." matches any single character (except newline).
# This pattern will match "fox", "f_x", "f9x", etc.
pattern_fox = r"f.x"
# Search for the "f.x" pattern in the line.
result_fox = re.search(pattern_fox, line)

# Check if the pattern was found.
if result_fox:
    # If found, print the matched string.
    print(f"Found pattern 'f.x': {result_fox.group()}")

# Example 4: Using re.findall() to find all occurrences.
# Define a string with multiple email addresses.
text_with_emails = "Contact us at support@example.com or sales@example.net for more info."
# Define a pattern to match email addresses.
# This is a simplified email pattern for demonstration.
# It looks for sequences of word characters (\w+), followed by '@',
# then more word characters, a '.', and finally more word characters.
pattern_email = r"\w+@\w+\.\w+"
# Use re.findall() to find all non-overlapping matches of the email pattern.
# re.findall() returns a list of strings.
all_emails = re.findall(pattern_email, text_with_emails)

# Print the list of found email addresses.
print(f"Found email addresses: {all_emails}")