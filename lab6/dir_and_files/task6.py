import os

#path = "./task6/"
path = r"C:\Users\user\Desktop\pp2_2024\lab6\dir_and_files\task6"
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    with open(os.path.join(path, f"{letter}.txt"), "w") as file:
        file.write("this is a task6 from lab6")

