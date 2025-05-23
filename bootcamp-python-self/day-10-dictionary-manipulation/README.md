# Python Fundamentals for SRE/DevOps - Day 10: Dictionary Manipulation (Part 2)

This README covers advanced dictionary manipulation methods learned on Day 10, focusing on how to iterate through dictionary contents and remove elements. We also reviewed the Day 9 challenge task.

## Key Concepts Covered:

* **Iterating Through Dictionaries:**
    * `.keys()`: Returns a "view" object that displays a list of all the keys in the dictionary. Useful for iterating over keys.
    * `.values()`: Returns a "view" object that displays a list of all the values in the dictionary. Useful for iterating over values.
    * `.items()`: Returns a "view" object that displays a list of a dictionary's key-value tuple pairs. This is often the most common and useful for iterating over both keys and values simultaneously (e.g., `for key, value in my_dict.items():`).
* **Removing Elements from Dictionaries:**
    * `del my_dict[key]`: Deletes the item with the specified `key`. Raises `KeyError` if the key does not exist.
    * `my_dict.pop(key)`: Removes the item with the specified `key` and returns its `value`. Raises `KeyError` if the key does not exist.
    * `my_dict.popitem()`: Removes and returns an arbitrary (usually the last inserted) key-value pair as a tuple `(key, value)`. Raises `KeyError` if the dictionary is empty.

## Day 9 Task Review: Server Inventory

We reviewed the solution for the "Basic Server Inventory" task from Day 9. The task involved:
* Parsing raw string data (e.g., `"server_name:web-01;ip_address:192.168.1.10;status:running"`).
* Transforming it into a structured nested dictionary, where the `server_name` served as the primary key.

The review highlighted the effective use of string splitting (`.split()`) and dictionary manipulation, and offered a suggestion for a more robust parsing approach to handle varying field orders.

---