import os

# Create some dummy files/dirs for listing
os.makedirs("deployment_artifacts", exist_ok=True)
with open("deployment_artifacts/service_v1.0.tar.gz", "w") as f: f.write("")
with open("deployment_artifacts/config.yaml", "w") as f: f.write("")
os.makedirs("deployment_artifacts/old_versions", exist_ok=True)

contents = os.listdir("deployment_artifacts")
print(f"\nContents of 'deployment_artifacts': {contents}")

# SRE/DevOps Action: Loop through contents to process specific files
for item in contents:
    full_path = os.path.join("deployment_artifacts", item) # Always use os.path.join
    if os.path.isfile(full_path):
        print(f"  Found file: {item}")
    elif os.path.isdir(full_path):
        print(f"  Found directory: {item}")