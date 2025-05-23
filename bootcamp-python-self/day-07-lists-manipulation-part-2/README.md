# Python Fundamentals for SRE/DevOps - Day 7: List Manipulation (Part 2) and First Task

This README summarizes the final list manipulation techniques covered in Day 7 and introduces the first coding task focused on applying string and list manipulation skills, particularly relevant for basic log parsing in SRE and DevOps.

## Key Concepts Covered:

* **More List Methods:**
    * `.sort()`: Sorts the list in ascending order (in-place modification).
    * `sorted(list)`: Returns a new sorted list (original list remains unchanged).
    * `.reverse()`: Reverses the order of elements in the list (in-place modification).
    * `.count(value)`: Returns the number of occurrences of a specified `value` in the list.
* **Clearing a List:**
    * `.clear()`: Removes all elements from the list, making it empty.

## First Task: Simple Log Parser (with Optional Challenge)

The first task involved parsing a simplified log line string.

**Basic Task:**

* Split the log line into key-value pairs based on commas and equals signs.
* Store the data as a list of lists: `[['key', 'value'], ...]`.

**Challenge Task:**

* In addition to the basic parsing, filter the resulting list to only include key-value pairs where the **key** starts with the letter "t" (case-insensitive).

## Why This is Important for SRE/DevOps:

This task directly relates to common SRE/DevOps activities such as:

* **Log Analysis:** Extracting structured information from unstructured log data.
* **Data Extraction:** Processing text-based data to retrieve specific values.
* **Basic Data Filtering:** Selecting relevant information based on certain criteria.

This exercise reinforces the use of string methods (`split()`, `lower()`, `startswith()`) and list manipulation (creating lists, appending elements, iterating, and potentially creating new filtered lists).