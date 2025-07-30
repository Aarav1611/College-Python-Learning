import os

# Get the current working directory
directory = os.getcwd()

# List all files and folders in the directory
contents = os.listdir(directory)

print(f"Contents of directory '{directory}':")
for item in contents:
    print(item)
