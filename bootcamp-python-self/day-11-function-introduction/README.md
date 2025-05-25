# Python Fundamentals for SRE/DevOps - Day 11: Introduction to Functions

This README summarizes our introduction to **Functions** in Python, a critical concept for writing organized, reusable, and maintainable code, which is invaluable in SRE and DevOps.

## Key Concepts Covered:

* **What are Functions?**
    * Reusable blocks of code that perform specific tasks.
    * Defined using the `def` keyword, followed by a name, parentheses `()`, and a colon `:`.
    * Code inside the function must be indented.
    * Functions do not execute until they are **called** (invoked by their name).
* **Functions with Arguments (Parameters):**
    * **Arguments** are values passed into a function, allowing it to operate on different inputs (e.g., `def greet_name(name):`).
    * Multiple arguments can be passed, separated by commas (e.g., `def check_server(name, status):`).
* **Functions with Return Values:**
    * The `return` keyword sends data back from the function to the caller.
    * If no `return` statement is present, a function implicitly returns `None`.
    * Functions can return multiple values, which Python automatically bundles into a **tuple** (e.g., `return value1, value2`). These can be "unpacked" by the caller.

## Why This is Important for SRE/DevOps:

Functions are essential for:

* **Code Reusability (DRY Principle):** Avoid repeating the same logic. Write a function once and call it whenever needed (e.g., a function to check a server's status, parse a log line, or make an API call).
* **Modularity and Organization:** Break down complex scripts into smaller, more manageable, and understandable units.
* **Debugging and Testing:** Isolated functions are easier to test and debug than monolithic blocks of code.
* **Collaboration:** Clear functions make it easier for team members to understand and contribute to your codebase.

---