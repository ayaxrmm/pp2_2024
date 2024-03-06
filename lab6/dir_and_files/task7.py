def copy_file(source_path, destination_path):
    if os.path.exists(source_path):
        with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
            destination_file.write(source_file.read())
        print(f"File '{source_path}' successfully copied to '{destination_path}'.")
    else:
        print(f"Source file '{source_path}' not found.")

import os
source_file_path = r"C:\Users\user\Desktop\pp2_2024\lab6\dir_and_files\task6"
destination_file_path = r"C:\Users\user\Desktop\pp2_2024\lab6\dir_and_files\B.txt"
copy_file(source_file_path, destination_file_path)