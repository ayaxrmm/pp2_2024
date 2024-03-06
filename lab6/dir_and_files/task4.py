def count_lines(path):
    if (os.access(path, os.F_OK)) == True:
        with open(path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The file '{path}' has {line_count} line(s).")
    else:
        print(f"File '{path}' not found.")

import os
path = r"C:\Users\user\Desktop\pp2_2024\lab6\builtin_functions"
count_lines(path)