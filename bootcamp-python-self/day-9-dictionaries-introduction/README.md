# Python Fundamentals for SRE/DevOps - Day 9: Introduction to Dictionaries

This README summarizes our deep dive into **Dictionaries** in Python, a fundamental data structure for storing data as `key:value` pairs, which is incredibly useful for SRE and DevOps tasks.

## Key Concepts Covered:

* **What are Dictionaries?**
    * Unordered collections of items (in Python 3.7+, insertion order is preserved, but they are not indexed numerically).
    * Store data as `key:value` pairs.
    * **Keys** must be unique and immutable (e.g., strings, numbers, tuples).
    * **Values** can be any Python object (strings, numbers, lists, other dictionaries, etc.).
    * Defined using curly braces `{}`.
* **Creating Dictionaries:**
    * Creating empty dictionaries (`{}`).
    * Creating dictionaries with various key-value pairs.
* **Accessing Values:**
    * Using square bracket notation (`my_dict["key"]`). This will raise a `KeyError` if the key doesn't exist.
    * Using the `.get()` method (`my_dict.get("key")`). This returns `None` if the key doesn't exist (or a specified default value), allowing for safer access.
* **Adding and Modifying Values:**
    * Dictionaries are **mutable**.
    * Adding a new key-value pair: `my_dict["new_key"] = new_value`.
    * Modifying an existing value: `my_dict["existing_key"] = updated_value`.

## Day 9 Challenge Task: Basic Server Inventory

The task involved processing raw server information strings and structuring them into a nested dictionary format.

**Task Goal:**
* Transform a list of strings (e.g., `"server_name:web-01;ip_address:192.168.1.10;status:running"`)
* Into a dictionary where the `server_name` is the top-level key, and its value is another dictionary containing `ip_address` and `status`.

**This task reinforced:**
* String splitting (`.split()`).
* Creating and populating dictionaries.
* Working with nested data structures.

---