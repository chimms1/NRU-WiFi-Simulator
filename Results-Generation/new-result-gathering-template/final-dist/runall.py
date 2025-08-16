import os
import subprocess

times = 2

def get_level_one_directory_paths(root_path):
    directory_paths = []
    for directory in os.listdir(root_path):
        directory_path = os.path.join(root_path, directory)
        if os.path.isdir(directory_path):
            directory_paths.append(directory_path)
    return directory_paths

# Use a fallback if __file__ doesn't exist
try:
    root_folder = os.path.dirname(os.path.abspath(__file__))
except NameError:
    root_folder = os.getcwd()

level_one_directory_paths = get_level_one_directory_paths(root_folder)

codepaths = []

for directory_path in level_one_directory_paths:
    # Construct file paths using os.path.join for robustness
    filepath1 = os.path.join(directory_path, "run500.py") + " " + str(times)
    codepath1 = f"python \"{filepath1}\""

    if "21" in directory_path:
        file2 = "compute21.py" + " " + str(times)
    else:
        file2 = "compute7.py" + " " + str(times)

    filepath2 = os.path.join(directory_path, file2)
    codepath2 = f"python \"{filepath2}\""

    # Append command paths to the list
    codepaths.append(codepath1)
    codepaths.append(codepath2)


# Run sequentially using subprocess.run() for better control
for command in codepaths:
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing {command}")

print("======================")

# Optionally, run again if needed
for command in codepaths:
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error executing {command}")
