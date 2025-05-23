# Python String Manipulation for SRE/DevOps - Day 3 & Counting

This mini-README summarizes the string manipulation methods and techniques for counting substrings covered in **Day 3** of our bootcamp, relevant for SRE and DevOps tasks.

## Key Concepts Covered:

* **Basic String Methods:**
    * `len(string)`: Returns the length of the string.
    * `.lower()`: Converts the string to lowercase.
    * `.upper()`: Converts the string to uppercase.
    * `.strip()`: Removes leading and trailing whitespace.
    * `.lstrip()`: Removes leading whitespace.
    * `.rstrip()`: Removes trailing whitespace.
    * `.find(substring)`: Returns the starting index of the first occurrence of a substring (-1 if not found).
    * `.replace(old, new)`: Returns a new string where all occurrences of `old` are replaced by `new`.
    * `.startswith(prefix)`: Checks if the string starts with a given prefix (returns `True` or `False`).
    * `.endswith(suffix)`: Checks if the string ends with a given suffix (returns `True` or `False`).
    * `.split(delimiter)`: Splits the string into a list of substrings based on the specified delimiter.
    * `.join(list_of_strings)`: Concatenates a list of strings into a single string with a specified separator.

* **Finding and Counting Substrings:**
    * **`.count(substring)`:** Returns the number of non-overlapping occurrences of a substring. This is the most direct way for counting.
    * **Looping with `.find()` (or `.index()`):** Used to find the starting indices of all occurrences of a substring, allowing for a count based on the number of times the substring is found.

## Why This is Important for SRE/DevOps:

These string manipulation techniques are essential for:

* **Log Parsing:** Extracting specific information or counting events in log files.
* **Data Transformation:** Cleaning, formatting, and restructuring text-based data.
* **Configuration File Processing:** Reading and modifying text-based configuration files.
* **API Response Handling:** Extracting relevant data from text-based API responses.
* **Building Automation Scripts:** Creating logic based on the content of strings (e.g., checking for specific error messages).

