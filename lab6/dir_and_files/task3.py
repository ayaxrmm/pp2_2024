import os
path = r"C:\Users\user\Desktop\pp2_2024\lab6\dir_and_files"
def analyze_path(path):
    if (os.access(path, os.F_OK)) == True:
        dir, filename = os.path.split(path)
        print("given path: ", path)
        print("directory: ", dir)
        print("filename: ", filename)
    else:
        print("The path doesn't exist")


analyze_path(path)