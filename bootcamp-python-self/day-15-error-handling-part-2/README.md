# Python Fundamentals for SRE/DevOps - Day 15: Error Handling (Part 2) - `else` and `finally` Blocks 

**Focus:** Completing the error handling toolkit by understanding how to execute code only upon success (`else`) and ensure cleanup regardless of outcome (`finally`), vital for dependable SRE/DevOps automation.

On Day 14, we covered `try` and `except` to catch and handle specific errors. Today, we'll add `else` and `finally` to create even more controlled and reliable execution flows, which is paramount when managing production systems.

---

**Concepts & Explanation (Estimate: 15-18 Minutes)**

1.  **The `else` Block (6 minutes)**
    * **Purpose:** The code inside the `else` block executes **only if no exception occurred** within the `try` block.
    * **When to use:** It's best for operations that should *only* proceed if the potentially risky code in `try` was successful. This keeps the `try` block lean, containing only the code that might raise an error.

    **SRE/DevOps Relevance:**
    * Confirming successful API calls before processing data.
    * Verifying file parsing before using its content.
    * Ensuring a system command ran without error before acting on its output. This block signifies a "happy path" after a guarded operation.

2.  **The `finally` Block (9 minutes)**
    * **Purpose:** The code inside the `finally` block **always executes**, regardless of whether an exception occurred in the `try` block or not, and even if a `return` or `break` statement is encountered.
    * **When to use:** It's ideal for **cleanup operations** that *must* happen, such as:
        * Closing open files or network connections.
        * Releasing locks or temporary resources.
        * Deleting temporary files created during an operation.
        * Ensuring database connections are terminated.

    **SRE/DevOps Relevance:**
    * **Guaranteed Resource Release:** This is critical to prevent resource leaks (e.g., open file handles, database connections, cloud sessions) even if an automation script fails midway.
    * **Ensuring State Consistency:** Used for reverting temporary changes or cleaning up after a failed deployment, ensuring the system returns to a known state. For example, always deleting a temporary artifact download even if the deployment failed.


