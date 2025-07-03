# deleting files

import os

with open('temp_old_log.txt', 'w') as f:
    f.write('This is a temporary log file.')

file_to_delete = 'temp_old_log.txt'

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"{file_to_delete} has been deleted.")
else:
    print(f"{file_to_delete} does not exist.")
    

# deleting directories
import shutil

# create dummy directory for demonstration
os.makedirs('empty_dir_to_delete', exist_ok=True)
os.makedirs("non_empty_dir_to_delete/subdir", exist_ok=True)

with open("non_empty_dir_to_delete/file.txt", 'w') as f:
    f.write("content")

# delete empty directory
if os.path.isdir("empty_dir_to_delete"):
    os.rmdir("empty_dir_to_delete")
    print("SRE Action: Empty directory removed")

# delete non-empty directory
dir_to_remove = "non_empty_dir_to_delete"
if os.path.isdir("non_empty_dir_to_delete"):
    print(f"Warning: about to remove '{dir_to_remove}' and all its contents.")
    shutil.rmtree(dir_to_remove)
    print("SRE Action: non-empty directory removed")