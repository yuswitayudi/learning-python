import os
import shutil
from datetime import datetime

# Create a dummy file
with open("app.log", "w") as f:
    f.write("Initial log entries.")

# Rename/Move a file
old_log = "app.log"
new_log_archive = f"app.log.{datetime.now():%Y%m%d}.old"
if os.path.exists(old_log):
    os.rename(old_log, new_log_archive)
    print(f"SRE Action: Log file '{old_log}' renamed to '{new_log_archive}'.")

# Move a file to a different directory (if target exists, it moves INTO it)
os.makedirs("log_archive", exist_ok=True)
shutil.move(new_log_archive, "log_archive/")
print(f"SRE Action: Log archive moved into 'log_archive' directory.")