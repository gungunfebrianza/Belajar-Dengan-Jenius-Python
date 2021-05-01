import os

cmd = "notepad"
os.system(cmd)

# MAKE DIRECTORY
parent_directory = "D:\\"
directory = "pintercoding"
path = os.path.join(parent_directory,directory)

os.mkdir(path)
print("Directory '% s' created" % directory)