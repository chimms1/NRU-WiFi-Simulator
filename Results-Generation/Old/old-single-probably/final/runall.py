import os

times = 2

def get_level_one_directory_paths(root_path):
    directory_paths = []
    for directory in os.listdir(root_path):
        directory_path = os.path.join(root_path, directory)
        if os.path.isdir(directory_path):
            directory_paths.append(directory_path)
    return directory_paths

root_folder = os.path.dirname(os.path.abspath(__file__))
level_one_directory_paths = get_level_one_directory_paths(root_folder)

codepaths = []

if os.name == "posix":
    sep = "/"
else:
    sep = "\\"

for directory_path in level_one_directory_paths:
    # print(directory_path)
    filepath1 = directory_path+str(sep)+"run500.py"+" "+str(times)
    codepath1 = "python "+filepath1

    if "21" in directory_path:
        file2 = "compute21.py"+" "+str(times)
    else:
        file2 = "compute7.py"+" "+str(times)

    filepath2 = directory_path+str(sep)+file2
    codepath2 = "python "+filepath2

    print(codepath1)
    print(codepath2)
    codepaths.append(codepath1)
    codepaths.append(codepath2)


# run sequentially
for i in codepaths:
    print(i)

print("======================")
for i in codepaths:
    print(i)
    os.system(i)
