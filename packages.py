import os
import shutil
print(os.getcwd())
total, used, free = shutil.disk_usage("/")
print(f"Total disk space is: {total // (2**30)} GB")
print(f"used dsk space is: {used // (2**30)} GB")
print(f"free disk space is:{free // (2**30)} GB")
