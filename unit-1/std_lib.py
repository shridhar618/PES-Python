import os
print("The current workimng directory is ", os.getcwd())

new=("Directory")
os.mkdir(new)

os.rmdir("Directory")

if os.path.exists(new):
    print(f'Directory {new} is created successfully')
else:
    print("Error in creation")

os.chdir(new)
os.getcwd()

os.mkdir("dir1")
os.mkdir("dir2")

print("Parent id is:", os.getpid())
print("Parent id is:", os.getppid())

import platform

print(f"the host name is: {platform.node()}")

if "USERPROFILE" in os.environ:
    home=os.environ['USERPROFILE']
    print(f"Home directory is {home}")





