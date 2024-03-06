import os
filename = "task1.py"

print(os.access(filename, os.F_OK)) #existence
print(os.access(filename, os.R_OK)) #readable
print(os.access(filename, os.W_OK)) #writable
print(os.access(filename, os.X_OK)) #executable
