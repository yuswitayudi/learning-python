# Python Fundamentals for SRE/DevOps - Day 17: File System Interaction (Part 2) - Managing Files and Directories (Approx. 20 Minutes)

**Focus:** Expanding on Day 16's file system interaction by learning how to delete, rename, move, and list files and directories programmatically, crucial for comprehensive SRE/DevOps automation.

On Day 16, we covered reading, writing, and checking for the existence of files and directories. Today, we'll move into more active management: modifying the file system by deleting, renaming, and moving items, as well as listing their contents. These operations are fundamental for automated cleanup, data organization, and deployment workflows.

---

**Concepts & Explanation (Estimate: 18-20 Minutes)**

1.  **Deleting Files (`os.remove()`) (4 minutes)**
    * The `os.remove()` function is used to delete a specific file.
    * **Caution:** Once a file is removed, it's typically gone! Always use checks (`os.path.exists()`) before deleting.
    * **SRE/DevOps Relevance:**
        * Cleaning up old log archives to free up disk space.
        * Removing temporary deployment files after a successful installation.
        * Deleting obsolete configuration backups to maintain a clean state.

2.  **Deleting Directories (`os.rmdir()` and `shutil.rmtree()`) (5 minutes)**
    * `os.rmdir(path)`: Deletes an **empty** directory. This will raise an `OSError` if the directory contains any files or subdirectories.
    * `shutil.rmtree(path)`: Deletes a directory **and all its contents recursively**. This is a powerful and potentially dangerous function; use with extreme care! You'll need to `import shutil` for this.
    * **SRE/DevOps Relevance:**
        * `os.rmdir()`: Removing empty deployment stage directories once all artifacts have been moved out.
        * `shutil.rmtree()`: Cleaning up entire temporary workspaces, old build directories, or previous application versions during a rollback or a comprehensive cleanup phase.

3.  **Moving/Renaming Files and Directories (`os.rename()` and `shutil.move()`) (5 minutes)**
    * `os.rename(src, dst)`: Renames a file or directory from `src` (source path) to `dst` (destination path). It can also move items *within the same filesystem*. This function will raise an `OSError` if `dst` already exists and is a file.
    * `shutil.move(src, dst)`: Moves a file or directory from `src` to `dst`. This is generally more robust than `os.rename()` as it can move items across different filesystems and handles overwriting (if `dst` is an existing directory, `src` moves *into* it).
    * **SRE/DevOps Relevance:**
        * Rotating log files (e.g., renaming `app.log` to `app.log.old` before a new log starts).
        * Staging new deployment artifacts into their final locations.
        * Organizing monitoring data into dated archives.

4.  **Listing Directory Contents (`os.listdir()`) (4 minutes)**
    * `os.listdir(path)`: Returns a list of all file and directory names (as strings) within the specified `path`. It does *not* include the special entries `.` (current directory) or `..` (parent directory).
    * **SRE/DevOps Relevance:**
        * Discovering all log files in a directory for automated processing or archival.
        * Finding specific deployment artifacts or checking for their presence.
        * Iterating through subdirectories for inventory, compliance checks, or cleanup operations.

